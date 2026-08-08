"""阶段 3 的固定查询计划契约。"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Mapping


QUERY_PLAN_INTENTS = frozenset(
    {
        "RECIPE_STEP",
        "INGREDIENT_RECIPES",
        "INGREDIENT_VEGETABLE_PAIRS",
        "TECHNIQUE_CHUNKS",
        "RECIPE_CUISINE_FILTER",
    }
)

TEMPLATE_BY_INTENT = {
    "RECIPE_STEP": "recipe_step_anchor_v1",
    "INGREDIENT_RECIPES": "ingredient_recipes_v1",
    "INGREDIENT_VEGETABLE_PAIRS": "ingredient_vegetable_pairs_v1",
    "TECHNIQUE_CHUNKS": "technique_chunks_v1",
    "RECIPE_CUISINE_FILTER": "recipe_cuisine_filter_v1",
}

ENTITY_TYPE_BY_INTENT = {
    "RECIPE_STEP": "Recipe",
    "INGREDIENT_RECIPES": "Ingredient",
    "INGREDIENT_VEGETABLE_PAIRS": "Ingredient",
    "TECHNIQUE_CHUNKS": "TechniqueDoc",
    "RECIPE_CUISINE_FILTER": "Recipe",
}


@dataclass(frozen=True)
class QueryPlan:
    """经过 validator 校验后才可交给 TargetedGraphRetriever 的计划。"""

    intent: str
    template_id: str
    entity_type: str
    parameters: Mapping[str, Any]
    max_candidates: int = 20
    source: str = "rule"

    def __post_init__(self) -> None:
        object.__setattr__(self, "parameters", dict(self.parameters))

    def to_dict(self) -> dict[str, Any]:
        return {
            "intent": self.intent,
            "template_id": self.template_id,
            "entity_type": self.entity_type,
            "parameters": dict(self.parameters),
            "max_candidates": self.max_candidates,
            "source": self.source,
        }

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "QueryPlan":
        return cls(
            intent=value["intent"],
            template_id=value["template_id"],
            entity_type=value["entity_type"],
            parameters=value.get("parameters", {}),
            max_candidates=value.get("max_candidates", 20),
            source=value.get("source", "rule"),
        )

    @classmethod
    def from_json(cls, payload: str) -> "QueryPlan":
        decoded = json.loads(payload)
        if not isinstance(decoded, Mapping):
            raise ValueError("QueryPlan JSON 必须是对象")
        return cls.from_dict(decoded)
