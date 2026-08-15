# RAG Process

audit_id: 20260814_155011_654_736b9553
timestamp: 2026-08-14T15:50:11.655
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:50:11.655
- end: 2026-08-14T15:50:11.655
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:50:17.331
- end: 2026-08-14T15:50:17.331
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5676
- attempt_count: 1
- response_hash: 707f14e1a336220a9f52a86cceaf17ce9e2c42935ba29a28f1fa7d198fb71447
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:50:17.362
- end: 2026-08-14T15:50:17.362
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 1a3af5ec3cfc9d93ad13cd40fc86443b99dc90d10e42b4554e17c02719e9746d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:50:17.363
- end: 2026-08-14T15:50:17.363
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:17.363+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T15:50:17.368
- end: 2026-08-14T15:50:17.368
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:50:17.363+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T15:50:17.369
- request_duration_ms: 5713
- success: True
- final_source: compile_terminal

