# RAG Process

audit_id: 20260811_161722_008_cdfa47ae
timestamp: 2026-08-11T16:17:22.009
## Request
- original_query: 请给出水煮鱼的完整做法，包括主要食材和步骤。
- original_query_hash: 80f6e88f9a0a6252
- session_id: 2026-08-12-真实考试-001:old:S01-A-03
- request_mode: stream
- request_start: 2026-08-11T16:17:22.010
- evaluation_sample_id: 20260811_161722_008_cdfa47ae
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:17:22.010
- end: 2026-08-11T16:17:22.010
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:17:22.011
- end: 2026-08-11T16:17:22.011
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 22
- enhanced_query_length: 22
- enhanced_query_hash: 80f6e88f9a0a6252

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:17:22.011
- end: 2026-08-11T16:17:22.011
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 22
- analysis_input_query_hash: 80f6e88f9a0a6252
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:17:22.012
- end: 2026-08-11T16:17:28.593
- duration_ms: 6580
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询属于面向单一菜品“水煮鱼”的直接操作性信息检索，核心诉求是获取主要食材和制作步骤。虽然“水煮鱼”“主要食材”“步骤”构成菜品与属性/流程的基础关联，但不涉及跨实体的复杂关系网络、知识发现或多跳推理。无需因果分析，也不需要对比分析；采用关键词检索结合语义检索的 hybrid_traditional 策略即可高效返回完整菜谱信息。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 2, 'graph_rag_count': 0, 'total_queries': 2}
- route_stats_after: {'traditional_count': 3, 'graph_rag_count': 0, 'total_queries': 3}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['水煮鱼', '鱼片', '豆芽', '辣椒', '花椒', '郫县豆瓣酱', '姜', '蒜', '葱', '食用油', '炒锅']
- topic_keywords: ['川菜', '麻辣', '香辣', '下饭菜', '烹饪步骤', '调味', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5836

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '麻辣', '香辣', '下饭菜', '烹饪步骤', '调味', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 52

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 438

## Hybrid Branch Status / entity_level
- keywords: ['水煮鱼', '鱼片', '豆芽', '辣椒', '花椒', '郫县豆瓣酱', '姜', '蒜', '葱', '食用油', '炒锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 1
- duration_ms: 576

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 29
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 29
- duration_ms: 28537
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '汤类': 1, 'Ingredient': 1, '主食,凉菜': 1}
- deferred_count: 7
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 34963
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:17:22.012
- end: 2026-08-11T16:18:03.557
- duration_ms: 41545
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2686
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
- chunk_count: 474
- redacted_field: 4710
- total_duration_ms: 20815
- fallback_used: False

## Final Output
- answer_chars: 618
- answer_hash: 5afaa34aab2bbbbb
- success: True

## Request Complete
- request_end: 2026-08-11T16:18:24.397
- request_duration_ms: 62387
- success: True
- final_source: generation

