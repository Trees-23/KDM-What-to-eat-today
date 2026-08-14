"""本地推荐约束编译器。

模型只能提交 ``IntentCandidate`` 的受控槽位。本模块只使用可信用户原话为
这些槽位赋予软偏好或硬约束，且从不产生查询语言、实体 ID 或排序表达式。
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Mapping, Sequence

from .intent_candidate import IntentCandidate


_METHOD_TERMS = {
    "STEAM": ("蒸制", "蒸菜", "蒸"),
    "BOIL": ("煮", "水煮"),
    "FRY": ("油炸", "炸制", "炸"),
    "STEW": ("炖", "焖"),
    "STIR_FRY": ("煸炒", "爆炒", "炒菜", "炒"),
}
_TOOL_TERMS = {
    "MICROWAVE": ("微波炉",),
    "RICE_COOKER": ("电饭煲",),
}
_POSITIVE_HARD = ("完全只能", "只能", "只有", "只用", "仅用", "必须", "仅", "只")
_NEGATIVE_HARD = ("完全不要", "不使用", "不要", "不能", "不得")
_SOFT = ("优先", "尽量", "也行", "最好", "想试试")


@dataclass(frozen=True)
class HardRecipeFilters:
    cuisines: tuple[str, ...] = ()
    verified_ingredient_ids: tuple[str, ...] = ()
    methods: tuple[str, ...] = ()
    excluded_methods: tuple[str, ...] = ()
    required_cooking_appliances: tuple[str, ...] = ()
    excluded_cooking_appliances: tuple[str, ...] = ()
    # 仅“只用/只有”这种排他原话可设置；普通 required 不代表排他。
    exclusive_cooking_appliances: tuple[str, ...] = ()
    max_total_minutes: int | None = None


@dataclass(frozen=True)
class SoftRecipePreferences:
    methods: tuple[str, ...] = ()
    tools: tuple[str, ...] = ()
    preferences: tuple[str, ...] = ()
    meal_context: tuple[str, ...] = ()
    prefer_shorter_time: bool = False
    target_servings: int | None = None


@dataclass(frozen=True)
class ConstraintSpec:
    intent: str
    hard_filters: HardRecipeFilters = HardRecipeFilters()
    soft_preferences: SoftRecipePreferences = SoftRecipePreferences()
    clarification_reason: str | None = None
    policy_version: str = "recommendation_constraints_v1"
    decisions: tuple[Mapping[str, str], ...] = ()

    @property
    def executable(self) -> bool:
        return self.clarification_reason is None


@dataclass(frozen=True)
class ResolvedCandidateScope:
    build_id: str
    parent_ids: tuple[str, ...]
    hard_filter_counts: Mapping[str, int]


class RecommendationConstraintCompiler:
    """将已验证槽位与原始问题编译为低权限本地约束。"""

    def compile(
        self,
        user_message: str,
        candidate: IntentCandidate,
        *,
        verified_ingredient_ids: Sequence[str] = (),
    ) -> ConstraintSpec:
        if not isinstance(candidate, IntentCandidate) or candidate.intent != "PREFERENCE_RECOMMEND":
            return ConstraintSpec(intent=getattr(candidate, "intent", "INVALID"), clarification_reason="INTENT_NOT_PREFERENCE")
        text = str(user_message or "").strip()
        if not text:
            return ConstraintSpec(intent=candidate.intent, clarification_reason="USER_MESSAGE_EMPTY")
        methods = self._mentioned_slots(text, candidate.slots.methods, _METHOD_TERMS)
        tools = self._mentioned_slots(text, candidate.slots.tools, _TOOL_TERMS)
        decisions: list[Mapping[str, str]] = []
        positive_methods: list[str] = []
        excluded_methods: list[str] = []
        positive_tools: list[str] = []
        excluded_tools: list[str] = []
        exclusive_tools: list[str] = []
        soft_methods: list[str] = []
        soft_tools: list[str] = []
        local_conflict_reason: str | None = None

        for value in methods:
            strength, marker = self._strength(text, _METHOD_TERMS[value])
            decisions.append({"field": "method", "value": value, "strength": strength, "marker": marker})
            if strength == "conflict":
                local_conflict_reason = "CONSTRAINT_CONFLICT_METHOD"
                continue
            if strength == "positive_hard":
                positive_methods.append(value)
                # “只蒸”本身也排除 V1 明确冲突做法。
                if marker in {"只", "仅", "只能", "只有", "只用", "仅用", "完全只能"}:
                    excluded_methods.extend(item for item in ("FRY", "STIR_FRY") if item != value)
            elif strength == "negative_hard":
                excluded_methods.append(value)
            else:
                soft_methods.append(value)

        for value in tools:
            strength, marker = self._strength(text, _TOOL_TERMS[value])
            # “家里只有微波炉”与“只能用微波炉”均为设备排他约束。
            exclusive = value == "MICROWAVE" and bool(re.search(r"(?:家里)?只有\s*微波炉|只(?:能|用)?\s*微波炉", text))
            if exclusive:
                strength, marker = "positive_hard", "排他设备"
            decisions.append({"field": "tool", "value": value, "strength": strength, "marker": marker})
            if strength == "conflict":
                local_conflict_reason = "CONSTRAINT_CONFLICT_APPLIANCE"
                continue
            if strength == "positive_hard":
                positive_tools.append(value)
                if exclusive or marker in {"只", "仅", "只能", "只有", "只用", "仅用", "完全只能"}:
                    exclusive_tools.append(value)
            elif strength == "negative_hard":
                excluded_tools.append(value)
            else:
                soft_tools.append(value)

        max_minutes = self._max_minutes(text)
        if max_minutes is not None:
            decisions.append({"field": "total_minutes", "value": str(max_minutes), "strength": "positive_hard", "marker": "分钟内"})
        hard = HardRecipeFilters(
            cuisines=tuple(candidate.slots.cuisines),
            verified_ingredient_ids=tuple(dict.fromkeys(str(value) for value in verified_ingredient_ids if str(value))),
            methods=tuple(dict.fromkeys(positive_methods)),
            excluded_methods=tuple(dict.fromkeys(excluded_methods)),
            required_cooking_appliances=tuple(dict.fromkeys(positive_tools)),
            excluded_cooking_appliances=tuple(dict.fromkeys(excluded_tools)),
            exclusive_cooking_appliances=tuple(dict.fromkeys(exclusive_tools)),
            max_total_minutes=max_minutes,
        )
        soft = SoftRecipePreferences(
            methods=tuple(dict.fromkeys(soft_methods)),
            tools=tuple(dict.fromkeys(soft_tools)),
            preferences=tuple(candidate.slots.preferences),
            meal_context=tuple(candidate.slots.meal_context),
            prefer_shorter_time="FEW_STEPS" in candidate.slots.preferences,
            target_servings=candidate.slots.servings,
        )
        reason = local_conflict_reason or self._conflict_reason(hard)
        return ConstraintSpec(candidate.intent, hard, soft, reason, decisions=tuple(decisions))

    @staticmethod
    def _mentioned_slots(text: str, slots: Sequence[str], vocabulary: Mapping[str, Sequence[str]]) -> tuple[str, ...]:
        # 本地字典仅用于核对模型给出的受控值，不能把任意自由文本升格为执行字段。
        return tuple(value for value in dict.fromkeys(slots) if value in vocabulary and any(term in text for term in vocabulary[value]))

    @staticmethod
    def _strength(text: str, terms: Sequence[str]) -> tuple[str, str]:
        positions = [match.start() for term in terms for match in re.finditer(re.escape(term), text)]
        if not positions:
            return "soft", ""
        strengths: list[tuple[str, str]] = []
        for position in positions:
            strength = RecommendationConstraintCompiler._strength_at(text, position)
            if strength != ("soft", ""):
                strengths.append(strength)
        kinds = {value for value, _marker in strengths}
        if "positive_hard" in kinds and "negative_hard" in kinds:
            return "conflict", "同一对象同时肯定和否定"
        if "negative_hard" in kinds:
            return next(item for item in strengths if item[0] == "negative_hard")
        if "positive_hard" in kinds:
            return next(item for item in strengths if item[0] == "positive_hard")
        return strengths[0] if strengths else ("soft", "")

    @staticmethod
    def _strength_at(text: str, position: int) -> tuple[str, str]:
        # 限制词必须修饰紧随其后的对象；不能让“不要油炸”反向影响同句前面的
        # “只要蒸菜”。句尾的“蒸菜也行”仍允许作为软偏好识别。
        prefix = text[max(0, position - 8):position]
        suffix = text[position: min(len(text), position + 8)]
        for marker in _NEGATIVE_HARD:
            if marker in prefix:
                return "negative_hard", marker
        for marker in _POSITIVE_HARD:
            if marker in prefix:
                return "positive_hard", marker
        for marker in _SOFT:
            if marker in prefix or marker in suffix:
                return "soft", marker
        return "soft", ""

    @staticmethod
    def _max_minutes(text: str) -> int | None:
        match = re.search(r"(?<!\d)(\d{1,4})\s*分钟(?:之)?内", text)
        if not match:
            return None
        value = int(match.group(1))
        return value if 1 <= value <= 1440 else None

    @staticmethod
    def _conflict_reason(hard: HardRecipeFilters) -> str | None:
        if set(hard.methods) & set(hard.excluded_methods):
            return "CONSTRAINT_CONFLICT_METHOD"
        if set(hard.required_cooking_appliances) & set(hard.excluded_cooking_appliances):
            return "CONSTRAINT_CONFLICT_APPLIANCE"
        return None
