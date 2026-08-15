# RAG Process

audit_id: 20260814_201806_247_5ae41242
timestamp: 2026-08-14T20:18:06.248
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:18:06.248
- end: 2026-08-14T20:18:06.248
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 19

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:18:10.033
- end: 2026-08-14T20:18:10.033
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.97
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3784
- attempt_count: 1
- response_hash: 90ae3175319a5072431703e011da06325db262f4dcdc11b7e29f500f5bdb3ddd
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:18:10.040
- end: 2026-08-14T20:18:10.040
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 77043a35d5978c43c70252e2beb4dd858c42dd4202083078fdc27c3c726407d8
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:18:10.041
- end: 2026-08-14T20:18:10.041
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:18:10.041+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:18:10.044
- end: 2026-08-14T20:18:10.044
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:18:10.041+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:18:10.045
- end: 2026-08-14T20:18:10.045
- duration_ms: 0
- entity_id: 201000319
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:18:10.048
- end: 2026-08-14T20:18:10.048
- duration_ms: 0
- recipe_id: 201000319
- step_id: 201000330

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:18:10.050
- end: 2026-08-14T20:18:10.050
- duration_ms: 0
- parent_id: 201000319
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201000330
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1621
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
- duration_ms: 7714
- response_chars: 203
- response_hash: ad3d23ce08f9ff75

## Final Output
- answer_chars: 203
- answer_hash: ad3d23ce08f9ff75
- success: True

## Request Complete
- request_end: 2026-08-14T20:18:17.766
- request_duration_ms: 11518
- success: True
- final_source: generation

