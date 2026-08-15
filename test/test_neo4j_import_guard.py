import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from scripts import build_recipe_graph_csv
from scripts import neo4j_graph_import
from scripts.neo4j_graph_import import Neo4jImportGuardError, validate_import
from scripts.neo4j_snapshot import SnapshotGuardError, create_snapshot, restore_snapshot, verify_snapshot


def _source_manifest(tmp_path: Path) -> Path:
    dishes = tmp_path / "dishes"
    dishes.mkdir()
    (dishes / "菜A.md").write_text("""# 菜A的做法

## 必备原料和工具

- 鸡肉 200g

## 操作

1. 鸡肉切块
""", encoding="utf-8")
    manifest = tmp_path / "sources.json"
    manifest.write_text(json.dumps({"schema_version": "recipe-source-manifest-v1", "source_root": "dishes", "files": [{"path": "菜A.md"}]}, ensure_ascii=False), encoding="utf-8")
    return manifest


def _build_csv(tmp_path: Path) -> Path:
    output = tmp_path / "csv"
    assert build_recipe_graph_csv.main(["--input-manifest", str(_source_manifest(tmp_path)), "--output", str(output)]) == 0
    return output


def test_snapshot_verify_restore_isolated_and_rejects_default_database(tmp_path):
    export = tmp_path / "graph.jsonl"
    export.write_text(json.dumps({"kind": "node", "nodeId": "recipe-1", "label": "Recipe"}) + "\n" + json.dumps({"kind": "node", "nodeId": "ingredient-1", "label": "Ingredient"}) + "\n" + json.dumps({"kind": "relationship", "startNodeId": "recipe-1", "endNodeId": "ingredient-1", "type": "REQUIRES"}) + "\n", encoding="utf-8")
    backup_root = tmp_path / "backups"
    backup = backup_root / "snapshot"
    with pytest.raises(SnapshotGuardError, match="默认"):
        create_snapshot(database="neo4j", allowed_database="neo4j", source_export=export, output=backup)
    manifest = create_snapshot(database="staging-db", allowed_database="staging-db", source_export=export, output=backup)
    verify = verify_snapshot(database="staging-db", allowed_database="staging-db", manifest_path=backup / "manifest.json", allowed_backup_root=backup_root)
    assert verify["status"] == "verified"
    restored = restore_snapshot(manifest_path=backup / "manifest.json", target_database="staging-restore", allowed_database="staging-restore", allowed_backup_root=backup_root, restore_output=tmp_path / "restored", allowed_restore_root=tmp_path)
    assert restored["restored_from_database"] == "staging-db"
    assert (tmp_path / "restored" / "graph.jsonl").is_file()


def test_import_dry_run_and_apply_require_verified_backup_and_approval(tmp_path):
    csv_dir = _build_csv(tmp_path)
    export = tmp_path / "graph.jsonl"
    export.write_text(json.dumps({"kind": "node", "nodeId": "recipe-1"}) + "\n", encoding="utf-8")
    backup_root = tmp_path / "backups"
    backup = backup_root / "snapshot"
    create_snapshot(database="staging-db", allowed_database="staging-db", source_export=export, output=backup)
    dry_run = validate_import(database="staging-db", allowed_database="staging-db", csv_dir=csv_dir, allowed_csv_root=tmp_path, apply=False)
    assert dry_run["status"] == "dry_run"
    backup_sha = __import__("hashlib").sha256((backup / "manifest.json").read_bytes()).hexdigest()
    with pytest.raises(Neo4jImportGuardError, match="backup verify"):
        validate_import(database="staging-db", allowed_database="staging-db", csv_dir=csv_dir, allowed_csv_root=tmp_path, apply=True, backup_manifest=backup / "manifest.json", backup_root=backup_root, expected_backup_sha256=backup_sha, approval_record=tmp_path / "missing.json", allowed_approval_root=tmp_path, batch_size=50)

    # Build output is valid; bind the backup verification to this exact CSV manifest.
    csv_sha = __import__("hashlib").sha256((csv_dir / "recipe-build-manifest.json").read_bytes()).hexdigest()
    verify_snapshot(database="staging-db", allowed_database="staging-db", manifest_path=backup / "manifest.json", allowed_backup_root=backup_root, csv_manifest=csv_dir / "recipe-build-manifest.json")
    approval_root = tmp_path / "approvals"
    approval_root.mkdir()
    approval = approval_root / "approval.json"
    approval.write_text(json.dumps({"database": "staging-db", "csv_manifest_sha256": csv_sha, "backup_sha256": backup_sha, "batch_size": 50, "approved_by": "owner", "change_id": "local-6c", "expires_at": (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()}), encoding="utf-8")
    result = validate_import(database="staging-db", allowed_database="staging-db", csv_dir=csv_dir, allowed_csv_root=tmp_path, apply=True, backup_manifest=backup / "manifest.json", backup_root=backup_root, expected_backup_sha256=backup_sha, approval_record=approval, allowed_approval_root=approval_root, batch_size=50)
    assert result["status"] == "guarded_apply_ready"


def test_apply_never_reports_success_without_a_real_executor(monkeypatch, tmp_path):
    monkeypatch.setattr(neo4j_graph_import, "validate_import", lambda **_kwargs: {"status": "guarded_apply_ready"})
    with pytest.raises(Neo4jImportGuardError, match="尚未实现"):
        neo4j_graph_import.main(["--database", "staging-db", "--allowed-database", "staging-db", "--csv-dir", str(tmp_path), "--allowed-csv-root", str(tmp_path), "--apply", "--neo4j-uri", "bolt://staging"])


def test_recipe_import_uses_source_path_to_exclude_hierarchy_nodes():
    cypher = (Path(__file__).resolve().parents[1] / "data" / "cypher" / "neo4j_import.cypher").read_text(encoding="utf-8")
    recipe_block = cypher.split("// 创建食材节点", 1)[0]
    assert "row.filePath IS NOT NULL" in recipe_block
    assert "trim(row.filePath) <> ''" in recipe_block
