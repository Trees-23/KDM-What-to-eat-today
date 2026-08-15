# RAG Process

audit_id: 20260811_194055_317_3e1a4e7f
timestamp: 2026-08-11T19:40:55.318
## Request
- original_query: 我只要知识库能证明的手工水饺做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: f595486f4bf2239b
- session_id: 2026-08-12-真实考试-001:new:S01-C-01
- request_mode: stream
- request_start: 2026-08-11T19:40:55.318
- evaluation_sample_id: 20260811_194055_317_3e1a4e7f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:40:55.319
- end: 2026-08-11T19:40:55.319
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:40:55.319
- end: 2026-08-11T19:40:55.319
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: f595486f4bf2239b

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:40:55.324
- end: 2026-08-11T19:40:55.324
- duration_ms: 0
- entity_id: 201004017
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:40:55.324
- end: 2026-08-11T19:40:55.324
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:40:55.324
- end: 2026-08-11T19:40:55.324
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: f595486f4bf2239b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:40:55.324
- end: 2026-08-11T19:41:03.329
- duration_ms: 8004
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.35
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是检索“手工水饺做法”这一具体主题，并严格限定答案只能使用知识库中可引用、可验证的内容。其难点主要在于证据约束、引用对齐和未被检索证据支持内容的排除，而非多实体关系发现或复杂图谱推理。无需多跳推理、因果分析或对比分析；适合采用关键词/语义混合检索后进行来源过滤与引用覆盖校验。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 18, 'graph_rag_count': 0, 'total_queries': 18}
- route_stats_after: {'traditional_count': 19, 'graph_rag_count': 0, 'total_queries': 19}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['手工水饺']
- topic_keywords: ['水饺做法', '知识库依据', '引用']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4651

## Hybrid Branch Status / topic_level
- keywords: ['水饺做法', '知识库依据', '引用']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 11

## Hybrid Branch Status / entity_level
- keywords: ['手工水饺']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 12

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 597

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 6
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['焯水', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 7
- duration_ms: 11465
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 1, '半成品': 1, '早餐': 1, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 16750
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:40:55.324
- end: 2026-08-11T19:41:20.080
- duration_ms: 24755
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3553
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
- chunk_count: 694
- redacted_field: 1820
- total_duration_ms: 16612
- fallback_used: False

## Final Output
- answer_chars: 913
- answer_hash: a32df712f3ee0396
- success: True

## Request Complete
- request_end: 2026-08-11T19:41:36.710
- request_duration_ms: 41391
- success: True
- final_source: generation

