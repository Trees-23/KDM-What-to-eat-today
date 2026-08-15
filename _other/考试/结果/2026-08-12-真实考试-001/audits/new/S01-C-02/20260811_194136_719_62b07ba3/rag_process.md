# RAG Process

audit_id: 20260811_194136_719_62b07ba3
timestamp: 2026-08-11T19:41:36.729
## Request
- original_query: 我只要知识库能证明的炸酱面做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: d0798846537321a5
- session_id: 2026-08-12-真实考试-001:new:S01-C-02
- request_mode: stream
- request_start: 2026-08-11T19:41:36.730
- evaluation_sample_id: 20260811_194136_719_62b07ba3
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:41:36.730
- end: 2026-08-11T19:41:36.730
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:41:36.730
- end: 2026-08-11T19:41:36.730
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 34
- enhanced_query_length: 34
- enhanced_query_hash: d0798846537321a5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:41:36.735
- end: 2026-08-11T19:41:36.735
- duration_ms: 0
- entity_id: 201004135
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:41:36.735
- end: 2026-08-11T19:41:36.735
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:41:36.735
- end: 2026-08-11T19:41:36.735
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 34
- analysis_input_query_hash: d0798846537321a5
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:41:36.736
- end: 2026-08-11T19:41:47.030
- duration_ms: 10294
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是定位“炸酱面做法”相关知识库内容，并严格执行证据约束：仅输出能被检索文档直接支持的步骤、配料和结论，同时排除无引用的替代方案及营养结论。它不要求探索多实体关系网络、因果解释或跨领域知识发现，因此适合采用 hybrid_traditional，通过关键词检索、语义召回、文档重排序和逐条引用校验完成。需要有限推理，主要是证据归属与回答边界控制；不需要多跳推理、因果分析或对比分析。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 19, 'graph_rag_count': 0, 'total_queries': 19}
- route_stats_after: {'traditional_count': 20, 'graph_rag_count': 0, 'total_queries': 20}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['炸酱面']
- topic_keywords: ['做法', '知识库证据', '引用依据']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3865

## Hybrid Branch Status / entity_level
- keywords: ['炸酱面']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 11

## Hybrid Branch Status / topic_level
- keywords: ['做法', '知识库证据', '引用依据']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 47

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 516

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
- doc_names: ['去腥', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 16955
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'Recipe': 1, '主食': 2, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21364
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:41:36.736
- end: 2026-08-11T19:42:08.395
- duration_ms: 31659
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2150
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
- chunk_count: 290
- redacted_field: 1937
- total_duration_ms: 6909
- fallback_used: False

## Final Output
- answer_chars: 425
- answer_hash: 4ada57f16efd1abf
- success: True

## Request Complete
- request_end: 2026-08-11T19:42:15.316
- request_duration_ms: 38586
- success: True
- final_source: generation

