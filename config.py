"""
基于图数据库的RAG系统配置文件
"""

import os
import json
import hashlib
from dataclasses import dataclass
from typing import Dict, Any

from rag_modules.nutrition_policy import SOFT_PREFERENCE_POLICY


def _env_bool(name: str, default: bool) -> bool:
    """读取布尔环境变量，支持常见 true/false 写法。"""
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _strict_nutrition_enabled() -> bool:
    """严格营养开关只能在治理策略明确允许时生效。"""
    return _env_bool("RETRIEVAL_STRICT_NUTRITION_ENABLED", False) and SOFT_PREFERENCE_POLICY.strict_mode_available


def _env_rollout_percentage(name: str, default: float = 0.0) -> float:
    """读取 0..100 的渐进流量比例；非法配置保持关闭。"""
    value = os.getenv(name)
    if value is None:
        return default
    try:
        percentage = float(value)
    except ValueError:
        return default
    return percentage if 0.0 <= percentage <= 100.0 else default


def _env_rollout_allowlist(name: str) -> tuple[str, ...]:
    """读取以逗号分隔的稳定请求标识，不接受空白项。"""
    return tuple(item.strip() for item in os.getenv(name, "").split(",") if item.strip())


@dataclass
class GraphRAGConfig:
    """基于图数据库的RAG系统配置类"""

    # Neo4j数据库配置
    neo4j_uri: str = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    neo4j_user: str = os.getenv("NEO4J_USER", "neo4j")
    neo4j_password: str = os.getenv("NEO4J_PASSWORD", "all-in-rag")
    neo4j_database: str = os.getenv("NEO4J_DATABASE", "neo4j")

    # Milvus配置
    milvus_host: str = os.getenv("MILVUS_HOST", "localhost")
    milvus_port: int = int(os.getenv("MILVUS_PORT", "19530"))
    milvus_collection_name: str = "cooking_knowledge"
    milvus_dimension: int = 512  # BGE-small-zh-v1.5的向量维度

    # 模型配置
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-zh-v1.5")
    llm_model: str = os.getenv("LLM_MODEL", "moonshot-v1-8k")
    enable_rerank: bool = _env_bool("ENABLE_RERANK", True)
    rerank_model: str = os.getenv("RERANK_MODEL", "BAAI/bge-reranker-base")
    rerank_batch_size: int = int(os.getenv("RERANK_BATCH_SIZE", "8"))

    # 检索配置
    top_k: int = 5

    # RAG审计配置
    enable_rag_audit: bool = _env_bool("ENABLE_RAG_AUDIT", False)
    rag_audit_root_dir: str = os.getenv("RAG_AUDIT_ROOT_DIR", os.path.join(os.path.dirname(__file__), "run"))
    rag_audit_max_content_chars: int = int(os.getenv("RAG_AUDIT_MAX_CONTENT_CHARS", "4000"))
    rag_experiment_id: str = os.getenv("RAG_EXPERIMENT_ID", "baseline")
    rag_variant_name: str = os.getenv("RAG_VARIANT_NAME", "default")

    # 生成配置
    temperature: float = 0.1
    max_tokens: int = 2048

    # 图数据处理配置
    chunk_size: int = 500
    chunk_overlap: int = 50
    max_graph_depth: int = 2  # 图遍历最大深度

    # ParentDocumentStore（阶段 1，默认关闭，仅健康检查）
    retrieval_parent_store_enabled: bool = _env_bool("RETRIEVAL_PARENT_STORE_ENABLED", False)
    parent_store_path: str = os.getenv(
        "RETRIEVAL_PARENT_STORE_PATH",
        os.path.join(os.path.dirname(__file__), "run", "retrieval"),
    )
    parent_store_active_pointer: str = os.getenv(
        "RETRIEVAL_PARENT_STORE_ACTIVE_POINTER",
        os.path.join(os.path.dirname(__file__), "run", "retrieval", "parent_store.active"),
    )
    # 阶段 2：实体直达必须同时依赖已启用且健康的 PDS，默认保持关闭。
    retrieval_entity_direct_enabled: bool = _env_bool("RETRIEVAL_ENTITY_DIRECT_ENABLED", False)
    # 阶段 3：固定 QueryPlan 与目标化图查询，默认保持关闭。
    retrieval_query_plan_enabled: bool = _env_bool("RETRIEVAL_QUERY_PLAN_ENABLED", False)
    retrieval_targeted_graph_enabled: bool = _env_bool("RETRIEVAL_TARGETED_GRAPH_ENABLED", False)
    # 阶段 4：仅允许联合 artifact manifest 指向全新 V2 collection，默认关闭。
    retrieval_milvus_v2_enabled: bool = _env_bool("RETRIEVAL_MILVUS_V2_ENABLED", False)
    # 阶段 6：默认不将任何请求分流至新路径；allowlist 优先于流量比例。
    retrieval_new_path_allowlist: tuple[str, ...] = _env_rollout_allowlist("RETRIEVAL_NEW_PATH_ALLOWLIST")
    retrieval_new_path_traffic_percent: float = _env_rollout_percentage("RETRIEVAL_NEW_PATH_TRAFFIC_PERCENT")
    # 阶段 6：新路径无法安全完成时，默认保留现有 Router 作为兼容回退。
    retrieval_legacy_fallback_enabled: bool = _env_bool("RETRIEVAL_LEGACY_FALLBACK_ENABLED", True)
    # 意图规划独立开关。启用后 new 路径必须 fail-closed，不能回退旧 Router。
    retrieval_intent_planner_enabled: bool = _env_bool("RETRIEVAL_INTENT_PLANNER_ENABLED", False)
    retrieval_intent_planner_version: str = os.getenv("RETRIEVAL_INTENT_PLANNER_VERSION", "v1")
    retrieval_intent_planner_timeout_seconds: float = float(os.getenv("RETRIEVAL_INTENT_PLANNER_TIMEOUT_SECONDS", "30"))
    retrieval_milvus_database: str = os.getenv("RETRIEVAL_MILVUS_DATABASE", "default")
    retrieval_milvus_collection: str = os.getenv("RETRIEVAL_MILVUS_COLLECTION", "")
    retrieval_artifact_manifest_path: str = os.getenv(
        "RETRIEVAL_ARTIFACT_MANIFEST_PATH",
        os.path.join(os.path.dirname(__file__), "run", "retrieval", "retrieval_artifact_manifest.json"),
    )
    # 阶段 5：当前软偏好策略没有受治理营养源，因此即使环境变量为 true 也保持关闭。
    retrieval_strict_nutrition_enabled: bool = _strict_nutrition_enabled()

    def __post_init__(self):
        """严格营养开关始终受当前治理策略约束。"""
        self.retrieval_strict_nutrition_enabled = bool(
            self.retrieval_strict_nutrition_enabled and SOFT_PREFERENCE_POLICY.strict_mode_available
        )
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'GraphRAGConfig':
        """从字典创建配置对象"""
        return cls(**config_dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'neo4j_uri': self.neo4j_uri,
            'neo4j_user': self.neo4j_user,
            'neo4j_password': self.neo4j_password,
            'neo4j_database': self.neo4j_database,
            'milvus_host': self.milvus_host,
            'milvus_port': self.milvus_port,
            'milvus_collection_name': self.milvus_collection_name,
            'milvus_dimension': self.milvus_dimension,
            'embedding_model': self.embedding_model,
            'llm_model': self.llm_model,
            'enable_rerank': self.enable_rerank,
            'rerank_model': self.rerank_model,
            'rerank_batch_size': self.rerank_batch_size,
            'top_k': self.top_k,
            'enable_rag_audit': self.enable_rag_audit,
            'rag_audit_root_dir': self.rag_audit_root_dir,
            'rag_audit_max_content_chars': self.rag_audit_max_content_chars,
            'rag_experiment_id': self.rag_experiment_id,
            'rag_variant_name': self.rag_variant_name,

            'temperature': self.temperature,
            'max_tokens': self.max_tokens,
            'chunk_size': self.chunk_size,
            'chunk_overlap': self.chunk_overlap,
            'max_graph_depth': self.max_graph_depth,
            'retrieval_parent_store_enabled': self.retrieval_parent_store_enabled,
            'parent_store_path': self.parent_store_path,
            'parent_store_active_pointer': self.parent_store_active_pointer,
            'retrieval_entity_direct_enabled': self.retrieval_entity_direct_enabled,
            'retrieval_query_plan_enabled': self.retrieval_query_plan_enabled,
            'retrieval_targeted_graph_enabled': self.retrieval_targeted_graph_enabled,
            'retrieval_milvus_v2_enabled': self.retrieval_milvus_v2_enabled,
            'retrieval_new_path_allowlist': self.retrieval_new_path_allowlist,
            'retrieval_new_path_traffic_percent': self.retrieval_new_path_traffic_percent,
            'retrieval_legacy_fallback_enabled': self.retrieval_legacy_fallback_enabled,
            'retrieval_intent_planner_enabled': self.retrieval_intent_planner_enabled,
            'retrieval_intent_planner_version': self.retrieval_intent_planner_version,
            'retrieval_intent_planner_timeout_seconds': self.retrieval_intent_planner_timeout_seconds,
            'retrieval_milvus_database': self.retrieval_milvus_database,
            'retrieval_milvus_collection': self.retrieval_milvus_collection,
            'retrieval_artifact_manifest_path': self.retrieval_artifact_manifest_path,
            'retrieval_strict_nutrition_enabled': self.retrieval_strict_nutrition_enabled,
        }

    def config_hash(self) -> str:
        snapshot = {
            "top_k": self.top_k,
            "enable_rerank": self.enable_rerank,
            "rerank_model": self.rerank_model,
            "rerank_batch_size": self.rerank_batch_size,
            "embedding_model": self.embedding_model,
            "llm_model": self.llm_model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "chunk_size": self.chunk_size,
            "chunk_overlap": self.chunk_overlap,
            "max_graph_depth": self.max_graph_depth,
            "retrieval_parent_store_enabled": self.retrieval_parent_store_enabled,
            "parent_store_path": self.parent_store_path,
            "parent_store_active_pointer": self.parent_store_active_pointer,
            "retrieval_entity_direct_enabled": self.retrieval_entity_direct_enabled,
            "retrieval_query_plan_enabled": self.retrieval_query_plan_enabled,
            "retrieval_targeted_graph_enabled": self.retrieval_targeted_graph_enabled,
            "retrieval_milvus_v2_enabled": self.retrieval_milvus_v2_enabled,
            "retrieval_new_path_allowlist": self.retrieval_new_path_allowlist,
            "retrieval_new_path_traffic_percent": self.retrieval_new_path_traffic_percent,
            "retrieval_legacy_fallback_enabled": self.retrieval_legacy_fallback_enabled,
            "retrieval_intent_planner_enabled": self.retrieval_intent_planner_enabled,
            "retrieval_intent_planner_version": self.retrieval_intent_planner_version,
            "retrieval_intent_planner_timeout_seconds": self.retrieval_intent_planner_timeout_seconds,
            "retrieval_milvus_database": self.retrieval_milvus_database,
            "retrieval_milvus_collection": self.retrieval_milvus_collection,
            "retrieval_artifact_manifest_path": self.retrieval_artifact_manifest_path,
            "retrieval_strict_nutrition_enabled": self.retrieval_strict_nutrition_enabled,
        }
        payload = json.dumps(snapshot, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

# 默认配置实例
DEFAULT_CONFIG = GraphRAGConfig() 
