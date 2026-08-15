# RAG Process

audit_id: 20260814_163113_999_a332b749
timestamp: 2026-08-14T16:31:14.011
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:31:14.011
- end: 2026-08-14T16:31:14.011
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 9

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:31:17.926
- end: 2026-08-14T16:31:17.926
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['金针菇'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3914
- attempt_count: 1
- response_hash: ca1add6e26f1391a3780660e14554d694f9a5cede63484789623e19e14bc9ab2
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:31:17.942
- end: 2026-08-14T16:31:17.942
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 11f888249c3807bb3a2eaeafff5f41bcbab3ac3d19c4799bcfef69694be8d1a2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:31:17.942
- end: 2026-08-14T16:31:17.942
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:17.942+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: unavailable
- start: 2026-08-14T16:31:17.942
- end: 2026-08-14T16:31:17.942
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:31:17.942+00:00
- error_type: OSError

## Request Complete
- request_end: 2026-08-14T16:31:17.942
- request_duration_ms: 3931
- success: True
- final_source: compile_terminal

