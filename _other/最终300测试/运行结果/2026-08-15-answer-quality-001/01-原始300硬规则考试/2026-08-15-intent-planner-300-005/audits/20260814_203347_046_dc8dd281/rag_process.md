# RAG Process

audit_id: 20260814_203347_046_dc8dd281
timestamp: 2026-08-14T20:33:47.047
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:33:47.047
- end: 2026-08-14T20:33:47.047
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:33:51.211
- end: 2026-08-14T20:33:51.211
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4164
- attempt_count: 1
- response_hash: 2a096e086dbfec08f0355bb3648ab0e474cc3a7f16143994ea23cbc6a820c121
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:33:51.215
- end: 2026-08-14T20:33:51.215
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: ecbd4ae16cfdeb2d53700df1e052aa7ef844fe68ef05da1243df6e01a43bb776
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:33:51.215
- end: 2026-08-14T20:33:51.215
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:33:51.215+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:33:51.218
- end: 2026-08-14T20:33:51.218
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:33:51.215+00:00
- result_count: 6

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:33:51.218
- end: 2026-08-14T20:33:51.218
- duration_ms: 0
- entity_id: tipdoc_4ba80da791e4
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:33:51.231
- end: 2026-08-14T20:33:51.231
- duration_ms: 0
- parent_id: tipdoc_4ba80da791e4
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 10

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4260
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 15787
- response_chars: 820
- response_hash: ef1aa17f95d7c4e9

## Final Output
- answer_chars: 820
- answer_hash: ef1aa17f95d7c4e9
- success: True

## Request Complete
- request_end: 2026-08-14T20:34:07.020
- request_duration_ms: 19972
- success: True
- final_source: generation

