# RAG Process

audit_id: 20260811_164419_097_acc4c023
timestamp: 2026-08-11T16:44:19.099
## Request
- original_query: 小炒黄牛肉的第 1 步应该怎么做？
- original_query_hash: 33793bbb657d8c0e
- session_id: 2026-08-12-真实考试-001:old:S02-A-08
- request_mode: stream
- request_start: 2026-08-11T16:44:19.100
- evaluation_sample_id: 20260811_164419_097_acc4c023
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:44:19.102
- end: 2026-08-11T16:44:19.102
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:44:19.103
- end: 2026-08-11T16:44:19.103
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 17
- enhanced_query_length: 17
- enhanced_query_hash: 33793bbb657d8c0e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:44:19.104
- end: 2026-08-11T16:44:19.104
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 17
- analysis_input_query_hash: 33793bbb657d8c0e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:44:19.104
- end: 2026-08-11T16:44:29.960
- duration_ms: 10855
- analysis_mode: llm
- query_complexity: 0.15
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对特定菜品“小炒黄牛肉”的指定流程节点“第1步”的直接信息查找，目标明确、答案通常可从菜谱步骤中直接定位。无需多跳推理、因果分析或对比分析。明确实体包括菜品实体“小炒黄牛肉”和流程步骤实体“第1步”，适合采用关键词匹配与语义检索结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 37, 'graph_rag_count': 0, 'total_queries': 37}
- route_stats_after: {'traditional_count': 38, 'graph_rag_count': 0, 'total_queries': 38}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['小炒黄牛肉', '黄牛肉']
- topic_keywords: ['湘菜', '小炒', '烹饪步骤', '腌制', '入味', '去腥']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3257

## Hybrid Branch Status / entity_level
- keywords: ['小炒黄牛肉', '黄牛肉']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 22

## Hybrid Branch Status / topic_level
- keywords: ['湘菜', '小炒', '烹饪步骤', '腌制', '入味', '去腥']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 95

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 345

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 10
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 17
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
- candidate_count: 17
- duration_ms: 22721
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '素菜': 2}
- deferred_count: 13
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26350
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:44:19.104
- end: 2026-08-11T16:44:56.312
- duration_ms: 37207
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2685
- retrieval_levels: ['', 'topic']
- search_types: ['topic_level', 'vector_enhanced']
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
- chunk_count: 60
- redacted_field: 2956
- total_duration_ms: 4461
- fallback_used: False

## Final Output
- answer_chars: 81
- answer_hash: 1682f4e343d27bbe
- success: True

## Request Complete
- request_end: 2026-08-11T16:45:00.798
- request_duration_ms: 41697
- success: True
- final_source: generation

