from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from rag_modules.parent_document_store import (
    AnchorRecord,
    BuildManifest,
    CanonicalChunk,
    ParentDocumentStore,
    ParentRecord,
    make_build_manifest,
)


def _fixture_rows():
    parents = [
        ParentRecord(
            parent_id="recipe-1",
            node_type="Recipe",
            title="测试菜谱",
            full_content="# 测试菜谱\n\n## 制作步骤\n### 第1步\n腌制",
            metadata={"category": "家常菜"},
        ),
        ParentRecord(
            parent_id="tech-1",
            node_type="TechniqueDoc",
            title="测试技巧",
            full_content="# 测试技巧\n\n## 正文\n测试正文",
            metadata={"category": "技巧"},
        ),
    ]
    manifest = make_build_manifest(
        parents,
        chunk_config={"chunk_size": 80, "chunk_overlap": 10, "splitter": "heading_v1"},
        builder_version="test",
        created_at="2026-08-08T00:00:00+00:00",
    )
    chunks = [
        CanonicalChunk("recipe-1:chunk:0", "recipe-1", 0, 1, "主标题", parents[0].full_content, manifest.build_id),
        CanonicalChunk("tech-1:chunk:0", "tech-1", 0, 1, "主标题", parents[1].full_content, manifest.build_id),
    ]
    anchors = [
        AnchorRecord("CookingStep", "step-1", "recipe-1", manifest.build_id, "recipe-1:chunk:0", 0, "CONTAINS_STEP"),
        AnchorRecord("TechniqueChunk", "chunk-1", "tech-1", manifest.build_id, "tech-1:chunk:0", 0, "HAS_CHUNK"),
    ]
    return parents, manifest, chunks, anchors


def test_create_open_read_and_anchor_windows(tmp_path: Path):
    parents, manifest, chunks, anchors = _fixture_rows()
    db_path = tmp_path / "parent_store.sqlite"
    pointer = tmp_path / "active-build"
    ParentDocumentStore.create_build(
        db_path, manifest, parents, chunks, anchors, publish=True, active_pointer=pointer
    )

    with ParentDocumentStore.open(tmp_path, active_pointer=pointer) as store:
        assert store.active_build_id == manifest.build_id
        assert store.health_check()["status"] == "ok"
        parent = store.get_full_parent("recipe-1", expected_node_type="Recipe")
        assert parent is not None
        assert parent.title == "测试菜谱"
        assert store.get_full_parent("recipe-1", expected_node_type="TechniqueDoc") is None
        window = store.get_anchor_window("recipe-1", "CookingStep", "step-1", 1, 1)
        assert len(window) == 1
        assert window[0].anchor_ids == ("step-1",)
        assert list(store.iter_chunks())[0].text_hash
        assert store.validate_chunk_linkage(
            [{"chunk_id": "recipe-1:chunk:0", "parent_id": "recipe-1"}]
        ).valid
        report = store.validate_chunk_linkage(
            [{"chunk_id": "recipe-1:chunk:0", "parent_id": "wrong-parent"}]
        )
        assert not report.valid
        assert report.mismatched_rows == ("recipe-1:chunk:0",)


def test_failed_build_does_not_publish_or_overwrite(tmp_path: Path):
    parents, manifest, chunks, anchors = _fixture_rows()
    db_path = tmp_path / "parent_store.sqlite"
    pointer = tmp_path / "active-build"
    pointer.write_text("old-build\n", encoding="utf-8")
    bad_anchor = AnchorRecord(
        "CookingStep", "bad", "recipe-1", manifest.build_id, "missing-chunk", 0, "CONTAINS_STEP"
    )
    with pytest.raises(sqlite3.IntegrityError):
        ParentDocumentStore.create_build(db_path, manifest, parents, chunks, [bad_anchor], publish=True, active_pointer=pointer)
    assert not db_path.exists()
    assert pointer.read_text(encoding="utf-8").strip() == "old-build"


def test_existing_destination_is_never_overwritten(tmp_path: Path):
    parents, manifest, chunks, anchors = _fixture_rows()
    db_path = tmp_path / "parent_store.sqlite"
    ParentDocumentStore.create_build(db_path, manifest, parents, chunks, anchors)
    with pytest.raises(FileExistsError):
        ParentDocumentStore.create_build(db_path, manifest, parents, chunks, anchors)


def test_build_identity_covers_metadata_and_anchors():
    parents, _manifest, chunks, anchors = _fixture_rows()
    first = make_build_manifest(
        parents,
        chunks=chunks,
        anchors=anchors,
        chunk_config={"chunk_size": 80, "chunk_overlap": 10, "splitter": "heading_v1"},
        builder_version="test",
    )
    changed_metadata = [
        ParentRecord(
            parents[0].parent_id,
            parents[0].node_type,
            parents[0].title,
            parents[0].full_content,
            {"category": "川菜"},
        ),
        parents[1],
    ]
    metadata_changed = make_build_manifest(
        changed_metadata,
        chunks=chunks,
        anchors=anchors,
        chunk_config=first.chunk_config,
        builder_version="test",
    )
    changed_anchor = [
        AnchorRecord("CookingStep", "step-1", "recipe-1", "", "recipe-1:chunk:0", 1, "CONTAINS_STEP"),
        anchors[1],
    ]
    anchor_changed = make_build_manifest(
        parents,
        chunks=chunks,
        anchors=changed_anchor,
        chunk_config=first.chunk_config,
        builder_version="test",
    )
    assert first.build_id != metadata_changed.build_id
    assert first.build_id != anchor_changed.build_id


def test_publish_requires_pointer_and_pointer_failure_leaves_ready_build(tmp_path: Path, monkeypatch):
    parents, manifest, chunks, anchors = _fixture_rows()
    db_path = tmp_path / "parent_store.sqlite"
    with pytest.raises(ValueError, match="active_pointer"):
        ParentDocumentStore.create_build(db_path, manifest, parents, chunks, anchors, publish=True)
    assert not db_path.exists()

    pointer = tmp_path / "active-build"
    pointer.write_text("old-build\n", encoding="utf-8")

    def fail_pointer(*_args):
        raise OSError("pointer disk failure")

    monkeypatch.setattr(ParentDocumentStore, "_write_active_pointer", staticmethod(fail_pointer))
    with pytest.raises(OSError, match="pointer disk failure"):
        ParentDocumentStore.create_build(db_path, manifest, parents, chunks, anchors, publish=True, active_pointer=pointer)
    assert pointer.read_text(encoding="utf-8").strip() == "old-build"
    with ParentDocumentStore.open(db_path, active_build_id=manifest.build_id) as store:
        assert store.get_build_manifest(manifest.build_id).status == "ready"


def test_active_pointer_can_roll_back_to_verified_build(tmp_path: Path):
    parents, first_manifest, chunks, anchors = _fixture_rows()
    pointer = tmp_path / "active-build"
    first_path = tmp_path / "first.sqlite"
    ParentDocumentStore.create_build(first_path, first_manifest, parents, chunks, anchors, publish=True, active_pointer=pointer)

    changed_parents = [
        ParentRecord("recipe-1", "Recipe", "新版测试菜谱", "# 新版测试菜谱", {}),
        parents[1],
    ]
    second_manifest = make_build_manifest(
        changed_parents,
        chunk_config=first_manifest.chunk_config,
        builder_version="test",
        created_at="2026-08-08T00:00:01+00:00",
    )
    second_chunks = [
        CanonicalChunk("recipe-1:chunk:0", "recipe-1", 0, 1, "主标题", changed_parents[0].full_content, second_manifest.build_id),
        CanonicalChunk("tech-1:chunk:0", "tech-1", 0, 1, "主标题", parents[1].full_content, second_manifest.build_id),
    ]
    second_anchors = [
        AnchorRecord("CookingStep", "step-1", "recipe-1", second_manifest.build_id, "recipe-1:chunk:0", 0, "CONTAINS_STEP"),
        AnchorRecord("TechniqueChunk", "chunk-1", "tech-1", second_manifest.build_id, "tech-1:chunk:0", 0, "HAS_CHUNK"),
    ]
    second_path = tmp_path / "second.sqlite"
    ParentDocumentStore.create_build(second_path, second_manifest, changed_parents, second_chunks, second_anchors, publish=True, active_pointer=pointer)
    with ParentDocumentStore.open(tmp_path, active_pointer=pointer) as store:
        assert store.active_build_id == second_manifest.build_id

    ParentDocumentStore.publish_existing_build(first_path, first_manifest.build_id, pointer)
    with ParentDocumentStore.open(tmp_path, active_pointer=pointer) as store:
        assert store.active_build_id == first_manifest.build_id
        assert store.get_full_parent("recipe-1").title == "测试菜谱"
