# RAG Process

audit_id: 20260811_175706_442_674c16c0
timestamp: 2026-08-11T17:57:06.442
## Request
- original_query: 只给出图中能验证的新鲜菜心与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: c7b5ddaa60fbd6e5
- session_id: 2026-08-12-真实考试-001:old:S05-C-04
- request_mode: stream
- request_start: 2026-08-11T17:57:06.442
- evaluation_sample_id: 20260811_175706_442_674c16c0
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:57:06.443
- end: 2026-08-11T17:57:06.443
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:57:06.443
- end: 2026-08-11T17:57:06.443
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 32
- enhanced_query_length: 32
- enhanced_query_hash: c7b5ddaa60fbd6e5

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:57:06.445
- end: 2026-08-11T17:57:06.445
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 32
- analysis_input_query_hash: c7b5ddaa60fbd6e5
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:57:06.445
- end: 2026-08-11T17:57:14.412
- duration_ms: 7966
- analysis_mode: llm
- query_complexity: 0.86
- relationship_intensity: 0.84
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.9
- reasoning: 查询要求仅输出“图中可验证”的新鲜菜心与其他蔬菜之间的搭配关系，并要求在不存在可追溯关系路径时明确说明无法证明。这不仅需要识别实体“新鲜菜心”和“蔬菜”，还需要基于图像证据或知识图谱中的实体—关系—证据路径进行约束性验证。需要多跳或路径推理来确认搭配关系是否成立，不需要因果分析，也不以比较优劣为目标。由于核心需求是关系路径可验证性与缺失路径判定，适合使用graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 24, 'total_queries': 143}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 25, 'total_queries': 144}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['新鲜菜心']
- target_entities: ['可与新鲜菜心搭配的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 8729

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 8751
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:57:06.445
- end: 2026-08-11T17:57:23.164
- duration_ms: 16719
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 923
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
- redacted_field: 5374
- total_duration_ms: 6639
- fallback_used: False

## Final Output
- answer_chars: 83
- answer_hash: 0bfb6ca0b65bf8ee
- success: True

## Request Complete
- request_end: 2026-08-11T17:57:29.839
- request_duration_ms: 23396
- success: True
- final_source: generation

