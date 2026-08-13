from __future__ import annotations

from contextlib import contextmanager

import pytest

from rag_modules.milvus_v2_index import ArtifactMismatchError
from rag_modules.parent_document_materializer import ParentDocumentMaterializer, SourceParent
from rag_modules.parent_document_store import ParentDocumentStore
from rag_modules.restricted_vector_retrieval import RestrictedVectorRetriever


class FakeMilvus:
    def __init__(self, hits):
        self.hits = hits
        self.calls = []

    def search(self, **kwargs):
        self.calls.append(kwargs)
        return [self.hits]


class FakeEmbedder:
    def __init__(self):
        self.queries = []

    def embed_query(self, query):
        self.queries.append(query)
        return [0.1] * 512


def _store(tmp_path):
    result = ParentDocumentMaterializer(chunk_size=50, chunk_overlap=5).materialize_documents(
        [
            SourceParent("parent-a", "Recipe", "甲", "甲正文", {"node_id": "parent-a"}),
            SourceParent("parent-b", "Recipe", "乙", "乙正文", {"node_id": "parent-b"}),
            SourceParent("tip-a", "TechniqueDoc", "技巧", "技巧正文", {"node_id": "tip-a"}),
        ]
    )
    path = tmp_path / "pds.sqlite"
    pointer = tmp_path / "active.json"
    result.write(str(path), publish=True, active_pointer=str(pointer))
    return ParentDocumentStore.open(path, active_pointer=pointer), result


def test_parent_aggregation_hydrates_top_parent_and_applies_scope_filter(tmp_path):
    store, result = _store(tmp_path)
    chunks = list(store.iter_chunks(result.manifest.build_id))
    first = chunks[0]
    second = chunks[-1]
    client = FakeMilvus(
        [
            {"id": first.chunk_id, "distance": 0.91, "entity": {"chunk_id": first.chunk_id, "parent_id": first.parent_id, "chunk_index": 0, "build_id": result.manifest.build_id, "text_hash": first.text_hash}},
            {"id": second.chunk_id, "distance": 0.80, "entity": {"chunk_id": second.chunk_id, "parent_id": second.parent_id, "chunk_index": 0, "build_id": result.manifest.build_id, "text_hash": second.text_hash}},
        ]
    )
    retriever = RestrictedVectorRetriever(client, parent_store=store, collection=f"cooking_knowledge_v2_{result.manifest.build_id[:12]}", build_id=result.manifest.build_id)

    results = retriever.retrieve("测试", parent_ids=[first.parent_id], top_k=1, query_vector=[0.1] * 512)

    assert len(results) == 1
    assert results[0].parent_id == first.parent_id
    assert results[0].text_evidence.text == "甲正文"
    assert "parent_id in ['parent-a']" == client.calls[0]["filter"]
    store.close()


def test_empty_scope_is_never_a_full_collection_fallback(tmp_path):
    store, result = _store(tmp_path)
    client = FakeMilvus([])
    retriever = RestrictedVectorRetriever(client, parent_store=store, collection=f"cooking_knowledge_v2_{result.manifest.build_id[:12]}", build_id=result.manifest.build_id)
    with pytest.raises(ValueError, match="为空"):
        retriever.retrieve("测试", parent_ids=[], query_vector=[0.1] * 512)
    assert client.calls == []
    store.close()


def test_retriever_uses_explicit_embedder_for_query_text(tmp_path):
    store, result = _store(tmp_path)
    chunk = next(store.iter_chunks(result.manifest.build_id))
    embedder = FakeEmbedder()
    client = FakeMilvus(
        [{
            "id": chunk.chunk_id,
            "distance": 0.9,
            "entity": {
                "parent_id": chunk.parent_id,
                "chunk_index": 0,
                "build_id": result.manifest.build_id,
                "text_hash": chunk.text_hash,
            },
        }]
    )
    retriever = RestrictedVectorRetriever(
        client,
        parent_store=store,
        collection=f"cooking_knowledge_v2_{result.manifest.build_id[:12]}",
        build_id=result.manifest.build_id,
        embedder=embedder,
    )

    retriever.retrieve("清淡", top_k=1)

    assert embedder.queries == ["清淡"]
    assert client.calls[0]["data"] == [[0.1] * 512]
    store.close()


def test_retriever_filters_parent_evidence_to_locally_selected_type(tmp_path):
    store, result = _store(tmp_path)
    chunks = list(store.iter_chunks(result.manifest.build_id))
    recipe = next(chunk for chunk in chunks if chunk.parent_id == "parent-a")
    technique = next(chunk for chunk in chunks if chunk.parent_id == "tip-a")
    client = FakeMilvus(
        [
            {"id": technique.chunk_id, "distance": 0.99, "entity": {"chunk_id": technique.chunk_id, "parent_id": technique.parent_id, "chunk_index": technique.chunk_index, "build_id": result.manifest.build_id, "text_hash": technique.text_hash}},
            {"id": recipe.chunk_id, "distance": 0.90, "entity": {"chunk_id": recipe.chunk_id, "parent_id": recipe.parent_id, "chunk_index": recipe.chunk_index, "build_id": result.manifest.build_id, "text_hash": recipe.text_hash}},
        ]
    )
    retriever = RestrictedVectorRetriever(client, parent_store=store, collection=f"cooking_knowledge_v2_{result.manifest.build_id[:12]}", build_id=result.manifest.build_id)

    results = retriever.retrieve("快手家常菜", expected_parent_type="Recipe", top_k=2, query_vector=[0.1] * 512)

    assert [item.parent_id for item in results] == ["parent-a"]
    assert all(item.text_evidence.parent_id != "tip-a" for item in results)
    store.close()


def test_mismatched_child_build_rejects_hydration(tmp_path):
    store, result = _store(tmp_path)
    chunk = next(store.iter_chunks(result.manifest.build_id))
    client = FakeMilvus([{"id": chunk.chunk_id, "distance": 0.9, "entity": {"chunk_id": chunk.chunk_id, "parent_id": chunk.parent_id, "chunk_index": 0, "build_id": "wrong", "text_hash": chunk.text_hash}}])
    retriever = RestrictedVectorRetriever(client, parent_store=store, collection=f"cooking_knowledge_v2_{result.manifest.build_id[:12]}", build_id=result.manifest.build_id)
    with pytest.raises(ArtifactMismatchError):
        retriever.retrieve("测试", query_vector=[0.1] * 512)
    store.close()
