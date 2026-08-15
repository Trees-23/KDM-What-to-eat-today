#!/usr/bin/env python3
"""报告活动或指定 PDS build 的推荐属性覆盖率，不读取菜谱正文。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rag_modules.parent_document_store import ParentDocumentStore


FIELDS = (
    "recipe_methods", "recipe_tools", "recipe_cooking_appliances",
    "recipe_optional_cooking_appliances", "unknown_cooking_appliance", "step_count",
    "prep_minutes", "cook_minutes", "total_minutes", "servings_count", "attribute_provenance",
)


def report(store: ParentDocumentStore, build_id: str) -> dict[str, object]:
    rows = list(store.iter_recipe_metadata(build_id=build_id))
    total = len(rows)
    present = {
        field: sum(1 for row in rows if field in row.metadata and row.metadata[field] is not None)
        for field in FIELDS
    }
    return {
        "build_id": build_id,
        "recipe_count": total,
        "present": present,
        "coverage": {field: (count / total if total else 0.0) for field, count in present.items()},
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-store", required=True)
    parser.add_argument("--build", required=True)
    args = parser.parse_args(argv)
    with ParentDocumentStore.open(args.parent_store, active_build_id=args.build) as store:
        print(json.dumps(report(store, args.build), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
