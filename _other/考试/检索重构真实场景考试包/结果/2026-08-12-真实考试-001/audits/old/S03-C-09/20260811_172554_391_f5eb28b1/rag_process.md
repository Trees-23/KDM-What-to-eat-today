# RAG Process

audit_id: 20260811_172554_391_f5eb28b1
timestamp: 2026-08-11T17:25:54.395
## Request
- original_query: 只根据“辅料技巧”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: f9d2d9415a89af77
- session_id: 2026-08-12-真实考试-001:old:S03-C-09
- request_mode: stream
- request_start: 2026-08-11T17:25:54.395
- evaluation_sample_id: 20260811_172554_391_f5eb28b1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:25:54.397
- end: 2026-08-11T17:25:54.397
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:25:54.397
- end: 2026-08-11T17:25:54.397
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: f9d2d9415a89af77

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:25:54.399
- end: 2026-08-11T17:25:54.399
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: f9d2d9415a89af77
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:25:54.400
- end: 2026-08-11T17:26:05.007
- duration_ms: 10606
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询本质上是对回答范围和证据边界的约束：仅检索并依据“辅料技巧”章节的关键要点作答，资料未覆盖的结论需明确保留。不存在需要跨章节、多实体关联的多跳推理，也不要求因果或对比分析。明确实体为“辅料技巧”技巧章节，适合通过关键词、章节标题过滤和语义检索进行定向召回，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 87, 'graph_rag_count': 1, 'total_queries': 88}
- route_stats_after: {'traditional_count': 88, 'graph_rag_count': 1, 'total_queries': 89}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['辅料技巧']
- topic_keywords: ['烹饪技巧', '关键要点', '资料范围', '结论保留']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3788

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '关键要点', '资料范围', '结论保留']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 7

## Hybrid Branch Status / entity_level
- keywords: ['辅料技巧']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 18

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 448

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 0
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 4
- duplicate_count: 8

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['辅料技巧', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 5
- duration_ms: 8603
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, 'TechniqueDoc': 1, 'TechniqueChunk': 1, '汤类': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 12865
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:25:54.400
- end: 2026-08-11T17:26:17.873
- duration_ms: 23472
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3885
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
- chunk_count: 34
- redacted_field: 4911
- total_duration_ms: 5405
- fallback_used: False

## Final Output
- answer_chars: 52
- answer_hash: 3ebe0214439d1bdd
- success: True

## Request Complete
- request_end: 2026-08-11T17:26:23.304
- request_duration_ms: 28909
- success: True
- final_source: generation

