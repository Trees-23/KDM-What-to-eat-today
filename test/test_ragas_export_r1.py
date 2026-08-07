import json
import tempfile
import unittest
from pathlib import Path

from eval.run_eval import EvalResult, read_audit_sample, write_jsonl, write_score_jsonl
from rag_modules.rag_audit import RAGAuditManager


class RAGASExportR1Test(unittest.TestCase):
    def test_single_audit_dir_exports_valid_ragas_sample(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=1000).create_run()
            audit.append_process(
                "Request",
                {
                    "original_query": "推荐低脂菜",
                    "selected_strategy": "hybrid_traditional",
                    "top_k": 5,
                    "candidate_k": 10,
                    "rerank_model": "reranker",
                    "embedding_model": "embedding",
                    "request_duration_ms": 123,
                    "evaluation_sample_id": audit.audit_id,
                    "experiment_id": "baseline",
                    "variant_name": "default",
                    "config_hash": "abc123",
                    "model_name": "test-model",
                    "prompt_template_version": "v1",
                },
            )
            audit.append_recall(
                "Final Prompt Context",
                "### result_order=0\nsource: generation_context\n\n```text\n上下文A\n```\n",
            )

            sample = read_audit_sample(audit.root_dir, audit.audit_id)

            self.assertEqual(sample["retrieved_contexts"], ["上下文A"])
            self.assertEqual(sample["metadata"]["audit_id"], audit.audit_id)
            self.assertEqual(sample["metadata"]["strategy"], "hybrid_traditional")
            self.assertEqual(sample["metadata"]["top_k"], 5)
            self.assertEqual(sample["metadata"]["evaluation_sample_id"], audit.audit_id)
            self.assertEqual(sample["metadata"]["experiment_id"], "baseline")
            self.assertEqual(sample["metadata"]["variant_name"], "default")
            self.assertEqual(sample["metadata"]["config_hash"], "abc123")
            self.assertEqual(sample["metadata"]["generation_model"], "test-model")
            self.assertEqual(sample["metadata"]["prompt_version"], "v1")

    def test_write_jsonl_outputs_result_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "eval_results.jsonl"
            row = EvalResult(
                id="q001",
                user_input="问题",
                reference="标准答案",
                category="recipe_steps",
                expected_strategy_hint="hybrid_traditional",
                session_id="eval-q001",
                response="回答",
                retrieved_contexts=["上下文"],
                metadata={"audit_id": "audit-1"},
                scores={"faithfulness": 1.0},
                status="success",
                error=None,
                latency_ms=12,
            )

            count = write_jsonl([row], output)

            self.assertEqual(count, 1)
            lines = output.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual(json.loads(lines[0])["retrieved_contexts"], ["上下文"])
            self.assertEqual(json.loads(lines[0])["scores"], {"faithfulness": 1.0})

    def test_write_score_jsonl_outputs_only_scores(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "ragas_scores.jsonl"
            row = EvalResult(
                id="q001",
                user_input="问题",
                reference="标准答案",
                category="recipe_steps",
                expected_strategy_hint="hybrid_traditional",
                session_id="eval-q001",
                response="回答",
                retrieved_contexts=["上下文"],
                metadata={"audit_id": "audit-1"},
                scores={"faithfulness": 1.0},
                status="success",
                error=None,
                latency_ms=12,
            )

            count = write_score_jsonl([row], output)

            self.assertEqual(count, 1)
            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(data["id"], "q001")
            self.assertEqual(data["scores"], {"faithfulness": 1.0})
            self.assertNotIn("response", data)


if __name__ == "__main__":
    unittest.main()
