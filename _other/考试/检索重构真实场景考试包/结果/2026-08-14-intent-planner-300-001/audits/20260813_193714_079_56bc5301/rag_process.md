# RAG Process

audit_id: 20260813_193714_079_56bc5301
timestamp: 2026-08-13T19:37:14.080
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:37:14.081
- end: 2026-08-13T19:37:14.081
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:37:17.693
- end: 2026-08-13T19:37:17.693
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3612
- attempt_count: 1
- response_hash: 7ae5e31a9cc31510efc6afaa5dbbf3d2faed16249f73b72a7eff5d2043d29649
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:37:17.699
- end: 2026-08-13T19:37:17.699
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 23516cefb39f2a9690240a519ee42a616ddc40c560bdac953c4156c168563874
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:37:17.699
- end: 2026-08-13T19:37:17.699
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:37:17.699+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-13T19:37:17.702
- end: 2026-08-13T19:37:17.702
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:37:17.699+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-13T19:37:17.702
- request_duration_ms: 3621
- success: True
- final_source: compile_terminal

