# RAG Process

audit_id: 20260811_194251_398_922ed9f1
timestamp: 2026-08-11T19:42:51.401
## Request
- original_query: 我只要知识库能证明的鸡蛋三明治做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 5f43ed0e16aec2a4
- session_id: 2026-08-12-真实考试-001:new:S01-C-04
- request_mode: stream
- request_start: 2026-08-11T19:42:51.402
- evaluation_sample_id: 20260811_194251_398_922ed9f1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:42:51.403
- end: 2026-08-11T19:42:51.403
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:42:51.403
- end: 2026-08-11T19:42:51.403
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 5f43ed0e16aec2a4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:42:51.412
- end: 2026-08-11T19:42:51.412
- duration_ms: 0
- entity_id: 201000730
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:42:51.413
- end: 2026-08-11T19:42:51.413
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:42:51.413
- end: 2026-08-11T19:42:51.413
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 5f43ed0e16aec2a4
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:42:51.413
- end: 2026-08-11T19:42:58.968
- duration_ms: 7555
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.2
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 核心任务是检索知识库中关于“鸡蛋三明治做法”的直接证据，并仅基于可引用内容组织答案。查询不涉及多实体间的复杂关系网络、因果解释或方案对比，因此不需要图谱式多跳推理。其主要难点是证据约束与回答边界控制：需要逐条核验做法是否有知识库来源支持，排除无引用的替代方案、常识补全和营养结论。适合采用 hybrid_traditional，通过关键词/语义检索召回食谱步骤，再进行引用覆盖校验与证据过滤。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 21, 'graph_rag_count': 0, 'total_queries': 21}
- route_stats_after: {'traditional_count': 22, 'graph_rag_count': 0, 'total_queries': 22}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸡蛋三明治', '鸡蛋']
- topic_keywords: ['食谱做法', '知识库依据', '引用', '证据支持']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4105

## Hybrid Branch Status / topic_level
- keywords: ['食谱做法', '知识库依据', '引用', '证据支持']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 14

## Hybrid Branch Status / entity_level
- keywords: ['鸡蛋三明治', '鸡蛋']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 28

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 327

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 0
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 11
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['炒/煎', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 12
- duration_ms: 14373
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'早餐': 2, '主食': 2, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18842
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:42:51.413
- end: 2026-08-11T19:43:17.811
- duration_ms: 26398
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1965
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
- chunk_count: 174
- redacted_field: 6632
- total_duration_ms: 10684
- fallback_used: False

## Final Output
- answer_chars: 253
- answer_hash: 4372b162cbed3948
- success: True

## Request Complete
- request_end: 2026-08-11T19:43:28.521
- request_duration_ms: 37119
- success: True
- final_source: generation

