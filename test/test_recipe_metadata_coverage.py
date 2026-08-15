import importlib.util
from pathlib import Path

from rag_modules.parent_document_materializer import ParentDocumentMaterializer, SourceParent
from rag_modules.parent_document_store import ParentDocumentStore


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("recipe_metadata_coverage", ROOT / "scripts" / "validate_recipe_metadata_coverage.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_coverage_reports_only_metadata_without_parent_body(tmp_path):
    result = ParentDocumentMaterializer().materialize_documents([
        SourceParent("r1", "Recipe", "标题", "正文", {"recipe_methods": [], "unknown_cooking_appliance": False}),
    ])
    path = tmp_path / "pds.sqlite"
    result.write(str(path))
    with ParentDocumentStore.open(path, active_build_id=result.manifest.build_id) as store:
        actual = MODULE.report(store, result.manifest.build_id)
    assert actual["recipe_count"] == 1
    assert actual["coverage"]["recipe_methods"] == 1
    assert actual["coverage"]["total_minutes"] == 0
