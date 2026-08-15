# RAG Process

audit_id: 20260814_155017_371_14c39454
timestamp: 2026-08-14T15:50:17.371
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:50:17.372
- end: 2026-08-14T15:50:17.372
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:50:25.304
- end: 2026-08-14T15:50:25.304
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7931
- attempt_count: 1
- response_hash: a6a5dd4b8967658f250717d8a650d9c2dbe975785105649ce50c69f7cf4fcad7
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:50:25.337
- end: 2026-08-14T15:50:25.337
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: d30d5868c24d26d4864facfbd968da79551462f9514f79ab58362d3cf7494209
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:50:25.338
- end: 2026-08-14T15:50:25.338
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:25.337+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T15:50:25.343
- end: 2026-08-14T15:50:25.343
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:25.337+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T15:50:25.343
- request_duration_ms: 7971
- success: True
- final_source: compile_terminal

