#!/usr/bin/env python3
"""V2 collection verify/build CLI，所有目标必须显式白名单绑定。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from rag_modules.milvus_v2_index import MilvusV2IndexBuilder, validate_v2_collection_name
from rag_modules.parent_document_store import ParentDocumentStore


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", required=True)
    parser.add_argument("--allowed-database", required=True)
    parser.add_argument("--uri", help="Milvus URI；实际创建时必须显式提供")
    parser.add_argument("--collection", required=True)
    parser.add_argument("--allowed-collection", required=True)
    parser.add_argument("--parent-store", required=True)
    parser.add_argument("--parent-store-build", required=True)
    parser.add_argument("--dimension", type=int, default=512)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--verify-only",
        action="store_true",
        help="只校验 PDS source，不连接或读取 Milvus collection",
    )
    mode.add_argument(
        "--verify-existing",
        action="store_true",
        help="只读校验已存在的 V2 collection，不创建或修改 collection",
    )
    parser.add_argument("--vectors-json")
    parser.add_argument("--confirm-create", action="store_true")
    return parser


def _read_vectors(path_value: str, *, dimension: int) -> list[list[float]]:
    path = Path(path_value).expanduser().resolve()
    if not path.is_absolute() or not path.is_file():
        raise ValueError("vectors-json 必须是存在的绝对路径")
    value: Any = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or not value:
        raise ValueError("vectors-json 必须是非空数组")
    vectors: list[list[float]] = []
    for index, vector in enumerate(value):
        if not isinstance(vector, list) or len(vector) != dimension:
            raise ValueError(f"vectors-json 第 {index} 项维度不正确")
        try:
            vectors.append([float(item) for item in vector])
        except (TypeError, ValueError) as error:
            raise ValueError(f"vectors-json 第 {index} 项包含非数值") from error
    return vectors


def _new_client(uri: str, database: str):
    try:
        from pymilvus import MilvusClient
    except ImportError as error:
        raise RuntimeError("实际构建需要安装 pymilvus") from error
    return MilvusClient(uri=uri, db_name=database)


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.database != args.allowed_database:
        raise SystemExit("database 不在白名单")
    if args.collection != args.allowed_collection:
        raise SystemExit("collection 不在白名单")
    validate_v2_collection_name(args.collection, args.parent_store_build)
    path = Path(args.parent_store).expanduser().resolve()
    pointer = path / "parent_store.active" if path.is_dir() else None
    with ParentDocumentStore.open(path, active_build_id=args.parent_store_build, active_pointer=pointer) as store:
        if args.verify_only:
            class VerifyOnlyClient:
                def has_collection(self, **_kwargs):
                    return False
            builder = MilvusV2IndexBuilder(
                VerifyOnlyClient(), parent_store=store, database=args.database,
                collection=args.collection, build_id=args.parent_store_build, dimension=args.dimension,
            )
            print(json.dumps(builder.verify_source(), ensure_ascii=False, sort_keys=True))
            return 0
        if args.verify_existing:
            if not args.uri:
                raise SystemExit("--verify-existing 需要显式提供 --uri")
            vectors = _read_vectors(args.vectors_json, dimension=args.dimension) if args.vectors_json else None
            client = _new_client(args.uri, args.database)
            builder = MilvusV2IndexBuilder(
                client,
                parent_store=store,
                database=args.database,
                collection=args.collection,
                build_id=args.parent_store_build,
                dimension=args.dimension,
            )
            print(
                json.dumps(
                    builder.verify_existing(sample_vector=vectors[0] if vectors else None),
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            return 0
        if not args.confirm_create or not args.vectors_json or not args.uri:
            raise SystemExit("实际创建需要 --confirm-create 和 --vectors-json")
        vectors = _read_vectors(args.vectors_json, dimension=args.dimension)
        client = _new_client(args.uri, args.database)
        builder = MilvusV2IndexBuilder(
            client,
            parent_store=store,
            database=args.database,
            collection=args.collection,
            build_id=args.parent_store_build,
            dimension=args.dimension,
        )
        print(json.dumps(builder.build(vectors, confirm_create=True), ensure_ascii=False, sort_keys=True))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
