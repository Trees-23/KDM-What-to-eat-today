"""
混合检索模块
基于双层检索范式：实体级 + 主题级检索
结合图结构检索和向量检索，使用直接合并去重 + 可选CrossEncoder语义重排
"""

import json
import logging
from datetime import datetime
from typing import List, Dict, Tuple, Any
from dataclasses import dataclass

try:
    from langchain_core.documents import Document
except ImportError:
    class Document:
        def __init__(self, page_content: str = "", metadata: Dict[str, Any] = None):
            self.page_content = page_content
            self.metadata = metadata or {}

try:
    from langchain_community.retrievers import BM25Retriever
except ImportError:
    BM25Retriever = None

try:
    from neo4j import GraphDatabase
except ImportError:
    GraphDatabase = None

try:
    from .graph_indexing import GraphIndexingModule
except ImportError:
    class GraphIndexingModule:
        def __init__(self, *_args, **_kwargs):
            raise ImportError("graph_indexing dependencies are required to initialize GraphIndexingModule")

from rag_modules.rag_audit import query_hash

logger = logging.getLogger(__name__)

@dataclass
class RetrievalResult:
    """检索结果数据结构"""
    content: str
    node_id: str
    node_type: str
    relevance_score: float
    retrieval_level: str  # 'low' or 'high'
    metadata: Dict[str, Any]

class HybridRetrievalModule:
    """
    混合检索模块
    核心特点：
    1. 双层检索范式（实体级 + 主题级）
    2. 关键词提取和匹配
    3. 图结构+向量检索结合
    4. 一跳邻居扩展
    5. 多路候选合并去重 + 语义重排 + 轻量多样性控制
    """
    
    def __init__(self, config, milvus_module, data_module, llm_client):
        self.config = config
        self.milvus_module = milvus_module
        self.data_module = data_module
        self.llm_client = llm_client
        self.driver = None
        self.bm25_retriever = None
        self.reranker = None
        self.reranker_load_failed = False
        
        # 图索引模块
        self.graph_indexing = GraphIndexingModule(config, llm_client)
        self.graph_indexed = False
        
    def initialize(self, chunks: List[Document]):
        """初始化检索系统"""
        logger.info("初始化混合检索模块...")
        
        # 连接Neo4j
        if GraphDatabase is None:
            raise ImportError("neo4j is required to initialize HybridRetrievalModule")
        self.driver = GraphDatabase.driver(
            self.config.neo4j_uri, 
            auth=(self.config.neo4j_user, self.config.neo4j_password)
        )
        
        # 初始化BM25检索器
        if chunks:
            if BM25Retriever is None:
                raise ImportError("langchain_community is required to initialize BM25Retriever")
            self.bm25_retriever = BM25Retriever.from_documents(chunks)
            logger.info(f"BM25检索器初始化完成，文档数量: {len(chunks)}")
        
        # 初始化图索引
        self._build_graph_index()
        
    def _build_graph_index(self):
        """构建图索引"""
        if self.graph_indexed:
            return
            
        logger.info("开始构建图索引...")
        
        try:
            # 获取图数据
            recipes = self.data_module.recipes
            ingredients = self.data_module.ingredients
            cooking_steps = self.data_module.cooking_steps
            technique_docs = getattr(self.data_module, "technique_docs", [])
            technique_chunks = getattr(self.data_module, "technique_chunks", [])
            
            # 创建实体键值对
            self.graph_indexing.create_entity_key_values(
                recipes,
                ingredients,
                cooking_steps,
                technique_docs=technique_docs,
                technique_chunks=technique_chunks,
            )
            
            # 创建关系键值对（这里需要从Neo4j获取关系数据）
            relationships = self._extract_relationships_from_graph()
            self.graph_indexing.create_relation_key_values(relationships)
            
            # 去重优化
            self.graph_indexing.deduplicate_entities_and_relations()
            
            self.graph_indexed = True
            stats = self.graph_indexing.get_statistics()
            logger.info(f"图索引构建完成: {stats}")
            
        except Exception as e:
            logger.error(f"构建图索引失败: {e}")
            
    def _extract_relationships_from_graph(self) -> List[Tuple[str, str, str]]:
        """从Neo4j图中提取关系"""
        relationships = []
        
        try:
            with self.driver.session() as session:
                query = """
                MATCH (source)-[r]->(target)
                WHERE source.nodeId >= '200000000'
                   OR target.nodeId >= '200000000'
                   OR source:TechniqueDoc
                   OR source:TechniqueChunk
                   OR target:TechniqueDoc
                   OR target:TechniqueChunk
                RETURN source.nodeId as source_id, type(r) as relation_type, target.nodeId as target_id
                LIMIT 3000
                """
                result = session.run(query)
                
                for record in result:
                    relationships.append((
                        record["source_id"],
                        record["relation_type"],
                        record["target_id"]
                    ))
                    
        except Exception as e:
            logger.error(f"提取图关系失败: {e}")
            
        return relationships
            
    def extract_query_keywords(self, query: str) -> Tuple[List[str], List[str]]:
        """
        提取查询关键词：实体级 + 主题级
        """
        prompt = f"""
        作为烹饪知识助手，请分析以下查询并提取关键词，分为两个层次：

        查询：{query}

        提取规则：
        1. 实体级关键词：具体的食材、菜品名称、工具、品牌等有形实体
           - 例如：鸡胸肉、西兰花、红烧肉、平底锅、老干妈
           - 对于技巧类查询，保留明确技巧名或文档名，例如：腌肉、焯水、凉拌、微波炉、空气炸锅、食品安全

        2. 主题级关键词：抽象概念、烹饪主题、饮食风格、营养特点等
           - 例如：减肥、低热量、川菜、素食、下饭菜、快手菜、烹饪技巧、去腥、入味、火候、食品安全
           - 排除动作词：推荐、介绍、制作、怎么做等

        示例：
        查询："推荐几个减肥菜" 
        {{
            "entity_keywords": ["鸡胸肉", "西兰花", "水煮蛋", "胡萝卜", "黄瓜"],
            "topic_keywords": ["减肥", "低热量", "高蛋白", "低脂"]
        }}

        查询："川菜有什么特色"
        {{
            "entity_keywords": ["麻婆豆腐", "宫保鸡丁", "水煮鱼", "辣椒", "花椒"],
            "topic_keywords": ["川菜", "麻辣", "香辣", "下饭菜"]
        }}

        查询："请讲讲腌肉的关键要点，适合用在哪些烹饪场景？"
        {{
            "entity_keywords": ["腌肉", "腌（肉）", "腌制", "腌渍"],
            "topic_keywords": ["烹饪技巧", "入味", "调味", "炸", "烤", "快炒"]
        }}

        请严格按照JSON格式返回，不要包含多余的文字：
        {{
            "entity_keywords": ["实体1", "实体2", ...],
            "topic_keywords": ["主题1", "主题2", ...]
        }}
        """
        
        try:
            response = self.llm_client.chat.completions.create(
                model=self.config.llm_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=500
            )
            
            result = json.loads(response.choices[0].message.content.strip())
            entity_keywords = result.get("entity_keywords", [])
            topic_keywords = result.get("topic_keywords", [])
            
            logger.info(f"关键词提取完成 - 实体级: {entity_keywords}, 主题级: {topic_keywords}")
            return entity_keywords, topic_keywords
            
        except Exception as e:
            logger.error(f"关键词提取失败: {e}")
            # 降级方案：简单的关键词分割
            keywords = query.split()
            return keywords[:3], keywords[3:6] if len(keywords) > 3 else keywords
    
    def entity_level_retrieval(self, entity_keywords: List[str], top_k: int = 5) -> List[RetrievalResult]:
        """
        实体级检索：专注于具体实体和关系
        使用图索引的键值对结构进行检索
        """
        results = []
        
        # 1. 使用图索引进行实体检索
        for keyword in entity_keywords:
            # 检索匹配的实体
            entities = self.graph_indexing.get_entities_by_key(keyword)
            
            for entity in entities:
                # 获取邻居信息
                neighbors = self._get_node_neighbors(entity.metadata["node_id"], max_neighbors=2)
                neighbor_text = self._format_node_neighbors(neighbors)
                
                # 构建增强内容
                enhanced_content = f"命中关键词: {keyword}\n{entity.value_content}"
                if neighbor_text:
                    enhanced_content += f"\n关联图谱:\n{neighbor_text}"
                
                results.append(RetrievalResult(
                    content=enhanced_content,
                    node_id=entity.metadata["node_id"],
                    node_type=entity.entity_type,
                    relevance_score=0.9,  # 精确匹配得分较高
                    retrieval_level="entity",
                    metadata={
                        "entity_name": entity.entity_name,
                        "entity_type": entity.entity_type,
                        "index_keys": entity.index_keys,
                        "matched_keyword": keyword,
                        "graph_neighbors": neighbors
                    }
                ))
        
        # 2. 如果图索引结果不足，使用Neo4j进行补充检索
        if len(results) < top_k:
            neo4j_results = self._neo4j_entity_level_search(entity_keywords, top_k - len(results))
            results.extend(neo4j_results)
            
        # 3. 按相关性排序并返回
        results.sort(key=lambda x: x.relevance_score, reverse=True)
        
        logger.info(f"实体级检索完成，返回 {len(results)} 个结果")
        return results[:top_k]
    
    def _neo4j_entity_level_search(self, keywords: List[str], limit: int) -> List[RetrievalResult]:
        """Neo4j补充检索"""
        results = []
        
        # 删掉了 WHERE node:Recipe
        try:
            with self.driver.session() as session:
                cypher_query = """
                UNWIND $keywords as keyword
                CALL db.index.fulltext.queryNodes('recipe_fulltext_index', keyword + '*') 
                YIELD node, score

                RETURN 
                    node.nodeId as node_id,
                    node.name as name,
                    node.description as description,
                    labels(node) as labels,
                    score,
                    keyword as matched_keyword
                ORDER BY score DESC
                LIMIT $limit
                """
                
                result = session.run(cypher_query, {
                    "keywords": keywords,
                    "limit": limit
                })
                
                for record in result:
                    content_parts = []
                    if record["matched_keyword"]:
                        content_parts.append(f"命中关键词: {record['matched_keyword']}")
                    if record["name"]:
                        content_parts.append(f"菜品: {record['name']}")
                    if record["description"]:
                        content_parts.append(f"描述: {record['description']}")

                    neighbors = self._get_node_neighbors(record["node_id"], max_neighbors=2)
                    neighbor_text = self._format_node_neighbors(neighbors)
                    if neighbor_text:
                        content_parts.append(f"关联图谱:\n{neighbor_text}")
                    
                    results.append(RetrievalResult(
                        content='\n'.join(content_parts),
                        node_id=record["node_id"],
                        node_type="Recipe",
                        relevance_score=float(record["score"]) * 0.7,  # 补充检索得分较低
                        retrieval_level="entity",
                        metadata={
                            "name": record["name"],
                            "labels": record["labels"],
                            "matched_keyword": record["matched_keyword"],
                            "source": "neo4j_fallback",
                            "graph_neighbors": neighbors
                        }
                    ))
                    
        except Exception as e:
            logger.error(f"Neo4j补充检索失败: {e}")
            
        return results
    
    def topic_level_retrieval(self, topic_keywords: List[str], top_k: int = 5) -> List[RetrievalResult]:
        """
        主题级检索：专注于广泛主题和概念
        使用图索引的关系键值对结构进行主题检索
        """
        results = []
        
        # 1. 使用图索引进行关系/主题检索
        for keyword in topic_keywords:
            # 检索匹配的关系
            relations = self.graph_indexing.get_relations_by_key(keyword)
            
            for relation in relations:
                # 获取相关实体信息
                source_entity = self.graph_indexing.entity_kv_store.get(relation.source_entity)
                target_entity = self.graph_indexing.entity_kv_store.get(relation.target_entity)
                
                if source_entity and target_entity:
                    neighbors = self._get_node_neighbors(relation.source_entity, max_neighbors=2)
                    neighbor_text = self._format_node_neighbors(neighbors)

                    # 构建丰富的主题内容
                    content_parts = [
                        f"命中关键词: {keyword}",
                        relation.value_content,
                        f"相关菜品: {source_entity.entity_name}",
                        f"相关信息: {target_entity.entity_name}"
                    ]
                    if neighbor_text:
                        content_parts.append(f"关联图谱:\n{neighbor_text}")
                    
                    # 添加源实体的详细信息
                    if source_entity.entity_type == "Recipe":
                        newline = '\n'
                        content_parts.append(f"菜品详情: {source_entity.value_content.split(newline)[0]}")
                    
                    results.append(RetrievalResult(
                        content='\n'.join(content_parts),
                        node_id=relation.source_entity,  # 以主要实体为ID
                        node_type=source_entity.entity_type,
                        relevance_score=0.95,  # 主题匹配得分
                        retrieval_level="topic",
                        metadata={
                            "relation_id": relation.relation_id,
                            "relation_type": relation.relation_type,
                            "source_name": source_entity.entity_name,
                            "target_name": target_entity.entity_name,
                            "matched_keyword": keyword,
                            "index_keys": relation.index_keys,
                            "graph_neighbors": neighbors
                        }
                    ))
        
        # 2. 使用实体的分类信息进行主题检索
        for keyword in topic_keywords:
            entities = self.graph_indexing.get_entities_by_key(keyword)
            for entity in entities:
                if entity.entity_type == "Recipe":
                    neighbors = self._get_node_neighbors(entity.metadata["node_id"], max_neighbors=2)
                    neighbor_text = self._format_node_neighbors(neighbors)

                    # 构建分类主题内容
                    content_parts = [
                        f"命中关键词: {keyword}",
                        entity.value_content
                    ]
                    if neighbor_text:
                        content_parts.append(f"关联图谱:\n{neighbor_text}")
                    
                    results.append(RetrievalResult(
                        content='\n'.join(content_parts),
                        node_id=entity.metadata["node_id"],
                        node_type=entity.entity_type,
                        relevance_score=0.85,  # 分类匹配得分
                        retrieval_level="topic",
                        metadata={
                            "entity_name": entity.entity_name,
                            "entity_type": entity.entity_type,
                            "matched_keyword": keyword,
                            "source": "category_match",
                            "graph_neighbors": neighbors
                        }
                    ))
        
        # 3. 如果结果不足，使用Neo4j进行补充检索
        if len(results) < top_k:
            neo4j_results = self._neo4j_topic_level_search(topic_keywords, top_k - len(results))
            results.extend(neo4j_results)
            
        # 4. 按相关性排序并返回
        results.sort(key=lambda x: x.relevance_score, reverse=True)
        
        logger.info(f"主题级检索完成，返回 {len(results)} 个结果")
        return results[:top_k]
    
    def _neo4j_topic_level_search(self, keywords: List[str], limit: int) -> List[RetrievalResult]:
        """Neo4j主题级检索补充"""
        results = []
        
        try:
            with self.driver.session() as session:
                cypher_query = """
                UNWIND $keywords as keyword
                MATCH (r:Recipe)
                WHERE r.category CONTAINS keyword 
                   OR r.cuisineType CONTAINS keyword
                   OR r.tags CONTAINS keyword
                WITH r, keyword
                OPTIONAL MATCH (r)-[:REQUIRES]->(i:Ingredient)
                WITH r, keyword, collect(i.name)[0..3] as ingredients
                RETURN 
                    r.nodeId as node_id,
                    r.name as name,
                    r.category as category,
                    r.cuisineType as cuisine_type,
                    r.difficulty as difficulty,
                    ingredients,
                    keyword as matched_keyword
                ORDER BY r.difficulty ASC, r.name
                LIMIT $limit
                """
                
                result = session.run(cypher_query, {
                    "keywords": keywords,
                    "limit": limit
                })
                
                for record in result:
                    content_parts = []
                    if record["matched_keyword"]:
                        content_parts.append(f"命中关键词: {record['matched_keyword']}")
                    content_parts.append(f"菜品: {record['name']}")
                    
                    if record["category"]:
                        content_parts.append(f"分类: {record['category']}")
                    if record["cuisine_type"]:
                        content_parts.append(f"菜系: {record['cuisine_type']}")
                    if record["difficulty"]:
                        content_parts.append(f"难度: {record['difficulty']}")
                    
                    if record["ingredients"]:
                        ingredients_str = ', '.join(record["ingredients"][:3])
                        content_parts.append(f"主要食材: {ingredients_str}")

                    neighbors = self._get_node_neighbors(record["node_id"], max_neighbors=3)
                    neighbor_text = self._format_node_neighbors(neighbors)
                    if neighbor_text:
                        content_parts.append(f"关联图谱:\n{neighbor_text}")
                    
                    results.append(RetrievalResult(
                        content='\n'.join(content_parts),
                        node_id=record["node_id"],
                        node_type="Recipe",
                        relevance_score=0.75,  # 补充检索得分
                        retrieval_level="topic",
                        metadata={
                            "name": record["name"],
                            "category": record["category"],
                            "cuisine_type": record["cuisine_type"],
                            "difficulty": record["difficulty"],
                            "matched_keyword": record["matched_keyword"],
                            "source": "neo4j_fallback",
                            "graph_neighbors": neighbors
                        }
                    ))
                    
        except Exception as e:
            logger.error(f"Neo4j主题级检索失败: {e}")
            
        return results
        
    def dual_level_retrieval(self, query: str, top_k: int = 5) -> List[Document]:
        """
        双层检索：结合实体级和主题级检索
        """
        logger.info(f"开始双层检索: {query}")
        
        # 1. 提取关键词
        entity_keywords, topic_keywords = self.extract_query_keywords(query)
        
        # 2. 执行双层检索
        entity_results = self.entity_level_retrieval(entity_keywords, top_k)
        topic_results = self.topic_level_retrieval(topic_keywords, top_k)
        
        # 3. 结果合并和排序
        all_results = entity_results + topic_results
        
        # 4. 去重和重排序
        seen_nodes = set()
        unique_results = []
        
        for result in sorted(all_results, key=lambda x: x.relevance_score, reverse=True):
            if result.node_id not in seen_nodes:
                seen_nodes.add(result.node_id)
                unique_results.append(result)
        
        # 5. 转换为Document格式
        documents = [
            self._retrieval_result_to_document(result, search_type="dual_level")
            for result in unique_results[:top_k]
        ]
            
        logger.info(f"双层检索完成，返回 {len(documents)} 个文档")
        return documents

    def _retrieval_result_to_document(self, result: RetrievalResult, search_type: str) -> Document:
        """将内部检索结果转换为 LangChain Document，并补齐统一元数据。"""
        recipe_name = (
            result.metadata.get("name")
            or result.metadata.get("entity_name")
            or result.metadata.get("source_name")
            or "未知菜品"
        )

        return Document(
            page_content=result.content,
            metadata={
                "node_id": result.node_id,
                "node_type": result.node_type,
                "retrieval_level": result.retrieval_level,
                "relevance_score": result.relevance_score,
                "recipe_name": recipe_name,
                "search_type": search_type,
                **result.metadata
            }
        )

    @staticmethod
    def _candidate_pool_size(top_k: int) -> int:
        """每路召回候选池大小。Rerank前适度扩召回，避免候选池过大。"""
        return max(top_k * 2, 8)

    @staticmethod
    def _document_dedupe_key(doc: Document) -> str:
        """跨检索源去重键：优先 node_id，其次 recipe_name，最后内容 hash。"""
        metadata = doc.metadata or {}
        node_id = metadata.get("node_id")
        if node_id:
            return f"node:{node_id}"
        recipe_name = metadata.get("recipe_name")
        if recipe_name and recipe_name != "未知菜品":
            return f"recipe:{recipe_name}"
        return f"content:{hash(doc.page_content[:300])}"

    @staticmethod
    def _category_key(doc: Document) -> str:
        """用于结果多样性控制的粗粒度类别。"""
        metadata = doc.metadata or {}
        return str(
            metadata.get("category")
            or metadata.get("cuisine_type")
            or metadata.get("node_type")
            or ""
        ).strip()

    def _merge_retrieved_documents(self, ranked_sources: Dict[str, List[Document]]) -> List[Document]:
        """直接合并多路候选并去重，保留更丰富的同源菜谱文本。"""
        merged: Dict[str, Dict[str, Any]] = {}

        for source_name, docs in ranked_sources.items():
            for rank, doc in enumerate(docs, start=1):
                key = self._document_dedupe_key(doc)
                entry = merged.setdefault(
                    key,
                    {
                        "doc": doc,
                        "sources": {},
                        "first_order": len(merged),
                    }
                )
                entry["sources"][source_name] = rank

                # 同一个菜谱可能被多路召回，后续rerank更依赖文本信息，保留内容更完整的版本。
                if len(doc.page_content or "") > len(entry["doc"].page_content or ""):
                    entry["doc"] = doc

        candidates = []
        for entry in sorted(merged.values(), key=lambda item: item["first_order"]):
            doc = entry["doc"]
            sources = entry["sources"]
            doc.metadata.update({
                "search_method": "direct_merge",
                "merge_sources": sorted(sources.keys()),
                "source_ranks": dict(sorted(sources.items())),
                "source_coverage": len(sources),
            })
            candidates.append(doc)

        for order, doc in enumerate(candidates):
            doc.metadata["merge_order"] = order
        return candidates

    def _collect_technique_node_ids_from_docs(self, documents: List[Document]) -> List[str]:
        """从混合检索候选中收集技巧文档/章节 node_id。"""
        node_ids = []
        seen = set()
        for doc in documents:
            metadata = doc.metadata or {}
            node_type = metadata.get("node_type") or metadata.get("entity_type")
            node_id = metadata.get("node_id")
            if node_type not in {"TechniqueDoc", "TechniqueChunk"} or not node_id:
                continue
            if node_id not in seen:
                seen.add(node_id)
                node_ids.append(node_id)
        return node_ids

    @staticmethod
    def _format_technique_chunk_record(record: Dict[str, Any], max_chars: int = 900) -> str:
        """将技巧章节记录格式化为可直接进入上下文的正文片段。"""
        title = record.get("section_title") or record.get("chunk_name") or "技巧章节"
        content = record.get("content") or record.get("summary") or ""
        if not content:
            return ""
        return f"## {title}\n{str(content).strip()[:max_chars]}"

    def _fetch_technique_sibling_chunks(self, node_ids: List[str], limit: int = 8) -> List[Dict[str, Any]]:
        """命中 TechniqueDoc/TechniqueChunk 后查询同文档兄弟章节。"""
        if not node_ids:
            return []
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
                RETURN
                    doc.nodeId AS doc_id,
                    doc.name AS doc_name,
                    chunk.nodeId AS chunk_id,
                    chunk.name AS chunk_name,
                    chunk.sectionTitle AS section_title,
                    chunk.summary AS summary,
                    chunk.content AS content,
                    COALESCE(r.chunkOrder, chunk.chunkIndex, 999) AS chunk_order
                ORDER BY doc.nodeId, chunk_order
                LIMIT $limit
                """
                result = session.run(query, {"node_ids": node_ids, "limit": limit})
                return [dict(record) for record in result]
        except Exception as e:
            logger.error(f"混合检索补充技巧兄弟章节失败: {e}")
            return []

    def _expand_technique_contexts(self, documents: List[Document], limit: int = 8, audit_run=None) -> List[Document]:
        """为命中的技巧文档/章节补充同文档兄弟 chunk。"""
        node_ids = self._collect_technique_node_ids_from_docs(documents)
        if not node_ids:
            if audit_run:
                audit_run.append_process(
                    "Hybrid Technique Expansion",
                    {"enabled": True, "seed_count": 0, "expanded_count": 0},
                )
            return documents

        rows = self._fetch_technique_sibling_chunks(node_ids, limit=limit)
        sections = []
        seen_sections = set()
        doc_names = []
        chunk_ids = []

        for row in rows:
            doc_name = row.get("doc_name")
            if doc_name and doc_name not in doc_names:
                doc_names.append(doc_name)
            chunk_id = row.get("chunk_id")
            if chunk_id:
                chunk_ids.append(chunk_id)
            text = self._format_technique_chunk_record(row)
            if text and text not in seen_sections:
                seen_sections.add(text)
                sections.append(text)

        if not sections:
            if audit_run:
                audit_run.append_process(
                    "Hybrid Technique Expansion",
                    {"enabled": True, "seed_count": len(node_ids), "expanded_count": 0},
                )
            return documents

        title = "、".join(doc_names[:3]) if doc_names else "技巧文档"
        content = "\n".join([
            f"技巧文档扩展上下文: {title}",
            "关键技巧内容:",
            *sections,
        ])
        doc = Document(
            page_content=content,
            metadata={
                "node_id": f"technique_expansion:{','.join(node_ids[:5])}",
                "node_type": "TechniqueExpansion",
                "recipe_name": title,
                "search_type": "technique_expansion",
                "retrieval_level": "context_expansion",
                "relevance_score": 0.98,
                "source": "technique_sibling_chunks",
                "seed_node_ids": node_ids,
                "expanded_chunk_ids": chunk_ids,
                "category": "烹饪技巧",
            },
        )
        expanded = documents + [doc]
        if audit_run:
            audit_run.append_process(
                "Hybrid Technique Expansion",
                {
                    "enabled": True,
                    "seed_count": len(node_ids),
                    "expanded_count": len(sections),
                    "doc_names": doc_names[:5],
                },
            )
            audit_run.write_documents(
                "Hybrid Retrieval / Technique Expanded Context",
                [doc],
                "technique_expansion",
            )
        return expanded

    def _ensure_technique_expansion_in_final(
        self,
        final_docs: List[Document],
        candidates: List[Document],
        top_k: int,
        audit_run=None,
    ) -> List[Document]:
        """命中技巧节点时，确保兄弟章节扩展上下文进入最终结果。"""
        expansion_docs = [
            doc for doc in candidates
            if (doc.metadata or {}).get("search_type") == "technique_expansion"
        ]
        if not expansion_docs:
            return final_docs

        selected_keys = {self._document_dedupe_key(doc) for doc in final_docs}
        if any(self._document_dedupe_key(doc) in selected_keys for doc in expansion_docs):
            return final_docs

        expansion_doc = expansion_docs[0]
        preserved = list(final_docs)
        if len(preserved) >= top_k and preserved:
            replace_index = self._find_low_priority_replacement_index(preserved)
            replaced_doc = preserved[replace_index]
            preserved[replace_index] = expansion_doc
            replaced_name = (replaced_doc.metadata or {}).get("recipe_name", "")
        else:
            preserved.append(expansion_doc)
            replaced_name = ""

        for order, doc in enumerate(preserved[:top_k]):
            doc.metadata["result_order"] = order
            doc.metadata["technique_expansion_forced"] = (
                (doc.metadata or {}).get("search_type") == "technique_expansion"
            )

        if audit_run:
            audit_run.append_process(
                "Hybrid Technique Expansion Final Guard",
                {
                    "enabled": True,
                    "inserted": True,
                    "replaced_recipe_name": replaced_name,
                    "final_count": len(preserved[:top_k]),
                },
            )
        return preserved[:top_k]

    def _find_low_priority_replacement_index(self, documents: List[Document]) -> int:
        """选择最终结果中最适合被技巧扩展上下文替换的位置。"""
        for index in range(len(documents) - 1, -1, -1):
            metadata = documents[index].metadata or {}
            if metadata.get("node_type") not in {"TechniqueDoc", "TechniqueChunk", "TechniqueExpansion"}:
                return index
        return len(documents) - 1

    def _get_reranker(self):
        """懒加载CrossEncoder reranker；加载失败时降级为合并后的原始顺序。"""
        if self.reranker is not None:
            return self.reranker
        if self.reranker_load_failed:
            return None

        model_name = getattr(self.config, "rerank_model", "BAAI/bge-reranker-base")
        try:
            from sentence_transformers import CrossEncoder

            self.reranker = CrossEncoder(model_name)
            logger.info(f"Reranker加载完成: {model_name}")
            return self.reranker
        except Exception as e:
            self.reranker_load_failed = True
            logger.warning(f"Reranker加载失败，将退回合并顺序: {e}")
            return None

    @staticmethod
    def _rerank_text(doc: Document, max_chars: int = 900) -> str:
        """构造给reranker的候选文本，优先保留菜谱名和关键元数据。"""
        metadata = doc.metadata or {}
        content = doc.page_content or ""
        prefix_parts = []
        recipe_name = metadata.get("recipe_name") or metadata.get("name")
        if recipe_name and str(recipe_name) not in content:
            prefix_parts.append(f"菜品: {recipe_name}")
        category = metadata.get("category")
        if category and str(category) not in content:
            prefix_parts.append(f"分类: {category}")
        cuisine_type = metadata.get("cuisine_type")
        if cuisine_type and str(cuisine_type) not in content:
            prefix_parts.append(f"菜系: {cuisine_type}")
        matched_keyword = metadata.get("matched_keyword")
        if matched_keyword and str(matched_keyword) not in content:
            prefix_parts.append(f"命中关键词: {matched_keyword}")

        text = "\n".join(prefix_parts + [content]).strip()
        return text[:max_chars]

    def _rerank_documents(self, query: str, documents: List[Document], top_k: int, audit_run=None) -> List[Document]:
        """对合并候选池做语义精排，失败则保持合并顺序。"""
        started_at = datetime.now()
        if not documents or not getattr(self.config, "enable_rerank", True):
            if audit_run:
                audit_run.append_process(
                    "Hybrid Rerank",
                    {
                        "enabled": bool(getattr(self.config, "enable_rerank", True)),
                        "model": getattr(self.config, "rerank_model", ""),
                        "load_success": False,
                        "batch_size": getattr(self.config, "rerank_batch_size", 8),
                        "candidate_count": len(documents),
                        "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                        "fallback_used": True,
                    },
                )
            return self._apply_diversity(documents, top_k, audit_run=audit_run)

        reranker = self._get_reranker()
        if reranker is None:
            if audit_run:
                audit_run.append_process(
                    "Hybrid Rerank",
                    {
                        "enabled": True,
                        "model": getattr(self.config, "rerank_model", ""),
                        "load_success": False,
                        "batch_size": getattr(self.config, "rerank_batch_size", 8),
                        "candidate_count": len(documents),
                        "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                        "fallback_used": True,
                    },
                )
            return self._apply_diversity(documents, top_k, audit_run=audit_run)

        try:
            pairs = [(query, self._rerank_text(doc)) for doc in documents]
            if audit_run:
                audit_run.append_recall(
                    "Hybrid Retrieval / Rerank Input Texts",
                    self._format_rerank_inputs(documents),
                )
            batch_size = int(getattr(self.config, "rerank_batch_size", 8))
            scores = reranker.predict(pairs, batch_size=batch_size)

            scored_docs = []
            for doc, score in zip(documents, scores):
                rerank_score = float(score)
                doc.metadata["rerank_score"] = rerank_score
                doc.metadata["search_method"] = "direct_merge_bge_rerank"
                scored_docs.append(doc)

            scored_docs.sort(key=lambda doc: doc.metadata.get("rerank_score", 0.0), reverse=True)
            if audit_run:
                audit_run.append_process(
                    "Hybrid Rerank",
                    {
                        "enabled": True,
                        "model": getattr(self.config, "rerank_model", ""),
                        "load_success": True,
                        "batch_size": batch_size,
                        "candidate_count": len(documents),
                        "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                        "fallback_used": False,
                    },
                )
                audit_run.write_documents(
                    "Hybrid Retrieval / Reranked Results",
                    scored_docs,
                    "reranked_results",
                )
            reranked = self._apply_diversity(scored_docs, top_k, audit_run=audit_run)
            for order, doc in enumerate(reranked):
                doc.metadata["rerank_order"] = order
            return reranked
        except Exception as e:
            logger.warning(f"Rerank执行失败，将退回合并顺序: {e}")
            if audit_run:
                audit_run.record_error("hybrid_rerank", e, fallback_used=True)
            return self._apply_diversity(documents, top_k, audit_run=audit_run)

    def _apply_diversity(
        self,
        documents: List[Document],
        top_k: int,
        *,
        max_per_category: int = 2,
        audit_run=None,
    ) -> List[Document]:
        """轻量多样性控制，避免同一类别/菜系挤占全部 top_k。"""
        selected = []
        deferred = []
        category_counts: Dict[str, int] = {}

        for doc in documents:
            category = self._category_key(doc)
            if category and category_counts.get(category, 0) >= max_per_category:
                deferred.append(doc)
                continue
            selected.append(doc)
            if category:
                category_counts[category] = category_counts.get(category, 0) + 1
            if len(selected) >= top_k:
                break

        if len(selected) < top_k:
            selected_keys = {self._document_dedupe_key(doc) for doc in selected}
            for doc in deferred:
                key = self._document_dedupe_key(doc)
                if key in selected_keys:
                    continue
                selected.append(doc)
                selected_keys.add(key)
                if len(selected) >= top_k:
                    break

        for order, doc in enumerate(selected):
            doc.metadata["result_order"] = order
        if audit_run:
            audit_run.append_process(
                "Hybrid Diversity",
                {
                    "max_per_category": max_per_category,
                    "category_counts": category_counts,
                    "deferred_count": len(deferred),
                    "selected_count": len(selected[:top_k]),
                },
            )
        return selected[:top_k]
    
    def vector_search_enhanced(self, query: str, top_k: int = 5) -> List[Document]:
        """
        增强的向量检索：结合图信息
        """
        try:
            # 使用Milvus进行向量检索
            vector_docs = self.milvus_module.similarity_search(query, k=top_k*2)
            
            # 用图信息增强结果并转换为Document对象
            enhanced_docs = []
            for result in vector_docs:
                # 从Milvus结果创建Document对象
                content = result.get("text", "")
                metadata = result.get("metadata", {})
                node_id = metadata.get("node_id")
                
                if node_id:
                    # 从图中获取邻居信息
                    neighbors = self._get_node_neighbors(node_id)
                    neighbor_text = self._format_node_neighbors(neighbors)
                    if neighbor_text:
                        # 将图关系信息添加到内容中
                        content += f"\n关联图谱:\n{neighbor_text}"
                else:
                    neighbors = []
                
                # 确保recipe_name字段正确设置
                recipe_name = metadata.get("recipe_name", "未知菜品")
                
                # 调试：打印向量得分
                vector_score = result.get("score", 0.0)
                logger.debug(f"向量检索得分: {recipe_name} = {vector_score}")
                
                # 创建Document对象
                doc = Document(
                    page_content=content,
                    metadata={
                        **metadata,
                        "recipe_name": recipe_name,  # 确保有recipe_name字段
                        "score": vector_score,
                        "search_type": "vector_enhanced",
                        "graph_neighbors": neighbors
                    }
                )
                enhanced_docs.append(doc)
                
            return enhanced_docs[:top_k]
            
        except Exception as e:
            logger.error(f"增强向量检索失败: {e}")
            return []
    
    @staticmethod
    def _brief_neighbor_properties(properties: Dict[str, Any]) -> str:
        """抽取少量稳定属性，避免把完整节点属性塞进召回文本。"""
        if not properties:
            return ""

        display_keys = [
            "description",
            "category",
            "cuisineType",
            "difficulty",
            "cookingTime",
            "nutrition",
            "technique",
            "time",
            "order",
        ]
        parts = []
        for key in display_keys:
            value = properties.get(key)
            if value in (None, "", []):
                continue
            parts.append(f"{key}: {value}")
            if len(parts) >= 3:
                break
        return "；".join(parts)

    @staticmethod
    def _format_node_neighbors(neighbors: List[Dict[str, Any]]) -> str:
        """将结构化邻居转成适合写入候选文本的短描述。"""
        lines = []
        for neighbor in neighbors:
            direction = neighbor.get("direction") or "--"
            relation_type = neighbor.get("relation_type") or "RELATED"
            name = neighbor.get("name") or "未知节点"
            labels = neighbor.get("labels") or []
            label_text = f" ({'/'.join(labels)})" if labels else ""
            properties = neighbor.get("property_summary")
            property_text = f": {properties}" if properties else ""
            lines.append(f"- {direction} {relation_type} {name}{label_text}{property_text}")
        return "\n".join(lines)

    def _get_node_neighbors(self, node_id: str, max_neighbors: int = 3) -> List[Dict[str, Any]]:
        """获取节点的一跳邻居，包含关系方向、关系类型、邻居标签和少量属性。"""
        try:
            with self.driver.session() as session:
                query = """
                MATCH (n {nodeId: $node_id})-[r]-(neighbor)
                RETURN
                    neighbor.nodeId as node_id,
                    neighbor.name as name,
                    labels(neighbor) as labels,
                    type(r) as relation_type,
                    CASE WHEN startNode(r) = n THEN 'OUT' ELSE 'IN' END as direction,
                    properties(neighbor) as properties
                LIMIT $limit
                """
                result = session.run(query, {"node_id": node_id, "limit": max_neighbors})
                neighbors = []
                for record in result:
                    properties = dict(record["properties"] or {})
                    neighbors.append({
                        "node_id": record["node_id"],
                        "name": record["name"],
                        "labels": list(record["labels"] or []),
                        "relation_type": record["relation_type"],
                        "direction": record["direction"],
                        "property_summary": self._brief_neighbor_properties(properties),
                    })
                return neighbors
        except Exception as e:
            logger.error(f"获取邻居节点失败: {e}")
            return []
    
    def hybrid_search(self, query: str, top_k: int = 5, audit_run=None) -> List[Document]:
        """
        混合检索：并行执行多种检索策略
        """
        import concurrent.futures

        logger.info(f"开始并行混合检索: {query}")
        hybrid_started_at = datetime.now()

        candidate_k = self._candidate_pool_size(top_k)
        if audit_run:
            audit_run.append_process(
                "Hybrid Retrieval Config",
                {
                    "top_k": top_k,
                    "candidate_k": candidate_k,
                    "enable_rerank": getattr(self.config, "enable_rerank", True),
                    "rerank_model": getattr(self.config, "rerank_model", ""),
                    "rerank_batch_size": getattr(self.config, "rerank_batch_size", 8),
                    "embedding_model": getattr(self.config, "embedding_model", ""),
                },
            )
        keyword_started_at = datetime.now()
        entity_keywords, topic_keywords = self.extract_query_keywords(query)
        if audit_run:
            audit_run.append_process(
                "Hybrid Keyword Extraction",
                {
                    "entity_keywords": entity_keywords,
                    "topic_keywords": topic_keywords,
                    "prompt_template_hash": query_hash("hybrid_extract_query_keywords_v1"),
                    "duration_ms": int((datetime.now() - keyword_started_at).total_seconds() * 1000),
                },
            )

        # 并行执行不同检索策略，控制每路候选数量，合并去重后交给reranker精排。
        entity_docs = []
        topic_docs = []
        vector_docs = []
        branch_stats = {}

        def entity_search():
            nonlocal entity_docs, branch_stats
            started_at = datetime.now()
            try:
                entity_results = self.entity_level_retrieval(entity_keywords, candidate_k)
                entity_docs = [
                    self._retrieval_result_to_document(result, search_type="entity_level")
                    for result in entity_results
                ]
                branch_stats["entity_level"] = {
                    "keywords": entity_keywords,
                    "requested_k": candidate_k,
                    "actual_count": len(entity_docs),
                    "fallback_count": sum(1 for doc in entity_docs if doc.metadata.get("source") == "neo4j_fallback"),
                    "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                }
                logger.info(f"实体级检索完成: {len(entity_docs)} 个候选")
            except Exception as e:
                logger.error(f"实体级检索失败: {e}")
                branch_stats["entity_level"] = {
                    "keywords": entity_keywords,
                    "requested_k": candidate_k,
                    "actual_count": 0,
                    "fallback_count": 0,
                    "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                    "error": str(e),
                }
                if audit_run:
                    audit_run.record_error("hybrid_entity_retrieval", e)
                entity_docs = []

        def topic_search():
            nonlocal topic_docs, branch_stats
            started_at = datetime.now()
            try:
                topic_results = self.topic_level_retrieval(topic_keywords, candidate_k)
                topic_docs = [
                    self._retrieval_result_to_document(result, search_type="topic_level")
                    for result in topic_results
                ]
                branch_stats["topic_level"] = {
                    "keywords": topic_keywords,
                    "requested_k": candidate_k,
                    "actual_count": len(topic_docs),
                    "fallback_count": sum(1 for doc in topic_docs if doc.metadata.get("source") == "neo4j_fallback"),
                    "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                }
                logger.info(f"主题级检索完成: {len(topic_docs)} 个候选")
            except Exception as e:
                logger.error(f"主题级检索失败: {e}")
                branch_stats["topic_level"] = {
                    "keywords": topic_keywords,
                    "requested_k": candidate_k,
                    "actual_count": 0,
                    "fallback_count": 0,
                    "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                    "error": str(e),
                }
                if audit_run:
                    audit_run.record_error("hybrid_topic_retrieval", e)
                topic_docs = []

        def vector_search():
            nonlocal vector_docs, branch_stats
            started_at = datetime.now()
            try:
                vector_docs = self.vector_search_enhanced(query, candidate_k)
                branch_stats["vector_enhanced"] = {
                    "requested_k": candidate_k,
                    "actual_count": len(vector_docs),
                    "collection": getattr(self.config, "milvus_collection_name", ""),
                    "metric": "default",
                    "ef": "default",
                    "embedding_model": getattr(self.config, "embedding_model", ""),
                    "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                }
                logger.info(f"向量检索完成: {len(vector_docs)} 个候选")
            except Exception as e:
                logger.error(f"向量检索失败: {e}")
                branch_stats["vector_enhanced"] = {
                    "requested_k": candidate_k,
                    "actual_count": 0,
                    "duration_ms": int((datetime.now() - started_at).total_seconds() * 1000),
                    "error": str(e),
                }
                if audit_run:
                    audit_run.record_error("hybrid_vector_retrieval", e)
                vector_docs = []

        # 使用线程池并行执行
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            future_entity = executor.submit(entity_search)
            future_topic = executor.submit(topic_search)
            future_vector = executor.submit(vector_search)

            # 等待检索完成
            concurrent.futures.wait([future_entity, future_topic, future_vector], timeout=20)

        ranked_sources = {
            "entity_level": entity_docs,
            "topic_level": topic_docs,
            "vector_enhanced": vector_docs,
        }
        origin_len = sum(len(docs) for docs in ranked_sources.values())
        if audit_run:
            for source_name, stats in branch_stats.items():
                audit_run.append_process(f"Hybrid Branch Status / {source_name}", stats)
            audit_run.append_process(
                "Hybrid Branch Summary",
                {
                    "entity_count": len(entity_docs),
                    "topic_count": len(topic_docs),
                    "vector_count": len(vector_docs),
                    "origin_len": origin_len,
                },
            )
            audit_run.write_documents(
                "Hybrid Retrieval / Entity Branch Raw Results",
                entity_docs,
                "entity_level",
            )
            audit_run.write_documents(
                "Hybrid Retrieval / Topic Branch Raw Results",
                topic_docs,
                "topic_level",
            )
            audit_run.write_documents(
                "Hybrid Retrieval / Vector Branch Raw Results",
                vector_docs,
                "vector_enhanced",
            )
            audit_run.write_documents(
                "Hybrid Retrieval / Branches Before Merge",
                entity_docs + topic_docs + vector_docs,
                "branch_grouped",
            )
        merged_candidates = self._merge_retrieved_documents(ranked_sources)
        if audit_run:
            duplicate_count = max(0, origin_len - len(merged_candidates))
            audit_run.append_process(
                "Hybrid Merge Dedup",
                {
                    "dedupe_key": "node_id -> recipe_name -> hash(page_content[:300])",
                    "before_count": origin_len,
                    "after_count": len(merged_candidates),
                    "duplicate_count": duplicate_count,
                },
            )
            audit_run.write_documents(
                "Hybrid Retrieval / Merged Candidates",
                merged_candidates,
                "merged_candidates",
            )
        rerank_candidates = self._expand_technique_contexts(
            merged_candidates,
            limit=max(top_k + 4, 8),
            audit_run=audit_run,
        )
        final_docs = self._rerank_documents(query, rerank_candidates, top_k, audit_run=audit_run)
        final_docs = self._ensure_technique_expansion_in_final(
            final_docs,
            rerank_candidates,
            top_k,
            audit_run=audit_run,
        )
        if audit_run:
            audit_run.write_documents(
                "Hybrid Retrieval / Top-K Final Retrieval Context",
                final_docs,
                "top_k_final",
            )
            audit_run.append_process(
                "Hybrid Retrieval Complete",
                {
                    "hybrid_total_duration_ms": int((datetime.now() - hybrid_started_at).total_seconds() * 1000),
                    "final_count": len(final_docs),
                },
            )

        logger.info(
            "直接合并+Rerank：实体级%s、主题级%s、向量%s，总候选%s，去重后%s，Rerank候选%s，返回%s个文档",
            len(entity_docs), len(topic_docs), len(vector_docs), origin_len,
            len(merged_candidates), len(rerank_candidates), len(final_docs)
        )
        logger.info(f"混合检索完成，返回 {len(final_docs)} 个文档")
        return final_docs

    def _format_rerank_inputs(self, documents: List[Document]) -> str:
        parts = []
        for index, doc in enumerate(documents):
            parts.extend(
                [
                    f"### pair_order={index}",
                    "source: rerank_input",
                    "",
                    "```text",
                    self._rerank_text(doc),
                    "```",
                    "",
                ]
            )
        return "\n".join(parts) if parts else "_no content_"
        
    def close(self):
        """关闭资源连接"""
        if self.driver:
            self.driver.close()
            logger.info("Neo4j连接已关闭") 
