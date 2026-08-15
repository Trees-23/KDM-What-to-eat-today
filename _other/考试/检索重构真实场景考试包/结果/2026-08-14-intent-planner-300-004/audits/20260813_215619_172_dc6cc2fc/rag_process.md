# RAG Process

audit_id: 20260813_215619_172_dc6cc2fc
timestamp: 2026-08-13T21:56:19.173
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:56:19.173
- end: 2026-08-13T21:56:19.173
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:56:22.542
- end: 2026-08-13T21:56:22.542
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3370
- attempt_count: 1
- response_hash: c320bbd3b647767884b8c547b8de667c851ce727edbcc00f593d3cafa5d88ab9
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:56:22.545
- end: 2026-08-13T21:56:22.545
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 15f490cf8895dfd193851753d4c22590dffda1b4d4ffcd2ab44fc4ddea9e5dd0
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:56:22.546
- end: 2026-08-13T21:56:22.546
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:56:22.546+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:56:22.547
- end: 2026-08-13T21:56:22.547
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:56:22.546+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:56:22.547
- end: 2026-08-13T21:56:22.547
- duration_ms: 0
- entity_id: 201001746
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T21:56:22.549
- end: 2026-08-13T21:56:22.549
- duration_ms: 0
- recipe_id: 201001746
- step_id: 201001769

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:56:22.550
- end: 2026-08-13T21:56:22.550
- duration_ms: 0
- parent_id: 201001746
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- anchor_id: 201001769
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2316
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
- duration_ms: 4701
- response_chars: 127
- response_hash: 5f74e64a2e113785

## Final Output
- answer_chars: 127
- answer_hash: 5f74e64a2e113785
- success: True

## Request Complete
- request_end: 2026-08-13T21:56:27.253
- request_duration_ms: 8080
- success: True
- final_source: generation

