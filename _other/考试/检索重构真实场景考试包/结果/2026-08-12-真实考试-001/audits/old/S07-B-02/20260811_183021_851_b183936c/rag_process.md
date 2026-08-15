# RAG Process

audit_id: 20260811_183021_851_b183936c
timestamp: 2026-08-11T18:30:21.852
## Request
- original_query: 希望川菜里蔬菜多一点，有哪些做法比较贴近这种偏好？
- original_query_hash: f94eea10e6ce7c11
- session_id: 2026-08-12-真实考试-001:old:S07-B-02
- request_mode: stream
- request_start: 2026-08-11T18:30:21.852
- evaluation_sample_id: 20260811_183021_851_b183936c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:30:21.853
- end: 2026-08-11T18:30:21.853
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:30:21.853
- end: 2026-08-11T18:30:21.853
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: f94eea10e6ce7c11

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:30:21.854
- end: 2026-08-11T18:30:21.854
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: f94eea10e6ce7c11
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:30:21.854
- end: 2026-08-11T18:30:33.852
- duration_ms: 11997
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.55
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.87
- reasoning: 该查询属于带偏好约束的菜品/做法推荐：需识别“川菜”菜系范围，理解“蔬菜多一点”的配料偏好，并筛选或改造符合该偏好的做法。明确实体包括“川菜”“蔬菜”“做法”。需要一定的条件匹配与轻度对比分析，例如区分以肉类为主、蔬菜为辅的川菜和本身蔬菜占比较高或适合增加蔬菜的做法；不需要跨多个知识节点进行复杂多跳推理，也不涉及因果分析。因此适合使用关键词检索、菜谱/菜品标签过滤与语义召回结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 157, 'graph_rag_count': 33, 'total_queries': 190}
- route_stats_after: {'traditional_count': 158, 'graph_rag_count': 33, 'total_queries': 191}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鱼香茄子', '地三鲜', '干煸四季豆', '炝炒莲白', '手撕包菜', '麻婆豆腐', '回锅肉', '青椒', '茄子', '四季豆', '莲白', '包菜', '豆腐', '木耳', '笋']
- topic_keywords: ['川菜', '蔬菜多', '荤素搭配', '素菜', '家常菜', '麻辣', '香辣', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3928

## Hybrid Branch Status / entity_level
- keywords: ['鱼香茄子', '地三鲜', '干煸四季豆', '炝炒莲白', '手撕包菜', '麻婆豆腐', '回锅肉', '青椒', '茄子', '四季豆', '莲白', '包菜', '豆腐', '木耳', '笋']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 102

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '蔬菜多', '荤素搭配', '素菜', '家常菜', '麻辣', '香辣', '下饭菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 101

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 687

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
- seed_count: 4
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 28
- duration_ms: 18004
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 1, '主食': 1, '通用知识': 1, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 汤面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22667
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:30:21.854
- end: 2026-08-11T18:30:56.521
- duration_ms: 34666
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3391
- retrieval_levels: ['', 'context_expansion']
- search_types: ['technique_expansion', 'vector_enhanced']
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
- chunk_count: 1248
- redacted_field: 10060
- total_duration_ms: 58363
- fallback_used: False

## Final Output
- answer_chars: 1588
- answer_hash: 38fbf5d2b8a44155
- success: True

## Request Complete
- request_end: 2026-08-11T18:31:54.914
- request_duration_ms: 93061
- success: True
- final_source: generation

