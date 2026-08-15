# RAG Process

audit_id: 20260811_171303_256_35a95145
timestamp: 2026-08-11T17:13:03.260
## Request
- original_query: 我想学使用空气炸锅，它的关键要点和适用场景是什么？
- original_query_hash: 8d25f4cabb4b8d1b
- session_id: 2026-08-12-真实考试-001:old:S03-B-04
- request_mode: stream
- request_start: 2026-08-11T17:13:03.260
- evaluation_sample_id: 20260811_171303_256_35a95145
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:13:03.261
- end: 2026-08-11T17:13:03.261
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:13:03.262
- end: 2026-08-11T17:13:03.262
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: 8d25f4cabb4b8d1b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:13:03.262
- end: 2026-08-11T17:13:03.262
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: 8d25f4cabb4b8d1b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:13:03.263
- end: 2026-08-11T17:13:16.423
- duration_ms: 13160
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.4
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询面向空气炸锅的入门使用，核心是获取操作要点及其与不同食材、烹饪任务之间的适用关系。虽包含“关键要点”和“适用场景”两个信息子任务，需要按食材特性、烹饪目标和设备限制进行归纳，但通常不要求跨多跳知识推理、深层因果链分析或多方案严格对比。明确实体包括“空气炸锅”（厨电设备）、“关键要点”（操作/知识属性）和“适用场景”（烹饪任务或应用场景）。适合采用关键词检索结合语义检索的 hybrid_traditional 策略，以召回操作指南、温度时间建议、安全注意事项和适用食材说明。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 73, 'graph_rag_count': 0, 'total_queries': 73}
- route_stats_after: {'traditional_count': 74, 'graph_rag_count': 0, 'total_queries': 74}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['空气炸锅']
- topic_keywords: ['烹饪技巧', '无油烹饪', '低油脂', '健康饮食', '烘烤', '煎炸', '复热', '快手菜', '火候', '食品安全']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6871

## Hybrid Branch Status / entity_level
- keywords: ['空气炸锅']
- requested_k: 10
- actual_count: 9
- fallback_count: 0
- duration_ms: 142

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '无油烹饪', '低油脂', '健康饮食', '烘烤', '煎炸', '复热', '快手菜', '火候', '食品安全']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 142

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 756

## Hybrid Branch Summary
- entity_count: 9
- topic_count: 10
- vector_count: 10
- origin_len: 29

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 29
- after_count: 21
- duplicate_count: 8

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 22
- duration_ms: 16087
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, 'TechniqueChunk': 2, 'TechniqueDoc': 1, '半成品': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23802
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:13:03.262
- end: 2026-08-11T17:13:40.226
- duration_ms: 36963
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4102
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
- chunk_count: 1472
- redacted_field: 2842
- total_duration_ms: 31799
- fallback_used: False

## Final Output
- answer_chars: 1957
- answer_hash: 4d16a16274561a2a
- success: True

## Request Complete
- request_end: 2026-08-11T17:14:12.052
- request_duration_ms: 68791
- success: True
- final_source: generation

