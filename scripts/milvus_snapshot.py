#!/usr/bin/env python3
"""受白名单保护的 Milvus 逻辑快照、恢复与检索验证。

Milvus standalone 没有可由 ``MilvusClient`` 直接调用的原子 collection dump
API。本脚本因此导出完整行（包括向量）和冻结 schema/index 描述；恢复始终
写入一个从未存在过的 ``*_restore_*`` collection，绝不覆盖源 collection。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any, Iterable, Mapping


SNAPSHOT_VERSION = "milvus_snapshot_v2"
_IDENTIFIER = re.compile(r"^[A-Za-z0-9_]{1,255}$")


class SnapshotTargetError(ValueError):
    """快照、恢复或路径不在显式允许范围。"""


def _absolute_path(value: str, label: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise SnapshotTargetError(f"{label} 必须是绝对路径")
    return path.resolve()


def _within(path: Path, root: Path, label: str) -> Path:
    try:
        path.relative_to(root)
    except ValueError as error:
        raise SnapshotTargetError(f"{label} 不在允许根目录内") from error
    return path


def validate_target(database: str, collection: str, *, allowed_database: str, allowed_collection: str) -> None:
    if database != allowed_database or collection != allowed_collection:
        raise SnapshotTargetError("database/collection 不在允许的快照白名单中")
    if not _IDENTIFIER.fullmatch(database) or not _IDENTIFIER.fullmatch(collection):
        raise SnapshotTargetError("database/collection 含非法字符")


def validate_backup_path(value: str, allowed_root: str, label: str) -> Path:
    root = _absolute_path(allowed_root, "allowed-backup-root")
    return _within(_absolute_path(value, label), root, label)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def text_hash(value: Any) -> str:
    return hashlib.sha256(str(value or "").encode("utf-8")).hexdigest()


def _json_safe(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    # pymilvus 通常把 FLOAT_VECTOR 返回为 numpy.float32 列表。
    item_method = getattr(value, "item", None)
    if callable(item_method):
        return _json_safe(item_method())
    name = getattr(value, "name", None)
    if name:
        return str(name)
    return value


def _canonical_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _schema_fingerprint(schema: Mapping[str, Any]) -> str:
    structural = {
        "fields": schema.get("fields", []),
        "auto_id": bool(schema.get("auto_id", False)),
        "enable_dynamic_field": bool(schema.get("enable_dynamic_field", False)),
    }
    return hashlib.sha256(_canonical_json(structural).encode("utf-8")).hexdigest()


def _schema_fields(description: Mapping[str, Any]) -> list[dict[str, Any]]:
    result = []
    for field in description.get("fields", []):
        item = dict(field)
        field_type = item.get("type", "")
        result.append(
            {
                "name": str(item.get("name", "")),
                "type": str(getattr(field_type, "name", field_type)).rsplit(".", 1)[-1],
                "params": {str(key): str(value) for key, value in dict(item.get("params", {})).items()},
                "is_primary": bool(item.get("is_primary", False)),
            }
        )
    if not result or not any(field["is_primary"] for field in result):
        raise SnapshotTargetError("collection schema 缺少主键字段")
    return result


def _primary_field(fields: Iterable[Mapping[str, Any]]) -> Mapping[str, Any]:
    return next(field for field in fields if field.get("is_primary"))


def _query_filter(primary: Mapping[str, Any]) -> str:
    name = str(primary["name"])
    if not _IDENTIFIER.fullmatch(name):
        raise SnapshotTargetError("主键字段名非法")
    return f'{name} != ""' if primary["type"] == "VARCHAR" else f"{name} >= 0"


def _export_rows(client: Any, collection: str, fields: list[dict[str, Any]]) -> list[dict[str, Any]]:
    primary = _primary_field(fields)
    field_names = [field["name"] for field in fields]
    iterator = client.query_iterator(
        collection,
        filter=_query_filter(primary),
        output_fields=field_names,
        batch_size=500,
        limit=-1,
    )
    rows: list[dict[str, Any]] = []
    try:
        while True:
            batch = iterator.next()
            if not batch:
                break
            rows.extend(_json_safe(dict(row)) for row in batch)
    finally:
        iterator.close()
    primary_name = str(primary["name"])
    rows.sort(key=lambda row: str(row.get(primary_name, "")))
    if len({str(row.get(primary_name, "")) for row in rows}) != len(rows):
        raise SnapshotTargetError("快照导出包含重复或缺失主键")
    return rows


def _write_rows(path: Path, rows: Iterable[Mapping[str, Any]]) -> str:
    digest = hashlib.sha256()
    with path.open("w", encoding="utf-8", newline="\n") as output:
        for row in rows:
            encoded = (_canonical_json(dict(row)) + "\n").encode("utf-8")
            output.write(encoded.decode("utf-8"))
            digest.update(encoded)
        output.flush()
        os.fsync(output.fileno())
    return digest.hexdigest()


def _read_rows(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            try:
                row = json.loads(line)
            except json.JSONDecodeError as error:
                raise SnapshotTargetError(f"snapshot payload 第 {line_number} 行非法") from error
            if not isinstance(row, Mapping):
                raise SnapshotTargetError(f"snapshot payload 第 {line_number} 行不是对象")
            rows.append(dict(row))
    return rows


def _row_hashes_sha256(rows: Iterable[Mapping[str, Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update(hashlib.sha256(_canonical_json(dict(row)).encode("utf-8")).digest())
    return digest.hexdigest()


def _atomic_json(path: Path, value: Mapping[str, Any]) -> None:
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as temporary:
        json.dump(value, temporary, ensure_ascii=False, sort_keys=True, indent=2)
        temporary.write("\n")
        temporary.flush()
        os.fsync(temporary.fileno())
        temporary_path = Path(temporary.name)
    os.replace(temporary_path, path)


def _new_client(uri: str, database: str):
    if not uri:
        raise SnapshotTargetError("必须显式提供 Milvus URI")
    try:
        from pymilvus import MilvusClient
    except ImportError as error:
        raise RuntimeError("Milvus 快照需要安装 pymilvus") from error
    return MilvusClient(uri=uri, db_name=database)


def create_snapshot(client: Any, *, database: str, collection: str, output: Path) -> dict[str, Any]:
    if output.exists():
        raise SnapshotTargetError("immutable backup 输出目录已存在，拒绝覆盖")
    description = _json_safe(client.describe_collection(collection))
    fields = _schema_fields(description)
    row_count = int(client.get_collection_stats(collection).get("row_count", -1))
    rows = _export_rows(client, collection, fields)
    if row_count != len(rows):
        raise SnapshotTargetError("Milvus 行数与导出行数不一致，拒绝生成不完整快照")
    indexes = [_json_safe(client.describe_index(collection, index)) for index in client.list_indexes(collection)]
    output.mkdir(parents=True, exist_ok=False)
    payload = output / "rows.jsonl"
    payload_sha256 = _write_rows(payload, rows)
    primary = _primary_field(fields)
    primary_name = str(primary["name"])
    samples = [
        {"id": str(row[primary_name]), "text_hash": text_hash(row.get("text", ""))}
        for row in rows[: min(10, len(rows))]
    ]
    schema_payload = {
        "fields": fields,
        "auto_id": bool(description.get("auto_id", False)),
        "enable_dynamic_field": bool(description.get("enable_dynamic_field", False)),
        "description": str(description.get("description", "")),
    }
    manifest = {
        "version": SNAPSHOT_VERSION,
        "database": database,
        "collection": collection,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "payload_file": payload.name,
        "payload_sha256": payload_sha256,
        "row_hashes_sha256": _row_hashes_sha256(rows),
        "row_count": len(rows),
        "schema": schema_payload,
        "schema_sha256": _schema_fingerprint(schema_payload),
        "indexes": indexes,
        "samples": samples,
    }
    _atomic_json(output / "manifest.json", manifest)
    return manifest


def load_manifest(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]], Path]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(manifest, Mapping) or manifest.get("version") != SNAPSHOT_VERSION:
        raise SnapshotTargetError("snapshot manifest 版本非法")
    payload_name = manifest.get("payload_file")
    if not isinstance(payload_name, str) or Path(payload_name).name != payload_name:
        raise SnapshotTargetError("snapshot payload 文件名非法")
    payload = path.parent / payload_name
    if not payload.is_file() or sha256_file(payload) != manifest.get("payload_sha256"):
        raise SnapshotTargetError("snapshot payload SHA-256 不一致")
    rows = _read_rows(payload)
    if len(rows) != int(manifest.get("row_count", -1)):
        raise SnapshotTargetError("snapshot payload 行数不一致")
    if _row_hashes_sha256(rows) != manifest.get("row_hashes_sha256"):
        raise SnapshotTargetError("snapshot 行哈希不一致")
    return dict(manifest), rows, payload


def verify_snapshot(client: Any, manifest: Mapping[str, Any], rows: list[dict[str, Any]], *, database: str, collection: str, check_search: bool) -> dict[str, Any]:
    source_collection = str(manifest.get("collection", ""))
    if manifest.get("database") != database or not (
        collection == source_collection or collection.startswith(f"{source_collection}_restore_")
    ):
        raise SnapshotTargetError("snapshot manifest 与验证目标不一致")
    description = _json_safe(client.describe_collection(collection))
    actual_schema = {
        "fields": _schema_fields(description),
        "auto_id": bool(description.get("auto_id", False)),
        "enable_dynamic_field": bool(description.get("enable_dynamic_field", False)),
        "description": str(description.get("description", "")),
    }
    if _schema_fingerprint(actual_schema) != manifest.get("schema_sha256"):
        raise SnapshotTargetError("目标 collection schema 与 snapshot 不一致")
    if int(client.get_collection_stats(collection).get("row_count", -1)) != len(rows):
        raise SnapshotTargetError("目标 collection 行数与 snapshot 不一致")
    fields = list(manifest["schema"]["fields"])
    primary_name = str(_primary_field(fields)["name"])
    for sample in manifest.get("samples", []):
        found = client.query(collection, ids=[sample["id"]], output_fields=[primary_name, "text"])
        if len(found) != 1 or text_hash(found[0].get("text", "")) != sample["text_hash"]:
            raise SnapshotTargetError("目标 collection 抽样 text_hash 与 snapshot 不一致")
    if check_search:
        vector_name = next((field["name"] for field in fields if field["type"] == "FLOAT_VECTOR"), None)
        if not vector_name or not rows or vector_name not in rows[0]:
            raise SnapshotTargetError("snapshot 没有可用于检索验证的向量")
        result = client.search(
            collection_name=collection,
            data=[rows[0][vector_name]],
            anns_field=vector_name,
            limit=1,
            output_fields=[primary_name],
            search_params={"metric_type": "COSINE", "params": {"ef": 64}},
        )
        if not result or not result[0]:
            raise SnapshotTargetError("目标 collection 检索验证没有返回命中")
    return {"status": "verified", "database": database, "collection": collection, "row_count": len(rows)}


def _restore_schema(manifest: Mapping[str, Any]):
    try:
        from pymilvus import DataType, MilvusClient
    except ImportError as error:
        raise RuntimeError("Milvus 恢复需要安装 pymilvus") from error
    schema_info = manifest["schema"]
    schema = MilvusClient.create_schema(
        auto_id=bool(schema_info["auto_id"]),
        enable_dynamic_field=bool(schema_info["enable_dynamic_field"]),
    )
    for field in schema_info["fields"]:
        datatype = getattr(DataType, field["type"], None)
        if datatype is None:
            raise SnapshotTargetError(f"不支持恢复的数据类型: {field['type']}")
        options: dict[str, Any] = {"is_primary": bool(field["is_primary"])}
        params = field.get("params", {})
        if field["type"] == "VARCHAR":
            options["max_length"] = int(params["max_length"])
        if field["type"].endswith("_VECTOR"):
            options["dim"] = int(params["dim"])
        schema.add_field(field_name=field["name"], datatype=datatype, **options)
    return schema


def restore_snapshot(client: Any, manifest: Mapping[str, Any], rows: list[dict[str, Any]], *, target_collection: str) -> dict[str, Any]:
    source_collection = str(manifest["collection"])
    if target_collection == source_collection or not target_collection.startswith(f"{source_collection}_restore_"):
        raise SnapshotTargetError("恢复目标必须是源 collection 对应的全新 restore collection")
    if client.has_collection(collection_name=target_collection):
        raise SnapshotTargetError("恢复目标 collection 已存在，拒绝覆盖")
    schema = _restore_schema(manifest)
    client.create_collection(
        collection_name=target_collection,
        schema=schema,
        consistency_level="Strong",
        description=str(manifest["schema"].get("description", "")),
    )
    for start in range(0, len(rows), 500):
        client.insert(collection_name=target_collection, data=rows[start : start + 500])
    client.flush(collection_name=target_collection)
    index_params = client.prepare_index_params()
    for index in manifest.get("indexes", []):
        if not index.get("field_name") or not index.get("index_type"):
            continue
        params = {key: value for key, value in index.items() if key in {"M", "efConstruction", "nlist"}}
        index_params.add_index(
            field_name=index["field_name"],
            index_type=index["index_type"],
            metric_type=index.get("metric_type", "COSINE"),
            params=params,
        )
    client.create_index(collection_name=target_collection, index_params=index_params)
    client.load_collection(collection_name=target_collection)
    return {"status": "restored", "collection": target_collection, "row_count": len(rows)}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create")
    create.add_argument("--uri", required=True)
    create.add_argument("--database", required=True)
    create.add_argument("--collection", required=True)
    create.add_argument("--output", required=True)
    create.add_argument("--allowed-backup-root", required=True)
    create.add_argument("--allowed-database", required=True)
    create.add_argument("--allowed-collection", required=True)
    create.add_argument("--confirm-create", action="store_true")
    verify = sub.add_parser("verify")
    verify.add_argument("--uri", required=True)
    verify.add_argument("--manifest", required=True)
    verify.add_argument("--allowed-backup-root", required=True)
    verify.add_argument("--database", required=True)
    verify.add_argument("--collection", required=True)
    verify.add_argument("--allowed-database", required=True)
    verify.add_argument("--allowed-collection", required=True)
    verify.add_argument("--check-search", action="store_true")
    restore = sub.add_parser("restore")
    restore.add_argument("--uri", required=True)
    restore.add_argument("--manifest", required=True)
    restore.add_argument("--allowed-backup-root", required=True)
    restore.add_argument("--target-database", required=True)
    restore.add_argument("--target-collection", required=True)
    restore.add_argument("--allowed-database", required=True)
    restore.add_argument("--allowed-collection", required=True)
    restore.add_argument("--confirm-restore", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "create":
        validate_target(args.database, args.collection, allowed_database=args.allowed_database, allowed_collection=args.allowed_collection)
        output = validate_backup_path(args.output, args.allowed_backup_root, "output")
        if not args.confirm_create:
            raise SystemExit("创建快照需要 --confirm-create")
        print(json.dumps({"action": "create", "database": args.database, "collection": args.collection, "output": str(output)}, ensure_ascii=False))
        result = create_snapshot(_new_client(args.uri, args.database), database=args.database, collection=args.collection, output=output)
        print(json.dumps({"status": "created", "manifest": str(output / "manifest.json"), "payload_sha256": result["payload_sha256"]}, ensure_ascii=False))
        return 0
    manifest_path = validate_backup_path(args.manifest, args.allowed_backup_root, "manifest")
    manifest, rows, _payload = load_manifest(manifest_path)
    if args.command == "verify":
        validate_target(args.database, args.collection, allowed_database=args.allowed_database, allowed_collection=args.allowed_collection)
        result = verify_snapshot(
            _new_client(args.uri, args.database),
            manifest,
            rows,
            database=args.database,
            collection=args.collection,
            check_search=args.check_search,
        )
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0
    validate_target(args.target_database, args.target_collection, allowed_database=args.allowed_database, allowed_collection=args.allowed_collection)
    if manifest.get("database") != args.target_database:
        raise SystemExit("restore target database 必须与 snapshot database 一致")
    if not args.confirm_restore:
        raise SystemExit("恢复需要 --confirm-restore")
    print(json.dumps({"action": "restore", "database": args.target_database, "collection": args.target_collection}, ensure_ascii=False))
    result = restore_snapshot(
        _new_client(args.uri, args.target_database), manifest, rows, target_collection=args.target_collection
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
