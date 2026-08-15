# RAG Process

audit_id: 20260813_224648_361_65212ed0
timestamp: 2026-08-13T22:46:48.362
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:46:48.362
- end: 2026-08-13T22:46:48.362
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:46:51.929
- end: 2026-08-13T22:46:51.929
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3566
- attempt_count: 1
- response_hash: 9bfdd37a432757abadc98596e54f69c6e5c8d6a330d7c963e71179428cabbb56
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:46:51.931
- end: 2026-08-13T22:46:51.931
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 7df3f0dc5749160777e03a4f4a37bffd31853b180dbeaf40c8e7ff02c1954e55
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:46:51.932
- end: 2026-08-13T22:46:51.932
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:51.932+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:46:51.932
- end: 2026-08-13T22:46:51.932
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:51.932+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:46:51.932
- request_duration_ms: 3569
- success: True
- final_source: compile_terminal

