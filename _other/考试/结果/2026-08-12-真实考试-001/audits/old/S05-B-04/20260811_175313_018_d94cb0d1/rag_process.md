# RAG Process

audit_id: 20260811_175313_018_d94cb0d1
timestamp: 2026-08-11T17:53:13.019
## Request
- original_query: 做青蟹相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: 9cbefc7eb1411484
- session_id: 2026-08-12-真实考试-001:old:S05-B-04
- request_mode: stream
- request_start: 2026-08-11T17:53:13.019
- evaluation_sample_id: 20260811_175313_018_d94cb0d1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:53:13.020
- end: 2026-08-11T17:53:13.020
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:53:13.020
- end: 2026-08-11T17:53:13.020
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 9cbefc7eb1411484

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:53:13.021
- end: 2026-08-11T17:53:13.021
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 9cbefc7eb1411484
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:53:13.021
- end: 2026-08-11T17:53:21.553
- duration_ms: 8531
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.72
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.88
- reasoning: 查询核心是识别“青蟹”与“蔬菜”之间的菜品搭配关系，而非查找单一实体属性。需要在知识图谱中沿“食材-搭配/适配菜品-蔬菜”关系检索，并可能聚合多个菜谱或菜品节点后筛选蔬菜实体，属于中等复杂度的关系型查询。通常不需要因果分析或多方案优劣对比，但需要至少一跳的图关系查询（青蟹→搭配蔬菜），若图谱以菜品为中间节点组织，则需要两跳推理（青蟹→相关菜品→蔬菜）。明确实体包括“青蟹”和“蔬菜”，其中青蟹为水产食材实体，蔬菜为食材类别实体。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 14, 'total_queries': 133}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 15, 'total_queries': 134}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['青蟹']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5410

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5446
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:53:13.021
- end: 2026-08-11T17:53:27.000
- duration_ms: 13978
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
- chunk_count: 103
- redacted_field: 3046
- total_duration_ms: 5232
- fallback_used: False

## Final Output
- answer_chars: 132
- answer_hash: 7627ff62ba9bfcb4
- success: True

## Request Complete
- request_end: 2026-08-11T17:53:32.251
- request_duration_ms: 19232
- success: True
- final_source: generation

