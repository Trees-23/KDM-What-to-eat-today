# RAG Process

audit_id: 20260811_174146_824_7a5dd735
timestamp: 2026-08-11T17:41:46.825
## Request
- original_query: 花菜能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: 9779d4c48c4a79b8
- session_id: 2026-08-12-真实考试-001:old:S04-C-01
- request_mode: stream
- request_start: 2026-08-11T17:41:46.825
- evaluation_sample_id: 20260811_174146_824_7a5dd735
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:41:46.825
- end: 2026-08-11T17:41:46.825
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:41:46.826
- end: 2026-08-11T17:41:46.826
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 9779d4c48c4a79b8

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:41:46.826
- end: 2026-08-11T17:41:46.826
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 9779d4c48c4a79b8
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:41:46.826
- end: 2026-08-11T17:41:56.232
- duration_ms: 9405
- analysis_mode: llm
- query_complexity: 0.68
- relationship_intensity: 0.82
- reasoning_required: True
- entity_count: 1
- strategy: graph_rag
- confidence: 0.93
- reasoning: 查询的核心明确实体为“花菜”（食材实体），目标是检索与其存在“使用/作为食材”明确图关系的菜谱实体。用户显式要求仅列出图关系可证明的菜谱，排除基于常识、语义相似或模型补全得到的菜名，因此需要在知识图谱中执行“花菜 -> 被用于/作为原料 -> 菜谱”的关系约束查询，并最好保留关系证据或来源。该任务通常不要求多跳推理，主要是带证据约束的一跳实体关系检索；不需要因果分析，也不需要对比分析。但其结果正确性高度依赖图谱关系的存在性、方向性和可验证性，故应选择 graph_rag 而非 hybrid_traditional。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 1, 'total_queries': 110}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 2, 'total_queries': 111}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['花菜']
- target_entities: ['使用花菜的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5617

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5983
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:41:46.826
- end: 2026-08-11T17:42:02.216
- duration_ms: 15389
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
- chunk_count: 22
- redacted_field: 9404
- total_duration_ms: 9896
- fallback_used: False

## Final Output
- answer_chars: 31
- answer_hash: a7b71cdbf3e94331
- success: True

## Request Complete
- request_end: 2026-08-11T17:42:12.134
- request_duration_ms: 25308
- success: True
- final_source: generation

