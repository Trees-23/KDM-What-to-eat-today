# RAG Process

audit_id: 20260811_182220_961_4512500f
timestamp: 2026-08-11T18:22:20.964
## Request
- original_query: 想吃甜品但不想步骤太复杂。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: 07ce4db883b1ed38
- session_id: 2026-08-12-真实考试-001:old:S06-C-10
- request_mode: stream
- request_start: 2026-08-11T18:22:20.965
- evaluation_sample_id: 20260811_182220_961_4512500f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:22:20.966
- end: 2026-08-11T18:22:20.966
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:22:20.966
- end: 2026-08-11T18:22:20.966
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 43
- enhanced_query_length: 43
- enhanced_query_hash: 07ce4db883b1ed38

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:22:20.967
- end: 2026-08-11T18:22:20.967
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 43
- analysis_input_query_hash: 07ce4db883b1ed38
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:22:20.967
- end: 2026-08-11T18:22:34.679
- duration_ms: 13712
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询的核心目标是从甜品食谱资料中筛选并推荐“步骤不复杂”的候选项，同时展示推荐所依据的可验证信息（如步骤数量、所需食材数量、制作时长或资料中的难度标注）。这需要对多个食谱进行条件匹配和轻量对比，但不涉及跨领域、多实体、多跳的复杂关系网络推理。明确实体主要包括“甜品”和“制作步骤/复杂度”；“想吃”属于用户偏好，“展示推荐依据”和“不将无资料支持的推测写成事实”属于回答约束。适合采用 hybrid_traditional，通过关键词、语义检索及元数据过滤召回甜品食谱，再依据资料中明确记载的步骤和难度信息排序，并为每项推荐附上来源依据。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 146, 'graph_rag_count': 33, 'total_queries': 179}
- route_stats_after: {'traditional_count': 147, 'graph_rag_count': 33, 'total_queries': 180}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['甜品']
- topic_keywords: ['简单步骤', '操作简便', '快手甜品']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7835

## Hybrid Branch Status / entity_level
- keywords: ['甜品']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 9

## Hybrid Branch Status / topic_level
- keywords: ['简单步骤', '操作简便', '快手甜品']
- requested_k: 10
- actual_count: 1
- fallback_count: 1
- duration_ms: 21

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 452

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 1
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 8
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 9
- duration_ms: 13925
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'甜品': 2, '烹饪技巧': 2, '通用知识': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22245
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:22:20.967
- end: 2026-08-11T18:22:56.926
- duration_ms: 35959
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3168
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
- chunk_count: 205
- redacted_field: 2136
- total_duration_ms: 5992
- fallback_used: False

## Final Output
- answer_chars: 293
- answer_hash: 27de0ad6f15b367d
- success: True

## Request Complete
- request_end: 2026-08-11T18:23:02.944
- request_duration_ms: 41979
- success: True
- final_source: generation

