# RAG Process

audit_id: 20260811_174457_660_eba48f9a
timestamp: 2026-08-11T17:44:57.661
## Request
- original_query: 干豆腐能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: 3184b3fb222dadf9
- session_id: 2026-08-12-真实考试-001:old:S04-C-10
- request_mode: stream
- request_start: 2026-08-11T17:44:57.662
- evaluation_sample_id: 20260811_174457_660_eba48f9a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:44:57.663
- end: 2026-08-11T17:44:57.663
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:44:57.664
- end: 2026-08-11T17:44:57.664
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: 3184b3fb222dadf9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:44:57.665
- end: 2026-08-11T17:44:57.665
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: 3184b3fb222dadf9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:44:57.665
- end: 2026-08-11T17:45:12.208
- duration_ms: 14542
- analysis_mode: llm
- query_complexity: 0.68
- relationship_intensity: 0.82
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.93
- reasoning: 查询的核心不是按常识生成菜名，而是要求仅返回能够由图谱关系证明“使用了干豆腐”的菜谱。这需要以“干豆腐—作为食材/使用于—菜谱”的显式关系边为依据进行实体链接、关系过滤和证据校验。主要需要直接关系查询与约束过滤，通常不需要多跳推理，不需要因果分析或对比分析；但由于结果必须受图关系证据约束，graph_rag 比 hybrid_traditional 更适合。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 10, 'total_queries': 119}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 11, 'total_queries': 120}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['干豆腐']
- target_entities: ['使用干豆腐的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5104

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5122
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:44:57.665
- end: 2026-08-11T17:45:17.331
- duration_ms: 19666
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
- redacted_field: 2938
- total_duration_ms: 3736
- fallback_used: False

## Final Output
- answer_chars: 35
- answer_hash: f6c14875c54f7ec7
- success: True

## Request Complete
- request_end: 2026-08-11T17:45:21.108
- request_duration_ms: 23446
- success: True
- final_source: generation

