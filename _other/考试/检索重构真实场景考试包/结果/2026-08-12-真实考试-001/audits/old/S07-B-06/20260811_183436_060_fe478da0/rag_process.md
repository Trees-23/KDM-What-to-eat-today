# RAG Process

audit_id: 20260811_183436_060_fe478da0
timestamp: 2026-08-11T18:34:36.061
## Request
- original_query: 想吃鱼但不想做得太重口的川菜，有哪些做法比较贴近这种偏好？
- original_query_hash: d49a8eef23956846
- session_id: 2026-08-12-真实考试-001:old:S07-B-06
- request_mode: stream
- request_start: 2026-08-11T18:34:36.062
- evaluation_sample_id: 20260811_183436_060_fe478da0
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:34:36.062
- end: 2026-08-11T18:34:36.062
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:34:36.063
- end: 2026-08-11T18:34:36.063
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 29
- enhanced_query_length: 29
- enhanced_query_hash: d49a8eef23956846

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:34:36.063
- end: 2026-08-11T18:34:36.063
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 29
- analysis_input_query_hash: d49a8eef23956846
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:34:36.063
- end: 2026-08-11T18:34:43.712
- duration_ms: 7649
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.55
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.87
- reasoning: 该查询的核心是将“鱼”和“川菜”两个明确实体，与“口味不重”这一偏好约束进行匹配，筛选出符合条件的烹饪做法。需要进行一定的对比分析，例如区分水煮鱼、麻辣鱼等重麻重辣做法，与清蒸、豆瓣用量较轻或家常风味较淡的做法；但通常不需要跨越多个知识节点的多跳推理，也不涉及复杂因果链。适合通过关键词检索、语义召回和菜谱标签/口味标签过滤的 hybrid_traditional 策略完成。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 161, 'graph_rag_count': 33, 'total_queries': 194}
- route_stats_after: {'traditional_count': 162, 'graph_rag_count': 33, 'total_queries': 195}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鱼', '豆瓣鱼', '家常烧鱼', '泡菜鱼', '酸菜鱼', '清蒸鱼', '葱烧鱼', '藿香鲫鱼']
- topic_keywords: ['川菜', '清淡', '少油', '少辣', '微辣', '鲜香', '鱼类菜肴', '不重口']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4217

## Hybrid Branch Status / entity_level
- keywords: ['鱼', '豆瓣鱼', '家常烧鱼', '泡菜鱼', '酸菜鱼', '清蒸鱼', '葱烧鱼', '藿香鲫鱼']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 82

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '清淡', '少油', '少辣', '微辣', '鲜香', '鱼类菜肴', '不重口']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 86

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 611

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 23
- duplicate_count: 7

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 20113
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, 'Recipe': 1, '素菜': 1, '主食,凉菜': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24963
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:34:36.063
- end: 2026-08-11T18:35:08.677
- duration_ms: 32614
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2195
- retrieval_levels: ['', 'entity', 'topic']
- search_types: ['entity_level', 'topic_level', 'vector_enhanced']
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
- chunk_count: 631
- redacted_field: 2182
- total_duration_ms: 19844
- fallback_used: False

## Final Output
- answer_chars: 758
- answer_hash: ef61f760310e71b7
- success: True

## Request Complete
- request_end: 2026-08-11T18:35:28.549
- request_duration_ms: 52486
- success: True
- final_source: generation

