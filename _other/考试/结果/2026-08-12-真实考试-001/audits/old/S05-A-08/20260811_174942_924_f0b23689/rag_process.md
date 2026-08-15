# RAG Process

audit_id: 20260811_174942_924_f0b23689
timestamp: 2026-08-11T17:49:42.925
## Request
- original_query: 虾适合搭配什么蔬菜？
- original_query_hash: 7f746847edc889e2
- session_id: 2026-08-12-真实考试-001:old:S05-A-08
- request_mode: stream
- request_start: 2026-08-11T17:49:42.925
- evaluation_sample_id: 20260811_174942_924_f0b23689
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:49:42.925
- end: 2026-08-11T17:49:42.925
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:49:42.926
- end: 2026-08-11T17:49:42.926
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 10
- enhanced_query_length: 10
- enhanced_query_hash: 7f746847edc889e2

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:49:42.926
- end: 2026-08-11T17:49:42.926
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 10
- analysis_input_query_hash: 7f746847edc889e2
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:49:42.926
- end: 2026-08-11T17:49:52.022
- duration_ms: 9095
- analysis_mode: llm
- query_complexity: 0.28
- relationship_intensity: 0.52
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询是围绕“虾”与“蔬菜”之间适宜搭配关系的直接信息查找，目标明确，通常可通过菜谱、营养搭配知识或烹饪经验类文档直接检索得到答案。虽存在实体间的搭配关系，但不涉及多跳推理、复杂因果链或多方案严格对比，因此适合采用hybrid_traditional进行关键词与语义混合检索。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 116, 'graph_rag_count': 11, 'total_queries': 127}
- route_stats_after: {'traditional_count': 117, 'graph_rag_count': 11, 'total_queries': 128}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['虾', '西兰花', '芦笋', '荷兰豆', '玉米', '胡萝卜', '黄瓜', '番茄', '娃娃菜', '菠菜']
- topic_keywords: ['食材搭配', '荤素搭配', '营养均衡', '海鲜料理', '清淡']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5789

## Hybrid Branch Status / entity_level
- keywords: ['虾', '西兰花', '芦笋', '荷兰豆', '玉米', '胡萝卜', '黄瓜', '番茄', '娃娃菜', '菠菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 1
- duration_ms: 88

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 535

## Hybrid Branch Status / topic_level
- keywords: ['食材搭配', '荤素搭配', '营养均衡', '海鲜料理', '清淡']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 3875

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 22
- duplicate_count: 8

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 3
- doc_names: ['揭秘食材搭配的智慧：这些食物不宜同食']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 15068
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '通用知识': 1, '烹饪技巧': 1, 'Recipe': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24754
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:49:42.926
- end: 2026-08-11T17:50:16.777
- duration_ms: 33850
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4245
- retrieval_levels: ['', 'context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion', 'vector_enhanced']
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
- chunk_count: 221
- redacted_field: 6887
- total_duration_ms: 11390
- fallback_used: False

## Final Output
- answer_chars: 273
- answer_hash: dd17e4ba988d8e34
- success: True

## Request Complete
- request_end: 2026-08-11T17:50:28.183
- request_duration_ms: 45258
- success: True
- final_source: generation

