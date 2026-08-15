# RAG Process

audit_id: 20260814_202505_696_b87b8d5e
timestamp: 2026-08-14T20:25:05.697
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:25:05.697
- end: 2026-08-14T20:25:05.697
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 42

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:25:10.419
- end: 2026-08-14T20:25:10.419
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': ['RICE_COOKER'], 'methods': ['STEAM', 'STEW'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4721
- attempt_count: 1
- response_hash: 117e1a9813f3e6029f04c93ccff4a1acf4bf030087f7a4ab3974f03ae2bca96a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:25:10.423
- end: 2026-08-14T20:25:10.423
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: ecbd4ae16cfdeb2d53700df1e052aa7ef844fe68ef05da1243df6e01a43bb776
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': ['RICE_COOKER', 'STEAM', 'STEW'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:25:10.423
- end: 2026-08-14T20:25:10.423
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:25:10.423+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:25:10.426
- end: 2026-08-14T20:25:10.426
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:25:10.423+00:00
- result_count: 6

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:25:10.426
- end: 2026-08-14T20:25:10.426
- duration_ms: 0
- entity_id: tipdoc_4ba80da791e4
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:25:10.436
- end: 2026-08-14T20:25:10.436
- duration_ms: 0
- parent_id: tipdoc_4ba80da791e4
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 10

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4290
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
- duration_ms: 23912
- response_chars: 1136
- response_hash: 8c8f1dc0c9ff7847

## Final Output
- answer_chars: 1136
- answer_hash: 8c8f1dc0c9ff7847
- success: True

## Request Complete
- request_end: 2026-08-14T20:25:34.350
- request_duration_ms: 28652
- success: True
- final_source: generation

