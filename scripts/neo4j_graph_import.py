#!/usr/bin/env python3
"""Neo4j 图 CSV staging 导入的白名单、备份和审批守卫。

``--dry-run`` 只校验 CSV；``--apply`` 在所有备份/审批条件通过后仍要求显式的
Neo4j 连接参数。没有真实 staging 目标时脚本会在连接前失败，不会自行启动服务或
写入默认数据库。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# 支持文档约定的 ``python scripts/neo4j_graph_import.py`` 调用方式。
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.neo4j_snapshot import SnapshotGuardError, _absolute_path, _within, load_manifest, sha256_file, validate_database
from scripts.validate_recipe_graph_csv import validate_artifact


class Neo4jImportGuardError(ValueError):
    """导入目标、CSV、备份或审批记录未通过守卫。"""


_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _read_json(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise Neo4jImportGuardError(f"{label} 不是有效 JSON") from error
    if not isinstance(value, dict):
        raise Neo4jImportGuardError(f"{label} 必须是 JSON 对象")
    return value


def _csv_manifest_sha(csv_dir: Path) -> str:
    manifest_path = csv_dir / "recipe-build-manifest.json"
    if not manifest_path.is_file():
        raise Neo4jImportGuardError("CSV 目录缺少 recipe-build-manifest.json")
    return sha256_file(manifest_path)


def _approval_valid(path: Path, root: Path, *, database: str, csv_sha: str, backup_sha: str, batch_size: int) -> None:
    approval_path = _within(_absolute_path(str(path), "approval-record"), _absolute_path(str(root), "allowed-approval-root"), "approval-record")
    approval = _read_json(approval_path, "approval-record")
    required = {
        "database": database,
        "csv_manifest_sha256": csv_sha,
        "backup_sha256": backup_sha,
        "batch_size": batch_size,
    }
    for key, expected in required.items():
        if approval.get(key) != expected:
            raise Neo4jImportGuardError(f"审批记录与导入参数不一致: {key}")
    if not approval.get("approved_by") or not approval.get("change_id"):
        raise Neo4jImportGuardError("审批记录缺少 approved_by 或 change_id")
    try:
        expires_at = datetime.fromisoformat(str(approval.get("expires_at", "")).replace("Z", "+00:00"))
    except ValueError as error:
        raise Neo4jImportGuardError("审批过期时间不是合法 ISO-8601") from error
    if expires_at.tzinfo is None or expires_at.astimezone(timezone.utc) <= datetime.now(timezone.utc):
        raise Neo4jImportGuardError("审批记录已过期")


def validate_import(*, database: str, allowed_database: str, csv_dir: Path, allowed_csv_root: Path, apply: bool, backup_manifest: Path | None = None, backup_root: Path | None = None, expected_backup_sha256: str | None = None, approval_record: Path | None = None, allowed_approval_root: Path | None = None, batch_size: int = 500) -> dict[str, Any]:
    try:
        validate_database(database, allowed_database)
    except SnapshotGuardError as error:
        raise Neo4jImportGuardError(str(error)) from error
    csv_path = _within(_absolute_path(str(csv_dir), "csv-dir"), _absolute_path(str(allowed_csv_root), "allowed-csv-root"), "csv-dir")
    if not csv_path.is_dir():
        raise Neo4jImportGuardError("csv-dir 不存在或不是目录")
    if batch_size < 1 or batch_size > 1000:
        raise Neo4jImportGuardError("batch-size 必须在 1..1000")
    report = validate_artifact(csv_path, strict=True)
    if not report.get("valid"):
        raise Neo4jImportGuardError("CSV 严格校验未通过")
    csv_sha = _csv_manifest_sha(csv_path)
    result: dict[str, Any] = {"database": database, "csv_dir": str(csv_path), "csv_manifest_sha256": csv_sha, "batch_size": batch_size, "node_count": report["node_count"], "relationship_count": report["relationship_count"]}
    if not apply:
        result["status"] = "dry_run"
        return result
    if not backup_manifest or not backup_root or not expected_backup_sha256 or not approval_record or not allowed_approval_root:
        raise Neo4jImportGuardError("apply 必须提供 backup-manifest、backup-root、expected-backup-sha256 和 approval-record")
    backup_path = _within(_absolute_path(str(backup_manifest), "backup-manifest"), _absolute_path(str(backup_root), "backup-root"), "backup-manifest")
    if not _SHA256.fullmatch(expected_backup_sha256.lower()) or sha256_file(backup_path) != expected_backup_sha256.lower():
        raise Neo4jImportGuardError("backup manifest SHA-256 与预期不一致")
    manifest = load_manifest(backup_path, allowed_backup_root=_absolute_path(str(backup_root), "backup-root"))
    if manifest.get("database") != database:
        raise Neo4jImportGuardError("backup manifest 未绑定同一 staging database")
    verify_path = backup_path.parent / "verify.json"
    verify = _read_json(verify_path, "backup verify record") if verify_path.is_file() else {}
    if verify.get("status") != "verified" or verify.get("manifest_sha256") != expected_backup_sha256.lower() or verify.get("database") != database or verify.get("csv_manifest_sha256") != csv_sha:
        raise Neo4jImportGuardError("backup verify record 缺失、未验证或未绑定同一 CSV manifest")
    _approval_valid(approval_record, allowed_approval_root, database=database, csv_sha=csv_sha, backup_sha=expected_backup_sha256.lower(), batch_size=batch_size)
    result["status"] = "guarded_apply_ready"
    result["backup_manifest_sha256"] = expected_backup_sha256.lower()
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", required=True)
    parser.add_argument("--allowed-database", required=True)
    parser.add_argument("--csv-dir", required=True, type=Path)
    parser.add_argument("--allowed-csv-root", required=True, type=Path)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    parser.add_argument("--backup-root", type=Path)
    parser.add_argument("--backup-manifest", type=Path)
    parser.add_argument("--expected-backup-sha256")
    parser.add_argument("--batch-size", type=int, default=500)
    parser.add_argument("--approval-record", type=Path)
    parser.add_argument("--allowed-approval-root", type=Path)
    parser.add_argument("--neo4j-uri")
    args = parser.parse_args(argv)
    result = validate_import(database=args.database, allowed_database=args.allowed_database, csv_dir=args.csv_dir, allowed_csv_root=args.allowed_csv_root, apply=args.apply, backup_manifest=args.backup_manifest, backup_root=args.backup_root, expected_backup_sha256=args.expected_backup_sha256, approval_record=args.approval_record, allowed_approval_root=args.allowed_approval_root, batch_size=args.batch_size)
    if args.apply:
        raise Neo4jImportGuardError("真实 Neo4j apply 尚未实现；守卫预检不会连接、导入或报告成功")
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
