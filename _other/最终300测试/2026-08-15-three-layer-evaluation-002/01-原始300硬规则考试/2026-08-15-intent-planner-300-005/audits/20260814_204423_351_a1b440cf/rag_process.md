# RAG Process

audit_id: 20260814_204423_351_a1b440cf
timestamp: 2026-08-14T20:44:23.351
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:44:23.351
- end: 2026-08-14T20:44:23.351
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:44:27.148
- end: 2026-08-14T20:44:27.148
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3797
- attempt_count: 1
- response_hash: 6739ef5c5411fd3855134204129b7ac971b10cc6da71085f7af8122ee3fd8500
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:44:27.156
- end: 2026-08-14T20:44:27.156
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 1237b3361a50c2efe25bbbdd6b02c140372db4969fa02528659299f34a60a3b4
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:44:27.156
- end: 2026-08-14T20:44:27.156
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:44:27.156+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:44:27.159
- end: 2026-08-14T20:44:27.159
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:44:27.156+00:00
- result_count: 36

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.159
- end: 2026-08-14T20:44:27.159
- duration_ms: 0
- entity_id: 201002122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.165
- end: 2026-08-14T20:44:27.165
- duration_ms: 0
- parent_id: 201002122
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.165
- end: 2026-08-14T20:44:27.165
- duration_ms: 0
- entity_id: 201002309
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.171
- end: 2026-08-14T20:44:27.171
- duration_ms: 0
- parent_id: 201002309
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.171
- end: 2026-08-14T20:44:27.171
- duration_ms: 0
- entity_id: 201002575
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.177
- end: 2026-08-14T20:44:27.177
- duration_ms: 0
- parent_id: 201002575
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.178
- end: 2026-08-14T20:44:27.177
- duration_ms: 0
- entity_id: 201002647
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.183
- end: 2026-08-14T20:44:27.183
- duration_ms: 0
- parent_id: 201002647
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.183
- end: 2026-08-14T20:44:27.183
- duration_ms: 0
- entity_id: 201002920
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.189
- end: 2026-08-14T20:44:27.189
- duration_ms: 0
- parent_id: 201002920
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.189
- end: 2026-08-14T20:44:27.189
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.195
- end: 2026-08-14T20:44:27.195
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.195
- end: 2026-08-14T20:44:27.195
- duration_ms: 0
- entity_id: 201003275
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.202
- end: 2026-08-14T20:44:27.202
- duration_ms: 0
- parent_id: 201003275
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.202
- end: 2026-08-14T20:44:27.202
- duration_ms: 0
- entity_id: 201003355
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.208
- end: 2026-08-14T20:44:27.208
- duration_ms: 0
- parent_id: 201003355
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.208
- end: 2026-08-14T20:44:27.208
- duration_ms: 0
- entity_id: 201004525
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.214
- end: 2026-08-14T20:44:27.214
- duration_ms: 0
- parent_id: 201004525
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.214
- end: 2026-08-14T20:44:27.214
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.220
- end: 2026-08-14T20:44:27.220
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.220
- end: 2026-08-14T20:44:27.220
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.226
- end: 2026-08-14T20:44:27.226
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.227
- end: 2026-08-14T20:44:27.227
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.233
- end: 2026-08-14T20:44:27.233
- duration_ms: 0
- parent_id: 201005195
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:27.233
- end: 2026-08-14T20:44:27.233
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:27.239
- end: 2026-08-14T20:44:27.239
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 25441
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 13
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
- duration_ms: 19082
- response_chars: 467
- response_hash: 51b4f7a468c76a42

## Final Output
- answer_chars: 467
- answer_hash: 51b4f7a468c76a42
- success: True

## Request Complete
- request_end: 2026-08-14T20:44:46.322
- request_duration_ms: 22971
- success: True
- final_source: generation

