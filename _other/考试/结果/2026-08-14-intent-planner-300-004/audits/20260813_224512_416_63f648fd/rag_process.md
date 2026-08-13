# RAG Process

audit_id: 20260813_224512_416_63f648fd
timestamp: 2026-08-13T22:45:12.417
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:45:12.418
- end: 2026-08-13T22:45:12.418
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:45:15.766
- end: 2026-08-13T22:45:15.766
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3348
- attempt_count: 1
- response_hash: 59e0406540d311c209949b9ec2a4e9f03ae92452d3d546646cac03137eb87638
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:45:15.770
- end: 2026-08-13T22:45:15.770
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 18ba07c3e1078f43f68ee84f8a9497df330f3a1c58bc835c49be86737af797fa
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:45:15.771
- end: 2026-08-13T22:45:15.771
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:45:15.771+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:45:15.771
- end: 2026-08-13T22:45:15.771
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:45:15.771+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:45:15.771
- request_duration_ms: 3353
- success: True
- final_source: compile_terminal

