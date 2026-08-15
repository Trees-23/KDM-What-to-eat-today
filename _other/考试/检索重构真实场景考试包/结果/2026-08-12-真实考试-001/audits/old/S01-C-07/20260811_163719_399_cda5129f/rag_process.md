# RAG Process

audit_id: 20260811_163719_399_cda5129f
timestamp: 2026-08-11T16:37:19.402
## Request
- original_query: 我只要知识库能证明的提拉米苏做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 40a51fe450c06c7a
- session_id: 2026-08-12-真实考试-001:old:S01-C-07
- request_mode: stream
- request_start: 2026-08-11T16:37:19.402
- evaluation_sample_id: 20260811_163719_399_cda5129f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:37:19.403
- end: 2026-08-11T16:37:19.403
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:37:19.403
- end: 2026-08-11T16:37:19.403
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 40a51fe450c06c7a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:37:19.404
- end: 2026-08-11T16:37:19.404
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 40a51fe450c06c7a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:37:19.404
- end: 2026-08-11T16:37:34.561
- duration_ms: 15156
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.25
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询的核心实体为“提拉米苏”和“知识库”。用户主要诉求是检索知识库中有明确依据的提拉米苏做法，并施加严格的证据约束：答案中的步骤、配料和结论必须可由检索到的内容直接支持，且不得补充未被引用的替代方案或营养结论。该任务不需要多跳推理、因果分析或实体关系网络推理，也不涉及不同方案之间的对比；重点在于关键词/语义检索、文档证据定位、引用覆盖校验与生成约束。因此适合采用 hybrid_traditional，通过关键词检索“提拉米苏/做法/配料/步骤”结合向量语义召回，再基于引用证据进行答案生成与约束过滤。

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
- entity_keywords: ['提拉米苏']
- topic_keywords: ['做法', '知识库依据', '引用', '证据支持']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3578

## Hybrid Branch Status / entity_level
- keywords: ['提拉米苏']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 20

## Hybrid Branch Status / topic_level
- keywords: ['做法', '知识库依据', '引用', '证据支持']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 56

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 416

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
- seed_count: 1
- expanded_count: 9
- doc_names: ['凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 13365
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'Recipe': 1, '烹饪技巧': 2, '主食': 1, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 17381
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:37:19.404
- end: 2026-08-11T16:37:51.943
- duration_ms: 32539
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1569
- retrieval_levels: ['', 'context_expansion', 'entity', 'topic']
- search_types: ['entity_level', 'technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 108
- redacted_field: 3357
- total_duration_ms: 7574
- fallback_used: False

## Final Output
- answer_chars: 155
- answer_hash: 42ca55a3bfc80317
- success: True

## Request Complete
- request_end: 2026-08-11T16:37:59.542
- request_duration_ms: 40139
- success: True
- final_source: generation

