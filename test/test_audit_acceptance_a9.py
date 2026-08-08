import tempfile
import unittest
from pathlib import Path

from test_generation_audit_a8 import TestGenerationModule
from test_graph_audit_a6 import TestGraphRetrieval
from test_hybrid_audit_a5 import Config as HybridConfig
from test_hybrid_audit_a5 import TestHybridRetrieval
from test_router_audit_a4 import FakeRetrieval, RouterAuditA4Test
from test_web_audit_a3 import FakeRAGSystem, WebServiceHandler, install_fake_flask

from rag_modules.graph_rag_retrieval import QueryType
from rag_modules.rag_audit import RAGAuditManager


class AuditAcceptanceA9Test(unittest.TestCase):
    def make_audit(self, tmp):
        return RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=1200).create_run()

    def test_a9_directory_and_dual_file_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = self.make_audit(tmp)
            self.assertTrue(audit.run_dir.exists())
            self.assertTrue((audit.run_dir / "rag_process.md").exists())
            self.assertTrue((audit.run_dir / "recall_content.md").exists())

    def test_a9_hybrid_graph_combined_and_generation_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = self.make_audit(tmp)
            hybrid = TestHybridRetrieval(HybridConfig())
            hybrid_docs = hybrid.hybrid_search("推荐低脂鸡肉菜", top_k=2, audit_run=audit)

            graph = TestGraphRetrieval(QueryType.MULTI_HOP)
            graph_docs = graph.graph_rag_search("鸡肉适合搭配什么蔬菜", top_k=1, audit_run=audit)

            generation = TestGenerationModule()
            answer = generation.generate_adaptive_answer("问题", hybrid_docs + graph_docs, audit_run=audit)

            self.assertEqual(answer, "非流式回答")
            process_text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
            recall_text = (audit.run_dir / "recall_content.md").read_text(encoding="utf-8")
            self.assertIn("## Hybrid Retrieval Config", process_text)
            self.assertIn("## Graph Query Understanding", process_text)
            self.assertIn("## Prompt Assembly", process_text)
            self.assertIn("## Hybrid Retrieval / Top-K Final Retrieval Context", recall_text)
            self.assertIn("## Graph Retrieval / Path Top-K", recall_text)
            self.assertIn("## Final Prompt Context", recall_text)

    def test_a9_stream_and_cache_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            install_fake_flask({"message": "重复问题", "session_id": "s1"})
            rag_system = FakeRAGSystem(Path(tmp), cached_response="cached answer")
            handler = WebServiceHandler(rag_system)

            response = handler._handle_stream_request()
            chunks = list(response.iterable)

            self.assertIn("data: [DONE]\n\n", chunks)
            latest = sorted(Path(tmp).iterdir())[-1]
            process_text = (latest / "rag_process.md").read_text(encoding="utf-8")
            recall_text = (latest / "recall_content.md").read_text(encoding="utf-8")
            self.assertIn("- cache_hit: True", process_text)
            self.assertIn("- final_source: cache", process_text)
            self.assertNotIn("cached answer", recall_text)

    def test_a9_combined_partial_failure_acceptance(self):
        case = RouterAuditA4Test()
        with tempfile.TemporaryDirectory() as tmp:
            audit = self.make_audit(tmp)
            router = case.make_router(
                "combined",
                traditional=FakeRetrieval("traditional"),
                graph=FakeRetrieval("graph", error=True),
            )

            docs, _ = router.route_query("组合异常问题", top_k=3, audit_run=audit)

            self.assertGreaterEqual(len(docs), 1)
            process_text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
            # `combined` 已被路由器兼容归一为 graph_rag；图分支失败后走传统混合检索，
            # 不应再期待已删除的 combined 子分支审计事件。
            self.assertIn("- stage: route_query", process_text)
            self.assertIn("- fallback_strategy: hybrid_traditional", process_text)
            self.assertNotIn("- stage: combined_graph_branch", process_text)


if __name__ == "__main__":
    unittest.main()
