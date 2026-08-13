# RAG Process

audit_id: 20260813_205119_328_89b090c7
timestamp: 2026-08-13T20:51:19.328
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:51:19.329
- end: 2026-08-13T20:51:19.329
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 18

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:51:23.908
- end: 2026-08-13T20:51:23.908
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4578
- attempt_count: 1
- response_hash: ab1da188b39a984dc2c347ffe936fe64bc5367f01129e046225caa8b62a170ac
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:51:23.915
- end: 2026-08-13T20:51:23.915
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: c3f3c899b507fb8559b83c691438d6007cd5a40018b018b8b4bc01a0f2c26dac
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:51:23.915
- end: 2026-08-13T20:51:23.915
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:51:23.915+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-13T20:51:23.918
- end: 2026-08-13T20:51:23.918
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:51:23.915+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-13T20:51:23.919
- request_duration_ms: 4589
- success: True
- final_source: compile_terminal

