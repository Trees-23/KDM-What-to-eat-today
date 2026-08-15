# RAG Process

audit_id: 20260814_155005_519_deb9eb5b
timestamp: 2026-08-14T15:50:05.519
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:50:05.520
- end: 2026-08-14T15:50:05.520
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:50:11.641
- end: 2026-08-14T15:50:11.641
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6121
- attempt_count: 1
- response_hash: 42455bd888e0fa70fead925a8bb071d148b5ca774baee641352db6a0a61af33b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:50:11.651
- end: 2026-08-14T15:50:11.651
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 42ad5eeeae9b6055b05113016dca0781bb1fa59e6a03efab753ee004bb960190
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:50:11.652
- end: 2026-08-14T15:50:11.652
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:11.652+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T15:50:11.653
- end: 2026-08-14T15:50:11.653
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:11.652+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T15:50:11.654
- request_duration_ms: 6134
- success: True
- final_source: compile_terminal

