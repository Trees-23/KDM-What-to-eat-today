# RAG Process

audit_id: 20260813_225739_867_87c3dff6
timestamp: 2026-08-13T22:57:39.868
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:57:39.868
- end: 2026-08-13T22:57:39.868
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:57:44.146
- end: 2026-08-13T22:57:44.146
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4277
- attempt_count: 1
- response_hash: 5ddb3c1794ce9b2f8e67076962e55d3371a432187fb8b4b8c7a73abba1d9dc62
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:57:44.166
- end: 2026-08-13T22:57:44.166
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 9cb6f2919dade2c3198014703353b0050855fc4f908ffb68ede50d59ce152d1e
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:57:44.167
- end: 2026-08-13T22:57:44.167
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:57:44.167+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:57:44.171
- end: 2026-08-13T22:57:44.171
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:57:44.167+00:00
- result_count: 14

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:57:44.171
- end: 2026-08-13T22:57:44.171
- duration_ms: 0
- entity_id: 201003459
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:57:44.182
- end: 2026-08-13T22:57:44.182
- duration_ms: 0
- parent_id: 201003459
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:57:44.182
- end: 2026-08-13T22:57:44.182
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:57:44.191
- end: 2026-08-13T22:57:44.191
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:57:44.191
- end: 2026-08-13T22:57:44.191
- duration_ms: 0
- entity_id: 201005001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:57:44.198
- end: 2026-08-13T22:57:44.198
- duration_ms: 0
- parent_id: 201005001
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:57:44.199
- end: 2026-08-13T22:57:44.199
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:57:44.205
- end: 2026-08-13T22:57:44.205
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:57:44.205
- end: 2026-08-13T22:57:44.205
- duration_ms: 0
- entity_id: 201005146
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:57:44.211
- end: 2026-08-13T22:57:44.211
- duration_ms: 0
- parent_id: 201005146
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:57:44.211
- end: 2026-08-13T22:57:44.211
- duration_ms: 0
- entity_id: 201005492
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:57:44.217
- end: 2026-08-13T22:57:44.217
- duration_ms: 0
- parent_id: 201005492
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 11141
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 6
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 10789
- response_chars: 394
- response_hash: b82a1998038ef5e4

## Final Output
- answer_chars: 394
- answer_hash: b82a1998038ef5e4
- success: True

## Request Complete
- request_end: 2026-08-13T22:57:55.008
- request_duration_ms: 15139
- success: True
- final_source: generation

