# RAG Process

audit_id: 20260811_172152_911_15f625a6
timestamp: 2026-08-11T17:21:52.915
## Request
- original_query: 只根据“焯水”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: 50a81deabf78fcbd
- session_id: 2026-08-12-真实考试-001:old:S03-C-03
- request_mode: stream
- request_start: 2026-08-11T17:21:52.915
- evaluation_sample_id: 20260811_172152_911_15f625a6
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:21:52.916
- end: 2026-08-11T17:21:52.916
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:21:52.916
- end: 2026-08-11T17:21:52.916
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 34
- enhanced_query_length: 34
- enhanced_query_hash: 50a81deabf78fcbd

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:21:52.916
- end: 2026-08-11T17:21:52.916
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 34
- analysis_input_query_hash: 50a81deabf78fcbd
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:21:52.917
- end: 2026-08-11T17:22:02.885
- duration_ms: 9968
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询本质上是对特定资料范围（“焯水”技巧章节）施加回答约束，而非提出需要跨实体关联、因果归因或多跳推理的内容问题。检索时应精确定位该章节及其关键要点，并采用严格的证据约束：仅依据章节明确陈述的信息作答，资料未说明的结论应标注为未提供或无法确定。明确实体主要为“焯水”技巧章节。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 81, 'graph_rag_count': 1, 'total_queries': 82}
- route_stats_after: {'traditional_count': 82, 'graph_rag_count': 1, 'total_queries': 83}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['焯水', '“焯水”技巧章节']
- topic_keywords: ['烹饪技巧', '关键要点', '资料依据', '信息保留']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2958

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '关键要点', '资料依据', '信息保留']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / entity_level
- keywords: ['焯水', '“焯水”技巧章节']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 158

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 515

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
- seed_count: 10
- expanded_count: 9
- doc_names: ['去腥', '揭秘食材搭配的智慧：这些食物不宜同食']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 18143
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, 'TechniqueChunk': 2, '烹饪技巧': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21651
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:21:52.917
- end: 2026-08-11T17:22:24.538
- duration_ms: 31621
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6854
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
- chunk_count: 51
- redacted_field: 3426
- total_duration_ms: 4156
- fallback_used: False

## Final Output
- answer_chars: 73
- answer_hash: 8d53a0837f7aee7c
- success: True

## Request Complete
- request_end: 2026-08-11T17:22:28.723
- request_duration_ms: 35808
- success: True
- final_source: generation

