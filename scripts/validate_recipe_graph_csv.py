"""校验 Recipe 图 CSV 构建工件的引用、方向、顺序和摘要。"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

try:
    from scripts.build_recipe_graph_csv import (
        BUILD_MANIFEST_NAME,
        BUILD_SCHEMA_VERSION,
        CONTAINS_STEP_RELATIONSHIP,
        NODE_FIELDS,
        PRODUCER_VERSION,
        REQUIRES_RELATIONSHIP,
        RELATIONSHIP_FIELDS,
        _canonical_json,
        _id_digest,
    )
except ModuleNotFoundError:  # pragma: no cover - 支持直接执行脚本。
    from build_recipe_graph_csv import (  # type: ignore
        BUILD_MANIFEST_NAME,
        BUILD_SCHEMA_VERSION,
        CONTAINS_STEP_RELATIONSHIP,
        NODE_FIELDS,
        PRODUCER_VERSION,
        REQUIRES_RELATIONSHIP,
        RELATIONSHIP_FIELDS,
        _canonical_json,
        _id_digest,
    )


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _read_csv(path: Path, expected_fields: tuple[str, ...], errors: list[str]) -> list[dict[str, str]]:
    if not path.is_file():
        errors.append(f"缺少 CSV: {path.name}")
        return []
    raw = path.read_bytes()
    if b"\x00" in raw:
        errors.append(f"CSV 包含 NUL 字节: {path.name}")
        return []
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, strict=True)
            if tuple(reader.fieldnames or ()) != expected_fields:
                errors.append(f"CSV 表头不匹配: {path.name}")
                return []
            rows = list(reader)
    except (csv.Error, UnicodeDecodeError) as error:
        errors.append(f"CSV 转义或编码无效: {path.name}: {error}")
        return []
    if any(None in row for row in rows):
        errors.append(f"CSV 存在未转义的额外列: {path.name}")
    return rows


def _parse_positive_integer(value: str) -> int | None:
    try:
        decimal = Decimal(value)
    except InvalidOperation:
        return None
    if decimal <= 0 or decimal != decimal.to_integral_value():
        return None
    return int(decimal)


def validate_artifact(directory: Path, *, strict: bool) -> dict[str, Any]:
    errors: list[str] = []
    directory = directory.resolve()
    nodes_path = directory / "nodes.csv"
    relationships_path = directory / "relationships.csv"
    manifest_path = directory / BUILD_MANIFEST_NAME
    nodes = _read_csv(nodes_path, NODE_FIELDS, errors)
    relationships = _read_csv(relationships_path, RELATIONSHIP_FIELDS, errors)
    manifest: dict[str, Any] = {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"缺少 manifest: {BUILD_MANIFEST_NAME}")
    except json.JSONDecodeError as error:
        errors.append(f"manifest 不是有效 JSON: {error.msg}")

    node_ids = [row.get("nodeId", "") for row in nodes]
    node_by_id = {row.get("nodeId", ""): row for row in nodes}
    if any(not node_id for node_id in node_ids):
        errors.append("存在空 nodeId")
    if len(set(node_ids)) != len(node_ids):
        errors.append("nodeId 不唯一")
    if any(not re.fullmatch(r"[0-9]{18}", node_id) for node_id in node_ids if node_id):
        errors.append("nodeId 必须是 18 位稳定数字 ID")
    allowed_labels = {"Recipe", "Ingredient", "CookingStep"}
    if any(row.get("labels") not in allowed_labels for row in nodes):
        errors.append("存在未支持的 Recipe 图节点标签")

    relationship_ids = [row.get("relationshipId", "") for row in relationships]
    if any(not relationship_id for relationship_id in relationship_ids):
        errors.append("存在空 relationshipId")
    if len(set(relationship_ids)) != len(relationship_ids):
        errors.append("relationshipId 不唯一")

    requires_by_recipe: Counter[str] = Counter()
    steps_by_recipe: dict[str, list[tuple[int, dict[str, str]]]] = defaultdict(list)
    for row in relationships:
        start_id = row.get("startNodeId", "")
        end_id = row.get("endNodeId", "")
        relationship_type = row.get("relationshipType", "")
        if start_id not in node_by_id or end_id not in node_by_id:
            errors.append(f"关系外键不存在: {row.get('relationshipId', '')}")
            continue
        start_label = node_by_id[start_id].get("labels")
        end_label = node_by_id[end_id].get("labels")
        if relationship_type == REQUIRES_RELATIONSHIP:
            if start_label != "Recipe" or end_label != "Ingredient":
                errors.append(f"REQUIRES 方向无效: {row.get('relationshipId', '')}")
            requires_by_recipe[start_id] += 1
        elif relationship_type == CONTAINS_STEP_RELATIONSHIP:
            if start_label != "Recipe" or end_label != "CookingStep":
                errors.append(f"CONTAINS_STEP 方向无效: {row.get('relationshipId', '')}")
            ordinal = _parse_positive_integer(row.get("step_order", ""))
            if ordinal is None:
                errors.append(f"CONTAINS_STEP 缺少有效步骤顺序: {row.get('relationshipId', '')}")
            else:
                steps_by_recipe[start_id].append((ordinal, row))
        else:
            errors.append(f"不支持的关系类型: {relationship_type}")

    for recipe_id, recipe in sorted(node_by_id.items()):
        if recipe.get("labels") != "Recipe":
            continue
        if strict and not requires_by_recipe[recipe_id]:
            errors.append(f"Recipe 缺少 REQUIRES: {recipe_id}")
        recipe_steps = sorted(steps_by_recipe[recipe_id], key=lambda item: item[0])
        if strict and not recipe_steps:
            errors.append(f"Recipe 缺少 CONTAINS_STEP: {recipe_id}")
        expected_orders = list(range(1, len(recipe_steps) + 1))
        actual_orders = [ordinal for ordinal, _row in recipe_steps]
        if recipe_steps and actual_orders != expected_orders:
            errors.append(f"Recipe 步骤顺序不连续: {recipe_id}")
        for ordinal, row in recipe_steps:
            step_number = _parse_positive_integer(node_by_id[row["endNodeId"]].get("stepNumber", ""))
            if step_number != ordinal:
                errors.append(f"CookingStep 与 CONTAINS_STEP 顺序不一致: {row.get('relationshipId', '')}")

    if manifest:
        if manifest.get("schema_version") != BUILD_SCHEMA_VERSION:
            errors.append("manifest schema_version 无效")
        if manifest.get("producer_version") != PRODUCER_VERSION:
            errors.append("manifest producer_version 无效")
        sources = manifest.get("source_files")
        if not isinstance(sources, list) or not sources:
            errors.append("manifest source_files 无效")
        else:
            source_paths = [item.get("path") for item in sources if isinstance(item, dict)]
            if len(source_paths) != len(sources) or source_paths != sorted(source_paths) or len(set(source_paths)) != len(source_paths):
                errors.append("manifest source_files 未按路径唯一排序")
            if any(not isinstance(item.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", item["sha256"]) for item in sources if isinstance(item, dict)):
                errors.append("manifest source_files SHA-256 无效")
        if manifest.get("node_count") != len(nodes) or manifest.get("relationship_count") != len(relationships):
            errors.append("manifest 节点或关系计数不匹配")
        expected_node_counts = Counter(row.get("labels") for row in nodes)
        if manifest.get("node_counts") != {label: expected_node_counts[label] for label in sorted(expected_node_counts)}:
            errors.append("manifest 节点分类计数不匹配")
        expected_relationship_counts = {
            "REQUIRES": sum(1 for row in relationships if row.get("relationshipType") == REQUIRES_RELATIONSHIP),
            "CONTAINS_STEP": sum(1 for row in relationships if row.get("relationshipType") == CONTAINS_STEP_RELATIONSHIP),
        }
        if manifest.get("relationship_counts") != expected_relationship_counts:
            errors.append("manifest 关系分类计数不匹配")
        expected_csv_hashes = {"nodes.csv": _sha256_file(nodes_path), "relationships.csv": _sha256_file(relationships_path)} if nodes_path.is_file() and relationships_path.is_file() else {}
        if manifest.get("csv_sha256") != expected_csv_hashes:
            errors.append("manifest CSV SHA-256 不匹配")
        summary = manifest.get("stable_id_summary")
        if not isinstance(summary, dict) or summary.get("node_ids_sha256") != _id_digest(node_ids) or summary.get("relationship_ids_sha256") != _id_digest(relationship_ids):
            errors.append("manifest 稳定 ID 摘要不匹配")
        expected_manifest_hash = manifest.get("manifest_sha256")
        without_hash = dict(manifest)
        without_hash.pop("manifest_sha256", None)
        actual_manifest_hash = hashlib.sha256(_canonical_json(without_hash).encode("utf-8")).hexdigest()
        if expected_manifest_hash != actual_manifest_hash:
            errors.append("manifest SHA-256 不匹配")
        mapping = manifest.get("pds_milvus_mapping")
        if not isinstance(mapping, dict) or mapping.get("status") != "unbound":
            errors.append("manifest PDS/Milvus 映射状态无效")

    return {
        "valid": not errors,
        "strict": strict,
        "node_count": len(nodes),
        "relationship_count": len(relationships),
        "errors": errors,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="校验 Recipe 图 CSV 构建工件")
    parser.add_argument("--input", required=True)
    parser.add_argument("--strict", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    report = validate_artifact(Path(args.input), strict=args.strict)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
