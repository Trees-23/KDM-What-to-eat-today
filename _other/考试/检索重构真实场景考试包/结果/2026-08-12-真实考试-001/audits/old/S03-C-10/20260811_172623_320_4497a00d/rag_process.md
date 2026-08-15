# RAG Process

audit_id: 20260811_172623_320_4497a00d
timestamp: 2026-08-11T17:26:23.322
## Request
- original_query: 只根据“食品安全”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: 01619fd1a9f1afc7
- session_id: 2026-08-12-真实考试-001:old:S03-C-10
- request_mode: stream
- request_start: 2026-08-11T17:26:23.322
- evaluation_sample_id: 20260811_172623_320_4497a00d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:26:23.323
- end: 2026-08-11T17:26:23.323
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:26:23.324
- end: 2026-08-11T17:26:23.324
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 01619fd1a9f1afc7

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:26:23.324
- end: 2026-08-11T17:26:23.324
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 01619fd1a9f1afc7
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:26:23.325
- end: 2026-08-11T17:26:31.212
- duration_ms: 7887
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.15
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询本身未提出需要回答的具体食品安全问题，而是规定了回答范围与证据约束：仅检索并依据“食品安全”技巧章节的关键要点作答，对于资料未覆盖的内容必须明确保留。核心需求是章节级定向检索、内容过滤与证据忠实性校验，不涉及多实体关系网络、因果链路或跨章节多跳推理。明确实体为“食品安全”技巧章节（文档章节/知识范围实体）。因此适合采用 hybrid_traditional，通过关键词、章节标题、语义检索和重排序定位限定资料，并在生成阶段执行未证实结论保留策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 88, 'graph_rag_count': 1, 'total_queries': 89}
- route_stats_after: {'traditional_count': 89, 'graph_rag_count': 1, 'total_queries': 90}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['食品安全']
- topic_keywords: ['食品安全', '关键要点', '资料范围限制', '结论保留']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4188

## Hybrid Branch Status / topic_level
- keywords: ['食品安全', '关键要点', '资料范围限制', '结论保留']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / entity_level
- keywords: ['食品安全']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 138

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 667

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
- doc_names: ['炒/煎', '食品安全']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 12
- duration_ms: 15113
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueChunk': 2, 'TechniqueDoc': 2, '烹饪技巧': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20007
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:26:23.325
- end: 2026-08-11T17:26:51.220
- duration_ms: 27895
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5489
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
- chunk_count: 60
- redacted_field: 2802
- total_duration_ms: 4034
- fallback_used: False

## Final Output
- answer_chars: 83
- answer_hash: a9427e721142c147
- success: True

## Request Complete
- request_end: 2026-08-11T17:26:55.280
- request_duration_ms: 31958
- success: True
- final_source: generation

