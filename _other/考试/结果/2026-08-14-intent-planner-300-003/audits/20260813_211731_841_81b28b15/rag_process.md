# RAG Process

audit_id: 20260813_211731_841_81b28b15
timestamp: 2026-08-13T21:17:31.841
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:17:31.842
- end: 2026-08-13T21:17:31.842
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:17:35.420
- end: 2026-08-13T21:17:35.420
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3579
- attempt_count: 1
- response_hash: 16d61fa8c2798ca43762cad8ac3232f66dcada212d485300358dd2d263f161f3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:17:35.425
- end: 2026-08-13T21:17:35.425
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: e71a3c5f96904496a022cbe7edbe063a605d5ae4d4fb43f5c87aad3d053b53ee
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:17:35.425
- end: 2026-08-13T21:17:35.425
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:35.425+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:17:35.425
- end: 2026-08-13T21:17:35.425
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:17:35.425+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:17:35.426
- request_duration_ms: 3584
- success: True
- final_source: compile_terminal

