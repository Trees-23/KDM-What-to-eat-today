# RAG Process

audit_id: 20260811_174255_280_98848b37
timestamp: 2026-08-11T17:42:55.281
## Request
- original_query: 豆角能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: a14d4ea771945ff8
- session_id: 2026-08-12-真实考试-001:old:S04-C-04
- request_mode: stream
- request_start: 2026-08-11T17:42:55.282
- evaluation_sample_id: 20260811_174255_280_98848b37
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:42:55.283
- end: 2026-08-11T17:42:55.283
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:42:55.283
- end: 2026-08-11T17:42:55.283
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: a14d4ea771945ff8

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:42:55.284
- end: 2026-08-11T17:42:55.284
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: a14d4ea771945ff8
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:42:55.285
- end: 2026-08-11T17:43:08.349
- duration_ms: 13063
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.68
- reasoning_required: True
- entity_count: 1
- strategy: graph_rag
- confidence: 0.92
- reasoning: 查询的核心实体是“豆角”（食材实体），目标是找出与其存在“菜谱使用食材”关系的菜谱实体。用户明确要求仅列出能够由图关系证明使用了豆角的菜谱，排除基于常识、语义相似度或模型补全得到的菜名。因此需要在知识图谱中执行“豆角 → 被用于/作为食材 → 菜谱”的关系查询，并对每个结果保留可追溯的关系证据。该任务通常不需要多跳推理，主要是受关系证据约束的一跳检索；不需要因果分析或对比分析。但由于结果必须由图边事实验证，推荐使用graph_rag而非hybrid_traditional。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 4, 'total_queries': 113}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 5, 'total_queries': 114}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['豆角']
- target_entities: ['使用豆角的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5818

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5847
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:42:55.285
- end: 2026-08-11T17:43:14.198
- duration_ms: 18913
- selected_strategy: graph_rag
- document_count: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 0
- context_chars: 0
- retrieval_levels: []
- search_types: []
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
- chunk_count: 21
- redacted_field: 3396
- total_duration_ms: 3988
- fallback_used: False

## Final Output
- answer_chars: 29
- answer_hash: c7b3ce3917922a74
- success: True

## Request Complete
- request_end: 2026-08-11T17:43:18.209
- request_duration_ms: 22927
- success: True
- final_source: generation

