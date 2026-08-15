# RAG Process

audit_id: 20260813_215729_015_65f33cec
timestamp: 2026-08-13T21:57:29.016
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:57:29.017
- end: 2026-08-13T21:57:29.017
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 39

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:57:35.310
- end: 2026-08-13T21:57:35.310
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6292
- attempt_count: 1
- response_hash: 7408ea03ff5741c2db7edac7b47db263bf336f3dbc683fa9a574977f841b033f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:57:35.315
- end: 2026-08-13T21:57:35.315
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 07380e993f672ad987a8b9c012a2cb42a8107b6790f2a4f10e751f768ef15ec9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:57:35.316
- end: 2026-08-13T21:57:35.316
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:57:35.316+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:57:35.319
- end: 2026-08-13T21:57:35.319
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:57:35.316+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:57:35.319
- end: 2026-08-13T21:57:35.319
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T21:57:35.322
- end: 2026-08-13T21:57:35.322
- duration_ms: 0
- recipe_id: 201005669
- step_id: 201005675

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:57:35.324
- end: 2026-08-13T21:57:35.324
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- anchor_id: 201005675
- chunk_count: 2

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1500
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 1
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 5551
- response_chars: 115
- response_hash: 9ac074e96d8bf721

## Final Output
- answer_chars: 115
- answer_hash: 9ac074e96d8bf721
- success: True

## Request Complete
- request_end: 2026-08-13T21:57:40.877
- request_duration_ms: 11860
- success: True
- final_source: generation

