# RAG Process

audit_id: 20260811_173640_804_c132667c
timestamp: 2026-08-11T17:36:40.808
## Request
- original_query: 有鸭肉可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 7b066efcaf46ec37
- session_id: 2026-08-12-真实考试-001:old:S04-B-04
- request_mode: stream
- request_start: 2026-08-11T17:36:40.808
- evaluation_sample_id: 20260811_173640_804_c132667c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:36:40.810
- end: 2026-08-11T17:36:40.810
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:36:40.811
- end: 2026-08-11T17:36:40.811
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 7b066efcaf46ec37

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:36:40.811
- end: 2026-08-11T17:36:40.811
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: 7b066efcaf46ec37
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:36:40.811
- end: 2026-08-11T17:36:48.677
- duration_ms: 7865
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.55
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询以“鸭肉”为核心食材，要求检索可制作的菜品，并进一步验证菜谱配料表中确实包含鸭肉。本质是食材—菜谱之间的包含关系筛选与事实核验，属于中等复杂度的直接检索任务。无需多跳推理、因果分析或跨实体对比；可通过关键词检索、菜谱字段过滤及配料表匹配完成，因此推荐hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 102, 'graph_rag_count': 1, 'total_queries': 103}
- route_stats_after: {'traditional_count': 103, 'graph_rag_count': 1, 'total_queries': 104}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸭肉', '北京烤鸭', '啤酒鸭', '红烧鸭肉', '盐水鸭', '南京板鸭', '老鸭汤', '姜母鸭', '烤鸭', '鸭血粉丝汤']
- topic_keywords: ['鸭肉菜谱', '家常菜', '禽肉料理', '炖煮', '红烧', '焖烧', '煲汤', '烤制']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 10179

## Hybrid Branch Status / entity_level
- keywords: ['鸭肉', '北京烤鸭', '啤酒鸭', '红烧鸭肉', '盐水鸭', '南京板鸭', '老鸭汤', '姜母鸭', '烤鸭', '鸭血粉丝汤']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 13

## Hybrid Branch Status / topic_level
- keywords: ['鸭肉菜谱', '家常菜', '禽肉料理', '炖煮', '红烧', '焖烧', '煲汤', '烤制']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 29

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 346

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 8
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 16
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['如何决策吃什么', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 13283
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '通用知识': 1, '烹饪技巧': 1, 'Ingredient': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23841
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:36:40.811
- end: 2026-08-11T17:37:12.519
- duration_ms: 31707
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2623
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
- chunk_count: 321
- redacted_field: 2350
- total_duration_ms: 8667
- fallback_used: False

## Final Output
- answer_chars: 390
- answer_hash: 43bb3872bf264423
- success: True

## Request Complete
- request_end: 2026-08-11T17:37:21.209
- request_duration_ms: 40400
- success: True
- final_source: generation

