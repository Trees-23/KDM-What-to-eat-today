"""
Web服务处理模块
负责处理Web API和静态文件服务
"""

import logging
import json
import time
import concurrent.futures
from datetime import datetime
from typing import Dict, Any, Optional

from rag_modules.rag_audit import RAGAuditManager, query_hash

logger = logging.getLogger(__name__)

class WebServiceHandler:
    """
    Web服务处理器
    
    功能：
    1. API路由处理
    2. 静态文件服务
    3. 错误处理
    4. 响应格式化
    """
    
    def __init__(self, rag_system):
        """初始化Web服务处理器"""
        self.rag_system = rag_system
        self.audit_manager = RAGAuditManager.from_config(rag_system.config)
        self.app = None
    
    def setup_flask_app(self):
        """设置Flask应用和路由"""
        try:
            from flask import Flask, request, jsonify, Response
            from flask_cors import CORS
            
            self.app = Flask(__name__)
            CORS(self.app)
            
            # 设置路由
            self._setup_routes()
            
            return self.app
            
        except ImportError as e:
            logger.error(f"Flask导入失败: {e}")
            return None
    
    def _setup_routes(self):
        """设置所有API路由"""
        from flask import request, jsonify, Response, send_from_directory
        
        @self.app.route('/')
        def serve_index():
            """提供主页"""
            return self._serve_static_file('index.html')
        
        @self.app.route('/<path:filename>')
        def serve_static(filename):
            """提供静态文件服务"""
            return self._serve_static_file(filename)
        
        @self.app.route('/health', methods=['GET'])
        def health_check():
            """健康检查端点"""
            return jsonify({
                "status": "healthy",
                "timestamp": str(datetime.now()),
                "service": "RAG System"
            })
        
        @self.app.route('/api/chat', methods=['POST'])
        def chat():
            """聊天API - 普通响应"""
            return self._handle_chat_request()
        
        @self.app.route('/api/chat/stream', methods=['POST'])
        def chat_stream():
            """聊天API - 流式响应"""
            return self._handle_stream_request()
        
        @self.app.route('/api/recipes/recommendations', methods=['POST'])
        def get_recommendations():
            """获取菜谱推荐"""
            return self._handle_recommendations_request()
        
        @self.app.route('/api/recipes/<recipe_id>', methods=['GET'])
        def get_recipe_detail(recipe_id):
            """获取菜谱详情"""
            return self._handle_recipe_detail_request(recipe_id)
        
        @self.app.route('/api/stats', methods=['GET'])
        def get_stats():
            """获取系统统计信息"""
            return self._handle_stats_request()
    
    def _serve_static_file(self, filename):
        """提供静态文件服务"""
        import os
        from flask import send_from_directory
        
        # 安全检查，防止路径遍历攻击
        if '..' in filename or filename.startswith('/'):
            return "Forbidden", 403
        
        # 前端文件路径
        frontend_path = os.path.join(os.getcwd(), 'frontend', 'dist')
        
        try:
            if filename == 'index.html' or filename == '':
                return send_from_directory(frontend_path, 'index.html')
            else:
                return send_from_directory(frontend_path, filename)
        except FileNotFoundError:
            # 如果文件不存在，返回index.html（用于SPA路由）
            return send_from_directory(frontend_path, 'index.html')
    
    def _handle_chat_request(self):
        """处理普通聊天请求"""
        from flask import request, jsonify
        
        try:
            data = request.get_json()
            query = data.get('message', '')
            session_id = data.get('session_id', '')
            allow_generalized_advice = data.get('allow_generalized_advice') is True
            
            if not query:
                return jsonify({"error": "消息不能为空"}), 400

            audit_run = self.audit_manager.create_run()
            request_start = audit_run.mark_request_start()
            self._record_request_start(audit_run, query, session_id, "non_stream", request_start)
            
            # 🚀 并行执行缓存检查和预处理
            cached_response = None
            enhanced_query = query
            cache_started_at = None
            cache_finished_at = None
            cache_error = None
            context_started_at = None
            context_finished_at = None
            context_error = None
            context_history_count = self._session_history_count(session_id)
            
            def check_cache():
                nonlocal cached_response, cache_started_at, cache_finished_at, cache_error
                cache_started_at = datetime.now()
                try:
                    cached_response = self.rag_system.cache_manager.check_semantic_cache(query, session_id)
                except Exception as e:
                    cache_error = e
                    raise
                finally:
                    cache_finished_at = datetime.now()
            
            def prepare_query():
                nonlocal enhanced_query, context_started_at, context_finished_at, context_error
                context_started_at = datetime.now()
                try:
                    enhanced_query = self.rag_system.cache_manager.get_context_for_query(session_id, query)
                except Exception as e:
                    context_error = e
                    raise
                finally:
                    context_finished_at = datetime.now()
            
            # 并行执行缓存检查和查询预处理
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                future_cache = executor.submit(check_cache)
                future_query = executor.submit(prepare_query)
                
                # 等待缓存检查完成
                concurrent.futures.wait([future_cache], timeout=1)
                self._record_cache_check(audit_run, cached_response, cache_started_at, cache_finished_at, cache_error)
                
                if cached_response:
                    # 缓存命中，取消查询预处理
                    future_query.cancel()
                    self.rag_system.cache_manager.add_to_context(session_id, query, cached_response)
                    self._record_context_enhancement(
                        audit_run,
                        query,
                        enhanced_query,
                        context_history_count,
                        context_started_at,
                        context_finished_at,
                        context_error,
                        cancelled=True,
                    )
                    audit_run.append_process(
                        "Final Output",
                        {
                            "final_source": "cache",
                            "response_chars": len(cached_response),
                            "response_hash": query_hash(cached_response),
                        },
                    )
                    audit_run.finish_request(success=True, final_source="cache")
                    return jsonify({
                        "response": cached_response,
                        "query": query,
                        "session_id": session_id,
                        "timestamp": str(datetime.now()),
                        "from_cache": True
                    })
                
                # 缓存未命中，等待查询预处理完成
                concurrent.futures.wait([future_query], timeout=2)
                self._record_context_enhancement(
                    audit_run,
                    query,
                    enhanced_query,
                    context_history_count,
                    context_started_at,
                    context_finished_at,
                    context_error,
                )
            
            # 缓存未命中，执行完整的RAG流程
            if hasattr(self.rag_system, "retrieve_for_generation"):
                documents, analysis = self.rag_system.retrieve_for_generation(
                    enhanced_query,
                    self.rag_system.config.top_k,
                    audit_run=audit_run,
                    allow_generalized_advice=allow_generalized_advice,
                )
            else:
                documents, analysis = self.rag_system.query_router.route_query(
                    query=enhanced_query,
                    top_k=self.rag_system.config.top_k,
                    audit_run=audit_run,
                )
            # 使用生成模块生成最终答案
            response = self.rag_system.generation_module.generate_adaptive_answer(
                enhanced_query,
                documents,
                audit_run=audit_run,
            )
            
            # 将结果添加到会话缓存和上下文
            self.rag_system.cache_manager.add_to_semantic_cache(query, response, session_id)
            self.rag_system.cache_manager.add_to_context(session_id, query, response)
            audit_run.finish_request(success=True, final_source="generation")
            
            return jsonify({
                "response": response,
                "query": query,
                "timestamp": str(datetime.now())
            })
            
        except Exception as e:
            logger.error(f"Chat API错误: {e}")
            if "audit_run" in locals():
                audit_run.record_error("request", e)
                audit_run.finish_request(success=False, final_source="error")
            return jsonify({"error": str(e)}), 500
    
    def _handle_stream_request(self):
        """处理流式聊天请求"""
        from flask import request, jsonify, Response
        
        try:
            data = request.get_json()
            query = data.get('message', '')
            session_id = data.get('session_id', '')
            allow_generalized_advice = data.get('allow_generalized_advice') is True
            
            if not query:
                return jsonify({"error": "消息不能为空"}), 400

            audit_run = self.audit_manager.create_run()
            request_start = audit_run.mark_request_start()
            self._record_request_start(audit_run, query, session_id, "stream", request_start)
            
            def generate():
                try:
                    # 🚀 并行执行缓存检查和预处理
                    cached_response = None
                    enhanced_query = query
                    cache_started_at = None
                    cache_finished_at = None
                    cache_error = None
                    context_started_at = None
                    context_finished_at = None
                    context_error = None
                    context_history_count = self._session_history_count(session_id)
                    
                    def check_cache():
                        nonlocal cached_response, cache_started_at, cache_finished_at, cache_error
                        cache_started_at = datetime.now()
                        try:
                            cached_response = self.rag_system.cache_manager.check_semantic_cache(query, session_id)
                        except Exception as e:
                            cache_error = e
                            raise
                        finally:
                            cache_finished_at = datetime.now()
                    
                    def prepare_query():
                        nonlocal enhanced_query, context_started_at, context_finished_at, context_error
                        context_started_at = datetime.now()
                        try:
                            enhanced_query = self.rag_system.cache_manager.get_context_for_query(session_id, query)
                        except Exception as e:
                            context_error = e
                            raise
                        finally:
                            context_finished_at = datetime.now()
                    
                    # 并行执行缓存检查和查询预处理
                    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                        future_cache = executor.submit(check_cache)
                        future_query = executor.submit(prepare_query)
                        
                        # 等待缓存检查完成
                        concurrent.futures.wait([future_cache], timeout=1)
                        self._record_cache_check(audit_run, cached_response, cache_started_at, cache_finished_at, cache_error)
                        
                        if cached_response:
                            # 缓存命中，快速返回
                            future_query.cancel()
                            self.rag_system.cache_manager.add_to_context(session_id, query, cached_response)
                            self._record_context_enhancement(
                                audit_run,
                                query,
                                enhanced_query,
                                context_history_count,
                                context_started_at,
                                context_finished_at,
                                context_error,
                                cancelled=True,
                            )
                            audit_run.append_process(
                                "Final Output",
                                {
                                    "final_source": "cache",
                                    "response_chars": len(cached_response),
                                    "response_hash": query_hash(cached_response),
                                },
                            )
                            chunk_size = 3
                            for i in range(0, len(cached_response), chunk_size):
                                chunk = cached_response[i:i+chunk_size]
                                data_obj = {"chunk": chunk, "from_cache": True}
                                yield f"data: {json.dumps(data_obj)}\n\n"
                                time.sleep(0.02)  # 更快的流式响应
                            audit_run.finish_request(success=True, final_source="cache")
                            yield f"data: [DONE]\n\n"
                            return
                        
                        # 缓存未命中，等待查询预处理完成
                        concurrent.futures.wait([future_query], timeout=2)
                        self._record_context_enhancement(
                            audit_run,
                            query,
                            enhanced_query,
                            context_history_count,
                            context_started_at,
                            context_finished_at,
                            context_error,
                        )
                    
                    # 缓存未命中，执行完整的RAG流程
                    if hasattr(self.rag_system, "retrieve_for_generation"):
                        documents, analysis = self.rag_system.retrieve_for_generation(
                            enhanced_query,
                            self.rag_system.config.top_k,
                            audit_run=audit_run,
                            allow_generalized_advice=allow_generalized_advice,
                        )
                    else:
                        documents, analysis = self.rag_system.query_router.route_query(
                            query=enhanced_query,
                            top_k=self.rag_system.config.top_k,
                            audit_run=audit_run,
                        )
                    
                    # 流式生成答案
                    full_response = ""
                    for chunk in self.rag_system.generation_module.generate_adaptive_answer_stream(
                        enhanced_query,
                        documents,
                        audit_run=audit_run,
                    ):
                        full_response += chunk
                        data_obj = {"chunk": chunk}
                        yield f"data: {json.dumps(data_obj)}\n\n"
                    
                    # 将完整结果添加到会话缓存和上下文
                    self.rag_system.cache_manager.add_to_semantic_cache(query, full_response, session_id)
                    self.rag_system.cache_manager.add_to_context(session_id, query, full_response)
                    audit_run.finish_request(success=True, final_source="generation")
                    
                    # 发送结束标记
                    yield f"data: [DONE]\n\n"
                
                except Exception as e:
                    logger.error(f"Stream API错误: {e}")
                    audit_run.record_error("stream_request", e)
                    audit_run.finish_request(success=False, final_source="error")
                    error_msg = f"抱歉，处理您的问题时出现错误：{str(e)}"
                    data_obj = {"chunk": error_msg}
                    yield f"data: {json.dumps(data_obj)}\n\n"
                    yield f"data: [DONE]\n\n"
            
            response = Response(generate(), mimetype='text/event-stream')
            response.headers['Cache-Control'] = 'no-cache'
            response.headers['Connection'] = 'keep-alive'
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response
            
        except Exception as e:
            logger.error(f"Stream API错误: {e}")
            if "audit_run" in locals():
                audit_run.record_error("stream_setup", e)
                audit_run.finish_request(success=False, final_source="error")
            return jsonify({"error": str(e)}), 500

    def _record_request_start(self, audit_run, query: str, session_id: str, request_mode: str, started_at: datetime):
        audit_run.append_process(
            "Request",
            {
                "original_query": query,
                "original_query_hash": query_hash(query),
                "session_id": session_id or "",
                "request_mode": request_mode,
                "request_start": started_at.isoformat(timespec="milliseconds"),
                "evaluation_sample_id": audit_run.audit_id,
                "experiment_id": getattr(self.rag_system.config, "rag_experiment_id", "baseline"),
                "variant_name": getattr(self.rag_system.config, "rag_variant_name", "default"),
                "config_hash": self.rag_system.config.config_hash() if hasattr(self.rag_system.config, "config_hash") else "",
            },
        )

    def _record_cache_check(self, audit_run, cached_response, started_at, finished_at, error):
        if error is not None:
            audit_run.record_error("cache_check", error)
        audit_run.record_event(
            "cache_check",
            status="error" if error else "completed",
            start_time=started_at,
            end_time=finished_at,
            cache_hit=bool(cached_response),
            cached_response_chars=len(cached_response) if cached_response else 0,
        )

    def _record_context_enhancement(
        self,
        audit_run,
        original_query: str,
        enhanced_query: str,
        history_count: int,
        started_at,
        finished_at,
        error,
        cancelled: bool = False,
    ):
        if error is not None:
            audit_run.record_error("context_enhancement", error)
        audit_run.record_event(
            "context_enhancement",
            status="cancelled" if cancelled else ("error" if error else "completed"),
            start_time=started_at,
            end_time=finished_at,
            enhanced=bool(enhanced_query and enhanced_query != original_query),
            history_count=history_count,
            original_query_length=len(original_query or ""),
            enhanced_query_length=len(enhanced_query or original_query or ""),
            enhanced_query_hash=query_hash(enhanced_query or original_query or ""),
        )

    def _session_history_count(self, session_id: str) -> int:
        try:
            if not session_id:
                return 0
            contexts = getattr(self.rag_system.cache_manager, "session_contexts", {})
            return len(contexts.get(session_id, []))
        except Exception:
            return 0
    
    def _handle_recommendations_request(self):
        """处理菜谱推荐请求"""
        from flask import request, jsonify
        
        try:
            data = request.get_json() or {}
            preferences = data.get('preferences', {})
            
            # 获取推荐菜谱
            recipes = self.rag_system.recipe_manager.get_random_recipes_with_images(limit=3)
            
            return jsonify({
                "success": True,
                "data": recipes,
                "message": "推荐获取成功"
            })
            
        except Exception as e:
            logger.error(f"推荐API错误: {e}")
            return jsonify({"error": str(e)}), 500
    
    def _handle_recipe_detail_request(self, recipe_id):
        """处理菜谱详情请求"""
        from flask import jsonify
        
        try:
            recipe = self.rag_system.recipe_manager.get_recipe_by_id(recipe_id)
            if recipe:
                return jsonify({
                    "success": True,
                    "data": recipe
                })
            else:
                return jsonify({"error": "菜谱不存在"}), 404
                
        except Exception as e:
            logger.error(f"菜谱详情API错误: {e}")
            return jsonify({"error": str(e)}), 500
    
    def _handle_stats_request(self):
        """处理统计信息请求"""
        from flask import jsonify
        
        try:
            # 获取系统统计信息
            stats = {
                "cache_stats": self.rag_system.cache_manager.get_session_stats(),
                "route_stats": self.rag_system.query_router.get_route_statistics(),
                "system_info": {
                    "timestamp": str(datetime.now()),
                    "status": "running"
                }
            }
            return jsonify(stats)
            
        except Exception as e:
            logger.error(f"统计API错误: {e}")
            return jsonify({"error": str(e)}), 500
