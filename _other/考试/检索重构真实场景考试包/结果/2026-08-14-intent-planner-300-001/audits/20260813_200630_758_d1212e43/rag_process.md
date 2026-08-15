# RAG Process

audit_id: 20260813_200630_758_d1212e43
timestamp: 2026-08-13T20:06:30.758
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:06:30.759
- end: 2026-08-13T20:06:30.759
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:06:33.570
- end: 2026-08-13T20:06:33.570
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3450
- attempt_count: 1
- response_hash: 17a1d3ef75abd541c6b84d08a2e9d988155d260a6586fa86c70ac32f83a4c0b4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:06:33.575
- end: 2026-08-13T20:06:33.575
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: c534066c8ceb460432a421bb0f6c15a03bf73b8ad71728b3da55d4207103b675
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:06:33.575
- end: 2026-08-13T20:06:33.575
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:33.575+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T20:06:33.575
- end: 2026-08-13T20:06:33.575
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:33.575+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T20:06:33.576
- request_duration_ms: 2816
- success: True
- final_source: compile_terminal

