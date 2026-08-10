from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys
import types
from unittest.mock import patch

import pytest

from rag_modules.entity_direct_retrieval import EntityDirectRetriever
from rag_modules.evidence_builder import EvidenceBuilder
from rag_modules.parent_document_materializer import AnchorSpec, ParentDocumentMaterializer, SourceParent
from rag_modules.parent_document_store import ParentDocumentStore
from rag_modules.query_plan import QueryPlan
from rag_modules.query_plan_validator import QueryPlanValidator
from rag_modules.rag_audit import NULL_AUDIT_RUN
from rag_modules.retrieval_contracts import EntityCandidate, EvidenceBundle
from rag_modules.targeted_graph_retrieval import TargetedGraphRetriever
from rag_modules.milvus_v2_index import (
    ArtifactMismatchError,
    MilvusV2Schema,
    RetrievalArtifactManifest,
    create_milvus_client,
    pds_manifest_sha256,
)
from rag_modules.nutrition_policy import SOFT_PREFERENCE_POLICY
from rag_modules.recommendation_evidence import RecommendationEvidence
from rag_modules.restricted_vector_retrieval import RestrictedVectorRetriever


class FakeSession:
    def __init__(self, step_row=None, error=None):
        self.step_row = step_row
        self.error = error
        self.calls = []

    def run(self, query, parameters):
        self.calls.append((query, parameters))
        if self.error:
            raise self.error
        if "recipe_step_anchor_v1" in query:
            return [self.step_row] if self.step_row else []
        if "technique_chunk_anchor_v1" in query:
            return []
        raise AssertionError("实体直达执行了未知图查询")


class FakeDriver:
    def __init__(self, session):
        self.session_instance = session

    @contextmanager
    def session(self, database=None):
        yield self.session_instance


def _recipe_candidate():
    return EntityCandidate("recipe-1", "Recipe", "测试菜谱", "exact_name", 1.0, False)


def _build_store(tmp_path):
    source = SourceParent(
        parent_id="recipe-1",
        node_type="Recipe",
        title="测试菜谱",
        full_content="# 测试菜谱\n\n## 所需食材\n花生米\n\n## 制作步骤\n### 第1步\n先腌制鸡肉\n\n### 第2步\n下锅翻炒",
        metadata={"node_id": "recipe-1", "cuisine_type": "川菜"},
        anchors=(
            AnchorSpec("CookingStep", "step-1", "### 第1步\n先腌制鸡肉", 0, "CONTAINS_STEP"),
            AnchorSpec("CookingStep", "step-2", "### 第2步\n下锅翻炒", 1, "CONTAINS_STEP"),
        ),
    )
    materializer = ParentDocumentMaterializer(chunk_size=28, chunk_overlap=6)
    artifact = materializer.materialize_documents([source])
    db_path = tmp_path / "parent.sqlite"
    pointer = tmp_path / "active.json"
    artifact.write(str(db_path), publish=True, active_pointer=str(pointer))
    return ParentDocumentStore.open(tmp_path, active_pointer=pointer)


def test_recipe_full_reads_pds_and_never_calls_global_vector_search(tmp_path):
    store = _build_store(tmp_path)
    driver = FakeDriver(FakeSession())
    retriever = EntityDirectRetriever(store, driver, database="neo4j")

    bundle = retriever.retrieve(_recipe_candidate(), {"scope": "RECIPE_FULL"})

    assert bundle.text_evidence[0].parent_id == "recipe-1"
    assert "所需食材" in bundle.text_evidence[0].text
    assert bundle.text_evidence[0].chunk_ids
    assert driver.session_instance.calls == []
    assert bundle.graph_facts[0].template_id == "entity_resolution_v1"


def test_recipe_step_uses_only_fixed_parameterized_anchor_template(tmp_path):
    store = _build_store(tmp_path)
    session = FakeSession({"step_id": "step-1", "step_order": 1, "step_number": 1})
    retriever = EntityDirectRetriever(store, FakeDriver(session), database="neo4j")

    bundle = retriever.retrieve(
        _recipe_candidate(), {"scope": "RECIPE_STEP", "step_number": 1, "before": 1, "after": 1}
    )

    assert bundle.graph_facts[-1].template_id == "recipe_step_anchor_v1"
    assert bundle.graph_facts[-1].status == "verified"
    assert "先腌制鸡肉" in bundle.text_evidence[0].text
    assert any("花生米" in evidence.text for evidence in bundle.text_evidence)
    query, parameters = session.calls[0]
    assert "MATCH (r:Recipe {nodeId: $recipe_id})-[c:CONTAINS_STEP]->(s:CookingStep)" in query
    assert parameters == {"recipe_id": "recipe-1", "step_id": None, "step_number": 1}


@pytest.mark.parametrize(
    "scope",
    [
        {"scope": "RECIPE_STEP", "step_number": 1, "cypher": "MATCH (n) RETURN n"},
        {"scope": "RECIPE_STEP", "step_number": 1, "label": "Recipe"},
        {"scope": "RECIPE_STEP", "step_number": 1, "relationship": "HAS_CHUNK"},
        {"scope": "RECIPE_STEP", "step_number": 1, "step_id": "step-1"},
    ],
)
def test_recipe_step_rejects_free_cypher_labels_relationships_and_ambiguous_parameters(tmp_path, scope):
    store = _build_store(tmp_path)
    session = FakeSession({"step_id": "step-1", "step_order": 1, "step_number": 1})
    retriever = EntityDirectRetriever(store, FakeDriver(session))

    with pytest.raises(ValueError):
        retriever.retrieve(_recipe_candidate(), scope)

    assert session.calls == []


def test_step_not_found_and_graph_unavailable_are_explicit_and_auditable(tmp_path):
    store = _build_store(tmp_path)
    missing = EntityDirectRetriever(store, FakeDriver(FakeSession()))
    missing_bundle = missing.retrieve(_recipe_candidate(), {"scope": "RECIPE_STEP", "step_number": 9})
    assert missing_bundle.graph_facts[-1].status == "not_found"
    assert "STEP_NOT_FOUND" in missing_bundle.limitations

    unavailable = EntityDirectRetriever(store, FakeDriver(FakeSession(error=OSError("neo4j down"))))
    unavailable_bundle = unavailable.retrieve(_recipe_candidate(), {"scope": "RECIPE_STEP", "step_number": 1})
    assert unavailable_bundle.graph_facts[-1].status == "unavailable"
    assert "graph-unavailable" in unavailable_bundle.limitations


def test_parent_store_failure_does_not_fabricate_text_and_marks_legacy_fallback():
    class FailingStore:
        active_build_id = "build-test"

        def get_full_parent(self, *_args, **_kwargs):
            raise OSError("sqlite unavailable")

    retriever = EntityDirectRetriever(FailingStore(), FakeDriver(FakeSession()))

    bundle = retriever.retrieve(_recipe_candidate(), {"scope": "RECIPE_FULL"})

    assert bundle.text_evidence == ()
    assert "parent-store-unavailable" in bundle.limitations
    assert bundle.requires_legacy_fallback


class _EmptyResolver:
    def __init__(self):
        self.calls = []

    def resolve(self, query, expected_types):
        self.calls.append((query, expected_types))
        return []


class _SingleResolver:
    def __init__(self, candidate):
        self.candidate = candidate
        self.calls = []

    def resolve(self, query, expected_types):
        self.calls.append((query, expected_types))
        return [self.candidate]


class _FailingResolver:
    def resolve(self, query, expected_types):
        raise OSError("neo4j resolver down")


class _Router:
    def __init__(self):
        self.calls = []

    def route_query(self, query, top_k, audit_run=None):
        self.calls.append((query, top_k, audit_run))
        return ["legacy"], "legacy-analysis"


class _MismatchedVectorRetriever:
    def retrieve(self, *_args, **_kwargs):
        raise ArtifactMismatchError("test artifact mismatch")


class _RecordingVectorRetriever:
    def __init__(self):
        self.calls = []

    def retrieve(self, query, **kwargs):
        self.calls.append((query, kwargs))
        return []


class _AuditRun:
    def __init__(self):
        self.events = []
        self.finished = []
        self.errors = []

    def mark_request_start(self):
        return None

    def record_event(self, stage, status="completed", **fields):
        self.events.append((stage, status, fields))

    def finish_request(self, **fields):
        self.finished.append(fields)

    def record_error(self, stage, error):
        self.errors.append((stage, error))


class _Generation:
    def __init__(self):
        self.calls = []

    def generate_adaptive_answer(self, query, documents, audit_run=None):
        self.calls.append((query, documents, audit_run))
        return "generated"


@dataclass
class _Config:
    top_k: int = 3
    enable_rag_audit: bool = True
    rag_audit_root_dir: str = ""
    rag_audit_max_content_chars: int = 4000
    retrieval_query_plan_enabled: bool = False
    retrieval_targeted_graph_enabled: bool = False


def _system_with_empty_resolver(audit_manager=None):
    system_type = _load_main_system_type(audit_manager=audit_manager)
    system = system_type.__new__(system_type)
    system.entity_resolver = _EmptyResolver()
    system.entity_direct_retriever = object()
    system.query_router = _Router()
    return system


def _load_main_system_type(audit_manager=None):
    """在不加载可选运行时客户端的前提下测试实际入口分派。"""
    package = types.ModuleType("rag_modules")
    package.GraphDataPreparationModule = object
    package.MilvusIndexConstructionModule = object
    package.GenerationIntegrationModule = object

    def module_with(**attributes):
        module = types.ModuleType("unused")
        for name, value in attributes.items():
            setattr(module, name, value)
        return module

    if audit_manager is None:
        class _UnusedAuditManager:
            @classmethod
            def from_config(cls, _config):
                raise AssertionError("测试应显式传入 audit_run")

        audit_manager = _UnusedAuditManager

    modules = {
        "config": module_with(DEFAULT_CONFIG=object(), GraphRAGConfig=object),
        "rag_modules": package,
        "rag_modules.hybrid_retrieval": module_with(HybridRetrievalModule=object),
        "rag_modules.graph_rag_retrieval": module_with(GraphRAGRetrieval=object),
        "rag_modules.intelligent_query_router": module_with(IntelligentQueryRouter=object, QueryAnalysis=object),
        "rag_modules.session_cache_manager": module_with(SessionCacheManager=object),
        "rag_modules.web_service_handler": module_with(WebServiceHandler=object),
        "rag_modules.recipe_recommendation": module_with(RecipeRecommendationManager=object),
        "rag_modules.parent_document_store": module_with(ParentDocumentStore=object),
        "rag_modules.entity_resolver": module_with(EntityResolver=object),
        "rag_modules.entity_direct_retrieval": module_with(EntityDirectRetriever=object),
        "rag_modules.evidence_builder": module_with(EvidenceBuilder=EvidenceBuilder),
        "rag_modules.query_plan": module_with(QueryPlan=QueryPlan),
        "rag_modules.query_plan_validator": module_with(QueryPlanValidator=QueryPlanValidator),
        "rag_modules.targeted_graph_retrieval": module_with(TargetedGraphRetriever=TargetedGraphRetriever),
        "rag_modules.milvus_v2_index": module_with(
            ArtifactMismatchError=ArtifactMismatchError,
            MilvusV2Schema=MilvusV2Schema,
            RetrievalArtifactManifest=RetrievalArtifactManifest,
            create_milvus_client=create_milvus_client,
            pds_manifest_sha256=pds_manifest_sha256,
        ),
        "rag_modules.restricted_vector_retrieval": module_with(RestrictedVectorRetriever=RestrictedVectorRetriever),
        "rag_modules.rag_audit": module_with(RAGAuditManager=audit_manager),
        "rag_modules.retrieval_contracts": sys.modules["rag_modules.retrieval_contracts"],
        "rag_modules.nutrition_policy": module_with(SOFT_PREFERENCE_POLICY=SOFT_PREFERENCE_POLICY),
        "rag_modules.recommendation_evidence": module_with(RecommendationEvidence=RecommendationEvidence),
    }
    main_path = Path(__file__).resolve().parents[1] / "main.py"
    spec = importlib.util.spec_from_file_location("_phase2_main_under_test", main_path)
    module = importlib.util.module_from_spec(spec)
    with patch.dict(sys.modules, modules):
        assert spec.loader is not None
        spec.loader.exec_module(module)
    return module.AdvancedGraphRAGSystem


def test_unresolved_entity_is_explicit_and_never_calls_legacy_router_without_authorization():
    system = _system_with_empty_resolver()
    audit = _AuditRun()

    bundle, analysis = system.retrieve_for_generation(
        "有蓝莓红烧肉这道菜吗？",
        3,
        audit_run=audit,
    )

    assert isinstance(bundle, EvidenceBundle)
    assert analysis is None
    assert "ENTITY_NOT_FOUND" in bundle.limitations
    assert system.query_router.calls == []
    assert ("entity_direct", "entity_not_found") == audit.events[0][:2]
    assert audit.events[0][2]["vector_search_calls"] == 0


def test_unresolved_entity_can_use_legacy_router_only_after_explicit_generalized_authorization():
    system = _system_with_empty_resolver()
    audit = _AuditRun()

    documents, analysis = system.retrieve_for_generation(
        "有蓝莓红烧肉这道菜吗？",
        3,
        audit_run=audit,
        allow_generalized_advice=True,
    )

    assert documents == ["legacy"]
    assert analysis == "legacy-analysis"
    assert len(system.query_router.calls) == 1
    assert system.query_router.calls[0][2] is audit
    assert ("entity_direct", "entity_not_found_generalized") == audit.events[0][:2]
    assert audit.events[0][2]["vector_search_calls"] == 0


def test_v2_artifact_mismatch_returns_to_legacy_router():
    system_type = _load_main_system_type()
    system = system_type.__new__(system_type)
    system.config = _Config()
    system.config.retrieval_milvus_v2_enabled = True
    system.query_plan_validator = QueryPlanValidator()
    system.entity_resolver = None
    system.entity_direct_retriever = None
    system.restricted_vector_retriever = _MismatchedVectorRetriever()
    system.query_router = _Router()
    audit = _AuditRun()

    documents, analysis = system.retrieve_for_generation("夏天吃什么清淡的？", 3, audit_run=audit)

    assert documents == ["legacy"]
    assert analysis == "legacy-analysis"
    assert len(system.query_router.calls) == 1
    assert any(event[:2] == ("restricted_vector", "artifact-mismatch") for event in audit.events)


def test_legacy_fallback_can_be_explicitly_disabled():
    system_type = _load_main_system_type()
    system = system_type.__new__(system_type)
    system.config = _Config()
    system.config.retrieval_milvus_v2_enabled = True
    system.config.retrieval_legacy_fallback_enabled = False
    system.query_plan_validator = QueryPlanValidator()
    system.entity_resolver = None
    system.entity_direct_retriever = None
    system.restricted_vector_retriever = _MismatchedVectorRetriever()
    system.query_router = _Router()
    audit = _AuditRun()

    bundle, analysis = system.retrieve_for_generation("夏天吃什么清淡的？", 3, audit_run=audit)

    assert analysis is None
    assert isinstance(bundle, EvidenceBundle)
    assert "LEGACY_FALLBACK_DISABLED" in bundle.limitations
    assert system.query_router.calls == []
    assert any(event[:2] == ("legacy_fallback", "disabled") for event in audit.events)


def test_preference_query_plan_passes_cuisine_parent_scope_to_v2(tmp_path):
    system_type = _load_main_system_type()
    system = system_type.__new__(system_type)
    system.config = _Config()
    system.config.retrieval_milvus_v2_enabled = True
    system.query_plan_validator = QueryPlanValidator()
    system.parent_document_store = _build_store(tmp_path)
    system.entity_resolver = None
    system.entity_direct_retriever = None
    system.restricted_vector_retriever = _RecordingVectorRetriever()
    system.query_router = _Router()

    bundle, analysis = system.retrieve_for_generation("推荐川菜清淡的菜", 3)

    assert analysis is None
    assert bundle.query_plan["intent"] == "PREFERENCE_RECOMMEND"
    assert bundle.query_plan["parameters"]["scope"] == "candidate_parents"
    assert bundle.query_plan["parameters"]["parent_ids"] == ["recipe-1"]
    assert system.restricted_vector_retriever.calls == [
        ("推荐川菜清淡的菜", {"parent_ids": ["recipe-1"], "top_k": 3})
    ]
    assert system.query_router.calls == []


def test_preference_query_without_candidates_uses_explicit_full_child_scope():
    system_type = _load_main_system_type()
    system = system_type.__new__(system_type)
    system.config = _Config()
    system.config.retrieval_milvus_v2_enabled = True
    system.query_plan_validator = QueryPlanValidator()
    system.entity_resolver = None
    system.entity_direct_retriever = None
    system.restricted_vector_retriever = _RecordingVectorRetriever()
    system.query_router = _Router()

    bundle, analysis = system.retrieve_for_generation("夏天吃什么清淡的？", 3)

    assert analysis is None
    assert bundle.query_plan["parameters"]["scope"] == "all_child_chunks"
    assert "parent_ids" not in bundle.query_plan["parameters"]
    assert system.restricted_vector_retriever.calls == [
        ("夏天吃什么清淡的？", {"parent_ids": None, "top_k": 3})
    ]


def test_preference_initialization_failure_returns_to_legacy_router(tmp_path):
    system_type = _load_main_system_type()
    system = system_type.__new__(system_type)
    system.config = _Config()
    system.config.retrieval_milvus_v2_enabled = True
    system.config.retrieval_artifact_manifest_path = str(tmp_path / "missing-manifest.json")
    system.query_plan_validator = QueryPlanValidator()
    system.entity_resolver = None
    system.entity_direct_retriever = None
    system.restricted_vector_retriever = object()
    system.query_router = _Router()
    audit = _AuditRun()

    system._initialize_restricted_vector_retriever()

    documents, analysis = system.retrieve_for_generation("夏天吃什么清淡的？", 3, audit_run=audit)

    assert system.restricted_vector_retriever is None
    assert documents == ["legacy"]
    assert analysis == "legacy-analysis"
    assert len(system.query_router.calls) == 1
    assert any(event[:2] == ("restricted_vector", "artifact-unavailable") for event in audit.events)


def test_preference_initialization_artifact_mismatch_is_audited_before_legacy_fallback(tmp_path):
    system_type = _load_main_system_type()
    system = system_type.__new__(system_type)
    system.config = _Config()
    system.config.retrieval_milvus_v2_enabled = True
    system.config.retrieval_artifact_manifest_path = str(tmp_path / "mismatched-manifest.json")
    system.query_plan_validator = QueryPlanValidator()
    system.entity_resolver = None
    system.entity_direct_retriever = None
    system.restricted_vector_retriever = object()
    system.query_router = _Router()
    audit = _AuditRun()

    with patch.object(RetrievalArtifactManifest, "read", side_effect=ArtifactMismatchError("PDS build mismatch")):
        system._initialize_restricted_vector_retriever()

    documents, analysis = system.retrieve_for_generation("夏天吃什么清淡的？", 3, audit_run=audit)

    assert system.restricted_vector_retriever is None
    assert documents == ["legacy"]
    assert analysis == "legacy-analysis"
    assert len(system.query_router.calls) == 1
    assert any(event[:2] == ("restricted_vector", "artifact-mismatch") for event in audit.events)


def test_query_plan_prioritizes_step_graph_fact_and_hydrates_existing_pds_text(tmp_path):
    system_type = _load_main_system_type()
    session = FakeSession({"recipe_id": "recipe-1", "step_id": "step-1", "step_order": 1, "step_number": 1})
    system = system_type.__new__(system_type)
    system.config = _Config(retrieval_query_plan_enabled=True, retrieval_targeted_graph_enabled=True)
    system.entity_resolver = _SingleResolver(_recipe_candidate())
    system.entity_direct_retriever = EntityDirectRetriever(_build_store(tmp_path), FakeDriver(session), database="neo4j")
    system.query_plan_validator = QueryPlanValidator()
    system.targeted_graph_retriever = TargetedGraphRetriever(FakeDriver(session), database="neo4j")
    system.query_router = _Router()

    bundle, analysis = system.retrieve_for_generation("测试菜谱第一步怎么做？", 3)

    assert analysis is None
    assert bundle.query_plan["template_id"] == "recipe_step_anchor_v1"
    assert len(bundle.graph_facts) == 1
    assert bundle.graph_facts[0].status == "verified"
    assert "先腌制鸡肉" in bundle.text_evidence[0].text
    assert system.query_router.calls == []


def test_query_plan_returns_unavailable_when_targeted_graph_flag_is_disabled():
    system_type = _load_main_system_type()
    system = system_type.__new__(system_type)
    system.config = _Config(retrieval_query_plan_enabled=True, retrieval_targeted_graph_enabled=False)
    system.entity_resolver = _SingleResolver(
        EntityCandidate("ingredient-1", "Ingredient", "鸡肉", "exact_name", 1.0, False)
    )
    system.entity_direct_retriever = None
    system.query_plan_validator = QueryPlanValidator()
    system.targeted_graph_retriever = None
    system.query_router = _Router()

    bundle, analysis = system.retrieve_for_generation("鸡肉能做什么？", 3)

    assert analysis is None
    assert bundle.graph_facts[0].status == "unavailable"
    assert "GRAPH_UNAVAILABLE" in bundle.limitations
    assert system.query_router.calls == []


def test_query_plan_converts_entity_resolver_failure_to_unavailable_fact():
    system_type = _load_main_system_type()
    system = system_type.__new__(system_type)
    system.config = _Config(retrieval_query_plan_enabled=True, retrieval_targeted_graph_enabled=True)
    system.entity_resolver = _FailingResolver()
    system.entity_direct_retriever = None
    system.query_plan_validator = QueryPlanValidator()
    system.targeted_graph_retriever = None
    system.query_router = _Router()

    bundle, analysis = system.retrieve_for_generation("鸡肉能做什么？", 3)

    assert analysis is None
    assert bundle.graph_facts[0].status == "unavailable"
    assert bundle.graph_facts[0].properties["error_type"] == "OSError"
    assert "GRAPH_UNAVAILABLE" in bundle.limitations
    assert system.query_router.calls == []


def test_cli_path_passes_audit_run_to_entity_not_found_and_generation(tmp_path):
    system = _system_with_empty_resolver()
    system.system_ready = True
    system.config = _Config(rag_audit_root_dir=str(Path(tmp_path)))
    system.generation_module = _Generation()
    audit = _AuditRun()

    result, analysis = system.ask_question_with_routing(
        "有蓝莓红烧肉这道菜吗？",
        audit_run=audit,
    )

    assert result == "generated"
    assert analysis is None
    assert system.query_router.calls == []
    assert system.generation_module.calls[0][2] is audit
    assert ("entity_direct", "entity_not_found") == audit.events[0][:2]
    assert audit.finished == [{"success": True, "final_source": "entity_direct"}]


def test_cli_path_works_when_audit_is_disabled():
    class _DisabledAuditManager:
        @classmethod
        def from_config(cls, _config):
            return cls()

        def create_run(self):
            return NULL_AUDIT_RUN

    system = _system_with_empty_resolver(audit_manager=_DisabledAuditManager)
    system.system_ready = True
    system.config = _Config(enable_rag_audit=False)
    system.generation_module = _Generation()

    result, analysis = system.ask_question_with_routing("有蓝莓红烧肉这道菜吗？")

    assert result == "generated"
    assert analysis is None
    assert system.query_router.calls == []
    assert system.generation_module.calls[0][2] is NULL_AUDIT_RUN
