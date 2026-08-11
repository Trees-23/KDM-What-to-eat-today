# RAG Process

audit_id: 20260811_182803_338_335ce50f
timestamp: 2026-08-11T18:28:03.341
## Request
- original_query: 想吃豆腐类川菜又希望有味道。请推荐几个可考虑的菜。
- original_query_hash: 21ca442f9a501683
- session_id: 2026-08-12-真实考试-001:old:S07-A-09
- request_mode: stream
- request_start: 2026-08-11T18:28:03.342
- evaluation_sample_id: 20260811_182803_338_335ce50f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:28:03.342
- end: 2026-08-11T18:28:03.342
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:28:03.343
- end: 2026-08-11T18:28:03.343
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: 21ca442f9a501683

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:28:03.343
- end: 2026-08-11T18:28:03.343
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: 21ca442f9a501683
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:28:03.343
- end: 2026-08-11T18:28:10.994
- duration_ms: 7650
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.56
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带条件的菜品推荐任务，核心约束为“豆腐类”“川菜”和“有味道（通常可理解为麻辣、香辣、酱香或浓郁调味）”。需要从川菜菜品集合中筛选以豆腐为主要或重要食材、且风味较突出的候选菜，并可按麻辣度、肉类搭配或口味浓郁程度进行轻量排序。查询存在菜系、食材和口味偏好之间的关联匹配，但不涉及复杂知识网络、历史因果或多层实体关系推演，因此适合使用关键词检索、菜品标签过滤和语义召回相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 154, 'graph_rag_count': 33, 'total_queries': 187}
- route_stats_after: {'traditional_count': 155, 'graph_rag_count': 33, 'total_queries': 188}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['豆腐', '麻婆豆腐', '家常豆腐', '鱼香豆腐', '熊掌豆腐', '豆花']
- topic_keywords: ['川菜', '豆腐类菜', '麻辣', '香辣', '入味', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6297

## Hybrid Branch Status / entity_level
- keywords: ['豆腐', '麻婆豆腐', '家常豆腐', '鱼香豆腐', '熊掌豆腐', '豆花']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 23

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '豆腐类菜', '麻辣', '香辣', '入味', '下饭菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 81

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 641

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 18
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 5
- doc_names: ['如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 19
- duration_ms: 11766
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 1, '素菜': 2, '通用知识': 1, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 葱煎豆腐
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18726
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:28:03.343
- end: 2026-08-11T18:28:29.722
- duration_ms: 26378
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1697
- retrieval_levels: ['', 'context_expansion']
- search_types: ['technique_expansion', 'vector_enhanced']
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
- chunk_count: 390
- redacted_field: 4397
- total_duration_ms: 12001
- fallback_used: False

## Final Output
- answer_chars: 483
- answer_hash: 0a0bc6c934e75337
- success: True

## Request Complete
- request_end: 2026-08-11T18:28:41.745
- request_duration_ms: 38403
- success: True
- final_source: generation

