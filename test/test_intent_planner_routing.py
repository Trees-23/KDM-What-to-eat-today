from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace

from rag_modules.intent_candidate import IntentCandidate
from rag_modules.intent_plan_compiler import IntentPlanCompiler
from rag_modules.intent_planner import PlannerResult
from rag_modules.query_plan_validator import QueryPlanValidator
from rag_modules.retrieval_contracts import EvidenceBundle


class _Planner:
    def __init__(self, result): self.result = result; self.calls = []
    def plan(self, message, audit_run=None): self.calls.append(message); return self.result


class _Router:
    def __init__(self): self.calls = []
    def route_query(self, *args, **kwargs): self.calls.append((args, kwargs)); return ["legacy"], object()


class _Vector:
    def __init__(self): self.calls = []
    def retrieve(self, query, **kwargs): self.calls.append((query, kwargs)); return []


class _Audit:
    def __init__(self): self.events = []
    def record_event(self, stage, status="completed", **fields): self.events.append((stage, status, fields))


@dataclass
class _Config:
    retrieval_intent_planner_enabled: bool = True
    retrieval_new_path_allowlist: tuple[str, ...] = ()
    retrieval_new_path_traffic_percent: float = 100.0
    retrieval_legacy_fallback_enabled: bool = True
    top_k: int = 3


def _candidate():
    return IntentCandidate(intent="PREFERENCE_RECOMMEND", confidence=.9, slots={"preferences": ["LIGHT_FEEL"], "meal_context": [], "cuisines": [], "ingredients": [], "tools": [], "methods": [], "servings": None, "time_budget_minutes": None, "step_number": None, "nutrition_constraint": None})


def _system_type():
    import main
    return main.AdvancedGraphRAGSystem


def _system(result):
    system = _system_type().__new__(_system_type())
    system.config = _Config()
    system.intent_planner = _Planner(result)
    system.intent_plan_compiler = IntentPlanCompiler(QueryPlanValidator(), max_candidates=3)
    system.query_plan_validator = QueryPlanValidator()
    system.restricted_vector_retriever = _Vector()
    system.query_router = _Router()
    system._restricted_vector_init_status = None
    return system


def test_invalid_planner_output_fail_closed_without_legacy_or_retrieval():
    system = _system(PlannerResult("PLANNER_INVALID_OUTPUT", reason="JSONDecodeError"))
    bundle, analysis = system.retrieve_for_generation("清淡晚餐", 3, audit_run=_Audit())
    assert analysis is None and isinstance(bundle, EvidenceBundle)
    assert "PLANNER_INVALID_OUTPUT" in bundle.limitations
    assert system.query_router.calls == []
    assert system.restricted_vector_retriever.calls == []


def test_valid_preference_uses_restricted_vector_plan_and_never_legacy_router():
    system = _system(PlannerResult("VALID", candidate=_candidate()))
    bundle, _ = system.retrieve_for_generation("清淡晚餐", 3, audit_run=_Audit())
    assert bundle.query_plan["template_id"] == "preference_recommend_v1"
    assert system.restricted_vector_retriever.calls[0][1]["parent_ids"] is None
    assert system.query_router.calls == []


def test_unavailable_planner_is_not_legacy_fallback():
    system = _system(PlannerResult("PLANNER_UNAVAILABLE", reason="TimeoutError"))
    bundle, _ = system.retrieve_for_generation("清淡晚餐", 3)
    assert "PLANNER_UNAVAILABLE" in bundle.limitations
    assert system.query_router.calls == []


def test_strict_nutrition_uses_only_user_message_hard_gate_without_llm_or_retrieval():
    system = _system(PlannerResult("VALID", candidate=_candidate()))
    bundle, _ = system.retrieve_for_generation("每份脂肪不超过 5 克的晚餐", 3)
    assert "NUTRITION_EVIDENCE_INSUFFICIENT" in bundle.limitations
    assert system.intent_planner.calls == []
    assert system.restricted_vector_retriever.calls == []


def test_negative_low_fat_phrase_is_not_a_strict_nutrition_request():
    system = _system(PlannerResult("VALID", candidate=_candidate()))
    system.retrieve_for_generation("清淡晚餐，我不要求低脂", 3)
    assert system.intent_planner.calls == ["清淡晚餐，我不要求低脂"]
