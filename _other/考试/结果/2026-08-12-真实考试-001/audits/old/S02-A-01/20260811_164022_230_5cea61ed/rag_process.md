# RAG Process

audit_id: 20260811_164022_230_5cea61ed
timestamp: 2026-08-11T16:40:22.236
## Request
- original_query: 回锅肉的第 1 步应该怎么做？
- original_query_hash: a488329948e4c411
- session_id: 2026-08-12-真实考试-001:old:S02-A-01
- request_mode: stream
- request_start: 2026-08-11T16:40:22.237
- evaluation_sample_id: 20260811_164022_230_5cea61ed
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:40:22.239
- end: 2026-08-11T16:40:22.239
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:40:22.239
- end: 2026-08-11T16:40:22.240
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 15
- enhanced_query_length: 15
- enhanced_query_hash: a488329948e4c411

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:40:22.241
- end: 2026-08-11T16:40:22.241
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 15
- analysis_input_query_hash: a488329948e4c411
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:40:22.241
- end: 2026-08-11T16:40:29.261
- duration_ms: 7019
- analysis_mode: llm
- query_complexity: 0.15
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对菜品“回锅肉”制作流程中“第1步”的直接定位与信息查找，不需要多跳推理、因果分析或对比分析。明确实体包括菜品实体“回锅肉”和流程步骤实体“第1步”。适合通过关键词检索、菜谱标题匹配及步骤字段定位的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 30, 'graph_rag_count': 0, 'total_queries': 30}
- route_stats_after: {'traditional_count': 31, 'graph_rag_count': 0, 'total_queries': 31}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['回锅肉']
- topic_keywords: ['川菜', '烹饪步骤', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5354

## Hybrid Branch Status / entity_level
- keywords: ['回锅肉']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 14

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '烹饪步骤', '烹饪技巧']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 45

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 498

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 10
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 18
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 17709
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 2, '主食,凉菜': 1}
- deferred_count: 8
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23583
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:40:22.241
- end: 2026-08-11T16:40:52.846
- duration_ms: 30604
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3582
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
- chunk_count: 57
- redacted_field: 2373
- total_duration_ms: 3601
- fallback_used: False

## Final Output
- answer_chars: 61
- answer_hash: 4c6bddb160ddfe09
- success: True

## Request Complete
- request_end: 2026-08-11T16:40:56.474
- request_duration_ms: 34237
- success: True
- final_source: generation

