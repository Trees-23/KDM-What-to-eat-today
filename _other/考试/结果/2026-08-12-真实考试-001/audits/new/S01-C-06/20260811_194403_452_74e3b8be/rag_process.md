# RAG Process

audit_id: 20260811_194403_452_74e3b8be
timestamp: 2026-08-11T19:44:03.452
## Request
- original_query: 我只要知识库能证明的玉米排骨汤做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 5cfad7703b41a46e
- session_id: 2026-08-12-真实考试-001:new:S01-C-06
- request_mode: stream
- request_start: 2026-08-11T19:44:03.453
- evaluation_sample_id: 20260811_194403_452_74e3b8be
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:44:03.454
- end: 2026-08-11T19:44:03.454
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:44:03.454
- end: 2026-08-11T19:44:03.454
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 5cfad7703b41a46e

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:44:03.460
- end: 2026-08-11T19:44:03.460
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:44:03.460
- end: 2026-08-11T19:44:03.460
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:44:03.460
- end: 2026-08-11T19:44:03.460
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 5cfad7703b41a46e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:44:03.461
- end: 2026-08-11T19:44:11.749
- duration_ms: 8288
- analysis_mode: llm
- query_complexity: 0.5
- relationship_intensity: 0.35
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是检索知识库中可直接支撑“玉米排骨汤做法”的证据，并要求回答严格受引用内容约束，不补充替代方案或营养结论。其复杂性主要来自证据溯源、引用覆盖校验和输出边界控制，而非多实体关系推理。明确实体包括“玉米”“排骨”“玉米排骨汤”。不需要多跳推理、因果分析或对比分析；适合通过关键词检索、语义检索与引用片段重排来定位包含食材、步骤和用量的权威文档，再仅基于检索证据生成答案，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 23, 'graph_rag_count': 0, 'total_queries': 23}
- route_stats_after: {'traditional_count': 24, 'graph_rag_count': 0, 'total_queries': 24}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['玉米排骨汤', '玉米', '排骨']
- topic_keywords: ['汤品', '烹饪做法', '知识库证据', '引用依据']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4816

## Hybrid Branch Status / topic_level
- keywords: ['汤品', '烹饪做法', '知识库证据', '引用依据']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / entity_level
- keywords: ['玉米排骨汤', '玉米', '排骨']
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
- duration_ms: 313

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 0
- vector_count: 10
- origin_len: 13

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 13
- after_count: 8
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 8
- duration_ms: 8966
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'汤类': 2, 'Ingredient': 1, '主食': 2}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 14110
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:44:03.461
- end: 2026-08-11T19:44:25.861
- duration_ms: 22400
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1887
- retrieval_levels: ['', 'entity']
- search_types: ['entity_level', 'vector_enhanced']
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
- chunk_count: 307
- redacted_field: 1843
- total_duration_ms: 8124
- fallback_used: False

## Final Output
- answer_chars: 423
- answer_hash: 7543a4a827de62d3
- success: True

## Request Complete
- request_end: 2026-08-11T19:44:34.019
- request_duration_ms: 30565
- success: True
- final_source: generation

