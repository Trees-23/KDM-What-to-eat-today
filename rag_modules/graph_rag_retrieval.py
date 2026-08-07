"""
真正的图RAG检索模块
基于图结构的知识推理和检索，而非简单的关键词匹配

优化说明：
1. 修复图结果表达过薄的问题：在生成 Document 时，直接将节点、关系、路径解释和推理链展开到
   page_content 中，而不是只保留一句概述，便于后续生成模块直接拼接上下文。

2. 补强 graph_structure_reasoning：由原来的占位实现改为启发式推理，基于关系类型和节点标签识别
   “食材组成 / 步骤流程 / 分类归属 / 难度映射 / 相似特征”等模式，并生成可解释的推理链。

3. 修复关系序列化：在子图和路径解析时保留关系类型、起点、终点和属性，避免后续只能看到数量、
   却看不到关系语义的问题。

4. 保持生成层简洁：generation_integration.py 仍然只消费 Document.page_content，因此图检索模块
   负责把 metadata 翻译成高信息密度文本，降低后续 prompt 组装复杂度。
"""

import json
import logging
import re
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

try:
    from langchain_core.documents import Document
except ImportError:
    class Document:
        def __init__(self, page_content: str = "", metadata: Optional[Dict[str, Any]] = None):
            self.page_content = page_content
            self.metadata = metadata or {}

try:
    from neo4j import GraphDatabase
except ImportError:
    GraphDatabase = None

logger = logging.getLogger(__name__)

MAX_REASONING_CHAINS = 6

class QueryType(Enum):
    """查询类型枚举"""
    ENTITY_RELATION = "entity_relation"  # 实体关系查询：A和B有什么关系？
    MULTI_HOP = "multi_hop"  # 多跳查询：A通过什么连接到C？
    SUBGRAPH = "subgraph"  # 子图查询：A相关的所有信息
    PATH_FINDING = "path_finding"  # 路径查找：从A到B的最佳路径
    CLUSTERING = "clustering"  # 聚类查询：和A相似的都有什么？

@dataclass
class GraphQuery:
    """图查询结构"""
    query_type: QueryType
    source_entities: List[str]
    target_entities: List[str] = None
    relation_types: List[str] = None
    target_labels: List[str] = None
    normalized_relation_types: List[str] = None
    max_depth: int = 2
    max_nodes: int = 50
    constraints: Dict[str, Any] = None

@dataclass
class GraphPath:
    """图路径结构"""
    nodes: List[Dict[str, Any]]
    relationships: List[Dict[str, Any]]
    path_length: int
    relevance_score: float
    path_type: str

@dataclass
class KnowledgeSubgraph:
    """知识子图结构"""
    central_nodes: List[Dict[str, Any]]
    connected_nodes: List[Dict[str, Any]]
    relationships: List[Dict[str, Any]]
    graph_metrics: Dict[str, float]
    reasoning_chains: List[str]

class GraphRAGRetrieval:
    """
    真正的图RAG检索系统
    核心特点：
    1. 查询意图理解：识别图查询模式
    2. 多跳图遍历：深度关系探索
    3. 子图提取：相关知识网络
    4. 图结构推理：基于拓扑的推理
    5. 动态查询规划：自适应遍历策略
    """
    
    def __init__(self, config, llm_client):
        self.config = config
        self.llm_client = llm_client
        self.driver = None
        
        # 图结构缓存
        self.entity_cache = {}
        self.relation_cache = {}
        self.subgraph_cache = {}
        
    def initialize(self):
        """初始化图RAG检索系统"""
        logger.info("初始化图RAG检索系统...")
        
        # 连接Neo4j
        try:
            if GraphDatabase is None:
                raise ImportError("neo4j is required to initialize GraphRAGRetrieval")
            self.driver = GraphDatabase.driver(
                self.config.neo4j_uri, 
                auth=(self.config.neo4j_user, self.config.neo4j_password)
            )
            # 测试连接
            with self.driver.session() as session:
                session.run("RETURN 1")
            logger.info("Neo4j连接成功")
        except Exception as e:
            logger.error(f"Neo4j连接失败: {e}")
            return
        
        # 预热：构建实体和关系索引
        self._build_graph_index()
        
    def _build_graph_index(self):
        """构建图索引以加速查询"""
        logger.info("构建图结构索引...")
        
        try:
            with self.driver.session() as session:
                # 构建实体索引 - 修复Neo4j语法兼容性问题
                entity_query = """
                MATCH (n)
                WHERE n.nodeId IS NOT NULL
                WITH n, COUNT { (n)--() } as degree
                RETURN labels(n) as node_labels, n.nodeId as node_id, 
                       n.name as name, n.category as category, degree
                ORDER BY degree DESC
                LIMIT 1000
                """
                
                result = session.run(entity_query)
                for record in result:
                    node_id = record["node_id"]
                    self.entity_cache[node_id] = {
                        "labels": record["node_labels"],
                        "name": record["name"],
                        "category": record["category"],
                        "degree": record["degree"]
                    }
                
                # 构建关系类型索引
                relation_query = """
                MATCH ()-[r]->()
                RETURN type(r) as rel_type, count(r) as frequency
                ORDER BY frequency DESC
                """
                
                result = session.run(relation_query)
                for record in result:
                    rel_type = record["rel_type"]
                    self.relation_cache[rel_type] = record["frequency"]
                    
                logger.info(f"索引构建完成: {len(self.entity_cache)}个实体, {len(self.relation_cache)}个关系类型")
                
        except Exception as e:
            logger.error(f"构建图索引失败: {e}")
    
    def understand_graph_query(self, query: str) -> GraphQuery:
        """
        理解查询的图结构意图
        这是图RAG的核心：从自然语言到图查询的转换
        """
        prompt = f"""
        作为图数据库专家，分析以下查询的图结构意图：
        
        查询：{query}
        
        请识别：
        1. 查询类型：
           - entity_relation: 询问实体间的直接关系（如：鸡肉和胡萝卜能一起做菜吗？）
           - multi_hop: 需要多跳推理（如：鸡肉配什么蔬菜？需要：鸡肉→菜品→食材→蔬菜）
           - subgraph: 需要完整子图（如：川菜有什么特色？需要川菜相关的完整知识网络）
           - path_finding: 路径查找（如：从食材到成品菜的制作路径）
           - clustering: 聚类相似性（如：和宫保鸡丁类似的菜有哪些？）
        
        2. 核心实体：查询中的关键实体名称
        3. 目标实体：期望找到的实体类型
        4. 目标节点标签：必须从真实图谱标签中选择
        5. 关系类型：必须优先从真实图谱关系中选择
        5. 遍历深度：需要的图遍历深度（1-3跳）

        真实图谱节点标签只能使用：
        - Recipe: 菜谱 / 菜品
        - Ingredient: 食材 / 原料 / 调料
        - CookingStep: 烹饪步骤 / 制作流程
        - Category: 分类 / 菜系 / 知识类别
        - DifficultyLevel: 难度
        - TechniqueDoc: 烹饪技巧文档，例如“腌（肉）”
        - TechniqueChunk: 烹饪技巧章节或知识点，例如“腌渍基本概念”“腌渍容器及时间”“适用场景”
        - ConceptType: 概念类型

        真实图谱关系类型只能使用：
        - REQUIRES: 菜谱需要食材
        - CONTAINS_STEP: 菜谱包含步骤
        - NEXT_STEP: 步骤流程的下一步
        - BELONGS_TO_CATEGORY / BELONGS_TO: 分类归属
        - HAS_DIFFICULTY_LEVEL / DIFFICULTY_LEVEL: 难度映射
        - HAS_CONCEPT_TYPE: 概念类型
        - HAS_CHUNK: 技巧文档包含技巧章节
        - SIMILAR / USES_SAME_TOOL / USES_SAME_METHOD: 相似或相同工具/方法

        重要规则：
        - 如果用户问“技巧、知识点、要点、注意事项、适用场景、腌肉、腌制、腌渍”等，应优先使用 TechniqueDoc / TechniqueChunk 和 HAS_CHUNK。
        - target_labels 必须返回真实 Neo4j label，不要返回“技巧类节点”这类自然语言。
        - normalized_relation_types 必须返回真实 Neo4j relationship type。
        
        示例：
        查询："鸡肉配什么蔬菜好？"
        分析：这是multi_hop查询，需要通过"鸡肉→使用鸡肉的菜品→这些菜品使用的蔬菜"的路径推理
        
        返回JSON格式：
        {{
            "query_type": "multi_hop",
            "source_entities": ["鸡肉"],
            "target_entities": ["蔬菜类食材"],
            "target_labels": ["Ingredient"],
            "relation_types": ["REQUIRES", "BELONGS_TO_CATEGORY"],
            "normalized_relation_types": ["REQUIRES", "BELONGS_TO_CATEGORY"],
            "max_depth": 3,
            "reasoning": "需要多跳推理：鸡肉→菜品→食材→蔬菜"
        }}

        技巧类示例：
        查询："请讲讲腌（肉）的关键要点，适合用在哪些烹饪场景？"
        返回：
        {{
            "query_type": "subgraph",
            "source_entities": ["腌（肉）", "腌肉", "腌渍"],
            "target_entities": ["腌肉技巧章节", "关键要点", "适用场景"],
            "target_labels": ["TechniqueDoc", "TechniqueChunk"],
            "relation_types": ["HAS_CHUNK"],
            "normalized_relation_types": ["HAS_CHUNK"],
            "max_depth": 2,
            "reasoning": "需要围绕腌（肉）技巧文档展开章节子图，读取关键知识点和适用场景"
        }}
        """
        
        try:
            response = self.llm_client.chat.completions.create(
                model=self.config.llm_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=1000
            )
            
            result = self._safe_json_loads(response.choices[0].message.content.strip())
            
            return GraphQuery(
                query_type=QueryType(result.get("query_type", "subgraph")),
                source_entities=result.get("source_entities", []),
                target_entities=result.get("target_entities", []),
                relation_types=result.get("relation_types", []),
                target_labels=self._normalize_target_labels(result.get("target_labels", [])),
                normalized_relation_types=self._normalize_relation_types(
                    result.get("normalized_relation_types", []) or result.get("relation_types", [])
                ),
                max_depth=result.get("max_depth", 2),
                max_nodes=50
            )
            
        except Exception as e:
            logger.error(f"查询意图理解失败: {e}")
            # 降级方案：默认子图查询
            return GraphQuery(
                query_type=QueryType.SUBGRAPH,
                source_entities=[query],
                target_labels=[],
                normalized_relation_types=[],
                max_depth=2
            )
    
    def multi_hop_traversal(self, graph_query: GraphQuery) -> List[GraphPath]:
        """
        多跳图遍历：这是图RAG的核心优势
        通过图结构发现隐含的知识关联
        """
        logger.info(f"执行多跳遍历: {graph_query.source_entities} -> {graph_query.target_entities}")
        
        paths = []
        
        if not self.driver:
            logger.error("Neo4j连接未建立")
            return paths
            
        try:
            with self.driver.session() as session:
                # 构建多跳遍历查询
                source_entities = graph_query.source_entities
                target_entities = graph_query.target_entities or []
                max_depth = max(1, min(int(graph_query.max_depth or 2), 4))
                target_labels = self._get_query_target_labels(graph_query)
                relation_types = self._get_query_relation_types(graph_query)
                
                # 根据查询类型选择不同的遍历策略
                if graph_query.query_type == QueryType.MULTI_HOP:
                    target_filter = (
                        "AND ANY(label IN labels(target) WHERE label IN $target_labels)"
                        if target_labels else ""
                    )
                    cypher_query = f"""
                    // 多跳推理查询
                    UNWIND $source_entities as source_name
                    MATCH (source)
                    WHERE source.name CONTAINS source_name OR source.nodeId = source_name
                    
                    // 执行多跳遍历
                    MATCH path = (source)-[*1..{max_depth}]-(target)
                    WHERE NOT source = target
                    {target_filter}
                    
                    // 计算路径相关性
                    WITH path, source, target,
                         length(path) as path_len,
                         relationships(path) as rels,
                         nodes(path) as path_nodes
                    
                    // 路径评分：短路径 + 高度数节点 + 关系类型匹配
                    WITH path, source, target, path_len, rels, path_nodes,
                         (1.0 / path_len) + 
                         (REDUCE(s = 0.0, n IN path_nodes | s + COUNT {{ (n)--() }}) / 10.0 / size(path_nodes)) +
                         (CASE WHEN ANY(r IN rels WHERE type(r) IN $relation_types) THEN 0.3 ELSE 0.0 END) +
                         (CASE WHEN ANY(label IN labels(target) WHERE label IN $target_labels) THEN 0.2 ELSE 0.0 END) as relevance
                    
                    ORDER BY relevance DESC
                    LIMIT 20
                    
                    RETURN path, source, target, path_len, rels, path_nodes, relevance
                    """
                    
                    result = session.run(cypher_query, {
                        "source_entities": source_entities,
                        "target_labels": target_labels,
                        "relation_types": relation_types
                    })
                    
                    for record in result:
                        path_data = self._parse_neo4j_path(record)
                        if path_data:
                            paths.append(path_data)
                
                elif graph_query.query_type == QueryType.ENTITY_RELATION:
                    # 实体间关系查询
                    paths.extend(self._find_entity_relations(graph_query, session))
                
                elif graph_query.query_type == QueryType.PATH_FINDING:
                    # 最短路径查找
                    paths.extend(self._find_shortest_paths(graph_query, session))
                    
        except Exception as e:
            logger.error(f"多跳遍历失败: {e}")
            
        logger.info(f"多跳遍历完成，找到 {len(paths)} 条路径")
        return paths
    
    def extract_knowledge_subgraph(self, graph_query: GraphQuery, query: str = "") -> KnowledgeSubgraph:
        """
        提取知识子图：获取实体相关的完整知识网络
        这体现了图RAG的整体性思维
        """
        logger.info(f"提取知识子图: {graph_query.source_entities}")
        
        if not self.driver:
            logger.error("Neo4j连接未建立")
            return self._fallback_subgraph_extraction(graph_query)
        
        try:
            with self.driver.session() as session:
                max_depth = max(1, min(int(graph_query.max_depth or 2), 3))
                max_nodes = max(5, min(int(graph_query.max_nodes or 50), 80))
                target_labels = self._infer_subgraph_target_labels(graph_query, query)
                relation_types = self._infer_subgraph_relation_types(graph_query, query)

                # 子图抽取不再用 size(neighbors) <= max_nodes 过滤整张子图。
                # 旧写法会在中心节点邻居过多时直接丢掉结果；这里改为 query-aware 打分：
                # 距离越近越重要，命中目标节点类型/关系类型会加分，节点度只作为辅助项。
                cypher_query = f"""
                // 找到源实体
                UNWIND $source_entities as entity_name
                MATCH (source)
                WHERE source.name CONTAINS entity_name 
                   OR source.nodeId = entity_name
                
                // 获取指定深度内最有代表性的邻居
                CALL {{
                    WITH source
                    MATCH path = (source)-[*1..{max_depth}]-(neighbor)
                    WHERE source <> neighbor
                    WITH neighbor,
                         min(length(path)) as min_distance,
                         collect(relationships(path))[0] as rels,
                         COUNT {{ (neighbor)--() }} as degree
                    WITH neighbor, min_distance, rels, degree,
                         (1.0 / min_distance) as distance_score,
                         (CASE WHEN size($target_labels) > 0
                                AND ANY(label IN labels(neighbor) WHERE label IN $target_labels)
                               THEN 0.8 ELSE 0.0 END) as label_score,
                         (CASE WHEN size($relation_types) > 0
                                AND ANY(rel IN rels WHERE type(rel) IN $relation_types)
                               THEN 0.8 ELSE 0.0 END) as relation_score,
                         log(toFloat(degree) + 1.0) * 0.08 as degree_score
                    WITH neighbor, rels, min_distance, degree,
                         distance_score + label_score + relation_score + degree_score as node_score
                    ORDER BY node_score DESC, min_distance ASC, degree DESC
                    LIMIT $max_nodes
                    RETURN collect({{
                        node: neighbor,
                        rels: rels,
                        distance: min_distance,
                        degree: degree,
                        score: node_score
                    }}) as entries
                }}
                
                // 计算图指标
                WITH source,
                     [entry IN entries | entry.node] as neighbors,
                     REDUCE(all_rels = [], entry IN entries | all_rels + entry.rels) as relationships
                WITH source, neighbors, relationships,
                     size(neighbors) as node_count,
                     size(relationships) as rel_count
                
                RETURN 
                    source,
                    neighbors as nodes,
                    relationships as rels,
                    {{
                        node_count: node_count,
                        relationship_count: rel_count,
                        density: CASE WHEN node_count > 1 THEN toFloat(rel_count) / (node_count * (node_count - 1) / 2) ELSE 0.0 END
                    }} as metrics
                """
                
                result = session.run(cypher_query, {
                    "source_entities": graph_query.source_entities,
                    "max_nodes": max_nodes,
                    "target_labels": target_labels,
                    "relation_types": relation_types
                })
                
                records = list(result)
                if records:
                    subgraph = self._build_merged_knowledge_subgraph(records)
                    return self._expand_technique_subgraph(subgraph)
                    
        except Exception as e:
            logger.error(f"子图提取失败: {e}")
            
        # 降级方案：简单邻居查询
        return self._fallback_subgraph_extraction(graph_query)
    
    def graph_structure_reasoning(self, subgraph: KnowledgeSubgraph, query: str) -> List[str]:
        """
        基于图结构的推理：这是图RAG的智能之处
        不仅检索信息，还能进行逻辑推理
        """
        reasoning_chains = []
        
        try:
            # 1. 识别推理模式
            reasoning_patterns = self._identify_reasoning_patterns(subgraph)
            
            # 2. 构建推理链
            for pattern in reasoning_patterns:
                reasoning_chains.extend(self._build_reasoning_chains(pattern, subgraph))
            
            # 3. 验证推理链的可信度
            validated_chains = self._validate_reasoning_chains(reasoning_chains, query)
            subgraph.reasoning_chains = validated_chains
            
            logger.info(f"图结构推理完成，生成 {len(validated_chains)} 条推理链")
            return validated_chains
            
        except Exception as e:
            logger.error(f"图结构推理失败: {e}")
            return []
    
    def adaptive_query_planning(self, query: str) -> List[GraphQuery]:
        """
        自适应查询规划：根据查询复杂度动态调整策略
        """
        # 分析查询复杂度
        complexity_score = self._analyze_query_complexity(query)
        
        query_plans = []
        
        if complexity_score < 0.3:
            # 简单查询：直接邻居查询
            plan = GraphQuery(
                query_type=QueryType.ENTITY_RELATION,
                source_entities=[query],
                max_depth=1,
                max_nodes=20
            )
            query_plans.append(plan)
            
        elif complexity_score < 0.7:
            # 中等复杂度：多跳查询
            plan = GraphQuery(
                query_type=QueryType.MULTI_HOP,
                source_entities=[query],
                max_depth=2,
                max_nodes=50
            )
            query_plans.append(plan)
            
        else:
            # 复杂查询：子图提取 + 推理
            plan1 = GraphQuery(
                query_type=QueryType.SUBGRAPH,
                source_entities=[query],
                max_depth=3,
                max_nodes=100
            )
            plan2 = GraphQuery(
                query_type=QueryType.MULTI_HOP,
                source_entities=[query],
                max_depth=3,
                max_nodes=50
            )
            query_plans.extend([plan1, plan2])
            
        return query_plans
    
    def graph_rag_search(self, query: str, top_k: int = 5, audit_run=None) -> List[Document]:
        """
        图RAG主搜索接口：整合所有图RAG能力
        """
        logger.info(f"开始图RAG检索: {query}")
        graph_started_at = datetime.now()
        
        if not self.driver:
            logger.warning("Neo4j连接未建立，返回空结果")
            if audit_run:
                audit_run.append_process(
                    "Graph Retrieval Complete",
                    {
                        "graph_total_duration_ms": 0,
                        "status": "no_driver",
                        "final_count": 0,
                    },
                )
            return []
        
        # 1. 查询意图理解
        understand_started_at = datetime.now()
        graph_query = self.understand_graph_query(query)
        logger.info(f"查询类型: {graph_query.query_type.value}")
        if audit_run:
            audit_run.append_process(
                "Graph Query Understanding",
                {
                    "query_type": graph_query.query_type.value,
                    "source_entities": graph_query.source_entities or [],
                    "target_entities": graph_query.target_entities or [],
                    "target_labels": graph_query.target_labels or [],
                    "relation_types": graph_query.relation_types or [],
                    "normalized_relation_types": graph_query.normalized_relation_types or [],
                    "max_depth": graph_query.max_depth,
                    "max_nodes": graph_query.max_nodes,
                    "llm_model": getattr(self.config, "llm_model", ""),
                    "temperature": 0.1,
                    "max_tokens": 1000,
                    "duration_ms": int((datetime.now() - understand_started_at).total_seconds() * 1000),
                },
            )
        
        try:
            # 2. 图检索主模式只保留两类：
            #    - 路径型检索：回答“实体之间怎么关联”，返回多条路径证据。
            #    - 子图型检索：回答“某个主题有哪些相关信息”，返回一个局部知识网络。
            if self._is_path_query(graph_query.query_type):
                audit_run and audit_run.append_process(
                    "Graph Path Retrieval Config",
                    {
                        "max_depth": graph_query.max_depth,
                        "target_labels": self._get_query_target_labels(graph_query),
                        "relation_types": self._get_query_relation_types(graph_query),
                        "cypher_template_hash": "graph_path_v1",
                        "limit": 20,
                    },
                )
                paths = self.multi_hop_traversal(graph_query)
                if audit_run:
                    audit_run.append_recall(
                        "Graph Retrieval / Path Raw Results",
                        self._format_paths_for_recall(paths),
                    )
                results = self._paths_to_documents(paths, query)

                # Neo4j 查询内部已经 ORDER BY relevance DESC LIMIT 20，
                # 这里保留排序作为 Python 侧最终保险和后续 rerank/去重扩展点。
                results = self._rank_by_graph_relevance(results, query)
                if audit_run:
                    audit_run.write_documents(
                        "Graph Retrieval / Path Ranked Results",
                        results,
                        "graph_path_ranked",
                    )
                    final_docs = results[:top_k]
                    audit_run.write_documents(
                        "Graph Retrieval / Path Top-K",
                        final_docs,
                        "graph_path_top_k",
                    )
                    audit_run.append_process(
                        "Graph Retrieval Complete",
                        {
                            "graph_total_duration_ms": int((datetime.now() - graph_started_at).total_seconds() * 1000),
                            "mode": "path",
                            "path_count": len(paths),
                            "final_count": len(final_docs),
                        },
                    )

                logger.info(f"路径型图RAG检索完成，返回 {len(results[:top_k])} 个结果")
                return results[:top_k]

            if self._is_subgraph_query(graph_query.query_type):
                audit_run and audit_run.append_process(
                    "Graph Subgraph Extraction Config",
                    {
                        "source_entities": graph_query.source_entities or [],
                        "max_depth": graph_query.max_depth,
                        "max_nodes": graph_query.max_nodes,
                        "target_labels": self._infer_subgraph_target_labels(graph_query, query),
                        "relation_types": self._infer_subgraph_relation_types(graph_query, query),
                    },
                )
                subgraph = self.extract_knowledge_subgraph(graph_query, query)
                if audit_run:
                    audit_run.append_process(
                        "Graph Subgraph Status",
                        {
                            "central_count": len(subgraph.central_nodes),
                            "connected_count": len(subgraph.connected_nodes),
                            "relationship_count": len(subgraph.relationships),
                            "density": subgraph.graph_metrics.get("density", 0.0),
                            "dedupe_count": 0,
                        },
                    )
                    audit_run.append_recall(
                        "Graph Retrieval / Subgraph Raw Content",
                        self._format_subgraph_for_recall(subgraph),
                    )
                    patterns = self._identify_reasoning_patterns(subgraph)
                    audit_run.append_process(
                        "Graph Reasoning Patterns",
                        {"reasoning_patterns": patterns},
                    )
                reasoning_started_at = datetime.now()
                before_chains = list(subgraph.reasoning_chains or [])
                self.graph_structure_reasoning(subgraph, query)
                if audit_run:
                    audit_run.append_recall(
                        "Graph Retrieval / Candidate Reasoning Chains",
                        self._format_chains_for_recall(before_chains),
                    )
                    audit_run.append_process(
                        "Graph Reasoning Validation",
                        {
                            "judge_model": getattr(self.config, "llm_model", ""),
                            "candidate_count": len(before_chains),
                            "accepted_count": len(subgraph.reasoning_chains or []),
                            "fallback_used": False,
                            "duration_ms": int((datetime.now() - reasoning_started_at).total_seconds() * 1000),
                        },
                    )
                    audit_run.append_recall(
                        "Graph Retrieval / Accepted Reasoning Chains",
                        self._format_chains_for_recall((subgraph.reasoning_chains or [])[:MAX_REASONING_CHAINS]),
                    )
                results = self._subgraph_to_documents(subgraph, query)
                if audit_run:
                    audit_run.write_documents(
                        "Graph Retrieval / Subgraph Documents",
                        results,
                        "knowledge_subgraph",
                    )
                    final_docs = results[:top_k]
                    audit_run.append_process(
                        "Graph Retrieval Complete",
                        {
                            "graph_total_duration_ms": int((datetime.now() - graph_started_at).total_seconds() * 1000),
                            "mode": "subgraph",
                            "final_count": len(final_docs),
                        },
                    )

                # 子图结果和路径结果不是同一粒度，不在这里做路径 relevance 混排。
                logger.info(f"子图型图RAG检索完成，返回 {len(results[:top_k])} 个结果")
                return results[:top_k]

            logger.warning(f"未识别的图查询类型: {graph_query.query_type}，返回空结果")
            return []
            
        except Exception as e:
            logger.error(f"图RAG检索失败: {e}")
            if audit_run:
                audit_run.record_error("graph_rag_search", e)
                audit_run.append_process(
                    "Graph Retrieval Complete",
                    {
                        "graph_total_duration_ms": int((datetime.now() - graph_started_at).total_seconds() * 1000),
                        "status": "error",
                        "final_count": 0,
                    },
                )
            return []
    
    # ========== 辅助方法 ==========
    
    def _parse_neo4j_path(self, record) -> Optional[GraphPath]:
        """解析Neo4j路径记录"""
        try:
            path_nodes = []
            for node in record["path_nodes"]:
                path_nodes.append(self._serialize_node(node))
            
            relationships = []
            for rel in record["rels"]:
                serialized = self._serialize_relationship(rel)
                if isinstance(serialized, list):
                    relationships.extend(serialized)
                elif serialized:
                    relationships.append(serialized)
            
            return GraphPath(
                nodes=path_nodes,
                relationships=relationships,
                path_length=record["path_len"],
                relevance_score=record["relevance"],
                path_type="multi_hop"
            )
            
        except Exception as e:
            logger.error(f"路径解析失败: {e}")
            return None
    
    def _build_knowledge_subgraph(self, record) -> KnowledgeSubgraph:
        """构建知识子图对象"""
        try:
            central_nodes = [self._serialize_node(record["source"])]
            connected_nodes = [self._serialize_node(node) for node in record["nodes"]]
            relationships = []
            for rel in record["rels"]:
                serialized = self._serialize_relationship(rel)
                if isinstance(serialized, list):
                    relationships.extend(serialized)
                elif serialized:
                    relationships.append(serialized)
            
            return KnowledgeSubgraph(
                central_nodes=central_nodes,
                connected_nodes=connected_nodes,
                relationships=relationships,
                graph_metrics=record["metrics"],
                reasoning_chains=[]
            )
        except Exception as e:
            logger.error(f"构建知识子图失败: {e}")
            return KnowledgeSubgraph(
                central_nodes=[],
                connected_nodes=[],
                relationships=[],
                graph_metrics={},
                reasoning_chains=[]
            )

    def _build_merged_knowledge_subgraph(self, records) -> KnowledgeSubgraph:
        """合并多个中心实体的子图结果，并做节点/关系去重。"""
        central_nodes = []
        connected_nodes = []
        relationships = []
        metrics = {
            "node_count": 0,
            "relationship_count": 0,
            "density": 0.0,
        }

        seen_central = set()
        seen_nodes = set()
        seen_rels = set()
        densities = []

        for record in records:
            subgraph = self._build_knowledge_subgraph(record)
            for node in subgraph.central_nodes:
                key = self._node_key(node)
                if key not in seen_central:
                    seen_central.add(key)
                    central_nodes.append(node)

            for node in subgraph.connected_nodes:
                key = self._node_key(node)
                if key not in seen_nodes and key not in seen_central:
                    seen_nodes.add(key)
                    connected_nodes.append(node)

            for rel in subgraph.relationships:
                key = self._relationship_key(rel)
                if key not in seen_rels:
                    seen_rels.add(key)
                    relationships.append(rel)

            if subgraph.graph_metrics.get("density") is not None:
                densities.append(float(subgraph.graph_metrics.get("density", 0.0)))

        metrics["node_count"] = len(connected_nodes)
        metrics["relationship_count"] = len(relationships)
        metrics["density"] = sum(densities) / len(densities) if densities else 0.0

        return KnowledgeSubgraph(
            central_nodes=central_nodes,
            connected_nodes=connected_nodes,
            relationships=relationships,
            graph_metrics=metrics,
            reasoning_chains=[]
        )

    @staticmethod
    def _is_technique_node(node: Dict[str, Any]) -> bool:
        """判断节点是否为技巧文档或技巧章节。"""
        labels = set(node.get("labels") or [])
        return bool({"TechniqueDoc", "TechniqueChunk"} & labels)

    def _collect_technique_node_ids(self, subgraph: KnowledgeSubgraph) -> List[str]:
        """从子图中心节点和关联节点中提取技巧节点ID，保持顺序去重。"""
        node_ids = []
        seen = set()
        for node in (subgraph.central_nodes or []) + (subgraph.connected_nodes or []):
            if not self._is_technique_node(node):
                continue
            node_id = node.get("id") or node.get("properties", {}).get("nodeId")
            if node_id and node_id not in seen:
                seen.add(node_id)
                node_ids.append(node_id)
        return node_ids

    def _fetch_technique_sibling_chunks(self, node_ids: List[str], limit: int = 8) -> Dict[str, Any]:
        """命中技巧文档或章节后，取同一技巧文档下的兄弟章节。"""
        if not node_ids or not self.driver:
            return {"docs": [], "chunks": [], "relationships": []}

        try:
            with self.driver.session() as session:
                query = """
                UNWIND $node_ids AS node_id
                MATCH (n {nodeId: node_id})
                OPTIONAL MATCH (doc_from_chunk:TechniqueDoc)-[:HAS_CHUNK]->(n)
                WITH collect(DISTINCT CASE WHEN n:TechniqueDoc THEN n ELSE doc_from_chunk END) AS docs
                UNWIND docs AS doc
                WITH DISTINCT doc
                WHERE doc IS NOT NULL
                MATCH (doc)-[r:HAS_CHUNK]->(chunk:TechniqueChunk)
                WITH doc, r, chunk
                ORDER BY doc.nodeId, COALESCE(r.chunkOrder, chunk.chunkIndex, 999)
                RETURN doc, r, chunk
                LIMIT $limit
                """
                result = session.run(query, {"node_ids": node_ids, "limit": limit})
                docs = []
                chunks = []
                relationships = []
                for record in result:
                    docs.append(self._serialize_node(record["doc"]))
                    chunks.append(self._serialize_node(record["chunk"]))
                    relationships.append(self._serialize_relationship(record["r"]))
                return {
                    "docs": docs,
                    "chunks": chunks,
                    "relationships": relationships,
                }
        except Exception as e:
            logger.error(f"查询技巧兄弟章节失败: {e}")
            return {"docs": [], "chunks": [], "relationships": []}

    def _expand_technique_subgraph(self, subgraph: KnowledgeSubgraph, limit: int = 8) -> KnowledgeSubgraph:
        """如果子图命中技巧节点，则补齐同文档下的兄弟章节和 HAS_CHUNK 关系。"""
        node_ids = self._collect_technique_node_ids(subgraph)
        if not node_ids:
            return subgraph

        expansion = self._fetch_technique_sibling_chunks(node_ids, limit=limit)

        seen_central = {self._node_key(node) for node in subgraph.central_nodes}
        seen_nodes = {self._node_key(node) for node in subgraph.connected_nodes}
        seen_rels = {self._relationship_key(rel) for rel in subgraph.relationships}

        for doc in expansion.get("docs", []):
            key = self._node_key(doc)
            if key not in seen_central and key not in seen_nodes:
                subgraph.connected_nodes.append(doc)
                seen_nodes.add(key)

        for chunk in expansion.get("chunks", []):
            key = self._node_key(chunk)
            if key not in seen_central and key not in seen_nodes:
                subgraph.connected_nodes.append(chunk)
                seen_nodes.add(key)

        for rel in expansion.get("relationships", []):
            key = self._relationship_key(rel)
            if key not in seen_rels:
                subgraph.relationships.append(rel)
                seen_rels.add(key)

        subgraph.graph_metrics["node_count"] = len(subgraph.connected_nodes)
        subgraph.graph_metrics["relationship_count"] = len(subgraph.relationships)
        return subgraph
    
    def _paths_to_documents(self, paths: List[GraphPath], query: str) -> List[Document]:
        """将图路径转换为Document对象"""
        documents = []
        
        for i, path in enumerate(paths):
            # 构建路径描述
            path_desc = self._build_path_description(path)
            anchor_name = path.nodes[0].get("name", "图结构结果") if path.nodes else "图结构结果"
            
            doc = Document(
                page_content=path_desc,
                metadata={
                    "search_type": "graph_path",
                    "path_length": path.path_length,
                    "relevance_score": path.relevance_score,
                    "path_type": path.path_type,
                    "node_count": len(path.nodes),
                    "relationship_count": len(path.relationships),
                    "recipe_name": anchor_name
                }
            )
            documents.append(doc)
            
        return documents

    def _format_paths_for_recall(self, paths: List[GraphPath]) -> str:
        parts = []
        for index, path in enumerate(paths):
            parts.extend(
                [
                    f"### path_order={index}",
                    f"source: graph_path",
                    f"path_length: {path.path_length}",
                    f"relevance_score: {path.relevance_score}",
                    "",
                    "```text",
                    self._build_path_description(path),
                    "```",
                    "",
                ]
            )
        return "\n".join(parts) if parts else "_no content_"

    def _format_subgraph_for_recall(self, subgraph: KnowledgeSubgraph) -> str:
        return "\n".join(
            [
                "### subgraph_order=0",
                "source: knowledge_subgraph",
                "",
                "```text",
                self._build_subgraph_description(subgraph),
                "```",
            ]
        )

    @staticmethod
    def _format_chains_for_recall(chains: List[str]) -> str:
        parts = []
        for index, chain in enumerate(chains):
            parts.extend(
                [
                    f"### chain_order={index}",
                    "source: graph_structure_reasoning",
                    "",
                    "```text",
                    chain,
                    "```",
                    "",
                ]
            )
        return "\n".join(parts) if parts else "_no content_"
    
    def _subgraph_to_documents(self, subgraph: KnowledgeSubgraph, query: str) -> List[Document]:
        """将知识子图转换为Document对象"""
        documents = []

        # 子图整体描述
        subgraph_desc = self._build_subgraph_description(subgraph)
        anchor_name = subgraph.central_nodes[0].get("name", "知识子图") if subgraph.central_nodes else "知识子图"
        reasoning_chains = subgraph.reasoning_chains or []
        relevance_score = self._score_subgraph_relevance(subgraph, reasoning_chains, query)
        
        doc = Document(
            page_content=subgraph_desc,
            metadata={
                "search_type": "knowledge_subgraph",
                "node_count": len(subgraph.connected_nodes),
                "relationship_count": len(subgraph.relationships),
                "graph_density": subgraph.graph_metrics.get("density", 0.0),
                "relevance_score": relevance_score,
                "reasoning_chains": reasoning_chains,
                "recipe_name": anchor_name
            }
        )
        documents.append(doc)
        
        return documents
    
    def _build_path_description(self, path: GraphPath) -> str:
        """构建路径的自然语言描述"""
        if not path.nodes:
            return "空路径"

        chain_text = " -> ".join(self._format_node_brief(node) for node in path.nodes)
        relation_lines = []
        for rel in path.relationships:
            relation_lines.append(f"- {self._format_relationship_text(rel)}")

        conclusion = self._infer_path_conclusion(path)
        parts = [
            f"图路径概览：{chain_text}",
            f"路径长度：{path.path_length} 跳",
            f"相关性得分：{path.relevance_score:.3f}",
        ]
        if relation_lines:
            parts.append("关系明细：")
            parts.extend(relation_lines[:6])
        if conclusion:
            parts.append(f"推理结论：{conclusion}")

        return "\n".join(parts)
    
    def _build_subgraph_description(self, subgraph: KnowledgeSubgraph) -> str:
        """构建子图的自然语言描述"""
        central_names = [node.get("name", "未知") for node in subgraph.central_nodes]
        node_count = len(subgraph.connected_nodes)
        rel_count = len(subgraph.relationships)

        parts = [
            f"知识子图主题：{', '.join(central_names) if central_names else '未知主题'}",
            f"子图规模：{node_count} 个相关节点，{rel_count} 条关系，图密度 {subgraph.graph_metrics.get('density', 0.0):.3f}",
        ]

        grouped_nodes = self._group_nodes_by_label(subgraph.connected_nodes)
        if grouped_nodes:
            parts.append("关键节点：")
            for label, names in grouped_nodes.items():
                parts.append(f"- {label}：{', '.join(names[:5])}")

        technique_sections = self._build_technique_content_sections(subgraph.connected_nodes)
        if technique_sections:
            parts.append("关键技巧内容：")
            parts.extend(technique_sections)

        relation_lines = self._summarize_relationships(subgraph.relationships)
        if relation_lines:
            parts.append("关键关系：")
            parts.extend(f"- {line}" for line in relation_lines[:8])

        if subgraph.reasoning_chains:
            parts.append("图推理链：")
            parts.extend(f"- {chain}" for chain in subgraph.reasoning_chains[:MAX_REASONING_CHAINS])

        return "\n".join(parts)

    def _build_technique_content_sections(self, nodes: List[Dict[str, Any]], limit: int = 8) -> List[str]:
        """提取技巧节点正文，优先按 chunkIndex 顺序输出 TechniqueChunk 内容。"""
        technique_nodes = [
            node for node in nodes
            if self._is_technique_node(node)
        ]
        if not technique_nodes:
            return []

        def sort_key(node: Dict[str, Any]) -> tuple:
            props = node.get("properties", {})
            labels = node.get("labels") or []
            is_doc = 0 if "TechniqueDoc" in labels else 1
            chunk_index = props.get("chunkIndex")
            try:
                chunk_index = int(chunk_index)
            except Exception:
                chunk_index = 999
            return (is_doc, chunk_index, node.get("name") or "")

        sections = []
        seen = set()
        for node in sorted(technique_nodes, key=sort_key):
            detail = self._format_node_detail(node)
            if not detail or detail in seen:
                continue
            seen.add(detail)
            sections.append(detail)
            if len(sections) >= limit:
                break
        return sections

    def _format_node_detail(self, node: Dict[str, Any], max_chars: int = 900) -> str:
        """把节点属性转为可给LLM直接使用的正文片段。"""
        props = node.get("properties", {}) or {}
        labels = set(node.get("labels") or [])
        name = node.get("name") or props.get("name") or "未知节点"

        if "TechniqueChunk" in labels:
            title = props.get("sectionTitle") or props.get("title") or name
            body = props.get("content") or props.get("summary") or ""
            if not body:
                return ""
            return f"## {title}\n{str(body).strip()[:max_chars]}"

        if "TechniqueDoc" in labels:
            title = props.get("title") or name
            body = props.get("summary") or props.get("content") or ""
            if not body:
                return ""
            return f"## {title}\n{str(body).strip()[:max_chars]}"

        if "CookingStep" in labels:
            body_parts = []
            for key, label in [("description", "步骤描述"), ("technique", "技巧"), ("time", "时间")]:
                value = props.get(key)
                if value:
                    body_parts.append(f"{label}: {value}")
            return f"## {name}\n" + "\n".join(body_parts) if body_parts else ""

        if "Recipe" in labels:
            body_parts = []
            for key, label in [("description", "描述"), ("category", "分类"), ("cuisineType", "菜系")]:
                value = props.get(key)
                if value:
                    body_parts.append(f"{label}: {value}")
            return f"## {name}\n" + "\n".join(body_parts) if body_parts else ""

        return ""
    
    def _rank_by_graph_relevance(self, documents: List[Document], query: str) -> List[Document]:
        """对路径型检索结果按图结构相关性排序。

        当前多跳/实体关系/最短路径 Cypher 已经做了 ORDER BY relevance DESC LIMIT，
        因此这个函数主要作为 Python 侧最终保险，以及后续增加路径去重、多样性控制、
        LLM rerank 时的统一入口。它不再用于子图结果和路径结果的跨类型比较。
        """
        return sorted(documents, 
                     key=lambda x: x.metadata.get("relevance_score", 0.0), 
                     reverse=True)

    @staticmethod
    def _is_path_query(query_type: QueryType) -> bool:
        """路径型检索：实体关系、多跳、最短路径都统一返回路径证据。"""
        return query_type in {
            QueryType.ENTITY_RELATION,
            QueryType.MULTI_HOP,
            QueryType.PATH_FINDING,
        }

    @staticmethod
    def _is_subgraph_query(query_type: QueryType) -> bool:
        """子图型检索：围绕主题展开局部知识网络。"""
        return query_type in {
            QueryType.SUBGRAPH,
            QueryType.CLUSTERING,
        }

    def _score_subgraph_relevance(self, subgraph: KnowledgeSubgraph, reasoning_chains: List[str], query: str) -> float:
        """为子图结果生成可与路径结果比较的相关性分数。"""
        central_text = " ".join(node.get("name", "") for node in subgraph.central_nodes)
        relation_types = {rel.get("type", "") for rel in subgraph.relationships}
        query_terms = self._extract_query_terms(query)
        score = 0.2
        if any(term in central_text for term in query_terms):
            score += 0.25
        score += min(len(reasoning_chains) * 0.15, 0.35)
        score += min(len(relation_types) * 0.04, 0.2)
        score += min(float(subgraph.graph_metrics.get("density", 0.0) or 0.0), 0.2)
        return min(score, 1.0)
    
    def _analyze_query_complexity(self, query: str) -> float:
        """分析查询复杂度"""
        complexity_indicators = ["什么", "如何", "为什么", "哪些", "关系", "影响", "原因"]
        score = sum(1 for indicator in complexity_indicators if indicator in query)
        return min(score / len(complexity_indicators), 1.0)
    
    def _identify_reasoning_patterns(self, subgraph: KnowledgeSubgraph) -> List[str]:
        """识别推理模式"""
        patterns = []
        relation_types = {rel.get("type", "") for rel in subgraph.relationships}

        if "REQUIRES" in relation_types:
            patterns.append("食材组成")
        if "CONTAINS_STEP" in relation_types or "NEXT_STEP" in relation_types:
            patterns.append("步骤流程")
        if "BELONGS_TO_CATEGORY" in relation_types or "BELONGS_TO" in relation_types:
            patterns.append("分类归属")
        if "DIFFICULTY_LEVEL" in relation_types or "HAS_DIFFICULTY_LEVEL" in relation_types:
            patterns.append("难度映射")
        if {"SIMILAR", "USES_SAME_TOOL", "USES_SAME_METHOD"} & relation_types:
            patterns.append("相似特征")

        if not patterns and subgraph.connected_nodes:
            patterns.append("关联扩散")

        return patterns
    
    def _build_reasoning_chains(self, pattern: str, subgraph: KnowledgeSubgraph) -> List[str]:
        """基于中心节点的直接关系证据构建推理链。"""
        chains = []
        central_nodes = subgraph.central_nodes or []

        for central_node in central_nodes:
            central_name = self._node_name(central_node) or "该主题"

            if pattern == "食材组成":
                ingredient_names = self._direct_neighbor_names(
                    subgraph,
                    central_node,
                    {"REQUIRES"},
                    label="Ingredient",
                    limit=5,
                )
                if ingredient_names:
                    chains.append(
                        f"{central_name} 通过 REQUIRES 关系直接关联的关键食材包括 {', '.join(ingredient_names)}，说明该主题的组成关系主要围绕这些原料展开。"
                    )
                continue

            if pattern == "步骤流程":
                step_names = self._direct_neighbor_names(
                    subgraph,
                    central_node,
                    {"CONTAINS_STEP", "NEXT_STEP"},
                    label="CookingStep",
                    limit=5,
                )
                if step_names:
                    chains.append(
                        f"{central_name} 通过步骤关系直接关联的关键步骤包括 {', '.join(step_names)}，子图中存在明确的流程型证据，可用于回答制作过程类问题。"
                    )
                continue

            if pattern == "分类归属":
                categories = self._direct_neighbor_names(
                    subgraph,
                    central_node,
                    {"BELONGS_TO_CATEGORY", "BELONGS_TO"},
                    limit=4,
                )
                if categories:
                    chains.append(
                        f"{central_name} 在图中与 {', '.join(categories)} 存在直接归属关系，可据此推断其类别、菜系或知识层级。"
                    )
                continue

            if pattern == "难度映射":
                difficulty_nodes = self._direct_neighbor_names(
                    subgraph,
                    central_node,
                    {"DIFFICULTY_LEVEL", "HAS_DIFFICULTY_LEVEL"},
                    label="DifficultyLevel",
                    limit=3,
                )
                if difficulty_nodes:
                    chains.append(
                        f"{central_name} 与难度节点 {', '.join(difficulty_nodes)} 直接相连，可用于回答复杂度、上手门槛等问题。"
                    )
                continue

            if pattern == "相似特征":
                similar_targets = self._direct_neighbor_names(
                    subgraph,
                    central_node,
                    {"SIMILAR", "USES_SAME_TOOL", "USES_SAME_METHOD"},
                    limit=4,
                )
                if similar_targets:
                    chains.append(
                        f"{central_name} 与 {', '.join(similar_targets)} 存在直接相似特征关系，可据此扩展推荐相近菜谱、工具或方法。"
                    )
                continue

            if pattern == "关联扩散":
                labels = self._direct_neighbor_labels(subgraph, central_node)
                if labels:
                    chains.append(
                        f"{central_name} 的直接邻域覆盖 {'、'.join(labels)} 等多类节点，说明该主题具有跨类型关联能力。"
                    )

        return chains

    def _build_reasoning_chain(self, pattern: str, subgraph: KnowledgeSubgraph) -> Optional[str]:
        """兼容旧调用：返回第一条中心节点关系推理链。"""
        chains = self._build_reasoning_chains(pattern, subgraph)
        return chains[0] if chains else None

    def _direct_neighbor_names(
        self,
        subgraph: KnowledgeSubgraph,
        central_node: Dict[str, Any],
        rel_types: set,
        *,
        label: Optional[str] = None,
        limit: int = 5,
    ) -> List[str]:
        """按关系证据抽取与中心节点直接相连的邻居名称。"""
        central_key = self._node_key(central_node)
        names = []
        for rel in subgraph.relationships:
            if rel.get("type") not in rel_types:
                continue
            other = self._other_relationship_node(rel, central_key)
            if not other:
                continue
            if label and label not in (other.get("labels") or []):
                continue
            name = self._node_name(other)
            if name and name not in names:
                names.append(name)
            if len(names) >= limit:
                break
        return names

    def _direct_neighbor_labels(self, subgraph: KnowledgeSubgraph, central_node: Dict[str, Any]) -> List[str]:
        """抽取与中心节点直接相连的邻居标签。"""
        central_key = self._node_key(central_node)
        labels = []
        for rel in subgraph.relationships:
            other = self._other_relationship_node(rel, central_key)
            if not other:
                continue
            for label in other.get("labels") or ["Node"]:
                if label not in labels:
                    labels.append(label)
        return labels

    def _other_relationship_node(self, rel: Dict[str, Any], central_key: str) -> Optional[Dict[str, Any]]:
        """如果关系一端是中心节点，返回另一端节点。"""
        start = rel.get("start") or {}
        end = rel.get("end") or {}
        if self._node_key(start) == central_key:
            return end
        if self._node_key(end) == central_key:
            return start
        return None

    @staticmethod
    def _node_name(node: Dict[str, Any]) -> str:
        """获取节点名称。"""
        return node.get("name") or node.get("properties", {}).get("name") or ""

    
    def _validate_reasoning_chains(self, chains: List[str], query: str) -> List[str]:
        """
        使用 LLM 判断推理链是否真正回答了用户问题。

        旧实现按 query 关键词是否出现在 chain 中打分，容易把“字面相似但语义无关”的链保留下来。
        这里改为 LLM Judge：输入用户问题和候选链，要求模型只保留有图证据支撑、能帮助回答问题的链。
        如果 LLM 不可用或 JSON 解析失败，再退回到轻量启发式排序，保证系统可用。
        """
        if not chains:
            return []

        unique_chains = []
        seen = set()
        for chain in chains:
            clean_chain = chain.strip()
            if not clean_chain or clean_chain in seen:
                continue
            seen.add(clean_chain)
            unique_chains.append(clean_chain)

        if not unique_chains:
            return []

        judged = self._llm_validate_reasoning_chains(unique_chains, query)
        if judged:
            return judged[:MAX_REASONING_CHAINS]

        return self._fallback_validate_reasoning_chains(unique_chains, query)

    def _llm_validate_reasoning_chains(self, chains: List[str], query: str) -> List[str]:
        """调用 LLM 对候选推理链做语义相关性和证据充分性判断。"""
        if not self.llm_client:
            return []

        chain_payload = [
            {"id": idx + 1, "chain": chain}
            for idx, chain in enumerate(chains[:8])
        ]
        prompt = f"""
你是图RAG检索结果的质量评估器。请判断候选图推理链是否对用户问题有帮助。

用户问题：
{query}

候选推理链：
{json.dumps(chain_payload, ensure_ascii=False, indent=2)}

判断标准：
1. 只保留能直接帮助回答用户问题的推理链。
2. 推理链必须有明确实体、关系或图结构证据，不能只是泛泛描述。
3. 如果链只是在说“有关联”“覆盖多类节点”，但不能支持答案，应降低分数或剔除。
4. 不要因为出现相同关键词就判相关，要判断语义是否真的匹配问题意图。
5. 最多保留6条。

请只返回JSON，不要返回解释性正文：
{{
  "accepted": [
    {{"id": 1, "score": 0.92, "reason": "与问题直接相关"}}
  ]
}}
"""

        try:
            response = self.llm_client.chat.completions.create(
                model=self.config.llm_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=800
            )
            content = response.choices[0].message.content.strip()
            result = self._safe_json_loads(content)
            accepted = result.get("accepted", []) if isinstance(result, dict) else []
            scored = []
            for item in accepted:
                try:
                    chain_id = int(item.get("id"))
                    score = float(item.get("score", 0.0))
                except Exception:
                    continue
                if 1 <= chain_id <= len(chain_payload) and score >= 0.55:
                    scored.append((score, chain_payload[chain_id - 1]["chain"]))
            scored.sort(key=lambda item: item[0], reverse=True)
            return [chain for _, chain in scored]
        except Exception as e:
            logger.warning(f"LLM推理链验证失败，使用降级验证: {e}")
            return []

    def _fallback_validate_reasoning_chains(self, chains: List[str], query: str) -> List[str]:
        """LLM 不可用时的保底排序，仍然避免纯关键词命中占主导。"""
        query_terms = [term for term in [query] + self._extract_query_terms(query) if term]
        structural_terms = ["需要", "包含步骤", "属于", "难度", "相似", "共现", "流程", "分类", "食材"]
        scored = []
        for chain in chains:
            score = 0.0
            score += 0.4 if any(term in chain for term in structural_terms) else 0.0
            score += min(sum(1 for term in query_terms if term and term in chain) * 0.15, 0.45)
            score += min(len(chain) / 120.0, 0.15)
            scored.append((score, chain))
        scored.sort(key=lambda item: item[0], reverse=True)
        return [chain for _, chain in scored[:MAX_REASONING_CHAINS]]

    def _safe_json_loads(self, text: str) -> Any:
        """尽量从 LLM 输出中提取 JSON，兼容模型包裹代码块或额外说明。"""
        try:
            return json.loads(text)
        except Exception:
            pass

        fenced = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
        if fenced:
            try:
                return json.loads(fenced.group(1).strip())
            except Exception:
                pass

        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(text[start:end + 1])
        raise ValueError("未找到可解析的JSON")

    def _normalize_target_labels(self, target_entities: List[str]) -> List[str]:
        """把 LLM 输出的自然语言目标实体映射成真实 Neo4j label。"""
        if not target_entities:
            return []
        label_patterns = [
            ("techniquechunk", "TechniqueChunk"),
            ("techniquedoc", "TechniqueDoc"),
            ("烹饪技巧", "TechniqueDoc"),
            ("技巧章节", "TechniqueChunk"),
            ("知识章节", "TechniqueChunk"),
            ("注意事项", "TechniqueChunk"),
            ("适用场景", "TechniqueChunk"),
            ("知识点", "TechniqueChunk"),
            ("腌（肉）", "TechniqueDoc"),
            ("腌肉", "TechniqueDoc"),
            ("腌制", "TechniqueDoc"),
            ("腌渍", "TechniqueDoc"),
            ("技巧", "TechniqueDoc"),
            ("知识", "TechniqueDoc"),
            ("要点", "TechniqueChunk"),
            ("场景", "TechniqueChunk"),
            ("蔬菜", "Ingredient"),
            ("肉类", "Ingredient"),
            ("调料", "Ingredient"),
            ("食材", "Ingredient"),
            ("原料", "Ingredient"),
            ("配料", "Ingredient"),
            ("ingredient", "Ingredient"),
            ("烹饪步骤", "CookingStep"),
            ("制作步骤", "CookingStep"),
            ("做法", "CookingStep"),
            ("流程", "CookingStep"),
            ("步骤", "CookingStep"),
            ("cookingstep", "CookingStep"),
            ("菜系", "Category"),
            ("分类", "Category"),
            ("类别", "Category"),
            ("难度", "DifficultyLevel"),
            ("菜品", "Recipe"),
            ("菜谱", "Recipe"),
            ("食谱", "Recipe"),
            ("recipe", "Recipe"),
            ("菜", "Recipe"),
        ]
        # 长词优先，避免“蔬菜类食材”先命中单字“菜”而误判成 Recipe。
        label_patterns = sorted(label_patterns, key=lambda item: len(item[0]), reverse=True)
        labels = []
        valid_labels = {
            "Recipe",
            "Ingredient",
            "CookingStep",
            "Category",
            "ConceptType",
            "DifficultyLevel",
            "TechniqueDoc",
            "TechniqueChunk",
        }
        for item in target_entities:
            text = str(item).strip()
            if not text:
                continue
            if text in valid_labels:
                label = text
            else:
                label = next((mapped for key, mapped in label_patterns if key.lower() in text.lower()), "")
            if label and label not in labels:
                labels.append(label)
        return labels

    def _normalize_relation_types(self, relation_types: List[str]) -> List[str]:
        """将自然语言关系类型映射成图谱中的关系名。"""
        relation_map = {
            "包含章节": "HAS_CHUNK",
            "文档分块": "HAS_CHUNK",
            "知识点": "HAS_CHUNK",
            "章节": "HAS_CHUNK",
            "内容": "HAS_CHUNK",
            "技巧": "HAS_CHUNK",
            "要点": "HAS_CHUNK",
            "需要": "REQUIRES",
            "食材": "REQUIRES",
            "包含": "CONTAINS_STEP",
            "步骤": "CONTAINS_STEP",
            "下一步": "NEXT_STEP",
            "属于": "BELONGS_TO_CATEGORY",
            "分类": "BELONGS_TO_CATEGORY",
            "菜系": "BELONGS_TO_CATEGORY",
            "难度": "HAS_DIFFICULTY_LEVEL",
            "相似": "SIMILAR",
            "同工具": "USES_SAME_TOOL",
            "同方法": "USES_SAME_METHOD",
        }
        valid_types = {
            "REQUIRES", "CONTAINS_STEP", "NEXT_STEP", "BELONGS_TO", "BELONGS_TO_CATEGORY",
            "DIFFICULTY_LEVEL", "HAS_DIFFICULTY_LEVEL", "HAS_CONCEPT_TYPE", "SIMILAR",
            "USES_SAME_TOOL", "USES_SAME_METHOD", "HAS_CHUNK"
        }
        normalized = []
        for item in relation_types:
            text = str(item).strip()
            if not text:
                continue
            rel_type = text if text in valid_types else next(
                (mapped for key, mapped in relation_map.items() if key in text),
                ""
            )
            if rel_type and rel_type not in normalized:
                normalized.append(rel_type)
        return normalized

    def _get_query_target_labels(self, graph_query: GraphQuery) -> List[str]:
        """优先使用 LLM 输出的真实图谱标签，缺失时再做自然语言规范化。"""
        labels = self._normalize_target_labels(graph_query.target_labels or [])
        if labels:
            return labels
        return self._normalize_target_labels(graph_query.target_entities or [])

    def _get_query_relation_types(self, graph_query: GraphQuery) -> List[str]:
        """优先使用 LLM 输出的真实关系类型，缺失时再做自然语言规范化。"""
        relation_types = self._normalize_relation_types(graph_query.normalized_relation_types or [])
        if relation_types:
            return relation_types
        return self._normalize_relation_types(graph_query.relation_types or [])

    def _infer_subgraph_target_labels(self, graph_query: GraphQuery, query: str = "") -> List[str]:
        """为子图抽取推断需要优先保留的节点类型。"""
        labels = self._get_query_target_labels(graph_query)
        relation_text = " ".join(graph_query.relation_types or [])
        source_text = " ".join(graph_query.source_entities or [])
        target_text = " ".join(graph_query.target_entities or [])
        hint_text = f"{query} {source_text} {target_text} {relation_text}"

        inferred = []
        if any(word in hint_text for word in ["技巧", "知识", "知识点", "要点", "注意事项", "适用场景", "场景", "腌肉", "腌（肉）", "腌制", "腌渍"]):
            inferred.extend(["TechniqueDoc", "TechniqueChunk"])
        if any(word in hint_text for word in ["怎么做", "做法", "步骤", "流程", "过程", "制作"]):
            inferred.append("CookingStep")
        if any(word in hint_text for word in ["配什么", "搭配", "食材", "原料", "配料", "蔬菜", "肉类"]):
            inferred.append("Ingredient")
        if any(word in hint_text for word in ["分类", "菜系", "属于", "类别", "特色"]):
            inferred.append("Category")
        if any(word in hint_text for word in ["难度", "简单", "复杂", "上手"]):
            inferred.append("DifficultyLevel")

        for label in inferred:
            if label not in labels:
                labels.append(label)
        return labels

    def _infer_subgraph_relation_types(self, graph_query: GraphQuery, query: str = "") -> List[str]:
        """为子图抽取推断需要优先保留的关系类型。"""
        relation_types = self._get_query_relation_types(graph_query)
        relation_text = " ".join(graph_query.relation_types or [])
        hint_text = " ".join([query] + (graph_query.source_entities or []) + (graph_query.target_entities or []) + [relation_text])

        inferred = []
        if any(word in hint_text for word in ["技巧", "知识", "知识点", "要点", "注意事项", "适用场景", "场景", "腌肉", "腌（肉）", "腌制", "腌渍", "章节", "内容"]):
            inferred.append("HAS_CHUNK")
        if any(word in hint_text for word in ["怎么做", "做法", "步骤", "流程", "过程", "制作"]):
            inferred.extend(["CONTAINS_STEP", "NEXT_STEP"])
        if any(word in hint_text for word in ["配什么", "搭配", "食材", "原料", "配料", "蔬菜", "肉类"]):
            inferred.append("REQUIRES")
        if any(word in hint_text for word in ["分类", "菜系", "属于", "类别", "特色"]):
            inferred.extend(["BELONGS_TO_CATEGORY", "BELONGS_TO"])
        if any(word in hint_text for word in ["难度", "简单", "复杂", "上手"]):
            inferred.extend(["HAS_DIFFICULTY_LEVEL", "DIFFICULTY_LEVEL"])
        if any(word in hint_text for word in ["相似", "类似", "同类", "推荐"]):
            inferred.extend(["SIMILAR", "USES_SAME_TOOL", "USES_SAME_METHOD"])

        for rel_type in inferred:
            if rel_type not in relation_types:
                relation_types.append(rel_type)
        return relation_types

    def _node_key(self, node: Dict[str, Any]) -> str:
        """节点去重键。"""
        return str(node.get("id") or node.get("name") or json.dumps(node, ensure_ascii=False, sort_keys=True))

    def _relationship_key(self, rel: Dict[str, Any]) -> str:
        """关系去重键。"""
        return "|".join([
            str(rel.get("start", {}).get("id") or rel.get("start", {}).get("name") or ""),
            str(rel.get("type") or ""),
            str(rel.get("end", {}).get("id") or rel.get("end", {}).get("name") or ""),
        ])

    def _serialize_node(self, node: Any) -> Dict[str, Any]:
        """统一序列化Neo4j节点对象，保留名称、标签和属性。"""
        if isinstance(node, dict):
            properties = dict(node)
            labels = list(node.get("labels", []))
        else:
            try:
                properties = dict(node)
            except Exception:
                properties = {}
            labels = list(getattr(node, "labels", []))

        return {
            "id": properties.get("nodeId", ""),
            "name": properties.get("name", ""),
            "labels": labels,
            "properties": properties
        }

    def _serialize_relationship(self, rel: Any) -> Any:
        """统一序列化Neo4j关系对象，支持子图查询中返回的嵌套关系列表。"""
        if isinstance(rel, (list, tuple)):
            flattened = []
            for item in rel:
                serialized = self._serialize_relationship(item)
                if isinstance(serialized, list):
                    flattened.extend(serialized)
                elif serialized:
                    flattened.append(serialized)
            return flattened

        try:
            properties = dict(rel)
        except Exception:
            properties = {}

        start_node = getattr(rel, "start_node", None)
        end_node = getattr(rel, "end_node", None)
        if start_node is None or end_node is None:
            nodes = getattr(rel, "nodes", None)
            if nodes and len(nodes) == 2:
                start_node, end_node = nodes

        rel_type = getattr(rel, "type", None)
        if callable(rel_type):
            rel_type = rel_type()
        if not rel_type:
            rel_type = type(rel).__name__

        return {
            "type": rel_type,
            "properties": properties,
            "start": self._serialize_node(start_node) if start_node is not None else {},
            "end": self._serialize_node(end_node) if end_node is not None else {}
        }

    def _format_node_brief(self, node: Dict[str, Any]) -> str:
        """将节点格式化为适合展示的紧凑文本。"""
        name = node.get("name") or node.get("properties", {}).get("name") or "未知节点"
        labels = node.get("labels") or []
        label = labels[0] if labels else "Node"
        return f"{name}（{label}）"

    def _format_relationship_text(self, rel: Dict[str, Any]) -> str:
        """将关系和两端节点转成更适合LLM消费的自然语言。"""
        start_name = rel.get("start", {}).get("name", "起点")
        end_name = rel.get("end", {}).get("name", "终点")
        rel_type = rel.get("type", "相关")
        phrase = {
            "REQUIRES": "需要",
            "CONTAINS_STEP": "包含步骤",
            "BELONGS_TO": "属于",
            "BELONGS_TO_CATEGORY": "属于分类",
            "DIFFICULTY_LEVEL": "对应难度",
            "HAS_DIFFICULTY_LEVEL": "具有难度",
            "HAS_CONCEPT_TYPE": "具有概念类型",
            "NEXT_STEP": "下一步是",
            "SIMILAR": "相似于",
            "USES_SAME_TOOL": "与之使用相同工具的是",
            "USES_SAME_METHOD": "与之使用相同方法的是",
        }.get(rel_type, rel_type)

        detail_parts = []
        props = rel.get("properties", {})
        if props.get("amount") and props.get("unit"):
            detail_parts.append(f"{props['amount']}{props['unit']}")
        if props.get("stepOrder") is not None:
            detail_parts.append(f"步骤顺序 {props['stepOrder']}")
        if props.get("similarity") is not None:
            detail_parts.append(f"相似度 {props['similarity']}")

        detail = f"（{'，'.join(detail_parts)}）" if detail_parts else ""
        return f"{start_name} {phrase} {end_name}{detail}"

    def _infer_path_conclusion(self, path: GraphPath) -> str:
        """基于路径结构生成一个简洁的推理结论。"""
        if len(path.nodes) < 2:
            return ""

        rel_types = [rel.get("type", "") for rel in path.relationships]
        node_labels = [node.get("labels", []) for node in path.nodes]
        start_name = path.nodes[0].get("name", "起点")
        end_name = path.nodes[-1].get("name", "终点")

        if rel_types.count("REQUIRES") >= 2 and any("Recipe" in labels for labels in node_labels):
            return f"{start_name} 与 {end_name} 通过同一道菜谱发生共现，适合用于回答食材搭配或菜谱关联问题。"
        if "CONTAINS_STEP" in rel_types or "NEXT_STEP" in rel_types:
            return f"这条路径体现了从实体到烹饪步骤的流程关系，可用于解释制作顺序或操作过程。"
        if "BELONGS_TO" in rel_types or "BELONGS_TO_CATEGORY" in rel_types:
            return f"这条路径展示了 {start_name} 与 {end_name} 的类别归属关系，可用于回答分类或菜系问题。"

        return f"{start_name} 与 {end_name} 之间存在 {path.path_length} 跳关联，可作为图谱推理的证据路径。"

    def _group_nodes_by_label(self, nodes: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """按节点标签聚合名称，便于构造高密度上下文。"""
        grouped: Dict[str, List[str]] = {}
        for node in nodes:
            name = node.get("name") or node.get("properties", {}).get("name")
            labels = node.get("labels") or ["Node"]
            label = labels[0]
            if not name:
                continue
            grouped.setdefault(label, [])
            if name not in grouped[label]:
                grouped[label].append(name)
        return grouped

    def _summarize_relationships(self, relationships: List[Dict[str, Any]]) -> List[str]:
        """关系去重后转为自然语言摘要。"""
        lines = []
        seen = set()
        for rel in relationships:
            line = self._format_relationship_text(rel)
            if line not in seen:
                seen.add(line)
                lines.append(line)
        return lines

    def _top_node_names_by_label(self, nodes: List[Dict[str, Any]], label: str, limit: int = 5) -> List[str]:
        """提取某类节点的前几个名称。"""
        names = []
        for node in nodes:
            if label in (node.get("labels") or []):
                name = node.get("name") or node.get("properties", {}).get("name")
                if name and name not in names:
                    names.append(name)
            if len(names) >= limit:
                break
        return names

    def _extract_relation_targets(self, relationships: List[Dict[str, Any]], rel_types: set, limit: int = 4) -> List[str]:
        """按关系类型抽取终点节点名称。"""
        targets = []
        for rel in relationships:
            if rel.get("type") in rel_types:
                name = rel.get("end", {}).get("name")
                if name and name not in targets:
                    targets.append(name)
            if len(targets) >= limit:
                break
        return targets

    def _first_available_name(self, nodes: List[Dict[str, Any]]) -> str:
        """获取第一个可用节点名。"""
        for node in nodes:
            name = node.get("name") or node.get("properties", {}).get("name")
            if name:
                return name
        return "该主题"

    def _extract_query_terms(self, query: str) -> List[str]:
        """轻量提取查询中的关键片段，用于推理链筛选。"""
        separators = ["，", "。", "？", "?", "、", " ", "怎么", "如何", "为什么", "哪些"]
        terms = [query]
        for sep in separators:
            split_terms = []
            for term in terms:
                split_terms.extend(term.split(sep))
            terms = split_terms
        return [term.strip() for term in terms if term.strip() and len(term.strip()) >= 2]
    
    def _find_entity_relations(self, graph_query: GraphQuery, session) -> List[GraphPath]:
        """查找实体间关系"""
        source_entities = graph_query.source_entities or []
        target_entities = graph_query.target_entities or []
        relation_types = self._get_query_relation_types(graph_query)
        max_depth = max(1, min(int(graph_query.max_depth or 2), 3))

        if not source_entities:
            return []

        if target_entities:
            cypher_query = f"""
            UNWIND $source_entities as source_name
            UNWIND $target_entities as target_name
            MATCH (source)
            WHERE source.name CONTAINS source_name OR source.nodeId = source_name
            MATCH (target)
            WHERE target.name CONTAINS target_name OR target.nodeId = target_name
            MATCH path = shortestPath((source)-[*1..{max_depth}]-(target))
            WHERE source <> target
            WITH path, relationships(path) as rels, nodes(path) as path_nodes, length(path) as path_len
            WHERE size($relation_types) = 0 OR ALL(r IN rels WHERE type(r) IN $relation_types)
            WITH path, rels, path_nodes, path_len,
                 (1.0 / path_len) +
                 (CASE WHEN size($relation_types) > 0 AND ANY(r IN rels WHERE type(r) IN $relation_types) THEN 0.4 ELSE 0.0 END) as relevance
            ORDER BY relevance DESC
            LIMIT 10
            RETURN path, path_len, rels, path_nodes, relevance
            """
            params = {
                "source_entities": source_entities,
                "target_entities": target_entities,
                "relation_types": relation_types,
            }
        else:
            cypher_query = f"""
            UNWIND $source_entities as source_name
            MATCH (source)
            WHERE source.name CONTAINS source_name OR source.nodeId = source_name
            MATCH path = (source)-[r*1..{max_depth}]-(target)
            WHERE source <> target
            WITH path, relationships(path) as rels, nodes(path) as path_nodes, length(path) as path_len, target
            WHERE size($relation_types) = 0 OR ALL(rel IN rels WHERE type(rel) IN $relation_types)
            WITH path, rels, path_nodes, path_len,
                 (1.0 / path_len) +
                 (COUNT {{ (target)--() }} / 20.0) +
                 (CASE WHEN size($relation_types) > 0 AND ANY(rel IN rels WHERE type(rel) IN $relation_types) THEN 0.4 ELSE 0.0 END) as relevance
            ORDER BY relevance DESC
            LIMIT 10
            RETURN path, path_len, rels, path_nodes, relevance
            """
            params = {
                "source_entities": source_entities,
                "relation_types": relation_types,
            }

        paths = []
        try:
            result = session.run(cypher_query, params)
            for record in result:
                path_data = self._parse_neo4j_path(record)
                if path_data:
                    path_data.path_type = "entity_relation"
                    paths.append(path_data)
        except Exception as e:
            logger.error(f"实体关系查询失败: {e}")
        return paths
    
    def _find_shortest_paths(self, graph_query: GraphQuery, session) -> List[GraphPath]:
        """查找最短路径"""
        source_entities = graph_query.source_entities or []
        target_entities = graph_query.target_entities or []
        max_depth = max(1, min(int(graph_query.max_depth or 3), 4))
        if not source_entities or not target_entities:
            return self._find_entity_relations(graph_query, session)

        cypher_query = f"""
        UNWIND $source_entities as source_name
        UNWIND $target_entities as target_name
        MATCH (source)
        WHERE source.name CONTAINS source_name OR source.nodeId = source_name
        MATCH (target)
        WHERE target.name CONTAINS target_name OR target.nodeId = target_name
        MATCH path = shortestPath((source)-[*1..{max_depth}]-(target))
        WHERE source <> target
        WITH path, relationships(path) as rels, nodes(path) as path_nodes, length(path) as path_len
        WITH path, rels, path_nodes, path_len,
             (1.0 / path_len) +
             (REDUCE(s = 0.0, n IN path_nodes | s + COUNT {{ (n)--() }}) / 20.0 / size(path_nodes)) as relevance
        ORDER BY relevance DESC
        LIMIT 10
        RETURN path, path_len, rels, path_nodes, relevance
        """

        paths = []
        try:
            result = session.run(cypher_query, {
                "source_entities": source_entities,
                "target_entities": target_entities,
            })
            for record in result:
                path_data = self._parse_neo4j_path(record)
                if path_data:
                    path_data.path_type = "shortest_path"
                    paths.append(path_data)
        except Exception as e:
            logger.error(f"最短路径查询失败: {e}")
        return paths
    
    def _fallback_subgraph_extraction(self, graph_query: GraphQuery) -> KnowledgeSubgraph:
        """降级子图提取"""
        return KnowledgeSubgraph(
            central_nodes=[],
            connected_nodes=[],
            relationships=[],
            graph_metrics={},
            reasoning_chains=[]
        )
    
    def close(self):
        """关闭资源连接"""
        if hasattr(self, 'driver') and self.driver:
            self.driver.close()
            logger.info("图RAG检索系统已关闭") 
