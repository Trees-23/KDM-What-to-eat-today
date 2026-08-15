# RAG Process

audit_id: 20260813_224630_112_ef341840
timestamp: 2026-08-13T22:46:30.113
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:46:30.115
- end: 2026-08-13T22:46:30.115
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 8

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:46:33.498
- end: 2026-08-13T22:46:33.498
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3382
- attempt_count: 1
- response_hash: fb532577024278c71c0d23ddd9c53b8d099e6d9c305fb826c51ae1627be296d9
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:46:33.501
- end: 2026-08-13T22:46:33.501
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 2a356182272177af57ee55f6f61040941cdc431cba8d5e0ebf827fe50e7aaa56
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:46:33.501
- end: 2026-08-13T22:46:33.501
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:33.501+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-13T22:46:33.501
- end: 2026-08-13T22:46:33.501
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:46:33.501+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-13T22:46:33.502
- request_duration_ms: 3386
- success: True
- final_source: compile_terminal

