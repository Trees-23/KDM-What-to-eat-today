# RAG Process

audit_id: 20260811_172655_297_bc6a67b3
timestamp: 2026-08-11T17:26:55.299
## Request
- original_query: 家里有牛肉，知识库里能做哪些菜？
- original_query_hash: d6b623295d0d1c45
- session_id: 2026-08-12-真实考试-001:old:S04-A-01
- request_mode: stream
- request_start: 2026-08-11T17:26:55.299
- evaluation_sample_id: 20260811_172655_297_bc6a67b3
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:26:55.300
- end: 2026-08-11T17:26:55.300
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:26:55.301
- end: 2026-08-11T17:26:55.301
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: d6b623295d0d1c45

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:26:55.302
- end: 2026-08-11T17:26:55.302
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: d6b623295d0d1c45
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:26:55.303
- end: 2026-08-11T17:27:29.149
- duration_ms: 33846
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.45
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是以“牛肉”为食材条件，从知识库中检索可制作的“菜品/食谱”。主要涉及食材与菜谱之间的直接包含或适用关系，不需要多跳推理、因果分析或复杂对比。可通过关键词检索、食材字段过滤及语义召回匹配相关菜谱，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 89, 'graph_rag_count': 1, 'total_queries': 90}
- route_stats_after: {'traditional_count': 90, 'graph_rag_count': 1, 'total_queries': 91}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['牛肉']
- topic_keywords: ['菜品', '牛肉菜谱']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7351

## Hybrid Branch Status / topic_level
- keywords: ['菜品', '牛肉菜谱']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 22

## Hybrid Branch Status / entity_level
- keywords: ['牛肉']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 27

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 529

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 10
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 11
- duration_ms: 16521
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, '荤菜': 2, '汤类': 1}
- deferred_count: 5
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24434
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:26:55.303
- end: 2026-08-11T17:27:53.585
- duration_ms: 58282
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6937
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
- chunk_count: 438
- redacted_field: 3117
- total_duration_ms: 12251
- fallback_used: False

## Final Output
- answer_chars: 534
- answer_hash: a1505c29976d798e
- success: True

## Request Complete
- request_end: 2026-08-11T17:28:05.857
- request_duration_ms: 70557
- success: True
- final_source: generation

