# RAG Process

audit_id: 20260811_180517_849_acac4c7c
timestamp: 2026-08-11T18:05:17.851
## Request
- original_query: 招待两个人，想做一道看起来体面的鱼。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: d416f1464105d000
- session_id: 2026-08-12-真实考试-001:old:S06-A-09
- request_mode: stream
- request_start: 2026-08-11T18:05:17.851
- evaluation_sample_id: 20260811_180517_849_acac4c7c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:05:17.851
- end: 2026-08-11T18:05:17.851
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:05:17.851
- end: 2026-08-11T18:05:17.851
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: d416f1464105d000

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:05:17.852
- end: 2026-08-11T18:05:17.852
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: d416f1464105d000
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:05:17.852
- end: 2026-08-11T18:05:29.918
- duration_ms: 12065
- analysis_mode: llm
- query_complexity: 0.68
- relationship_intensity: 0.64
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.84
- reasoning: 该查询不是单纯查找某道鱼的做法，而是基于“招待两个人”和“菜品看起来体面”两个约束，从知识库中的多道鱼类菜品中进行筛选与排序。需要关联菜品、适用人数、摆盘观感、食材规格、制作难度、待客场景等属性，并对候选菜品进行对比后给出最优推荐。查询包含“鱼”和“两个人”两个明确实体/约束，其中“体面”属于主观菜品属性与场景偏好。需要多跳检索与对比推理，但不以因果分析为主，因此选择更适合关联菜品属性和场景关系的 graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 126, 'graph_rag_count': 32, 'total_queries': 158}
- route_stats_after: {'traditional_count': 126, 'graph_rag_count': 33, 'total_queries': 159}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['鱼', '两人招待', '体面']
- target_entities: ['适合两人招待且外观体面的鱼类菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES', 'HAS_DIFFICULTY_LEVEL', 'BELONGS_TO_CATEGORY', 'CONTAINS_STEP']
- normalized_relation_types: ['REQUIRES', 'HAS_DIFFICULTY_LEVEL', 'BELONGS_TO_CATEGORY', 'CONTAINS_STEP']
- max_depth: 2
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 9344

## Graph Path Retrieval Config
- max_depth: 2
- target_labels: ['Recipe']
- relation_types: ['REQUIRES', 'HAS_DIFFICULTY_LEVEL', 'BELONGS_TO_CATEGORY', 'CONTAINS_STEP']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 9900
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:05:17.852
- end: 2026-08-11T18:05:39.819
- duration_ms: 21966
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 826
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
- chunk_count: 200
- redacted_field: 1823
- total_duration_ms: 7507
- fallback_used: False

## Final Output
- answer_chars: 258
- answer_hash: b0558bac739f7667
- success: True

## Request Complete
- request_end: 2026-08-11T18:05:47.371
- request_duration_ms: 29520
- success: True
- final_source: generation

