# RAG Process

audit_id: 20260811_174337_220_3f574db3
timestamp: 2026-08-11T17:43:37.221
## Request
- original_query: 金针菇能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: 289a77d5979e1694
- session_id: 2026-08-12-真实考试-001:old:S04-C-06
- request_mode: stream
- request_start: 2026-08-11T17:43:37.221
- evaluation_sample_id: 20260811_174337_220_3f574db3
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:43:37.223
- end: 2026-08-11T17:43:37.223
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:43:37.223
- end: 2026-08-11T17:43:37.223
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: 289a77d5979e1694

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:43:37.224
- end: 2026-08-11T17:43:37.224
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: 289a77d5979e1694
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:43:37.224
- end: 2026-08-11T17:43:43.592
- duration_ms: 6368
- analysis_mode: llm
- query_complexity: 0.68
- relationship_intensity: 0.82
- reasoning_required: True
- entity_count: 1
- strategy: graph_rag
- confidence: 0.96
- reasoning: 查询的核心实体是“金针菇”（食材实体），目标是查找与其存在“作为食材/使用于”明确图关系的菜谱实体。用户明确要求仅输出可由图关系证明的菜谱，禁止基于常识、语义相似度或模型先验补全菜名。因此需执行从“金针菇”到“菜谱”的关系遍历，并对每个结果验证其图边类型及证据来源。该任务通常不需要多跳因果推理或对比分析，但高度依赖结构化实体关系与关系证据约束，适合graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 6, 'total_queries': 115}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 7, 'total_queries': 116}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['金针菇']
- target_entities: ['使用金针菇的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5801

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5838
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:43:37.224
- end: 2026-08-11T17:43:49.431
- duration_ms: 12207
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
- chunk_count: 25
- redacted_field: 6070
- total_duration_ms: 6602
- fallback_used: False

## Final Output
- answer_chars: 35
- answer_hash: 4647c4d53f601b93
- success: True

## Request Complete
- request_end: 2026-08-11T17:43:56.061
- request_duration_ms: 18839
- success: True
- final_source: generation

