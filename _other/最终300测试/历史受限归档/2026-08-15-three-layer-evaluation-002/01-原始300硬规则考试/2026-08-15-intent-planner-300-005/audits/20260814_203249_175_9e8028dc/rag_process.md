# RAG Process

audit_id: 20260814_203249_175_9e8028dc
timestamp: 2026-08-14T20:32:49.176
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:32:49.176
- end: 2026-08-14T20:32:49.176
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:32:53.437
- end: 2026-08-14T20:32:53.437
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4260
- attempt_count: 1
- response_hash: 5a31ad59a4935be09c32eb2a03bd34212d2f3aced318191814c1b87b14e0ecb5
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:32:53.440
- end: 2026-08-14T20:32:53.440
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 86b6f69ee220a8bff0366753292d3ae4a6c4168590176b5d173ee480f15f1def
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:32:53.440
- end: 2026-08-14T20:32:53.440
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:32:53.440+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:32:53.442
- end: 2026-08-14T20:32:53.442
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:32:53.440+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:32:53.443
- end: 2026-08-14T20:32:53.443
- duration_ms: 0
- entity_id: tipdoc_9e62e8f43239
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:32:53.454
- end: 2026-08-14T20:32:53.454
- duration_ms: 0
- parent_id: tipdoc_9e62e8f43239
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 9

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2936
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
- duration_ms: 11454
- response_chars: 388
- response_hash: 5b7269cc75433562

## Final Output
- answer_chars: 388
- answer_hash: 5b7269cc75433562
- success: True

## Request Complete
- request_end: 2026-08-14T20:33:04.911
- request_duration_ms: 15734
- success: True
- final_source: generation

