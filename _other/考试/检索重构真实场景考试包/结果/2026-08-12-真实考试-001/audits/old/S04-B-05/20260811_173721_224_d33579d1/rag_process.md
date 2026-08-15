# RAG Process

audit_id: 20260811_173721_224_d33579d1
timestamp: 2026-08-11T17:37:21.225
## Request
- original_query: 有青蟹可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: c2366b43035842b6
- session_id: 2026-08-12-真实考试-001:old:S04-B-05
- request_mode: stream
- request_start: 2026-08-11T17:37:21.225
- evaluation_sample_id: 20260811_173721_224_d33579d1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:37:21.226
- end: 2026-08-11T17:37:21.226
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:37:21.226
- end: 2026-08-11T17:37:21.226
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: c2366b43035842b6

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:37:21.227
- end: 2026-08-11T17:37:21.227
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: c2366b43035842b6
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:37:21.228
- end: 2026-08-11T17:37:28.848
- duration_ms: 7620
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.62
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询的核心是识别食材实体“青蟹”与菜谱实体之间的包含关系，并筛选出配料表中确实出现青蟹的菜谱。需要进行菜谱召回、食材字段匹配及结果验证，属于中等复杂度的关系查询；但不涉及跨领域、多跳因果推理或复杂知识网络发现。采用关键词检索与向量检索结合的 hybrid_traditional 策略，可同时覆盖“青蟹”的别名、具体菜名和菜谱配料文本，并通过结构化配料字段或正文证据确认其真实包含关系。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 103, 'graph_rag_count': 1, 'total_queries': 104}
- route_stats_after: {'traditional_count': 104, 'graph_rag_count': 1, 'total_queries': 105}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['青蟹', '清蒸青蟹', '姜葱炒青蟹', '咖喱青蟹', '避风塘炒蟹', '青蟹粥', '青蟹煲']
- topic_keywords: ['海鲜菜', '螃蟹菜谱', '蒸菜', '炒菜', '煲仔菜', '鲜味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5903

## Hybrid Branch Status / topic_level
- keywords: ['海鲜菜', '螃蟹菜谱', '蒸菜', '炒菜', '煲仔菜', '鲜味']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 8

## Hybrid Branch Status / entity_level
- keywords: ['青蟹', '清蒸青蟹', '姜葱炒青蟹', '咖喱青蟹', '避风塘炒蟹', '青蟹粥', '青蟹煲']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 10

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 308

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 8
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 7
- doc_names: ['焯水']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 9
- duration_ms: 14481
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'Ingredient': 1, '水产': 1, '烹饪技巧': 1, '荤菜': 1, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20709
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:37:21.228
- end: 2026-08-11T17:37:49.558
- duration_ms: 28330
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3696
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
- chunk_count: 358
- redacted_field: 5493
- total_duration_ms: 13225
- fallback_used: False

## Final Output
- answer_chars: 463
- answer_hash: 87d6b641aa4619a4
- success: True

## Request Complete
- request_end: 2026-08-11T17:38:02.822
- request_duration_ms: 41596
- success: True
- final_source: generation

