# RAG Process

audit_id: 20260811_194434_032_a25a358c
timestamp: 2026-08-11T19:44:34.032
## Request
- original_query: 我只要知识库能证明的提拉米苏做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 40a51fe450c06c7a
- session_id: 2026-08-12-真实考试-001:new:S01-C-07
- request_mode: stream
- request_start: 2026-08-11T19:44:34.033
- evaluation_sample_id: 20260811_194434_032_a25a358c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:44:34.034
- end: 2026-08-11T19:44:34.034
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:44:34.034
- end: 2026-08-11T19:44:34.034
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 40a51fe450c06c7a

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:44:34.042
- end: 2026-08-11T19:44:34.042
- duration_ms: 0
- entity_id: 201000935
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:44:34.042
- end: 2026-08-11T19:44:34.042
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:44:34.042
- end: 2026-08-11T19:44:34.042
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 40a51fe450c06c7a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:44:34.043
- end: 2026-08-11T19:44:42.114
- duration_ms: 8071
- analysis_mode: llm
- query_complexity: 0.42
- relationship_intensity: 0.28
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询的核心目标是检索知识库中可直接证实的“提拉米苏做法”，并严格约束回答仅使用有引用支撑的内容。它不要求解释制作原理、比较不同配方，或分析多实体间的复杂关系网络，因此复杂度和关系密集度较低。需要的推理主要是证据约束校验：将检索到的步骤、配料和用量与具体知识库片段逐项对齐，过滤无引用支撑的替代方案及营养结论。无需多跳推理、因果分析或对比分析。明确实体包括“提拉米苏”和“知识库”；其中提拉米苏属于菜品/甜点实体，知识库属于信息源/证据范围实体。适合使用hybrid_traditional，通过关键词、语义检索和引用片段重排序来获取并验证可溯源内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 24, 'graph_rag_count': 0, 'total_queries': 24}
- route_stats_after: {'traditional_count': 25, 'graph_rag_count': 0, 'total_queries': 25}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['提拉米苏']
- topic_keywords: ['烹饪做法', '知识库依据', '引用', '证据约束']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5329

## Hybrid Branch Status / topic_level
- keywords: ['烹饪做法', '知识库依据', '引用', '证据约束']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / entity_level
- keywords: ['提拉米苏']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 17

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 392

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 9
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
- candidate_count: 10
- duration_ms: 9603
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'Recipe': 1, '烹饪技巧': 2, '主食': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 15346
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:44:34.043
- end: 2026-08-11T19:44:57.462
- duration_ms: 23419
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1679
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
- chunk_count: 95
- redacted_field: 1875
- total_duration_ms: 3744
- fallback_used: False

## Final Output
- answer_chars: 138
- answer_hash: 07b8d4c0f47ff36b
- success: True

## Request Complete
- request_end: 2026-08-11T19:45:01.234
- request_duration_ms: 27201
- success: True
- final_source: generation

