# RAG Process

audit_id: 20260811_172847_741_6669bc1b
timestamp: 2026-08-11T17:28:47.743
## Request
- original_query: 家里有鸡肉，知识库里能做哪些菜？
- original_query_hash: 2b70893df36e6191
- session_id: 2026-08-12-真实考试-001:old:S04-A-03
- request_mode: stream
- request_start: 2026-08-11T17:28:47.743
- evaluation_sample_id: 20260811_172847_741_6669bc1b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:28:47.744
- end: 2026-08-11T17:28:47.744
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:28:47.745
- end: 2026-08-11T17:28:47.745
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 2b70893df36e6191

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:28:47.746
- end: 2026-08-11T17:28:47.746
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 2b70893df36e6191
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:28:47.746
- end: 2026-08-11T17:28:54.998
- duration_ms: 7252
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.45
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询的核心意图是基于食材“鸡肉”从知识库中筛选可制作的菜品，属于明确的食材到菜谱的关联检索。虽存在“鸡肉—菜品”的一对多关系，但不要求跨多实体、多跳推理，也不涉及因果或对比分析。适合采用关键词匹配、向量语义召回及菜谱字段过滤相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 91, 'graph_rag_count': 1, 'total_queries': 92}
- route_stats_after: {'traditional_count': 92, 'graph_rag_count': 1, 'total_queries': 93}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸡肉']
- topic_keywords: ['鸡肉菜品', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2148

## Hybrid Branch Status / entity_level
- keywords: ['鸡肉']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 26

## Hybrid Branch Status / topic_level
- keywords: ['鸡肉菜品', '家常菜']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 31

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 548

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 2
- vector_count: 10
- origin_len: 13

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 13
- after_count: 13
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['如何决策吃什么', '腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 17490
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'通用知识': 1, '荤菜': 2, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20209
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:28:47.746
- end: 2026-08-11T17:29:15.208
- duration_ms: 27462
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4529
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
- chunk_count: 377
- redacted_field: 2619
- total_duration_ms: 10149
- fallback_used: False

## Final Output
- answer_chars: 475
- answer_hash: b95e2948ccbbe454
- success: True

## Request Complete
- request_end: 2026-08-11T17:29:25.375
- request_duration_ms: 37632
- success: True
- final_source: generation

