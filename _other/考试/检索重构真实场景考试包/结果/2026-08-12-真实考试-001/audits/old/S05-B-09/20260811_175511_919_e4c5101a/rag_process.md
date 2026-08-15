# RAG Process

audit_id: 20260811_175511_919_e4c5101a
timestamp: 2026-08-11T17:55:11.920
## Request
- original_query: 做花菜相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: 28e4ddfdbee182d7
- session_id: 2026-08-12-真实考试-001:old:S05-B-09
- request_mode: stream
- request_start: 2026-08-11T17:55:11.920
- evaluation_sample_id: 20260811_175511_919_e4c5101a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:55:11.921
- end: 2026-08-11T17:55:11.921
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:55:11.921
- end: 2026-08-11T17:55:11.921
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 28e4ddfdbee182d7

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:55:11.921
- end: 2026-08-11T17:55:11.921
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 28e4ddfdbee182d7
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:55:11.922
- end: 2026-08-11T17:55:21.922
- duration_ms: 9999
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.72
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.9
- reasoning: 查询核心目标是从知识图谱中查找“花菜”与其他“蔬菜”之间的搭配关系，属于围绕单个核心食材进行关联实体扩展的任务。复杂度中等：不要求解释烹饪原理、营养因果或菜系历史，但需要在图谱中定位花菜实体，并遍历其“可搭配/适宜同烹/常见配菜”等关系边，返回多个关联蔬菜。关系密集度较高，因为结果不是单一属性，而是一个由花菜连接到多种蔬菜实体的关系集合。需要一跳关系查询或有限的关系类型归并，不需要多跳推理、因果分析或对比分析。明确实体包括“花菜”（食材/蔬菜实体）和“蔬菜”（食材类别实体）。推荐使用graph_rag，以便利用知识图谱中的搭配关系进行精确扩展、关系过滤与结果排序。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 19, 'total_queries': 138}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 20, 'total_queries': 139}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['花菜']
- target_entities: ['与花菜共同用于菜谱的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 6439

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 6585
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:55:11.922
- end: 2026-08-11T17:55:28.508
- duration_ms: 16586
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 983
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
- chunk_count: 90
- redacted_field: 5176
- total_duration_ms: 7206
- fallback_used: False

## Final Output
- answer_chars: 120
- answer_hash: c05b0055841e5e88
- success: True

## Request Complete
- request_end: 2026-08-11T17:55:35.762
- request_duration_ms: 23842
- success: True
- final_source: generation

