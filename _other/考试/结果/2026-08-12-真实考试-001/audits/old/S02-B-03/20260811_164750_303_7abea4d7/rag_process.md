# RAG Process

audit_id: 20260811_164750_303_7abea4d7
timestamp: 2026-08-11T16:47:50.305
## Request
- original_query: 刚开始做粉蒸肉时，第一步具体要处理什么？
- original_query_hash: 4cae596491bcfc3e
- session_id: 2026-08-12-真实考试-001:old:S02-B-03
- request_mode: stream
- request_start: 2026-08-11T16:47:50.305
- evaluation_sample_id: 20260811_164750_303_7abea4d7
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:47:50.306
- end: 2026-08-11T16:47:50.306
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:47:50.306
- end: 2026-08-11T16:47:50.306
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 4cae596491bcfc3e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:47:50.306
- end: 2026-08-11T16:47:50.306
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: 4cae596491bcfc3e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:47:50.307
- end: 2026-08-11T16:48:00.646
- duration_ms: 10339
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.97
- reasoning: 该查询是对菜品“粉蒸肉”制作流程中首个操作步骤的直接事实查找，目标明确且答案通常位于食谱步骤开头。无需多跳推理、因果分析或方案对比；仅需通过关键词匹配与语义检索定位可靠食谱中的前置处理步骤。明确实体为“粉蒸肉”（菜品/烹饪对象），“第一步”属于流程位置约束而非独立实体。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 42, 'graph_rag_count': 0, 'total_queries': 42}
- route_stats_after: {'traditional_count': 43, 'graph_rag_count': 0, 'total_queries': 43}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['粉蒸肉', '五花肉', '蒸肉米粉']
- topic_keywords: ['烹饪步骤', '前期处理', '食材准备', '腌制', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4950

## Hybrid Branch Status / entity_level
- keywords: ['粉蒸肉', '五花肉', '蒸肉米粉']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 41

## Hybrid Branch Status / topic_level
- keywords: ['烹饪步骤', '前期处理', '食材准备', '腌制', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 73

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 450

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 19
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
- candidate_count: 19
- duration_ms: 17113
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 2, 'Ingredient': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22534
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:47:50.307
- end: 2026-08-11T16:48:23.182
- duration_ms: 32874
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3610
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
- chunk_count: 64
- redacted_field: 1956
- total_duration_ms: 3272
- fallback_used: False

## Final Output
- answer_chars: 92
- answer_hash: ca2a4433c91075db
- success: True

## Request Complete
- request_end: 2026-08-11T16:48:26.466
- request_duration_ms: 36161
- success: True
- final_source: generation

