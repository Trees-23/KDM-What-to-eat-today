# RAG Process

audit_id: 20260811_194656_872_9d9cdeca
timestamp: 2026-08-11T19:46:56.873
## Request
- original_query: 羊排焖面的第 1 步应该怎么做？
- original_query_hash: 8bec15e0e20e5112
- session_id: 2026-08-12-真实考试-001:new:S02-A-07
- request_mode: stream
- request_start: 2026-08-11T19:46:56.874
- evaluation_sample_id: 20260811_194656_872_9d9cdeca
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:46:56.874
- end: 2026-08-11T19:46:56.874
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:46:56.875
- end: 2026-08-11T19:46:56.875
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 8bec15e0e20e5112

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:46:56.878
- end: 2026-08-11T19:46:56.878
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-11T19:46:56.878+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:46:56.880
- end: 2026-08-11T19:46:56.880
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-11T19:46:56.878+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:46:56.880
- end: 2026-08-11T19:46:56.880
- duration_ms: 0
- entity_id: 201003025
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-11T19:46:56.881
- end: 2026-08-11T19:46:56.881
- duration_ms: 0
- recipe_id: 201003025
- step_id: 201003039

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:46:56.881
- end: 2026-08-11T19:46:56.881
- duration_ms: 0
- error_type: ProgrammingError

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:46:56.882
- end: 2026-08-11T19:46:56.882
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: ['parent-store-unavailable']
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 530
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 0
- limitation_count: 1
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Request Complete
- request_end: 2026-08-11T19:46:56.893
- request_duration_ms: 19
- success: True
- final_source: generation

