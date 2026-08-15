# RAG Process

audit_id: 20260811_183154_933_0efb6857
timestamp: 2026-08-11T18:31:54.934
## Request
- original_query: 晚餐想少一些油腻感，想吃川菜，有哪些做法比较贴近这种偏好？
- original_query_hash: e7eb342de8d5e70a
- session_id: 2026-08-12-真实考试-001:old:S07-B-03
- request_mode: stream
- request_start: 2026-08-11T18:31:54.935
- evaluation_sample_id: 20260811_183154_933_0efb6857
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:31:54.937
- end: 2026-08-11T18:31:54.937
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:31:54.937
- end: 2026-08-11T18:31:54.937
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 29
- enhanced_query_length: 29
- enhanced_query_hash: e7eb342de8d5e70a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:31:54.938
- end: 2026-08-11T18:31:54.938
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 29
- analysis_input_query_hash: e7eb342de8d5e70a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:31:54.938
- end: 2026-08-11T18:32:06.684
- duration_ms: 11746
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带偏好约束的菜谱/做法推荐：用户限定了用餐场景（晚餐）、菜系（川菜）和口感偏好（少油腻），需要从川菜做法中筛选或调整出清爽、少油、少重芡、少油炸的方案。它需要轻量级的属性匹配与对比分析，例如比较蒸、煮、炝拌、清炒等做法相对于干煸、回锅、油炸类做法的油腻程度；但通常不需要跨多个实体进行多跳推理，也不涉及复杂的历史、地理或因果关系网络。明确实体/概念可识别为“晚餐”“川菜”“做法（烹饪方式）”，其中“少油腻感”是核心偏好约束。适合使用关键词检索、语义召回及菜品属性过滤相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 158, 'graph_rag_count': 33, 'total_queries': 191}
- route_stats_after: {'traditional_count': 159, 'graph_rag_count': 33, 'total_queries': 192}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['酸菜鱼', '清蒸鱼', '凉拌鸡丝', '凉拌木耳', '炝拌菠菜', '豆花', '冬瓜', '菌菇', '花椒', '辣椒', '醋']
- topic_keywords: ['川菜', '少油', '清淡', '低脂', '开胃', '酸辣', '凉拌菜', '蒸菜', '汤菜', '晚餐']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6102

## Hybrid Branch Status / entity_level
- keywords: ['酸菜鱼', '清蒸鱼', '凉拌鸡丝', '凉拌木耳', '炝拌菠菜', '豆花', '冬瓜', '菌菇', '花椒', '辣椒', '醋']
- requested_k: 10
- actual_count: 10
- fallback_count: 3
- duration_ms: 86

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '少油', '清淡', '低脂', '开胃', '酸辣', '凉拌菜', '蒸菜', '汤菜', '晚餐']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 86

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 662

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 25
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['去腥', '厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 26
- duration_ms: 18106
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '荤菜': 1, '素菜': 1, '主食,凉菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 酸辣蕨根粉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24895
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:31:54.938
- end: 2026-08-11T18:32:31.580
- duration_ms: 36642
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2416
- retrieval_levels: ['context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level']
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
- chunk_count: 592
- redacted_field: 2087
- total_duration_ms: 13738
- fallback_used: False

## Final Output
- answer_chars: 766
- answer_hash: 716b9b03c9e9a997
- success: True

## Request Complete
- request_end: 2026-08-11T18:32:45.343
- request_duration_ms: 50407
- success: True
- final_source: generation

