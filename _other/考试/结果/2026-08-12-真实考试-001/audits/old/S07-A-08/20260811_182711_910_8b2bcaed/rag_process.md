# RAG Process

audit_id: 20260811_182711_910_8b2bcaed
timestamp: 2026-08-11T18:27:11.910
## Request
- original_query: 希望做法简单、吃起来不厚重的川味菜。请推荐几个可考虑的菜。
- original_query_hash: 72467d350533998e
- session_id: 2026-08-12-真实考试-001:old:S07-A-08
- request_mode: stream
- request_start: 2026-08-11T18:27:11.911
- evaluation_sample_id: 20260811_182711_910_8b2bcaed
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:27:11.911
- end: 2026-08-11T18:27:11.911
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:27:11.912
- end: 2026-08-11T18:27:11.912
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 29
- enhanced_query_length: 29
- enhanced_query_hash: 72467d350533998e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:27:11.912
- end: 2026-08-11T18:27:11.912
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 29
- analysis_input_query_hash: 72467d350533998e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:27:11.912
- end: 2026-08-11T18:27:20.752
- duration_ms: 8839
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询属于带多重偏好约束的菜品推荐：用户希望候选菜同时满足“川味”“做法简单”和“口感不厚重”三个条件。主要任务是从川味菜候选中进行属性过滤与排序，而非解释复杂的历史、地理或食材关系网络。需要进行轻量级对比分析，例如区分油重、勾芡重、步骤繁琐的菜与清爽、快手型菜品；不需要多跳推理或因果分析。明确语义实体可归纳为“川味菜”“做法简单”“不厚重/清爽口感”三类，因此适合使用关键词检索结合向量语义检索、标签过滤和排序的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 153, 'graph_rag_count': 33, 'total_queries': 186}
- route_stats_after: {'traditional_count': 154, 'graph_rag_count': 33, 'total_queries': 187}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['凉拌黄瓜', '酸辣土豆丝', '炝炒空心菜', '清炒豌豆尖', '凉拌木耳', '凉拌鸡丝', '花椒', '辣椒', '醋']
- topic_keywords: ['川菜', '川味', '家常菜', '快手菜', '做法简单', '清爽', '低油', '不厚重', '开胃', '凉拌菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8090

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '川味', '家常菜', '快手菜', '做法简单', '清爽', '低油', '不厚重', '开胃', '凉拌菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 42

## Hybrid Branch Status / entity_level
- keywords: ['凉拌黄瓜', '酸辣土豆丝', '炝炒空心菜', '清炒豌豆尖', '凉拌木耳', '凉拌鸡丝', '花椒', '辣椒', '醋']
- requested_k: 10
- actual_count: 10
- fallback_count: 3
- duration_ms: 87

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 450

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 25
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['去腥', '如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 26
- duration_ms: 22274
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '主食': 2, '主食,凉菜': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 酸辣蕨根粉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 30854
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:27:11.912
- end: 2026-08-11T18:27:51.607
- duration_ms: 39694
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1836
- retrieval_levels: ['context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level']
- stream: True
- max_retries: 3
- evidence_bundle: False
- verified_graph_fact_count: 0
- text_evidence_count: 0
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: True
- timeout: 60
- max_retries: 3

## Generation Stream
- status: success
- chunk_count: 332
- redacted_field: 5100
- total_duration_ms: 11694
- fallback_used: False

## Final Output
- answer_chars: 473
- answer_hash: ee944759f1e8e79d
- success: True

## Request Complete
- request_end: 2026-08-11T18:28:03.323
- request_duration_ms: 51412
- success: True
- final_source: generation

