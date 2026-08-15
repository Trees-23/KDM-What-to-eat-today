# RAG Process

audit_id: 20260811_180317_909_294d0338
timestamp: 2026-08-11T18:03:17.912
## Request
- original_query: 想做一道下饭的素菜。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: 617fbc207ab38d40
- session_id: 2026-08-12-真实考试-001:old:S06-A-06
- request_mode: stream
- request_start: 2026-08-11T18:03:17.913
- evaluation_sample_id: 20260811_180317_909_294d0338
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:03:17.914
- end: 2026-08-11T18:03:17.914
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:03:17.914
- end: 2026-08-11T18:03:17.914
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 29
- enhanced_query_length: 29
- enhanced_query_hash: 617fbc207ab38d40

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:03:17.914
- end: 2026-08-11T18:03:17.914
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 29
- analysis_input_query_hash: 617fbc207ab38d40
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:03:17.915
- end: 2026-08-11T18:03:25.639
- duration_ms: 7724
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.87
- reasoning: 该查询的核心任务是在知识库菜品中进行条件筛选和排序：首先限定“素菜”类别，再依据“下饭”这一口味/适配属性（通常关联咸鲜、微辣、酱香、口感丰富等特征）推荐最合适的菜品，并给出匹配依据。查询不包含明确的菜名或复杂实体网络，主要需要对候选菜品进行属性匹配与横向比较；不需要多跳推理或因果分析，但需要轻度的比较分析。因此适合采用 hybrid_traditional，通过关键词检索、菜品标签过滤及语义排序获得结果。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 123, 'graph_rag_count': 32, 'total_queries': 155}
- route_stats_after: {'traditional_count': 124, 'graph_rag_count': 32, 'total_queries': 156}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: []
- topic_keywords: ['素食', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2624

## Hybrid Branch Status / entity_level
- keywords: []
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / topic_level
- keywords: ['素食', '下饭菜']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 7

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 458

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 0
- vector_count: 10
- origin_len: 10

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 10
- after_count: 7
- duplicate_count: 3

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
- candidate_count: 8
- duration_ms: 7942
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'通用知识': 1, '烹饪技巧': 1, '主食': 2, '荤菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 11038
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:03:17.914
- end: 2026-08-11T18:03:36.679
- duration_ms: 18764
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1936
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
- chunk_count: 203
- redacted_field: 3875
- total_duration_ms: 7860
- fallback_used: False

## Final Output
- answer_chars: 259
- answer_hash: 558ac0ec39c4ed8c
- success: True

## Request Complete
- request_end: 2026-08-11T18:03:44.554
- request_duration_ms: 26641
- success: True
- final_source: generation

