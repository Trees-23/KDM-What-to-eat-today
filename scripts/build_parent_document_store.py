#!/usr/bin/env python3
"""构建或检查版本化 ParentDocumentStore。

默认只从显式 Neo4j 配置读取，不扫描 Markdown，也不触碰 Milvus。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import DEFAULT_CONFIG
from rag_modules.parent_document_materializer import ParentDocumentMaterializer
from rag_modules.parent_document_store import ParentDocumentStore


def _build_output_path(output: str, build_id: str) -> Path:
    path = Path(output).expanduser()
    if path.suffix.lower() == ".sqlite":
        return path
    return path / f"parent_store.{build_id}.sqlite"


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="构建版本化 ParentDocumentStore")
    parser.add_argument("--source", choices=["neo4j"], default="neo4j")
    parser.add_argument("--output", help="SQLite 文件路径或输出目录")
    parser.add_argument("--active-pointer", default=DEFAULT_CONFIG.parent_store_active_pointer)
    parser.add_argument("--build-id")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--activate-existing", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--check-active", action="store_true")
    parser.add_argument("--expected-build")
    return parser


def main() -> int:
    args = _parser().parse_args()
    if args.check_active:
        if not args.output or not args.expected_build:
            raise SystemExit("--check-active 需要同时提供 --output 和 --expected-build")
        with ParentDocumentStore.open(args.output, active_pointer=args.active_pointer) as store:
            if store.active_build_id != args.expected_build:
                raise SystemExit(
                    f"active build 不匹配: {store.active_build_id} != {args.expected_build}"
                )
            print(json.dumps(store.health_check(), ensure_ascii=False, sort_keys=True))
        return 0

    if args.activate_existing:
        if not args.output or not args.expected_build:
            raise SystemExit("--activate-existing 需要同时提供 --output 和 --expected-build")
        ParentDocumentStore.publish_existing_build(args.output, args.expected_build, args.active_pointer)
        print(json.dumps({"status": "activated", "build_id": args.expected_build}, ensure_ascii=False))
        return 0

    if not args.output:
        raise SystemExit("构建需要 --output")
    if args.publish and not args.active_pointer:
        raise SystemExit("--publish 需要 --active-pointer")

    materializer = ParentDocumentMaterializer(
        uri=DEFAULT_CONFIG.neo4j_uri,
        user=DEFAULT_CONFIG.neo4j_user,
        password=DEFAULT_CONFIG.neo4j_password,
        database=DEFAULT_CONFIG.neo4j_database,
        chunk_size=DEFAULT_CONFIG.chunk_size,
        chunk_overlap=DEFAULT_CONFIG.chunk_overlap,
    )
    try:
        result = materializer.materialize_from_neo4j()
        if args.build_id and args.build_id != result.manifest.build_id:
            raise SystemExit(
                f"指定 build_id 与计算值不一致: {args.build_id} != {result.manifest.build_id}"
            )
        output_path = _build_output_path(args.output, result.manifest.build_id)
        if not args.dry_run:
            result.write(
                str(output_path),
                publish=args.publish,
                active_pointer=args.active_pointer if args.publish else None,
            )
        print(
            json.dumps(
                {
                    "build_id": result.manifest.build_id,
                    "source_fingerprint": result.manifest.source_fingerprint,
                    "parents": len(result.parents),
                    "chunks": len(result.chunks),
                    "anchors": len(result.anchors),
                    "output": str(output_path),
                    "dry_run": args.dry_run,
                    "published": bool(args.publish and not args.dry_run),
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0
    finally:
        materializer.close()


if __name__ == "__main__":
    raise SystemExit(main())
