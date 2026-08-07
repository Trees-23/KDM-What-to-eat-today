"""基于图数据库的RAG模块包。"""

__all__ = [
    "GraphDataPreparationModule",
    "MilvusIndexConstructionModule",
    "HybridRetrievalModule",
    "GenerationIntegrationModule",
]


def __getattr__(name):
    if name == "GraphDataPreparationModule":
        from .graph_data_preparation import GraphDataPreparationModule

        return GraphDataPreparationModule
    if name == "MilvusIndexConstructionModule":
        from .milvus_index_construction import MilvusIndexConstructionModule

        return MilvusIndexConstructionModule
    if name == "HybridRetrievalModule":
        from .hybrid_retrieval import HybridRetrievalModule

        return HybridRetrievalModule
    if name == "GenerationIntegrationModule":
        from .generation_integration import GenerationIntegrationModule

        return GenerationIntegrationModule
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
