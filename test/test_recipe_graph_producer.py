from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

from scripts import build_recipe_graph_csv, validate_recipe_graph_csv


def _write_source_manifest(tmp_path: Path) -> Path:
    dishes = tmp_path / "dishes"
    meat = dishes / "meat"
    vegetable = dishes / "vegetable"
    meat.mkdir(parents=True)
    vegetable.mkdir(parents=True)
    (meat / "菜A.md").write_text(
        """# 菜A的做法

带有\"引号\"、逗号的说明。

## 必备原料和工具

- 鸡肉 200g
- 大葱（可选）

## 操作

- 鸡肉切块备用
- 加入\"酱汁\"，翻炒均匀
""",
        encoding="utf-8",
    )
    (vegetable / "菜B.md").write_text(
        """# 菜B的做法

## 必备原料和工具

- 豆腐 1块

## 操作

1. 豆腐切块
2. 小火煎至两面金黄
""",
        encoding="utf-8",
    )
    manifest = tmp_path / "sources.json"
    manifest.write_text(
        json.dumps(
            {
                "schema_version": "recipe-source-manifest-v1",
                "source_root": "dishes",
                "files": [
                    {"path": "vegetable/菜B.md"},
                    {"path": "meat/菜A.md"},
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return manifest


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _refresh_manifest_hash(output: Path) -> None:
    relationships_path = output / "relationships.csv"
    build_manifest_path = output / "recipe-build-manifest.json"
    build_manifest = json.loads(build_manifest_path.read_text(encoding="utf-8"))
    build_manifest["csv_sha256"]["relationships.csv"] = hashlib.sha256(relationships_path.read_bytes()).hexdigest()
    build_manifest.pop("manifest_sha256")
    build_manifest["manifest_sha256"] = hashlib.sha256(
        build_recipe_graph_csv._canonical_json(build_manifest).encode("utf-8")
    ).hexdigest()
    build_manifest_path.write_text(json.dumps(build_manifest, ensure_ascii=False), encoding="utf-8")


def test_manifest_input_builds_repeatable_csv_and_passes_strict_validation(tmp_path: Path):
    manifest = _write_source_manifest(tmp_path)
    first = tmp_path / "first"
    second = tmp_path / "second"

    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(first)]) == 0
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(second)]) == 0
    assert validate_recipe_graph_csv.main(["--input", str(first), "--strict"]) == 0

    for name in ("nodes.csv", "relationships.csv", "recipe-build-manifest.json"):
        assert (first / name).read_bytes() == (second / name).read_bytes()

    build_manifest = json.loads((first / "recipe-build-manifest.json").read_text(encoding="utf-8"))
    assert build_manifest["schema_version"] == "recipe-build-manifest-v1"
    assert build_manifest["producer_version"] == "recipe_graph_csv_producer_v1"
    assert [item["path"] for item in build_manifest["source_files"]] == ["meat/菜A.md", "vegetable/菜B.md"]
    assert all(len(item["sha256"]) == 64 for item in build_manifest["source_files"])
    assert build_manifest["manifest_sha256"]
    assert build_manifest["csv_sha256"]["nodes.csv"] == hashlib.sha256((first / "nodes.csv").read_bytes()).hexdigest()

    nodes = _rows(first / "nodes.csv")
    relationships = _rows(first / "relationships.csv")
    labels_by_id = {row["nodeId"]: row["labels"] for row in nodes}
    assert {row["labels"] for row in nodes} == {"Recipe", "Ingredient", "CookingStep"}
    assert any('"酱汁"' in row["description"] for row in nodes)
    assert '""' in (first / "nodes.csv").read_text(encoding="utf-8")
    assert all(labels_by_id[row["startNodeId"]] == "Recipe" for row in relationships)
    assert all(
        labels_by_id[row["endNodeId"]] == ("Ingredient" if row["relationshipType"] == "801000001" else "CookingStep")
        for row in relationships
    )


def test_manifest_input_rejects_source_hash_mismatch(tmp_path: Path):
    manifest = _write_source_manifest(tmp_path)
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["files"][0]["sha256"] = "0" * 64
    manifest.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(tmp_path / "output")]) == 2
    assert not (tmp_path / "output").exists()


def test_directory_input_and_dry_run_are_explicit_and_non_writing(tmp_path: Path):
    manifest = _write_source_manifest(tmp_path)
    source_directory = tmp_path / "dishes"
    output = tmp_path / "output"
    dry_output = tmp_path / "dry-output"

    assert build_recipe_graph_csv.main(["--input-dir", str(source_directory), "--output", str(output)]) == 0
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(dry_output), "--dry-run"]) == 0
    assert (output / "nodes.csv").is_file()
    assert not dry_output.exists()


def test_validator_rejects_bad_relationship_direction(tmp_path: Path, capsys):
    manifest = _write_source_manifest(tmp_path)
    output = tmp_path / "output"
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(output)]) == 0

    relationships_path = output / "relationships.csv"
    rows = _rows(relationships_path)
    requires = next(row for row in rows if row["relationshipType"] == "801000001")
    requires["startNodeId"], requires["endNodeId"] = requires["endNodeId"], requires["startNodeId"]
    with relationships_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    _refresh_manifest_hash(output)

    assert validate_recipe_graph_csv.main(["--input", str(output), "--strict"]) == 2
    report = json.loads(capsys.readouterr().out.splitlines()[-1])
    assert any("REQUIRES 方向无效" in error for error in report["errors"])


def test_validator_rejects_missing_foreign_key_and_non_contiguous_step_order(tmp_path: Path, capsys):
    manifest = _write_source_manifest(tmp_path)
    output = tmp_path / "output"
    assert build_recipe_graph_csv.main(["--input-manifest", str(manifest), "--output", str(output)]) == 0

    relationships_path = output / "relationships.csv"
    rows = _rows(relationships_path)
    next(row for row in rows if row["relationshipType"] == "801000001")["endNodeId"] = "999999999999999999"
    step = next(row for row in rows if row["relationshipType"] == "801000003" and row["step_order"] == "2")
    step["step_order"] = "9"
    with relationships_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    _refresh_manifest_hash(output)

    assert validate_recipe_graph_csv.main(["--input", str(output), "--strict"]) == 2
    report = json.loads(capsys.readouterr().out.splitlines()[-1])
    assert any("关系外键不存在" in error for error in report["errors"])
    assert any("Recipe 步骤顺序不连续" in error for error in report["errors"])
