from __future__ import annotations

from pathlib import Path

from scripts.validate_pds_milvus_linkage import validate_rows
from rag_modules.parent_document_materializer import ParentDocumentMaterializer, SourceParent
from rag_modules.parent_document_store import ParentDocumentStore


def test_preinsert_linkage_report_covers_every_canonical_chunk(tmp_path: Path):
    result = ParentDocumentMaterializer(chunk_size=40, chunk_overlap=4).materialize_documents(
        [SourceParent("recipe-1", "Recipe", "测试", "正文", {"node_id": "recipe-1"})]
    )
    db_path = tmp_path / "pds.sqlite"
    pointer = tmp_path / "active.json"
    result.write(str(db_path), publish=True, active_pointer=str(pointer))
    with ParentDocumentStore.open(db_path, active_pointer=pointer) as store:
        rows = [
            {
                "chunk_id": chunk.chunk_id,
                "parent_id": chunk.parent_id,
                "chunk_index": chunk.chunk_index,
                "build_id": chunk.build_id,
                "text_hash": chunk.text_hash,
            }
            for chunk in store.iter_chunks(result.manifest.build_id)
        ]
        report = validate_rows(store, result.manifest.build_id, rows)
    assert report["valid"] is True
    assert report["pds_chunk_count"] == report["milvus_row_count"]
