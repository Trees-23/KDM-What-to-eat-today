# RAG Process

audit_id: 20260811_180232_330_aff128ad
timestamp: 2026-08-11T18:02:32.333
## Request
- original_query: 想吃带汤的家常菜，别太难。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: 21a5b9a9e911290e
- session_id: 2026-08-12-真实考试-001:old:S06-A-05
- request_mode: stream
- request_start: 2026-08-11T18:02:32.333
- evaluation_sample_id: 20260811_180232_330_aff128ad
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:02:32.335
- end: 2026-08-11T18:02:32.335
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:02:32.335
- end: 2026-08-11T18:02:32.335
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 32
- enhanced_query_length: 32
- enhanced_query_hash: 21a5b9a9e911290e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:02:32.336
- end: 2026-08-11T18:02:32.336
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 32
- analysis_input_query_hash: 21a5b9a9e911290e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:02:32.337
- end: 2026-08-11T18:02:47.214
- duration_ms: 14876
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询不是针对某一道明确菜品的信息查找，而是需要在知识库菜谱中按多个条件进行筛选和排序：菜品需“带汤”、属于或适合作为“家常菜”、且制作难度“别太难”。这属于中等复杂度的约束匹配与候选比较任务。查询中不存在需要追溯多层实体关系的复杂知识网络，也不需要历史、地域或食材关系的多跳推理；主要需要对检索到的候选菜谱进行属性过滤和难度、汤汁特征、家常适配性的对比排序。因此适合采用 hybrid_traditional，通过关键词/语义检索召回“汤菜、炖菜、煮菜、家常菜”等候选，再结合菜谱难度、步骤数、烹饪时长等结构化字段进行重排，并基于匹配条件说明推荐依据。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 122, 'graph_rag_count': 32, 'total_queries': 154}
- route_stats_after: {'traditional_count': 123, 'graph_rag_count': 32, 'total_queries': 155}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['番茄鸡蛋汤', '紫菜蛋花汤', '豆腐青菜汤', '冬瓜虾皮汤', '丝瓜鸡蛋汤', '鸡蛋', '豆腐', '番茄', '青菜', '紫菜']
- topic_keywords: ['带汤菜', '家常菜', '简单易做', '快手菜', '汤菜', '清淡']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6366

## Hybrid Branch Status / entity_level
- keywords: ['番茄鸡蛋汤', '紫菜蛋花汤', '豆腐青菜汤', '冬瓜虾皮汤', '丝瓜鸡蛋汤', '鸡蛋', '豆腐', '番茄', '青菜', '紫菜']
- requested_k: 10
- actual_count: 5
- fallback_count: 0
- duration_ms: 41

## Hybrid Branch Status / topic_level
- keywords: ['带汤菜', '家常菜', '简单易做', '快手菜', '汤菜', '清淡']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 61

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 441

## Hybrid Branch Summary
- entity_count: 5
- topic_count: 8
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 20
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 4
- expanded_count: 9
- doc_names: ['去腥', '揭秘食材搭配的智慧：这些食物不宜同食']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 21
- duration_ms: 17348
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'通用知识': 1, '主食': 1, '烹饪技巧': 1, '荤菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 姜葱捞鸡
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24193
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:02:32.337
- end: 2026-08-11T18:03:11.411
- duration_ms: 39073
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3275
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 1
- redacted_field: 6465
- total_duration_ms: 6469
- fallback_used: False

## Final Output
- answer_chars: 321
- answer_hash: 79e5b300ed730472
- success: True

## Request Complete
- request_end: 2026-08-11T18:03:17.898
- request_duration_ms: 45564
- success: True
- final_source: generation

