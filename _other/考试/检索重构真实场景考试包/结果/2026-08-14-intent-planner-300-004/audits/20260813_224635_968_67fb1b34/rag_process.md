# RAG Process

audit_id: 20260813_224635_968_67fb1b34
timestamp: 2026-08-13T22:46:35.977
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:46:35.979
- end: 2026-08-13T22:46:35.979
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:46:39.657
- end: 2026-08-13T22:46:39.657
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3678
- attempt_count: 1
- response_hash: b187f8843651c2488382323e6344f4b441daf04c8901d3604e6225d44a30e74d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:46:39.663
- end: 2026-08-13T22:46:39.663
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 8eac1850c425a36f563174d816ccf01dda0e57906076e8bb174a17eeae660735
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:46:39.664
- end: 2026-08-13T22:46:39.664
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:39.664+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:46:39.664
- end: 2026-08-13T22:46:39.664
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:39.664+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:46:39.664
- request_duration_ms: 3685
- success: True
- final_source: compile_terminal

