# RAG Process

audit_id: 20260811_194328_532_5e5f67dd
timestamp: 2026-08-11T19:43:28.532
## Request
- original_query: 我只要知识库能证明的西红柿鸡蛋汤做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 5ea0bfc40944e677
- session_id: 2026-08-12-真实考试-001:new:S01-C-05
- request_mode: stream
- request_start: 2026-08-11T19:43:28.532
- evaluation_sample_id: 20260811_194328_532_5e5f67dd
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:43:28.533
- end: 2026-08-11T19:43:28.533
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:43:28.534
- end: 2026-08-11T19:43:28.534
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: 5ea0bfc40944e677

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:43:28.539
- end: 2026-08-11T19:43:28.539
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:43:28.539
- end: 2026-08-11T19:43:28.539
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:43:28.539
- end: 2026-08-11T19:43:28.539
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: 5ea0bfc40944e677
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:43:28.539
- end: 2026-08-11T19:43:36.489
- duration_ms: 7950
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.35
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询的核心目标是检索“西红柿鸡蛋汤”的做法，并且要求所有步骤均可由知识库中的引用证据支持，禁止补充无引用的替代方案或营养结论。其主要难点在于证据约束、引用对齐和生成边界控制，而非跨实体的复杂关系发现或多跳图推理。明确实体包括“西红柿”“鸡蛋”“西红柿鸡蛋汤”；“知识库”“引用”属于检索与证据约束条件。推荐使用hybrid_traditional，通过关键词/语义混合召回获取相关菜谱片段，再按来源、步骤完整性与可引用性进行重排序和证据过滤。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 22, 'graph_rag_count': 0, 'total_queries': 22}
- route_stats_after: {'traditional_count': 23, 'graph_rag_count': 0, 'total_queries': 23}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西红柿鸡蛋汤', '西红柿', '鸡蛋']
- topic_keywords: ['烹饪方法', '知识库依据', '引用', '信息可信度']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4347

## Hybrid Branch Status / topic_level
- keywords: ['烹饪方法', '知识库依据', '引用', '信息可信度']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 13

## Hybrid Branch Status / entity_level
- keywords: ['西红柿鸡蛋汤', '西红柿', '鸡蛋']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 25

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 706

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 0
- vector_count: 10
- origin_len: 13

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 13
- after_count: 10
- duplicate_count: 3

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
- candidate_count: 11
- duration_ms: 10185
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'汤类': 2, '素菜': 2, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 番茄牛肉蛋花汤
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 15264
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:43:28.539
- end: 2026-08-11T19:43:51.755
- duration_ms: 23215
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2211
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
- chunk_count: 156
- redacted_field: 4598
- total_duration_ms: 11670
- fallback_used: False

## Final Output
- answer_chars: 213
- answer_hash: 4fb0e3bec781e7fd
- success: True

## Request Complete
- request_end: 2026-08-11T19:44:03.441
- request_duration_ms: 34908
- success: True
- final_source: generation

