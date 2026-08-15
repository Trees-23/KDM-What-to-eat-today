# RAG Process

audit_id: 20260811_194657_200_5892d3be
timestamp: 2026-08-11T19:46:57.200
## Request
- original_query: 刚开始做清蒸鲈鱼时，第一步具体要处理什么？
- original_query_hash: 7bb94fd7121d4a9a
- session_id: 2026-08-12-真实考试-001:new:S02-B-07
- request_mode: stream
- request_start: 2026-08-11T19:46:57.201
- evaluation_sample_id: 20260811_194657_200_5892d3be
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:46:57.201
- end: 2026-08-11T19:46:57.201
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:46:57.201
- end: 2026-08-11T19:46:57.201
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 7bb94fd7121d4a9a

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:46:57.204
- end: 2026-08-11T19:46:57.204
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-11T19:46:57.204+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:46:57.206
- end: 2026-08-11T19:46:57.206
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-11T19:46:57.204+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:46:57.206
- end: 2026-08-11T19:46:57.206
- duration_ms: 0
- entity_id: 201000257
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-11T19:46:57.208
- end: 2026-08-11T19:46:57.208
- duration_ms: 0
- recipe_id: 201000257
- step_id: 201000265

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:46:57.208
- end: 2026-08-11T19:46:57.208
- duration_ms: 0
- error_type: ProgrammingError

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:46:57.208
- end: 2026-08-11T19:46:57.208
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
- request_end: 2026-08-11T19:46:57.219
- request_duration_ms: 18
- success: True
- final_source: generation

