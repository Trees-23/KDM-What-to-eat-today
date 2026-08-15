# RAG Process

audit_id: 20260811_192702_153_773e85a9
timestamp: 2026-08-11T19:27:02.153
## Request
- original_query: 请给出清蒸鲈鱼的完整做法，包括主要食材和步骤。
- original_query_hash: a5dd296e5aae3d11
- session_id: 2026-08-12-真实考试-001:new:S01-A-01
- request_mode: stream
- request_start: 2026-08-11T19:27:02.153
- evaluation_sample_id: 20260811_192702_153_773e85a9
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:27:02.156
- end: 2026-08-11T19:27:02.156
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:27:02.156
- end: 2026-08-11T19:27:02.156
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: a5dd296e5aae3d11

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:27:02.173
- end: 2026-08-11T19:27:02.173
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:27:02.173
- end: 2026-08-11T19:27:02.173
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:27:02.174
- end: 2026-08-11T19:27:02.174
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: a5dd296e5aae3d11
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:27:02.174
- end: 2026-08-11T19:27:09.729
- duration_ms: 7554
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询是对单一道菜“清蒸鲈鱼”制作方法的直接信息查找，要求返回主要食材和线性烹饪步骤。虽包含鲈鱼、主要食材、步骤等实体或信息要素，但它们属于菜谱的固定属性与组成部分，不涉及跨实体的复杂关系网络、多跳推理、因果分析或方案对比。适合通过关键词、菜谱字段匹配和语义检索相结合的 hybrid_traditional 策略获取高相关结果。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 0, 'graph_rag_count': 0, 'total_queries': 0}
- route_stats_after: {'traditional_count': 1, 'graph_rag_count': 0, 'total_queries': 1}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['清蒸鲈鱼', '鲈鱼', '姜', '葱', '料酒', '蒸鱼豉油', '食用油', '蒸锅']
- topic_keywords: ['清蒸', '蒸鱼', '去腥', '火候', '烹饪步骤', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3497

## Hybrid Branch Status / topic_level
- keywords: ['清蒸', '蒸鱼', '去腥', '火候', '烹饪步骤', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 112

## Hybrid Branch Status / entity_level
- keywords: ['清蒸鲈鱼', '鲈鱼', '姜', '葱', '料酒', '蒸鱼豉油', '食用油', '蒸锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 133

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 858

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 26
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 5
- doc_names: ['蒸']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 27
- duration_ms: 44281
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 1, '早餐': 1, '汤类': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 昂刺鱼豆腐汤
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 48736
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:27:02.174
- end: 2026-08-11T19:27:58.467
- duration_ms: 56292
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2928
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 435
- redacted_field: 3149
- total_duration_ms: 14758
- fallback_used: False

## Final Output
- answer_chars: 581
- answer_hash: d3ea8bff7aa9a898
- success: True

## Request Complete
- request_end: 2026-08-11T19:28:13.244
- request_duration_ms: 71090
- success: True
- final_source: generation

