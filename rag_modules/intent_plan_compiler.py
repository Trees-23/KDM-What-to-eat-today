"""把低权限 IntentCandidate 编译为唯一受控执行动作。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .intent_candidate import IntentCandidate
from .query_plan import QueryPlan
from .query_plan_validator import QueryPlanValidator


@dataclass(frozen=True)
class ClaimPolicy:
    hard_constraints: tuple[str, ...] = ()
    soft_preferences: tuple[str, ...] = ()
    display_requests: tuple[str, ...] = ()
    forbidden_claims: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, list[str]]:
        return {
            "hard_constraints": list(self.hard_constraints),
            "soft_preferences": list(self.soft_preferences),
            "display_requests": list(self.display_requests),
            "forbidden_claims": list(self.forbidden_claims),
        }


@dataclass(frozen=True)
class CompileResult:
    status: str
    action: str
    query_plan: QueryPlan | None = None
    claim_policy: ClaimPolicy = ClaimPolicy()
    reason: str | None = None
    limitations: tuple[str, ...] = ()

    @property
    def can_execute(self) -> bool:
        return self.status == "EXECUTE"

    @property
    def may_generate(self) -> bool:
        return self.can_execute


class IntentPlanCompiler:
    """所有执行字段均由此处从本地真实结果构造。"""

    _MIN_CONFIDENCE = 0.70
    _EXPECTED_TYPES = {
        "ENTITY_LOOKUP": ("Recipe", "Ingredient", "TechniqueDoc"),
        "RECIPE_DETAIL": ("Recipe",),
        "RECIPE_STEP": ("Recipe",),
        "TECHNIQUE_SECTION": ("TechniqueDoc",),
        "INGREDIENT_RECIPES": ("Ingredient",),
        "INGREDIENT_VEGETABLE_PAIRS": ("Ingredient",),
        "PREFERENCE_RECOMMEND": ("Ingredient",),
    }

    def __init__(self, validator: QueryPlanValidator | None = None, *, max_candidates: int = QueryPlanValidator.MAX_CANDIDATES):
        self.validator = validator or QueryPlanValidator()
        if not 1 <= max_candidates <= QueryPlanValidator.MAX_CANDIDATES:
            raise ValueError("max_candidates 超出范围")
        self.max_candidates = max_candidates

    def compile(
        self,
        candidate: IntentCandidate,
        *,
        resolved_entities: Sequence[Any] = (),
        scoped_recipe_ids: Sequence[str] | None = None,
        dependencies_available: bool = True,
    ) -> CompileResult:
        if not isinstance(candidate, IntentCandidate):
            return self._clarify("INTENT_CANDIDATE_INVALID")
        if candidate.confidence < self._MIN_CONFIDENCE:
            return self._clarify("LOW_CONFIDENCE")
        if candidate.intent == "CLARIFY_OR_OUT_OF_SCOPE":
            return self._clarify("CLARIFY_OR_OUT_OF_SCOPE")
        if not dependencies_available:
            return CompileResult("UNAVAILABLE", "DEPENDENCY_UNAVAILABLE", reason="DEPENDENCY_UNAVAILABLE")
        if candidate.intent == "STRICT_NUTRITION":
            return CompileResult(
                "TERMINAL",
                "NUTRITION_EVIDENCE_INSUFFICIENT",
                reason="NUTRITION_EVIDENCE_INSUFFICIENT",
                limitations=("NUTRITION_EVIDENCE_INSUFFICIENT", "当前没有受治理营养数据。"),
                claim_policy=ClaimPolicy(forbidden_claims=("低脂", "低热量", "医疗适用")),
            )
        if self._has_multiple_tasks(candidate):
            return self._clarify("MULTI_TASK")
        if candidate.intent == "PREFERENCE_RECOMMEND":
            return self._compile_preference(candidate, scoped_recipe_ids)
        return self._compile_entity(candidate, resolved_entities)

    def _compile_preference(self, candidate: IntentCandidate, scoped_recipe_ids: Sequence[str] | None) -> CompileResult:
        if scoped_recipe_ids is not None:
            ids = tuple(dict.fromkeys(str(item).strip() for item in scoped_recipe_ids if str(item).strip()))
            if not ids:
                return CompileResult("TERMINAL", "NO_PREFERENCE_RESULTS", reason="HARD_SCOPE_EMPTY")
            if len(ids) > self.max_candidates:
                return CompileResult("TERMINAL", "SCOPE_TOO_LARGE", reason="HARD_SCOPE_TOO_LARGE")
            parameters = {"scope": "candidate_parents", "parent_ids": list(ids), "limit": self.max_candidates}
            plan = self._plan("PREFERENCE_RECOMMEND", "Recipe", parameters)
            hard = ("validated_recipe_scope",)
        else:
            plan = self._plan(
                "PREFERENCE_RECOMMEND",
                "Recipe",
                {"scope": "all_child_chunks", "limit": self.max_candidates},
            )
            hard = ()
        policy = self._claim_policy(candidate, hard_constraints=hard)
        return CompileResult("EXECUTE", "PREFERENCE_RECOMMEND", plan, policy)

    def _compile_entity(self, candidate: IntentCandidate, resolved_entities: Sequence[Any]) -> CompileResult:
        expected = self._EXPECTED_TYPES.get(candidate.intent)
        if expected is None:
            return self._clarify("UNSUPPORTED_INTENT")
        candidates = tuple(resolved_entities)
        if not candidates:
            return CompileResult("TERMINAL", "ENTITY_NOT_FOUND", reason="ENTITY_NOT_FOUND", limitations=("ENTITY_NOT_FOUND",))
        if len(candidates) != 1 or bool(getattr(candidates[0], "ambiguity", False)):
            return self._clarify("ENTITY_AMBIGUOUS")
        entity = candidates[0]
        node_type = getattr(entity, "node_type", None)
        node_id = getattr(entity, "node_id", None)
        if node_type not in expected or not isinstance(node_id, str) or not node_id.strip():
            return self._clarify("ENTITY_TYPE_MISMATCH")
        if candidate.intent == "ENTITY_LOOKUP":
            return CompileResult(
                "TERMINAL",
                "ENTITY_LOOKUP_RESOLVED",
                reason="ENTITY_LOOKUP_RESOLVED",
                limitations=("ENTITY_LOOKUP_RESOLVED",),
            )
        if candidate.intent == "RECIPE_DETAIL":
            return CompileResult(
                "EXECUTE",
                "PDS_ENTITY_DETAIL",
                claim_policy=self._claim_policy(candidate, display_requests=("正文",)),
            )
        if candidate.intent == "RECIPE_STEP":
            plan = self._plan("RECIPE_STEP", "Recipe", {"recipe_id": node_id, "step_number": candidate.slots.step_number, "limit": 1}, max_candidates=1)
        elif candidate.intent == "INGREDIENT_RECIPES":
            plan = self._plan("INGREDIENT_RECIPES", "Ingredient", {"ingredient_id": node_id, "limit": self.max_candidates})
        elif candidate.intent == "INGREDIENT_VEGETABLE_PAIRS":
            plan = self._plan("INGREDIENT_VEGETABLE_PAIRS", "Ingredient", {"ingredient_id": node_id, "vegetable_category": "蔬菜", "limit": self.max_candidates})
        elif candidate.intent == "TECHNIQUE_SECTION":
            plan = self._plan("TECHNIQUE_CHUNKS", "TechniqueDoc", {"technique_doc_id": node_id, "limit": self.max_candidates})
        else:
            return self._clarify("UNSUPPORTED_INTENT")
        return CompileResult("EXECUTE", candidate.intent, plan, self._claim_policy(candidate, hard_constraints=("verified_graph_relation",)))

    def _plan(self, intent: str, entity_type: str, parameters: Mapping[str, Any], *, max_candidates: int | None = None) -> QueryPlan:
        from .query_plan import TEMPLATE_BY_INTENT

        maximum = max_candidates or self.max_candidates
        return self.validator.validate(QueryPlan(intent, TEMPLATE_BY_INTENT[intent], entity_type, parameters, maximum, source="rule"))

    @staticmethod
    def _has_multiple_tasks(candidate: IntentCandidate) -> bool:
        return candidate.intent == "PREFERENCE_RECOMMEND" and bool(candidate.entity_mentions) and candidate.slots.step_number is not None

    @staticmethod
    def _claim_policy(candidate: IntentCandidate, *, hard_constraints: Sequence[str] = (), display_requests: Sequence[str] = ()) -> ClaimPolicy:
        return ClaimPolicy(
            hard_constraints=tuple(hard_constraints),
            soft_preferences=tuple(candidate.slots.preferences) + tuple(candidate.slots.meal_context) + tuple(candidate.slots.tools) + tuple(candidate.slots.methods),
            display_requests=tuple(display_requests),
            forbidden_claims=("低脂", "低热量", "医疗适用"),
        )

    @staticmethod
    def _clarify(reason: str) -> CompileResult:
        return CompileResult("CLARIFY", "CLARIFY_OR_OUT_OF_SCOPE", reason=reason, limitations=(reason,))
