# RAG Process

audit_id: 20260814_204837_750_a0ec805d
timestamp: 2026-08-14T20:48:37.750
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:48:37.751
- end: 2026-08-14T20:48:37.751
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:48:43.350
- end: 2026-08-14T20:48:43.350
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5599
- attempt_count: 1
- response_hash: 700f428d962edf832c8b415e42479b637c44442555de536c6d2a12cef937dcef
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:48:43.368
- end: 2026-08-14T20:48:43.368
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 52ee11a4b913d18ffe23b44ce5ffe523b8bf6dc07283c73ce060aedcd71195a1
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:48:43.368
- end: 2026-08-14T20:48:43.368
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:48:43.368+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T20:48:43.371
- end: 2026-08-14T20:48:43.371
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:48:43.368+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T20:48:43.371
- request_duration_ms: 5620
- success: True
- final_source: compile_terminal

