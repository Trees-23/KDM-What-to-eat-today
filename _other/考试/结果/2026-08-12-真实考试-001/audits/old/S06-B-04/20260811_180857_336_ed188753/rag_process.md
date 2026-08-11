# RAG Process

audit_id: 20260811_180857_336_ed188753
timestamp: 2026-08-11T18:08:57.336
## Request
- original_query: 想做口感软糯的肉菜，帮我找几个贴近这个需求的做法。
- original_query_hash: 45c1b7f059e76434
- session_id: 2026-08-12-真实考试-001:old:S06-B-04
- request_mode: stream
- request_start: 2026-08-11T18:08:57.337
- evaluation_sample_id: 20260811_180857_336_ed188753
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:08:57.338
- end: 2026-08-11T18:08:57.338
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:08:57.338
- end: 2026-08-11T18:08:57.338
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: 45c1b7f059e76434

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:08:57.339
- end: 2026-08-11T18:08:57.339
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: 45c1b7f059e76434
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:08:57.339
- end: 2026-08-11T18:09:09.164
- duration_ms: 11824
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带条件的菜谱推荐需求，核心约束是“肉菜”品类、“软糯”口感和“做法”输出形式。需要从菜谱中筛选出适合通过炖、焖、蒸、卤等烹饪方式获得软糯口感的肉类菜肴，并按需求匹配多个候选结果。虽存在口感、食材类别与烹饪方法之间的关联，但不涉及复杂知识网络、多跳事实追溯或因果机制分析，使用关键词检索、语义召回及菜谱标签过滤的 hybrid_traditional 策略更合适。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 130, 'graph_rag_count': 33, 'total_queries': 163}
- route_stats_after: {'traditional_count': 131, 'graph_rag_count': 33, 'total_queries': 164}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['红烧肉', '粉蒸肉', '东坡肉', '炖牛腩', '黄豆焖猪蹄', '排骨']
- topic_keywords: ['肉菜', '软糯', '软烂', '入口即化', '炖煮', '焖烧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5520

## Hybrid Branch Status / entity_level
- keywords: ['红烧肉', '粉蒸肉', '东坡肉', '炖牛腩', '黄豆焖猪蹄', '排骨']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 17

## Hybrid Branch Status / topic_level
- keywords: ['肉菜', '软糯', '软烂', '入口即化', '炖煮', '焖烧']
- requested_k: 10
- actual_count: 7
- fallback_count: 7
- duration_ms: 25

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 448

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 7
- vector_count: 10
- origin_len: 19

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 19
- after_count: 17
- duplicate_count: 2

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
- candidate_count: 18
- duration_ms: 10895
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 1, '通用知识': 1, '素菜': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 手撕包菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 16893
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:08:57.339
- end: 2026-08-11T18:09:26.059
- duration_ms: 28719
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1604
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
- chunk_count: 358
- redacted_field: 2301
- total_duration_ms: 9441
- fallback_used: False

## Final Output
- answer_chars: 453
- answer_hash: 2e8406dd80d90d27
- success: True

## Request Complete
- request_end: 2026-08-11T18:09:35.540
- request_duration_ms: 38202
- success: True
- final_source: generation

