# RAG Process

audit_id: 20260811_175942_211_ea780063
timestamp: 2026-08-11T17:59:42.211
## Request
- original_query: 只给出图中能验证的韭菜与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: 01b94c5baa2d9bca
- session_id: 2026-08-12-真实考试-001:old:S05-C-10
- request_mode: stream
- request_start: 2026-08-11T17:59:42.212
- evaluation_sample_id: 20260811_175942_211_ea780063
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:59:42.212
- end: 2026-08-11T17:59:42.212
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:59:42.212
- end: 2026-08-11T17:59:42.212
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 30
- enhanced_query_length: 30
- enhanced_query_hash: 01b94c5baa2d9bca

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:59:42.213
- end: 2026-08-11T17:59:42.213
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 30
- analysis_input_query_hash: 01b94c5baa2d9bca
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:59:42.213
- end: 2026-08-11T17:59:49.910
- duration_ms: 7697
- analysis_mode: llm
- query_complexity: 0.86
- relationship_intensity: 0.9
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.95
- reasoning: 查询的核心实体为“韭菜”和“蔬菜”，目标不是泛泛检索搭配建议，而是限定只能输出“图中能验证”的搭配关系。该查询要求在图结构中定位韭菜节点、识别其与蔬菜类节点之间的直接或可接受的关系路径，并依据路径证据筛选结果；当不存在可验证路径时，还需输出“无法证明”。因此需要关系路径检索与证据约束推理，适合采用graph_rag。该查询不需要因果分析或多方案对比，但需要图路径验证，可视为有限多跳关系推理。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 30, 'total_queries': 149}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 31, 'total_queries': 150}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['韭菜']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 8722

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 8784
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:59:42.213
- end: 2026-08-11T17:59:58.695
- duration_ms: 16482
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 893
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
- chunk_count: 73
- redacted_field: 2044
- total_duration_ms: 3552
- fallback_used: False

## Final Output
- answer_chars: 100
- answer_hash: 524074b68eea5d74
- success: True

## Request Complete
- request_end: 2026-08-11T18:00:02.281
- request_duration_ms: 20069
- success: True
- final_source: generation

