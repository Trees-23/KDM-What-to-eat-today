# RAG Process

audit_id: 20260814_151502_719_c9b4d3d4
timestamp: 2026-08-14T15:15:02.719
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:15:02.720
- end: 2026-08-14T15:15:02.720
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:15:07.453
- end: 2026-08-14T15:15:07.453
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4733
- attempt_count: 1
- response_hash: fd22cb004e2ce41d55c78306e80017dba2b1af8c86506b6ad34cb81fdc634295
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:15:07.459
- end: 2026-08-14T15:15:07.459
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: fa37a6241972f3004bd7467ecb507a045199b0e46b032dbcce97efdd1a3c77f0
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:15:07.459
- end: 2026-08-14T15:15:07.459
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:15:07.459+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:15:07.462
- end: 2026-08-14T15:15:07.462
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:15:07.459+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:15:07.462
- end: 2026-08-14T15:15:07.462
- duration_ms: 0
- entity_id: 201003025
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:15:07.466
- end: 2026-08-14T15:15:07.466
- duration_ms: 0
- recipe_id: 201003025
- step_id: 201003039

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:15:07.469
- end: 2026-08-14T15:15:07.469
- duration_ms: 0
- parent_id: 201003025
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201003039
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1758
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 6633
- response_chars: 160
- response_hash: 815097bce1a85cd7

## Final Output
- answer_chars: 160
- answer_hash: 815097bce1a85cd7
- success: True

## Request Complete
- request_end: 2026-08-14T15:15:14.105
- request_duration_ms: 11384
- success: True
- final_source: generation

