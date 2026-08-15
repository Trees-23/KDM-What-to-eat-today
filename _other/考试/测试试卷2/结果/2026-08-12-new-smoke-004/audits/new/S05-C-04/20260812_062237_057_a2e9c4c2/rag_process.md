# RAG Process

audit_id: 20260812_062237_057_a2e9c4c2
timestamp: 2026-08-12T06:22:37.058
## Request
- original_query: 只给出图中能验证的新鲜菜心与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: c7b5ddaa60fbd6e5
- session_id: 2026-08-12-new-smoke-004:new:S05-C-04
- request_mode: stream
- request_start: 2026-08-12T06:22:37.058
- evaluation_sample_id: 20260812_062237_057_a2e9c4c2
- experiment_id: 2026-08-12-new-smoke-004
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-12T06:22:37.059
- end: 2026-08-12T06:22:37.059
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-12T06:22:37.059
- end: 2026-08-12T06:22:37.059
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 32
- enhanced_query_length: 32
- enhanced_query_hash: c7b5ddaa60fbd6e5

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-12T06:22:37.064
- end: 2026-08-12T06:22:37.064
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T06:22:37.064+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-12T06:22:37.066
- end: 2026-08-12T06:22:37.066
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-12T06:22:37.064+00:00
- result_count: 0

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: not_found
- start: 2026-08-12T06:22:37.067
- end: 2026-08-12T06:22:37.067
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- graph_fact_status: not_found
- graph_fact_count: 1
- limitations: ['GRAPH_RELATION_NOT_FOUND', '当前图谱未找到该关系；正文不能证明该关系。']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 131
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 0
- limitation_count: 2
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Request Complete
- request_end: 2026-08-12T06:22:37.087
- request_duration_ms: 29
- success: True
- final_source: generation

