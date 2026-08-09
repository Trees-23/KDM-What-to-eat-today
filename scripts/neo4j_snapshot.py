#!/usr/bin/env python3
"""Neo4j staging 图快照的非破坏性导出、校验与恢复守卫。

脚本处理显式的 JSONL 图导出工件，避免在没有经过授权的 Neo4j 目标时猜测连接。
真实环境可由受控的只读导出器生成 ``--source-export``；本脚本不会连接默认数据库。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any


SNAPSHOT_VERSION = "neo4j_snapshot_v1"
_IDENTIFIER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$")


class SnapshotGuardError(ValueError):
    """快照目标、路径或内容未通过安全校验。"""


def _absolute_path(value: str, label: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise SnapshotGuardError(f"{label} 必须是绝对路径")
    return path.resolve()


def _within(path: Path, root: Path, label: str) -> Path:
    try:
        path.relative_to(root)
    except ValueError as error:
        raise SnapshotGuardError(f"{label} 不在允许根目录内") from error
    return path


def validate_database(database: str, allowed_database: str) -> None:
    if database != allowed_database:
        raise SnapshotGuardError("database 不在白名单")
    if database.lower() in {"default", "neo4j", "prod", "production"}:
        raise SnapshotGuardError("禁止对默认或生产数据库执行快照")
    if not _IDENTIFIER.fullmatch(database):
        raise SnapshotGuardError("database 标识符非法")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _read_export(path: Path) -> tuple[list[dict[str, Any]], int, int, str]:
    rows: list[dict[str, Any]] = []
    node_ids: list[str] = []
    node_count = relationship_count = 0
    digest = hashlib.sha256()
    with path.open("r", encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as error:
                raise SnapshotGuardError(f"图导出第 {line_number} 行不是有效 JSON") from error
            if not isinstance(value, dict) or value.get("kind") not in {"node", "relationship"}:
                raise SnapshotGuardError(f"图导出第 {line_number} 行必须声明 kind=node/relationship")
            if value["kind"] == "node":
                node_id = value.get("nodeId")
                if not isinstance(node_id, str) or not node_id:
                    raise SnapshotGuardError(f"图导出第 {line_number} 行缺少 nodeId")
                node_ids.append(node_id)
                node_count += 1
            else:
                if not isinstance(value.get("startNodeId"), str) or not isinstance(value.get("endNodeId"), str):
                    raise SnapshotGuardError(f"图导出第 {line_number} 行缺少关系外键")
                relationship_count += 1
            encoded = (_canonical_json(value) + "\n").encode("utf-8")
            digest.update(encoded)
            rows.append(value)
    if len(node_ids) != len(set(node_ids)):
        raise SnapshotGuardError("图导出包含重复 nodeId")
    sample_hash = hashlib.sha256("\n".join(sorted(node_ids)[:10]).encode("utf-8")).hexdigest()
    return rows, node_count, relationship_count, f"{digest.hexdigest()}:{sample_hash}"


def _atomic_json(path: Path, value: dict[str, Any]) -> None:
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as temporary:
        json.dump(value, temporary, ensure_ascii=False, sort_keys=True, indent=2)
        temporary.write("\n")
        temporary.flush()
        os.fsync(temporary.fileno())
        temporary_path = Path(temporary.name)
    os.replace(temporary_path, path)


def create_snapshot(*, database: str, allowed_database: str, source_export: Path, output: Path, schema: dict[str, Any] | None = None) -> dict[str, Any]:
    validate_database(database, allowed_database)
    source_export = _absolute_path(str(source_export), "source-export")
    output = _absolute_path(str(output), "snapshot-output")
    if not source_export.is_file():
        raise SnapshotGuardError("source-export 不存在或不是文件")
    if output.exists():
        raise SnapshotGuardError("immutable snapshot 输出目录已存在，拒绝覆盖")
    rows, node_count, relationship_count, combined_hash = _read_export(source_export)
    output.mkdir(parents=True, exist_ok=False)
    payload = output / "graph.jsonl"
    payload.write_text("".join(_canonical_json(row) + "\n" for row in rows), encoding="utf-8")
    manifest = {
        "version": SNAPSHOT_VERSION,
        "database": database,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "payload_file": payload.name,
        "payload_sha256": sha256_file(payload),
        "source_export_sha256": sha256_file(source_export),
        "node_count": node_count,
        "relationship_count": relationship_count,
        "sample_node_hash": combined_hash.split(":", 1)[1],
        "export_hash": combined_hash.split(":", 1)[0],
        "schema": schema or {},
        "verified": False,
    }
    _atomic_json(output / "manifest.json", manifest)
    return manifest


def load_manifest(manifest_path: Path, *, allowed_backup_root: Path) -> dict[str, Any]:
    manifest_path = _within(_absolute_path(str(manifest_path), "manifest"), _absolute_path(str(allowed_backup_root), "allowed-backup-root"), "manifest")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SnapshotGuardError("manifest 读取失败") from error
    if not isinstance(manifest, dict) or manifest.get("version") != SNAPSHOT_VERSION:
        raise SnapshotGuardError("manifest 版本非法")
    payload_name = manifest.get("payload_file")
    if not isinstance(payload_name, str) or Path(payload_name).name != payload_name:
        raise SnapshotGuardError("manifest payload_file 非法")
    payload = manifest_path.parent / payload_name
    if not payload.is_file() or sha256_file(payload) != manifest.get("payload_sha256"):
        raise SnapshotGuardError("snapshot payload SHA-256 不一致")
    rows, node_count, relationship_count, combined_hash = _read_export(payload)
    if node_count != manifest.get("node_count") or relationship_count != manifest.get("relationship_count"):
        raise SnapshotGuardError("snapshot 节点/关系计数不一致")
    if combined_hash.split(":", 1)[0] != manifest.get("export_hash") or combined_hash.split(":", 1)[1] != manifest.get("sample_node_hash"):
        raise SnapshotGuardError("snapshot 样本或导出摘要不一致")
    return manifest


def verify_snapshot(*, database: str, allowed_database: str, manifest_path: Path, allowed_backup_root: Path, csv_manifest: Path | None = None) -> dict[str, Any]:
    validate_database(database, allowed_database)
    manifest = load_manifest(manifest_path, allowed_backup_root=allowed_backup_root)
    if manifest.get("database") != database:
        raise SnapshotGuardError("manifest database 与验证目标不一致")
    csv_sha = sha256_file(_absolute_path(str(csv_manifest), "csv-manifest")) if csv_manifest else None
    record = {
        "status": "verified",
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "database": database,
        "manifest_sha256": sha256_file(_absolute_path(str(manifest_path), "manifest")),
        "csv_manifest_sha256": csv_sha,
    }
    _atomic_json(Path(manifest_path).resolve().parent / "verify.json", record)
    return record


def restore_snapshot(*, manifest_path: Path, target_database: str, allowed_database: str, allowed_backup_root: Path, restore_output: Path, allowed_restore_root: Path) -> dict[str, Any]:
    validate_database(target_database, allowed_database)
    manifest = load_manifest(manifest_path, allowed_backup_root=allowed_backup_root)
    if manifest.get("database") == target_database:
        raise SnapshotGuardError("恢复目标必须是新的隔离 database")
    restore_output = _within(_absolute_path(str(restore_output), "restore-output"), _absolute_path(str(allowed_restore_root), "allowed-restore-root"), "restore-output")
    if restore_output.exists():
        raise SnapshotGuardError("restore-output 已存在，拒绝覆盖")
    source_payload = Path(manifest_path).resolve().parent / str(manifest["payload_file"])
    restore_output.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(source_payload, restore_output / "graph.jsonl")
    restored = dict(manifest, database=target_database, restored_from_database=manifest["database"], verified=False)
    _atomic_json(restore_output / "manifest.json", restored)
    return restored


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    create = subparsers.add_parser("create")
    create.add_argument("--database", required=True)
    create.add_argument("--allowed-database", required=True)
    create.add_argument("--source-export", required=True, type=Path)
    create.add_argument("--output", required=True, type=Path)
    create.add_argument("--schema", type=Path)
    verify = subparsers.add_parser("verify")
    verify.add_argument("--database", required=True)
    verify.add_argument("--allowed-database", required=True)
    verify.add_argument("--manifest", required=True, type=Path)
    verify.add_argument("--allowed-backup-root", required=True, type=Path)
    verify.add_argument("--csv-manifest", type=Path)
    restore = subparsers.add_parser("restore")
    restore.add_argument("--manifest", required=True, type=Path)
    restore.add_argument("--target-database", required=True)
    restore.add_argument("--allowed-database", required=True)
    restore.add_argument("--allowed-backup-root", required=True, type=Path)
    restore.add_argument("--restore-output", required=True, type=Path)
    restore.add_argument("--allowed-restore-root", required=True, type=Path)
    args = parser.parse_args(argv)
    if args.command == "create":
        schema = json.loads(args.schema.read_text(encoding="utf-8")) if args.schema else None
        result = create_snapshot(database=args.database, allowed_database=args.allowed_database, source_export=args.source_export, output=args.output, schema=schema)
    elif args.command == "verify":
        result = verify_snapshot(database=args.database, allowed_database=args.allowed_database, manifest_path=args.manifest, allowed_backup_root=args.allowed_backup_root, csv_manifest=args.csv_manifest)
    else:
        result = restore_snapshot(manifest_path=args.manifest, target_database=args.target_database, allowed_database=args.allowed_database, allowed_backup_root=args.allowed_backup_root, restore_output=args.restore_output, allowed_restore_root=args.allowed_restore_root)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
