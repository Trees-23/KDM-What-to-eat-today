# RAG Process

audit_id: 20260811_165034_073_cbed035b
timestamp: 2026-08-11T16:50:34.073
## Request
- original_query: 刚开始做清蒸鲈鱼时，第一步具体要处理什么？
- original_query_hash: 7bb94fd7121d4a9a
- session_id: 2026-08-12-真实考试-001:old:S02-B-07
- request_mode: stream
- request_start: 2026-08-11T16:50:34.074
- evaluation_sample_id: 20260811_165034_073_cbed035b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:50:34.074
- end: 2026-08-11T16:50:34.074
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:50:34.075
- end: 2026-08-11T16:50:34.075
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 7bb94fd7121d4a9a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:50:34.075
- end: 2026-08-11T16:50:34.075
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 7bb94fd7121d4a9a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:50:34.076
- end: 2026-08-11T16:50:39.324
- duration_ms: 5248
- analysis_mode: llm
- query_complexity: 0.15
- relationship_intensity: 0.1
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.97
- reasoning: 该查询是针对“清蒸鲈鱼”制作流程起始步骤的直接事实检索，目标明确且答案通常位于菜谱的前置处理环节。无需多跳推理、因果分析或方案对比，也不涉及多个实体之间的复杂关系。明确实体为“清蒸鲈鱼”（菜品/烹饪对象），适合使用hybrid_traditional进行关键词和语义检索。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 46, 'graph_rag_count': 0, 'total_queries': 46}
- route_stats_after: {'traditional_count': 47, 'graph_rag_count': 0, 'total_queries': 47}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['清蒸鲈鱼', '鲈鱼']
- topic_keywords: ['清蒸', '烹饪技巧', '食材处理', '去腥']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3972

## Hybrid Branch Status / entity_level
- keywords: ['清蒸鲈鱼', '鲈鱼']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 18

## Hybrid Branch Status / topic_level
- keywords: ['清蒸', '烹饪技巧', '食材处理', '去腥']
- requested_k: 10
- actual_count: 5
- fallback_count: 5
- duration_ms: 33

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 319

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 5
- vector_count: 10
- origin_len: 17

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 17
- after_count: 14
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
- candidate_count: 14
- duration_ms: 16796
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '汤类': 1, 'Ingredient': 1, '荤菜': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21101
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:50:34.076
- end: 2026-08-11T16:51:00.427
- duration_ms: 26351
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3219
- retrieval_levels: ['', 'entity', 'topic']
- search_types: ['entity_level', 'topic_level', 'vector_enhanced']
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
- chunk_count: 79
- redacted_field: 2477
- total_duration_ms: 4219
- fallback_used: False

## Final Output
- answer_chars: 99
- answer_hash: 01e6490cb2dfda41
- success: True

## Request Complete
- request_end: 2026-08-11T16:51:04.659
- request_duration_ms: 30585
- success: True
- final_source: generation

