# RAG Process

audit_id: 20260813_222031_373_7c9c01ae
timestamp: 2026-08-13T22:20:31.374
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:20:31.374
- end: 2026-08-13T22:20:31.374
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:20:35.491
- end: 2026-08-13T22:20:35.491
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4117
- attempt_count: 1
- response_hash: 6322218517e1cdfd753d2cb9e6f77d5065646850f8d5e4c2768495df19c1901f
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:20:35.495
- end: 2026-08-13T22:20:35.495
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 39a211e9afaedaa3ae3f33bdc053aec5a64ae5517c61afce102f4faa2ec60e6f
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:20:35.496
- end: 2026-08-13T22:20:35.496
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:20:35.496+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-13T22:20:35.498
- end: 2026-08-13T22:20:35.498
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:20:35.496+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-13T22:20:35.499
- request_duration_ms: 4124
- success: True
- final_source: compile_terminal

