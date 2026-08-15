from __future__ import annotations

import hashlib
import json
import sys
import types
from datetime import datetime, timedelta, timezone

import pytest

from rag_modules.milvus_v2_index import ArtifactMismatchError, RetrievalArtifactManifest
from scripts import milvus_snapshot, retrieval_cutover


def _manifest():
    return RetrievalArtifactManifest(
        pds_build_id="pds_build123",
        pds_manifest_sha256="pds-hash",
        milvus_database="default",
        milvus_collection="cooking_knowledge_v2_pds_build1",
        milvus_schema_hash="schema-hash",
        milvus_build_id="pds_build123",
        created_at="2026-08-09T00:00:00+00:00",
        rollback_database="default",
        rollback_collection="cooking_knowledge",
        rollback_pds_build="pds_old",
    )


def test_manifest_round_trip_and_atomic_write(tmp_path):
    manifest = _manifest()
    path = manifest.write_atomic(tmp_path / "retrieval_artifact_manifest.json")
    loaded = RetrievalArtifactManifest.read(path)
    assert loaded == manifest
    assert loaded.sha256() == manifest.sha256()


def test_manifest_rejects_build_or_runtime_mismatch(tmp_path):
    with pytest.raises(ArtifactMismatchError):
        RetrievalArtifactManifest(
            pds_build_id="pds-a", pds_manifest_sha256="x", milvus_database="default",
            milvus_collection="cooking_knowledge_v2_pds-a", milvus_schema_hash="s",
            milvus_build_id="pds-b", created_at="now", rollback_database="default",
            rollback_collection="cooking_knowledge", rollback_pds_build="old",
        )
    with pytest.raises(ArtifactMismatchError):
        _manifest().validate_runtime(pds_build_id="other", milvus_database="default", milvus_collection=_manifest().milvus_collection, schema_hash="schema-hash")


class _Iterator:
    def __init__(self, rows):
        self.rows = list(rows)
        self.used = False

    def next(self):
        if self.used:
            return []
        self.used = True
        return self.rows

    def close(self):
        return None


class _IndexParams:
    def __init__(self):
        self.items = []

    def add_index(self, **kwargs):
        self.items.append(kwargs)


class _SnapshotClient:
    def __init__(self, rows):
        self.rows = rows
        self.created = []
        self.inserted = []

    def describe_collection(self, _collection):
        return {
            "auto_id": False,
            "enable_dynamic_field": False,
            "description": "snapshot",
            "fields": [
                {"name": "id", "type": "VARCHAR", "params": {"max_length": 20}, "is_primary": True},
                {"name": "vector", "type": "FLOAT_VECTOR", "params": {"dim": 2}, "is_primary": False},
                {"name": "text", "type": "VARCHAR", "params": {"max_length": 100}, "is_primary": False},
            ],
        }

    def get_collection_stats(self, _collection):
        return {"row_count": len(self.rows)}

    def query_iterator(self, *_args, **_kwargs):
        return _Iterator(self.rows)

    def list_indexes(self, _collection):
        return ["vector_index"]

    def describe_index(self, _collection, _index):
        return {"field_name": "vector", "index_type": "HNSW", "metric_type": "COSINE", "M": "16", "efConstruction": "200"}

    def query(self, _collection, *, ids, output_fields):
        return [row for row in self.rows if row["id"] in ids]

    def search(self, **_kwargs):
        return [[{"id": self.rows[0]["id"]}]]

    def has_collection(self, **_kwargs):
        return False

    def create_collection(self, **kwargs):
        self.created.append(kwargs)

    def insert(self, **kwargs):
        self.inserted.extend(kwargs["data"])

    def flush(self, **_kwargs):
        return None

    def prepare_index_params(self):
        return _IndexParams()

    def create_index(self, **kwargs):
        self.index = kwargs["index_params"].items

    def load_collection(self, **_kwargs):
        return None


def test_snapshot_round_trip_and_search_verification(tmp_path, monkeypatch):
    rows = [
        {"id": "chunk-1", "vector": [0.1, 0.2], "text": "正文一"},
        {"id": "chunk-2", "vector": [0.2, 0.3], "text": "正文二"},
    ]
    client = _SnapshotClient(rows)
    output = tmp_path / "backup"
    manifest = milvus_snapshot.create_snapshot(client, database="default", collection="cooking_knowledge", output=output)
    loaded, loaded_rows, _ = milvus_snapshot.load_manifest(output / "manifest.json")
    assert loaded == manifest
    assert milvus_snapshot.verify_snapshot(client, loaded, loaded_rows, database="default", collection="cooking_knowledge", check_search=True)["status"] == "verified"

    class _DataType:
        VARCHAR = "VARCHAR"
        FLOAT_VECTOR = "FLOAT_VECTOR"

    class _RestoreSchema:
        def __init__(self):
            self.fields = []

        def add_field(self, **kwargs):
            self.fields.append(kwargs)

    class _MilvusClient:
        @staticmethod
        def create_schema(**_kwargs):
            return _RestoreSchema()

    monkeypatch.setitem(sys.modules, "pymilvus", types.SimpleNamespace(DataType=_DataType, MilvusClient=_MilvusClient))
    restore_client = _SnapshotClient(rows)
    report = milvus_snapshot.restore_snapshot(restore_client, loaded, loaded_rows, target_collection="cooking_knowledge_restore_verify_test")
    assert report["status"] == "restored"
    assert restore_client.created[0]["collection_name"] == "cooking_knowledge_restore_verify_test"
    assert len(restore_client.inserted) == 2


def test_snapshot_payload_tamper_is_rejected(tmp_path):
    rows = [{"id": "chunk-1", "vector": [0.1, 0.2], "text": "正文一"}]
    output = tmp_path / "backup"
    milvus_snapshot.create_snapshot(_SnapshotClient(rows), database="default", collection="cooking_knowledge", output=output)
    (output / "rows.jsonl").write_text("{}\n", encoding="utf-8")
    with pytest.raises(milvus_snapshot.SnapshotTargetError, match="SHA-256"):
        milvus_snapshot.load_manifest(output / "manifest.json")


def test_cutover_requires_protected_approval_and_atomically_publishes(tmp_path, monkeypatch):
    build_id = "pds_build123"
    to_collection = f"cooking_knowledge_v2_{build_id[:12]}"
    manifest = RetrievalArtifactManifest(
        pds_build_id=build_id,
        pds_manifest_sha256="pds-manifest-sha",
        milvus_database="default",
        milvus_collection=to_collection,
        milvus_schema_hash="schema-sha",
        milvus_build_id=build_id,
        created_at="2026-08-09T00:00:00+00:00",
        rollback_database="default",
        rollback_collection="cooking_knowledge",
        rollback_pds_build="pds_old",
    )
    artifact_root = tmp_path / "artifacts"
    approval_root = tmp_path / "approvals"
    backup_root = tmp_path / "backups"
    active_root = tmp_path / "active"
    artifact_root.mkdir()
    approval_root.mkdir()
    backup_root.mkdir()
    active_root.mkdir()
    artifact_path = manifest.write_atomic(artifact_root / "candidate.json")
    backup_dir = backup_root / "source"
    backup_manifest = milvus_snapshot.create_snapshot(
        _SnapshotClient([
            {"id": "chunk-1", "vector": [0.1, 0.2], "text": "正文一"},
        ]),
        database="default",
        collection="cooking_knowledge",
        output=backup_dir,
    )
    backup_path = backup_dir / "manifest.json"
    backup_sha = hashlib.sha256(backup_path.read_bytes()).hexdigest()
    approval = {
        "approved_by": "operator-a",
        "second_approver": "operator-b",
        "change_id": "CHG-42",
        "from_collection": "cooking_knowledge",
        "to_collection": to_collection,
        "database": "default",
        "pds_build_id": build_id,
        "backup_sha256": backup_sha,
        "environment": "staging",
        "rollback_database": "default",
        "rollback_collection": "cooking_knowledge",
        "rollback_pds_build": "pds_old",
        "expires_at": (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat(),
    }
    approval_path = approval_root / "approval.json"
    approval_path.write_text(json.dumps(approval), encoding="utf-8")
    monkeypatch.setenv("RETRIEVAL_RELEASE_ENVIRONMENT", "staging")
    argv = [
        "--database", "default", "--allowed-database", "default",
        "--from", "cooking_knowledge", "--allowed-from-collection", "cooking_knowledge",
        "--to", to_collection, "--allowed-to-collection", to_collection,
        "--parent-store-build", build_id,
        "--artifact-manifest", str(artifact_path), "--approval-record", str(approval_path),
        "--backup-manifest", str(backup_path), "--expected-backup-sha256", backup_sha,
        "--active-pointer", str(active_root / "active.json"),
        "--allowed-backup-root", str(backup_root), "--allowed-artifact-root", str(artifact_root),
        "--allowed-approval-root", str(approval_root), "--allowed-active-root", str(active_root),
        "--environment", "staging", "--protected-environment", "staging", "--confirm-cutover",
    ]
    approval_without_rollback = dict(approval)
    approval_without_rollback.pop("rollback_pds_build")
    approval_path.write_text(json.dumps(approval_without_rollback), encoding="utf-8")
    with pytest.raises(retrieval_cutover.CutoverGuardError, match="审批记录与切换参数不一致"):
        retrieval_cutover.main(argv)
    approval_path.write_text(json.dumps(approval), encoding="utf-8")
    assert retrieval_cutover.main(argv) == 0
    assert RetrievalArtifactManifest.read(active_root / "active.json") == manifest

    foreign_dir = backup_root / "foreign"
    milvus_snapshot.create_snapshot(
        _SnapshotClient([{"id": "chunk-1", "vector": [0.1, 0.2], "text": "正文一"}]),
        database="default",
        collection="other_collection",
        output=foreign_dir,
    )
    foreign_path = foreign_dir / "manifest.json"
    foreign_approval = dict(approval, backup_sha256=hashlib.sha256(foreign_path.read_bytes()).hexdigest())
    approval_path.write_text(json.dumps(foreign_approval), encoding="utf-8")
    foreign_argv = list(argv)
    foreign_argv[foreign_argv.index("--backup-manifest") + 1] = str(foreign_path)
    foreign_argv[foreign_argv.index("--expected-backup-sha256") + 1] = foreign_approval["backup_sha256"]
    with pytest.raises(retrieval_cutover.CutoverGuardError, match="database/from collection"):
        retrieval_cutover.main(foreign_argv)


def test_cutover_rejects_missing_protected_arguments():
    with pytest.raises(SystemExit):
        retrieval_cutover.main(["--database", "default", "--allowed-database", "other"])


def test_protected_cutover_still_rejects_missing_approval_before_reading_paths(monkeypatch):
    monkeypatch.setenv("RETRIEVAL_RELEASE_ENVIRONMENT", "staging")
    args = types.SimpleNamespace(
        database="default",
        allowed_database="default",
        from_collection="cooking_knowledge",
        to_collection="cooking_knowledge_v2_pds_build123",
        allowed_from_collection="cooking_knowledge",
        allowed_to_collection="cooking_knowledge_v2_pds_build123",
        parent_store_build="pds_build123",
        release_profile="protected",
        protected_environment="staging",
        approval_record=None,
        allowed_approval_root=None,
    )

    with pytest.raises(retrieval_cutover.CutoverGuardError, match="审批记录"):
        retrieval_cutover._validate(args)


def test_personal_local_cutover_keeps_backup_and_manifest_guards_without_dual_approval(tmp_path, monkeypatch):
    build_id = "pds_build123"
    to_collection = f"cooking_knowledge_v2_{build_id[:12]}"
    manifest = RetrievalArtifactManifest(
        pds_build_id=build_id,
        pds_manifest_sha256="pds-manifest-sha",
        milvus_database="default",
        milvus_collection=to_collection,
        milvus_schema_hash="schema-sha",
        milvus_build_id=build_id,
        created_at="2026-08-09T00:00:00+00:00",
        rollback_database="default",
        rollback_collection="cooking_knowledge",
        rollback_pds_build="pds_old",
    )
    artifact_root = tmp_path / "artifacts"
    backup_root = tmp_path / "backups"
    active_root = tmp_path / "active"
    artifact_root.mkdir()
    backup_root.mkdir()
    active_root.mkdir()
    artifact_path = manifest.write_atomic(artifact_root / "candidate.json")
    backup_dir = backup_root / "source"
    milvus_snapshot.create_snapshot(
        _SnapshotClient([{"id": "chunk-1", "vector": [0.1, 0.2], "text": "正文一"}]),
        database="default",
        collection="cooking_knowledge",
        output=backup_dir,
    )
    backup_path = backup_dir / "manifest.json"
    backup_sha = hashlib.sha256(backup_path.read_bytes()).hexdigest()
    argv = [
        "--release-profile", "personal-local",
        "--database", "default", "--allowed-database", "default",
        "--from", "cooking_knowledge", "--allowed-from-collection", "cooking_knowledge",
        "--to", to_collection, "--allowed-to-collection", to_collection,
        "--parent-store-build", build_id,
        "--artifact-manifest", str(artifact_path),
        "--backup-manifest", str(backup_path), "--expected-backup-sha256", backup_sha,
        "--active-pointer", str(active_root / "active.json"),
        "--allowed-backup-root", str(backup_root), "--allowed-artifact-root", str(artifact_root),
        "--allowed-active-root", str(active_root),
        "--environment", "personal-local", "--confirm-cutover",
    ]
    monkeypatch.setenv("RETRIEVAL_RELEASE_ENVIRONMENT", "personal-local")

    assert retrieval_cutover.main(argv) == 0
    assert RetrievalArtifactManifest.read(active_root / "active.json") == manifest

    monkeypatch.setenv("RETRIEVAL_RELEASE_ENVIRONMENT", "staging")
    with pytest.raises(retrieval_cutover.CutoverGuardError, match="personal-local"):
        retrieval_cutover.main(argv)
