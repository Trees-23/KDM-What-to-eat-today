# RAG Process

audit_id: 20260811_175802_201_1e6ded0d
timestamp: 2026-08-11T17:58:02.204
## Request
- original_query: 只给出图中能验证的苦瓜与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: 03c7031428cd6cbb
- session_id: 2026-08-12-真实考试-001:old:S05-C-06
- request_mode: stream
- request_start: 2026-08-11T17:58:02.204
- evaluation_sample_id: 20260811_175802_201_1e6ded0d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:58:02.205
- end: 2026-08-11T17:58:02.205
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:58:02.205
- end: 2026-08-11T17:58:02.205
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 30
- enhanced_query_length: 30
- enhanced_query_hash: 03c7031428cd6cbb

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:58:02.207
- end: 2026-08-11T17:58:02.207
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 30
- analysis_input_query_hash: 03c7031428cd6cbb
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:58:02.207
- end: 2026-08-11T17:58:14.167
- duration_ms: 11959
- analysis_mode: llm
- query_complexity: 0.78
- relationship_intensity: 0.86
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.93
- reasoning: 查询的核心不是泛泛检索“苦瓜搭配什么蔬菜”，而是要求结果必须由图中的实体关系或可追溯路径验证，并在不存在有效路径时明确输出“无法证明”。这要求先识别“苦瓜”与“蔬菜”实体，再在图结构中检索其直接或多跳的“搭配”关系、验证关系路径及证据来源，并过滤无法被图谱支持的候选答案。因此具有较强的关系约束、路径验证和图谱可证性判断需求，适合采用 graph_rag。该查询不要求因果分析或多对象优劣对比，但可能需要有限的多跳推理来确认苦瓜与具体蔬菜之间是否存在可验证路径。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 26, 'total_queries': 145}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 27, 'total_queries': 146}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['苦瓜']
- target_entities: ['与苦瓜在同一菜谱中共现的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 7535

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 7611
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:58:02.207
- end: 2026-08-11T17:58:21.779
- duration_ms: 19571
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
- chunk_count: 62
- redacted_field: 1720
- total_duration_ms: 3046
- fallback_used: False

## Final Output
- answer_chars: 86
- answer_hash: f0de3c8b188266a4
- success: True

## Request Complete
- request_end: 2026-08-11T17:58:24.866
- request_duration_ms: 22661
- success: True
- final_source: generation

