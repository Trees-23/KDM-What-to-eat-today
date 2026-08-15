# RAG Process

audit_id: 20260813_200647_732_954419c6
timestamp: 2026-08-13T20:06:47.741
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:06:47.743
- end: 2026-08-13T20:06:47.743
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:06:51.833
- end: 2026-08-13T20:06:51.833
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4089
- attempt_count: 1
- response_hash: 269389b2d116d1915d3be5f32bec28262e860b158d0d07ff0f80e1a22fc4b759
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:06:51.836
- end: 2026-08-13T20:06:51.836
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: beeec1f7389a977fb34f293f824f0b9c7da26f25a8e09dcbd0de14472c4fee0c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:06:51.836
- end: 2026-08-13T20:06:51.836
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:51.836+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T20:06:51.836
- end: 2026-08-13T20:06:51.836
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:51.836+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T20:06:51.836
- request_duration_ms: 4092
- success: True
- final_source: compile_terminal

