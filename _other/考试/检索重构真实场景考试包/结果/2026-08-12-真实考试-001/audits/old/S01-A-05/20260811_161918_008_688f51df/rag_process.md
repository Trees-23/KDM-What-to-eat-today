# RAG Process

audit_id: 20260811_161918_008_688f51df
timestamp: 2026-08-11T16:19:18.009
## Request
- original_query: 请给出鳊鱼炖豆腐的完整做法，包括主要食材和步骤。
- original_query_hash: 747f25e2d25638f9
- session_id: 2026-08-12-真实考试-001:old:S01-A-05
- request_mode: stream
- request_start: 2026-08-11T16:19:18.009
- evaluation_sample_id: 20260811_161918_008_688f51df
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:19:18.010
- end: 2026-08-11T16:19:18.010
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:19:18.010
- end: 2026-08-11T16:19:18.010
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 24
- enhanced_query_length: 24
- enhanced_query_hash: 747f25e2d25638f9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:19:18.011
- end: 2026-08-11T16:19:18.011
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 24
- analysis_input_query_hash: 747f25e2d25638f9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:19:18.011
- end: 2026-08-11T16:19:26.121
- duration_ms: 8110
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.35
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是针对具体菜品“鳊鱼炖豆腐”的直接做法检索，目标明确，需要返回主要食材与线性烹饪步骤。涉及“鳊鱼”和“豆腐”两个核心食材实体及其搭配关系，但不要求跨文档、多跳知识推理、因果机制解释或方案对比。适合通过关键词、菜谱标题、食材字段和步骤字段进行混合检索与排序。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 4, 'graph_rag_count': 0, 'total_queries': 4}
- route_stats_after: {'traditional_count': 5, 'graph_rag_count': 0, 'total_queries': 5}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鳊鱼', '豆腐', '鳊鱼炖豆腐']
- topic_keywords: ['炖菜', '家常菜', '鱼类烹饪', '去腥', '火候', '汤鲜味美']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4106

## Hybrid Branch Status / topic_level
- keywords: ['炖菜', '家常菜', '鱼类烹饪', '去腥', '火候', '汤鲜味美']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 110

## Hybrid Branch Status / entity_level
- keywords: ['鳊鱼', '豆腐', '鳊鱼炖豆腐']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 202

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 674

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 20
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
- candidate_count: 20
- duration_ms: 17204
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '汤类': 1, '荤菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22001
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:19:18.011
- end: 2026-08-11T16:19:48.124
- duration_ms: 30113
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2672
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
- chunk_count: 428
- redacted_field: 2605
- total_duration_ms: 11249
- fallback_used: False

## Final Output
- answer_chars: 546
- answer_hash: 98b7a5ffc62f18c2
- success: True

## Request Complete
- request_end: 2026-08-11T16:19:59.425
- request_duration_ms: 41416
- success: True
- final_source: generation

