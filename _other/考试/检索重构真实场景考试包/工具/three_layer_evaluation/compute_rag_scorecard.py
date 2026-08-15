from __future__ import annotations

import argparse
from pathlib import Path

from common import candidate_ids, ranking_scores, read_json, read_jsonl, write_json


def build(cases_path: Path, registry_path: Path, output: Path) -> dict:
    cases, registry = read_jsonl(cases_path), read_json(registry_path)["cases"]
    records = []
    for case in cases:
        gold = registry[case["case_id"]]
        record = {"case_id": case["case_id"], "scenario_id": case["scenario_id"], "audit_id": case["audit_id"], "status": gold["status"], "gold_version": gold.get("gold_version"), "scope": gold.get("scope"), "reason": gold.get("reason") or gold.get("limitation"), "metrics": {}}
        if gold["status"] == "COMPUTABLE":
            ranked = candidate_ids(case["recommendation_trace"]["final_top5"])
            values = ranking_scores(ranked, gold["labels"], 5)
            record["metrics"] = {f"top30_pool_selection_{name}@5": value for name, value in values.items()}
            record["ranking_stage"] = "final_top5_within_top30"
        records.append(record)
    summary = {"case_count": len(records), "computable": sum(row["status"] == "COMPUTABLE" for row in records), "na": sum(row["status"] == "N/A" for row in records), "unverified": sum(row["status"] == "RAG_UNVERIFIED" for row in records)}
    payload = {"summary": summary, "cases": records}; write_json(output, payload); return payload


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--cases", type=Path, required=True); parser.add_argument("--registry", type=Path, required=True); parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); build(args.cases, args.registry, args.output); return 0


if __name__ == "__main__": raise SystemExit(main())
