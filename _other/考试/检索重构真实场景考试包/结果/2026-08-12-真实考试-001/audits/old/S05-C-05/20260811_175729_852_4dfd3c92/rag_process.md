# RAG Process

audit_id: 20260811_175729_852_4dfd3c92
timestamp: 2026-08-11T17:57:29.854
## Request
- original_query: 只给出图中能验证的空心菜与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: a430a6fc25173f8e
- session_id: 2026-08-12-真实考试-001:old:S05-C-05
- request_mode: stream
- request_start: 2026-08-11T17:57:29.854
- evaluation_sample_id: 20260811_175729_852_4dfd3c92
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:57:29.855
- end: 2026-08-11T17:57:29.855
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:57:29.855
- end: 2026-08-11T17:57:29.855
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: a430a6fc25173f8e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:57:29.856
- end: 2026-08-11T17:57:29.856
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 31
- analysis_input_query_hash: a430a6fc25173f8e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:57:29.856
- end: 2026-08-11T17:57:38.466
- duration_ms: 8609
- analysis_mode: llm
- query_complexity: 0.86
- relationship_intensity: 0.9
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.93
- reasoning: 查询要求仅输出“图中能够验证”的空心菜与其他蔬菜之间的搭配关系，并在不存在关系路径时明确说明无法证明。这不仅需要识别实体“空心菜”和“蔬菜”，还需要在图结构中执行关系检索与路径验证，避免依据外部常识或未连接信息进行推断。需要多跳或至少显式路径推理；不需要因果分析和对比分析。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 25, 'total_queries': 144}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 26, 'total_queries': 145}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['空心菜']
- target_entities: ['可与空心菜共同出现在同一菜谱中的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 14887

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 14967
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:57:29.856
- end: 2026-08-11T17:57:53.434
- duration_ms: 23577
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 908
- retrieval_levels: ['']
- search_types: ['graph_path']
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
- chunk_count: 61
- redacted_field: 7245
- total_duration_ms: 8713
- fallback_used: False

## Final Output
- answer_chars: 82
- answer_hash: 85f6ad11eb8a639c
- success: True

## Request Complete
- request_end: 2026-08-11T17:58:02.190
- request_duration_ms: 32335
- success: True
- final_source: generation

