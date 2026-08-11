# RAG Process

audit_id: 20260811_172114_926_4c37fe82
timestamp: 2026-08-11T17:21:14.927
## Request
- original_query: 只根据“腌（肉）”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: b9afc0b74b3c851b
- session_id: 2026-08-12-真实考试-001:old:S03-C-02
- request_mode: stream
- request_start: 2026-08-11T17:21:14.927
- evaluation_sample_id: 20260811_172114_926_4c37fe82
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:21:14.928
- end: 2026-08-11T17:21:14.928
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:21:14.929
- end: 2026-08-11T17:21:14.929
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: b9afc0b74b3c851b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:21:14.930
- end: 2026-08-11T17:21:14.930
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: b9afc0b74b3c851b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:21:14.930
- end: 2026-08-11T17:21:26.903
- duration_ms: 11973
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.2
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 该查询的核心是限定回答范围：仅检索并依据“腌（肉）”技巧章节中的关键要点作答，同时对资料未覆盖的内容明确保留。它不要求跨实体关系发现、多跳推理、因果分析或对比分析，但需要执行章节级过滤、要点抽取、证据约束与缺失信息识别。明确实体主要为“腌（肉）”技巧章节，因此适合采用支持关键词检索、章节/元数据过滤和语义召回的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 80, 'graph_rag_count': 1, 'total_queries': 81}
- route_stats_after: {'traditional_count': 81, 'graph_rag_count': 1, 'total_queries': 82}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['腌（肉）', '腌肉']
- topic_keywords: ['烹饪技巧', '关键要点', '资料范围', '结论保留']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4883

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '关键要点', '资料范围', '结论保留']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 8

## Hybrid Branch Status / entity_level
- keywords: ['腌（肉）', '腌肉']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 83

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 687

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 0
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 10
- duplicate_count: 10

## Hybrid Technique Expansion
- enabled: True
- seed_count: 9
- expanded_count: 9
- doc_names: ['腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 11
- duration_ms: 16596
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueChunk': 2, '烹饪技巧': 1, 'TechniqueDoc': 1, '荤菜': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22202
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:21:14.930
- end: 2026-08-11T17:21:49.107
- duration_ms: 34176
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5489
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
- chunk_count: 1
- redacted_field: 3773
- total_duration_ms: 3775
- fallback_used: False

## Final Output
- answer_chars: 60
- answer_hash: 76845645be08b1a6
- success: True

## Request Complete
- request_end: 2026-08-11T17:21:52.900
- request_duration_ms: 37972
- success: True
- final_source: generation

