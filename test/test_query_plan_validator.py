from __future__ import annotations

import pytest

from rag_modules.query_plan import QueryPlan
from rag_modules.query_plan_validator import QueryPlanValidationError, QueryPlanValidator


def _plan(intent, entity_type, parameters, *, max_candidates=20):
    templates = {
        "RECIPE_STEP": "recipe_step_anchor_v1",
        "INGREDIENT_RECIPES": "ingredient_recipes_v1",
        "INGREDIENT_VEGETABLE_PAIRS": "ingredient_vegetable_pairs_v1",
        "TECHNIQUE_CHUNKS": "technique_chunks_v1",
        "RECIPE_CUISINE_FILTER": "recipe_cuisine_filter_v1",
    }
    return QueryPlan(intent, templates[intent], entity_type, parameters, max_candidates=max_candidates)


@pytest.mark.parametrize(
    ("candidate", "expected_template"),
    [
        (_plan("RECIPE_STEP", "Recipe", {"recipe_id": "r1", "step_number": 1, "limit": 1}, max_candidates=1), "recipe_step_anchor_v1"),
        (_plan("INGREDIENT_RECIPES", "Ingredient", {"ingredient_id": "i1", "limit": 10}), "ingredient_recipes_v1"),
        (_plan("INGREDIENT_VEGETABLE_PAIRS", "Ingredient", {"ingredient_id": "i1", "vegetable_category": "蔬菜", "limit": 10}), "ingredient_vegetable_pairs_v1"),
        (_plan("TECHNIQUE_CHUNKS", "TechniqueDoc", {"technique_doc_id": "t1", "limit": 10}), "technique_chunks_v1"),
        (_plan("RECIPE_CUISINE_FILTER", "Recipe", {"recipe_ids": ["r1", "r2"], "cuisine_type": "川菜", "limit": 10}), "recipe_cuisine_filter_v1"),
    ],
)
def test_validator_accepts_only_complete_whitelist_plans(candidate, expected_template):
    plan = QueryPlanValidator().validate(candidate)

    assert plan.template_id == expected_template
    assert plan.parameters["limit"] <= plan.max_candidates


@pytest.mark.parametrize(
    "candidate",
    [
        {"intent": "INGREDIENT_RECIPES", "template_id": "ingredient_recipes_v1", "entity_type": "Ingredient", "parameters": {"ingredient_id": "i1", "cypher": "MATCH (n) RETURN n"}},
        {"intent": "INGREDIENT_RECIPES", "template_id": "ingredient_recipes_v1", "entity_type": "Ingredient", "parameters": {"ingredient_id": "i1", "label": "Recipe"}},
        {"intent": "INGREDIENT_RECIPES", "template_id": "ingredient_recipes_v1", "entity_type": "Ingredient", "parameters": {"ingredient_id": "i1", "relationship": "REQUIRES"}},
        {"intent": "INGREDIENT_RECIPES", "template_id": "recipe_step_anchor_v1", "entity_type": "Ingredient", "parameters": {"ingredient_id": "i1"}},
        {"intent": "INGREDIENT_RECIPES", "template_id": "ingredient_recipes_v1", "entity_type": "Ingredient", "parameters": {"ingredient_id": "i1", "limit": 51}},
    ],
)
def test_validator_rejects_arbitrary_cypher_schema_and_limit_escalation(candidate):
    with pytest.raises(QueryPlanValidationError):
        QueryPlanValidator().validate(candidate)


def test_invalid_llm_json_falls_back_only_to_rule_plan_with_stable_entity_id():
    validator = QueryPlanValidator()

    fallback = validator.validate_or_conservative(
        '{"cypher":"MATCH (n) RETURN n"}',
        query_text="鸡肉搭配什么蔬菜？",
        entity_id="ingredient-chicken",
    )

    assert fallback is not None
    assert fallback.intent == "INGREDIENT_VEGETABLE_PAIRS"
    assert fallback.parameters["ingredient_id"] == "ingredient-chicken"
    assert validator.validate_or_conservative("not json", query_text="鸡肉搭配什么蔬菜？") is None
