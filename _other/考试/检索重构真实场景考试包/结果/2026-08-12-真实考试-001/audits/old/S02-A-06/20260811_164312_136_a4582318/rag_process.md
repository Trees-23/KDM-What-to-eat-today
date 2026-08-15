# RAG Process

audit_id: 20260811_164312_136_a4582318
timestamp: 2026-08-11T16:43:12.142
## Request
- original_query: 酱牛肉的第 1 步应该怎么做？
- original_query_hash: bd63462909f976d2
- session_id: 2026-08-12-真实考试-001:old:S02-A-06
- request_mode: stream
- request_start: 2026-08-11T16:43:12.143
- evaluation_sample_id: 20260811_164312_136_a4582318
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:43:12.144
- end: 2026-08-11T16:43:12.144
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:43:12.145
- end: 2026-08-11T16:43:12.145
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 15
- enhanced_query_length: 15
- enhanced_query_hash: bd63462909f976d2

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:43:12.146
- end: 2026-08-11T16:43:12.146
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 15
- analysis_input_query_hash: bd63462909f976d2
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:43:12.147
- end: 2026-08-11T16:43:18.583
- duration_ms: 6436
- analysis_mode: llm
- query_complexity: 0.12
- relationship_intensity: 0.08
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.97
- reasoning: 该查询是对特定菜品“酱牛肉”制作流程中“第1步”的直接定位型信息查找。只需从食谱或步骤化文档中检索并抽取首个操作步骤，不涉及多跳推理、因果分析、实体关系推断或方案对比。明确实体包括“酱牛肉”（菜品）和“第1步”（制作流程步骤/序号）。因此适合使用传统关键词检索结合语义检索的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 35, 'graph_rag_count': 0, 'total_queries': 35}
- route_stats_after: {'traditional_count': 36, 'graph_rag_count': 0, 'total_queries': 36}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['酱牛肉', '牛肉']
- topic_keywords: ['烹饪步骤', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2407

## Hybrid Branch Status / topic_level
- keywords: ['烹饪步骤', '烹饪技巧']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 14

## Hybrid Branch Status / entity_level
- keywords: ['酱牛肉', '牛肉']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 38

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 519

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 0
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 10
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 16398
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, 'Ingredient': 1}
- deferred_count: 7
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19337
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:43:12.147
- end: 2026-08-11T16:43:37.922
- duration_ms: 25775
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3119
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
- chunk_count: 49
- redacted_field: 2519
- total_duration_ms: 3579
- fallback_used: False

## Final Output
- answer_chars: 59
- answer_hash: c322ac30eb48898f
- success: True

## Request Complete
- request_end: 2026-08-11T16:43:41.521
- request_duration_ms: 29377
- success: True
- final_source: generation

