# RAG Process

audit_id: 20260813_222111_717_2fc260c6
timestamp: 2026-08-13T22:21:11.718
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:21:11.718
- end: 2026-08-13T22:21:11.718
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:21:19.229
- end: 2026-08-13T22:21:19.229
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7511
- attempt_count: 1
- response_hash: 2e432649c44daf8ebb4372e7f2a7d168a1f3aa84c141b1e2d9c546c24b7c76f8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:21:19.237
- end: 2026-08-13T22:21:19.237
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: a84a6f1cba0aefb02b017f9fe349a84a11791dfb965cd3612bf5e752eb8f2235
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:21:19.237
- end: 2026-08-13T22:21:19.237
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:21:19.237+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-13T22:21:19.240
- end: 2026-08-13T22:21:19.240
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:21:19.237+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-13T22:21:19.241
- request_duration_ms: 7522
- success: True
- final_source: compile_terminal

