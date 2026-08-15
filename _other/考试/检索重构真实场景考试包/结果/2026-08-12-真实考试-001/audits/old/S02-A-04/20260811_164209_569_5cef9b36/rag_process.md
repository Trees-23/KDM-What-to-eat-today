# RAG Process

audit_id: 20260811_164209_569_5cef9b36
timestamp: 2026-08-11T16:42:09.570
## Request
- original_query: 糖醋排骨的第 1 步应该怎么做？
- original_query_hash: 7190f15974f2e88a
- session_id: 2026-08-12-真实考试-001:old:S02-A-04
- request_mode: stream
- request_start: 2026-08-11T16:42:09.570
- evaluation_sample_id: 20260811_164209_569_5cef9b36
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:42:09.571
- end: 2026-08-11T16:42:09.571
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:42:09.571
- end: 2026-08-11T16:42:09.571
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 7190f15974f2e88a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:42:09.571
- end: 2026-08-11T16:42:09.571
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 7190f15974f2e88a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:42:09.572
- end: 2026-08-11T16:42:13.557
- duration_ms: 3985
- analysis_mode: llm
- query_complexity: 0.15
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对菜谱“糖醋排骨”中具体步骤“第1步”的直接定位式信息查找，仅需从相关菜谱文本中检索并抽取首个制作步骤。无需多跳推理、因果分析或对比分析。明确实体包括菜品实体“糖醋排骨”和流程步骤实体“第1步”。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 33, 'graph_rag_count': 0, 'total_queries': 33}
- route_stats_after: {'traditional_count': 34, 'graph_rag_count': 0, 'total_queries': 34}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['糖醋排骨']
- topic_keywords: ['烹饪步骤', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2305

## Hybrid Branch Status / topic_level
- keywords: ['烹饪步骤', '烹饪技巧']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 11

## Hybrid Branch Status / entity_level
- keywords: ['糖醋排骨']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 16

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 670

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
- duration_ms: 15313
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '汤类': 2}
- deferred_count: 4
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18307
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:42:09.572
- end: 2026-08-11T16:42:31.866
- duration_ms: 22294
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3342
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
- chunk_count: 116
- redacted_field: 5810
- total_duration_ms: 8262
- fallback_used: False

## Final Output
- answer_chars: 146
- answer_hash: f58ffd01ca6619f4
- success: True

## Request Complete
- request_end: 2026-08-11T16:42:40.155
- request_duration_ms: 30585
- success: True
- final_source: generation

