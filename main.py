"""
基于图RAG的智能烹饪助手 - 主程序
整合传统检索和图RAG检索，实现真正的图数据优势
"""

import os
import sys
import time
import logging
import hashlib
from datetime import datetime
from typing import List, Optional

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
# 加载环境变量
# 需要在加载GraphRAGConfig执行调用load_dotenv()
load_dotenv()

from config import DEFAULT_CONFIG, GraphRAGConfig
from rag_modules import (
    GraphDataPreparationModule,
    MilvusIndexConstructionModule, 
    GenerationIntegrationModule
)
from rag_modules.hybrid_retrieval import HybridRetrievalModule
from rag_modules.graph_rag_retrieval import GraphRAGRetrieval
from rag_modules.intelligent_query_router import IntelligentQueryRouter, QueryAnalysis
from rag_modules.session_cache_manager import SessionCacheManager
from rag_modules.web_service_handler import WebServiceHandler
from rag_modules.recipe_recommendation import RecipeRecommendationManager
from rag_modules.parent_document_store import ParentDocumentStore
from rag_modules.entity_resolver import EntityResolver
from rag_modules.entity_direct_retrieval import EntityDirectRetriever
from rag_modules.rag_audit import RAGAuditManager
from rag_modules.retrieval_contracts import EntityCandidate, EvidenceBundle
from rag_modules.nutrition_policy import SOFT_PREFERENCE_POLICY
from rag_modules.recommendation_evidence import RecommendationEvidence
from rag_modules.evidence_builder import EvidenceBuilder
from rag_modules.query_plan import QueryPlan
from rag_modules.query_plan_validator import QueryPlanValidator
from rag_modules.targeted_graph_retrieval import TargetedGraphRetriever
from rag_modules.milvus_v2_index import (
    ArtifactMismatchError,
    MilvusV2Schema,
    RetrievalArtifactManifest,
    create_milvus_client,
    pds_manifest_sha256,
)
from rag_modules.restricted_vector_retrieval import RestrictedVectorRetriever
from rag_modules.intent_candidate import IntentCandidate
from rag_modules.intent_planner import IntentPlanner
from rag_modules.intent_plan_compiler import CompileResult, IntentPlanCompiler
from rag_modules.preference_reranker import PreferenceReranker
from rag_modules.recommendation_constraints import RecommendationConstraintCompiler, ResolvedCandidateScope
from rag_modules.nutrition_policy import SOFT_PREFERENCE_POLICY


_GENERIC_PREFERENCE_MENTIONS = frozenset({"蔬菜", "豆制品", "面食", "鱼", "海鲜", "肉菜", "素菜"})
_MAX_FILTER_PARENTS_PER_SEARCH = 20


class AdvancedGraphRAGSystem:
    """
    图RAG系统
    
    核心特性：
    1. 智能路由：自动选择最适合的检索策略
    2. 双引擎检索：传统混合检索 + 图RAG检索
    3. 图结构推理：多跳遍历、子图提取、关系推理
    4. 查询复杂度分析：深度理解用户意图
    5. 自适应学习：基于反馈优化系统性能
    """
    
    def __init__(self, config: Optional[GraphRAGConfig] = None):
        self.config = config or DEFAULT_CONFIG
        
        # 核心模块
        self.data_module = None
        self.index_module = None
        self.generation_module = None
        
        # 检索引擎
        self.traditional_retrieval = None
        self.graph_rag_retrieval = None
        self.query_router = None
        
        # 系统状态
        self.system_ready = False

        # 会话缓存管理器
        self.cache_manager = None
        # 阶段 1 PDS：只做可选健康检查，不接入旧 Router
        self.parent_document_store = None
        # 阶段 2：默认关闭的实体直达组件；开启失败时保留旧 Router。
        self.entity_resolver = None
        self.entity_direct_retriever = None
        # 阶段 3：默认关闭的 QueryPlan 与固定图查询组件。
        self.query_plan_validator = None
        self.targeted_graph_retriever = None
        # 阶段 4：V2 只读受限 child chunk 检索，必须绑定联合 artifact。
        self.restricted_vector_retriever = None
        self._restricted_vector_init_status = None
        self.intent_planner = None
        self.intent_plan_compiler = None
        self.recommendation_constraint_compiler = RecommendationConstraintCompiler()
        self.preference_reranker = PreferenceReranker()
        
    def initialize_system(self):
        """初始化高级图RAG系统"""
        logger.info("启动高级图RAG系统...")
        
        try:
            # 1. 数据准备模块
            print("初始化数据准备模块...")
            self.data_module = GraphDataPreparationModule(
                uri=self.config.neo4j_uri,
                user=self.config.neo4j_user,
                password=self.config.neo4j_password,
                database=self.config.neo4j_database
            )
            
            # 2. 向量索引模块
            print("初始化Milvus向量索引...")
            self.index_module = MilvusIndexConstructionModule(
                host=self.config.milvus_host,
                port=self.config.milvus_port,
                collection_name=self.config.milvus_collection_name,
                dimension=self.config.milvus_dimension,
                model_name=self.config.embedding_model
            )
            
            # 3. 生成模块
            print("初始化生成模块...")
            self.generation_module = GenerationIntegrationModule(
                model_name=self.config.llm_model,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            
            # 4. 传统混合检索模块
            print("初始化传统混合检索...")
            self.traditional_retrieval = HybridRetrievalModule(
                config=self.config,
                milvus_module=self.index_module,
                data_module=self.data_module,
                llm_client=self.generation_module.client
            )
            
            # 5. 图RAG检索模块
            print("初始化图RAG检索引擎...")
            self.graph_rag_retrieval = GraphRAGRetrieval(
                config=self.config,
                llm_client=self.generation_module.client
            )
            
            # 6. 智能查询路由器
            print("初始化智能查询路由器...")
            self.query_router = IntelligentQueryRouter(
                traditional_retrieval=self.traditional_retrieval,
                graph_rag_retrieval=self.graph_rag_retrieval,
                llm_client=self.generation_module.client,
                config=self.config
            )

            # 7. 会话缓存管理器
            print("初始化会话缓存管理器...")
            self.cache_manager = SessionCacheManager(
                embedding_model=self.index_module.embeddings
            )

            # 8. 菜谱推荐管理器
            print("初始化菜谱推荐管理器...")
            self.recipe_manager = RecipeRecommendationManager()

            if self.config.retrieval_parent_store_enabled:
                print("检查 ParentDocumentStore...")
                try:
                    self.parent_document_store = ParentDocumentStore.open(
                        self.config.parent_store_path,
                        active_pointer=self.config.parent_store_active_pointer,
                    )
                    logger.info("ParentDocumentStore 健康检查: %s", self.parent_document_store.health_check())
                except Exception:
                    if not self.config.retrieval_entity_direct_enabled:
                        raise
                    logger.exception("ParentDocumentStore 不可用，实体直达将保持关闭并回退旧 Router")

            if self.config.retrieval_entity_direct_enabled:
                if not self.config.retrieval_parent_store_enabled or self.parent_document_store is None:
                    logger.warning(
                        "RETRIEVAL_ENTITY_DIRECT_ENABLED 依赖 RETRIEVAL_PARENT_STORE_ENABLED 与健康 PDS；本次不启用实体直达"
                    )
                else:
                    self.entity_resolver = EntityResolver(
                        self.data_module.driver,
                        database=self.config.neo4j_database,
                    )
                    self.entity_direct_retriever = EntityDirectRetriever(
                        self.parent_document_store,
                        self.data_module.driver,
                        database=self.config.neo4j_database,
                    )
                    logger.info("阶段 2 实体直达已启用；旧 Router 仍作为 PDS 故障回退")

            if self.config.retrieval_query_plan_enabled or self.config.retrieval_milvus_v2_enabled:
                self.query_plan_validator = QueryPlanValidator()
                if self.data_module is not None:
                    self.entity_resolver = self.entity_resolver or EntityResolver(
                        self.data_module.driver,
                        database=self.config.neo4j_database,
                    )
                    if self.config.retrieval_targeted_graph_enabled:
                        self.targeted_graph_retriever = TargetedGraphRetriever(
                            self.data_module.driver,
                            database=self.config.neo4j_database,
                            validator=self.query_plan_validator,
                        )
                        logger.info("阶段 3 QueryPlan 与目标化图查询已启用")

            if self.config.retrieval_milvus_v2_enabled:
                self._initialize_restricted_vector_retriever()

            if getattr(self.config, "retrieval_intent_planner_enabled", False):
                self.intent_planner = IntentPlanner(
                    self.generation_module.client,
                    model=self.config.llm_model,
                    timeout_seconds=getattr(self.config, "retrieval_intent_planner_timeout_seconds", 30.0),
                )
                self.intent_plan_compiler = IntentPlanCompiler(
                    self.query_plan_validator,
                    recommendation_scope_max=self._recommendation_scope_limit(),
                )
                logger.info("意图规划器已启用：新路径失败将 fail-closed")

            # 9. Web服务处理器
            print("初始化Web服务处理器...")
            self.web_handler = WebServiceHandler(self)

            print("✅ 高级图RAG系统初始化完成！")
            
        except Exception as e:
            logger.error(f"系统初始化失败: {e}")
            raise
    
    def build_knowledge_base(self):
        """构建知识库（如果需要）"""
        print("\n检查知识库状态...")
        
        try:
            # 检查Milvus集合是否存在
            if self.index_module.has_collection():
                print("✅ 发现已存在的知识库，尝试加载...")
                if self.index_module.load_collection():
                    print("知识库加载成功！")
                    
                    # 重要：即使从已存在的知识库加载，也需要加载图数据以支持图索引
                    print("加载图数据以支持图检索...")
                    self.data_module.load_graph_data()
                    print("构建菜谱文档...")
                    self.data_module.build_recipe_documents()
                    print("构建技巧/知识文档...")
                    self.data_module.build_technique_documents()
                    print("进行文档分块...")
                    chunks = self.data_module.chunk_documents(
                        chunk_size=self.config.chunk_size,
                        chunk_overlap=self.config.chunk_overlap
                    )
                    
                    self._initialize_retrievers(chunks)
                    return
                else:
                    print("❌ 知识库加载失败，开始重建...")
            
            print("未找到已存在的集合，开始构建新的知识库...")
            
            # 从Neo4j加载图数据
            print("从Neo4j加载图数据...")
            self.data_module.load_graph_data()
            
            # 构建菜谱文档
            print("构建菜谱文档...")
            self.data_module.build_recipe_documents()

            # 构建技巧/知识文档
            print("构建技巧/知识文档...")
            self.data_module.build_technique_documents()
            
            # 进行文档分块
            print("进行文档分块...")
            chunks = self.data_module.chunk_documents(
                chunk_size=self.config.chunk_size,
                chunk_overlap=self.config.chunk_overlap
            )
            
            # 构建Milvus向量索引
            print("构建Milvus向量索引...")
            if not self.index_module.build_vector_index(chunks):
                raise Exception("构建向量索引失败")
            
            # 初始化检索器
            self._initialize_retrievers(chunks)
            
            # 显示统计信息
            self._show_knowledge_base_stats()
            
            print("✅ 知识库构建完成！")
            
        except Exception as e:
            logger.error(f"知识库构建失败: {e}")
            raise
    
    def _initialize_retrievers(self, chunks: List = None):
        """初始化检索器"""
        print("初始化检索引擎...")
        
        # 如果没有chunks，从数据模块获取
        if chunks is None:
            chunks = self.data_module.chunks or []
        
        # 初始化传统检索器
        self.traditional_retrieval.initialize(chunks)
        
        # 初始化图RAG检索器
        self.graph_rag_retrieval.initialize()
        
        self.system_ready = True
        print("✅ 检索引擎初始化完成！")
    
    def _show_knowledge_base_stats(self):
        """显示知识库统计信息"""
        print(f"\n知识库统计:")
        
        # 数据统计
        stats = self.data_module.get_statistics()
        print(f"   菜谱数量: {stats.get('total_recipes', 0)}")
        print(f"   食材数量: {stats.get('total_ingredients', 0)}")
        print(f"   烹饪步骤: {stats.get('total_cooking_steps', 0)}")
        print(f"   技巧文档: {stats.get('total_technique_docs', 0)}")
        print(f"   技巧文档块: {stats.get('total_technique_chunks', 0)}")
        print(f"   文档数量: {stats.get('total_documents', 0)}")
        print(f"   文本块数: {stats.get('total_chunks', 0)}")
        
        # Milvus统计
        milvus_stats = self.index_module.get_collection_stats()
        print(f"   向量索引: {milvus_stats.get('row_count', 0)} 条记录")
        
        # 图RAG统计
        route_stats = self.query_router.get_route_statistics()
        print(f"   路由统计: 总查询 {route_stats.get('total_queries', 0)} 次")
        
        if stats.get('categories'):
            categories = list(stats['categories'].keys())[:10]
            print(f"   🏷️ 主要分类: {', '.join(categories)}")
    
    def ask_question_with_routing(
        self,
        question: str,
        stream: bool = False,
        explain_routing: bool = False,
        allow_generalized_advice: bool = False,
        rollout_key: str | None = None,
        audit_run=None,
    ):
        """
        智能问答：自动选择最佳检索策略
        """
        if not self.system_ready:
            raise ValueError("系统未就绪，请先构建知识库")
            
        print(f"\n❓ 用户问题: {question}")
        
        # 显示路由决策解释（可选）
        if explain_routing:
            explanation = self.query_router.explain_routing_decision(question)
            print(explanation)
        
        start_time = time.time()
        if audit_run is None:
            audit_run = RAGAuditManager.from_config(self.config).create_run()
        audit_run.mark_request_start()
        
        try:
            # 1. 智能路由检索
            print("执行智能查询路由...")
            relevant_docs, analysis = self.retrieve_for_generation(
                question,
                self.config.top_k,
                audit_run=audit_run,
                allow_generalized_advice=allow_generalized_advice,
                rollout_key=rollout_key,
            )
            
            # 2. 显示路由信息
            strategy_icons = {
                "hybrid_traditional": "🔍",
                "graph_rag": "🕸️", 
                "combined": "🔄"
            }
            if analysis is not None:
                strategy_icon = strategy_icons.get(analysis.recommended_strategy.value, "❓")
                print(f"{strategy_icon} 使用策略: {analysis.recommended_strategy.value}")
                print(f"📊 复杂度: {analysis.query_complexity:.2f}, 关系密集度: {analysis.relationship_intensity:.2f}")
            else:
                print("🎯 使用阶段 2 实体直达证据链")
            
            # 3. 显示检索结果信息
            if isinstance(relevant_docs, EvidenceBundle):
                print(
                    f"📋 实体直达：图事实 {len(relevant_docs.graph_facts)} 条，"
                    f"正文证据 {len(relevant_docs.text_evidence)} 条"
                )
            elif relevant_docs:
                doc_info = []
                for doc in relevant_docs:
                    recipe_name = doc.metadata.get('recipe_name', '未知内容')
                    search_type = doc.metadata.get('search_type', doc.metadata.get('route_strategy', 'unknown'))
                    score = doc.metadata.get('final_score', doc.metadata.get('relevance_score', 0))
                    doc_info.append(f"{recipe_name}({search_type}, {score:.3f})")
                
                print(f"📋 找到 {len(relevant_docs)} 个相关文档: {', '.join(doc_info[:3])}")
                if len(doc_info) > 3:
                    print(f"    等 {len(relevant_docs)} 个结果...")
            else:
                return "抱歉，没有找到相关的烹饪信息。请尝试其他问题。"

            if (
                bool(getattr(self.config, "retrieval_intent_planner_enabled", False))
                and isinstance(relevant_docs, EvidenceBundle)
                and "INTENT_NON_EXECUTE" in relevant_docs.limitations
            ):
                result = self._intent_terminal_response(relevant_docs)
                audit_run.append_process(
                    "Final Output",
                    {
                        "answer_chars": len(result),
                        "answer_hash": hashlib.sha256(result.encode("utf-8")).hexdigest(),
                        "success": True,
                        "final_source": "compile_terminal",
                    },
                )
                audit_run.finish_request(success=True, final_source="compile_terminal")
                return result, analysis
            
            # 4. 生成回答
            print("🎯 智能生成回答...")
            
            if stream:
                try:
                    for chunk_text in self.generation_module.generate_adaptive_answer_stream(
                        question,
                        relevant_docs,
                        audit_run=audit_run,
                    ):
                        print(chunk_text, end="", flush=True)
                    print("\n")
                    result = "流式输出完成"
                except Exception as stream_error:
                    logger.error(f"流式输出过程中出现错误: {stream_error}")
                    print(f"\n⚠️ 流式输出中断，切换到标准模式...")
                    # 使用非流式作为后备
                    result = self.generation_module.generate_adaptive_answer(
                        question,
                        relevant_docs,
                        audit_run=audit_run,
                    )
            else:
                result = self.generation_module.generate_adaptive_answer(
                    question,
                    relevant_docs,
                    audit_run=audit_run,
                )
            
            # 5. 性能统计
            end_time = time.time()
            print(f"\n⏱️ 问答完成，耗时: {end_time - start_time:.2f}秒")
            audit_run.finish_request(
                success=True,
                final_source="entity_direct" if isinstance(relevant_docs, EvidenceBundle) else "generation",
            )
            
            return result, analysis
            
        except Exception as e:
            logger.error(f"问答处理失败: {e}")
            audit_run.record_error("cli_request", e)
            audit_run.finish_request(success=False, final_source="error")
            return f"抱歉，处理问题时出现错误：{str(e)}", None

    def retrieve_for_generation(
        self,
        query: str,
        top_k: int,
        audit_run=None,
        *,
        allow_generalized_advice: bool = False,
        rollout_key: str | None = None,
    ):
        """优先尝试默认关闭的实体直达；任何不安全状态均保留旧 Router。"""
        planner_enabled = bool(getattr(getattr(self, "config", None), "retrieval_intent_planner_enabled", False))
        if planner_enabled:
            rollout_stage = self._new_path_rollout_stage(query, rollout_key=rollout_key)
            if rollout_stage is None:
                if audit_run is not None and hasattr(audit_run, "record_event"):
                    audit_run.record_event("retrieval_rollout", status="legacy", reason="planner_not_selected")
                return self._legacy_fallback_or_decline(query, top_k, audit_run=audit_run)
            return self._retrieve_with_intent_planner(query, top_k, audit_run=audit_run)

        nutrition_bundle = self._try_nutrition_recommendation(query, top_k, audit_run=audit_run)
        if nutrition_bundle is not None:
            return nutrition_bundle, None
        rollout_stage = self._new_path_rollout_stage(query, rollout_key=rollout_key)
        if rollout_stage is None:
            if audit_run is not None and hasattr(audit_run, "record_event"):
                audit_run.record_event("retrieval_rollout", status="legacy", reason="not_selected")
            return self._legacy_fallback_or_decline(query, top_k, audit_run=audit_run)
        targeted_bundle = self._try_targeted_graph(query, audit_run=audit_run)
        if targeted_bundle is not None:
            self._audit_targeted_graph(audit_run, targeted_bundle)
            return targeted_bundle, None
        preference_plan = self._preference_plan(query, top_k)
        if preference_plan is not None and getattr(self.config, "retrieval_milvus_v2_enabled", False):
            preference_bundle = self._try_restricted_vector(
                query,
                top_k,
                preference_plan,
                audit_run=audit_run,
            )
            if preference_bundle is not None:
                return preference_bundle, None
        bundle = self._try_entity_direct(
            query,
            audit_run=audit_run,
            allow_generalized_advice=allow_generalized_advice,
        )
        if bundle is not None:
            if bundle.requires_legacy_fallback:
                self._audit_entity_direct(audit_run, "fallback", bundle)
            else:
                self._audit_entity_direct(audit_run, "selected", bundle)
                return bundle, None
        return self._legacy_fallback_or_decline(query, top_k, audit_run=audit_run)

    def _retrieve_with_intent_planner(self, user_message: str, top_k: int, *, audit_run=None):
        """planner 开启时唯一的新路径入口；所有失败均不触发旧 Router。"""
        # 只使用可信用户文本进行高风险预检。否定表达和评测约束不会传到此处。
        if self._is_strict_nutrition_or_medical_request(user_message):
            result = CompileResult(
                "TERMINAL",
                "NUTRITION_EVIDENCE_INSUFFICIENT",
                reason="NUTRITION_EVIDENCE_INSUFFICIENT",
                limitations=("NUTRITION_EVIDENCE_INSUFFICIENT",),
            )
            self._audit_compile_result(audit_run, result)
            return self._compile_result_bundle(result), None
        planner = getattr(self, "intent_planner", None)
        compiler = getattr(self, "intent_plan_compiler", None)
        if planner is None or compiler is None:
            return self._compile_result_bundle(CompileResult("UNAVAILABLE", "PLANNER_UNAVAILABLE", reason="PLANNER_NOT_INITIALIZED")), None
        planner_result = planner.plan(user_message, audit_run=audit_run)
        if not planner_result.executable:
            status = "UNAVAILABLE" if planner_result.status == "PLANNER_UNAVAILABLE" else "CLARIFY"
            return self._compile_result_bundle(CompileResult(status, planner_result.status, reason=planner_result.reason)), None
        candidate = self._reconcile_explicit_recipe_detail(user_message, planner_result.candidate, audit_run=audit_run)
        if candidate.intent == "PREFERENCE_RECOMMEND":
            if getattr(self.config, "retrieval_recommendation_constraints_enabled", False):
                return self._retrieve_with_recommendation_constraints(user_message, top_k, candidate, compiler, audit_run=audit_run)
            scoped_recipe_ids, scope_result = self._planner_preference_scope(candidate, audit_run=audit_run)
            if scope_result is not None:
                self._audit_compile_result(audit_run, scope_result)
                return self._compile_result_bundle(scope_result), None
            result = compiler.compile(
                candidate,
                scoped_recipe_ids=scoped_recipe_ids,
                dependencies_available=self._planner_dependencies_available(),
            )
            return self._execute_compile_result(user_message, top_k, result, audit_run=audit_run)
        resolved = self._resolve_candidate_entities(candidate, user_message=user_message)
        result = compiler.compile(candidate, resolved_entities=resolved, dependencies_available=self._planner_dependencies_available())
        return self._execute_compile_result(user_message, top_k, result, audit_run=audit_run, resolved_entities=resolved)

    def _retrieve_with_recommendation_constraints(self, user_message, top_k, candidate, compiler, *, audit_run=None):
        """新推荐路径：本地约束 -> metadata 硬范围 -> Top30 -> Top5 正文。"""
        constraint_compiler = getattr(self, "recommendation_constraint_compiler", None) or RecommendationConstraintCompiler()
        ingredient_ids, ingredient_result = self._verified_preference_ingredient_ids(candidate)
        if ingredient_result is not None:
            self._audit_compile_result(audit_run, ingredient_result)
            return self._compile_result_bundle(ingredient_result), None
        spec = constraint_compiler.compile(user_message, candidate, verified_ingredient_ids=ingredient_ids)
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event("recommendation_constraints", status="clarify" if spec.clarification_reason else "compiled", decisions=list(spec.decisions), clarification_reason=spec.clarification_reason)
        if spec.clarification_reason:
            return self._compile_result_bundle(CompileResult("CLARIFY", "RECOMMENDATION_CONSTRAINT_CLARIFY", reason=spec.clarification_reason)), None
        scoped_recipe_ids, scope_result = self._planner_preference_scope(candidate, audit_run=audit_run)
        if scope_result is not None:
            self._audit_compile_result(audit_run, scope_result)
            return self._compile_result_bundle(scope_result), None
        scope, scope_result = self._resolve_recommendation_scope(spec, scoped_recipe_ids)
        if scope_result is not None:
            self._audit_compile_result(audit_run, scope_result)
            return self._compile_result_bundle(scope_result), None
        result = compiler.compile(
            candidate,
            scoped_recipe_ids=scope.parent_ids if scope is not None else scoped_recipe_ids,
            dependencies_available=self._planner_dependencies_available(),
        )
        return self._execute_compile_result(user_message, top_k, result, audit_run=audit_run, constraint_spec=spec)

    def _verified_preference_ingredient_ids(self, candidate):
        """具名食材只有唯一 EntityResolver 结果才进入本地 ConstraintSpec。"""
        mentions = [mention.text for mention in candidate.entity_mentions]
        mentions.extend(value for value in candidate.slots.ingredients if value not in mentions)
        mentions = [value for value in mentions if value.strip() not in _GENERIC_PREFERENCE_MENTIONS]
        if not mentions:
            return (), None
        resolver = getattr(self, "entity_resolver", None)
        if resolver is None:
            return (), CompileResult("UNAVAILABLE", "ENTITY_RESOLVER_UNAVAILABLE", reason="ENTITY_RESOLVER_UNAVAILABLE")
        ids: list[str] = []
        for mention in mentions:
            try:
                entities = tuple(resolver.resolve(mention, expected_types=("Ingredient",)))
            except Exception:
                return (), CompileResult("UNAVAILABLE", "ENTITY_RESOLVER_UNAVAILABLE", reason="ENTITY_RESOLVER_UNAVAILABLE")
            if not entities:
                return (), CompileResult("TERMINAL", "ENTITY_NOT_FOUND", reason="INGREDIENT_NOT_FOUND")
            if len(entities) != 1 or entities[0].ambiguity:
                return (), CompileResult("CLARIFY", "ENTITY_AMBIGUOUS", reason="INGREDIENT_AMBIGUOUS")
            ids.append(entities[0].node_id)
        return tuple(dict.fromkeys(ids)), None

    @staticmethod
    def _is_strict_nutrition_or_medical_request(user_message: str) -> bool:
        text = (user_message or "").strip()
        negative = ("不要求低脂", "不要低脂", "不要说低脂", "不需低脂", "无需低脂")
        if any(marker in text for marker in negative):
            return False
        decision = SOFT_PREFERENCE_POLICY.assess(text)
        if decision is not None and decision.requires_evidence_insufficient:
            return True
        return "低脂" in text and any(marker in text for marker in ("推荐", "适合", "吃什么", "菜"))

    def _planner_dependencies_available(self) -> bool:
        return getattr(self, "query_plan_validator", None) is not None

    def _reconcile_explicit_recipe_detail(self, user_message: str, candidate: IntentCandidate, *, audit_run=None) -> IntentCandidate:
        """用唯一的本地菜谱命中纠正与明确菜名冲突的低权限意图。"""
        if candidate.intent in {"RECIPE_DETAIL", "RECIPE_STEP", "TECHNIQUE_SECTION", "STRICT_NUTRITION", "CLARIFY_OR_OUT_OF_SCOPE"}:
            return candidate
        resolver = getattr(self, "entity_resolver", None)
        if resolver is None:
            return candidate
        try:
            recipes = tuple(resolver.resolve(user_message, expected_types=("Recipe",)))
        except Exception:
            return candidate
        if len(recipes) != 1 or recipes[0].ambiguity:
            return candidate
        recipe = recipes[0]
        if not recipe.display_name or recipe.display_name not in user_message:
            return candidate
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event(
                "planner_local_reconciliation",
                status="recipe_detail_exact_name",
                previous_intent=candidate.intent,
                entity_type="Recipe",
                entity_id=recipe.node_id,
            )
        return IntentCandidate(
            intent="RECIPE_DETAIL",
            confidence=candidate.confidence,
            entity_mentions=[{"text": recipe.display_name}],
            slots=candidate.slots,
        )

    def _resolve_candidate_entities(self, candidate, *, user_message: str | None = None):
        expected = IntentPlanCompiler._EXPECTED_TYPES.get(candidate.intent, ())
        if not expected or getattr(self, "entity_resolver", None) is None:
            return ()
        mentions = [mention.text for mention in candidate.entity_mentions]
        if candidate.intent in {"INGREDIENT_RECIPES", "INGREDIENT_VEGETABLE_PAIRS"}:
            mentions.extend(value for value in candidate.slots.ingredients if value not in mentions)
        if candidate.intent == "INGREDIENT_VEGETABLE_PAIRS":
            # 模板的第二端点是固定、已校验的“蔬菜”类别，不是待解析的命名实体。
            mentions = [mention for mention in mentions if mention.strip() != "蔬菜"]
            # 模型遗漏唯一食材时，最多以用户原句进行一次本地同类型解析；
            # 多候选、缺失或任何解析异常仍然走澄清，绝不猜测实体。
            if not mentions and user_message:
                mentions = [user_message]
        if not mentions:
            return ()
        try:
            resolved = []
            for mention in mentions:
                candidates = tuple(self.entity_resolver.resolve(mention, expected_types=expected))
                # 关系问题中的每一项都是必须核验的对象。缺少任何一项时，不能
                # 忽略它并用其余对象发起一个不等价的图查询。
                if not candidates:
                    return ()
                resolved.extend(candidates)
            return tuple(resolved)
        except Exception:
            return ()

    def _planner_preference_scope(self, candidate, *, audit_run=None):
        """将菜系/食材转换为 verified Recipe 范围，绝不从软偏好猜测范围。"""
        has_cuisine_scope = "SICHUAN_STYLE" in candidate.slots.cuisines
        mentions = [mention.text for mention in candidate.entity_mentions]
        mentions.extend(value for value in candidate.slots.ingredients if value not in mentions)
        generic_mentions = tuple(mention for mention in mentions if mention.strip() in _GENERIC_PREFERENCE_MENTIONS)
        mentions = [mention for mention in mentions if mention.strip() not in _GENERIC_PREFERENCE_MENTIONS]
        if generic_mentions and audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event(
                "planner_preference_scope",
                status="generic_mentions_soft_preference",
                generic_mention_count=len(generic_mentions),
                generic_mention_hash=hashlib.sha256("\n".join(generic_mentions).encode("utf-8")).hexdigest(),
            )
        if not has_cuisine_scope and not mentions:
            return None, None
        if getattr(self, "targeted_graph_retriever", None) is None or getattr(self, "entity_resolver", None) is None:
            return None, CompileResult("UNAVAILABLE", "GRAPH_UNAVAILABLE", reason="GRAPH_UNAVAILABLE")
        scopes: list[set[str]] = []
        if has_cuisine_scope:
            candidate_ids = self._all_pds_parent_ids_by_cuisine("川菜")
            if not candidate_ids:
                return None, CompileResult("TERMINAL", "CUISINE_SCOPE_NOT_FOUND", reason="CUISINE_SCOPE_NOT_FOUND")
            scope_limit = self._recommendation_scope_limit()
            if len(candidate_ids) > scope_limit:
                return None, CompileResult("TERMINAL", "SCOPE_TOO_LARGE", reason="CUISINE_SCOPE_TOO_LARGE")
            plan = self.query_plan_validator.validate(QueryPlan(
                "RECIPE_CUISINE_FILTER", "recipe_cuisine_filter_v1", "Recipe",
                {"recipe_ids": candidate_ids, "cuisine_type": "川菜", "limit": len(candidate_ids)},
                max_candidates=len(candidate_ids), source="rule",
            ))
            fact = self.targeted_graph_retriever.retrieve(plan, audit_run=audit_run)
            if fact.status == "unavailable":
                return None, CompileResult("UNAVAILABLE", "GRAPH_UNAVAILABLE", reason="CUISINE_GRAPH_UNAVAILABLE")
            cuisine_ids = {str(row.get("recipe_id") or "") for row in fact.properties.get("rows", []) if row.get("recipe_id")}
            if not cuisine_ids:
                return None, CompileResult("TERMINAL", "CUISINE_SCOPE_NOT_FOUND", reason="CUISINE_SCOPE_NOT_FOUND")
            scopes.append(cuisine_ids)
        for mention in mentions:
            try:
                entities = tuple(self.entity_resolver.resolve(mention, expected_types=("Ingredient",)))
            except Exception:
                return None, CompileResult("UNAVAILABLE", "GRAPH_UNAVAILABLE", reason="ENTITY_RESOLVER_UNAVAILABLE")
            if not entities:
                return None, CompileResult("TERMINAL", "ENTITY_NOT_FOUND", reason="INGREDIENT_NOT_FOUND")
            if len(entities) != 1 or entities[0].ambiguity:
                return None, CompileResult("CLARIFY", "ENTITY_AMBIGUOUS", reason="INGREDIENT_AMBIGUOUS")
            plan = self.query_plan_validator.validate(QueryPlan(
                "INGREDIENT_RECIPES", "ingredient_recipes_v1", "Ingredient",
                {"ingredient_id": entities[0].node_id, "limit": self._recommendation_scope_limit()},
                max_candidates=self._recommendation_scope_limit(), source="rule",
            ))
            fact = self.targeted_graph_retriever.retrieve(plan, audit_run=audit_run)
            if fact.status == "unavailable":
                return None, CompileResult("UNAVAILABLE", "GRAPH_UNAVAILABLE", reason="INGREDIENT_GRAPH_UNAVAILABLE")
            rows = fact.properties.get("rows", [])
            if len(rows) >= self._recommendation_scope_limit():
                return None, CompileResult("TERMINAL", "SCOPE_TOO_LARGE", reason="INGREDIENT_SCOPE_TOO_LARGE")
            ids = {str(row.get("recipe_id") or "") for row in rows if row.get("recipe_id")}
            if not ids:
                return None, CompileResult("TERMINAL", "NO_PREFERENCE_RESULTS", reason="INGREDIENT_SCOPE_EMPTY")
            scopes.append(ids)
        combined = set.intersection(*scopes) if scopes else set()
        if not combined:
            return None, CompileResult("TERMINAL", "NO_PREFERENCE_RESULTS", reason="HARD_SCOPE_EMPTY")
        if len(combined) > self._recommendation_scope_limit():
            return None, CompileResult("TERMINAL", "SCOPE_TOO_LARGE", reason="HARD_SCOPE_TOO_LARGE")
        return sorted(combined), None

    def _recommendation_scope_limit(self) -> int:
        configured = getattr(getattr(self, "config", None), "retrieval_recommendation_max_hard_scope", QueryPlanValidator.MAX_RECOMMENDATION_SCOPE)
        try:
            return max(1, min(int(configured), QueryPlanValidator.MAX_RECOMMENDATION_SCOPE))
        except (TypeError, ValueError):
            return QueryPlanValidator.MAX_RECOMMENDATION_SCOPE

    def _resolve_recommendation_scope(self, spec, base_parent_ids, *, audit_run=None):
        """在活动 PDS metadata 上计算硬条件交集，完全不读取 Markdown 正文。"""
        hard = spec.hard_filters
        requires_scope = bool(
            base_parent_ids is not None or hard.methods or hard.excluded_methods
            or hard.required_cooking_appliances or hard.excluded_cooking_appliances
            or hard.exclusive_cooking_appliances or hard.max_total_minutes is not None
        )
        if not requires_scope:
            return None, None
        store = getattr(self, "parent_document_store", None)
        build_id = getattr(store, "active_build_id", None)
        if store is None or not build_id or not hasattr(store, "iter_recipe_metadata"):
            return None, CompileResult("UNAVAILABLE", "PDS_METADATA_UNAVAILABLE", reason="PDS_METADATA_UNAVAILABLE")
        rows = list(store.iter_recipe_metadata(build_id=build_id, parent_ids=base_parent_ids))
        counts: dict[str, int] = {"initial": len(rows)}

        def apply(name, predicate):
            nonlocal rows
            rows = [row for row in rows if predicate(row.metadata)]
            counts[name] = len(rows)

        if hard.methods:
            apply("methods", lambda meta: set(hard.methods) <= set(meta.get("recipe_methods") or ()))
        if hard.excluded_methods:
            apply("excluded_methods", lambda meta: not (set(hard.excluded_methods) & set(meta.get("recipe_methods") or ())))
        if hard.required_cooking_appliances:
            apply("required_cooking_appliances", lambda meta: set(hard.required_cooking_appliances) <= set(meta.get("recipe_cooking_appliances") or ()))
        if hard.excluded_cooking_appliances:
            apply("excluded_cooking_appliances", lambda meta: not (set(hard.excluded_cooking_appliances) & set(meta.get("recipe_cooking_appliances") or ())))
        if hard.exclusive_cooking_appliances:
            allowed = set(hard.exclusive_cooking_appliances)
            apply("exclusive_cooking_appliances", lambda meta: allowed <= set(meta.get("recipe_cooking_appliances") or ()) and set(meta.get("recipe_cooking_appliances") or ()) <= allowed and meta.get("unknown_cooking_appliance") is False)
        if hard.max_total_minutes is not None:
            apply("max_total_minutes", lambda meta: isinstance(meta.get("total_minutes"), int) and meta["total_minutes"] <= hard.max_total_minutes)
        if not rows:
            return None, CompileResult("TERMINAL", "NO_PREFERENCE_RESULTS", reason="HARD_SCOPE_EMPTY", limitations=("没有已验证同时满足全部硬约束的菜谱。",))
        if len(rows) > self._recommendation_scope_limit():
            return None, CompileResult("TERMINAL", "SCOPE_TOO_LARGE", reason="HARD_SCOPE_TOO_LARGE")
        scope = ResolvedCandidateScope(build_id, tuple(row.parent_id for row in rows), counts)
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event("recommendation_scope", status="resolved", build_id=build_id, parent_count=len(scope.parent_ids), hard_filter_counts=counts)
        return scope, None

    def _all_pds_parent_ids_by_cuisine(self, cuisine_type: str) -> list[str]:
        store = getattr(self, "parent_document_store", None)
        build_id = getattr(store, "active_build_id", None)
        if store is None or not build_id:
            return []
        if hasattr(store, "iter_recipe_metadata"):
            return [row.parent_id for row in store.iter_recipe_metadata(build_id=build_id) if str(row.metadata.get("cuisine_type", "")) == cuisine_type]
        ids: set[str] = set()
        for chunk in store.iter_chunks(build_id):
            parent = store.get_full_parent(chunk.parent_id)
            if parent is not None and parent.build_id == build_id and str(parent.metadata.get("cuisine_type", "")) == cuisine_type:
                ids.add(parent.parent_id)
        return sorted(ids)

    def _execute_compile_result(self, query: str, top_k: int, result: CompileResult, *, audit_run=None, resolved_entities=(), constraint_spec=None):
        self._audit_compile_result(audit_run, result)
        if not result.can_execute:
            return self._compile_result_bundle(result), None
        if result.action == "PDS_ENTITY_DETAIL":
            if not resolved_entities or getattr(self, "entity_direct_retriever", None) is None:
                return self._compile_result_bundle(CompileResult("UNAVAILABLE", "PDS_UNAVAILABLE", reason="PDS_UNAVAILABLE")), None
            bundle = self.entity_direct_retriever.retrieve(resolved_entities[0], self._direct_scope(query, resolved_entities[0]), audit_run=audit_run)
            return self._with_claim_policy(bundle, result), None
        plan = result.query_plan
        if plan.intent == "PREFERENCE_RECOMMEND":
            if constraint_spec is not None:
                bundle = self._try_recommendation_vector(query, plan, constraint_spec, audit_run=audit_run, claim_policy=result.claim_policy.to_dict())
            else:
                bundle = self._try_restricted_vector(query, top_k, plan, audit_run=audit_run, claim_policy=result.claim_policy.to_dict())
            if bundle is None:
                return self._compile_result_bundle(CompileResult("UNAVAILABLE", "VECTOR_UNAVAILABLE", reason="VECTOR_UNAVAILABLE")), None
            return bundle, None
        retriever = getattr(self, "targeted_graph_retriever", None)
        if retriever is None:
            return self._compile_result_bundle(CompileResult("UNAVAILABLE", "GRAPH_UNAVAILABLE", reason="GRAPH_UNAVAILABLE")), None
        fact = retriever.retrieve(plan, audit_run=audit_run)
        if fact.status != "verified":
            return self._compile_result_bundle(CompileResult("UNAVAILABLE" if fact.status == "unavailable" else "TERMINAL", "GRAPH_UNAVAILABLE" if fact.status == "unavailable" else "GRAPH_RELATION_NOT_FOUND", reason=fact.status)), None
        entity = resolved_entities[0] if resolved_entities else None
        text_evidence, limitations = self._targeted_text_evidence(plan, entity, fact, audit_run)
        return EvidenceBundle(query_plan=plan.to_dict(), entity_candidates=tuple(resolved_entities), graph_facts=(fact,), text_evidence=text_evidence, limitations=limitations, claim_policy=result.claim_policy.to_dict()), None

    def _try_recommendation_vector(self, query, plan, spec, *, audit_run=None, claim_policy=None):
        """执行候选 metadata Top30、确定性重排和 Top5 PDS 回补。"""
        retriever = getattr(self, "restricted_vector_retriever", None)
        if retriever is None or not hasattr(retriever, "retrieve_candidates"):
            if audit_run is not None and hasattr(audit_run, "record_event"):
                audit_run.record_event("recommendation_vector", status="artifact-unavailable", candidate_count=0)
            return None
        candidate_k = getattr(self.config, "retrieval_recommendation_candidate_k", 30)
        answer_k = getattr(self.config, "retrieval_recommendation_answer_k", 5)
        parent_ids = plan.parameters.get("parent_ids")
        try:
            candidates = retriever.retrieve_candidates(query, parent_ids=parent_ids, expected_parent_type="Recipe", top_k=candidate_k)
        except ArtifactMismatchError as error:
            logger.warning("推荐路径 artifact 不一致: %s", error)
            if audit_run is not None and hasattr(audit_run, "record_event"):
                audit_run.record_event("recommendation_vector", status="artifact-mismatch", candidate_count=0, verifiable=False)
            return None
        except Exception as error:
            logger.warning("推荐候选检索失败: %s", error)
            if audit_run is not None and hasattr(audit_run, "record_event"):
                audit_run.record_event("recommendation_vector", status="vector-unavailable", candidate_count=0)
            return None
        try:
            reranker = getattr(self, "preference_reranker", None) or PreferenceReranker()
            ranked = reranker.rank(candidates, spec)
            selected = [item.candidate for item in ranked[:answer_k]]
            rerank_status = "selected"
            rerank_audit = [item.audit_dict() for item in ranked]
        except Exception as error:
            # 仅本请求降级为已受限的原始向量排序，绝不放宽 hard scope。
            logger.warning("推荐重排失败，保持受限向量顺序: %s", error)
            selected = list(candidates[:answer_k])
            rerank_status = "rerank-unavailable"
            rerank_audit = []
        try:
            evidence = retriever.hydrate_candidates(selected, expected_parent_type="Recipe")
        except ArtifactMismatchError as error:
            logger.warning("推荐 Top5 PDS 回补不一致: %s", error)
            if audit_run is not None and hasattr(audit_run, "record_event"):
                audit_run.record_event("recommendation_vector", status="artifact-mismatch", candidate_count=len(candidates), verifiable=False)
            return None
        except Exception as error:
            logger.warning("推荐 Top5 PDS 回补失败: %s", error)
            return None
        limitations = () if candidates else ("NO_PREFERENCE_RESULTS", "当前受限范围没有可用的向量候选。")
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event(
                "recommendation_vector", status=rerank_status, candidate_count=len(candidates), answer_count=len(evidence),
                candidate_top30=[{"parent_id": item.parent_id, "title": item.title, "retrieval_score": item.retrieval_score, "metadata": dict(item.metadata)} for item in candidates],
                final_top5=rerank_audit if rerank_audit else [{"parent_id": item.parent_id, "retrieval_score": item.retrieval_score} for item in selected],
            )
        return EvidenceBundle(query_plan=plan.to_dict(), entity_candidates=(), graph_facts=(), text_evidence=tuple(evidence), limitations=limitations, claim_policy=claim_policy)

    @staticmethod
    def _with_claim_policy(bundle: EvidenceBundle, result: CompileResult) -> EvidenceBundle:
        return EvidenceBundle(
            query_plan=bundle.query_plan,
            entity_candidates=bundle.entity_candidates,
            graph_facts=bundle.graph_facts,
            text_evidence=bundle.text_evidence,
            limitations=bundle.limitations,
            recommendation_evidence=bundle.recommendation_evidence,
            claim_policy=result.claim_policy.to_dict(),
        )

    @staticmethod
    def _compile_result_bundle(result: CompileResult) -> EvidenceBundle:
        limitation = result.action if result.action else result.status
        return EvidenceBundle(
            query_plan=None,
            entity_candidates=(),
            graph_facts=(),
            text_evidence=(),
            limitations=(limitation, "INTENT_NON_EXECUTE") + tuple(result.limitations),
        )

    @staticmethod
    def _intent_terminal_response(bundle: EvidenceBundle) -> str:
        limitation = next((item for item in bundle.limitations if item != "INTENT_NON_EXECUTE"), "INTENT_UNRESOLVED")
        return f"当前无法安全执行该请求：{limitation}。请补充可验证的菜名、食材或偏好条件。"

    @staticmethod
    def _audit_compile_result(audit_run, result: CompileResult) -> None:
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event("intent_compile", status=result.status, compile_action=result.action, reason=result.reason, query_plan_hash=hashlib.sha256(str(result.query_plan.to_dict()).encode()).hexdigest() if result.query_plan else None, claim_policy=result.claim_policy.to_dict())

    def _new_path_rollout_stage(self, query: str, *, rollout_key: str | None = None) -> str | None:
        """按稳定 allowlist 或确定性比例决定单个请求是否可尝试新路径。"""

        config = getattr(self, "config", None)
        allowlist = set(getattr(config, "retrieval_new_path_allowlist", ()))
        request_key = rollout_key or query
        if request_key and request_key in allowlist:
            return "allowlist"
        try:
            percentage = float(getattr(config, "retrieval_new_path_traffic_percent", 100.0))
        except (TypeError, ValueError):
            return None
        if not 0.0 < percentage <= 100.0 or not request_key:
            return None
        if percentage == 100.0:
            return "percentage"
        bucket = int(hashlib.sha256(request_key.encode("utf-8")).hexdigest()[:8], 16) % 10_000
        return "percentage" if bucket < int(percentage * 100) else None

    def _legacy_fallback_or_decline(self, query: str, top_k: int, audit_run=None):
        """仅在兼容开关开启时调用未改动的旧 Router。"""

        if getattr(getattr(self, "config", None), "retrieval_legacy_fallback_enabled", True):
            return self.query_router.route_query(query, top_k, audit_run=audit_run)
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event("legacy_fallback", status="disabled")
        return EvidenceBundle(
            query_plan=None,
            entity_candidates=(),
            graph_facts=(),
            text_evidence=(),
            limitations=("LEGACY_FALLBACK_DISABLED", "新路径未提供可用证据，且旧路径兼容回退已关闭。"),
        ), None

    def _initialize_restricted_vector_retriever(self) -> None:
        """仅从已验证联合 manifest 初始化 V2，任何不一致都保持不可用。"""
        try:
            manifest = RetrievalArtifactManifest.read(self.config.retrieval_artifact_manifest_path)
            schema = MilvusV2Schema(
                dimension=self.config.milvus_dimension,
            )
            manifest.validate_runtime(
                pds_build_id=self.parent_document_store.active_build_id,
                pds_manifest_sha256=pds_manifest_sha256(
                    self.parent_document_store, self.parent_document_store.active_build_id
                ),
                milvus_database=self.config.retrieval_milvus_database,
                milvus_collection=self.config.retrieval_milvus_collection,
                schema_hash=schema.schema_hash,
            )
            host = getattr(self.index_module, "host", None) or self.config.milvus_host
            port = getattr(self.index_module, "port", None) or self.config.milvus_port
            client = create_milvus_client(f"http://{host}:{port}", self.config.retrieval_milvus_database)
            self.restricted_vector_retriever = RestrictedVectorRetriever(
                client,
                parent_store=self.parent_document_store,
                collection=self.config.retrieval_milvus_collection,
                build_id=manifest.milvus_build_id,
                database=self.config.retrieval_milvus_database,
                dimension=self.config.milvus_dimension,
                embedder=getattr(self.index_module, "embeddings", None),
            )
            self._restricted_vector_init_status = None
        except ArtifactMismatchError as error:
            logger.warning("阶段 4 V2 artifact 不匹配: %s", error)
            self.restricted_vector_retriever = None
            self._restricted_vector_init_status = "artifact-mismatch"
        except Exception as error:
            logger.warning("阶段 4 V2 artifact 不可用: %s", error)
            self.restricted_vector_retriever = None
            self._restricted_vector_init_status = "artifact-unavailable"

    @staticmethod
    def _is_preference_query(query: str) -> bool:
        text = query or ""
        return any(marker in text for marker in ("夏天吃", "天气热", "清淡", "清爽", "不腻"))

    def _preference_plan(
        self,
        query: str,
        top_k: int,
        *,
        parent_ids: list[str] | None = None,
        allow_nutrition: bool = False,
    ) -> QueryPlan | None:
        """把偏好检索范围冻结为 QueryPlan，禁止隐式全库降级。"""

        if not self._is_preference_query(query) and not allow_nutrition:
            return None
        validator = getattr(self, "query_plan_validator", None)
        if validator is None:
            return None
        parameters = {
            "scope": "all_child_chunks",
            "limit": min(top_k, QueryPlanValidator.MAX_CANDIDATES),
        }
        if parent_ids:
            parameters["scope"] = "candidate_parents"
            parameters["parent_ids"] = parent_ids
        elif "川菜" in (query or ""):
            cuisine_parent_ids = self._preference_parent_ids("川菜")
            if cuisine_parent_ids:
                parameters["scope"] = "candidate_parents"
                parameters["parent_ids"] = cuisine_parent_ids
        return validator.validate(
            QueryPlan(
                "PREFERENCE_RECOMMEND",
                "preference_recommend_v1",
                "Recipe",
                parameters,
                max_candidates=parameters["limit"],
            )
        )

    def _preference_parent_ids(self, cuisine_type: str) -> list[str]:
        """只从 active PDS build 的结构化 metadata 生成受限 parent 候选。"""

        store = getattr(self, "parent_document_store", None)
        build_id = getattr(store, "active_build_id", None)
        if store is None or not build_id:
            return []
        parent_ids: list[str] = []
        seen: set[str] = set()
        for chunk in store.iter_chunks(build_id):
            if chunk.parent_id in seen:
                continue
            parent = store.get_full_parent(chunk.parent_id)
            if parent is None or parent.build_id != build_id:
                continue
            if str(parent.metadata.get("cuisine_type", "")) != cuisine_type:
                continue
            seen.add(parent.parent_id)
            parent_ids.append(parent.parent_id)
            if len(parent_ids) == QueryPlanValidator.MAX_CANDIDATES:
                break
        return parent_ids

    def _try_restricted_vector(
        self,
        query: str,
        top_k: int,
        plan: QueryPlan,
        audit_run=None,
        *,
        recommendation_evidence: RecommendationEvidence | None = None,
        extra_limitations: tuple[str, ...] = (),
        claim_policy=None,
    ) -> EvidenceBundle | None:
        retriever = getattr(self, "restricted_vector_retriever", None)
        if retriever is None:
            if audit_run is not None and hasattr(audit_run, "record_event"):
                status = getattr(self, "_restricted_vector_init_status", None) or "artifact-unavailable"
                audit_run.record_event(
                    "restricted_vector",
                    status=status,
                    parent_count=0,
                    vector_scope="rejected" if status == "artifact-mismatch" else "none",
                )
            return None
        parent_ids = plan.parameters.get("parent_ids")
        filter_batch_count = (
            (len(parent_ids) + _MAX_FILTER_PARENTS_PER_SEARCH - 1) // _MAX_FILTER_PARENTS_PER_SEARCH
            if parent_ids
            else 0
        )
        try:
            aggregates = retriever.retrieve(
                query,
                parent_ids=parent_ids,
                expected_parent_type=plan.entity_type,
                top_k=top_k,
            )
        except ArtifactMismatchError as error:
            logger.warning("阶段 4 V2 artifact 不匹配: %s", error)
            if audit_run is not None and hasattr(audit_run, "record_event"):
                audit_run.record_event(
                    "restricted_vector",
                    status="artifact-mismatch",
                    parent_count=0,
                    vector_scope="rejected",
                )
            # 联合工件不一致时不得构造正文证据；交回既有 Router 路径。
            return None
        except Exception as error:
            logger.warning("阶段 4 V2 检索不可用: %s", error)
            if audit_run is not None and hasattr(audit_run, "record_event"):
                audit_run.record_event("restricted_vector", status="vector-unavailable", parent_count=0)
            return None
        else:
            limitations = () if aggregates else ("NO_PREFERENCE_RESULTS", "当前 V2 build 没有匹配的 child chunk。")
        bundle = EvidenceBundle(
            query_plan=plan.to_dict(),
            entity_candidates=(),
            graph_facts=(),
            text_evidence=tuple(item.text_evidence for item in aggregates),
            limitations=tuple(extra_limitations) + limitations,
            recommendation_evidence=recommendation_evidence,
            claim_policy=claim_policy,
        )
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event(
                "restricted_vector",
                status="selected" if aggregates else "unavailable",
                parent_count=len(aggregates),
                vector_scope=plan.parameters["scope"],
                expected_parent_type=plan.entity_type,
                filter_batch_count=filter_batch_count,
            )
        return bundle

    def _try_nutrition_recommendation(self, query: str, top_k: int, audit_run=None) -> EvidenceBundle | None:
        """执行阶段 5 的软偏好出口，严格请求绝不退回旧检索路径。"""

        decision = SOFT_PREFERENCE_POLICY.assess(query)
        if decision is None:
            return None
        if decision.requires_evidence_insufficient:
            bundle = self._nutrition_terminal_bundle(
                decision.evidence,
                (
                    "NUTRITION_EVIDENCE_INSUFFICIENT",
                    decision.evidence.missing_reason,
                ),
            )
            self._audit_nutrition_recommendation(audit_run, "evidence-insufficient", bundle)
            return bundle
        if not getattr(self.config, "retrieval_milvus_v2_enabled", False):
            bundle = self._nutrition_terminal_bundle(
                decision.evidence,
                (
                    "NUTRITION_PREFERENCE_RETRIEVAL_UNAVAILABLE",
                    "少油/清爽偏好检索未启用；不能用旧路径补造低脂推荐。",
                ),
            )
            self._audit_nutrition_recommendation(audit_run, "preference-retrieval-unavailable", bundle)
            return bundle
        if not decision.requires_cuisine_scope:
            bundle = self._nutrition_terminal_bundle(
                decision.evidence,
                (
                    "NUTRITION_CUISINE_SCOPE_NOT_FOUND",
                    "当前软偏好出口只支持经图谱验证的川菜候选范围。",
                ),
            )
            self._audit_nutrition_recommendation(audit_run, "cuisine-scope-required", bundle)
            return bundle
        parent_ids, scope_status = self._verified_nutrition_cuisine_scope(audit_run)
        if scope_status is not None:
            evidence = decision.evidence
            if scope_status[0] == "NUTRITION_CUISINE_EVIDENCE_UNAVAILABLE":
                evidence = self._nutrition_unavailable_evidence(decision.evidence, scope_status[1])
            bundle = self._nutrition_terminal_bundle(evidence, scope_status)
            self._audit_nutrition_recommendation(audit_run, "cuisine-scope-unavailable", bundle)
            return bundle
        plan = self._preference_plan(query, top_k, parent_ids=parent_ids, allow_nutrition=True)
        if plan is None:
            bundle = self._nutrition_terminal_bundle(
                decision.evidence,
                (
                    "NUTRITION_PREFERENCE_RETRIEVAL_UNAVAILABLE",
                    "偏好检索计划不可用；不能扩大为全库低脂推荐。",
                ),
            )
            self._audit_nutrition_recommendation(audit_run, "preference-plan-unavailable", bundle)
            return bundle
        bundle = self._try_restricted_vector(
            query,
            top_k,
            plan,
            audit_run=audit_run,
            recommendation_evidence=decision.evidence,
            extra_limitations=("NUTRITION_SOFT_PREFERENCE_ONLY", decision.evidence.missing_reason),
        )
        if bundle is None:
            bundle = self._nutrition_terminal_bundle(
                decision.evidence,
                (
                    "NUTRITION_PREFERENCE_RETRIEVAL_UNAVAILABLE",
                    "少油/清爽偏好检索当前不可用；不能回退为未受限的低脂推荐。",
                ),
            )
            self._audit_nutrition_recommendation(audit_run, "restricted-vector-unavailable", bundle)
            return bundle
        self._audit_nutrition_recommendation(audit_run, "soft-preference-selected", bundle)
        return bundle

    def _verified_nutrition_cuisine_scope(self, audit_run=None) -> tuple[list[str], tuple[str, str] | None]:
        """先用固定图模板验证 PDS 的川菜候选，图不可用时不允许全库降级。"""

        candidate_ids = self._preference_parent_ids("川菜")
        if not candidate_ids:
            return [], (
                "NUTRITION_CUISINE_SCOPE_NOT_FOUND",
                "当前没有可供图谱验证的川菜候选范围。",
            )
        validator = getattr(self, "query_plan_validator", None)
        retriever = getattr(self, "targeted_graph_retriever", None)
        if validator is None or retriever is None:
            return [], (
                "NUTRITION_CUISINE_EVIDENCE_UNAVAILABLE",
                "营养或菜系硬证据当前不可用；不能把未受限向量结果称为低脂川菜。",
            )
        plan = validator.validate(
            QueryPlan(
                "RECIPE_CUISINE_FILTER",
                "recipe_cuisine_filter_v1",
                "Recipe",
                {
                    "recipe_ids": candidate_ids,
                    "cuisine_type": "川菜",
                    "limit": len(candidate_ids),
                },
                max_candidates=len(candidate_ids),
            )
        )
        fact = retriever.retrieve(plan, audit_run=audit_run)
        if fact.status == "unavailable":
            return [], (
                "NUTRITION_CUISINE_EVIDENCE_UNAVAILABLE",
                "营养或菜系硬证据当前不可用；不能把未受限向量结果称为低脂川菜。",
            )
        if fact.status != "verified" or not fact.node_ids:
            return [], (
                "NUTRITION_CUISINE_SCOPE_NOT_FOUND",
                "当前图谱没有验证到川菜候选，不能把向量结果称为低脂川菜。",
            )
        return list(fact.node_ids), None

    @staticmethod
    def _nutrition_terminal_bundle(
        evidence: RecommendationEvidence,
        limitations: tuple[str, str],
    ) -> EvidenceBundle:
        return EvidenceBundle(
            query_plan={
                "intent": "PREFERENCE_RECOMMEND",
                "template_id": "preference_recommend_v1",
                "source": "nutrition_policy",
            },
            entity_candidates=(),
            graph_facts=(),
            text_evidence=(),
            limitations=limitations,
            recommendation_evidence=evidence,
        )

    @staticmethod
    def _nutrition_unavailable_evidence(
        evidence: RecommendationEvidence,
        missing_reason: str,
    ) -> RecommendationEvidence:
        return RecommendationEvidence(
            level="evidence_unavailable",
            policy_version=evidence.policy_version,
            source_status="nutrition_or_cuisine_hard_evidence_unavailable",
            missing_reason=missing_reason,
            claim_scope="不得把未受限向量结果称为低脂川菜",
        )

    @staticmethod
    def _audit_nutrition_recommendation(audit_run, status: str, bundle: EvidenceBundle) -> None:
        if audit_run is None or not hasattr(audit_run, "record_event"):
            return
        evidence = bundle.recommendation_evidence
        audit_run.record_event(
            "nutrition_recommendation",
            status=status,
            evidence_level=evidence.level if evidence else None,
            policy_version=evidence.policy_version if evidence else None,
            source_status=evidence.source_status if evidence else None,
            missing_reason=evidence.missing_reason if evidence else None,
            claim_scope=evidence.claim_scope if evidence else None,
            text_evidence_count=len(bundle.text_evidence),
            limitations=list(bundle.limitations),
        )

    def _try_targeted_graph(self, query: str, audit_run=None) -> EvidenceBundle | None:
        # 保持测试/兼容调用中仅构造部分系统对象时的旧路由语义。
        config = getattr(self, "config", None)
        if not getattr(config, "retrieval_query_plan_enabled", False):
            return None
        validator = getattr(self, "query_plan_validator", None)
        resolver = getattr(self, "entity_resolver", None)
        if validator is None or resolver is None:
            return None
        intent, expected_type = self._targeted_intent(query)
        if intent is None:
            return None
        try:
            candidates = resolver.resolve(query, expected_types=(expected_type,))
        except Exception as error:
            logger.warning("目标图实体解析不可用: %s", error)
            fact = TargetedGraphRetriever.unavailable_for_intent(
                intent,
                audit_run=audit_run,
                error_type=type(error).__name__,
            )
            base = EvidenceBundle(
                query_plan=None,
                entity_candidates=(),
                graph_facts=(),
                text_evidence=(),
                limitations=("GRAPH_UNAVAILABLE", "图实体解析当前不可用；不能验证请求的关系是否成立。"),
            )
            return EvidenceBuilder.merge_graph_facts(base, (fact,))
        if not candidates:
            return EvidenceBundle(
                query_plan=None,
                entity_candidates=(),
                graph_facts=(),
                text_evidence=(),
                limitations=("ENTITY_NOT_FOUND", "未定位到关系查询中的同名实体；未调用全库向量检索。"),
            )
        if candidates[0].ambiguity:
            if expected_type == "Ingredient" and intent in {"INGREDIENT_RECIPES", "INGREDIENT_VEGETABLE_PAIRS"}:
                return self._try_parallel_ingredient_graph(query, intent, candidates, audit_run)
            return EvidenceBundle(
                query_plan=None,
                entity_candidates=tuple(candidates),
                graph_facts=(),
                text_evidence=(),
                limitations=("ENTITY_AMBIGUOUS", "关系查询实体候选并列，未自动选择。"),
            )
        plan = self._targeted_plan(query, intent, candidates[0].node_id)
        if plan is None:
            return None
        targeted_retriever = getattr(self, "targeted_graph_retriever", None)
        if targeted_retriever is None:
            fact = TargetedGraphRetriever.unavailable_fact(plan, audit_run=audit_run)
        else:
            fact = targeted_retriever.retrieve(plan, audit_run=audit_run)
        limitations: tuple[str, ...] = ()
        if fact.status == "not_found":
            limitations = ("GRAPH_RELATION_NOT_FOUND", "当前图谱未找到该关系；正文不能证明该关系。")
        elif fact.status == "unavailable":
            limitations = ("GRAPH_UNAVAILABLE", "图证据当前不可用；不能回答关系已成立。")
        text_evidence, pds_limitations = self._targeted_text_evidence(plan, candidates[0], fact, audit_run)
        limitations += pds_limitations
        base = EvidenceBundle(
            query_plan=plan.to_dict(),
            entity_candidates=tuple(candidates),
            graph_facts=(),
            text_evidence=text_evidence,
            limitations=limitations,
        )
        return EvidenceBuilder.merge_graph_facts(base, (fact,))

    def _try_parallel_ingredient_graph(self, query: str, intent: str, candidates, audit_run) -> EvidenceBundle:
        """聚合精确同名 Ingredient 的固定图路径，绝不从并列候选中任选一个。"""

        plans = [self._targeted_plan(query, intent, candidate.node_id) for candidate in candidates]
        if not plans or any(plan is None for plan in plans):
            return EvidenceBundle(
                query_plan=None,
                entity_candidates=tuple(candidates),
                graph_facts=(),
                text_evidence=(),
                limitations=("ENTITY_AMBIGUOUS", "关系查询实体候选并列，未自动选择。"),
            )
        targeted_retriever = getattr(self, "targeted_graph_retriever", None)
        facts = []
        for plan in plans:
            if targeted_retriever is None:
                facts.append(TargetedGraphRetriever.unavailable_fact(plan, audit_run=audit_run))
            else:
                facts.append(targeted_retriever.retrieve(plan, audit_run=audit_run))
        limitations: tuple[str, ...] = ()
        if not any(fact.status == "verified" for fact in facts):
            if any(fact.status == "unavailable" for fact in facts):
                limitations = ("GRAPH_UNAVAILABLE", "图证据当前不可用；不能回答关系已成立。")
            else:
                limitations = ("GRAPH_RELATION_NOT_FOUND", "当前图谱未找到该关系；正文不能证明该关系。")
        query_plan = plans[0].to_dict()
        query_plan["parallel_candidate_ids"] = [candidate.node_id for candidate in candidates]
        query_plan["resolution_strategy"] = "parallel_exact_name_ingredients"
        text_evidence, pds_limitations = self._targeted_graph_recipe_evidence(facts, audit_run)
        limitations += pds_limitations
        base = EvidenceBundle(
            query_plan=query_plan,
            entity_candidates=tuple(candidates),
            graph_facts=(),
            text_evidence=text_evidence,
            limitations=limitations,
        )
        return EvidenceBuilder.merge_graph_facts(base, tuple(facts))

    def _targeted_text_evidence(self, plan: QueryPlan, candidate, fact, audit_run) -> tuple[tuple, tuple[str, ...]]:
        """为已验证目标图结果回补其所属实体的 PDS 正文。"""
        if fact.status != "verified":
            return (), ()
        retriever = getattr(self, "entity_direct_retriever", None)
        if retriever is None:
            return (), ("PDS_TEXT_UNAVAILABLE", "图已定位，但 PDS 正文回补未启用。")
        if plan.intent == "RECIPE_STEP":
            scope = {
                "scope": "RECIPE_STEP",
                "step_id": plan.parameters.get("step_id"),
                "step_number": plan.parameters.get("step_number"),
                "before": 1,
                "after": 1,
            }
            if scope["step_id"] is None:
                scope.pop("step_id")
            if scope["step_number"] is None:
                scope.pop("step_number")
        elif plan.intent == "TECHNIQUE_CHUNKS":
            scope = {"scope": "TECHNIQUE_FULL"}
        else:
            return self._targeted_graph_recipe_evidence((fact,), audit_run)
        try:
            hydrated = retriever.retrieve(candidate, scope, audit_run=audit_run)
        except Exception as error:
            logger.warning("目标图 PDS 回补不可用: %s", error)
            return (), ("PDS_TEXT_UNAVAILABLE", "图已定位，但 PDS 正文回补当前不可用。")
        pds_limitations = tuple(
            limitation
            for limitation in hydrated.limitations
            if limitation in {"PARENT_DOCUMENT_NOT_FOUND", "PDS_ANCHOR_NOT_FOUND", "parent-store-unavailable"}
        )
        if not hydrated.text_evidence and not pds_limitations:
            pds_limitations = ("PDS_TEXT_UNAVAILABLE", "图已定位，但没有可验证的 PDS 正文回补。")
        return hydrated.text_evidence, pds_limitations

    def _targeted_graph_recipe_evidence(self, facts, audit_run) -> tuple[tuple, tuple[str, ...]]:
        """为食材关系图中的 Recipe 节点回补正文，绝不以正文替代图关系。"""
        retriever = getattr(self, "entity_direct_retriever", None)
        if retriever is None:
            return (), ("PDS_TEXT_UNAVAILABLE", "图已定位，但 PDS 正文回补未启用。")
        seen_recipe_ids: set[str] = set()
        evidence = []
        limitations = []
        for fact in facts:
            if fact.status != "verified":
                continue
            for row in fact.properties.get("rows", []):
                recipe_id = str(row.get("recipe_id") or "").strip()
                if not recipe_id or recipe_id in seen_recipe_ids:
                    continue
                seen_recipe_ids.add(recipe_id)
                recipe_name = str(row.get("recipe_name") or recipe_id)
                candidate = EntityCandidate(recipe_id, "Recipe", recipe_name, "exact_name", 1.0, False)
                try:
                    hydrated = retriever.retrieve(candidate, {"scope": "RECIPE_FULL"}, audit_run=audit_run)
                except Exception as error:
                    logger.warning("目标图菜谱 PDS 回补不可用: %s", error)
                    limitations.append("PDS_TEXT_UNAVAILABLE")
                    continue
                evidence.extend(hydrated.text_evidence)
                limitations.extend(
                    limitation
                    for limitation in hydrated.limitations
                    if limitation in {"PARENT_DOCUMENT_NOT_FOUND", "parent-store-unavailable"}
                )
        if seen_recipe_ids and not evidence and not limitations:
            limitations.append("PDS_TEXT_UNAVAILABLE")
        return tuple(evidence), tuple(dict.fromkeys(limitations))

    @staticmethod
    def _targeted_intent(query: str) -> tuple[str | None, str | None]:
        text = query or ""
        if "蔬菜" in text and "搭配" in text:
            return "INGREDIENT_VEGETABLE_PAIRS", "Ingredient"
        if any(marker in text for marker in ("能做什么", "能做哪些", "可以做什么", "适合做什么")):
            return "INGREDIENT_RECIPES", "Ingredient"
        if any(marker in text for marker in ("第一步", "第1步", "第 1 步")):
            return "RECIPE_STEP", "Recipe"
        if any(marker in text for marker in ("关键要点", "适用场景", "技巧章节")):
            return "TECHNIQUE_CHUNKS", "TechniqueDoc"
        return None, None

    def _targeted_plan(self, query: str, intent: str, entity_id: str) -> QueryPlan | None:
        parameters = {"limit": min(self.config.top_k, QueryPlanValidator.MAX_CANDIDATES)}
        if intent == "INGREDIENT_VEGETABLE_PAIRS":
            parameters.update({"ingredient_id": entity_id, "vegetable_category": "蔬菜"})
            entity_type = "Ingredient"
        elif intent == "INGREDIENT_RECIPES":
            parameters["ingredient_id"] = entity_id
            entity_type = "Ingredient"
        elif intent == "RECIPE_STEP":
            import re

            match = re.search(r"第\s*(\d+)\s*步", query or "")
            parameters.update({"recipe_id": entity_id, "step_number": int(match.group(1)) if match else 1})
            parameters["limit"] = 1
            entity_type = "Recipe"
        elif intent == "TECHNIQUE_CHUNKS":
            parameters["technique_doc_id"] = entity_id
            entity_type = "TechniqueDoc"
        else:
            return None
        return self.query_plan_validator.validate(
            QueryPlan(
                intent=intent,
                template_id={
                    "RECIPE_STEP": "recipe_step_anchor_v1",
                    "INGREDIENT_RECIPES": "ingredient_recipes_v1",
                    "INGREDIENT_VEGETABLE_PAIRS": "ingredient_vegetable_pairs_v1",
                    "TECHNIQUE_CHUNKS": "technique_chunks_v1",
                }[intent],
                entity_type=entity_type,
                parameters=parameters,
                max_candidates=parameters["limit"],
            )
        )

    @staticmethod
    def _audit_targeted_graph(audit_run, bundle: EvidenceBundle) -> None:
        if audit_run is not None and hasattr(audit_run, "record_event"):
            fact = next((item for item in bundle.graph_facts if item.status == "verified"), None)
            fact = fact or (bundle.graph_facts[-1] if bundle.graph_facts else None)
            audit_run.record_event(
                "targeted_graph_selection",
                status=fact.status if fact else "not_found",
                template_id=fact.template_id if fact else None,
                graph_fact_status=fact.status if fact else None,
                graph_fact_count=len(bundle.graph_facts),
                limitations=list(bundle.limitations),
                vector_search_calls=0,
            )

    def _try_entity_direct(
        self,
        query: str,
        audit_run=None,
        *,
        allow_generalized_advice: bool = False,
    ) -> EvidenceBundle | None:
        if self.entity_resolver is None or self.entity_direct_retriever is None:
            return None
        try:
            candidates = self.entity_resolver.resolve(query, expected_types=("Recipe", "TechniqueDoc"))
        except Exception as error:
            logger.warning("实体直达解析不可用，回退旧 Router: %s", error)
            self._audit_entity_direct_error(audit_run, "resolver-unavailable", error)
            return None
        if not candidates:
            bundle = EvidenceBundle(
                query_plan=None,
                entity_candidates=(),
                graph_facts=(),
                text_evidence=(),
                limitations=("ENTITY_NOT_FOUND", "未定位到同名实体；未调用全库向量检索。"),
            )
            if allow_generalized_advice:
                self._audit_entity_direct(
                    audit_run,
                    "entity_not_found_generalized",
                    bundle,
                )
                return None
            self._audit_entity_direct(audit_run, "entity_not_found", bundle)
            return bundle
        if candidates[0].ambiguity:
            bundle = EvidenceBundle(
                query_plan=None,
                entity_candidates=tuple(candidates),
                graph_facts=(),
                text_evidence=(),
                limitations=("ENTITY_AMBIGUOUS", "实体候选并列，未自动选择且未调用全库向量检索。"),
            )
            self._audit_entity_direct(audit_run, "ambiguous", bundle)
            return bundle
        try:
            return self.entity_direct_retriever.retrieve(candidates[0], self._direct_scope(query, candidates[0]), audit_run=audit_run)
        except Exception as error:
            logger.warning("实体直达执行失败，回退旧 Router: %s", error)
            self._audit_entity_direct_error(audit_run, "retriever-unavailable", error)
            return None

    @staticmethod
    def _direct_scope(query: str, entity) -> dict:
        if entity.node_type == "Recipe":
            import re
            matched = re.search(r"第\s*(\d+)\s*步|第一步", query or "")
            if matched:
                number = int(matched.group(1)) if matched.group(1) else 1
                return {"scope": "RECIPE_STEP", "step_number": number, "before": 1, "after": 1}
            return {"scope": "RECIPE_FULL"}
        return {"scope": "TECHNIQUE_FULL"}

    @staticmethod
    def _audit_entity_direct(audit_run, status: str, bundle: EvidenceBundle) -> None:
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event(
                "entity_direct",
                status=status,
                candidate_count=len(bundle.entity_candidates),
                graph_fact_statuses=[fact.status for fact in bundle.graph_facts],
                text_evidence_count=len(bundle.text_evidence),
                limitations=list(bundle.limitations),
                vector_search_calls=0,
            )

    @staticmethod
    def _audit_entity_direct_error(audit_run, status: str, error: Exception) -> None:
        if audit_run is not None and hasattr(audit_run, "record_event"):
            audit_run.record_event("entity_direct", status=status, error_type=type(error).__name__, vector_search_calls=0)

    def _get_query_embedding(self, query: str):
        """获取查询的向量表示（用于语义缓存）"""
        try:
            if hasattr(self.index_module, 'embedding_model'):
                # 使用现有的embedding模型
                return self.index_module.embedding_model.embed_documents([query])[0]
            return None
        except Exception as e:
            logger.warning(f"获取查询向量失败: {e}")
            return None

    def run_web_service(self):
        """运行Web服务模式"""
        if not self.system_ready:
            print("❌ 系统未就绪，请先构建知识库")
            return

        try:
            # 使用Web服务处理器设置Flask应用
            app = self.web_handler.setup_flask_app()
            if not app:
                print("❌ Flask应用初始化失败")
                return

            print("🚀 启动Web服务...")
            print(f"📊 健康检查: http://localhost:8000/health")
            print(f"💬 聊天API: http://localhost:8000/api/chat")
            print(f"🌊 流式聊天: http://localhost:8000/api/chat/stream")
            print(f"🍽️ 菜谱推荐: http://localhost:8000/api/recipes/recommendations")
            print(f"📖 菜谱详情: http://localhost:8000/api/recipes/<recipe_id>")
            print(f"📈 统计信息: http://localhost:8000/api/stats")
            print("=" * 50)

            # 启动Flask应用
            app.run(host='0.0.0.0', port=8000, debug=False)

        except Exception as e:
            logger.error(f"Web服务启动失败: {e}")
            print(f"❌ Web服务启动失败: {e}")

    def _cleanup(self):
        """清理资源"""
        if self.data_module:
            self.data_module.close()
        if self.traditional_retrieval:
            self.traditional_retrieval.close()
        if self.graph_rag_retrieval:
            self.graph_rag_retrieval.close()
        if self.index_module:
            self.index_module.close()

def main():
    """主函数"""
    try:
        print("启动高级图RAG系统...")
        
        # 创建高级图RAG系统
        rag_system = AdvancedGraphRAGSystem()
        
        # 初始化系统
        rag_system.initialize_system()
        
        # 构建知识库
        rag_system.build_knowledge_base()
        
        # 启动Web服务（Docker环境）
        rag_system.run_web_service()
        
    except Exception as e:
        logger.error(f"系统运行失败: {e}")
        import traceback
        traceback.print_exc()
        print(f"\n❌ 系统错误: {e}")

if __name__ == "__main__":
    main() 
