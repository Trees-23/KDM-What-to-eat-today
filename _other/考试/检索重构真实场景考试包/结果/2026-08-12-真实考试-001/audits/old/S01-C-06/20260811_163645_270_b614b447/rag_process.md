# RAG Process

audit_id: 20260811_163645_270_b614b447
timestamp: 2026-08-11T16:36:45.271
## Request
- original_query: 我只要知识库能证明的玉米排骨汤做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 5cfad7703b41a46e
- session_id: 2026-08-12-真实考试-001:old:S01-C-06
- request_mode: stream
- request_start: 2026-08-11T16:36:45.271
- evaluation_sample_id: 20260811_163645_270_b614b447
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:36:45.272
- end: 2026-08-11T16:36:45.272
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:36:45.272
- end: 2026-08-11T16:36:45.272
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 5cfad7703b41a46e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:36:45.273
- end: 2026-08-11T16:36:45.273
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 5cfad7703b41a46e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:36:45.273
- end: 2026-08-11T16:36:54.907
- duration_ms: 9634
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.28
- reasoning_required: True
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询核心是检索“玉米排骨汤”的做法，并且要求所有内容必须能由知识库中的证据直接支持。它不涉及食材、历史、营养或替代方案之间的复杂关系推理，而主要包含结果过滤与引用约束：仅保留有知识库依据的步骤，排除无引用的替代方案和营养结论。因此适合采用 hybrid_traditional，通过关键词/语义检索定位菜品做法文档，再依据文档片段、元数据或引用标记进行证据校验与内容筛选。查询中的明确实体包括“玉米排骨汤”“知识库”“做法”“营养结论/替代方案约束”。

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
- entity_keywords: ['玉米排骨汤', '玉米', '排骨']
- topic_keywords: ['做法', '知识库依据', '引用', '可验证信息']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3959

## Hybrid Branch Status / entity_level
- keywords: ['玉米排骨汤', '玉米', '排骨']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 36

## Hybrid Branch Status / topic_level
- keywords: ['做法', '知识库依据', '引用', '可验证信息']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 62

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 511

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 8
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 16
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
- candidate_count: 16
- duration_ms: 12657
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'汤类': 2, '主食': 1, '荤菜': 2}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 17144
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:36:45.273
- end: 2026-08-11T16:37:12.053
- duration_ms: 26779
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1836
- retrieval_levels: ['', 'topic']
- search_types: ['topic_level', 'vector_enhanced']
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
- chunk_count: 321
- redacted_field: 1846
- total_duration_ms: 7293
- fallback_used: False

## Final Output
- answer_chars: 439
- answer_hash: f122f6c1ef6d38c2
- success: True

## Request Complete
- request_end: 2026-08-11T16:37:19.383
- request_duration_ms: 34111
- success: True
- final_source: generation

