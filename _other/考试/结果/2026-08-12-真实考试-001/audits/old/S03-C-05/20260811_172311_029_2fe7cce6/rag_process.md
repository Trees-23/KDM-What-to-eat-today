# RAG Process

audit_id: 20260811_172311_029_2fe7cce6
timestamp: 2026-08-11T17:23:11.030
## Request
- original_query: 只根据“炒/煎”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: 9cc934aec64bac9c
- session_id: 2026-08-12-真实考试-001:old:S03-C-05
- request_mode: stream
- request_start: 2026-08-11T17:23:11.030
- evaluation_sample_id: 20260811_172311_029_2fe7cce6
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:23:11.031
- end: 2026-08-11T17:23:11.031
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:23:11.031
- end: 2026-08-11T17:23:11.031
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 9cc934aec64bac9c

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:23:11.032
- end: 2026-08-11T17:23:11.032
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 9cc934aec64bac9c
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:23:11.032
- end: 2026-08-11T17:23:17.325
- duration_ms: 6293
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.15
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 该查询的核心是限定证据范围与回答规范：仅检索并依据“炒/煎”技巧章节的关键要点作答，对资料未明确说明的内容需保留而非补充推断。它不要求分析多个实体之间的复杂关联，也不需要多跳、因果或对比推理；主要需要章节级精确检索、关键要点抽取和证据边界校验。明确实体为“炒”和“煎”，均属于烹饪技法/章节主题。因此适合采用 hybrid_traditional，通过关键词、章节标题匹配和语义检索定位指定资料范围。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 83, 'graph_rag_count': 1, 'total_queries': 84}
- route_stats_after: {'traditional_count': 84, 'graph_rag_count': 1, 'total_queries': 85}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['炒', '煎', '“炒/煎”技巧章节']
- topic_keywords: ['烹饪技巧', '关键要点', '资料依据', '结论保留']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4999

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '关键要点', '资料依据', '结论保留']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 9

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 343

## Hybrid Branch Status / entity_level
- keywords: ['炒', '煎', '“炒/煎”技巧章节']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 355

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 0
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 13
- duplicate_count: 7

## Hybrid Technique Expansion
- enabled: True
- seed_count: 11
- expanded_count: 9
- doc_names: ['糖色的炒制', '炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 23924
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, '烹饪技巧': 1, 'TechniqueChunk': 2}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 29310
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:23:11.032
- end: 2026-08-11T17:23:46.638
- duration_ms: 35605
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4694
- retrieval_levels: ['context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion']
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
- chunk_count: 66
- redacted_field: 10724
- total_duration_ms: 12705
- fallback_used: False

## Final Output
- answer_chars: 90
- answer_hash: 892f068d8212f61d
- success: True

## Request Complete
- request_end: 2026-08-11T17:23:59.367
- request_duration_ms: 48336
- success: True
- final_source: generation

