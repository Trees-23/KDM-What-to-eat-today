# RAG Process

audit_id: 20260814_204538_122_fe4c141e
timestamp: 2026-08-14T20:45:38.122
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:45:38.123
- end: 2026-08-14T20:45:38.123
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 10

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:45:42.447
- end: 2026-08-14T20:45:42.447
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4324
- attempt_count: 1
- response_hash: d189b1e162d84b42d89c7518e8531146eaea766dd302276474e5a9ddfd4b0e80
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:45:42.454
- end: 2026-08-14T20:45:42.454
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 4062df9525f0148c7eac69740706ace8e3b824994a13b40d182600131ed2461b
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:45:42.454
- end: 2026-08-14T20:45:42.454
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:45:42.454+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:45:42.456
- end: 2026-08-14T20:45:42.456
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:45:42.454+00:00
- result_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:45:42.456
- end: 2026-08-14T20:45:42.456
- duration_ms: 0
- entity_id: 201000272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:45:42.464
- end: 2026-08-14T20:45:42.464
- duration_ms: 0
- parent_id: 201000272
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2565
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 1
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 6630
- response_chars: 147
- response_hash: 002e35c618fa2106

## Final Output
- answer_chars: 147
- answer_hash: 002e35c618fa2106
- success: True

## Request Complete
- request_end: 2026-08-14T20:45:49.096
- request_duration_ms: 10973
- success: True
- final_source: generation

