# RAG Process

audit_id: 20260814_162938_178_41e1ad3f
timestamp: 2026-08-14T16:29:38.179
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:29:38.179
- end: 2026-08-14T16:29:38.179
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:29:42.423
- end: 2026-08-14T16:29:42.423
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['茄子'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4244
- attempt_count: 1
- response_hash: bc7f29c0012b05206894d9df976a58ffac89d90a1ab14c48246b46ff94b8f6f6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:29:42.451
- end: 2026-08-14T16:29:42.451
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 26f67e4276e5e3ae393e720125ec5c97e34bdb546f1c1818614d295d6f37a8ea
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:29:42.451
- end: 2026-08-14T16:29:42.451
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:42.451+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:29:42.451
- end: 2026-08-14T16:29:42.451
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:42.451+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:29:42.451
- request_duration_ms: 4272
- success: True
- final_source: compile_terminal

