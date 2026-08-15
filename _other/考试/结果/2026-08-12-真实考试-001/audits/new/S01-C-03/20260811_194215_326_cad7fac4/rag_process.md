# RAG Process

audit_id: 20260811_194215_326_cad7fac4
timestamp: 2026-08-11T19:42:15.327
## Request
- original_query: 我只要知识库能证明的牛奶燕麦做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 51bed27bd3e54479
- session_id: 2026-08-12-真实考试-001:new:S01-C-03
- request_mode: stream
- request_start: 2026-08-11T19:42:15.327
- evaluation_sample_id: 20260811_194215_326_cad7fac4
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:42:15.327
- end: 2026-08-11T19:42:15.327
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:42:15.328
- end: 2026-08-11T19:42:15.328
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 51bed27bd3e54479

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:42:15.334
- end: 2026-08-11T19:42:15.334
- duration_ms: 0
- entity_id: 201000644
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:42:15.334
- end: 2026-08-11T19:42:15.334
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:42:15.334
- end: 2026-08-11T19:42:15.334
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 51bed27bd3e54479
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:42:15.334
- end: 2026-08-11T19:42:22.761
- duration_ms: 7426
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询的核心是检索知识库中可直接支撑“牛奶燕麦做法”的证据，并严格限制回答范围：仅输出有引用依据的步骤，不补充无引用的替代方案或营养结论。主要明确实体为“牛奶”和“燕麦”，二者构成简单的食材—做法关系。该任务不要求多跳推理、因果分析或实体关系网络发现，但需要较强的证据对齐、出处过滤和引用覆盖校验，因此适合使用 hybrid_traditional 进行关键词/语义混合检索，并依据检索证据生成受约束答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 20, 'graph_rag_count': 0, 'total_queries': 20}
- route_stats_after: {'traditional_count': 21, 'graph_rag_count': 0, 'total_queries': 21}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['牛奶', '燕麦', '牛奶燕麦']
- topic_keywords: ['做法', '知识库证据', '引用', '信息可信度']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4630

## Hybrid Branch Status / entity_level
- keywords: ['牛奶', '燕麦', '牛奶燕麦']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 25

## Hybrid Branch Status / topic_level
- keywords: ['做法', '知识库证据', '引用', '信息可信度']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 71

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 732

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 8
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 17
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
- candidate_count: 18
- duration_ms: 13372
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'早餐': 2, '烹饪技巧': 2, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18754
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:42:15.334
- end: 2026-08-11T19:42:41.516
- duration_ms: 26182
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2391
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
- chunk_count: 441
- redacted_field: 1885
- total_duration_ms: 9842
- fallback_used: False

## Final Output
- answer_chars: 546
- answer_hash: 2b0e77fc4e69ab39
- success: True

## Request Complete
- request_end: 2026-08-11T19:42:51.381
- request_duration_ms: 36053
- success: True
- final_source: generation

