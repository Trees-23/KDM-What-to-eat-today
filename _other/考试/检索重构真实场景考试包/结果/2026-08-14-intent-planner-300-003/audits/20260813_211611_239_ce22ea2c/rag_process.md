# RAG Process

audit_id: 20260813_211611_239_ce22ea2c
timestamp: 2026-08-13T21:16:11.239
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:16:11.240
- end: 2026-08-13T21:16:11.240
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:16:14.541
- end: 2026-08-13T21:16:14.541
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3301
- attempt_count: 1
- response_hash: 1c3413d3f91132ec504a56577dc767bff2e8bdab676aba16c1102beeb4d910d8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:16:14.543
- end: 2026-08-13T21:16:14.543
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: d65d39911bb7e5ed6e7b5ed509d24bc21fe5ec5b581f03e378fea8f209d33b5e
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:16:14.543
- end: 2026-08-13T21:16:14.543
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:14.543+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:16:14.543
- end: 2026-08-13T21:16:14.543
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:14.543+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:16:14.544
- request_duration_ms: 3303
- success: True
- final_source: compile_terminal

