# RAG Process

audit_id: 20260813_224604_816_b0d91b60
timestamp: 2026-08-13T22:46:04.817
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:46:04.818
- end: 2026-08-13T22:46:04.818
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:46:08.766
- end: 2026-08-13T22:46:08.766
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3948
- attempt_count: 1
- response_hash: c364fb2dac826b522c1763f6ee8c97699cafa37fd89f2c66828214232e459007
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:46:08.773
- end: 2026-08-13T22:46:08.773
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 9aedaa8d2d7664e5c2bd13246518a7450b6d35d3b197ac0eb2e609255f2d5578
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:46:08.774
- end: 2026-08-13T22:46:08.774
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:08.774+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:46:08.774
- end: 2026-08-13T22:46:08.774
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:08.774+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:46:08.774
- request_duration_ms: 3956
- success: True
- final_source: compile_terminal

