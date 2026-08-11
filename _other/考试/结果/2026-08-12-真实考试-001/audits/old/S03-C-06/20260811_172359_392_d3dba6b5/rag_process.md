# RAG Process

audit_id: 20260811_172359_392_d3dba6b5
timestamp: 2026-08-11T17:23:59.392
## Request
- original_query: 只根据“使用空气炸锅”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: c8ea93fbc30cd695
- session_id: 2026-08-12-真实考试-001:old:S03-C-06
- request_mode: stream
- request_start: 2026-08-11T17:23:59.392
- evaluation_sample_id: 20260811_172359_392_d3dba6b5
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:23:59.393
- end: 2026-08-11T17:23:59.393
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:23:59.394
- end: 2026-08-11T17:23:59.394
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 38
- enhanced_query_length: 38
- enhanced_query_hash: c8ea93fbc30cd695

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:23:59.395
- end: 2026-08-11T17:23:59.395
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 38
- analysis_input_query_hash: c8ea93fbc30cd695
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:23:59.396
- end: 2026-08-11T17:24:11.494
- duration_ms: 12098
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.22
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询的核心是限定证据范围：仅检索并依据“使用空气炸锅”技巧章节中的关键要点作答，同时对资料未覆盖的内容明确保留。它不要求跨章节、多实体关联、多跳推理、因果分析或对比分析；主要需要精确的章节级检索、关键要点抽取与基于证据的回答约束。因此适合采用 hybrid_traditional，通过关键词/章节标题匹配结合语义检索定位目标章节，并在生成阶段执行严格的引用范围与未知信息保留策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 84, 'graph_rag_count': 1, 'total_queries': 85}
- route_stats_after: {'traditional_count': 85, 'graph_rag_count': 1, 'total_queries': 86}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['空气炸锅', '使用空气炸锅']
- topic_keywords: ['烹饪技巧', '资料依据', '信息保留']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 10617

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '资料依据', '信息保留']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 30

## Hybrid Branch Status / entity_level
- keywords: ['空气炸锅', '使用空气炸锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 96

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 339

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 0
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 11
- duplicate_count: 9

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 12
- duration_ms: 14668
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, 'TechniqueChunk': 2, 'TechniqueDoc': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25657
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:23:59.396
- end: 2026-08-11T17:24:37.153
- duration_ms: 37756
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4887
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
- chunk_count: 69
- redacted_field: 2025
- total_duration_ms: 3480
- fallback_used: False

## Final Output
- answer_chars: 88
- answer_hash: c1fa013836f69b89
- success: True

## Request Complete
- request_end: 2026-08-11T17:24:40.646
- request_duration_ms: 41254
- success: True
- final_source: generation

