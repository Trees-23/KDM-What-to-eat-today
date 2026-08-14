from types import SimpleNamespace

from rag_modules.intent_candidate import IntentCandidate
from rag_modules.recommendation_constraints import RecommendationConstraintCompiler
from rag_modules.restricted_vector_retrieval import CandidateMetadata


class Audit:
    def __init__(self): self.events = []
    def record_event(self, stage, status="completed", **fields): self.events.append((stage, status, fields))


class Store:
    active_build_id = "build-1"
    def __init__(self, rows): self.rows = rows
    def iter_recipe_metadata(self, *, build_id=None, parent_ids=None):
        assert build_id == self.active_build_id
        allowed = set(parent_ids) if parent_ids is not None else None
        return [row for row in self.rows if allowed is None or row.parent_id in allowed]


def candidate(*, tools=(), methods=(), preferences=()):
    return IntentCandidate(intent="PREFERENCE_RECOMMEND", confidence=.9, slots={
        "step_number": None, "cuisines": [], "ingredients": [], "preferences": list(preferences),
        "meal_context": [], "tools": list(tools), "methods": list(methods), "servings": None,
        "time_budget_minutes": None, "nutrition_constraint": None,
    })


def system(rows):
    import main
    value = main.AdvancedGraphRAGSystem.__new__(main.AdvancedGraphRAGSystem)
    value.config = SimpleNamespace(retrieval_recommendation_max_hard_scope=200, retrieval_recommendation_candidate_k=30, retrieval_recommendation_answer_k=5)
    value.parent_document_store = Store(rows)
    return value


def test_only_microwave_scope_rejects_unknown_or_other_required_appliances():
    rows = [
        SimpleNamespace(parent_id="good", metadata={"recipe_cooking_appliances": ["MICROWAVE"], "unknown_cooking_appliance": False}),
        SimpleNamespace(parent_id="other", metadata={"recipe_cooking_appliances": ["MICROWAVE", "OVEN"], "unknown_cooking_appliance": False}),
        SimpleNamespace(parent_id="unknown", metadata={"recipe_cooking_appliances": ["MICROWAVE"], "unknown_cooking_appliance": True}),
    ]
    spec = RecommendationConstraintCompiler().compile("家里只有微波炉", candidate(tools=("MICROWAVE",)))
    scope, failure = system(rows)._resolve_recommendation_scope(spec, None)
    assert failure is None
    assert scope.parent_ids == ("good",)


def test_hard_metadata_unknown_never_passes_time_filter_and_empty_scope_is_closed():
    rows = [SimpleNamespace(parent_id="unknown", metadata={"total_minutes": None})]
    spec = RecommendationConstraintCompiler().compile("30 分钟内做什么", candidate())
    scope, failure = system(rows)._resolve_recommendation_scope(spec, None)
    assert scope is None
    assert failure.action == "NO_PREFERENCE_RESULTS"


class Vector:
    def __init__(self): self.hydrated = []
    def retrieve_candidates(self, _query, **_kwargs):
        return [CandidateMetadata(f"r{number}", f"菜{number}", float(30 - number), .001, float(30 - number), 1, (f"r{number}:0",), {"recipe_methods": ["STEAM"]}) for number in range(30)]
    def hydrate_candidates(self, candidates, **_kwargs):
        self.hydrated = [row.parent_id for row in candidates]
        from rag_modules.retrieval_contracts import TextEvidence
        return [TextEvidence(row.parent_id, "build-1", row.chunk_ids, (), "body:" + row.parent_id, "parent_store") for row in candidates]


def test_two_stage_pipeline_audits_top30_and_hydrates_only_top5():
    value = system([])
    value.restricted_vector_retriever = Vector()
    value.preference_reranker = None
    audit = Audit()
    plan = SimpleNamespace(parameters={"parent_ids": [f"r{number}" for number in range(30)]}, to_dict=lambda: {"intent": "PREFERENCE_RECOMMEND"})
    bundle = value._try_recommendation_vector("清爽", plan, RecommendationConstraintCompiler().compile("清爽", candidate(preferences=("LIGHT_FEEL",))), audit_run=audit)
    assert len(bundle.text_evidence) == 5
    assert len(value.restricted_vector_retriever.hydrated) == 5
    event = audit.events[-1]
    assert len(event[2]["candidate_top30"]) == 30
    assert len(event[2]["final_top5"]) == 5
