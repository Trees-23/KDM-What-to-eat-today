# RAG Process

audit_id: 20260814_201944_129_dccb866a
timestamp: 2026-08-14T20:19:44.129
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:19:44.130
- end: 2026-08-14T20:19:44.130
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:19:52.410
- end: 2026-08-14T20:19:52.410
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.9
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 8280
- attempt_count: 1
- response_hash: 26aa20a96c0f000cbb8c4686695310960b8e9b2de57014520cb7ace55cbf6cde
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:19:52.415
- end: 2026-08-14T20:19:52.415
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: b523a832887435f7352d45ba49b7e86ac4d87716e2e65563fc25833811eb99a3
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:19:52.415
- end: 2026-08-14T20:19:52.415
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:19:52.415+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:19:52.418
- end: 2026-08-14T20:19:52.418
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:19:52.415+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:19:52.419
- end: 2026-08-14T20:19:52.419
- duration_ms: 0
- entity_id: 201000160
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:19:52.421
- end: 2026-08-14T20:19:52.421
- duration_ms: 0
- recipe_id: 201000160
- step_id: 201000177

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:19:52.424
- end: 2026-08-14T20:19:52.424
- duration_ms: 0
- parent_id: 201000160
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201000177
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1578
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
- duration_ms: 7359
- response_chars: 154
- response_hash: 9cf4065c6fee4b3e

## Final Output
- answer_chars: 154
- answer_hash: 9cf4065c6fee4b3e
- success: True

## Request Complete
- request_end: 2026-08-14T20:19:59.785
- request_duration_ms: 15654
- success: True
- final_source: generation

