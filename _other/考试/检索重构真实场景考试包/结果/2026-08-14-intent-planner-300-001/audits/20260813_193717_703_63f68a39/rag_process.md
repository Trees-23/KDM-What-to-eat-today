# RAG Process

audit_id: 20260813_193717_703_63f68a39
timestamp: 2026-08-13T19:37:17.705
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:37:17.705
- end: 2026-08-13T19:37:17.705
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:37:20.842
- end: 2026-08-13T19:37:20.842
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3715
- attempt_count: 1
- response_hash: 7f8e2fa78a25c45b3bbef053639130df667dde291611153b601bc0d8bb136bf9
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:37:20.845
- end: 2026-08-13T19:37:20.845
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: be22ac259a9e4282b29805f500ec1cec4f09bb9b7f6005ce6cc58179d430ad90
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:37:20.846
- end: 2026-08-13T19:37:20.846
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:37:20.846+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-13T19:37:20.847
- end: 2026-08-13T19:37:20.847
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:37:20.846+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-13T19:37:20.847
- request_duration_ms: 3142
- success: True
- final_source: compile_terminal

