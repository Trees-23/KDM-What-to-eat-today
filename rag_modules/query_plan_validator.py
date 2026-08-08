"""QueryPlan 白名单校验与保守规则计划。"""

from __future__ import annotations

import json
import re
from typing import Any, Mapping

from .query_plan import ENTITY_TYPE_BY_INTENT, QUERY_PLAN_INTENTS, TEMPLATE_BY_INTENT, QueryPlan


class QueryPlanValidationError(ValueError):
    """计划未通过固定 schema 或参数白名单校验。"""


class QueryPlanValidator:
    MAX_CANDIDATES = 50
    _ALLOWED_FIELDS = frozenset(
        {"intent", "template_id", "entity_type", "parameters", "max_candidates", "source"}
    )
    _PARAMETERS = {
        "recipe_step_anchor_v1": frozenset({"recipe_id", "step_id", "step_number", "limit"}),
        "ingredient_recipes_v1": frozenset({"ingredient_id", "limit"}),
        "ingredient_vegetable_pairs_v1": frozenset({"ingredient_id", "vegetable_category", "limit"}),
        "technique_chunks_v1": frozenset({"technique_doc_id", "limit"}),
        "recipe_cuisine_filter_v1": frozenset({"recipe_ids", "cuisine_type", "limit"}),
    }
    _FORBIDDEN_KEYS = frozenset(
        {"cypher", "query", "label", "labels", "relationship", "relationships", "where", "filter"}
    )

    def validate(self, candidate: QueryPlan | Mapping[str, Any] | str) -> QueryPlan:
        if isinstance(candidate, str):
            try:
                candidate = json.loads(candidate)
            except json.JSONDecodeError as error:
                raise QueryPlanValidationError("QueryPlan JSON 非法") from error
        if isinstance(candidate, QueryPlan):
            raw = candidate.to_dict()
        elif isinstance(candidate, Mapping):
            raw = dict(candidate)
        else:
            raise QueryPlanValidationError("QueryPlan 必须是对象或 JSON 字符串")
        unknown_fields = set(raw) - self._ALLOWED_FIELDS
        if unknown_fields:
            raise QueryPlanValidationError(f"QueryPlan 含未知字段: {sorted(unknown_fields)}")
        intent = raw.get("intent")
        if intent not in QUERY_PLAN_INTENTS:
            raise QueryPlanValidationError(f"不支持的 intent: {intent}")
        template_id = raw.get("template_id")
        if template_id != TEMPLATE_BY_INTENT[intent]:
            raise QueryPlanValidationError("intent 与 template_id 不匹配")
        if raw.get("entity_type") != ENTITY_TYPE_BY_INTENT[intent]:
            raise QueryPlanValidationError("entity_type 与 intent 不匹配")
        source = raw.get("source", "rule")
        if source not in {"rule", "llm_candidate"}:
            raise QueryPlanValidationError("source 不在白名单中")
        max_candidates = raw.get("max_candidates", 20)
        if isinstance(max_candidates, bool) or not isinstance(max_candidates, int):
            raise QueryPlanValidationError("max_candidates 必须是整数")
        if not 1 <= max_candidates <= self.MAX_CANDIDATES:
            raise QueryPlanValidationError("max_candidates 超出范围")
        parameters = raw.get("parameters")
        if not isinstance(parameters, Mapping):
            raise QueryPlanValidationError("parameters 必须是对象")
        parameters = dict(parameters)
        forbidden = self._find_forbidden_keys(parameters)
        if forbidden:
            raise QueryPlanValidationError(f"parameters 含越权字段: {sorted(forbidden)}")
        unknown_parameters = set(parameters) - self._PARAMETERS[template_id]
        if unknown_parameters:
            raise QueryPlanValidationError(f"template 参数不在白名单中: {sorted(unknown_parameters)}")
        self._validate_parameters(template_id, parameters, max_candidates)
        return QueryPlan(intent, template_id, raw["entity_type"], parameters, max_candidates, source)

    def validate_or_conservative(
        self, candidate: QueryPlan | Mapping[str, Any] | str, *, query_text: str, entity_id: str | None = None
    ) -> QueryPlan | None:
        try:
            return self.validate(candidate)
        except (QueryPlanValidationError, ValueError, TypeError, json.JSONDecodeError):
            return self.conservative_plan(query_text, entity_id=entity_id)

    def conservative_plan(self, query_text: str, *, entity_id: str | None = None) -> QueryPlan | None:
        """只根据受控意图词生成计划；没有稳定实体 ID 时不猜测。"""
        text = str(query_text or "")
        if not entity_id:
            return None
        if "蔬菜" in text and "搭配" in text:
            return self.validate(
                QueryPlan(
                    "INGREDIENT_VEGETABLE_PAIRS",
                    TEMPLATE_BY_INTENT["INGREDIENT_VEGETABLE_PAIRS"],
                    "Ingredient",
                    {"ingredient_id": entity_id, "vegetable_category": "蔬菜", "limit": 20},
                )
            )
        if any(marker in text for marker in ("能做什么", "可以做什么", "适合做什么")):
            return self.validate(
                QueryPlan(
                    "INGREDIENT_RECIPES",
                    TEMPLATE_BY_INTENT["INGREDIENT_RECIPES"],
                    "Ingredient",
                    {"ingredient_id": entity_id, "limit": 20},
                )
            )
        if any(marker in text for marker in ("第一步", "第1步", "第 1 步")):
            match = re.search(r"第\s*(\d+)\s*步", text)
            step_number = int(match.group(1)) if match else 1
            return self.validate(
                QueryPlan(
                    "RECIPE_STEP",
                    TEMPLATE_BY_INTENT["RECIPE_STEP"],
                    "Recipe",
                    {"recipe_id": entity_id, "step_number": step_number, "limit": 1},
                    max_candidates=1,
                )
            )
        if any(marker in text for marker in ("关键要点", "适用场景", "技巧章节")):
            return self.validate(
                QueryPlan(
                    "TECHNIQUE_CHUNKS",
                    TEMPLATE_BY_INTENT["TECHNIQUE_CHUNKS"],
                    "TechniqueDoc",
                    {"technique_doc_id": entity_id, "limit": 20},
                )
            )
        return None

    @classmethod
    def _find_forbidden_keys(cls, value: Mapping[str, Any]) -> set[str]:
        keys = {str(key).lower() for key in value}
        return {key for key in keys if key in cls._FORBIDDEN_KEYS}

    @staticmethod
    def _required_id(parameters: Mapping[str, Any], key: str) -> str:
        value = parameters.get(key)
        if not isinstance(value, str) or not value.strip() or len(value) > 150:
            raise QueryPlanValidationError(f"{key} 必须是非空短字符串")
        return value.strip()

    def _validate_parameters(self, template_id: str, parameters: Mapping[str, Any], max_candidates: int) -> None:
        if "limit" in parameters:
            limit = parameters["limit"]
            if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= max_candidates:
                raise QueryPlanValidationError("limit 必须不超过 max_candidates")
        else:
            parameters["limit"] = max_candidates
        if template_id == "recipe_step_anchor_v1":
            parameters["recipe_id"] = self._required_id(parameters, "recipe_id")
            has_step_id = "step_id" in parameters and parameters["step_id"] is not None
            has_step_number = "step_number" in parameters and parameters["step_number"] is not None
            if has_step_id == has_step_number:
                raise QueryPlanValidationError("Recipe 步骤必须且只能提供 step_id 或 step_number")
            if has_step_id:
                parameters["step_id"] = self._required_id(parameters, "step_id")
            if has_step_number and (
                not isinstance(parameters["step_number"], int)
                or isinstance(parameters["step_number"], bool)
                or not 1 <= parameters["step_number"] <= 1000
            ):
                raise QueryPlanValidationError("step_number 超出范围")
        elif template_id == "ingredient_recipes_v1":
            parameters["ingredient_id"] = self._required_id(parameters, "ingredient_id")
        elif template_id == "ingredient_vegetable_pairs_v1":
            parameters["ingredient_id"] = self._required_id(parameters, "ingredient_id")
            if parameters.get("vegetable_category") != "蔬菜":
                raise QueryPlanValidationError("vegetable_category 只能是已核验的蔬菜分类")
        elif template_id == "technique_chunks_v1":
            self._required_id(parameters, "technique_doc_id")
        elif template_id == "recipe_cuisine_filter_v1":
            recipe_ids = parameters.get("recipe_ids")
            if not isinstance(recipe_ids, (list, tuple)) or not recipe_ids or len(recipe_ids) > self.MAX_CANDIDATES:
                raise QueryPlanValidationError("recipe_ids 必须是有限非空序列")
            for recipe_id in recipe_ids:
                if not isinstance(recipe_id, str) or not recipe_id.strip() or len(recipe_id) > 150:
                    raise QueryPlanValidationError("recipe_ids 含非法 ID")
            parameters["recipe_ids"] = [recipe_id.strip() for recipe_id in recipe_ids]
            parameters["cuisine_type"] = self._required_id(parameters, "cuisine_type")
