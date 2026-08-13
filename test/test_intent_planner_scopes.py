from __future__ import annotations

from types import SimpleNamespace

from rag_modules.intent_candidate import IntentCandidate
from rag_modules.query_plan_validator import QueryPlanValidator
from rag_modules.retrieval_contracts import GraphFact


class _Resolver:
    def __init__(self, values): self.values = values
    def resolve(self, mention, expected_types): return self.values.get(mention, [])


class _Graph:
    def __init__(self, rows_by_template): self.rows_by_template = rows_by_template; self.calls = []
    def retrieve(self, plan, audit_run=None):
        self.calls.append(plan)
        rows = self.rows_by_template.get(plan.template_id, [])
        return GraphFact("fact:" + plan.template_id, plan.template_id, tuple({row["recipe_id"] for row in rows}), (), {"rows": rows}, "verified")


class _Pds:
    active_build_id = "build"
    def __init__(self, parents): self.parents = parents
    def iter_chunks(self, _build): return [SimpleNamespace(parent_id=value) for value in self.parents]
    def get_full_parent(self, parent_id): return self.parents[parent_id]


def _candidate(*, cuisine=False, mentions=()):
    return IntentCandidate(intent="PREFERENCE_RECOMMEND", confidence=.9, entity_mentions=[{"text": value} for value in mentions], slots={"cuisines": ["SICHUAN_STYLE"] if cuisine else [], "ingredients": [], "preferences": ["LIGHT_FEEL"], "meal_context": [], "tools": [], "methods": [], "servings": None, "time_budget_minutes": None, "step_number": None, "nutrition_constraint": None})


def _system(resolver, graph, pds=None):
    import main
    system = main.AdvancedGraphRAGSystem.__new__(main.AdvancedGraphRAGSystem)
    system.entity_resolver = resolver; system.targeted_graph_retriever = graph; system.query_plan_validator = QueryPlanValidator(); system.parent_document_store = pds
    return system


def test_ingredient_scope_is_verified_before_vector_scope_and_empty_never_expands():
    chicken = SimpleNamespace(node_id="i-chicken", node_type="Ingredient", ambiguity=False)
    graph = _Graph({"ingredient_recipes_v1": [{"recipe_id": "r1"}, {"recipe_id": "r2"}]})
    system = _system(_Resolver({"鸡肉": [chicken]}), graph)
    ids, failure = system._planner_preference_scope(_candidate(mentions=("鸡肉",)))
    assert ids == ["r1", "r2"] and failure is None
    assert graph.calls[0].template_id == "ingredient_recipes_v1"


def test_multiple_ingredients_use_intersection_and_scope_excess_is_terminal():
    values = {name: [SimpleNamespace(node_id=node, node_type="Ingredient", ambiguity=False)] for name, node in (("鸡肉", "i1"), ("豆腐", "i2"))}
    graph = _Graph({"ingredient_recipes_v1": [{"recipe_id": "r2"}]})
    system = _system(_Resolver(values), graph)
    ids, failure = system._planner_preference_scope(_candidate(mentions=("鸡肉", "豆腐")))
    assert ids == ["r2"] and failure is None
    assert len(graph.calls) == 2


def test_cuisine_scope_requires_verified_graph_not_unscoped_pds_metadata():
    parent = SimpleNamespace(parent_id="r1", build_id="build", metadata={"cuisine_type": "川菜"})
    graph = _Graph({"recipe_cuisine_filter_v1": [{"recipe_id": "r1"}]})
    system = _system(_Resolver({}), graph, _Pds({"r1": parent}))
    ids, failure = system._planner_preference_scope(_candidate(cuisine=True))
    assert ids == ["r1"] and failure is None
    assert graph.calls[0].template_id == "recipe_cuisine_filter_v1"
