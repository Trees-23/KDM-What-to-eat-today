# RAG Process

audit_id: 20260811_172021_999_71e598b7
timestamp: 2026-08-11T17:20:21.999
## Request
- original_query: 只根据“去腥”技巧章节的关键要点回答；资料没有说明的结论请明确保留。
- original_query_hash: 37694054df54ec8b
- session_id: 2026-08-12-真实考试-001:old:S03-C-01
- request_mode: stream
- request_start: 2026-08-11T17:20:22.000
- evaluation_sample_id: 20260811_172021_999_71e598b7
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:20:22.001
- end: 2026-08-11T17:20:22.001
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:20:22.001
- end: 2026-08-11T17:20:22.001
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 34
- enhanced_query_length: 34
- enhanced_query_hash: 37694054df54ec8b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:20:22.001
- end: 2026-08-11T17:20:22.001
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 34
- analysis_input_query_hash: 37694054df54ec8b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:20:22.002
- end: 2026-08-11T17:20:34.596
- duration_ms: 12594
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询的核心是对回答证据范围施加约束：仅检索并依据“去腥”技巧章节的关键要点作答，且对章节资料未覆盖的结论进行明确保留。它不涉及多实体关系发现、跨章节多跳推理、因果链分析或方案对比，而是定向章节检索、关键要点抽取与基于证据的保守生成。明确实体主要为“去腥技巧章节”和“关键要点（资料证据范围）”。因此适合采用 hybrid_traditional，通过关键词/章节标题精确召回结合语义检索定位相关段落，并在生成阶段执行严格的来源约束与未知信息声明。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 79, 'graph_rag_count': 1, 'total_queries': 80}
- route_stats_after: {'traditional_count': 80, 'graph_rag_count': 1, 'total_queries': 81}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['去腥', '去腥技巧章节']
- topic_keywords: ['去腥', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 13670

## Hybrid Branch Status / topic_level
- keywords: ['去腥', '烹饪技巧']
- requested_k: 10
- actual_count: 5
- fallback_count: 5
- duration_ms: 26

## Hybrid Branch Status / entity_level
- keywords: ['去腥', '去腥技巧章节']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 106

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 697

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 5
- vector_count: 10
- origin_len: 25

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 25
- after_count: 16
- duplicate_count: 9

## Hybrid Technique Expansion
- enabled: True
- seed_count: 11
- expanded_count: 9
- doc_names: ['去腥', '腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 20581
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, 'TechniqueChunk': 2, '烹饪技巧': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 35003
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:20:22.002
- end: 2026-08-11T17:21:09.600
- duration_ms: 47598
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3897
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
- chunk_count: 36
- redacted_field: 4682
- total_duration_ms: 5290
- fallback_used: False

## Final Output
- answer_chars: 48
- answer_hash: a9bf6e310def5825
- success: True

## Request Complete
- request_end: 2026-08-11T17:21:14.916
- request_duration_ms: 52916
- success: True
- final_source: generation

