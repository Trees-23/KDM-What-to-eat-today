# RAG Process

audit_id: 20260811_161959_438_ee200c0a
timestamp: 2026-08-11T16:19:59.439
## Request
- original_query: 请给出蒜蓉虾的完整做法，包括主要食材和步骤。
- original_query_hash: 2477a9c219561c16
- session_id: 2026-08-12-真实考试-001:old:S01-A-06
- request_mode: stream
- request_start: 2026-08-11T16:19:59.440
- evaluation_sample_id: 20260811_161959_438_ee200c0a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:19:59.440
- end: 2026-08-11T16:19:59.440
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:19:59.441
- end: 2026-08-11T16:19:59.441
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 22
- enhanced_query_length: 22
- enhanced_query_hash: 2477a9c219561c16

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:19:59.441
- end: 2026-08-11T16:19:59.441
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 22
- analysis_input_query_hash: 2477a9c219561c16
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:19:59.441
- end: 2026-08-11T16:20:22.172
- duration_ms: 22730
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.25
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询属于明确的菜谱与操作步骤检索需求，目标是获取“蒜蓉虾”的主要食材和标准制作流程。虽涉及菜品、蒜蓉和虾等实体，以及食材与步骤之间的基本关联，但不需要跨文档多跳推理、因果分析或方案对比。采用关键词检索结合语义检索的 hybrid_traditional 策略即可高效召回完整且相关的菜谱内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 5, 'graph_rag_count': 0, 'total_queries': 5}
- route_stats_after: {'traditional_count': 6, 'graph_rag_count': 0, 'total_queries': 6}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蒜蓉虾', '鲜虾', '大蒜', '生姜', '小葱', '生抽', '料酒', '食用油']
- topic_keywords: ['家常菜', '海鲜', '蒜香', '烹饪步骤', '调味', '去腥', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3833

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '海鲜', '蒜香', '烹饪步骤', '调味', '去腥', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 108

## Hybrid Branch Status / entity_level
- keywords: ['蒜蓉虾', '鲜虾', '大蒜', '生姜', '小葱', '生抽', '料酒', '食用油']
- requested_k: 10
- actual_count: 8
- fallback_count: 0
- duration_ms: 116

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 439

## Hybrid Branch Summary
- entity_count: 8
- topic_count: 10
- vector_count: 10
- origin_len: 28

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 28
- after_count: 26
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 26
- duration_ms: 27565
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 2, '素菜': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 31852
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:19:59.441
- end: 2026-08-11T16:20:54.025
- duration_ms: 54583
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2293
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
- chunk_count: 250
- redacted_field: 2648
- total_duration_ms: 12303
- fallback_used: False

## Final Output
- answer_chars: 343
- answer_hash: 4c91188381fb359a
- success: True

## Request Complete
- request_end: 2026-08-11T16:21:06.344
- request_duration_ms: 66904
- success: True
- final_source: generation

