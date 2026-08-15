# RAG Process

audit_id: 20260813_193731_628_6bf1432b
timestamp: 2026-08-13T19:37:31.629
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:37:31.629
- end: 2026-08-13T19:37:31.629
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:37:34.866
- end: 2026-08-13T19:37:34.866
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3236
- attempt_count: 1
- response_hash: 94eb170b4178b6c743374667e24edcce850650c2084422183e3f5b812380f613
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:37:34.869
- end: 2026-08-13T19:37:34.869
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: a84a6f1cba0aefb02b017f9fe349a84a11791dfb965cd3612bf5e752eb8f2235
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:37:34.870
- end: 2026-08-13T19:37:34.870
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:37:34.870+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: not_found
- start: 2026-08-13T19:37:34.871
- end: 2026-08-13T19:37:34.871
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T19:37:34.870+00:00
- result_count: 0

## Request Complete
- request_end: 2026-08-13T19:37:34.871
- request_duration_ms: 3242
- success: True
- final_source: compile_terminal

