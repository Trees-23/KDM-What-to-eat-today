"""第二套定向测试题必须持续复用正式题库的原始题干和检索契约。"""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FULL_BANK = PROJECT_ROOT / "_other" / "考试" / "检索重构真实场景考试包" / "试卷题库.json"
FIRST_SMOKE_BANK = PROJECT_ROOT / "_other" / "考试" / "测试试卷" / "试卷题库.json"
SECOND_SMOKE_BANK = PROJECT_ROOT / "_other" / "考试" / "测试试卷2" / "试卷题库.json"


def test_second_new_path_smoke_paper_matches_unseen_full_bank_questions():
    full_questions = {
        question["question_id"]: question
        for question in json.loads(FULL_BANK.read_text(encoding="utf-8"))["questions"]
    }
    first = json.loads(FIRST_SMOKE_BANK.read_text(encoding="utf-8"))
    second = json.loads(SECOND_SMOKE_BANK.read_text(encoding="utf-8"))

    assert second["variant"] == "new"
    assert second["question_count"] == 10
    assert len(second["questions"]) == 10
    second_ids = {question["question_id"] for question in second["questions"]}
    assert len(second_ids) == 10
    assert second_ids.isdisjoint({question["question_id"] for question in first["questions"]})

    for question in second["questions"]:
        original = full_questions[question["question_id"]]
        assert question == original
