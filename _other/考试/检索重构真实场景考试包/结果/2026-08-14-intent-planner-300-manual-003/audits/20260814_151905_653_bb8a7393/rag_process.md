# RAG Process

audit_id: 20260814_151905_653_bb8a7393
timestamp: 2026-08-14T15:19:05.654
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:19:05.654
- end: 2026-08-14T15:19:05.654
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 39

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:19:11.244
- end: 2026-08-14T15:19:11.244
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5590
- attempt_count: 1
- response_hash: 7408ea03ff5741c2db7edac7b47db263bf336f3dbc683fa9a574977f841b033f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:19:11.247
- end: 2026-08-14T15:19:11.247
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 07380e993f672ad987a8b9c012a2cb42a8107b6790f2a4f10e751f768ef15ec9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:19:11.247
- end: 2026-08-14T15:19:11.247
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:19:11.247+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:19:11.248
- end: 2026-08-14T15:19:11.248
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:19:11.247+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:19:11.249
- end: 2026-08-14T15:19:11.249
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:19:11.250
- end: 2026-08-14T15:19:11.250
- duration_ms: 0
- recipe_id: 201005669
- step_id: 201005675

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:19:11.251
- end: 2026-08-14T15:19:11.251
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_51e5e228cb4a935de64e2b7a
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 5715
- response_chars: 148
- response_hash: 9789ae4971e321b8

## Final Output
- answer_chars: 148
- answer_hash: 9789ae4971e321b8
- success: True

## Request Complete
- request_end: 2026-08-14T15:19:16.967
- request_duration_ms: 11313
- success: True
- final_source: generation

