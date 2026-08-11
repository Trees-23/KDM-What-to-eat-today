# RAG Process

audit_id: 20260811_165244_983_71fc069a
timestamp: 2026-08-11T16:52:44.985
## Request
- original_query: 只回答蛋包饭的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: e50caec48b9b00cb
- session_id: 2026-08-12-真实考试-001:old:S02-C-01
- request_mode: stream
- request_start: 2026-08-11T16:52:44.985
- evaluation_sample_id: 20260811_165244_983_71fc069a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:52:44.986
- end: 2026-08-11T16:52:44.986
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:52:44.986
- end: 2026-08-11T16:52:44.986
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: e50caec48b9b00cb

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:52:44.987
- end: 2026-08-11T16:52:44.987
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: e50caec48b9b00cb
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:52:44.987
- end: 2026-08-11T16:52:53.525
- duration_ms: 8538
- analysis_mode: llm
- query_complexity: 0.42
- relationship_intensity: 0.35
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 查询核心是定位“蛋包饭”菜谱中的“第1步”，并返回该步骤的来源。虽然包含“不得混入后续步骤”的范围约束与溯源要求，但不涉及多实体、多关系网络或知识发现。无需多跳推理、因果分析或对比分析，仅需通过关键词/语义检索召回蛋包饭菜谱，并按步骤编号进行精确过滤与来源字段返回，因此适合 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 50, 'graph_rag_count': 0, 'total_queries': 50}
- route_stats_after: {'traditional_count': 51, 'graph_rag_count': 0, 'total_queries': 51}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蛋包饭', '菜谱步骤']
- topic_keywords: ['菜谱步骤', '步骤顺序', '烹饪流程']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2588

## Hybrid Branch Status / topic_level
- keywords: ['菜谱步骤', '步骤顺序', '烹饪流程']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 12

## Hybrid Branch Status / entity_level
- keywords: ['蛋包饭', '菜谱步骤']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 24

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 475

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 8
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
- candidate_count: 8
- duration_ms: 14500
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '素菜': 2, '水产': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 17577
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:52:44.987
- end: 2026-08-11T16:53:11.104
- duration_ms: 26117
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3530
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
- chunk_count: 66
- redacted_field: 7593
- total_duration_ms: 8603
- fallback_used: False

## Final Output
- answer_chars: 82
- answer_hash: 0dd1c580a59a2013
- success: True

## Request Complete
- request_end: 2026-08-11T16:53:19.734
- request_duration_ms: 34748
- success: True
- final_source: generation

