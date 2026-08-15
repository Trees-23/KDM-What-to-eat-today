# RAG Process

audit_id: 20260811_194609_175_b3aa482b
timestamp: 2026-08-11T19:46:09.176
## Request
- original_query: 我只要知识库能证明的西红柿土豆炖牛肉做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: ab13e4503000d9e4
- session_id: 2026-08-12-真实考试-001:new:S01-C-10
- request_mode: stream
- request_start: 2026-08-11T19:46:09.176
- evaluation_sample_id: 20260811_194609_175_b3aa482b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:46:09.178
- end: 2026-08-11T19:46:09.178
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:46:09.179
- end: 2026-08-11T19:46:09.179
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 39
- enhanced_query_length: 39
- enhanced_query_hash: ab13e4503000d9e4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:46:09.185
- end: 2026-08-11T19:46:09.185
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:46:09.185
- end: 2026-08-11T19:46:09.185
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:46:09.185
- end: 2026-08-11T19:46:09.185
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 39
- analysis_input_query_hash: ab13e4503000d9e4
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:46:09.185
- end: 2026-08-11T19:46:17.969
- duration_ms: 8783
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是查找“西红柿土豆炖牛肉”的可验证做法，并对生成结果施加严格的证据约束：步骤、配料和结论必须能被知识库内容直接支持，且不得扩展未引用的替代方案或营养结论。它涉及西红柿、土豆、牛肉及成品菜肴之间的配料—菜品关系，但不要求解释复杂历史、因果机制或跨文档知识发现。需要进行证据对齐、来源过滤和引用覆盖检查，但通常不需要多跳推理、因果分析或对比分析。因此更适合采用 hybrid_traditional，通过关键词检索、语义召回和引用片段排序来获得可直接支撑做法的知识库证据。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 27, 'graph_rag_count': 0, 'total_queries': 27}
- route_stats_after: {'traditional_count': 28, 'graph_rag_count': 0, 'total_queries': 28}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西红柿', '土豆', '牛肉', '西红柿土豆炖牛肉']
- topic_keywords: ['炖菜', '家常菜', '烹饪做法', '知识库引用', '证据支持']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6059

## Hybrid Branch Status / entity_level
- keywords: ['西红柿', '土豆', '牛肉', '西红柿土豆炖牛肉']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / topic_level
- keywords: ['炖菜', '家常菜', '烹饪做法', '知识库引用', '证据支持']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 19

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 499

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 2
- vector_count: 10
- origin_len: 16

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 16
- after_count: 13
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
- candidate_count: 13
- duration_ms: 16580
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '汤类': 1, '素菜': 1, '主食': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23148
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:46:09.185
- end: 2026-08-11T19:46:41.119
- duration_ms: 31933
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2622
- retrieval_levels: ['']
- search_types: ['vector_enhanced']
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
- chunk_count: 615
- redacted_field: 3651
- total_duration_ms: 14911
- fallback_used: False

## Final Output
- answer_chars: 806
- answer_hash: aa76a4318a47b710
- success: True

## Request Complete
- request_end: 2026-08-11T19:46:56.044
- request_duration_ms: 46867
- success: True
- final_source: generation

