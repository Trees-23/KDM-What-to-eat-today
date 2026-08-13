# RAG Process

audit_id: 20260813_202416_802_30a0274a
timestamp: 2026-08-13T20:24:16.803
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:24:16.803
- end: 2026-08-13T20:24:16.803
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:24:20.206
- end: 2026-08-13T20:24:20.206
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3402
- attempt_count: 1
- response_hash: 2c784889def9193d70b84c04400b8859a8de16599591580bc4e3df60e3d29f67
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:24:20.212
- end: 2026-08-13T20:24:20.212
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 0aa933c6cc6a1e1e1b003be437a59b2a1d8deb1d51f7297615d03775ad24f557
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:24:20.212
- end: 2026-08-13T20:24:20.212
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:24:20.212+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:24:20.216
- end: 2026-08-13T20:24:20.216
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:24:20.212+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:24:20.216
- end: 2026-08-13T20:24:20.216
- duration_ms: 0
- entity_id: 201002511
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T20:24:20.219
- end: 2026-08-13T20:24:20.219
- duration_ms: 0
- recipe_id: 201002511
- step_id: 201002519

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:24:20.222
- end: 2026-08-13T20:24:20.222
- duration_ms: 0
- parent_id: 201002511
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201002519
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1601
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
- duration_ms: 3629
- response_chars: 105
- response_hash: 16a95ce98ce4310e

## Final Output
- answer_chars: 105
- answer_hash: 16a95ce98ce4310e
- success: True

## Request Complete
- request_end: 2026-08-13T20:24:23.853
- request_duration_ms: 7050
- success: True
- final_source: generation

