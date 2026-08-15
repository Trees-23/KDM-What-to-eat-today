# RAG Process

audit_id: 20260814_204912_751_a9165ad6
timestamp: 2026-08-14T20:49:12.751
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:49:12.752
- end: 2026-08-14T20:49:12.752
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:49:19.964
- end: 2026-08-14T20:49:19.964
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7212
- attempt_count: 1
- response_hash: c587e941c89b242a94d61f718f8ffbd99831d0a21770ea55fed9b9a9642bc60b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:49:19.984
- end: 2026-08-14T20:49:19.984
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 1a3af5ec3cfc9d93ad13cd40fc86443b99dc90d10e42b4554e17c02719e9746d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:49:19.984
- end: 2026-08-14T20:49:19.984
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:49:19.984+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T20:49:19.987
- end: 2026-08-14T20:49:19.987
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:49:19.984+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T20:49:19.988
- request_duration_ms: 7236
- success: True
- final_source: compile_terminal

