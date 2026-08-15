# RAG Process

audit_id: 20260811_162331_088_3773b7da
timestamp: 2026-08-11T16:23:31.089
## Request
- original_query: 请给出红烧鱼头的完整做法，包括主要食材和步骤。
- original_query_hash: 17c614bdb263acba
- session_id: 2026-08-12-真实考试-001:old:S01-A-10
- request_mode: stream
- request_start: 2026-08-11T16:23:31.089
- evaluation_sample_id: 20260811_162331_088_3773b7da
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:23:31.090
- end: 2026-08-11T16:23:31.090
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:23:31.090
- end: 2026-08-11T16:23:31.090
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 17c614bdb263acba

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:23:31.091
- end: 2026-08-11T16:23:31.091
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: 17c614bdb263acba
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:23:31.091
- end: 2026-08-11T16:23:42.532
- duration_ms: 11440
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对“红烧鱼头”这一明确菜品的直接做法检索，需求包括主要食材和标准烹饪步骤，属于结构化但简单的信息获取任务。无需多跳推理、因果分析或跨菜系对比，仅需从可靠菜谱资料中检索并整合配料、调味比例、预处理、烹制和收汁等步骤。明确实体为“红烧鱼头”，类型为菜品。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 9, 'graph_rag_count': 0, 'total_queries': 9}
- route_stats_after: {'traditional_count': 10, 'graph_rag_count': 0, 'total_queries': 10}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['红烧鱼头', '鱼头', '生姜', '大葱', '大蒜', '料酒', '生抽', '老抽', '白糖', '食用油']
- topic_keywords: ['红烧', '家常菜', '中式烹饪', '去腥', '调味', '火候', '炖煮', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4444

## Hybrid Branch Status / entity_level
- keywords: ['红烧鱼头', '鱼头', '生姜', '大葱', '大蒜', '料酒', '生抽', '老抽', '白糖', '食用油']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 59

## Hybrid Branch Status / topic_level
- keywords: ['红烧', '家常菜', '中式烹饪', '去腥', '调味', '火候', '炖煮', '下饭菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 79

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 677

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 27
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
- candidate_count: 27
- duration_ms: 19826
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 1, '主食': 1, '调料': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24968
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:23:31.091
- end: 2026-08-11T16:24:07.502
- duration_ms: 36410
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2490
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
- chunk_count: 591
- redacted_field: 954
- total_duration_ms: 12897
- fallback_used: False

## Final Output
- answer_chars: 737
- answer_hash: b8f8339251c747e3
- success: True

## Request Complete
- request_end: 2026-08-11T16:24:20.422
- request_duration_ms: 49333
- success: True
- final_source: generation

