# RAG Process

audit_id: 20260814_154940_061_030caa37
timestamp: 2026-08-14T15:49:40.062
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:49:40.062
- end: 2026-08-14T15:49:40.062
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 18

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:49:47.342
- end: 2026-08-14T15:49:47.341
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.93
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7279
- attempt_count: 1
- response_hash: 15176f504fce1eeb58a658ea3729ad228df0b93388dfa197d3eb92649b069cdc
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:49:47.370
- end: 2026-08-14T15:49:47.370
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 88bff1ad6249d4cc4f0cfa9c15f0b5d7cea591beb9bb77173d342a1a7651332b
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:49:47.371
- end: 2026-08-14T15:49:47.371
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:49:47.371+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T15:49:47.375
- end: 2026-08-14T15:49:47.375
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:49:47.371+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T15:49:47.376
- request_duration_ms: 7313
- success: True
- final_source: compile_terminal

