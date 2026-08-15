# RAG Process

audit_id: 20260814_154959_662_187e3e4b
timestamp: 2026-08-14T15:49:59.664
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:49:59.665
- end: 2026-08-14T15:49:59.665
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:50:05.505
- end: 2026-08-14T15:50:05.505
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5839
- attempt_count: 1
- response_hash: 8baf24d2509e3f9b2a2e6d5701c4e3c96c7011c6b0ac9c5a6d8277f8ae94fb72
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:50:05.516
- end: 2026-08-14T15:50:05.516
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: be22ac259a9e4282b29805f500ec1cec4f09bb9b7f6005ce6cc58179d430ad90
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:50:05.516
- end: 2026-08-14T15:50:05.516
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:05.516+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T15:50:05.518
- end: 2026-08-14T15:50:05.518
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:05.516+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T15:50:05.518
- request_duration_ms: 5853
- success: True
- final_source: compile_terminal

