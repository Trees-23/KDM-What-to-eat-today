from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "merge_intent_planner_acceptance.py"


def _module():
    spec = importlib.util.spec_from_file_location("merge_intent_planner_acceptance", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_aggregate_requires_complete_official_question_coverage(tmp_path, monkeypatch):
    module = _module()
    bank = tmp_path / "bank.json"
    bank.write_text(json.dumps({"questions": [{"question_id": f"q-{index}"} for index in range(300)]}), encoding="utf-8")
    monkeypatch.setattr(module, "BANK", bank)
    base = tmp_path / "base"
    base.mkdir()
    (base / "new-results.jsonl").write_text(json.dumps({"question_id": "q-0", "status": "passed", "audit_id": "a"}) + "\n", encoding="utf-8")

    try:
        module.main(["--base", str(base), "--regression", str(base), "--output", str(tmp_path / "output")])
    except ValueError as error:
        assert "缺少题号" in str(error)
    else:
        raise AssertionError("不完整题号覆盖必须被拒绝")
