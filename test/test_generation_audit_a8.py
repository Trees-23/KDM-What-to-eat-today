import tempfile
import types
import unittest
from pathlib import Path

from rag_modules.generation_integration import Document, GenerationIntegrationModule
from rag_modules.rag_audit import RAGAuditManager


class FakeClient:
    def __init__(self, stream_error=False):
        self.stream_error = stream_error
        self.chat = types.SimpleNamespace(completions=types.SimpleNamespace(create=self.create))

    def create(self, **kwargs):
        if kwargs.get("stream"):
            if self.stream_error:
                raise RuntimeError("stream down")
            return iter(
                [
                    types.SimpleNamespace(
                        choices=[types.SimpleNamespace(delta=types.SimpleNamespace(content="流式"))]
                    ),
                    types.SimpleNamespace(
                        choices=[types.SimpleNamespace(delta=types.SimpleNamespace(content="回答"))]
                    ),
                ]
            )
        return types.SimpleNamespace(
            choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="非流式回答"))]
        )


class TestGenerationModule(GenerationIntegrationModule):
    def __init__(self, stream_error=False):
        self.model_name = "test-model"
        self.temperature = 0.2
        self.max_tokens = 128
        self.base_url = "https://api.example.com/v1"
        self.client = FakeClient(stream_error=stream_error)


class GenerationAuditA8Test(unittest.TestCase):
    def docs(self):
        return [
            Document(
                page_content="检索上下文A",
                metadata={"retrieval_level": "entity", "search_type": "entity_level", "recipe_name": "菜A"},
            )
        ]

    def test_non_stream_generation_records_context_config_and_response_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=1000).create_run()
            module = TestGenerationModule()

            answer = module.generate_adaptive_answer("问题", self.docs(), audit_run=audit)

            self.assertEqual(answer, "非流式回答")
            process_text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
            recall_text = (audit.run_dir / "recall_content.md").read_text(encoding="utf-8")
            self.assertIn("## Prompt Assembly", process_text)
            self.assertIn("- context_doc_count: 1", process_text)
            self.assertIn("## Generation Config", process_text)
            self.assertIn("- model_name: test-model", process_text)
            self.assertIn("- base_url_host: api.example.com", process_text)
            self.assertIn("## Generation Non-Stream", process_text)
            self.assertIn("- response_chars: 5", process_text)
            self.assertIn("## Final Output", process_text)
            self.assertIn("- timeout: 60.0", process_text)
            self.assertNotIn("非流式回答", process_text)
            self.assertIn("## Final Prompt Context", recall_text)
            self.assertIn("检索上下文A", recall_text)

    def test_non_stream_failure_is_not_returned_as_a_successful_answer(self):
        module = TestGenerationModule()

        def failing_create(**_kwargs):
            raise TimeoutError("upstream timeout")

        module.client.chat.completions.create = failing_create
        with self.assertRaisesRegex(RuntimeError, "GENERATION_NON_STREAM_FAILED"):
            module.generate_adaptive_answer("问题", self.docs(), timeout=12)

    def test_stream_generation_records_chunk_metrics_without_answer_body(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=1000).create_run()
            module = TestGenerationModule()

            chunks = list(module.generate_adaptive_answer_stream("问题", self.docs(), audit_run=audit))

            self.assertEqual(chunks, ["流式", "回答"])
            process_text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
            self.assertIn("## Generation Stream", process_text)
            self.assertIn("- chunk_count: 2", process_text)
            self.assertIn("- fallback_used: False", process_text)
            self.assertIn("- answer_chars: 4", process_text)
            self.assertNotIn("流式回答", process_text)


if __name__ == "__main__":
    unittest.main()
