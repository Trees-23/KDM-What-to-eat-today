import tempfile
import unittest
from pathlib import Path

from rag_modules.hybrid_retrieval import HybridRetrievalModule, RetrievalResult
from rag_modules.rag_audit import RAGAuditManager


class Config:
    llm_model = "test-llm"
    embedding_model = "test-embedding"
    enable_rerank = True
    rerank_model = "test-reranker"
    rerank_batch_size = 4
    milvus_collection_name = "test_collection"


class FakeReranker:
    def predict(self, pairs, batch_size):
        return [0.2, 0.9, 0.5, 0.1][: len(pairs)]


class TestHybridRetrieval(HybridRetrievalModule):
    def __init__(self, config):
        self.config = config
        self.milvus_module = None
        self.data_module = None
        self.llm_client = None
        self.driver = None
        self.bm25_retriever = None
        self.reranker = FakeReranker()
        self.reranker_load_failed = False
        self.graph_indexing = None
        self.graph_indexed = True

    def extract_query_keywords(self, query):
        return ["鸡肉"], ["低脂"]

    def entity_level_retrieval(self, entity_keywords, top_k=5):
        return [
            RetrievalResult(
                content="实体召回正文A\n关联图谱:\n- OUT REQUIRES 鸡肉",
                node_id="n1",
                node_type="Recipe",
                relevance_score=0.9,
                retrieval_level="entity",
                metadata={"entity_name": "菜A", "matched_keyword": "鸡肉"},
            ),
            RetrievalResult(
                content="实体召回正文B",
                node_id="n2",
                node_type="Recipe",
                relevance_score=0.8,
                retrieval_level="entity",
                metadata={"entity_name": "菜B", "matched_keyword": "鸡肉", "source": "neo4j_fallback"},
            ),
        ]

    def topic_level_retrieval(self, topic_keywords, top_k=5):
        return [
            RetrievalResult(
                content="主题召回正文C",
                node_id="n3",
                node_type="Recipe",
                relevance_score=0.95,
                retrieval_level="topic",
                metadata={"entity_name": "菜C", "matched_keyword": "低脂", "category": "健康"},
            )
        ]

    def vector_search_enhanced(self, query, top_k=5):
        from rag_modules.hybrid_retrieval import Document

        return [
            Document(
                page_content="向量召回正文D\n关联图谱:\n- IN MATCHES 低脂",
                metadata={"node_id": "n4", "recipe_name": "菜D", "score": 0.77, "category": "健康"},
            )
        ]


class HybridAuditA5Test(unittest.TestCase):
    def test_hybrid_search_writes_process_and_recall_sections(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=1000).create_run()
            module = TestHybridRetrieval(Config())

            docs = module.hybrid_search("推荐低脂鸡肉菜", top_k=2, audit_run=audit)

            self.assertEqual(len(docs), 2)
            self.assertEqual(docs[0].metadata["recipe_name"], "菜B")
            self.assertEqual(docs[1].metadata["recipe_name"], "菜C")

            process_text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
            recall_text = (audit.run_dir / "recall_content.md").read_text(encoding="utf-8")

            self.assertIn("## Hybrid Retrieval Config", process_text)
            self.assertIn("- top_k: 2", process_text)
            self.assertIn("- candidate_k: 8", process_text)
            self.assertIn("## Hybrid Keyword Extraction", process_text)
            self.assertIn("- entity_keywords: ['鸡肉']", process_text)
            self.assertIn("## Hybrid Branch Status / entity_level", process_text)
            self.assertIn("- fallback_count: 1", process_text)
            self.assertIn("## Hybrid Branch Summary", process_text)
            self.assertIn("- entity_count: 2", process_text)
            self.assertIn("- topic_count: 1", process_text)
            self.assertIn("- vector_count: 1", process_text)
            self.assertIn("## Hybrid Merge Dedup", process_text)
            self.assertIn("## Hybrid Rerank", process_text)
            self.assertIn("- load_success: True", process_text)
            self.assertIn("## Hybrid Diversity", process_text)
            self.assertIn("## Hybrid Retrieval Complete", process_text)

            self.assertIn("## Hybrid Retrieval / Entity Branch Raw Results", recall_text)
            self.assertIn("实体召回正文A", recall_text)
            self.assertIn("## Hybrid Retrieval / Topic Branch Raw Results", recall_text)
            self.assertIn("主题召回正文C", recall_text)
            self.assertIn("## Hybrid Retrieval / Vector Branch Raw Results", recall_text)
            self.assertIn("向量召回正文D", recall_text)
            self.assertIn("## Hybrid Retrieval / Merged Candidates", recall_text)
            self.assertIn("## Hybrid Retrieval / Rerank Input Texts", recall_text)
            self.assertIn("## Hybrid Retrieval / Reranked Results", recall_text)
            self.assertIn("## Hybrid Retrieval / Top-K Final Retrieval Context", recall_text)
            self.assertNotIn("duration_ms", recall_text)
            self.assertNotIn("test-reranker", recall_text)

    def test_hybrid_search_without_rerank_records_fallback_and_topk(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=1000).create_run()
            config = Config()
            config.enable_rerank = False
            module = TestHybridRetrieval(config)

            docs = module.hybrid_search("推荐低脂鸡肉菜", top_k=2, audit_run=audit)

            self.assertEqual(len(docs), 2)
            process_text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
            self.assertIn("- enabled: False", process_text)
            self.assertIn("- fallback_used: True", process_text)


if __name__ == "__main__":
    unittest.main()
