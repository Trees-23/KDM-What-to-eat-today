from __future__ import annotations

from types import SimpleNamespace

from main import AdvancedGraphRAGSystem
from rag_modules.query_plan_validator import QueryPlanValidator
from rag_modules.retrieval_contracts import EvidenceBundle, GraphFact, TextEvidence


class _ParentStore:
    active_build_id = "build-test"

    def iter_chunks(self, build_id):
        assert build_id == self.active_build_id
        return (SimpleNamespace(parent_id="recipe-sichuan"),)

    def get_full_parent(self, parent_id):
        assert parent_id == "recipe-sichuan"
        return SimpleNamespace(
            parent_id=parent_id,
            build_id=self.active_build_id,
            metadata={"cuisine_type": "川菜"},
        )


class _GraphScopeRetriever:
    def __init__(self, *, unavailable=False):
        self.unavailable = unavailable
        self.calls = []

    def retrieve(self, plan, audit_run=None):
        self.calls.append(plan)
        if self.unavailable:
            return GraphFact(
                fact_id="cuisine-unavailable",
                template_id=plan.template_id,
                node_ids=(),
                edges=(),
                properties={"error_type": "ServiceUnavailable"},
                status="unavailable",
            )
        return GraphFact(
            fact_id="cuisine-verified",
            template_id=plan.template_id,
            node_ids=("recipe-sichuan",),
            edges=(),
            properties={"cuisine_type": "川菜"},
            status="verified",
        )


class _RestrictedRetriever:
    def __init__(self):
        self.calls = []

    def retrieve(self, query, *, parent_ids=None, top_k=5):
        self.calls.append((query, tuple(parent_ids or ()), top_k))
        return (
            SimpleNamespace(
                text_evidence=TextEvidence(
                    parent_id="recipe-sichuan",
                    build_id="build-test",
                    chunk_ids=("recipe-sichuan:0",),
                    anchor_ids=(),
                    text="少油烹饪提示。",
                    origin="parent_store",
                )
            ),
        )


class _UnexpectedRouter:
    def route_query(self, *args, **kwargs):
        raise AssertionError("营养约束请求不应回退到旧 Router")


class _AuditRun:
    def __init__(self):
        self.events = []

    def record_event(self, stage, status="completed", **fields):
        self.events.append((stage, status, fields))


def _system(*, graph_unavailable=False):
    system = AdvancedGraphRAGSystem.__new__(AdvancedGraphRAGSystem)
    system.config = SimpleNamespace(
        retrieval_query_plan_enabled=False,
        retrieval_milvus_v2_enabled=True,
        retrieval_strict_nutrition_enabled=False,
        top_k=5,
    )
    system.parent_document_store = _ParentStore()
    system.query_plan_validator = QueryPlanValidator()
    system.targeted_graph_retriever = _GraphScopeRetriever(unavailable=graph_unavailable)
    system.restricted_vector_retriever = _RestrictedRetriever()
    system._restricted_vector_init_status = None
    system.entity_resolver = None
    system.entity_direct_retriever = None
    system.query_router = _UnexpectedRouter()
    return system


def test_low_fat_sichuan_query_uses_verified_cuisine_scope_then_returns_soft_preference_evidence():
    system = _system()

    bundle, analysis = system.retrieve_for_generation("推荐低脂川菜", 3)

    assert analysis is None
    assert isinstance(bundle, EvidenceBundle)
    assert system.targeted_graph_retriever.calls[0].parameters == {
        "recipe_ids": ["recipe-sichuan"],
        "cuisine_type": "川菜",
        "limit": 1,
    }
    assert system.restricted_vector_retriever.calls == [
        ("推荐低脂川菜", ("recipe-sichuan",), 3)
    ]
    assert bundle.recommendation_evidence.level == "soft_preference"
    assert "NUTRITION_SOFT_PREFERENCE_ONLY" in bundle.limitations
    assert "NUTRITION_EVIDENCE_INSUFFICIENT" not in bundle.limitations


def test_strict_low_fat_request_returns_evidence_insufficient_without_graph_or_vector_calls():
    system = _system()

    bundle, analysis = system.retrieve_for_generation("推荐严格低脂川菜，每份脂肪不超过 5 克", 3)

    assert analysis is None
    assert isinstance(bundle, EvidenceBundle)
    assert bundle.recommendation_evidence.level == "evidence_insufficient"
    assert "NUTRITION_EVIDENCE_INSUFFICIENT" in bundle.limitations
    assert system.targeted_graph_retriever.calls == []
    assert system.restricted_vector_retriever.calls == []


def test_graph_unavailable_does_not_label_unscoped_vector_results_as_low_fat_sichuan():
    system = _system(graph_unavailable=True)

    bundle, _ = system.retrieve_for_generation("推荐低脂川菜", 3)

    assert bundle.recommendation_evidence.level == "evidence_unavailable"
    assert "NUTRITION_CUISINE_EVIDENCE_UNAVAILABLE" in bundle.limitations
    assert system.restricted_vector_retriever.calls == []


def test_soft_preference_audit_records_evidence_level_policy_and_missing_reason():
    system = _system()
    audit_run = _AuditRun()

    system.retrieve_for_generation("推荐低脂川菜", 3, audit_run=audit_run)

    stage, status, fields = [event for event in audit_run.events if event[0] == "nutrition_recommendation"][-1]
    assert stage == "nutrition_recommendation"
    assert status == "soft-preference-selected"
    assert fields["evidence_level"] == "soft_preference"
    assert fields["policy_version"] == "nutrition_soft_preference_v1"
    assert "不能验证严格低脂" in fields["missing_reason"]
