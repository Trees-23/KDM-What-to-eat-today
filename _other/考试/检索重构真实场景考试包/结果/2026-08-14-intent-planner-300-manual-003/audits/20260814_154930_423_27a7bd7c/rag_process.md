# RAG Process

audit_id: 20260814_154930_423_27a7bd7c
timestamp: 2026-08-14T15:49:30.425
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:49:30.426
- end: 2026-08-14T15:49:30.426
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:49:34.816
- end: 2026-08-14T15:49:34.816
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4390
- attempt_count: 1
- response_hash: 388792d570b42cd3445ba4edbe2beed52877a5d86ecffe4883cefd779ff20004
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:49:34.847
- end: 2026-08-14T15:49:34.847
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 52ee11a4b913d18ffe23b44ce5ffe523b8bf6dc07283c73ce060aedcd71195a1
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:49:34.848
- end: 2026-08-14T15:49:34.848
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:49:34.848+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T15:49:34.853
- end: 2026-08-14T15:49:34.853
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:49:34.848+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T15:49:34.855
- request_duration_ms: 4429
- success: True
- final_source: compile_terminal

