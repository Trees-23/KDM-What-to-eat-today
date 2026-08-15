# RAG Process

audit_id: 20260814_162948_779_f570f038
timestamp: 2026-08-14T16:29:48.790
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:29:48.790
- end: 2026-08-14T16:29:48.790
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 7

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:29:55.172
- end: 2026-08-14T16:29:55.172
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['虾'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6381
- attempt_count: 1
- response_hash: 7225c6bbfd4d3ce11f0c95893b8d22d60f877d597d6db882c015c473422fdef6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:29:55.188
- end: 2026-08-14T16:29:55.188
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: a7f0ebc6e455415114ea01b7167b88b25107fd706779f78fa6b832c68d5bca92
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:29:55.188
- end: 2026-08-14T16:29:55.188
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:55.188+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:29:55.189
- end: 2026-08-14T16:29:55.189
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:29:55.188+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:29:55.189
- request_duration_ms: 6398
- success: True
- final_source: compile_terminal

