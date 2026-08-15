# RAG Process

audit_id: 20260811_193534_682_0a39f94a
timestamp: 2026-08-11T19:35:34.683
## Request
- original_query: 蒜蓉西兰花从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 0198f01ff5511d68
- session_id: 2026-08-12-真实考试-001:new:S01-B-03
- request_mode: stream
- request_start: 2026-08-11T19:35:34.683
- evaluation_sample_id: 20260811_193534_682_0a39f94a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:35:34.684
- end: 2026-08-11T19:35:34.684
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:35:34.685
- end: 2026-08-11T19:35:34.685
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 0198f01ff5511d68

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:35:34.689
- end: 2026-08-11T19:35:34.689
- duration_ms: 0
- entity_id: 201005129
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:35:34.689
- end: 2026-08-11T19:35:34.689
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:35:34.689
- end: 2026-08-11T19:35:34.689
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 0198f01ff5511d68
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:35:34.690
- end: 2026-08-11T19:35:40.818
- duration_ms: 6128
- analysis_mode: llm
- query_complexity: 0.28
- relationship_intensity: 0.22
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询是面向单一道菜“蒜蓉西兰花”的流程型做法检索，核心需求是从知识库中定位对应菜谱，并按备料、预处理、炒制到出锅的顺序返回步骤。虽包含“蒜蓉”和“西兰花”两个食材实体，但二者构成固定菜品名称，关系明确且不需要跨菜谱、多跳关联、因果解释或方案对比。适合采用关键词检索与语义检索结合的 hybrid_traditional 策略，以“蒜蓉西兰花”“备料”“做法”“出锅”等字段召回并排序知识库中的标准菜谱。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 11, 'graph_rag_count': 0, 'total_queries': 11}
- route_stats_after: {'traditional_count': 12, 'graph_rag_count': 0, 'total_queries': 12}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒜蓉西兰花', '西兰花', '大蒜', '蒜蓉']
- topic_keywords: ['家常菜', '素菜', '快手菜', '烹饪技巧', '焯水', '火候', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8497

## Hybrid Branch Status / entity_level
- keywords: ['蒜蓉西兰花', '西兰花', '大蒜', '蒜蓉']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 41

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '素菜', '快手菜', '烹饪技巧', '焯水', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 70

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 573

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 10
- vector_count: 10
- origin_len: 24

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 24
- after_count: 20
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 21
- duration_ms: 24455
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '烹饪技巧': 2, '荤菜': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 33546
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:35:34.689
- end: 2026-08-11T19:36:14.366
- duration_ms: 39676
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3355
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
- chunk_count: 281
- redacted_field: 2290
- total_duration_ms: 8072
- fallback_used: False

## Final Output
- answer_chars: 387
- answer_hash: e0ba1a02117f32b6
- success: True

## Request Complete
- request_end: 2026-08-11T19:36:22.457
- request_duration_ms: 47773
- success: True
- final_source: generation

