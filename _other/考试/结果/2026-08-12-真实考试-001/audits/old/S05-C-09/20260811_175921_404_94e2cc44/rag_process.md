# RAG Process

audit_id: 20260811_175921_404_94e2cc44
timestamp: 2026-08-11T17:59:21.405
## Request
- original_query: 只给出图中能验证的酸菜与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: b88739b2ff7e3cdf
- session_id: 2026-08-12-真实考试-001:old:S05-C-09
- request_mode: stream
- request_start: 2026-08-11T17:59:21.406
- evaluation_sample_id: 20260811_175921_404_94e2cc44
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:59:21.407
- end: 2026-08-11T17:59:21.407
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:59:21.407
- end: 2026-08-11T17:59:21.407
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 30
- enhanced_query_length: 30
- enhanced_query_hash: b88739b2ff7e3cdf

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:59:21.407
- end: 2026-08-11T17:59:21.407
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 30
- analysis_input_query_hash: b88739b2ff7e3cdf
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:59:21.407
- end: 2026-08-11T17:59:30.095
- duration_ms: 8687
- analysis_mode: llm
- query_complexity: 0.78
- relationship_intensity: 0.82
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.94
- reasoning: 查询的核心不是泛化地查找酸菜可搭配哪些蔬菜，而是要求仅输出“图中存在可验证路径”的酸菜—蔬菜搭配关系，并在缺少路径证据时明确说明无法证明。这需要在图谱中识别“酸菜”和“蔬菜”实体，遍历或检索两者之间的直接或间接关系路径，并基于路径存在性进行证据约束输出。需要多跳推理或路径验证，但不需要因果分析和对比分析。由于查询显式依赖图结构、关系路径和可验证性，推荐使用graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 29, 'total_queries': 148}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 30, 'total_queries': 149}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['酸菜']
- target_entities: ['与酸菜共同被菜谱使用的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 8345

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 8449
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:59:21.407
- end: 2026-08-11T17:59:38.546
- duration_ms: 17138
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 905
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
- chunk_count: 62
- redacted_field: 2381
- total_duration_ms: 3646
- fallback_used: False

## Final Output
- answer_chars: 89
- answer_hash: 7cee4763e30588af
- success: True

## Request Complete
- request_end: 2026-08-11T17:59:42.205
- request_duration_ms: 20798
- success: True
- final_source: generation

