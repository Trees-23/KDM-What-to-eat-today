# RAG Process

audit_id: 20260811_193622_468_afff5dbd
timestamp: 2026-08-11T19:36:22.468
## Request
- original_query: 酸辣土豆丝从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: ac38e5e62aba18df
- session_id: 2026-08-12-真实考试-001:new:S01-B-04
- request_mode: stream
- request_start: 2026-08-11T19:36:22.469
- evaluation_sample_id: 20260811_193622_468_afff5dbd
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:36:22.470
- end: 2026-08-11T19:36:22.470
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:36:22.470
- end: 2026-08-11T19:36:22.470
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: ac38e5e62aba18df

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:36:22.476
- end: 2026-08-11T19:36:22.476
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:36:22.476
- end: 2026-08-11T19:36:22.476
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:36:22.476
- end: 2026-08-11T19:36:22.476
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: ac38e5e62aba18df
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:36:22.476
- end: 2026-08-11T19:36:31.096
- duration_ms: 8620
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询是针对“酸辣土豆丝”这一明确菜品的标准做法查询，核心需求是从备料、处理食材、炒制到出锅的顺序化步骤信息，并要求以知识库中的做法为准。虽然包含烹饪流程中的食材—操作—时间/火候等轻度关联，但不需要跨文档多跳推理、因果归因或方案对比。明确实体主要包括“酸辣土豆丝”（菜品）和“土豆”（食材）；“酸”“辣”更适合作为口味属性而非独立实体。适合通过关键词、菜品别名、步骤字段及语义召回进行混合检索，再按知识库原始步骤组织回答。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 12, 'graph_rag_count': 0, 'total_queries': 12}
- route_stats_after: {'traditional_count': 13, 'graph_rag_count': 0, 'total_queries': 13}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['酸辣土豆丝', '土豆', '青椒', '红椒', '干辣椒', '蒜', '白醋', '米醋']
- topic_keywords: ['酸辣', '家常菜', '快手菜', '炒菜', '烹饪技巧', '火候', '爽脆']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3372

## Hybrid Branch Status / entity_level
- keywords: ['酸辣土豆丝', '土豆', '青椒', '红椒', '干辣椒', '蒜', '白醋', '米醋']
- requested_k: 10
- actual_count: 10
- fallback_count: 2
- duration_ms: 72

## Hybrid Branch Status / topic_level
- keywords: ['酸辣', '家常菜', '快手菜', '炒菜', '烹饪技巧', '火候', '爽脆']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 79

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 685

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
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 25
- duration_ms: 19063
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '荤菜': 2, '主食,凉菜': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23139
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:36:22.476
- end: 2026-08-11T19:36:54.236
- duration_ms: 31760
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3145
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
- chunk_count: 365
- redacted_field: 1853
- total_duration_ms: 7989
- fallback_used: False

## Final Output
- answer_chars: 491
- answer_hash: a3f2f402fc3623b9
- success: True

## Request Complete
- request_end: 2026-08-11T19:37:02.245
- request_duration_ms: 39776
- success: True
- final_source: generation

