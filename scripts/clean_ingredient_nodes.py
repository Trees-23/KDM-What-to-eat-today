"""规范化历史 Recipe 图中的同名 Ingredient 节点。

历史 CSV 把同一种食材按菜谱实例重复建节点。该工具只合并完全同名的
Ingredient，并把菜谱上下文属性保留到 REQUIRES 关系，避免合并后丢失用量
或分类信息。
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


NODE_FILE = "nodes.csv"
RELATIONSHIP_FILE = "relationships.csv"
CANONICAL_MAP_FILE = "ingredient_canonical_map.csv"
REPORT_FILE = "ingredient_cleaning_report.json"
RELATIONSHIP_CONTEXT_FIELDS = ("ingredientCategory", "isMain")


class IngredientCleaningError(ValueError):
    """输入 CSV 不满足清洗前提。"""


def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        raise IngredientCleaningError(f"缺少 CSV: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        fieldnames = list(reader.fieldnames or ())
        if not fieldnames:
            raise IngredientCleaningError(f"CSV 缺少表头: {path}")
        return fieldnames, list(reader)


def _write_csv(path: Path, fieldnames: Iterable[str], rows: Iterable[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), extrasaction="raise", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _canonical_category(rows: list[dict[str, str]]) -> str:
    categories = Counter(row.get("category", "") for row in rows if row.get("category", ""))
    if not categories:
        return ""
    return min(categories, key=lambda category: (-categories[category], category))


def clean_graph(input_directory: Path, output_directory: Path) -> dict[str, int]:
    """写出清洗后的图 CSV；输出目录必须不存在。"""

    input_directory = input_directory.resolve()
    output_directory = output_directory.resolve()
    if output_directory.exists():
        raise IngredientCleaningError(f"输出目录已存在，拒绝覆盖: {output_directory}")

    node_fields, nodes = _read_csv(input_directory / NODE_FILE)
    relationship_fields, relationships = _read_csv(input_directory / RELATIONSHIP_FILE)
    required_node_fields = {"nodeId", "labels", "name", "category", "amount", "unit", "isMain"}
    required_relationship_fields = {"startNodeId", "endNodeId", "relationshipId", "relationshipType", "amount", "unit"}
    if missing := required_node_fields.difference(node_fields):
        raise IngredientCleaningError(f"nodes.csv 缺少必要列: {', '.join(sorted(missing))}")
    if missing := required_relationship_fields.difference(relationship_fields):
        raise IngredientCleaningError(f"relationships.csv 缺少必要列: {', '.join(sorted(missing))}")

    ingredients_by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    ingredient_by_id: dict[str, dict[str, str]] = {}
    for node in nodes:
        if node.get("labels") != "Ingredient":
            continue
        node_id = node.get("nodeId", "")
        if not node_id:
            raise IngredientCleaningError("Ingredient 存在空 nodeId")
        if node_id in ingredient_by_id:
            raise IngredientCleaningError(f"Ingredient nodeId 重复: {node_id}")
        if not node.get("name", ""):
            raise IngredientCleaningError(f"Ingredient 存在空名称: {node_id}")
        ingredient_by_id[node_id] = node
        ingredients_by_name[node["name"]].append(node)

    canonical_by_id: dict[str, str] = {}
    canonical_nodes: dict[str, dict[str, str]] = {}
    canonical_map_rows: list[dict[str, str]] = []
    duplicate_groups = 0
    removed_nodes = 0
    category_conflicts = 0
    for name, group in sorted(ingredients_by_name.items()):
        ordered = sorted(group, key=lambda node: node["nodeId"])
        canonical_id = ordered[0]["nodeId"]
        if len(ordered) > 1:
            duplicate_groups += 1
            removed_nodes += len(ordered) - 1
        categories = {node.get("category", "") for node in ordered if node.get("category", "")}
        if len(categories) > 1:
            category_conflicts += 1
        canonical = dict(ordered[0])
        canonical["category"] = _canonical_category(ordered)
        # 这三项来自单个菜谱实例，清洗后只属于 REQUIRES 关系。
        canonical["amount"] = ""
        canonical["unit"] = ""
        canonical["isMain"] = ""
        canonical_nodes[canonical_id] = canonical
        for node in ordered:
            node_id = node["nodeId"]
            canonical_by_id[node_id] = canonical_id
            canonical_map_rows.append(
                {
                    "originalNodeId": node_id,
                    "canonicalNodeId": canonical_id,
                    "name": name,
                    "merged": "true" if node_id != canonical_id else "false",
                }
            )

    cleaned_nodes: list[dict[str, str]] = []
    for node in nodes:
        if node.get("labels") != "Ingredient":
            cleaned_nodes.append(node)
            continue
        node_id = node["nodeId"]
        if canonical_by_id[node_id] == node_id:
            cleaned_nodes.append(canonical_nodes[node_id])

    cleaned_relationships: list[dict[str, str]] = []
    rewritten_endpoints = 0
    for relationship in relationships:
        cleaned = dict(relationship)
        original_end_id = cleaned["endNodeId"]
        original_ingredient = ingredient_by_id.get(original_end_id)
        if original_ingredient is not None:
            cleaned["ingredientCategory"] = original_ingredient.get("category", "")
            cleaned["isMain"] = original_ingredient.get("isMain", "")
            canonical_id = canonical_by_id[original_end_id]
            if canonical_id != original_end_id:
                cleaned["endNodeId"] = canonical_id
                rewritten_endpoints += 1
        else:
            cleaned["ingredientCategory"] = ""
            cleaned["isMain"] = ""
        cleaned_relationships.append(cleaned)

    output_relationship_fields = list(relationship_fields)
    for field in RELATIONSHIP_CONTEXT_FIELDS:
        if field not in output_relationship_fields:
            output_relationship_fields.append(field)

    report = {
        "input_node_count": len(nodes),
        "output_node_count": len(cleaned_nodes),
        "input_relationship_count": len(relationships),
        "output_relationship_count": len(cleaned_relationships),
        "ingredient_duplicate_groups": duplicate_groups,
        "ingredient_nodes_removed": removed_nodes,
        "ingredient_category_conflicts": category_conflicts,
        "relationship_endpoints_rewritten": rewritten_endpoints,
    }
    parent = output_directory.parent
    parent.mkdir(parents=True, exist_ok=True)
    temporary_directory = Path(tempfile.mkdtemp(prefix=f".{output_directory.name}.", dir=parent))
    try:
        _write_csv(temporary_directory / NODE_FILE, node_fields, cleaned_nodes)
        _write_csv(temporary_directory / RELATIONSHIP_FILE, output_relationship_fields, cleaned_relationships)
        _write_csv(
            temporary_directory / CANONICAL_MAP_FILE,
            ("originalNodeId", "canonicalNodeId", "name", "merged"),
            canonical_map_rows,
        )
        (temporary_directory / REPORT_FILE).write_text(
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary_directory, output_directory)
    except Exception:
        for child in temporary_directory.iterdir():
            child.unlink()
        temporary_directory.rmdir()
        raise
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="合并历史 Recipe 图中的同名 Ingredient 节点")
    parser.add_argument("--input", required=True, help="包含 nodes.csv 与 relationships.csv 的目录")
    parser.add_argument("--output", required=True, help="不存在的输出目录")
    args = parser.parse_args(argv)
    try:
        report = clean_graph(Path(args.input), Path(args.output))
    except IngredientCleaningError as error:
        print(json.dumps({"valid": False, "error": str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps({"valid": True, **report}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
