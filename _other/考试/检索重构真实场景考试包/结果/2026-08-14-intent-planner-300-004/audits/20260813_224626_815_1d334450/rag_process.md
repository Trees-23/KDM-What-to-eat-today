# RAG Process

audit_id: 20260813_224626_815_1d334450
timestamp: 2026-08-13T22:46:26.816
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:46:26.816
- end: 2026-08-13T22:46:26.816
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:46:30.106
- end: 2026-08-13T22:46:30.106
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['豆角'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3290
- attempt_count: 1
- response_hash: ff4222894bd18ba49654511e6665fb1ca7b824a4f8d6bde99fe548c4b0c7404d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:46:30.110
- end: 2026-08-13T22:46:30.110
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: f71c477cc83a703d82c68977bd4642ec866991bb81d40114c6efbe8c11029e76
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:46:30.111
- end: 2026-08-13T22:46:30.111
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:30.111+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:46:30.111
- end: 2026-08-13T22:46:30.111
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:30.111+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:46:30.112
- request_duration_ms: 3296
- success: True
- final_source: compile_terminal

