import os
import re
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

from rag_modules.rag_audit import (
    NULL_AUDIT_RUN,
    PROCESS_FILE,
    RECALL_FILE,
    RAGAuditManager,
    sanitize_value,
)


@dataclass
class Document:
    page_content: str
    metadata: dict = field(default_factory=dict)


class RAGAuditA1Test(unittest.TestCase):
    def test_create_run_initializes_unique_directory_and_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            manager = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=40)
            audit = manager.create_run()

            self.assertTrue(audit.enabled)
            self.assertTrue(audit.run_dir.exists())
            self.assertRegex(audit.audit_id, r"^\d{8}_\d{6}_\d{3}_[0-9a-f]{8}$")
            self.assertTrue((audit.run_dir / PROCESS_FILE).exists())
            self.assertTrue((audit.run_dir / RECALL_FILE).exists())

            process_text = (audit.run_dir / PROCESS_FILE).read_text(encoding="utf-8")
            recall_text = (audit.run_dir / RECALL_FILE).read_text(encoding="utf-8")
            self.assertIn("# RAG Process", process_text)
            self.assertIn(f"audit_id: {audit.audit_id}", process_text)
            self.assertIn("# Recall Content", recall_text)
            self.assertIn(f"audit_id: {audit.audit_id}", recall_text)

    def test_disabled_manager_does_not_create_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            manager = RAGAuditManager(enabled=False, root_dir=Path(tmp))
            audit = manager.create_run()
            self.assertIs(audit, NULL_AUDIT_RUN)
            self.assertEqual(os.listdir(tmp), [])

    def test_concurrent_runs_do_not_collide(self):
        with tempfile.TemporaryDirectory() as tmp:
            manager = RAGAuditManager(enabled=True, root_dir=Path(tmp))
            with ThreadPoolExecutor(max_workers=8) as executor:
                audits = list(executor.map(lambda _: manager.create_run(), range(24)))

            audit_ids = [audit.audit_id for audit in audits]
            self.assertEqual(len(audit_ids), len(set(audit_ids)))
            self.assertEqual(len(list(Path(tmp).iterdir())), 24)

    def test_content_truncation_is_marked_in_recall_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=12).create_run()
            audit.write_documents(
                "Truncation Check",
                [Document(page_content="abcdefghijklmnopqrstuvwxyz", metadata={"recipe_name": "x"})],
                "unit",
            )
            recall_text = (audit.run_dir / RECALL_FILE).read_text(encoding="utf-8")
            self.assertIn("[TRUNCATED original_chars=26", recall_text)

    def test_process_sanitizes_sensitive_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp)).create_run()
            audit.append_process(
                "Sensitive Check",
                {
                    "OPENAI_API_KEY": "sk-secretsecret",
                    "Authorization": "Bearer token123",
                    "base_url": "https://example.com/v1",
                },
            )
            process_text = (audit.run_dir / PROCESS_FILE).read_text(encoding="utf-8")
            self.assertNotIn("sk-secretsecret", process_text)
            self.assertNotIn("Bearer token123", process_text)
            self.assertNotIn("Authorization", process_text)
            self.assertNotIn("Bearer", process_text)

    def test_write_failure_is_downgraded(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp)).create_run()
            audit.process_path = audit.run_dir
            audit.append_process("Should Not Raise", {"stage": "write_failure"})

    def test_sanitize_value_redacts_sensitive_dict_keys(self):
        redacted = sanitize_value({"password": "secret", "normal": "Bearer abc"})
        self.assertEqual(redacted["redacted_field"], "[REDACTED]")
        self.assertTrue(re.match(r"\[REDACTED_AUTH\]", redacted["normal"]))


if __name__ == "__main__":
    unittest.main()
