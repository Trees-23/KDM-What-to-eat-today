from __future__ import annotations

import argparse
from pathlib import Path

from common import read_json, read_jsonl, write_json


def build(source: Path, cases_path: Path, output: Path) -> dict:
    acceptance = read_json(source / "acceptance-report.json")
    failure = read_json(source / "failure-summary.json")
    cases = read_jsonl(cases_path)
    payload = {
        "source": {"acceptance_report": str((source / "acceptance-report.json").resolve()), "failure_summary": str((source / "failure-summary.json").resolve())},
        "original_summary": {"acceptance": acceptance, "failure_summary": failure},
        "case_count": len(cases),
        "status_counts": {status: sum(row.get("source_status") == status for row in cases) for status in sorted({row.get("source_status") for row in cases})},
        "cases": [{"case_id": row["case_id"], "source_status": row["source_status"], "audit_id": row["audit_id"], "failures": row["hard_reference"]["failures"]} for row in cases],
        "note": "本文件只引用既有硬规则考试结论，不重新判题。",
    }
    write_json(output, payload); return payload


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--source", type=Path, required=True); parser.add_argument("--cases", type=Path, required=True); parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); build(args.source, args.cases, args.output); return 0


if __name__ == "__main__": raise SystemExit(main())
