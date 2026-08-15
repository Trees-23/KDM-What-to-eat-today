from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

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


def test_recipe_metadata_materializes_controlled_methods_appliances_and_unknown_state():
    attributes = ParentDocumentMaterializer._recipe_attributes(
        {"prepTime": "6分钟", "cookTime": "15分钟", "servings": "2人份"},
        [
            {"methods": "爆炒", "tools": "微波炉、碗"},
            {"methods": "蒸制", "tools": "可选烤箱"},
        ],
    )
    assert set(attributes["recipe_methods"]) == {"STIR_FRY", "STEAM"}
    assert attributes["recipe_cooking_appliances"] == ["MICROWAVE"]
    assert attributes["recipe_optional_cooking_appliances"] == ["OVEN"]
    assert not attributes["unknown_cooking_appliance"]
    assert (attributes["step_count"], attributes["prep_minutes"], attributes["cook_minutes"], attributes["total_minutes"], attributes["servings_count"]) == (2, 6, 15, 21, 2)


def test_recipe_metadata_recognizes_catalogue_appliances_without_new_fields():
    attributes = ParentDocumentMaterializer._recipe_attributes(
        {"prepTime": "5分钟", "cookTime": "10分钟", "servings": "1人份"},
        [
            {"methods": "烤", "tools": "面包机"},
            {"methods": "烙", "tools": "电饼铛"},
            {"methods": "蒸", "tools": "蒸箱"},
            {"methods": "煮", "tools": "电锅"},
        ],
    )
    assert set(attributes["recipe_cooking_appliances"]) == {
        "BREAD_MAKER", "ELECTRIC_COOKER", "ELECTRIC_GRIDDLE", "STEAM_OVEN",
    }
    assert not attributes["unknown_cooking_appliance"]


def test_neo4j_materialization_excludes_recipe_hierarchy_without_source_path():
    queries = []

    class Session:
        def run(self, query, *_args, **_kwargs):
            queries.append(query)
            return []

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

    materializer = ParentDocumentMaterializer(driver=SimpleNamespace(session=lambda **_kwargs: Session()))
    materializer.materialize_from_neo4j()
    assert "WHERE r.filePath IS NOT NULL AND trim(r.filePath) <> ''" in queries[0]
