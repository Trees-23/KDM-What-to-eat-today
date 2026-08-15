# RAG Process

audit_id: 20260814_163035_778_54585e24
timestamp: 2026-08-14T16:30:35.788
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:30:35.788
- end: 2026-08-14T16:30:35.788
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:30:40.161
- end: 2026-08-14T16:30:40.161
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4373
- attempt_count: 1
- response_hash: 7094760bd71add1871f663fb6ea97084e526760608eb69069855e1598bcc3b1c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:30:40.171
- end: 2026-08-14T16:30:40.171
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 9aedaa8d2d7664e5c2bd13246518a7450b6d35d3b197ac0eb2e609255f2d5578
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:30:40.171
- end: 2026-08-14T16:30:40.171
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:40.171+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:30:40.171
- end: 2026-08-14T16:30:40.171
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:30:40.171+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:30:40.172
- request_duration_ms: 4383
- success: True
- final_source: compile_terminal

