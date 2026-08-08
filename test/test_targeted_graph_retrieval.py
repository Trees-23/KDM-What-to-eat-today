from __future__ import annotations

from contextlib import contextmanager

import pytest

from rag_modules.query_plan import QueryPlan
from rag_modules.targeted_graph_retrieval import TargetedGraphRetriever


class FakeSession:
    def __init__(self, rows=None, error=None):
        self.rows = rows or []
        self.error = error
        self.calls = []

    def run(self, query, parameters):
        self.calls.append((query, parameters))
        if self.error:
            raise self.error
        return self.rows


class FakeDriver:
    def __init__(self, session):
        self.session_instance = session

    @contextmanager
    def session(self, database=None):
        yield self.session_instance


def _plan(template_id, intent, entity_type, parameters, max_candidates=20):
    return QueryPlan(intent, template_id, entity_type, parameters, max_candidates=max_candidates)


@pytest.mark.parametrize(
    ("plan", "rows", "expected_nodes", "relationship"),
    [
        (_plan("recipe_step_anchor_v1", "RECIPE_STEP", "Recipe", {"recipe_id": "r1", "step_number": 1, "limit": 1}, 1), [{"recipe_id": "r1", "step_id": "s1", "step_order": 1}], {"r1", "s1"}, "CONTAINS_STEP"),
        (_plan("ingredient_recipes_v1", "INGREDIENT_RECIPES", "Ingredient", {"ingredient_id": "i1", "limit": 5}), [{"ingredient_id": "i1", "recipe_id": "r1", "recipe_name": "菜谱"}], {"i1", "r1"}, "REQUIRES"),
        (_plan("ingredient_vegetable_pairs_v1", "INGREDIENT_VEGETABLE_PAIRS", "Ingredient", {"ingredient_id": "i1", "vegetable_category": "蔬菜", "limit": 5}), [{"ingredient_id": "i1", "recipe_id": "r1", "vegetable_id": "v1", "vegetable_category": "蔬菜"}], {"i1", "r1", "v1"}, "REQUIRES"),
        (_plan("technique_chunks_v1", "TECHNIQUE_CHUNKS", "TechniqueDoc", {"technique_doc_id": "t1", "limit": 5}), [{"technique_doc_id": "t1", "technique_chunk_id": "c1", "chunk_order": 1}], {"t1", "c1"}, "HAS_CHUNK"),
        (_plan("recipe_cuisine_filter_v1", "RECIPE_CUISINE_FILTER", "Recipe", {"recipe_ids": ["r1"], "cuisine_type": "川菜", "limit": 5}), [{"recipe_id": "r1", "cuisine_type": "川菜"}], {"r1"}, "PROPERTY_FILTER"),
    ],
)
def test_fixed_templates_return_graph_facts_with_full_ids_direction_and_timestamp(plan, rows, expected_nodes, relationship):
    session = FakeSession(rows)
    fact = TargetedGraphRetriever(FakeDriver(session), database="neo4j").retrieve(plan)

    assert fact.status == "verified"
    assert set(fact.node_ids) == expected_nodes
    assert fact.properties["relationship_type"] == relationship
    assert fact.properties["database_timestamp"].endswith("+00:00")
    assert len(session.calls) == 1
    assert f"// {plan.template_id}" in session.calls[0][0]
    assert "LIMIT $limit" in session.calls[0][0]


def test_not_found_and_service_failure_are_explicit_without_text_evidence():
    plan = _plan("ingredient_recipes_v1", "INGREDIENT_RECIPES", "Ingredient", {"ingredient_id": "i1", "limit": 5})

    not_found = TargetedGraphRetriever(FakeDriver(FakeSession())).retrieve(plan)
    unavailable = TargetedGraphRetriever(FakeDriver(FakeSession(error=OSError("neo4j down")))).retrieve(plan)

    assert not_found.status == "not_found"
    assert not_found.node_ids == ()
    assert unavailable.status == "unavailable"
    assert unavailable.properties["error_type"] == "OSError"


def test_disabled_targeted_graph_keeps_the_validated_plan_as_unavailable():
    plan = _plan("ingredient_recipes_v1", "INGREDIENT_RECIPES", "Ingredient", {"ingredient_id": "i1", "limit": 5})

    fact = TargetedGraphRetriever.unavailable_fact(plan)

    assert fact.status == "unavailable"
    assert fact.node_ids == ()
    assert fact.properties["error_type"] == "FeatureFlagDisabled"


def test_unavailable_intent_without_entity_id_does_not_invent_node_ids():
    fact = TargetedGraphRetriever.unavailable_for_intent("INGREDIENT_RECIPES")

    assert fact.status == "unavailable"
    assert fact.node_ids == ()
    assert fact.properties["error_type"] == "EntityResolverUnavailable"


def test_retriever_rejects_free_cypher_before_opening_driver_session():
    session = FakeSession()
    retriever = TargetedGraphRetriever(FakeDriver(session))

    with pytest.raises(ValueError):
        retriever.retrieve(
            {
                "intent": "INGREDIENT_RECIPES",
                "template_id": "ingredient_recipes_v1",
                "entity_type": "Ingredient",
                "parameters": {"ingredient_id": "i1", "cypher": "MATCH (n) RETURN n"},
            }
        )

    assert session.calls == []
