# RAG Process

audit_id: 20260811_164132_768_08d30ea9
timestamp: 2026-08-11T16:41:32.769
## Request
- original_query: 水煮牛肉的第 1 步应该怎么做？
- original_query_hash: 2abfc72e1fc3c7dc
- session_id: 2026-08-12-真实考试-001:old:S02-A-03
- request_mode: stream
- request_start: 2026-08-11T16:41:32.769
- evaluation_sample_id: 20260811_164132_768_08d30ea9
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:41:32.770
- end: 2026-08-11T16:41:32.770
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:41:32.770
- end: 2026-08-11T16:41:32.770
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 2abfc72e1fc3c7dc

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:41:32.771
- end: 2026-08-11T16:41:32.771
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 2abfc72e1fc3c7dc
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:41:32.771
- end: 2026-08-11T16:41:39.318
- duration_ms: 6546
- analysis_mode: llm
- query_complexity: 0.12
- relationship_intensity: 0.1
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.97
- reasoning: 该查询是对菜谱“水煮牛肉”中指定步骤“第1步”的直接定位与事实查找，不涉及多跳推理、因果分析或多方案对比。明确实体包括菜品名称“水煮牛肉”和流程步骤“第1步”；其中“水煮牛肉”为菜品实体，“第1步”为配方/烹饪流程中的步骤定位实体。适合采用关键词检索、向量语义检索及步骤字段过滤的 hybrid_traditional 策略快速获取答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 32, 'graph_rag_count': 0, 'total_queries': 32}
- route_stats_after: {'traditional_count': 33, 'graph_rag_count': 0, 'total_queries': 33}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['水煮牛肉', '牛肉']
- topic_keywords: ['川菜', '麻辣', '烹饪步骤']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 1592

## Hybrid Branch Status / entity_level
- keywords: ['水煮牛肉', '牛肉']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 12

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '麻辣', '烹饪步骤']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 33

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 612

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 19
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
- candidate_count: 19
- duration_ms: 24603
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 2, '主食,凉菜': 1}
- deferred_count: 9
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26831
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:41:32.771
- end: 2026-08-11T16:42:06.151
- duration_ms: 33380
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2134
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
- chunk_count: 65
- redacted_field: 1959
- total_duration_ms: 3367
- fallback_used: False

## Final Output
- answer_chars: 79
- answer_hash: 31a9dab9c7dc5bb9
- success: True

## Request Complete
- request_end: 2026-08-11T16:42:09.546
- request_duration_ms: 36776
- success: True
- final_source: generation

