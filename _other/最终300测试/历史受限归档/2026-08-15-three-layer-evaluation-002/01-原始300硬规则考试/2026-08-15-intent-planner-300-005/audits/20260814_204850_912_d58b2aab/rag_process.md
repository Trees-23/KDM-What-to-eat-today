# RAG Process

audit_id: 20260814_204850_912_d58b2aab
timestamp: 2026-08-14T20:48:50.913
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:48:50.913
- end: 2026-08-14T20:48:50.913
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 18

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:48:55.140
- end: 2026-08-14T20:48:55.140
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4227
- attempt_count: 1
- response_hash: 2ab1bbd3f5ecd68eb44206b309975bceed602569f6408a4d558b4e67a0812d5e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:48:55.162
- end: 2026-08-14T20:48:55.162
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 88bff1ad6249d4cc4f0cfa9c15f0b5d7cea591beb9bb77173d342a1a7651332b
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:48:55.162
- end: 2026-08-14T20:48:55.162
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:48:55.162+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T20:48:55.163
- end: 2026-08-14T20:48:55.163
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:48:55.162+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T20:48:55.163
- request_duration_ms: 4250
- success: True
- final_source: compile_terminal

