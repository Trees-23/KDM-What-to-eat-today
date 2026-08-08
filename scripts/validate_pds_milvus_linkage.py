#!/usr/bin/env python3
"""校验 PDS CanonicalChunk 与 Milvus V2 行的 build/linkage。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from rag_modules.parent_document_store import ParentDocumentStore


def validate_rows(store: ParentDocumentStore, build_id: str, rows: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    chunks = list(store.iter_chunks(build_id))
    expected = {chunk.chunk_id: chunk for chunk in chunks}
    missing: list[str] = []
    mismatched: list[str] = []
    seen: set[str] = set()
    counts: dict[str, int] = {}
    for row in rows:
        chunk_id = str(row.get("chunk_id", row.get("id", "")))
        seen.add(chunk_id)
        counts[chunk_id] = counts.get(chunk_id, 0) + 1
        chunk = expected.get(chunk_id)
        if chunk is None:
            missing.append(chunk_id)
            continue
        if any(
            str(row.get(name, "")) != str(getattr(chunk, name))
            for name in ("parent_id", "build_id", "text_hash")
        ) or int(row.get("chunk_index", -1)) != chunk.chunk_index:
            mismatched.append(chunk_id)
    report = {
        "build_id": build_id,
        "pds_chunk_count": len(chunks),
        "milvus_row_count": sum(counts.values()),
        "matched_count": sum(1 for chunk_id, count in counts.items() if count == 1 and chunk_id in expected and chunk_id not in mismatched),
        "missing_rows": sorted(set(missing)),
        "mismatched_rows": sorted(set(mismatched)),
        "duplicate_rows": sorted(chunk_id for chunk_id, count in counts.items() if count > 1),
        "unexpected_rows": sorted(chunk_id for chunk_id in seen if chunk_id not in expected),
    }
    report["valid"] = (
        report["pds_chunk_count"] == report["milvus_row_count"]
        and not report["missing_rows"]
        and not report["mismatched_rows"]
        and not report["duplicate_rows"]
        and not report["unexpected_rows"]
    )
    return report


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-store", required=True)
    parser.add_argument("--build", required=True)
    parser.add_argument("--mode", choices=("preinsert", "postinsert"), required=True)
    parser.add_argument("--rows-json", help="postinsert 使用的脱敏行 JSON 文件")
    parser.add_argument("--uri")
    parser.add_argument("--database")
    parser.add_argument("--collection")
    parser.add_argument("--allowed-database")
    parser.add_argument("--allowed-collection")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    path = Path(args.parent_store).expanduser().resolve()
    pointer = path / "parent_store.active" if path.is_dir() else None
    with ParentDocumentStore.open(path, active_build_id=args.build, active_pointer=pointer) as store:
        if args.mode == "preinsert":
            rows = ({
                "chunk_id": chunk.chunk_id,
                "parent_id": chunk.parent_id,
                "chunk_index": chunk.chunk_index,
                "build_id": chunk.build_id,
                "text_hash": chunk.text_hash,
            } for chunk in store.iter_chunks(args.build))
        else:
            if args.rows_json:
                rows = json.loads(Path(args.rows_json).read_text(encoding="utf-8"))
                if not isinstance(rows, list):
                    raise SystemExit("rows-json 必须是数组")
            elif all((args.uri, args.database, args.collection, args.allowed_database, args.allowed_collection)):
                if args.database != args.allowed_database or args.collection != args.allowed_collection:
                    raise SystemExit("postinsert database/collection 不在白名单")
                try:
                    from pymilvus import MilvusClient
                except ImportError as error:
                    raise SystemExit("postinsert 真实校验需要 pymilvus") from error
                client = MilvusClient(uri=args.uri, db_name=args.database)
                iterator = client.query_iterator(
                    args.collection,
                    filter='id != ""',
                    output_fields=["id", "parent_id", "chunk_index", "build_id", "text_hash"],
                    batch_size=500,
                    limit=-1,
                )
                queried: list[dict[str, Any]] = []
                try:
                    while True:
                        batch = iterator.next()
                        if not batch:
                            break
                        queried.extend(dict(row) for row in batch)
                finally:
                    iterator.close()
                rows = queried
            else:
                raise SystemExit("postinsert 必须提供 rows-json，或完整的 Milvus URI/database/collection 白名单")
        report = validate_rows(store, args.build, rows)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
