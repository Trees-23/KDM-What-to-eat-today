import tempfile
import unittest
from pathlib import Path

from rag_modules.graph_rag_retrieval import (
    GraphPath,
    GraphQuery,
    GraphRAGRetrieval,
    KnowledgeSubgraph,
    QueryType,
)
from rag_modules.rag_audit import RAGAuditManager


class Config:
    llm_model = "test-graph-llm"


class TestGraphRetrieval(GraphRAGRetrieval):
    def __init__(self, query_type):
        self.config = Config()
        self.llm_client = None
        self.driver = object()
        self.query_type = query_type
        self.entity_cache = {}
        self.relation_cache = {}
        self.subgraph_cache = {}

    def understand_graph_query(self, query):
        return GraphQuery(
            query_type=self.query_type,
            source_entities=["鸡肉"],
            target_entities=["蔬菜"],
            relation_types=["REQUIRES"],
            max_depth=2,
            max_nodes=10,
        )

    def multi_hop_traversal(self, graph_query):
        return [
            GraphPath(
                nodes=[
                    {"name": "鸡肉", "labels": ["Ingredient"]},
                    {"name": "宫保鸡丁", "labels": ["Recipe"]},
                    {"name": "黄瓜", "labels": ["Ingredient"]},
                ],
                relationships=[
                    {"type": "REQUIRES", "start_name": "宫保鸡丁", "end_name": "鸡肉"},
                    {"type": "REQUIRES", "start_name": "宫保鸡丁", "end_name": "黄瓜"},
                ],
                path_length=2,
                relevance_score=0.92,
                path_type="multi_hop",
            )
        ]

    def extract_knowledge_subgraph(self, graph_query):
        return KnowledgeSubgraph(
            central_nodes=[{"name": "川菜", "labels": ["Category"]}],
            connected_nodes=[
                {"name": "麻婆豆腐", "labels": ["Recipe"]},
                {"name": "辣椒", "labels": ["Ingredient"]},
            ],
            relationships=[
                {"type": "BELONGS_TO_CATEGORY", "start_name": "麻婆豆腐", "end_name": "川菜"},
                {"type": "REQUIRES", "start_name": "麻婆豆腐", "end_name": "辣椒"},
            ],
            graph_metrics={"density": 0.5},
            reasoning_chains=["候选链：川菜 -> 麻婆豆腐 -> 辣椒"],
        )

    def graph_structure_reasoning(self, subgraph, query):
        subgraph.reasoning_chains = ["接受链：川菜通过麻婆豆腐体现麻辣特点"]
        return subgraph.reasoning_chains


class GraphAuditA6Test(unittest.TestCase):
    def test_path_graph_search_writes_path_sections(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=1000).create_run()
            module = TestGraphRetrieval(QueryType.MULTI_HOP)

            docs = module.graph_rag_search("鸡肉适合搭配什么蔬菜", top_k=1, audit_run=audit)

            self.assertEqual(len(docs), 1)
            self.assertEqual(docs[0].metadata["search_type"], "graph_path")

            process_text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
            recall_text = (audit.run_dir / "recall_content.md").read_text(encoding="utf-8")
            self.assertIn("## Graph Query Understanding", process_text)
            self.assertIn("- query_type: multi_hop", process_text)
            self.assertIn("## Graph Path Retrieval Config", process_text)
            self.assertIn("## Graph Retrieval Complete", process_text)
            self.assertIn("- mode: path", process_text)
            self.assertIn("## Graph Retrieval / Path Raw Results", recall_text)
            self.assertIn("图路径概览", recall_text)
            self.assertIn("## Graph Retrieval / Path Ranked Results", recall_text)
            self.assertIn("## Graph Retrieval / Path Top-K", recall_text)

    def test_subgraph_search_writes_subgraph_and_reasoning_sections(self):
        with tempfile.TemporaryDirectory() as tmp:
            audit = RAGAuditManager(enabled=True, root_dir=Path(tmp), max_content_chars=1200).create_run()
            module = TestGraphRetrieval(QueryType.SUBGRAPH)

            docs = module.graph_rag_search("川菜有什么特色", top_k=1, audit_run=audit)

            self.assertEqual(len(docs), 1)
            self.assertEqual(docs[0].metadata["search_type"], "knowledge_subgraph")

            process_text = (audit.run_dir / "rag_process.md").read_text(encoding="utf-8")
            recall_text = (audit.run_dir / "recall_content.md").read_text(encoding="utf-8")
            self.assertIn("## Graph Subgraph Extraction Config", process_text)
            self.assertIn("## Graph Subgraph Status", process_text)
            self.assertIn("## Graph Reasoning Patterns", process_text)
            self.assertIn("## Graph Reasoning Validation", process_text)
            self.assertIn("- accepted_count: 1", process_text)
            self.assertIn("- mode: subgraph", process_text)
            self.assertIn("## Graph Retrieval / Subgraph Raw Content", recall_text)
            self.assertIn("知识子图主题", recall_text)
            self.assertIn("## Graph Retrieval / Candidate Reasoning Chains", recall_text)
            self.assertIn("候选链", recall_text)
            self.assertIn("## Graph Retrieval / Accepted Reasoning Chains", recall_text)
            self.assertIn("接受链", recall_text)
            self.assertIn("## Graph Retrieval / Subgraph Documents", recall_text)


if __name__ == "__main__":
    unittest.main()
