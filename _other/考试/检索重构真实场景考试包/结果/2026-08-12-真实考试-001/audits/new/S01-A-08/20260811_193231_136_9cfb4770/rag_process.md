# RAG Process

audit_id: 20260811_193231_136_9cfb4770
timestamp: 2026-08-11T19:32:31.137
## Request
- original_query: 请给出葱烧海参的完整做法，包括主要食材和步骤。
- original_query_hash: ce6dd14fc4c01f5a
- session_id: 2026-08-12-真实考试-001:new:S01-A-08
- request_mode: stream
- request_start: 2026-08-11T19:32:31.137
- evaluation_sample_id: 20260811_193231_136_9cfb4770
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:32:31.138
- end: 2026-08-11T19:32:31.138
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:32:31.138
- end: 2026-08-11T19:32:31.138
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: ce6dd14fc4c01f5a

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:32:31.148
- end: 2026-08-11T19:32:31.148
- duration_ms: 0
- entity_id: 201000365
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:32:31.148
- end: 2026-08-11T19:32:31.148
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:32:31.148
- end: 2026-08-11T19:32:31.148
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: ce6dd14fc4c01f5a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:32:31.148
- end: 2026-08-11T19:32:36.771
- duration_ms: 5622
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是面向单一道菜“葱烧海参”的直接做法检索，明确要求主要食材和制作步骤，属于结构化事实与流程信息获取。查询中的核心实体为“葱烧海参”和“海参（主要原料）”，食材与步骤之间仅存在简单的制作流程关联，不需要多跳推理、因果分析或跨对象对比分析。适合使用关键词检索与语义检索结合的 hybrid_traditional 策略，以召回权威菜谱、烹饪教程等内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 7, 'graph_rag_count': 0, 'total_queries': 7}
- route_stats_after: {'traditional_count': 8, 'graph_rag_count': 0, 'total_queries': 8}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['葱烧海参', '海参', '大葱', '高汤', '蚝油', '生抽', '料酒', '淀粉']
- topic_keywords: ['鲁菜', '葱香', '海鲜', '宴客菜', '烹饪步骤', '火候', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3455

## Hybrid Branch Status / entity_level
- keywords: ['葱烧海参', '海参', '大葱', '高汤', '蚝油', '生抽', '料酒', '淀粉']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 60

## Hybrid Branch Status / topic_level
- keywords: ['鲁菜', '葱香', '海鲜', '宴客菜', '烹饪步骤', '火候', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 78

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 552

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 22
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 22
- duration_ms: 16244
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '调料': 1, '主食': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20268
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:32:31.148
- end: 2026-08-11T19:32:57.041
- duration_ms: 25892
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2126
- retrieval_levels: ['', 'topic']
- search_types: ['topic_level', 'vector_enhanced']
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
- chunk_count: 445
- redacted_field: 3677
- total_duration_ms: 13107
- fallback_used: False

## Final Output
- answer_chars: 603
- answer_hash: be3f986b3666fe1b
- success: True

## Request Complete
- request_end: 2026-08-11T19:33:10.167
- request_duration_ms: 39029
- success: True
- final_source: generation

