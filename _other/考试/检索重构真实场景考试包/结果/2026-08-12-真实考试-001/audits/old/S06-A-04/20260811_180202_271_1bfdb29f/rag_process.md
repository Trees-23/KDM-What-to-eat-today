# RAG Process

audit_id: 20260811_180202_271_1bfdb29f
timestamp: 2026-08-11T18:02:02.273
## Request
- original_query: 周末想做一道有仪式感的海鲜菜。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: ad61bda347f881e0
- session_id: 2026-08-12-真实考试-001:old:S06-A-04
- request_mode: stream
- request_start: 2026-08-11T18:02:02.273
- evaluation_sample_id: 20260811_180202_271_1bfdb29f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:02:02.274
- end: 2026-08-11T18:02:02.274
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:02:02.274
- end: 2026-08-11T18:02:02.274
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 34
- enhanced_query_length: 34
- enhanced_query_hash: ad61bda347f881e0

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:02:02.275
- end: 2026-08-11T18:02:02.275
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 34
- analysis_input_query_hash: ad61bda347f881e0
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:02:02.275
- end: 2026-08-11T18:02:13.970
- duration_ms: 11695
- analysis_mode: llm
- query_complexity: 0.68
- relationship_intensity: 0.62
- reasoning_required: True
- entity_count: 3
- strategy: graph_rag
- confidence: 0.82
- reasoning: 该查询不是对单一道菜做直接查找，而是要求从知识库中基于“海鲜菜”“周末场景”“仪式感”三个约束筛选并推荐最合适的菜品，同时说明推荐依据。系统需要关联菜品与食材类型、制作难度、摆盘效果、宴请/节日属性、烹饪时长等多个属性，并对候选菜进行适配度比较。虽然不涉及强因果链推理，但需要多属性关联、候选对比与推荐决策，因此更适合使用graph_rag进行关系检索和解释生成。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 122, 'graph_rag_count': 31, 'total_queries': 153}
- route_stats_after: {'traditional_count': 122, 'graph_rag_count': 32, 'total_queries': 154}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['海鲜', '周末', '仪式感']
- target_entities: ['适合周末制作且具有仪式感的海鲜菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES', 'CONTAINS_STEP', 'HAS_DIFFICULTY_LEVEL', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'CONTAINS_STEP', 'HAS_DIFFICULTY_LEVEL', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 9827

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Recipe']
- relation_types: ['REQUIRES', 'CONTAINS_STEP', 'HAS_DIFFICULTY_LEVEL', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 9948
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:02:02.275
- end: 2026-08-11T18:02:23.919
- duration_ms: 21644
- selected_strategy: graph_rag
- document_count: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 0
- context_chars: 0
- retrieval_levels: []
- search_types: []
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
- chunk_count: 227
- redacted_field: 3777
- total_duration_ms: 8352
- fallback_used: False

## Final Output
- answer_chars: 299
- answer_hash: e99797beb5428057
- success: True

## Request Complete
- request_end: 2026-08-11T18:02:32.317
- request_duration_ms: 30043
- success: True
- final_source: generation

