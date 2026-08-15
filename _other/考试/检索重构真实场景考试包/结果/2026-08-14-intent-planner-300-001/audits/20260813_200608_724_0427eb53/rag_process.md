# RAG Process

audit_id: 20260813_200608_724_0427eb53
timestamp: 2026-08-13T20:06:08.724
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:06:08.725
- end: 2026-08-13T20:06:08.725
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 7

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:06:13.267
- end: 2026-08-13T20:06:13.267
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4542
- attempt_count: 1
- response_hash: b1d2b2ddd5c5593f91d9bb132b0fda00ec62a94edbfa8f388c79061b150e6fa6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:06:13.272
- end: 2026-08-13T20:06:13.272
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: a7f0ebc6e455415114ea01b7167b88b25107fd706779f78fa6b832c68d5bca92
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:06:13.272
- end: 2026-08-13T20:06:13.272
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:13.272+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T20:06:13.272
- end: 2026-08-13T20:06:13.272
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:06:13.272+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T20:06:13.272
- request_duration_ms: 4547
- success: True
- final_source: compile_terminal

