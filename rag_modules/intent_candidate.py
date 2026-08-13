"""低权限意图候选单契约，和可执行 QueryPlan 严格隔离。"""

from __future__ import annotations

import math
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


INTENT_CANDIDATE_VERSION = "v1"

INTENT_CODES = frozenset(
    {
        "ENTITY_LOOKUP",
        "RECIPE_DETAIL",
        "RECIPE_STEP",
        "TECHNIQUE_SECTION",
        "INGREDIENT_RECIPES",
        "INGREDIENT_VEGETABLE_PAIRS",
        "PREFERENCE_RECOMMEND",
        "STRICT_NUTRITION",
        "CLARIFY_OR_OUT_OF_SCOPE",
    }
)

_FORBIDDEN_TERMS = frozenset(
    {
        "nodeid",
        "recipe_id",
        "ingredient_id",
        "step_id",
        "parent_id",
        "chunk_id",
        "build_id",
        "cypher",
        "sql",
        "query",
        "where",
        "filter",
        "collection",
        "database",
        "template_id",
        "vector_scope",
        "sort",
        "top_k",
        "max_candidates",
        "evidence",
        "claim_policy",
    }
)


class IntentCandidateValidationError(ValueError):
    """候选单不符合低权限、有限 schema 时抛出。"""


class EntityMention(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)

    text: str = Field(min_length=1, max_length=80)


class IntentSlots(BaseModel):
    """候选单只描述用户需求；所有枚举均由本地程序维护。"""

    model_config = ConfigDict(extra="forbid", frozen=True)

    step_number: int | None = Field(default=None, ge=1, le=1000)
    cuisines: list[Literal["SICHUAN_STYLE"]] = Field(default_factory=list, max_length=5)
    ingredients: list[str] = Field(default_factory=list, max_length=5)
    preferences: list[
        Literal["LIGHT_FEEL", "LOW_OIL_FEEL", "FEW_STEPS", "HOMESTYLE", "MILD_FLAVOR"]
    ] = Field(default_factory=list, max_length=5)
    meal_context: list[Literal["BREAKFAST", "LUNCH", "DINNER"]] = Field(default_factory=list, max_length=5)
    tools: list[Literal["MICROWAVE", "RICE_COOKER"]] = Field(default_factory=list, max_length=5)
    methods: list[Literal["STEAM", "BOIL", "FRY", "STEW"]] = Field(default_factory=list, max_length=5)
    servings: int | None = Field(default=None, ge=1, le=100)
    time_budget_minutes: int | None = Field(default=None, ge=1, le=1440)
    nutrition_constraint: dict[str, object] | None = None

    @field_validator("ingredients")
    @classmethod
    def validate_ingredients(cls, values: list[str]) -> list[str]:
        normalized = [value.strip() for value in values if isinstance(value, str) and value.strip()]
        if len(normalized) != len(values) or any(len(value) > 80 for value in normalized):
            raise ValueError("ingredients 必须是最长 80 字符的非空用户原话")
        return list(dict.fromkeys(normalized))

    @field_validator("cuisines", "preferences", "meal_context", "tools", "methods")
    @classmethod
    def deduplicate_values(cls, values: list[str]) -> list[str]:
        return list(dict.fromkeys(values))


class IntentCandidate(BaseModel):
    """LLM 可生成的唯一对象，不能携带任何检索执行信息。"""

    model_config = ConfigDict(extra="forbid", frozen=True)

    intent: Literal[
        "ENTITY_LOOKUP",
        "RECIPE_DETAIL",
        "RECIPE_STEP",
        "TECHNIQUE_SECTION",
        "INGREDIENT_RECIPES",
        "INGREDIENT_VEGETABLE_PAIRS",
        "PREFERENCE_RECOMMEND",
        "STRICT_NUTRITION",
        "CLARIFY_OR_OUT_OF_SCOPE",
    ]
    confidence: float = Field(ge=0, le=1)
    entity_mentions: list[EntityMention] = Field(default_factory=list, max_length=8)
    slots: IntentSlots = Field(default_factory=IntentSlots)

    @field_validator("confidence")
    @classmethod
    def finite_confidence(cls, value: float) -> float:
        if not math.isfinite(value):
            raise ValueError("confidence 必须是有限数值")
        return value

    @field_validator("entity_mentions")
    @classmethod
    def deduplicate_mentions(cls, values: list[EntityMention]) -> list[EntityMention]:
        seen: set[str] = set()
        result: list[EntityMention] = []
        for mention in values:
            key = mention.text.casefold()
            if key not in seen:
                seen.add(key)
                result.append(mention)
        return result

    @model_validator(mode="after")
    def validate_intent_slot_combination(self) -> "IntentCandidate":
        if self.intent == "RECIPE_STEP" and self.slots.step_number is None:
            raise ValueError("RECIPE_STEP 必须提供 step_number")
        if self.intent != "RECIPE_STEP" and self.slots.step_number is not None:
            raise ValueError("step_number 仅允许用于 RECIPE_STEP")
        if self.intent == "STRICT_NUTRITION" and self.slots.nutrition_constraint is None:
            raise ValueError("STRICT_NUTRITION 必须提供 nutrition_constraint")
        if self.intent != "STRICT_NUTRITION" and self.slots.nutrition_constraint is not None:
            raise ValueError("nutrition_constraint 仅允许用于 STRICT_NUTRITION")
        return self

    @classmethod
    def parse_untrusted(cls, payload: object) -> "IntentCandidate":
        """严格拒绝含执行权字段的模型输出。"""

        cls._reject_forbidden_keys(payload)
        try:
            return cls.model_validate(payload)
        except Exception as error:
            raise IntentCandidateValidationError(str(error)) from error

    @classmethod
    def json_schema(cls) -> dict[str, object]:
        return cls.model_json_schema()

    @classmethod
    def _reject_forbidden_keys(cls, value: object) -> None:
        if isinstance(value, dict):
            for key, nested in value.items():
                normalized = str(key).casefold()
                if normalized in _FORBIDDEN_TERMS:
                    raise IntentCandidateValidationError(f"候选单含越权字段: {key}")
                cls._reject_forbidden_keys(nested)
        elif isinstance(value, list):
            for nested in value:
                cls._reject_forbidden_keys(nested)
