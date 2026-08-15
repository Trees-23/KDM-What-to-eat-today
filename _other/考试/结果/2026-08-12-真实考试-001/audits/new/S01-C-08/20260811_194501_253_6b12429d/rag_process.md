# RAG Process

audit_id: 20260811_194501_253_6b12429d
timestamp: 2026-08-11T19:45:01.254
## Request
- original_query: 我只要知识库能证明的杨枝甘露做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 9dc9bd5f3c7a6a4b
- session_id: 2026-08-12-真实考试-001:new:S01-C-08
- request_mode: stream
- request_start: 2026-08-11T19:45:01.265
- evaluation_sample_id: 20260811_194501_253_6b12429d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:45:01.267
- end: 2026-08-11T19:45:01.267
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:45:01.268
- end: 2026-08-11T19:45:01.268
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 9dc9bd5f3c7a6a4b

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:45:01.279
- end: 2026-08-11T19:45:01.279
- duration_ms: 0
- entity_id: 201001206
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:45:01.279
- end: 2026-08-11T19:45:01.279
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:45:01.279
- end: 2026-08-11T19:45:01.279
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 9dc9bd5f3c7a6a4b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:45:01.280
- end: 2026-08-11T19:45:08.789
- duration_ms: 7508
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.2
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 查询核心是获取“杨枝甘露”的做法，属于单一菜品实体的直接信息检索；额外要求是答案必须由知识库证据支持，并禁止输出无引用的替代方案或营养结论。这需要进行检索结果的证据筛选、引用对齐和生成约束，但不需要多跳推理、因果分析或复杂实体关系建模。适合采用 hybrid_traditional，通过关键词/语义混合检索定位做法步骤，再仅基于可引用片段生成答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 25, 'graph_rag_count': 0, 'total_queries': 25}
- route_stats_after: {'traditional_count': 26, 'graph_rag_count': 0, 'total_queries': 26}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['杨枝甘露']
- topic_keywords: ['做法', '知识库依据', '引用', '证据支持']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3338

## Hybrid Branch Status / entity_level
- keywords: ['杨枝甘露']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 14

## Hybrid Branch Status / topic_level
- keywords: ['做法', '知识库依据', '引用', '证据支持']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 74

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 444

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 8
- vector_count: 10
- origin_len: 19

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 19
- after_count: 17
- duplicate_count: 2

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
- candidate_count: 18
- duration_ms: 16828
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'饮料': 1, '烹饪技巧': 2, '主食': 2}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20633
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:45:01.280
- end: 2026-08-11T19:45:29.423
- duration_ms: 28142
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2435
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 257
- redacted_field: 1791
- total_duration_ms: 7218
- fallback_used: False

## Final Output
- answer_chars: 330
- answer_hash: 008e818cfce7f508
- success: True

## Request Complete
- request_end: 2026-08-11T19:45:36.661
- request_duration_ms: 35396
- success: True
- final_source: generation

