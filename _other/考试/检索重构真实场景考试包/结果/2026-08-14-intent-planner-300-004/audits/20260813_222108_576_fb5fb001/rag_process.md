# RAG Process

audit_id: 20260813_222108_576_fb5fb001
timestamp: 2026-08-13T22:21:08.576
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:21:08.577
- end: 2026-08-13T22:21:08.577
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:21:11.696
- end: 2026-08-13T22:21:11.696
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3875
- attempt_count: 1
- response_hash: 7347210d21333c1e4071a28fb84ab01cc87012c88b3bdb640a161f0eb9c8919c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:21:11.701
- end: 2026-08-13T22:21:11.701
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: d30d5868c24d26d4864facfbd968da79551462f9514f79ab58362d3cf7494209
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:21:11.702
- end: 2026-08-13T22:21:11.702
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:21:11.702+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-13T22:21:11.716
- end: 2026-08-13T22:21:11.716
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:21:11.702+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-13T22:21:11.716
- request_duration_ms: 3139
- success: True
- final_source: compile_terminal

