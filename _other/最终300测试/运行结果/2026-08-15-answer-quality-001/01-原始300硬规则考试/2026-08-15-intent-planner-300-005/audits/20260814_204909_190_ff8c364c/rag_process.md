# RAG Process

audit_id: 20260814_204909_190_ff8c364c
timestamp: 2026-08-14T20:49:09.190
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:49:09.190
- end: 2026-08-14T20:49:09.190
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:49:12.738
- end: 2026-08-14T20:49:12.738
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3548
- attempt_count: 1
- response_hash: eb3f59d8e1a7fc1461304355b88a88b04e28742d717f607527bcb6789312681e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:49:12.749
- end: 2026-08-14T20:49:12.749
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 42ad5eeeae9b6055b05113016dca0781bb1fa59e6a03efab753ee004bb960190
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:49:12.750
- end: 2026-08-14T20:49:12.750
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:49:12.750+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-14T20:49:12.751
- end: 2026-08-14T20:49:12.751
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:49:12.750+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-14T20:49:12.751
- request_duration_ms: 3560
- success: True
- final_source: compile_terminal

