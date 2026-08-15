# RAG Process

audit_id: 20260814_212225_193_613eb9f7
timestamp: 2026-08-14T21:22:25.193
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T21:22:25.194
- end: 2026-08-14T21:22:25.194
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T21:22:28.947
- end: 2026-08-14T21:22:28.947
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['南瓜'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3753
- attempt_count: 1
- response_hash: 92dd22b0624a1f2f0325de43831ffb7268a7ab94dd3b5fc0561b211e22677719
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T21:22:28.961
- end: 2026-08-14T21:22:28.961
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: ae4d9ca251149a902687bbebd9ef0155d50473f044ba014041daf05261f17fd9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T21:22:28.962
- end: 2026-08-14T21:22:28.962
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:22:28.962+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T21:22:28.962
- end: 2026-08-14T21:22:28.962
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T21:22:28.962+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T21:22:28.962
- request_duration_ms: 3768
- success: True
- final_source: compile_terminal

