# RAG Process

audit_id: 20260811_174434_705_73cf3812
timestamp: 2026-08-11T17:44:34.705
## Request
- original_query: 菠菜能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: bca8defadcd60bbc
- session_id: 2026-08-12-真实考试-001:old:S04-C-09
- request_mode: stream
- request_start: 2026-08-11T17:44:34.705
- evaluation_sample_id: 20260811_174434_705_73cf3812
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:44:34.706
- end: 2026-08-11T17:44:34.706
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:44:34.706
- end: 2026-08-11T17:44:34.706
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: bca8defadcd60bbc

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:44:34.707
- end: 2026-08-11T17:44:34.707
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: bca8defadcd60bbc
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:44:34.708
- end: 2026-08-11T17:44:43.616
- duration_ms: 8907
- analysis_mode: llm
- query_complexity: 0.68
- relationship_intensity: 0.84
- reasoning_required: True
- entity_count: 1
- strategy: graph_rag
- confidence: 0.93
- reasoning: 查询的核心实体是“菠菜”（食材实体），目标是检索与其存在明确“用于/包含/原料为”等图关系连接的菜谱实体。用户明确要求“只列出图关系能够证明使用了它的菜谱”，这排除了基于常识、语义相似度或模型补全的结果，必须沿知识图谱中“菠菜→菜谱”的可验证边进行约束检索与证据过滤。该任务通常不需要因果分析或菜谱间对比，但需要至少一次受关系类型和证据约束的图遍历，因此推荐 graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 9, 'total_queries': 118}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 10, 'total_queries': 119}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['菠菜']
- target_entities: ['使用菠菜的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 10785

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 10832
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:44:34.708
- end: 2026-08-11T17:44:54.448
- duration_ms: 19740
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
- chunk_count: 23
- redacted_field: 2652
- total_duration_ms: 3171
- fallback_used: False

## Final Output
- answer_chars: 34
- answer_hash: 1e37387c457c2f32
- success: True

## Request Complete
- request_end: 2026-08-11T17:44:57.648
- request_duration_ms: 22942
- success: True
- final_source: generation

