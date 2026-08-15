# RAG Process

audit_id: 20260811_181440_983_2f3feed8
timestamp: 2026-08-11T18:14:41.003
## Request
- original_query: 想吃酸甜口的菜，帮我找几个贴近这个需求的做法。
- original_query_hash: b16be0d7d78b2cfa
- session_id: 2026-08-12-真实考试-001:old:S06-B-10
- request_mode: stream
- request_start: 2026-08-11T18:14:41.003
- evaluation_sample_id: 20260811_181440_983_2f3feed8
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:14:41.005
- end: 2026-08-11T18:14:41.005
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:14:41.005
- end: 2026-08-11T18:14:41.005
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: b16be0d7d78b2cfa

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:14:41.006
- end: 2026-08-11T18:14:41.006
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: b16be0d7d78b2cfa
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:14:41.007
- end: 2026-08-11T18:14:48.460
- duration_ms: 7452
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询核心是按“酸甜口”这一口味偏好筛选菜品做法，属于带条件的菜谱检索与结果排序。需要轻量级语义匹配和对比，以识别糖醋类、茄汁类、果味酸甜类等贴近需求的菜品，并排除偏酸、偏甜或酸辣口味的结果；但不需要多跳推理、因果分析或复杂实体关系网络。明确实体主要为“酸甜口”（口味属性）和“菜/做法”（菜谱内容类型），适合采用关键词检索结合语义召回与排序的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 136, 'graph_rag_count': 33, 'total_queries': 169}
- route_stats_after: {'traditional_count': 137, 'graph_rag_count': 33, 'total_queries': 170}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['糖醋里脊', '糖醋排骨', '糖醋鱼', '咕咾肉', '糖醋藕片', '糖醋茄子', '番茄炒蛋', '菠萝']
- topic_keywords: ['酸甜口', '糖醋味', '开胃菜', '家常菜', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5354

## Hybrid Branch Status / entity_level
- keywords: ['糖醋里脊', '糖醋排骨', '糖醋鱼', '咕咾肉', '糖醋藕片', '糖醋茄子', '番茄炒蛋', '菠萝']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 21

## Hybrid Branch Status / topic_level
- keywords: ['酸甜口', '糖醋味', '开胃菜', '家常菜', '下饭菜']
- requested_k: 10
- actual_count: 3
- fallback_count: 3
- duration_ms: 26

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 544

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 3
- vector_count: 10
- origin_len: 15

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 15
- after_count: 15
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
- candidate_count: 16
- duration_ms: 10675
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '烹饪技巧': 1, '主食': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 16604
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:14:41.007
- end: 2026-08-11T18:15:05.064
- duration_ms: 24057
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1560
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 291
- redacted_field: 2311
- total_duration_ms: 8153
- fallback_used: False

## Final Output
- answer_chars: 363
- answer_hash: a57f89c5b708e44b
- success: True

## Request Complete
- request_end: 2026-08-11T18:15:13.235
- request_duration_ms: 32232
- success: True
- final_source: generation

