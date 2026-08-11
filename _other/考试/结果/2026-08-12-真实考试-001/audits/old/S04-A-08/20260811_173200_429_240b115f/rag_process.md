# RAG Process

audit_id: 20260811_173200_429_240b115f
timestamp: 2026-08-11T17:32:00.435
## Request
- original_query: 家里有西红柿，知识库里能做哪些菜？
- original_query_hash: f8afbb1d3cb512ac
- session_id: 2026-08-12-真实考试-001:old:S04-A-08
- request_mode: stream
- request_start: 2026-08-11T17:32:00.436
- evaluation_sample_id: 20260811_173200_429_240b115f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:32:00.437
- end: 2026-08-11T17:32:00.437
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:32:00.437
- end: 2026-08-11T17:32:00.437
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 17
- enhanced_query_length: 17
- enhanced_query_hash: f8afbb1d3cb512ac

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:32:00.437
- end: 2026-08-11T17:32:00.437
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 17
- analysis_input_query_hash: f8afbb1d3cb512ac
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:32:00.438
- end: 2026-08-11T17:32:07.936
- duration_ms: 7498
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.5
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是以“西红柿”这一食材为条件，在知识库的菜谱中检索可制作的菜品。它需要识别菜谱与食材之间的包含关系，并可能根据菜谱标题、食材列表、别名（如番茄）进行匹配，但不涉及复杂的多跳关系网络、因果分析或多实体对比。适合采用关键词检索结合语义检索的 hybrid_traditional 策略，以召回包含西红柿/番茄的相关菜谱并进行排序。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 96, 'graph_rag_count': 1, 'total_queries': 97}
- route_stats_after: {'traditional_count': 97, 'graph_rag_count': 1, 'total_queries': 98}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西红柿', '番茄炒蛋', '番茄蛋汤', '番茄炖牛腩', '番茄炒面', '凉拌番茄']
- topic_keywords: ['家常菜', '快手菜', '素食', '汤菜', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3761

## Hybrid Branch Status / entity_level
- keywords: ['西红柿', '番茄炒蛋', '番茄蛋汤', '番茄炖牛腩', '番茄炒面', '凉拌番茄']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 25

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '快手菜', '素食', '汤菜', '下饭菜']
- requested_k: 10
- actual_count: 6
- fallback_count: 6
- duration_ms: 55

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 364

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 6
- vector_count: 10
- origin_len: 17

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 17
- after_count: 14
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
- candidate_count: 14
- duration_ms: 11814
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '荤菜': 1, 'Ingredient': 1, '汤类': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 15953
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:32:00.438
- end: 2026-08-11T17:32:23.891
- duration_ms: 23453
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1906
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
- chunk_count: 265
- redacted_field: 7158
- total_duration_ms: 12814
- fallback_used: False

## Final Output
- answer_chars: 337
- answer_hash: 8c33f6c92b57e287
- success: True

## Request Complete
- request_end: 2026-08-11T17:32:36.716
- request_duration_ms: 36279
- success: True
- final_source: generation

