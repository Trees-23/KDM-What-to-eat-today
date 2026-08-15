# RAG Process

audit_id: 20260811_193111_951_90bc03bb
timestamp: 2026-08-11T19:31:11.952
## Request
- original_query: 请给出蒜蓉虾的完整做法，包括主要食材和步骤。
- original_query_hash: 2477a9c219561c16
- session_id: 2026-08-12-真实考试-001:new:S01-A-06
- request_mode: stream
- request_start: 2026-08-11T19:31:11.952
- evaluation_sample_id: 20260811_193111_951_90bc03bb
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:31:11.953
- end: 2026-08-11T19:31:11.953
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:31:11.954
- end: 2026-08-11T19:31:11.954
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 22
- enhanced_query_length: 22
- enhanced_query_hash: 2477a9c219561c16

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:31:12.025
- end: 2026-08-11T19:31:12.025
- duration_ms: 0
- entity_id: 201000386
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:31:12.025
- end: 2026-08-11T19:31:12.025
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:31:12.026
- end: 2026-08-11T19:31:12.026
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 22
- analysis_input_query_hash: 2477a9c219561c16
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:31:12.026
- end: 2026-08-11T19:31:16.960
- duration_ms: 4933
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.25
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对单一道菜品“蒜蓉虾”制作方法的直接信息查找，目标明确为获取主要食材和操作步骤。虽然食材与步骤之间存在基本的配方和流程关联，但不涉及跨领域、多实体的复杂关系网络，也无需多跳推理、因果分析或方案对比。明确实体主要包括“蒜蓉虾”（菜品）和“虾”（食材）；“蒜蓉”可视为菜品名称中的核心调味/食材成分。适合使用hybrid_traditional，通过关键词检索、菜谱文档召回和排序即可满足需求。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 5, 'graph_rag_count': 0, 'total_queries': 5}
- route_stats_after: {'traditional_count': 6, 'graph_rag_count': 0, 'total_queries': 6}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒜蓉虾', '虾', '大蒜', '蒜蓉', '食用油', '生抽', '蚝油', '料酒', '盐', '白糖', '葱花']
- topic_keywords: ['家常菜', '海鲜', '蒜香', '烹饪步骤', '调味', '火候', '去腥', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3553

## Hybrid Branch Status / entity_level
- keywords: ['蒜蓉虾', '虾', '大蒜', '蒜蓉', '食用油', '生抽', '蚝油', '料酒', '盐', '白糖', '葱花']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 70

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '海鲜', '蒜香', '烹饪步骤', '调味', '火候', '去腥', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 95

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 603

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 27
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 27
- duration_ms: 24804
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 2, '素菜': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 28982
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:31:12.026
- end: 2026-08-11T19:31:45.944
- duration_ms: 33917
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2287
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
- chunk_count: 244
- redacted_field: 1821
- total_duration_ms: 5833
- fallback_used: False

## Final Output
- answer_chars: 337
- answer_hash: b43fd6c60caaaa3f
- success: True

## Request Complete
- request_end: 2026-08-11T19:31:51.790
- request_duration_ms: 39838
- success: True
- final_source: generation

