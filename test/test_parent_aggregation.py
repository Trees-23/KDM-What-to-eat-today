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


def _store(tmp_path):
    result = ParentDocumentMaterializer(chunk_size=50, chunk_overlap=5).materialize_documents(
        [
            SourceParent("parent-a", "Recipe", "甲", "甲正文", {"node_id": "parent-a"}),
            SourceParent("parent-b", "Recipe", "乙", "乙正文", {"node_id": "parent-b"}),
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


def test_mismatched_child_build_rejects_hydration(tmp_path):
    store, result = _store(tmp_path)
    chunk = next(store.iter_chunks(result.manifest.build_id))
    client = FakeMilvus([{"id": chunk.chunk_id, "distance": 0.9, "entity": {"chunk_id": chunk.chunk_id, "parent_id": chunk.parent_id, "chunk_index": 0, "build_id": "wrong", "text_hash": chunk.text_hash}}])
    retriever = RestrictedVectorRetriever(client, parent_store=store, collection=f"cooking_knowledge_v2_{result.manifest.build_id[:12]}", build_id=result.manifest.build_id)
    with pytest.raises(ArtifactMismatchError):
        retriever.retrieve("测试", query_vector=[0.1] * 512)
    store.close()
