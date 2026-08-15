# RAG Process

audit_id: 20260814_204919_988_0b9c682b
timestamp: 2026-08-14T20:49:19.989
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:49:19.989
- end: 2026-08-14T20:49:19.989
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:49:23.498
- end: 2026-08-14T20:49:23.498
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3508
- attempt_count: 1
- response_hash: 8eb7968a83b475d0afffdea14fb2c2e0f069fa6d4f22e8a1c4e70cad57f1c1de
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:49:23.523
- end: 2026-08-14T20:49:23.523
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: d30d5868c24d26d4864facfbd968da79551462f9514f79ab58362d3cf7494209
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:49:23.523
- end: 2026-08-14T20:49:23.523
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:49:23.523+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T20:49:23.527
- end: 2026-08-14T20:49:23.527
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:49:23.523+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T20:49:23.528
- request_duration_ms: 3538
- success: True
- final_source: compile_terminal

