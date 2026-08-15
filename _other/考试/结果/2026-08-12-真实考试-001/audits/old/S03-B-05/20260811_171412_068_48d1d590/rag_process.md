# RAG Process

audit_id: 20260811_171412_068_48d1d590
timestamp: 2026-08-11T17:14:12.069
## Request
- original_query: 我想学煮，它的关键要点和适用场景是什么？
- original_query_hash: 8e54aa9768cf33f7
- session_id: 2026-08-12-真实考试-001:old:S03-B-05
- request_mode: stream
- request_start: 2026-08-11T17:14:12.070
- evaluation_sample_id: 20260811_171412_068_48d1d590
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:14:12.071
- end: 2026-08-11T17:14:12.071
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:14:12.072
- end: 2026-08-11T17:14:12.072
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 8e54aa9768cf33f7

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:14:12.073
- end: 2026-08-11T17:14:12.073
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: 8e54aa9768cf33f7
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:14:12.073
- end: 2026-08-11T17:14:19.112
- duration_ms: 7038
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.25
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询核心实体为“煮”（一种烹饪技法），需求是获取其关键操作要点及适用场景，属于围绕单一概念的定义、方法和应用说明。虽需将技法要点与食材/菜品场景进行基础关联，但不涉及多跳推理、复杂因果链或多实体关系网络。适合通过关键词检索与语义检索结合的 hybrid_traditional 策略获取烹饪技法说明、操作规范和常见适用食材等信息。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 74, 'graph_rag_count': 0, 'total_queries': 74}
- route_stats_after: {'traditional_count': 75, 'graph_rag_count': 0, 'total_queries': 75}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['煮', '水煮', '白煮']
- topic_keywords: ['烹饪技巧', '火候', '水量', '烹饪时间', '食材熟度', '汤汁', '炖煮', '汆煮']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8372

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '火候', '水量', '烹饪时间', '食材熟度', '汤汁', '炖煮', '汆煮']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 82

## Hybrid Branch Status / entity_level
- keywords: ['煮', '水煮', '白煮']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 274

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 528

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 24
- duplicate_count: 6

## Hybrid Technique Expansion
- enabled: True
- seed_count: 12
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 25
- duration_ms: 27117
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, '高级技巧': 1, '烹饪技巧': 2}
- deferred_count: 7
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 36091
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:14:12.073
- end: 2026-08-11T17:14:55.204
- duration_ms: 43130
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 8716
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
- chunk_count: 974
- redacted_field: 2121
- total_duration_ms: 20594
- fallback_used: False

## Final Output
- answer_chars: 1314
- answer_hash: 8d5daa33cfe676fe
- success: True

## Request Complete
- request_end: 2026-08-11T17:15:15.828
- request_duration_ms: 63758
- success: True
- final_source: generation

