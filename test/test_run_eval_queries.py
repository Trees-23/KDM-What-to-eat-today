import json
import tempfile
import unittest
from pathlib import Path

from eval.run_eval import run_one_sample, write_jsonl


class RunEvalQueriesTest(unittest.TestCase):
    def create_audit_dir(self, run_dir: Path, audit_id: str):
        audit_dir = run_dir / audit_id
        audit_dir.mkdir(parents=True)
        (audit_dir / "rag_process.md").write_text("# RAG Process\n", encoding="utf-8")
        (audit_dir / "recall_content.md").write_text("# Recall Content\n", encoding="utf-8")

    def test_run_query_records_response_and_new_audit_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "run"
            run_dir.mkdir()

            def requester(_api_url, user_input, _session_id, _timeout):
                self.create_audit_dir(run_dir, "20260508_120000_000_abcdef12")
                return f"回答：{user_input}"

            result = run_one_sample(
                {
                    "id": "q001",
                    "user_input": "蚝油生菜怎么做？",
                    "category": "recipe_steps",
                    "expected_strategy_hint": "hybrid_traditional",
                },
                api_url="http://example.test/api/chat",
                run_dir=run_dir,
                timeout=10,
                session_prefix="eval",
                requester=requester,
            )

            self.assertEqual(result.status, "success")
            self.assertEqual(result.metadata["audit_id"], "20260508_120000_000_abcdef12")
            self.assertEqual(result.response, "回答：蚝油生菜怎么做？")
            self.assertEqual(result.session_id, "eval-q001")

    def test_write_jsonl_outputs_expected_shape(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "eval_results.jsonl"
            result = run_one_sample(
                {"id": "q002", "user_input": "问题", "category": "x"},
                api_url="http://example.test/api/chat",
                run_dir=Path(tmp) / "missing-run",
                timeout=10,
                session_prefix="eval",
                requester=lambda *_args: "答案",
            )

            count = write_jsonl([result], output)

            self.assertEqual(count, 1)
            row = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(row["user_input"], "问题")
            self.assertEqual(row["response"], "答案")
            self.assertEqual(row["status"], "success")


if __name__ == "__main__":
    unittest.main()
