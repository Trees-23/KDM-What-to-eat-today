# RAG Process

audit_id: 20260813_211652_766_f37fe593
timestamp: 2026-08-13T21:16:52.776
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:16:52.776
- end: 2026-08-13T21:16:52.776
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:16:57.093
- end: 2026-08-13T21:16:57.093
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4317
- attempt_count: 1
- response_hash: 463b5b8881a781a440ce776aec1e9a5aa9c17e0a412ff5689223dbd364dc704a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:16:57.097
- end: 2026-08-13T21:16:57.097
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: a46c56a1e4e8c53aaa3109e7b1f39ce80094a841031c3d71b1589c8356e86876
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:16:57.097
- end: 2026-08-13T21:16:57.097
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:57.097+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:16:57.097
- end: 2026-08-13T21:16:57.097
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:57.097+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:16:57.098
- request_duration_ms: 4321
- success: True
- final_source: compile_terminal

