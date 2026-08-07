import importlib.util
import sys
import types
from pathlib import Path


class Document:
    def __init__(self, page_content="", metadata=None):
        self.page_content = page_content
        self.metadata = metadata or {}


def load_hybrid_module():
    langchain_core = types.ModuleType("langchain_core")
    documents = types.ModuleType("langchain_core.documents")
    documents.Document = Document
    sys.modules.setdefault("langchain_core", langchain_core)
    sys.modules["langchain_core.documents"] = documents

    langchain_community = types.ModuleType("langchain_community")
    retrievers = types.ModuleType("langchain_community.retrievers")
    retrievers.BM25Retriever = object
    sys.modules.setdefault("langchain_community", langchain_community)
    sys.modules["langchain_community.retrievers"] = retrievers

    neo4j = types.ModuleType("neo4j")
    neo4j.GraphDatabase = object
    sys.modules["neo4j"] = neo4j

    graph_indexing = types.ModuleType("rag_modules.graph_indexing")
    graph_indexing.GraphIndexingModule = object
    sys.modules["rag_modules.graph_indexing"] = graph_indexing

    package = types.ModuleType("rag_modules")
    package.__path__ = []
    sys.modules.setdefault("rag_modules", package)

    module_path = Path(__file__).resolve().parents[1] / "rag_modules" / "hybrid_retrieval.py"
    spec = importlib.util.spec_from_file_location(
        "rag_modules.hybrid_retrieval",
        module_path,
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["rag_modules.hybrid_retrieval"] = module
    spec.loader.exec_module(module)
    return module


def make_doc(node_id, name, category="", content=None):
    return Document(
        page_content=content or f"{name} content",
        metadata={
            "node_id": node_id,
            "recipe_name": name,
            "category": category,
        },
    )


class Config:
    enable_rerank = True
    rerank_batch_size = 4


class FakeReranker:
    def __init__(self, scores):
        self.scores = scores
        self.pairs = None
        self.batch_size = None

    def predict(self, pairs, batch_size=8):
        self.pairs = pairs
        self.batch_size = batch_size
        return self.scores


def test_direct_merge_deduplicates_and_keeps_richer_content():
    module = load_hybrid_module()
    retriever = module.HybridRetrievalModule.__new__(module.HybridRetrievalModule)

    merged = retriever._merge_retrieved_documents(
        {
            "entity_level": [
                make_doc("r1", "宫保鸡丁", "川菜"),
                make_doc("r2", "麻婆豆腐", "川菜"),
            ],
            "topic_level": [
                make_doc("r3", "水煮鱼", "川菜"),
                make_doc("r1", "宫保鸡丁", "川菜", content="宫保鸡丁 richer content with topic details"),
            ],
            "vector_enhanced": [
                make_doc("r4", "番茄炒蛋", "家常菜"),
                make_doc("r1", "宫保鸡丁", "川菜"),
            ],
        },
    )

    by_id = {doc.metadata["node_id"]: doc for doc in merged}
    assert "r1" in by_id
    assert by_id["r1"].metadata["source_coverage"] == 3
    assert by_id["r1"].metadata["merge_sources"] == [
        "entity_level",
        "topic_level",
        "vector_enhanced",
    ]
    assert "richer content" in by_id["r1"].page_content
    assert [doc.metadata["merge_order"] for doc in merged] == list(range(len(merged)))


def test_apply_diversity_limits_repeated_categories():
    module = load_hybrid_module()
    retriever = module.HybridRetrievalModule.__new__(module.HybridRetrievalModule)

    selected = retriever._apply_diversity(
        [
            make_doc("s1", "川菜1", "川菜"),
            make_doc("s2", "川菜2", "川菜"),
            make_doc("s3", "川菜3", "川菜"),
            make_doc("h1", "家常菜1", "家常菜"),
        ],
        top_k=3
    )

    categories = [doc.metadata.get("category") for doc in selected]
    assert categories.count("川菜") <= 2
    assert "家常菜" in categories
    assert [doc.metadata["result_order"] for doc in selected] == [0, 1, 2]


def test_rerank_documents_uses_cross_encoder_scores_after_direct_merge():
    module = load_hybrid_module()
    retriever = module.HybridRetrievalModule.__new__(module.HybridRetrievalModule)
    retriever.config = Config()
    retriever.reranker = FakeReranker([0.1, 0.95, 0.3])
    retriever.reranker_load_failed = False

    docs = [
        make_doc("r1", "普通沙拉", "健康餐"),
        make_doc("r2", "鸡胸肉高蛋白晚餐", "健康餐"),
        make_doc("r3", "番茄炒蛋", "家常菜"),
    ]

    reranked = retriever._rerank_documents("推荐高蛋白减脂晚餐", docs, top_k=2)

    assert [doc.metadata["node_id"] for doc in reranked] == ["r2", "r3"]
    assert reranked[0].metadata["rerank_score"] == 0.95
    assert reranked[0].metadata["search_method"] == "direct_merge_bge_rerank"
    assert reranked[0].metadata["rerank_order"] == 0
    assert retriever.reranker.batch_size == 4


def test_rerank_documents_falls_back_to_merge_order_when_disabled():
    module = load_hybrid_module()
    retriever = module.HybridRetrievalModule.__new__(module.HybridRetrievalModule)
    retriever.config = type("DisabledConfig", (), {"enable_rerank": False})()
    retriever.reranker = FakeReranker([0.99, 0.01])
    retriever.reranker_load_failed = False

    docs = [
        make_doc("r1", "合并第一", "川菜"),
        make_doc("r2", "合并第二", "家常菜"),
    ]

    reranked = retriever._rerank_documents("任意问题", docs, top_k=2)

    assert [doc.metadata["node_id"] for doc in reranked] == ["r1", "r2"]
    assert "rerank_score" not in reranked[0].metadata
