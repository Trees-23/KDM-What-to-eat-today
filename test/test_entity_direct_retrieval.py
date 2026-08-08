from __future__ import annotations

from contextlib import contextmanager

import pytest

from rag_modules.entity_direct_retrieval import EntityDirectRetriever
from rag_modules.parent_document_materializer import AnchorSpec, ParentDocumentMaterializer, SourceParent
from rag_modules.parent_document_store import ParentDocumentStore
from rag_modules.retrieval_contracts import EntityCandidate


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
        metadata={"node_id": "recipe-1"},
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
