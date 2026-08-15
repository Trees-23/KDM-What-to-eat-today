# RAG Process

audit_id: 20260811_175638_778_4a2be3bc
timestamp: 2026-08-11T17:56:38.779
## Request
- original_query: 只给出图中能验证的新鲜玉米与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: f253a61e1feb471f
- session_id: 2026-08-12-真实考试-001:old:S05-C-03
- request_mode: stream
- request_start: 2026-08-11T17:56:38.779
- evaluation_sample_id: 20260811_175638_778_4a2be3bc
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:56:38.780
- end: 2026-08-11T17:56:38.780
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:56:38.780
- end: 2026-08-11T17:56:38.780
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 32
- enhanced_query_length: 32
- enhanced_query_hash: f253a61e1feb471f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:56:38.780
- end: 2026-08-11T17:56:38.780
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 32
- analysis_input_query_hash: f253a61e1feb471f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:56:38.781
- end: 2026-08-11T17:56:47.618
- duration_ms: 8837
- analysis_mode: llm
- query_complexity: 0.78
- relationship_intensity: 0.82
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.9
- reasoning: 查询的核心是识别“新鲜玉米”与“蔬菜”之间可由图像内容直接验证的搭配关系，并要求输出具备可追溯的证据路径；若图中不存在从玉米到具体蔬菜及其搭配关系的有效证据路径，则必须明确说明无法证明。该任务需要实体识别、图像证据绑定、关系验证与路径存在性判断，属于关系约束较强的图结构推理。需要多跳/路径推理以建立“图像证据→新鲜玉米→具体蔬菜→搭配关系”的可验证链路；不需要因果分析，也不以多对象优劣对比为核心。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 23, 'total_queries': 142}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 24, 'total_queries': 143}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['新鲜玉米']
- target_entities: ['与新鲜玉米共同用于同一菜谱的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 11519

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 11549
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:56:38.781
- end: 2026-08-11T17:56:59.168
- duration_ms: 20387
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
- chunk_count: 69
- redacted_field: 6043
- total_duration_ms: 7212
- fallback_used: False

## Final Output
- answer_chars: 91
- answer_hash: c9bd4a9eaf954f47
- success: True

## Request Complete
- request_end: 2026-08-11T17:57:06.426
- request_duration_ms: 27646
- success: True
- final_source: generation

