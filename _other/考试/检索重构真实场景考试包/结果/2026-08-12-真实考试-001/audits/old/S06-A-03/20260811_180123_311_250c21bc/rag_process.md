# RAG Process

audit_id: 20260811_180123_311_250c21bc
timestamp: 2026-08-11T18:01:23.312
## Request
- original_query: 早餐想吃热乎又不复杂的。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: efa6f391e518c29c
- session_id: 2026-08-12-真实考试-001:old:S06-A-03
- request_mode: stream
- request_start: 2026-08-11T18:01:23.313
- evaluation_sample_id: 20260811_180123_311_250c21bc
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:01:23.313
- end: 2026-08-11T18:01:23.313
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:01:23.314
- end: 2026-08-11T18:01:23.314
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: efa6f391e518c29c

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:01:23.314
- end: 2026-08-11T18:01:23.314
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 31
- analysis_input_query_hash: efa6f391e518c29c
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:01:23.315
- end: 2026-08-11T18:01:37.634
- duration_ms: 14319
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.42
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带偏好约束的菜品推荐：需要从知识库菜品中筛选适合“早餐”场景、符合“热乎”和“制作不复杂”两个属性的候选菜，并进行排序后说明推荐依据。它需要基于菜品标签、烹饪时长、步骤数量、成品温度等字段做条件匹配与轻量对比，但不涉及跨多实体、多关系路径的复杂知识推理，因此适合采用 hybrid_traditional，通过关键词/语义检索召回候选菜品，再结合结构化属性进行过滤和排序。明确概念包括“早餐”（用餐场景）、“热乎”（温度/食用体验约束）和“不复杂”（制作难度或步骤复杂度约束）。不需要多跳推理和因果分析，但需要候选菜品间的对比分析。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 121, 'graph_rag_count': 31, 'total_queries': 152}
- route_stats_after: {'traditional_count': 122, 'graph_rag_count': 31, 'total_queries': 153}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸡蛋', '鸡蛋羹', '西红柿鸡蛋面', '煎蛋', '热粥', '包子', '馒头']
- topic_keywords: ['早餐', '热乎', '快手菜', '简单易做', '省时', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6129

## Hybrid Branch Status / entity_level
- keywords: ['鸡蛋', '鸡蛋羹', '西红柿鸡蛋面', '煎蛋', '热粥', '包子', '馒头']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / topic_level
- keywords: ['早餐', '热乎', '快手菜', '简单易做', '省时', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 27

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: -196

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 10
- vector_count: 10
- origin_len: 24

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 24
- after_count: 24
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 5
- doc_names: ['如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 25
- duration_ms: 13168
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'早餐': 2, 'Ingredient': 1, '主食': 1, '烹饪技巧': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19118
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:01:23.315
- end: 2026-08-11T18:01:56.753
- duration_ms: 33438
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1488
- retrieval_levels: ['', 'context_expansion', 'entity', 'topic']
- search_types: ['entity_level', 'technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 169
- redacted_field: 2163
- total_duration_ms: 5477
- fallback_used: False

## Final Output
- answer_chars: 232
- answer_hash: 376dfa9385f4b4ee
- success: True

## Request Complete
- request_end: 2026-08-11T18:02:02.258
- request_duration_ms: 38945
- success: True
- final_source: generation

