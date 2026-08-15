# RAG Process

audit_id: 20260811_173045_870_6ebd80a2
timestamp: 2026-08-11T17:30:45.872
## Request
- original_query: 家里有土豆，知识库里能做哪些菜？
- original_query_hash: 625242350d1dff72
- session_id: 2026-08-12-真实考试-001:old:S04-A-06
- request_mode: stream
- request_start: 2026-08-11T17:30:45.872
- evaluation_sample_id: 20260811_173045_870_6ebd80a2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:30:45.873
- end: 2026-08-11T17:30:45.873
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:30:45.874
- end: 2026-08-11T17:30:45.874
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 625242350d1dff72

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:30:45.875
- end: 2026-08-11T17:30:45.875
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 625242350d1dff72
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:30:45.875
- end: 2026-08-11T17:30:52.066
- duration_ms: 6190
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.45
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 查询核心是以“土豆”这一食材实体检索知识库中的相关菜谱，属于明确的食材-菜品关联匹配与结果筛选。无需多跳推理、因果分析或对比分析；可通过关键词检索、菜谱标签/字段过滤及语义召回直接获取包含土豆的菜品，因此适合 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 94, 'graph_rag_count': 1, 'total_queries': 95}
- route_stats_after: {'traditional_count': 95, 'graph_rag_count': 1, 'total_queries': 96}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['土豆']
- topic_keywords: ['家常菜', '烹饪知识']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6067

## Hybrid Branch Status / entity_level
- keywords: ['土豆']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 14

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '烹饪知识']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 16

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 540

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 2
- vector_count: 10
- origin_len: 13

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 13
- after_count: 12
- duplicate_count: 1

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
- duration_ms: 9698
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '荤菜': 2, '主食': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 16319
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:30:45.875
- end: 2026-08-11T17:31:08.386
- duration_ms: 22510
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1553
- retrieval_levels: ['']
- search_types: ['vector_enhanced']
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
- chunk_count: 1
- redacted_field: 12247
- total_duration_ms: 12250
- fallback_used: False

## Final Output
- answer_chars: 385
- answer_hash: 31eebf8168632916
- success: True

## Request Complete
- request_end: 2026-08-11T17:31:20.659
- request_duration_ms: 34787
- success: True
- final_source: generation

