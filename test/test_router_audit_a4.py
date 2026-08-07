import json
import tempfile
import types
import unittest
from pathlib import Path

from rag_modules.intelligent_query_router import IntelligentQueryRouter, SearchStrategy
from rag_modules.rag_audit import RAGAuditManager


class FakeChoice:
    def __init__(self, content):
        self.message = types.SimpleNamespace(content=content)


class FakeLLMClient:
    def __init__(self, payload=None, error=None):
        self.payload = payload or {}
        self.error = error
        self.chat = types.SimpleNamespace(completions=types.SimpleNamespace(create=self.create))

    def create(self, **_kwargs):
        if self.error:
            raise self.error
        return types.SimpleNamespace(choices=[FakeChoice(json.dumps(self.payload, ensure_ascii=False))])


class FakeRetrieval:
    def __init__(self, name, error=False):
        self.name = name
        self.error = error
        self.calls = []

    def hybrid_search(self, query, top_k, audit_run=None):
        self.calls.append(("hybrid", query, top_k))
        if self.error:
            raise RuntimeError(f"{self.name} failed")
        return [types.SimpleNamespace(page_content=f"{self.name}-{i}", metadata={}) for i in range(top_k)]

    def graph_rag_search(self, query, top_k, audit_run=None):
        self.calls.append(("graph", query, top_k))
        if self.error:
            raise RuntimeError(f"{self.name} failed")
        return [types.SimpleNamespace(page_content=f"{self.name}-{i}", metadata={}) for i in range(top_k)]


class Config:
    llm_model = "test-model"


class RouterAuditA4Test(unittest.TestCase):
    def make_audit(self, tmp):
        return RAGAuditManager(enabled=True, root_dir=Path(tmp)).create_run()

    def process_text(self, audit):
        return (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")

    def recall_text(self, audit):
        return (audit.run_dir / "recall_content.md").read_text(encoding="utf-8")

    def make_router(
        self,
        strategy,
        llm_error=None,
        traditional=None,
        graph=None,
        query_complexity=0.6,
        relationship_intensity=0.7,
        reasoning_required=True,
        entity_count=2,
    ):
        payload = {
            "query_complexity": query_complexity,
            "relationship_intensity": relationship_intensity,
            "reasoning_required": reasoning_required,
            "entity_count": entity_count,
            "recommended_strategy": strategy,
            "confidence": 0.88,
            "reasoning": "需要关系推理",
        }
        return IntelligentQueryRouter(
            traditional or FakeRetrieval("traditional"),
            graph or FakeRetrieval("graph"),
            FakeLLMClient(payload=payload, error=llm_error),
            Config(),
        )

    def test_llm_analysis_and_graph_route_are_recorded(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = self.make_audit(tmp)
            graph = FakeRetrieval("graph")
            router = self.make_router("graph_rag", graph=graph)

            docs, analysis = router.route_query("鸡肉适合搭配什么蔬菜", top_k=2, audit_run=audit)

            self.assertEqual(analysis.recommended_strategy, SearchStrategy.GRAPH_RAG)
            self.assertEqual(len(docs), 2)
            text = self.process_text(audit)
            self.assertIn("- analysis_input_query_length:", text)
            self.assertIn("- llm_model: test-model", text)
            self.assertIn("- analysis_mode: llm", text)
            self.assertIn("- strategy: graph_rag", text)
            self.assertIn("- selected_strategy: graph_rag", text)
            self.assertIn("- route_stats_before:", text)
            self.assertIn("- route_stats_after:", text)
            self.assertNotIn("鸡肉适合搭配什么蔬菜\n", text)

    def test_rule_fallback_analysis_is_recorded_when_llm_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = self.make_audit(tmp)
            router = self.make_router("hybrid_traditional", llm_error=RuntimeError("llm down"))

            docs, analysis = router.route_query("红烧肉怎么做", top_k=1, audit_run=audit)

            self.assertEqual(len(docs), 1)
            text = self.process_text(audit)
            self.assertIn("- analysis_mode: rule_fallback", text)
            self.assertIn("- error_type: RuntimeError", text)
            self.assertIn("- fallback_strategy:", text)

    def test_hybrid_and_legacy_combined_routes_are_recorded(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit_hybrid = self.make_audit(tmp)
            hybrid_router = self.make_router("hybrid_traditional")
            hybrid_router.route_query("西红柿营养", top_k=1, audit_run=audit_hybrid)
            self.assertIn("- selected_strategy: hybrid_traditional", self.process_text(audit_hybrid))

            audit_legacy_combined = self.make_audit(tmp)
            legacy_combined_router = self.make_router(
                "combined",
                query_complexity=0.75,
                relationship_intensity=0.75,
                entity_count=3,
            )
            docs, analysis = legacy_combined_router.route_query(
                "推荐几个低脂菜并说明食材关系",
                top_k=3,
                audit_run=audit_legacy_combined,
            )
            combined_text = self.process_text(audit_legacy_combined)
            recall_text = self.recall_text(audit_legacy_combined)
            self.assertEqual(analysis.recommended_strategy, SearchStrategy.GRAPH_RAG)
            self.assertEqual(len(docs), 3)
            self.assertIn("- selected_strategy: graph_rag", combined_text)
            self.assertNotIn("- selected_strategy: combined", combined_text)
            self.assertNotIn("## Combined Retrieval Allocation", combined_text)
            self.assertNotIn("## Combined Retrieval / Final Documents", recall_text)

    def test_legacy_combined_graph_failure_falls_back_to_hybrid(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = self.make_audit(tmp)
            graph = FakeRetrieval("graph", error=True)
            traditional = FakeRetrieval("traditional")
            router = self.make_router(
                "combined",
                traditional=traditional,
                graph=graph,
                query_complexity=0.75,
                relationship_intensity=0.75,
                entity_count=3,
            )

            docs, analysis = router.route_query("组合检索问题", top_k=3, audit_run=audit)

            self.assertEqual(analysis.recommended_strategy, SearchStrategy.GRAPH_RAG)
            self.assertEqual(len(docs), 3)
            self.assertEqual(traditional.calls[-1], ("hybrid", "组合检索问题", 3))
            text = self.process_text(audit)
            recall_text = self.recall_text(audit)
            self.assertIn("## Errors", text)
            self.assertIn("- stage: route_query", text)
            self.assertIn("- fallback_strategy: hybrid_traditional", text)
            self.assertNotIn("## Combined Retrieval / Final Documents", recall_text)

    def test_route_exception_falls_back_to_hybrid_and_records_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = self.make_audit(tmp)
            graph = FakeRetrieval("graph", error=True)
            traditional = FakeRetrieval("traditional")
            router = self.make_router("graph_rag", traditional=traditional, graph=graph)

            docs, analysis = router.route_query("复杂关系问题", top_k=2, audit_run=audit)

            self.assertEqual(analysis.recommended_strategy, SearchStrategy.GRAPH_RAG)
            self.assertEqual(len(docs), 2)
            self.assertEqual(traditional.calls[-1], ("hybrid", "复杂关系问题", 2))
            text = self.process_text(audit)
            self.assertIn("- stage: route_query", text)
            self.assertIn("- error_type: RuntimeError", text)
            self.assertIn("- fallback_strategy: hybrid_traditional", text)
            self.assertIn("- status: fallback_completed", text)


if __name__ == "__main__":
    unittest.main()
