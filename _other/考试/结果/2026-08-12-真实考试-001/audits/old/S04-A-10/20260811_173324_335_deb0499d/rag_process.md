# RAG Process

audit_id: 20260811_173324_335_deb0499d
timestamp: 2026-08-11T17:33:24.339
## Request
- original_query: 家里有鲈鱼，知识库里能做哪些菜？
- original_query_hash: 67cff2e33e0fbad4
- session_id: 2026-08-12-真实考试-001:old:S04-A-10
- request_mode: stream
- request_start: 2026-08-11T17:33:24.340
- evaluation_sample_id: 20260811_173324_335_deb0499d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:33:24.340
- end: 2026-08-11T17:33:24.340
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:33:24.341
- end: 2026-08-11T17:33:24.341
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 67cff2e33e0fbad4

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:33:24.341
- end: 2026-08-11T17:33:24.341
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 67cff2e33e0fbad4
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:33:24.341
- end: 2026-08-11T17:33:29.144
- duration_ms: 4802
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.45
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 该查询的核心是以“鲈鱼”这一食材为条件，在知识库中检索可制作的菜谱或菜名，属于面向单一主食材的菜谱聚合与筛选任务。虽然隐含“鲈鱼—可制作菜品”的关联关系，但通常不需要多跳推理、因果分析或复杂对比；通过关键词检索、食材字段过滤与语义召回即可有效完成，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 98, 'graph_rag_count': 1, 'total_queries': 99}
- route_stats_after: {'traditional_count': 99, 'graph_rag_count': 1, 'total_queries': 100}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鲈鱼', '清蒸鲈鱼', '红烧鲈鱼', '香煎鲈鱼', '糖醋鲈鱼', '鲈鱼汤', '烤鲈鱼']
- topic_keywords: ['家常菜', '鱼类菜肴', '海鲜', '清蒸', '红烧', '煎制', '烤制', '煲汤']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7370

## Hybrid Branch Status / entity_level
- keywords: ['鲈鱼', '清蒸鲈鱼', '红烧鲈鱼', '香煎鲈鱼', '糖醋鲈鱼', '鲈鱼汤', '烤鲈鱼']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 35

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '鱼类菜肴', '海鲜', '清蒸', '红烧', '煎制', '烤制', '煲汤']
- requested_k: 10
- actual_count: 7
- fallback_count: 7
- duration_ms: 56

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 387

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 7
- vector_count: 10
- origin_len: 19

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 19
- after_count: 16
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
- candidate_count: 16
- duration_ms: 17467
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, 'Ingredient': 1, '荤菜': 1, '素菜': 1}
- deferred_count: 8
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25244
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:33:24.341
- end: 2026-08-11T17:33:54.389
- duration_ms: 30047
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2791
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
- chunk_count: 188
- redacted_field: 2496
- total_duration_ms: 5729
- fallback_used: False

## Final Output
- answer_chars: 230
- answer_hash: d63f70c1093eba49
- success: True

## Request Complete
- request_end: 2026-08-11T17:34:00.139
- request_duration_ms: 35799
- success: True
- final_source: generation

