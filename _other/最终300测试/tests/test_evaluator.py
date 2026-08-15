import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "_other/最终300测试/工具/answer_quality_evaluation"))

from evaluator import ScoreValidationError, answer_type, canonical_sha256, load_jsonl, validate_and_score


RUBRIC = json.loads((ROOT / "_other/最终300测试/配置/answer-quality-rubric-v1.json").read_text())
SCHEMA = json.loads((ROOT / "_other/最终300测试/配置/answer-quality-output-schema-v1.json").read_text())


def reply(**updates):
    value = {"task_score": 5, "preference_score": None, "evidence_expression_score": 5, "boundary_expression_score": None, "readability_score": 5, "issue_tags": [], "evidence_notes": [], "confidence": "high", "review_reason": "可用。"}
    value.update(updates)
    return value


class EvaluatorTests(unittest.TestCase):
    def test_answer_type_mapping(self):
        self.assertEqual(answer_type("S01-A-01"), "normal")
        self.assertEqual(answer_type("S06-A-01"), "recommendation")
        self.assertEqual(answer_type("S05-C-01"), "refusal_or_degraded")
        self.assertEqual(answer_type("S10-B-01"), "refusal_or_degraded")

    def test_weight_formula(self):
        result = validate_and_score(reply(), "normal", RUBRIC, SCHEMA, set())
        self.assertEqual(result["total_score_100"], 100)
        result = validate_and_score(reply(task_score=1, evidence_expression_score=1, readability_score=1), "normal", RUBRIC, SCHEMA, set())
        self.assertEqual(result["total_score_100"], 0)

    def test_rejects_non_applicable_dimension(self):
        with self.assertRaises(ScoreValidationError):
            validate_and_score(reply(preference_score=3), "normal", RUBRIC, SCHEMA, set())

    def test_rejects_unknown_evidence_id(self):
        with self.assertRaises(ScoreValidationError):
            validate_and_score(reply(evidence_notes=[{"answer_excerpt": "x", "verdict": "clear", "evidence_ids": ["unknown"]}]), "normal", RUBRIC, SCHEMA, {"allowed"})

    def test_checkpoint_terminal_records_do_not_repeat_success(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.jsonl"
            checkpoint.write_text('{"case_id":"S01-A-01","status":"PENDING"}\n{"case_id":"S01-A-01","status":"SCORED"}\n', encoding="utf-8")
            records = load_jsonl(checkpoint)
            terminal = {item["case_id"]: item for item in records if item["status"] in {"SCORED", "QUALITY_UNVERIFIED"}}
            self.assertEqual(list(terminal), ["S01-A-01"])

    def test_input_hash_is_stable(self):
        self.assertEqual(canonical_sha256({"b": 2, "a": 1}), canonical_sha256({"a": 1, "b": 2}))

if __name__ == "__main__":
    unittest.main()
