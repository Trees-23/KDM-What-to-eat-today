# RAG Process

audit_id: 20260813_211637_643_44d79071
timestamp: 2026-08-13T21:16:37.645
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:16:37.646
- end: 2026-08-13T21:16:37.646
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:16:41.321
- end: 2026-08-13T21:16:41.321
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3675
- attempt_count: 1
- response_hash: 42ce28ea798ab4073d779fa4ec6203098c02b2e0406de8665b692204c67d2f0d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:16:41.326
- end: 2026-08-13T21:16:41.326
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 17fe136647461470fc143c3f8c558a7986e47691be3fe9f9611c76f568471411
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:16:41.327
- end: 2026-08-13T21:16:41.327
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:41.327+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T21:16:41.327
- end: 2026-08-13T21:16:41.327
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T21:16:41.327+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T21:16:41.327
- request_duration_ms: 3681
- success: True
- final_source: compile_terminal

