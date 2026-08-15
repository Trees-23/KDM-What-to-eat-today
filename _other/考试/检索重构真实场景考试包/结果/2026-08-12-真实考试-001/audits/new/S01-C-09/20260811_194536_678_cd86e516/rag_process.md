# RAG Process

audit_id: 20260811_194536_678_cd86e516
timestamp: 2026-08-11T19:45:36.679
## Request
- original_query: 我只要知识库能证明的麻婆豆腐做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 919b2a12d98744e3
- session_id: 2026-08-12-真实考试-001:new:S01-C-09
- request_mode: stream
- request_start: 2026-08-11T19:45:36.680
- evaluation_sample_id: 20260811_194536_678_cd86e516
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:45:36.680
- end: 2026-08-11T19:45:36.680
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:45:36.681
- end: 2026-08-11T19:45:36.681
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 919b2a12d98744e3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:45:36.686
- end: 2026-08-11T19:45:36.686
- duration_ms: 0
- entity_id: 201003481
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:45:36.686
- end: 2026-08-11T19:45:36.686
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:45:36.686
- end: 2026-08-11T19:45:36.686
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 919b2a12d98744e3
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:45:36.686
- end: 2026-08-11T19:45:43.311
- duration_ms: 6625
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.25
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 查询的核心是查找“麻婆豆腐做法”，并施加严格的证据约束：所有输出内容必须能够由知识库检索结果直接证明，且不得补充无引用的替代方案或营养结论。它不涉及多实体之间的复杂关联、因果链或知识发现，重点在于高精度检索、段落级证据定位、引用覆盖校验与生成约束。明确实体包括“麻婆豆腐”和“知识库（作为证据来源）”。因此适合采用 hybrid_traditional，通过关键词检索、语义召回、重排序和引用绑定来返回有据可查的做法内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 26, 'graph_rag_count': 0, 'total_queries': 26}
- route_stats_after: {'traditional_count': 27, 'graph_rag_count': 0, 'total_queries': 27}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['麻婆豆腐']
- topic_keywords: ['川菜', '做法', '知识库证据', '引用', '可验证性']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2698

## Hybrid Branch Status / entity_level
- keywords: ['麻婆豆腐']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 11

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '做法', '知识库证据', '引用', '可验证性']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 68

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 673

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 10
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 19
- duplicate_count: 2

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
- candidate_count: 20
- duration_ms: 13208
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 1, '主食': 1, '烹饪技巧': 1, '素菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 葱煎豆腐
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 16597
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:45:36.686
- end: 2026-08-11T19:45:59.910
- duration_ms: 23223
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1727
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
- chunk_count: 191
- redacted_field: 4738
- total_duration_ms: 9218
- fallback_used: False

## Final Output
- answer_chars: 270
- answer_hash: 9a1a35c37c53e13a
- success: True

## Request Complete
- request_end: 2026-08-11T19:46:09.157
- request_duration_ms: 32477
- success: True
- final_source: generation

