# RAG Process

audit_id: 20260811_164056_490_ec51c988
timestamp: 2026-08-11T16:40:56.500
## Request
- original_query: 清蒸鳜鱼的第 1 步应该怎么做？
- original_query_hash: d834747786eb4802
- session_id: 2026-08-12-真实考试-001:old:S02-A-02
- request_mode: stream
- request_start: 2026-08-11T16:40:56.501
- evaluation_sample_id: 20260811_164056_490_ec51c988
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:40:56.502
- end: 2026-08-11T16:40:56.502
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:40:56.503
- end: 2026-08-11T16:40:56.503
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: d834747786eb4802

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:40:56.504
- end: 2026-08-11T16:40:56.504
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: d834747786eb4802
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:40:56.504
- end: 2026-08-11T16:41:03.167
- duration_ms: 6662
- analysis_mode: llm
- query_complexity: 0.12
- relationship_intensity: 0.18
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对特定菜品“清蒸鳜鱼”的单一步骤（第1步）进行直接查找，目标明确、范围极窄，不需要多跳推理、因果分析或对比分析。可通过关键词匹配、菜谱文档检索及步骤字段排序直接定位答案。明确实体包括“清蒸鳜鱼”（菜品）和“第1步”（烹饪流程步骤）。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 31, 'graph_rag_count': 0, 'total_queries': 31}
- route_stats_after: {'traditional_count': 32, 'graph_rag_count': 0, 'total_queries': 32}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['清蒸鳜鱼', '鳜鱼']
- topic_keywords: ['清蒸', '烹饪步骤', '去腥', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5712

## Hybrid Branch Status / entity_level
- keywords: ['清蒸鳜鱼', '鳜鱼']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 32

## Hybrid Branch Status / topic_level
- keywords: ['清蒸', '烹饪步骤', '去腥', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 82

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 453

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 18
- duplicate_count: 4

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
- duration_ms: 17560
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 2, 'Ingredient': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23756
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:40:56.504
- end: 2026-08-11T16:41:26.927
- duration_ms: 30422
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3566
- retrieval_levels: ['', 'entity']
- search_types: ['entity_level', 'vector_enhanced']
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
- redacted_field: 3010
- total_duration_ms: 5793
- fallback_used: False

## Final Output
- answer_chars: 63
- answer_hash: 7e0251ac95a1d3b8
- success: True

## Request Complete
- request_end: 2026-08-11T16:41:32.748
- request_duration_ms: 36247
- success: True
- final_source: generation

