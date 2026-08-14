"""推荐约束与重排验收卷 V1 的 18 题可重复组件验收。"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from rag_modules.intent_candidate import IntentCandidate
from rag_modules.preference_reranker import PreferenceReranker
from rag_modules.recommendation_constraints import RecommendationConstraintCompiler
from rag_modules.restricted_vector_retrieval import CandidateMetadata


PAPER = Path(__file__).resolve().parents[1] / "_other" / "考试" / "推荐约束与重排验收-V1" / "试卷题库.json"
QUESTIONS = json.loads(PAPER.read_text(encoding="utf-8"))["questions"]


def _candidate(question: str) -> IntentCandidate:
    tools = ["MICROWAVE"] if "微波炉" in question else []
    methods = []
    if "蒸" in question:
        methods.append("STEAM")
    if "油炸" in question or "炸" in question:
        methods.append("FRY")
    if "炒" in question:
        methods.append("STIR_FRY")
    preferences = []
    if "清爽" in question:
        preferences.append("LIGHT_FEEL")
    if "简单" in question or "少步骤" in question:
        preferences.append("FEW_STEPS")
    meal = ["BREAKFAST"] if "早餐" in question else (["DINNER"] if "晚餐" in question or "晚饭" in question else [])
    servings = 2 if "两个人" in question else None
    return IntentCandidate(intent="PREFERENCE_RECOMMEND", confidence=.9, slots={
        "step_number": None, "cuisines": ["SICHUAN_STYLE"] if "川菜" in question or "川味" in question else [],
        "ingredients": [], "preferences": preferences, "meal_context": meal, "tools": tools, "methods": methods,
        "servings": servings, "time_budget_minutes": None, "nutrition_constraint": None,
    })


@pytest.mark.parametrize("row", QUESTIONS, ids=[row["question_id"] for row in QUESTIONS])
def test_recommendation_constraints_acceptance_v1(row):
    question_id = row["question_id"]
    question = row["question"]
    spec = RecommendationConstraintCompiler().compile(question, _candidate(question))
    hard = spec.hard_filters
    if question_id == "RCR-01":
        assert hard.exclusive_cooking_appliances == ("MICROWAVE",)
    elif question_id == "RCR-02":
        assert hard.excluded_cooking_appliances == ("MICROWAVE",)
    elif question_id == "RCR-03":
        assert spec.soft_preferences.tools == ("MICROWAVE",) and not hard.required_cooking_appliances
    elif question_id == "RCR-04":
        assert hard.methods == ("STEAM",)
    elif question_id == "RCR-05":
        assert hard.methods == ("STEAM",) and {"FRY", "STIR_FRY"} <= set(hard.excluded_methods)
    elif question_id == "RCR-06":
        assert hard.methods == ("STIR_FRY",)
    elif question_id == "RCR-07":
        assert hard.excluded_methods == ("STIR_FRY",)
    elif question_id == "RCR-08":
        assert hard.cuisines == ("SICHUAN_STYLE",) and hard.methods == ("STEAM",)
    elif question_id == "RCR-09":
        assert hard.max_total_minutes == 30
    elif question_id == "RCR-10":
        assert spec.clarification_reason == "CONSTRAINT_CONFLICT_METHOD"
    elif question_id == "RCR-11":
        assert hard.exclusive_cooking_appliances == ("MICROWAVE",) and hard.methods == ("STEAM",) and hard.max_total_minutes == 30
    elif question_id == "RCR-12":
        assert hard.max_total_minutes is None and spec.soft_preferences.preferences == ()
    elif question_id == "RCR-13":
        assert spec.soft_preferences.target_servings == 2 and not hard.methods
    elif question_id == "RCR-14":
        assert "FEW_STEPS" in spec.soft_preferences.preferences
    elif question_id == "RCR-15":
        assert "LIGHT_FEEL" in spec.soft_preferences.preferences and "STEAM" in spec.soft_preferences.methods
    elif question_id == "RCR-16":
        hit = CandidateMetadata("r", "标题", .5, .001, .501, 1, ("r:0",), {})
        assert not hasattr(hit, "full_content")
    elif question_id == "RCR-17":
        assert RecommendationConstraintCompiler().compile(question, _candidate(question)).policy_version == "recommendation_constraints_v1"
    elif question_id == "RCR-18":
        assert PreferenceReranker.version == "recommendation_rerank_v1"
