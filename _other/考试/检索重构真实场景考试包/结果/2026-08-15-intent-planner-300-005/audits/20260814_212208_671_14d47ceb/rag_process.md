# RAG Process

audit_id: 20260814_212208_671_14d47ceb
timestamp: 2026-08-14T21:22:08.672
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:22:08.672
- end: 2026-08-14T21:22:08.672
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:22:12.467
- end: 2026-08-14T21:22:12.467
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['蘑菇'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3794
- attempt_count: 1
- response_hash: 7ffa323499e8a0dfbd47296d2a79c51768cee6a262a11b7267da903b73fe05fc
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:22:12.487
- end: 2026-08-14T21:22:12.487
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 2a356182272177af57ee55f6f61040941cdc431cba8d5e0ebf827fe50e7aaa56
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:22:12.487
- end: 2026-08-14T21:22:12.487
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:22:12.487+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:22:12.488
- end: 2026-08-14T21:22:12.488
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:22:12.487+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:22:12.488
- request_duration_ms: 3815
- success: True
- final_source: compile_terminal

