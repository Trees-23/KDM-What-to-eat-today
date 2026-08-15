"""定向测试试卷必须持续复用正式题库的原始题干和检索契约。"""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FULL_BANK = PROJECT_ROOT / "_other" / "考试" / "检索重构真实场景考试包" / "试卷题库.json"
SMOKE_BANK = PROJECT_ROOT / "_other" / "考试" / "测试试卷" / "试卷题库.json"


def test_new_path_smoke_paper_matches_the_selected_full_bank_questions():
    full_questions = {
        question["question_id"]: question
        for question in json.loads(FULL_BANK.read_text(encoding="utf-8"))["questions"]
    }
    smoke = json.loads(SMOKE_BANK.read_text(encoding="utf-8"))

    assert smoke["variant"] == "new"
    assert smoke["question_count"] == 10
    assert len(smoke["questions"]) == 10
    assert len({question["question_id"] for question in smoke["questions"]}) == 10

    for question in smoke["questions"]:
        original = full_questions[question["question_id"]]
        assert question["scenario_id"] == original["scenario_id"]
        assert question["difficulty_code"] == original["difficulty_code"]
        assert question["question"] == original["question"]
        assert question["contract"] == {
            key: value
            for key, value in original["contract"].items()
            if key not in {"required_metrics"}
        }
