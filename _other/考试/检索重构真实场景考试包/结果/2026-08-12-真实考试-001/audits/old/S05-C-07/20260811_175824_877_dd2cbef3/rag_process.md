# RAG Process

audit_id: 20260811_175824_877_dd2cbef3
timestamp: 2026-08-11T17:58:24.878
## Request
- original_query: 只给出图中能验证的菠菜与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: 227a3f3f37cf8322
- session_id: 2026-08-12-真实考试-001:old:S05-C-07
- request_mode: stream
- request_start: 2026-08-11T17:58:24.878
- evaluation_sample_id: 20260811_175824_877_dd2cbef3
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:58:24.879
- end: 2026-08-11T17:58:24.879
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:58:24.879
- end: 2026-08-11T17:58:24.879
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 30
- enhanced_query_length: 30
- enhanced_query_hash: 227a3f3f37cf8322

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:58:24.880
- end: 2026-08-11T17:58:24.880
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 30
- analysis_input_query_hash: 227a3f3f37cf8322
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:58:24.880
- end: 2026-08-11T17:58:36.337
- duration_ms: 11457
- analysis_mode: llm
- query_complexity: 0.86
- relationship_intensity: 0.82
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.94
- reasoning: 查询的核心不是泛化地寻找菠菜搭配建议，而是要求仅输出“图中可验证”的菠菜与蔬菜搭配，并在菠菜与候选蔬菜之间不存在可证明关系路径时明确说明无法证明。这要求在知识图谱中定位“菠菜”和“蔬菜”实体，识别搭配/适配等关系边，并执行路径存在性验证，可能涉及从菠菜经由菜品、食材类别、搭配规则等中间节点到具体蔬菜的多跳推理。无需因果分析，也不以多方案优劣对比为主，但存在严格的证据约束和图路径验证需求，因此推荐graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 27, 'total_queries': 146}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 28, 'total_queries': 147}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['菠菜']
- target_entities: ['与菠菜共同用于同一菜谱的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 12574

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 12720
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:58:24.880
- end: 2026-08-11T17:58:49.059
- duration_ms: 24178
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 950
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
- redacted_field: 2259
- total_duration_ms: 3681
- fallback_used: False

## Final Output
- answer_chars: 96
- answer_hash: 7b545b9d01bb93bd
- success: True

## Request Complete
- request_end: 2026-08-11T17:58:52.768
- request_duration_ms: 27890
- success: True
- final_source: generation

