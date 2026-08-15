# RAG Process

audit_id: 20260811_192813_264_899d202c
timestamp: 2026-08-11T19:28:13.265
## Request
- original_query: 请给出油焖大虾的完整做法，包括主要食材和步骤。
- original_query_hash: baf5975e093e69e6
- session_id: 2026-08-12-真实考试-001:new:S01-A-02
- request_mode: stream
- request_start: 2026-08-11T19:28:13.265
- evaluation_sample_id: 20260811_192813_264_899d202c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:28:13.266
- end: 2026-08-11T19:28:13.266
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:28:13.266
- end: 2026-08-11T19:28:13.266
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: baf5975e093e69e6

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:28:13.476
- end: 2026-08-11T19:28:13.476
- duration_ms: 0
- entity_id: 201000206
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:28:13.477
- end: 2026-08-11T19:28:13.477
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:28:13.477
- end: 2026-08-11T19:28:13.477
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: baf5975e093e69e6
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:28:13.477
- end: 2026-08-11T19:28:19.281
- duration_ms: 5804
- analysis_mode: llm
- query_complexity: 0.22
- relationship_intensity: 0.18
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是针对单一道菜“油焖大虾”的直接制作信息请求，核心目标是获取主要食材及线性烹饪步骤。查询包含“油焖大虾”和“大虾”两个明确实体，分别属于菜品与食材类型；食材、调料和操作步骤之间虽存在基础的组成与顺序关系，但不构成需要跨实体、多跳检索的复杂关系网络。无需因果分析、对比分析或多跳推理，采用基于关键词、菜谱文档与结构化字段匹配的 hybrid_traditional 策略即可有效满足需求。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 1, 'graph_rag_count': 0, 'total_queries': 1}
- route_stats_after: {'traditional_count': 2, 'graph_rag_count': 0, 'total_queries': 2}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['油焖大虾', '大虾', '姜', '蒜', '葱', '料酒', '生抽', '白糖', '盐', '食用油']
- topic_keywords: ['家常菜', '鲁菜', '海鲜', '焖烧', '调味', '火候', '去腥', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3486

## Hybrid Branch Status / entity_level
- keywords: ['油焖大虾', '大虾', '姜', '蒜', '葱', '料酒', '生抽', '白糖', '盐', '食用油']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 79

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '鲁菜', '海鲜', '焖烧', '调味', '火候', '去腥', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 242

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 511

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
- duration_ms: 22658
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 1, '主食': 1, 'Ingredient': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26671
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:28:13.477
- end: 2026-08-11T19:28:45.954
- duration_ms: 32476
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2445
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
- chunk_count: 415
- redacted_field: 1784
- total_duration_ms: 10487
- fallback_used: False

## Final Output
- answer_chars: 552
- answer_hash: 1ddf1d4741cbb908
- success: True

## Request Complete
- request_end: 2026-08-11T19:28:56.463
- request_duration_ms: 43198
- success: True
- final_source: generation

