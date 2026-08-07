"""
智能查询路由器
根据查询特点自动选择最适合的检索策略：
- 传统混合检索：适合简单的信息查找
- 图RAG检索：适合复杂的关系推理和知识发现
"""

import json
import logging
import re
from datetime import datetime
from typing import List, Dict, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum

try:
    from langchain_core.documents import Document
except ImportError:
    class Document:
        def __init__(self, page_content: str = "", metadata: Optional[Dict[str, Any]] = None):
            self.page_content = page_content
            self.metadata = metadata or {}

from rag_modules.rag_audit import query_hash

logger = logging.getLogger(__name__)

class SearchStrategy(Enum):
    """搜索策略枚举"""
    HYBRID_TRADITIONAL = "hybrid_traditional"  # 传统混合检索
    GRAPH_RAG = "graph_rag"  # 图RAG检索
    
@dataclass
class QueryAnalysis:
    """查询分析结果"""
    query_complexity: float  # 查询复杂度 (0-1)
    relationship_intensity: float  # 关系密集度 (0-1)
    reasoning_required: bool  # 是否需要推理
    entity_count: int  # 实体数量
    recommended_strategy: SearchStrategy
    confidence: float  # 推荐置信度
    reasoning: str  # 推荐理由

class IntelligentQueryRouter:
    """
    智能查询路由器
    
    核心能力：
    1. 查询复杂度分析：识别简单查找 vs 复杂推理
    2. 关系密集度评估：判断是否需要图结构优势
    3. 策略自动选择：路由到最适合的检索引擎
    4. 结果质量监控：基于反馈优化路由决策
    """
    
    def __init__(self, 
                 traditional_retrieval,  # 传统混合检索模块
                 graph_rag_retrieval,    # 图RAG检索模块
                 llm_client,
                 config):
        self.traditional_retrieval = traditional_retrieval
        self.graph_rag_retrieval = graph_rag_retrieval
        self.llm_client = llm_client
        self.config = config
        
        # 路由统计
        self.route_stats = {
            "traditional_count": 0,
            "graph_rag_count": 0,
            "total_queries": 0
        }
        
    def analyze_query(self, query: str, audit_run=None) -> QueryAnalysis:
        """
        深度分析查询特征，决定最佳检索策略
        优化：后续完全可以基于这两个分数继续做更细粒度优化，比如高复杂度问题自动增加图遍历深度，高关系密集度问题提高图检索占比
        """
        logger.info(f"分析查询特征: {query}")
        analysis_started_at = datetime.now()
        if audit_run:
            audit_run.append_process(
                "Query Analysis Input",
                {
                    "analysis_input_query_length": len(query or ""),
                    "analysis_input_query_hash": query_hash(query or ""),
                    "llm_model": self.config.llm_model,
                    "temperature": 0.1,
                    "max_tokens": 800,
                },
            )
        
        # 使用LLM进行智能分析
        analysis_prompt = f"""
        作为RAG系统的查询分析专家，请深度分析以下查询的特征：
        
        查询：{query}
        
        请从以下维度分析：
        
        1. 查询复杂度 (0-1)：
           - 0.0-0.3: 简单信息查找（如：红烧肉怎么做？）
           - 0.4-0.7: 中等复杂度（如：川菜有哪些特色菜？）
           - 0.8-1.0: 高复杂度推理（如：为什么川菜用花椒而不是胡椒？）
        
        2. 关系密集度 (0-1)：
           - 0.0-0.3: 单一实体信息（如：西红柿的营养价值）
           - 0.4-0.7: 实体间关系（如：鸡肉配什么蔬菜？）
           - 0.8-1.0: 复杂关系网络（如：川菜的形成与地理、历史的关系）
        
        3. 推理需求：
           - 是否需要多跳推理？
           - 是否需要因果分析？
           - 是否需要对比分析？
        
        4. 实体识别：
           - 查询中包含多少个明确实体？
           - 实体类型是什么？
        
        基于分析推荐检索策略：
        - hybrid_traditional: 适合简单直接的信息查找
        - graph_rag: 适合复杂关系推理和知识发现
        
        注意：当前只允许在 hybrid_traditional 和 graph_rag 两个策略中选择，不要返回 combined。
        
        返回JSON格式：
        {{
            "query_complexity": 0.6,
            "relationship_intensity": 0.8,
            "reasoning_required": true,
            "entity_count": 3,
            "recommended_strategy": "graph_rag",
            "confidence": 0.85,
            "reasoning": "该查询涉及多个实体间的复杂关系，需要图结构推理"
        }}
        """
        
        try:
            response = self.llm_client.chat.completions.create(
                model=self.config.llm_model,
                messages=[{"role": "user", "content": analysis_prompt}],
                temperature=0.1,
                max_tokens=800
            )
            
            result = json.loads(response.choices[0].message.content.strip())
            strategy = self._normalize_strategy(
                result.get("recommended_strategy", "hybrid_traditional"),
                result.get("query_complexity", 0.5),
                result.get("relationship_intensity", 0.5),
                result.get("reasoning_required", False),
                result.get("entity_count", 1),
            )
            
            analysis = QueryAnalysis(
                query_complexity=result.get("query_complexity", 0.5),
                relationship_intensity=result.get("relationship_intensity", 0.5),
                reasoning_required=result.get("reasoning_required", False),
                entity_count=result.get("entity_count", 1),
                recommended_strategy=strategy,
                confidence=result.get("confidence", 0.5),
                reasoning=result.get("reasoning", "默认分析")
            )
            
            logger.info(f"查询分析完成: {analysis.recommended_strategy.value} (置信度: {analysis.confidence:.2f})")
            self._record_query_analysis(
                audit_run,
                analysis,
                analysis_started_at,
                analysis_mode="llm",
            )
            return analysis
            
        except Exception as e:
            logger.error(f"查询分析失败: {e}")
            # 降级方案：基于规则的简单分析
            analysis = self._rule_based_analysis(query)
            if audit_run:
                audit_run.record_error("query_analysis", e, fallback_strategy=analysis.recommended_strategy.value)
            self._record_query_analysis(
                audit_run,
                analysis,
                analysis_started_at,
                analysis_mode="rule_fallback",
            )
            return analysis
    
    # 降级规则优化说明：
    # 1. 修改前的问题：
    #    - 采用“命中词数 / 关键词总数”的归一化方式，分母固定且偏大，导致复杂度和关系分数被压低。
    #    - 只能识别少量关键词，无法利用“配什么”“有什么关系”“从A到B”这类强句式信号。
    #    - entity_count 直接使用 split()，对中文几乎无效，很多查询都会被错误估成 1 个实体。
    # 2. 修改后的思路：
    #    - 改成“关键词 + 句式 + 轻量实体估计 + 图信号”的多特征打分，而不是简单词表归一化。
    #    - 将 fallback 路由分为两档：简单和中等问题走传统混合检索，强关系/强推理问题走 GRAPH_RAG。
    #    - 让 confidence 随规则命中强度变化，而不是固定写死为 0.6。
    # 3. 面试时可背诵：
    #    - 旧版 fallback 规则比较粗糙，容易因为分母过大把本该走图检索的问题压到传统混合检索。
    #    - 我把它升级成了一个轻量、可解释的多特征路由器，在模型不可用时仍能根据句式、关系词、
    #      实体数和图信号做较稳定的策略分流。
    def _rule_based_analysis(self, query: str) -> QueryAnalysis:
        """基于规则的降级分析"""
        # 推理强信号：更偏“为什么/如何/区别/路径/步骤”这类需要解释或流程推导的问题
        complexity_keywords = {
            "strong": ["为什么", "原因", "区别", "比较", "影响", "路径", "流程"],
            "medium": ["如何", "怎么", "步骤", "过程", "关系", "连接", "通过"],
            "graph_hint": ["分类", "菜系", "难度", "相似", "组成", "属于"]
        }

        # 关系强信号：更偏“搭配/联系/从A到B/共同出现”这类实体关系问题
        relation_keywords = {
            "strong": ["搭配", "配什么", "有什么关系", "之间关系", "联系", "相关", "连接"],
            "medium": ["组合", "一起", "共同", "关联", "通过", "从", "到"],
            "graph_hint": ["包含", "需要", "步骤", "下一步", "相似", "同类"]
        }

        complexity_hits = (
            0.35 * self._count_keyword_hits(query, complexity_keywords["strong"]) +
            0.20 * self._count_keyword_hits(query, complexity_keywords["medium"]) +
            0.15 * self._count_keyword_hits(query, complexity_keywords["graph_hint"])
        )
        relation_hits = (
            0.35 * self._count_keyword_hits(query, relation_keywords["strong"]) +
            0.20 * self._count_keyword_hits(query, relation_keywords["medium"]) +
            0.15 * self._count_keyword_hits(query, relation_keywords["graph_hint"])
        )

        reasoning_pattern_score = 0.0
        relation_pattern_score = 0.0

        if re.search(r"为什么|什么原因|区别|比较", query):
            reasoning_pattern_score += 0.35
        if re.search(r"如何|怎么|步骤|流程|过程", query):
            reasoning_pattern_score += 0.25
        if re.search(r"通过什么|从.+到.+", query):
            reasoning_pattern_score += 0.25
            relation_pattern_score += 0.20
        if re.search(r"配什么|搭配什么|和.+有什么关系|与.+有什么关系|之间关系", query):
            relation_pattern_score += 0.40
        if re.search(r"哪些|有哪些|推荐几个", query):
            reasoning_pattern_score += 0.10

        entity_count = self._estimate_entity_count(query)
        multi_entity_bonus = 0.20 if entity_count >= 2 else 0.0
        graph_query_bonus = 0.15 if re.search(r"分类|菜系|难度|相似|路径|步骤", query) else 0.0

        complexity = min(1.0, complexity_hits + reasoning_pattern_score + graph_query_bonus)
        relation_intensity = min(1.0, relation_hits + relation_pattern_score + multi_entity_bonus)
        reasoning_required = complexity >= 0.45 or "为什么" in query or "如何" in query

        if complexity >= 0.60 or relation_intensity >= 0.65:
            strategy = SearchStrategy.GRAPH_RAG
        else:
            strategy = SearchStrategy.HYBRID_TRADITIONAL

        confidence = min(
            0.85,
            0.45 + 0.25 * max(complexity, relation_intensity) + (0.10 if entity_count >= 2 else 0.0)
        )

        reasoning_parts = [
            f"规则命中：复杂度={complexity:.2f}",
            f"关系密集度={relation_intensity:.2f}",
            f"实体数≈{entity_count}",
            f"推荐策略={strategy.value}"
        ]

        return QueryAnalysis(
            query_complexity=complexity,
            relationship_intensity=relation_intensity,
            reasoning_required=reasoning_required,
            entity_count=entity_count,
            recommended_strategy=strategy,
            confidence=confidence,
            reasoning="；".join(reasoning_parts)
        )

    def _normalize_strategy(
        self,
        raw_strategy: str,
        query_complexity: float,
        relationship_intensity: float,
        reasoning_required: bool,
        entity_count: int,
    ) -> SearchStrategy:
        """把LLM返回的策略收敛到当前启用的两种检索方式。"""
        if raw_strategy == SearchStrategy.GRAPH_RAG.value:
            return SearchStrategy.GRAPH_RAG
        if raw_strategy == SearchStrategy.HYBRID_TRADITIONAL.value:
            return SearchStrategy.HYBRID_TRADITIONAL

        # 兼容旧提示或模型惯性返回的 combined：强关系/强推理走图检索，其余走传统混合检索。
        if (
            raw_strategy == "combined"
            and (
                query_complexity >= 0.70
                or relationship_intensity >= 0.70
                or (reasoning_required and entity_count >= 3)
            )
        ):
            return SearchStrategy.GRAPH_RAG

        return SearchStrategy.HYBRID_TRADITIONAL

    def _count_keyword_hits(self, query: str, keywords: List[str]) -> int:
        """统计关键词命中数，作为降级规则的一部分。"""
        return sum(1 for kw in keywords if kw in query)

    def _estimate_entity_count(self, query: str) -> int:
        """轻量估计中文查询中的实体个数，避免直接 split() 造成几乎恒为 1。"""
        cleaned_query = query
        stop_phrases = [
            "有什么关系", "之间关系", "配什么", "搭配什么", "推荐几个", "有哪些", "为什么", "如何", "怎么",
            "步骤", "流程", "过程", "分类", "菜系", "难度", "相似", "通过什么"
        ]
        for phrase in stop_phrases:
            cleaned_query = cleaned_query.replace(phrase, " ")

        parts = re.split(r"[，。！？、,\s]+|和|与|跟|及|配|搭配|联系|相关|连接|通过|从|到", cleaned_query)
        candidates = []
        for part in parts:
            token = part.strip()
            if len(token) < 2:
                continue
            if token not in candidates:
                candidates.append(token)

        if candidates:
            return max(1, min(len(candidates), 5))

        return 1
    
    def route_query(self, query: str, top_k: int = 5, audit_run=None) -> Tuple[List[Document], QueryAnalysis]:
        """
        智能路由查询到最适合的检索引擎
        """
        logger.info(f"开始智能路由: {query}")
        route_started_at = datetime.now()
        
        # 1. 分析查询特征
        analysis = self.analyze_query(query, audit_run=audit_run)
        
        # 2. 更新统计
        stats_before = dict(self.route_stats)
        self._update_route_stats(analysis.recommended_strategy)
        stats_after = dict(self.route_stats)
        if audit_run:
            audit_run.append_process(
                "Routing Decision",
                {
                    "selected_strategy": analysis.recommended_strategy.value,
                    "top_k": top_k,
                    "route_stats_before": stats_before,
                    "route_stats_after": stats_after,
                },
            )
        
        # 3. 根据策略执行检索
        documents = []
        
        try:
            if analysis.recommended_strategy == SearchStrategy.HYBRID_TRADITIONAL:
                logger.info("使用传统混合检索")
                documents = self.traditional_retrieval.hybrid_search(query, top_k, audit_run=audit_run)
                
            elif analysis.recommended_strategy == SearchStrategy.GRAPH_RAG:
                logger.info("🕸️ 使用图RAG检索")
                documents = self.graph_rag_retrieval.graph_rag_search(query, top_k, audit_run=audit_run)
            
            # 4. 结果后处理
            documents = self._post_process_results(documents, analysis)
            if audit_run:
                audit_run.record_event(
                    "route_query",
                    status="completed",
                    start_time=route_started_at,
                    end_time=datetime.now(),
                    selected_strategy=analysis.recommended_strategy.value,
                    document_count=len(documents),
                )
            
            logger.info(f"路由完成，返回 {len(documents)} 个结果")
            return documents, analysis
            
        except Exception as e:
            logger.error(f"查询路由失败: {e}")
            if audit_run:
                audit_run.record_error(
                    "route_query",
                    e,
                    fallback_strategy=SearchStrategy.HYBRID_TRADITIONAL.value,
                )
            # 降级到传统检索
            documents = self.traditional_retrieval.hybrid_search(query, top_k, audit_run=audit_run)
            if audit_run:
                audit_run.record_event(
                    "route_query",
                    status="fallback_completed",
                    start_time=route_started_at,
                    end_time=datetime.now(),
                    selected_strategy=analysis.recommended_strategy.value,
                    fallback_strategy=SearchStrategy.HYBRID_TRADITIONAL.value,
                    document_count=len(documents),
            )
            return documents, analysis
    
    def _post_process_results(self, documents: List[Document], analysis: QueryAnalysis) -> List[Document]:
        """
        结果后处理：根据查询分析优化结果
        """
        for doc in documents:
            # 添加路由信息到元数据
            doc.metadata.update({
                "route_strategy": analysis.recommended_strategy.value,
                "query_complexity": analysis.query_complexity,
                "route_confidence": analysis.confidence
            })
        
        return documents
    
    def _update_route_stats(self, strategy: SearchStrategy):
        """更新路由统计"""
        self.route_stats["total_queries"] += 1
        
        if strategy == SearchStrategy.HYBRID_TRADITIONAL:
            self.route_stats["traditional_count"] += 1
        elif strategy == SearchStrategy.GRAPH_RAG:
            self.route_stats["graph_rag_count"] += 1

    def _record_query_analysis(
        self,
        audit_run,
        analysis: QueryAnalysis,
        started_at: datetime,
        analysis_mode: str,
    ) -> None:
        if not audit_run:
            return
        audit_run.record_event(
            "query_analysis",
            status="completed",
            start_time=started_at,
            end_time=datetime.now(),
            analysis_mode=analysis_mode,
            query_complexity=analysis.query_complexity,
            relationship_intensity=analysis.relationship_intensity,
            reasoning_required=analysis.reasoning_required,
            entity_count=analysis.entity_count,
            strategy=analysis.recommended_strategy.value,
            confidence=analysis.confidence,
            reasoning=analysis.reasoning,
        )
    
    def get_route_statistics(self) -> Dict[str, Any]:
        """获取路由统计信息"""
        total = self.route_stats["total_queries"]
        if total == 0:
            return self.route_stats
        
        return {
            **self.route_stats,
            "traditional_ratio": self.route_stats["traditional_count"] / total,
            "graph_rag_ratio": self.route_stats["graph_rag_count"] / total
        }
    
    def explain_routing_decision(self, query: str) -> str:
        """解释路由决策过程"""
        analysis = self.analyze_query(query)
        
        explanation = f"""
        查询路由分析报告
        
        查询：{query}
        
        特征分析：
        - 复杂度：{analysis.query_complexity:.2f} ({'简单' if analysis.query_complexity < 0.4 else '中等' if analysis.query_complexity < 0.8 else '复杂'})
        - 关系密集度：{analysis.relationship_intensity:.2f} ({'单一实体' if analysis.relationship_intensity < 0.4 else '实体关系' if analysis.relationship_intensity < 0.8 else '复杂关系网络'})
        - 推理需求：{'是' if analysis.reasoning_required else '否'}
        - 实体数量：{analysis.entity_count}
        
        推荐策略：{analysis.recommended_strategy.value}
        置信度：{analysis.confidence:.2f}
        
        决策理由：{analysis.reasoning}
        """
        
        return explanation

 
