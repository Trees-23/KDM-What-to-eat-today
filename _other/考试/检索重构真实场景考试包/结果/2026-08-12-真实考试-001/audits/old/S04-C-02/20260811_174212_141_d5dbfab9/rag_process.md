# RAG Process

audit_id: 20260811_174212_141_d5dbfab9
timestamp: 2026-08-11T17:42:12.142
## Request
- original_query: 西兰花能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: ee54715779723749
- session_id: 2026-08-12-真实考试-001:old:S04-C-02
- request_mode: stream
- request_start: 2026-08-11T17:42:12.142
- evaluation_sample_id: 20260811_174212_141_d5dbfab9
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:42:12.142
- end: 2026-08-11T17:42:12.142
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:42:12.143
- end: 2026-08-11T17:42:12.143
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: ee54715779723749

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:42:12.143
- end: 2026-08-11T17:42:12.143
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: ee54715779723749
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:42:12.143
- end: 2026-08-11T17:42:21.897
- duration_ms: 9754
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.78
- reasoning_required: True
- entity_count: 1
- strategy: graph_rag
- confidence: 0.93
- reasoning: 查询的核心实体是“西兰花”（食材实体），目标是找出与其存在“作为食材/被菜谱使用”关系的菜谱实体。用户明确要求仅列出能够由图关系证明的菜谱，不能基于常识、语义相似度或模型先验补全，因此需要在知识图谱中执行“西兰花 → 食材关系 → 菜谱”的关系遍历和证据校验。通常不需要多跳推理，直接的一跳食材—菜谱关系即可；不需要因果分析或对比分析。但由于结果必须受图谱关系约束并可验证，graph_rag 比 hybrid_traditional 更适合。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 2, 'total_queries': 111}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 3, 'total_queries': 112}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['西兰花']
- target_entities: ['使用西兰花的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 7490

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 7517
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:42:12.143
- end: 2026-08-11T17:42:29.416
- duration_ms: 17272
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
- redacted_field: 5536
- total_duration_ms: 7277
- fallback_used: False

## Final Output
- answer_chars: 33
- answer_hash: 450a35583b2ac284
- success: True

## Request Complete
- request_end: 2026-08-11T17:42:36.711
- request_duration_ms: 24569
- success: True
- final_source: generation

