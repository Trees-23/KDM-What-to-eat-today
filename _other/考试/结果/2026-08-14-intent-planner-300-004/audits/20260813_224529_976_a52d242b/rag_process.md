# RAG Process

audit_id: 20260813_224529_976_a52d242b
timestamp: 2026-08-13T22:45:29.976
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:45:29.977
- end: 2026-08-13T22:45:29.977
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 7

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:45:32.325
- end: 2026-08-13T22:45:32.325
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3158
- attempt_count: 1
- response_hash: 025fde6b21b08c71879ff7667fe2858507b1720490c26b8941d1a5d749dbbcf3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:45:32.329
- end: 2026-08-13T22:45:32.329
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: a7f0ebc6e455415114ea01b7167b88b25107fd706779f78fa6b832c68d5bca92
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:45:32.330
- end: 2026-08-13T22:45:32.330
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:45:32.330+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:45:32.330
- end: 2026-08-13T22:45:32.330
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:45:32.330+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:45:32.330
- request_duration_ms: 2353
- success: True
- final_source: compile_terminal

