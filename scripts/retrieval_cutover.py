#!/usr/bin/env python3
"""受保护环境中的联合 retrieval artifact 原子切换守卫。"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from rag_modules.milvus_v2_index import RetrievalArtifactManifest, validate_v2_collection_name


class CutoverGuardError(ValueError):
    """切换目标、审批或路径未通过安全校验。"""


def _absolute_path(value: str, label: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise CutoverGuardError(f"{label} 必须是绝对路径")
    return path.resolve()


def _within(path: Path, root: Path, label: str) -> Path:
    try:
        path.relative_to(root)
    except ValueError as error:
        raise CutoverGuardError(f"{label} 不在允许根目录内") from error
    return path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _parse_expiry(value: str) -> datetime:
    try:
        expiry = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise CutoverGuardError("审批过期时间不是合法 ISO-8601") from error
    if expiry.tzinfo is None:
        raise CutoverGuardError("审批过期时间必须带时区")
    return expiry.astimezone(timezone.utc)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", required=True)
    parser.add_argument("--allowed-database", required=True)
    parser.add_argument("--from", dest="from_collection", required=True)
    parser.add_argument("--to", dest="to_collection", required=True)
    parser.add_argument("--allowed-from-collection", required=True)
    parser.add_argument("--allowed-to-collection", required=True)
    parser.add_argument("--parent-store-build", required=True)
    parser.add_argument("--artifact-manifest", required=True)
    parser.add_argument("--approval-record", required=True)
    parser.add_argument("--backup-manifest", required=True)
    parser.add_argument("--expected-backup-sha256", required=True)
    parser.add_argument("--active-pointer", required=True)
    parser.add_argument("--allowed-backup-root", required=True)
    parser.add_argument("--allowed-artifact-root", required=True)
    parser.add_argument("--allowed-approval-root", required=True)
    parser.add_argument("--allowed-active-root", required=True)
    parser.add_argument("--environment", required=True)
    parser.add_argument("--protected-environment", required=True)
    parser.add_argument("--confirm-cutover", action="store_true")
    return parser


def _validate(args: argparse.Namespace) -> RetrievalArtifactManifest:
    if args.database != args.allowed_database:
        raise CutoverGuardError("database 不在白名单")
    if args.from_collection == args.to_collection:
        raise CutoverGuardError("from/to collection 不能相同")
    if args.from_collection != args.allowed_from_collection or args.to_collection != args.allowed_to_collection:
        raise CutoverGuardError("from/to collection 不在白名单")
    validate_v2_collection_name(args.to_collection, args.parent_store_build)
    if args.environment != args.protected_environment:
        raise CutoverGuardError("当前环境不是受保护发布环境")
    runtime_environment = os.getenv("RETRIEVAL_RELEASE_ENVIRONMENT")
    if runtime_environment != args.protected_environment:
        raise CutoverGuardError("RETRIEVAL_RELEASE_ENVIRONMENT 未绑定受保护环境")

    artifact_path = _within(
        _absolute_path(args.artifact_manifest, "artifact-manifest"),
        _absolute_path(args.allowed_artifact_root, "allowed-artifact-root"),
        "artifact-manifest",
    )
    approval_path = _within(
        _absolute_path(args.approval_record, "approval-record"),
        _absolute_path(args.allowed_approval_root, "allowed-approval-root"),
        "approval-record",
    )
    backup_path = _within(
        _absolute_path(args.backup_manifest, "backup-manifest"),
        _absolute_path(args.allowed_backup_root, "allowed-backup-root"),
        "backup-manifest",
    )
    if len(args.expected_backup_sha256) != 64 or any(char not in "0123456789abcdef" for char in args.expected_backup_sha256.lower()):
        raise CutoverGuardError("expected-backup-sha256 必须是 64 位十六进制摘要")
    if not backup_path.is_file() or _sha256(backup_path) != args.expected_backup_sha256:
        raise CutoverGuardError("backup manifest SHA-256 与预期不一致")
    manifest = RetrievalArtifactManifest.read(artifact_path)
    manifest.validate_runtime(
        pds_build_id=args.parent_store_build,
        milvus_database=args.database,
        milvus_collection=args.to_collection,
        schema_hash=manifest.milvus_schema_hash,
    )
    approval = json.loads(approval_path.read_text(encoding="utf-8"))
    if not isinstance(approval, dict):
        raise CutoverGuardError("审批记录必须是 JSON 对象")
    required = {
        "from_collection": args.from_collection,
        "to_collection": args.to_collection,
        "database": args.database,
        "pds_build_id": args.parent_store_build,
        "backup_sha256": args.expected_backup_sha256,
        "environment": args.protected_environment,
    }
    for key, expected in required.items():
        if approval.get(key) != expected:
            raise CutoverGuardError(f"审批记录与切换参数不一致: {key}")
    if not approval.get("approved_by") or not approval.get("second_approver") or not approval.get("change_id"):
        raise CutoverGuardError("审批记录缺少双人审批或变更单号")
    if _parse_expiry(str(approval.get("expires_at", ""))) <= datetime.now(timezone.utc):
        raise CutoverGuardError("审批记录已过期")
    if not args.confirm_cutover:
        raise CutoverGuardError("切换需要 --confirm-cutover")
    pointer = _within(
        _absolute_path(args.active_pointer, "active-pointer"),
        _absolute_path(args.allowed_active_root, "allowed-active-root"),
        "active-pointer",
    )
    if pointer.exists() and pointer.is_dir():
        raise CutoverGuardError("active-pointer 不能是目录")
    return manifest


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    manifest = _validate(args)
    pointer = _within(
        _absolute_path(args.active_pointer, "active-pointer"),
        _absolute_path(args.allowed_active_root, "allowed-active-root"),
        "active-pointer",
    )
    pointer.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_atomic(pointer)
    print(json.dumps({"status": "cutover", "database": args.database, "collection": args.to_collection, "rollback_collection": manifest.rollback_collection}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
