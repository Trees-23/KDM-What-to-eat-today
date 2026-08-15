# RAG Process

audit_id: 20260814_155025_344_1ee2f7a6
timestamp: 2026-08-14T15:50:25.345
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:50:25.346
- end: 2026-08-14T15:50:25.346
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:50:34.516
- end: 2026-08-14T15:50:34.516
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 10723
- attempt_count: 2
- response_hash: 593ba3b01c90e7740dc76d3577e08969888b7248db2afe36ac03657960b086d4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:50:34.540
- end: 2026-08-14T15:50:34.540
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: a84a6f1cba0aefb02b017f9fe349a84a11791dfb965cd3612bf5e752eb8f2235
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:50:34.540
- end: 2026-08-14T15:50:34.540
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:34.540+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T15:50:34.546
- end: 2026-08-14T15:50:34.546
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:34.540+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T15:50:34.546
- request_duration_ms: 9200
- success: True
- final_source: compile_terminal

