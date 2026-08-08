from __future__ import annotations

from pathlib import Path

from rag_modules.parent_document_materializer import AnchorSpec, ParentDocumentMaterializer, SourceParent
from rag_modules.parent_document_store import ParentDocumentStore


def test_materializer_builds_stable_chunks_and_anchors(tmp_path: Path):
    source = SourceParent(
        parent_id="recipe-1",
        node_type="Recipe",
        title="测试菜谱",
        full_content="# 测试菜谱\n\n## 制作步骤\n### 第1步\n先腌制\n\n## 成品\n完成",
        metadata={"node_id": "recipe-1"},
        anchors=(AnchorSpec("CookingStep", "step-1", "### 第1步\n先腌制", 0, "CONTAINS_STEP"),),
    )
    with ParentDocumentMaterializer(chunk_size=12, chunk_overlap=3) as materializer:
        first = materializer.materialize_documents([source])
        second = materializer.materialize_documents([source])
        assert first.manifest.build_id == second.manifest.build_id
        assert [chunk.chunk_id for chunk in first.chunks] == [chunk.chunk_id for chunk in second.chunks]
        assert len(first.anchors) == 1
        assert first.anchors[0].anchor_type == "CookingStep"
        assert first.anchors[0].chunk_id in {chunk.chunk_id for chunk in first.chunks}

    db_path = tmp_path / "parent_store.sqlite"
    pointer = tmp_path / "active-build"
    first.write(str(db_path), publish=True, active_pointer=str(pointer))
    with ParentDocumentStore.open(db_path, active_pointer=pointer) as store:
        assert store.get_full_parent("recipe-1") is not None
        assert store.get_anchor_window("recipe-1", "CookingStep", "step-1", 1, 1)


def test_materializer_rejects_invalid_overlap():
    try:
        ParentDocumentMaterializer(driver=object(), chunk_size=10, chunk_overlap=10)
    except ValueError as exc:
        assert "chunk_overlap" in str(exc)
    else:
        raise AssertionError("应拒绝 overlap >= size")

