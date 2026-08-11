# RAG Process

audit_id: 20260811_180048_152_a65f3f62
timestamp: 2026-08-11T18:00:48.152
## Request
- original_query: 下班很晚，想找准备步骤少的家常菜。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: e81a54d181c25f0c
- session_id: 2026-08-12-真实考试-001:old:S06-A-02
- request_mode: stream
- request_start: 2026-08-11T18:00:48.153
- evaluation_sample_id: 20260811_180048_152_a65f3f62
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:00:48.154
- end: 2026-08-11T18:00:48.154
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:00:48.155
- end: 2026-08-11T18:00:48.155
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: e81a54d181c25f0c

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:00:48.155
- end: 2026-08-11T18:00:48.155
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: e81a54d181c25f0c
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:00:48.156
- end: 2026-08-11T18:00:56.417
- duration_ms: 8261
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.42
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询不是单纯查找某一道菜的做法，而是需要依据“下班很晚”和“准备步骤少”两个约束，从知识库中的家常菜候选中进行筛选、排序和推荐，并说明推荐依据。因此具有中等复杂度，且需要轻量级的条件匹配与对比分析。但查询并未涉及多实体、多层关系网络、历史因果或跨领域知识发现，不需要图谱多跳推理。建议采用 hybrid_traditional，通过关键词检索（如“快手菜、家常菜、少步骤、15分钟”）结合语义检索召回菜品，再利用准备时长、食材数量、预处理要求、烹饪步骤数等结构化字段进行排序，选出最合适的菜品并生成依据。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 120, 'graph_rag_count': 31, 'total_queries': 151}
- route_stats_after: {'traditional_count': 121, 'graph_rag_count': 31, 'total_queries': 152}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: []
- topic_keywords: ['快手菜', '家常菜', '准备步骤少', '省时', '简单易做', '晚餐']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4744

## Hybrid Branch Status / topic_level
- keywords: ['快手菜', '家常菜', '准备步骤少', '省时', '简单易做', '晚餐']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 35

## Hybrid Branch Status / entity_level
- keywords: []
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 52

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 453

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 10
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 17
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 14984
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'通用知识': 1, '主食': 2, '荤菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 姜葱捞鸡
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20199
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:00:48.156
- end: 2026-08-11T18:01:16.617
- duration_ms: 28461
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3141
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
- chunk_count: 230
- redacted_field: 2168
- total_duration_ms: 6648
- fallback_used: False

## Final Output
- answer_chars: 289
- answer_hash: fceafe03d3354b73
- success: True

## Request Complete
- request_end: 2026-08-11T18:01:23.289
- request_duration_ms: 35136
- success: True
- final_source: generation

