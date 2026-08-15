"""校验未来严格营养出口的数据集，不将菜谱文本当成营养数据。"""

from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


REQUIRED_FIELDS = (
    "nodeId",
    "fat_g_per_serving",
    "nutrition_source",
    "nutrition_version",
    "policy_version",
    "reviewed_at",
)


def _records(source: Path) -> Iterable[dict[str, Any]]:
    if source.suffix.lower() == ".csv":
        with source.open("r", encoding="utf-8", newline="") as handle:
            yield from csv.DictReader(handle)
        return
    with source.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, list):
        raise ValueError("JSON 营养数据集必须是记录数组")
    for record in payload:
        if not isinstance(record, dict):
            raise ValueError("营养数据集记录必须是对象")
        yield record


def validate(source: Path, policy_version: str) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    for row_number, record in enumerate(_records(source), start=1):
        prefix = f"第 {row_number} 行"
        missing = [field for field in REQUIRED_FIELDS if not str(record.get(field, "")).strip()]
        if missing:
            errors.append(f"{prefix} 缺少字段: {', '.join(missing)}")
            continue
        node_id = str(record["nodeId"]).strip()
        if node_id in seen_ids:
            errors.append(f"{prefix} nodeId 重复: {node_id}")
        seen_ids.add(node_id)
        try:
            fat = float(record["fat_g_per_serving"])
        except (TypeError, ValueError):
            errors.append(f"{prefix} fat_g_per_serving 必须是数值")
        else:
            if not math.isfinite(fat) or fat < 0:
                errors.append(f"{prefix} fat_g_per_serving 必须是非负有限数值")
        try:
            datetime.fromisoformat(str(record["reviewed_at"]).replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"{prefix} reviewed_at 必须为 ISO-8601 时间")
        if str(record["policy_version"]).strip() != policy_version:
            errors.append(f"{prefix} policy_version 与 --policy 不一致")
    if not seen_ids:
        errors.append("营养数据集不能为空")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="校验受治理的严格营养数据集")
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--strict", action="store_true", required=True)
    args = parser.parse_args()

    if args.policy == "nutrition_soft_preference_v1":
        parser.error("当前策略没有受治理营养数据，严格模式必须保持关闭")
    if not args.source.is_file():
        parser.error(f"营养数据集不存在: {args.source}")
    errors = validate(args.source, args.policy)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {args.source} 通过 {args.policy} 校验")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
