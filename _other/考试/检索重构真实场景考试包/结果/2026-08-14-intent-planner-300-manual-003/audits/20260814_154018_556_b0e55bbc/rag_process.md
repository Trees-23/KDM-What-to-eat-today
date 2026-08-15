# RAG Process

audit_id: 20260814_154018_556_b0e55bbc
timestamp: 2026-08-14T15:40:18.557
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:40:18.557
- end: 2026-08-14T15:40:18.557
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:40:27.376
- end: 2026-08-14T15:40:27.376
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鳜鱼'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 8819
- attempt_count: 1
- response_hash: af934bf0458da38f9dfd59ab9d7469ee44d683f2d31f94b601ddee273010447c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / planner_local_reconciliation
- stage: planner_local_reconciliation
- status: recipe_detail_exact_name
- start: 2026-08-14T15:40:27.385
- end: 2026-08-14T15:40:27.385
- duration_ms: 0
- previous_intent: INGREDIENT_RECIPES
- entity_type: Recipe
- entity_id: 200000000

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:40:27.394
- end: 2026-08-14T15:40:27.394
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:40:27.395
- end: 2026-08-14T15:40:27.395
- duration_ms: 0
- entity_id: 200000000
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: not_found
- start: 2026-08-14T15:40:27.396
- end: 2026-08-14T15:40:27.396
- duration_ms: 0
- parent_id: 200000000

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 436
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 0
- limitation_count: 2
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Request Complete
- request_end: 2026-08-14T15:40:27.397
- request_duration_ms: 8839
- success: True
- final_source: generation

