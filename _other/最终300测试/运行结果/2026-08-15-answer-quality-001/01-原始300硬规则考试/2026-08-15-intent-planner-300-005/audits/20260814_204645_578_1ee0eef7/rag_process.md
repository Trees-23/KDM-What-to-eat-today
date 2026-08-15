# RAG Process

audit_id: 20260814_204645_578_1ee0eef7
timestamp: 2026-08-14T20:46:45.578
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:46:45.578
- end: 2026-08-14T20:46:45.578
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:46:49.132
- end: 2026-08-14T20:46:49.132
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.94
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3553
- attempt_count: 1
- response_hash: 85f953fffdfb792b8fa8f85a01291a29d77b8a741cd231873476bcbb9a2be14b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:46:49.148
- end: 2026-08-14T20:46:49.148
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: c7f5c8ce174552bdcbaa7c555b482b92f4c96d4e52a49f61c050f084b9b50d96
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:46:49.148
- end: 2026-08-14T20:46:49.148
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:46:49.148+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:46:49.152
- end: 2026-08-14T20:46:49.152
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:46:49.148+00:00
- result_count: 6

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:46:49.152
- end: 2026-08-14T20:46:49.152
- duration_ms: 0
- entity_id: 201001428
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:46:49.165
- end: 2026-08-14T20:46:49.165
- duration_ms: 0
- parent_id: 201001428
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:46:49.166
- end: 2026-08-14T20:46:49.166
- duration_ms: 0
- entity_id: 201002327
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:46:49.174
- end: 2026-08-14T20:46:49.174
- duration_ms: 0
- parent_id: 201002327
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4273
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 2
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
- duration_ms: 9078
- response_chars: 278
- response_hash: b2288daa01817e88

## Final Output
- answer_chars: 278
- answer_hash: b2288daa01817e88
- success: True

## Request Complete
- request_end: 2026-08-14T20:46:58.254
- request_duration_ms: 12675
- success: True
- final_source: generation

