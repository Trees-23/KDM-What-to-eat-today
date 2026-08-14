from __future__ import annotations

import pytest

from rag_modules.intent_candidate import IntentCandidate, IntentCandidateValidationError
from rag_modules.request_boundary import RetrievalRequest


def _candidate(**overrides):
    value = {
        "intent": "PREFERENCE_RECOMMEND",
        "confidence": 0.9,
        "entity_mentions": [],
        "slots": {
            "step_number": None,
            "cuisines": ["SICHUAN_STYLE"],
            "ingredients": [],
            "flavor_ingredients": [],
            "preferences": ["LIGHT_FEEL"],
            "meal_context": ["DINNER"],
            "tools": [],
            "methods": [],
            "servings": None,
            "time_budget_minutes": None,
            "nutrition_constraint": None,
        },
    }
    value.update(overrides)
    return value


def test_candidate_schema_accepts_only_low_privilege_user_demand_fields():
    candidate = IntentCandidate.parse_untrusted(_candidate())

    assert candidate.intent == "PREFERENCE_RECOMMEND"
    assert "template_id" not in IntentCandidate.json_schema().get("properties", {})


def test_candidate_accepts_flavor_components_without_execution_authority():
    payload = _candidate()
    payload["slots"]["flavor_ingredients"] = ["番茄", "大蒜"]

    candidate = IntentCandidate.parse_untrusted(payload)

    assert candidate.slots.flavor_ingredients == ["番茄", "大蒜"]


@pytest.mark.parametrize("key", ["recipe_id", "template_id", "filter", "top_k", "evidence", "cypher"])
def test_candidate_rejects_execution_authority_fields_at_any_depth(key):
    payload = _candidate()
    payload["slots"][key] = "untrusted"

    with pytest.raises(IntentCandidateValidationError, match="越权字段"):
        IntentCandidate.parse_untrusted(payload)


def test_candidate_rejects_unknown_enum_and_invalid_step_combination():
    invalid_enum = _candidate()
    invalid_enum["slots"]["preferences"] = ["LOW_CALORIE"]
    with pytest.raises(IntentCandidateValidationError):
        IntentCandidate.parse_untrusted(invalid_enum)

    invalid_step = _candidate(intent="RECIPE_STEP")
    with pytest.raises(IntentCandidateValidationError):
        IntentCandidate.parse_untrusted(invalid_step)


def test_strict_nutrition_constraint_is_closed_and_json_schema_safe():
    strict = _candidate(intent="STRICT_NUTRITION")
    strict["slots"]["nutrition_constraint"] = {"constraint_type": "FAT_GRAMS", "max_value": 5}
    candidate = IntentCandidate.parse_untrusted(strict)

    assert candidate.slots.nutrition_constraint.constraint_type == "FAT_GRAMS"
    invalid = _candidate(intent="STRICT_NUTRITION")
    invalid["slots"]["nutrition_constraint"] = {"constraint_type": "FAT_GRAMS", "max_value": 5, "filter": "forged"}
    with pytest.raises(IntentCandidateValidationError):
        IntentCandidate.parse_untrusted(invalid)

    schema = IntentCandidate.json_schema()
    assert schema["$defs"]["NutritionConstraint"]["additionalProperties"] is False
    assert set(schema["$defs"]["IntentSlots"]["required"]) == set(schema["$defs"]["IntentSlots"]["properties"])


def test_request_boundary_excludes_evaluation_constraints_from_planner_and_nutrition_input():
    request = RetrievalRequest(
        user_message="想喝一碗清淡些的川味汤。",
        evaluation_constraints="没有治理数据时不要断言低脂。",
        system_instructions="始终使用证据。",
    )

    assert request.planner_input == "想喝一碗清淡些的川味汤。"
    assert request.nutrition_input == "想喝一碗清淡些的川味汤。"
    assert "低脂" not in request.planner_input
