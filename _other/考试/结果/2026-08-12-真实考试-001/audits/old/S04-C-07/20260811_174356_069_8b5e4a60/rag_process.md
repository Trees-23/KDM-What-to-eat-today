# RAG Process

audit_id: 20260811_174356_069_8b5e4a60
timestamp: 2026-08-11T17:43:56.070
## Request
- original_query: 莲藕能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: 4ac0bbb773f21b30
- session_id: 2026-08-12-真实考试-001:old:S04-C-07
- request_mode: stream
- request_start: 2026-08-11T17:43:56.070
- evaluation_sample_id: 20260811_174356_069_8b5e4a60
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:43:56.071
- end: 2026-08-11T17:43:56.071
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:43:56.071
- end: 2026-08-11T17:43:56.071
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 4ac0bbb773f21b30

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:43:56.072
- end: 2026-08-11T17:43:56.072
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 4ac0bbb773f21b30
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:43:56.072
- end: 2026-08-11T17:44:03.530
- duration_ms: 7458
- analysis_mode: llm
- query_complexity: 0.65
- relationship_intensity: 0.78
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.93
- reasoning: 查询核心实体为“莲藕”（食材）和“菜谱/菜品”（菜谱类实体）。用户要求仅返回能够被图谱中“菜谱—使用食材—莲藕”显式关系证明的结果，并明确禁止依据常识补全菜名，因此检索不仅要找到相关菜谱，还必须验证图关系证据。主要需要基于图谱执行一跳关系查询与关系存在性校验；不需要因果分析、对比分析或复杂多跳推理，但图关系约束是结果正确性的关键，适合采用 graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 7, 'total_queries': 116}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 8, 'total_queries': 117}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['莲藕']
- target_entities: ['使用莲藕的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5508

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5526
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:43:56.072
- end: 2026-08-11T17:44:09.058
- duration_ms: 12986
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
- redacted_field: 3057
- total_duration_ms: 3673
- fallback_used: False

## Final Output
- answer_chars: 33
- answer_hash: 852a5a96a27817a9
- success: True

## Request Complete
- request_end: 2026-08-11T17:44:12.765
- request_duration_ms: 16694
- success: True
- final_source: generation

