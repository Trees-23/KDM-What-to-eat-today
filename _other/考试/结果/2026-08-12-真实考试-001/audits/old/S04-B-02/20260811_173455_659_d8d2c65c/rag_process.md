# RAG Process

audit_id: 20260811_173455_659_d8d2c65c
timestamp: 2026-08-11T17:34:55.659
## Request
- original_query: 有排骨可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 471e8361c69a888c
- session_id: 2026-08-12-真实考试-001:old:S04-B-02
- request_mode: stream
- request_start: 2026-08-11T17:34:55.660
- evaluation_sample_id: 20260811_173455_659_d8d2c65c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:34:55.660
- end: 2026-08-11T17:34:55.660
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:34:55.660
- end: 2026-08-11T17:34:55.660
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 471e8361c69a888c

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:34:55.661
- end: 2026-08-11T17:34:55.661
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: 471e8361c69a888c
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:34:55.661
- end: 2026-08-11T17:35:08.576
- duration_ms: 12914
- analysis_mode: llm
- query_complexity: 0.42
- relationship_intensity: 0.55
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心实体为“排骨”（食材实体），目标是发现可制作的菜品，并验证候选菜谱的配料表中确实包含排骨。该任务主要依赖关键词/语义检索、菜谱字段过滤与配料文本匹配，属于中等复杂度的实体—菜谱包含关系查询；不需要多跳推理、因果分析或复杂关系网络建模，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 100, 'graph_rag_count': 1, 'total_queries': 101}
- route_stats_after: {'traditional_count': 101, 'graph_rag_count': 1, 'total_queries': 102}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['排骨', '红烧排骨', '糖醋排骨', '清蒸排骨', '椒盐排骨', '排骨汤', '玉米排骨汤', '莲藕排骨汤', '冬瓜排骨汤', '土豆烧排骨']
- topic_keywords: ['家常菜', '排骨菜谱', '炖汤', '红烧', '糖醋', '蒸菜', '确实包含食材']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4207

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '排骨菜谱', '炖汤', '红烧', '糖醋', '蒸菜', '确实包含食材']
- requested_k: 10
- actual_count: 3
- fallback_count: 3
- duration_ms: 42

## Hybrid Branch Status / entity_level
- keywords: ['排骨', '红烧排骨', '糖醋排骨', '清蒸排骨', '椒盐排骨', '排骨汤', '玉米排骨汤', '莲藕排骨汤', '冬瓜排骨汤', '土豆烧排骨']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 47

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 291

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 3
- vector_count: 10
- origin_len: 16

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 16
- after_count: 12
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 12
- duration_ms: 14246
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '汤类': 2, 'Ingredient': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18765
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:34:55.661
- end: 2026-08-11T17:35:27.342
- duration_ms: 31680
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2524
- retrieval_levels: ['', 'entity']
- search_types: ['entity_level', 'vector_enhanced']
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
- chunk_count: 550
- redacted_field: 6108
- total_duration_ms: 25485
- fallback_used: False

## Final Output
- answer_chars: 699
- answer_hash: 589a5bbffb2800e4
- success: True

## Request Complete
- request_end: 2026-08-11T17:35:52.838
- request_duration_ms: 57178
- success: True
- final_source: generation

