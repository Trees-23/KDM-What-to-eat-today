import tempfile
import unittest
from dataclasses import dataclass, field
from pathlib import Path

from rag_modules.rag_audit import PROCESS_FILE, RECALL_FILE, RAGAuditManager


@dataclass
class Document:
    page_content: str
    metadata: dict = field(default_factory=dict)


class RAGAuditA2Test(unittest.TestCase):
    def test_recall_document_serialization_contains_content_and_metadata_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=200).create_run()
            audit.write_documents(
                "Hybrid Retrieval / Entity Branch Raw Results",
                [
                    Document(
                        page_content="宫保鸡丁做法正文",
                        metadata={"node_id": "n1", "recipe_name": "宫保鸡丁", "score": 0.91},
                    )
                ],
                "entity_level",
            )

            recall_text = (audit.run_dir / RECALL_FILE).read_text(encoding="utf-8")
            self.assertIn("## Hybrid Retrieval / Entity Branch Raw Results", recall_text)
            self.assertIn("### result_order=0", recall_text)
            self.assertIn("source: entity_level", recall_text)
            self.assertIn("metadata_summary: node_id=n1, recipe_name=宫保鸡丁, score=0.91", recall_text)
            self.assertIn("```text\n宫保鸡丁做法正文\n```", recall_text)

    def test_process_event_format_contains_stage_status_and_duration(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp)).create_run()
            audit.record_event("cache_check", status="completed", cache_hit=False)
            process_text = (audit.run_dir / PROCESS_FILE).read_text(encoding="utf-8")
            self.assertIn("## Event / cache_check", process_text)
            self.assertIn("- stage: cache_check", process_text)
            self.assertIn("- status: completed", process_text)
            self.assertRegex(process_text, r"- duration_ms: \d+")
            self.assertIn("- cache_hit: False", process_text)

    def test_process_redacts_body_like_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp)).create_run()
            audit.append_process(
                "Body Redaction",
                {
                    "document_content": "这是一段不应该进入 process 的召回正文",
                    "final_context": "这是一段不应该进入 process 的最终上下文",
                    "answer": "这是一段不应该进入 process 的完整回答",
                    "response_chars": 12,
                },
            )
            process_text = (audit.run_dir / PROCESS_FILE).read_text(encoding="utf-8")
            self.assertNotIn("召回正文", process_text)
            self.assertNotIn("最终上下文", process_text)
            self.assertNotIn("完整回答", process_text)
            self.assertIn("[BODY_REDACTED chars=", process_text)
            self.assertIn("- response_chars: 12", process_text)

    def test_recall_sanitizes_sensitive_literals_but_allows_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=500).create_run()
            audit.write_documents(
                "Sensitive Recall",
                [Document(page_content="正文 sk-secretsecret 和 Bearer token123", metadata={})],
                "unit",
            )
            recall_text = (audit.run_dir / RECALL_FILE).read_text(encoding="utf-8")
            self.assertIn("正文", recall_text)
            self.assertNotIn("sk-secretsecret", recall_text)
            self.assertNotIn("Bearer token123", recall_text)

    def test_recall_file_keeps_process_fields_outside_content_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=500).create_run()
            audit.write_documents("Clean Recall", [Document(page_content="只有正文", metadata={})], "unit")
            recall_text = (audit.run_dir / RECALL_FILE).read_text(encoding="utf-8")
            self.assertNotIn("duration_ms", recall_text)
            self.assertNotIn("error_type", recall_text)
            self.assertNotIn("llm_model", recall_text)


if __name__ == "__main__":
    unittest.main()
