# RAG Process

audit_id: 20260811_175332_260_c81e8069
timestamp: 2026-08-11T17:53:32.260
## Request
- original_query: 做鲤鱼相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: fa984c7281ce6c1f
- session_id: 2026-08-12-真实考试-001:old:S05-B-05
- request_mode: stream
- request_start: 2026-08-11T17:53:32.261
- evaluation_sample_id: 20260811_175332_260_c81e8069
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:53:32.261
- end: 2026-08-11T17:53:32.261
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:53:32.261
- end: 2026-08-11T17:53:32.261
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: fa984c7281ce6c1f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:53:32.262
- end: 2026-08-11T17:53:32.262
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: fa984c7281ce6c1f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:53:32.262
- end: 2026-08-11T17:53:39.499
- duration_ms: 7236
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.68
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.88
- reasoning: 查询的核心目标是从知识图谱中查找“鲤鱼”与“蔬菜”之间的菜品搭配关系，而非获取单一实体属性。明确实体包括“鲤鱼”（食材/水产类）和“蔬菜”（食材类别）；“相关菜”可视为菜品场景或关系约束。该任务通常需要沿知识图谱执行至少一跳关系查询，例如“鲤鱼—适合搭配—蔬菜”，并可能经过“鲤鱼—相关菜品—配菜/食材—蔬菜”的两跳路径来获得结果。不需要因果分析，也不需要对比分析，但关系筛选与类别归属判断使其更适合采用 graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 15, 'total_queries': 134}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 16, 'total_queries': 135}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['鲤鱼']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 7554

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 8829
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:53:32.262
- end: 2026-08-11T17:53:48.329
- duration_ms: 16066
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
- chunk_count: 108
- redacted_field: 5362
- total_duration_ms: 9268
- fallback_used: False

## Final Output
- answer_chars: 138
- answer_hash: 8b07689e3a897861
- success: True

## Request Complete
- request_end: 2026-08-11T17:53:57.620
- request_duration_ms: 25359
- success: True
- final_source: generation

