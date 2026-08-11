# RAG Process

audit_id: 20260811_162144_921_73be7ca5
timestamp: 2026-08-11T16:21:44.922
## Request
- original_query: 请给出葱烧海参的完整做法，包括主要食材和步骤。
- original_query_hash: ce6dd14fc4c01f5a
- session_id: 2026-08-12-真实考试-001:old:S01-A-08
- request_mode: stream
- request_start: 2026-08-11T16:21:44.922
- evaluation_sample_id: 20260811_162144_921_73be7ca5
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:21:44.923
- end: 2026-08-11T16:21:44.923
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:21:44.923
- end: 2026-08-11T16:21:44.923
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: ce6dd14fc4c01f5a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:21:44.924
- end: 2026-08-11T16:21:44.924
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: ce6dd14fc4c01f5a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:21:44.924
- end: 2026-08-11T16:21:50.432
- duration_ms: 5507
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是针对单一道菜“葱烧海参”的直接做法查询，核心需求为获取主要食材及线性烹饪步骤。明确实体主要包括“葱烧海参”（菜品）和“海参”（主食材）；“葱”可视为菜品名称及配料中的辅助实体。查询不要求跨文档、多跳关联推理，也不涉及成因、机制或多方案对比分析。采用关键词/语义混合检索可高效召回权威菜谱、烹饪教程及食材处理说明。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 7, 'graph_rag_count': 0, 'total_queries': 7}
- route_stats_after: {'traditional_count': 8, 'graph_rag_count': 0, 'total_queries': 8}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['葱烧海参', '海参', '大葱', '高汤', '蚝油', '生抽', '老抽', '淀粉']
- topic_keywords: ['鲁菜', '海鲜菜', '葱香', '烧制', '火候', '调味', '宴客菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7205

## Hybrid Branch Status / entity_level
- keywords: ['葱烧海参', '海参', '大葱', '高汤', '蚝油', '生抽', '老抽', '淀粉']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 49

## Hybrid Branch Status / topic_level
- keywords: ['鲁菜', '海鲜菜', '葱香', '烧制', '火候', '调味', '宴客菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 65

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 322

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 22
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
- candidate_count: 22
- duration_ms: 16414
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '调料': 1, '主食': 2}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23954
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:21:44.924
- end: 2026-08-11T16:22:14.388
- duration_ms: 29463
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2121
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
- chunk_count: 422
- redacted_field: 1958
- total_duration_ms: 10661
- fallback_used: False

## Final Output
- answer_chars: 561
- answer_hash: 4ad2945b90d8cdbd
- success: True

## Request Complete
- request_end: 2026-08-11T16:22:25.078
- request_duration_ms: 40156
- success: True
- final_source: generation

