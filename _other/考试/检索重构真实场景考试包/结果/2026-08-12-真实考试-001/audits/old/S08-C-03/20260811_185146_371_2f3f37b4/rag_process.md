# RAG Process

audit_id: 20260811_185146_371_2f3f37b4
timestamp: 2026-08-11T18:51:46.371
## Request
- original_query: 请查云岚23号幻味砂锅的做法；未收录时只说明未找到，不要根据名称猜配方。
- original_query_hash: a6eb529da91f3630
- session_id: 2026-08-12-真实考试-001:old:S08-C-03
- request_mode: stream
- request_start: 2026-08-11T18:51:46.372
- evaluation_sample_id: 20260811_185146_371_2f3f37b4
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:51:46.373
- end: 2026-08-11T18:51:46.373
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:51:46.374
- end: 2026-08-11T18:51:46.374
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: a6eb529da91f3630

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:51:46.374
- end: 2026-08-11T18:51:46.374
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: a6eb529da91f3630
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:51:46.375
- end: 2026-08-11T18:51:53.041
- duration_ms: 6665
- analysis_mode: llm
- query_complexity: 0.28
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是针对明确菜品名称“云岚23号幻味砂锅”的定向做法检索，并包含严格的结果约束：仅在知识库已收录时返回做法，未收录则明确说明未找到，禁止基于名称进行配方推测。查询不涉及多实体关系、多跳推理、因果分析或对比分析，适合采用关键词、精确短语匹配、别名匹配及文档元数据过滤的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 187, 'graph_rag_count': 33, 'total_queries': 220}
- route_stats_after: {'traditional_count': 188, 'graph_rag_count': 33, 'total_queries': 221}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚23号幻味砂锅']
- topic_keywords: []
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 1516

## Hybrid Branch Status / entity_level
- keywords: ['云岚23号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 3

## Hybrid Branch Status / topic_level
- keywords: []
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 3

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 547

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 0
- vector_count: 10
- origin_len: 10

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 10
- after_count: 10
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 8
- doc_names: ['炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 11
- duration_ms: 16288
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '烹饪技巧': 1, '汤类': 1, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 韭菜盒子
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18374
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:51:46.375
- end: 2026-08-11T18:52:11.416
- duration_ms: 25041
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1739
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
- chunk_count: 19
- redacted_field: 2009
- total_duration_ms: 2538
- fallback_used: False

## Final Output
- answer_chars: 24
- answer_hash: 1234b2b807992657
- success: True

## Request Complete
- request_end: 2026-08-11T18:52:13.973
- request_duration_ms: 27601
- success: True
- final_source: generation

