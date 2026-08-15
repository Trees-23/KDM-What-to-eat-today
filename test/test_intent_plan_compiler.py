from __future__ import annotations

from types import SimpleNamespace

from rag_modules.intent_candidate import IntentCandidate
from rag_modules.intent_plan_compiler import IntentPlanCompiler


def candidate(intent="PREFERENCE_RECOMMEND", *, mentions=None, slots=None):
    default_slots = {
        "cuisines": [], "ingredients": [], "preferences": ["LIGHT_FEEL"], "meal_context": ["DINNER"],
        "tools": [], "methods": [], "servings": None, "time_budget_minutes": None,
        "step_number": None, "nutrition_constraint": None,
    }
    default_slots.update(slots or {})
    if intent == "RECIPE_STEP":
        default_slots["step_number"] = 1
    if intent == "STRICT_NUTRITION":
        default_slots["nutrition_constraint"] = {"constraint_type": "FAT_GRAMS", "max_value": 5}
    return IntentCandidate(intent=intent, confidence=0.9, entity_mentions=mentions or [], slots=default_slots)


def entity(node_id="i1", node_type="Ingredient", ambiguity=False):
    return SimpleNamespace(node_id=node_id, node_type=node_type, ambiguity=ambiguity)


def test_preference_without_hard_scope_compiles_to_restricted_all_child_chunks():
    result = IntentPlanCompiler(max_candidates=3).compile(candidate())
    assert result.status == "EXECUTE"
    assert result.query_plan.parameters == {"scope": "all_child_chunks", "limit": 3}
    assert result.query_plan.source == "rule"
    assert result.claim_policy.soft_preferences == ("LIGHT_FEEL", "DINNER")


def test_preference_with_scope_never_expands_empty_or_large_scope():
    compiler = IntentPlanCompiler(max_candidates=2)
    assert compiler.compile(candidate(), scoped_recipe_ids=[]).action == "NO_PREFERENCE_RESULTS"
    assert compiler.compile(candidate(), scoped_recipe_ids=["r1", "r2", "r3"]).action == "SCOPE_TOO_LARGE"
    scoped = compiler.compile(candidate(), scoped_recipe_ids=["r1"])
    assert scoped.query_plan.parameters["scope"] == "candidate_parents"


def test_preference_accepts_complete_verified_parent_scope_up_to_validator_bound():
    compiler = IntentPlanCompiler()
    ids = [f"recipe-{number}" for number in range(32)]

    result = compiler.compile(candidate(), scoped_recipe_ids=ids)

    assert result.status == "EXECUTE"
    assert result.query_plan.parameters["parent_ids"] == ids
    assert result.query_plan.parameters["limit"] == 50


def test_entity_plans_are_local_and_non_execute_states_have_no_plan():
    compiler = IntentPlanCompiler(max_candidates=3)
    recipe_step = compiler.compile(candidate("RECIPE_STEP", mentions=[{"text": "菜"}]), resolved_entities=[entity("r1", "Recipe")])
    assert recipe_step.query_plan.parameters == {"recipe_id": "r1", "step_number": 1, "limit": 1}
    assert compiler.compile(candidate("RECIPE_DETAIL"), resolved_entities=[]).status == "TERMINAL"
    assert compiler.compile(candidate("RECIPE_DETAIL"), resolved_entities=[entity("r1", "Recipe", True)]).status == "CLARIFY"
    detail = compiler.compile(candidate("RECIPE_DETAIL"), resolved_entities=[entity("r1", "Recipe")])
    assert detail.can_execute and detail.query_plan is None
    lookup = compiler.compile(candidate("ENTITY_LOOKUP"), resolved_entities=[entity("r1", "Recipe")])
    assert lookup.status == "TERMINAL"
    assert lookup.action == "ENTITY_LOOKUP_RESOLVED"


def test_strict_nutrition_and_dependency_failure_are_terminal_and_unavailable():
    compiler = IntentPlanCompiler()
    nutrition = compiler.compile(candidate("STRICT_NUTRITION"))
    unavailable = compiler.compile(candidate(), dependencies_available=False)
    assert nutrition.status == "TERMINAL"
    assert nutrition.action == "NUTRITION_EVIDENCE_INSUFFICIENT"
    assert not nutrition.may_generate
    assert unavailable.status == "UNAVAILABLE"
    assert unavailable.query_plan is None
