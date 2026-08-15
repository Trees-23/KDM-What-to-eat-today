# RAG Process

audit_id: 20260814_154244_941_c91c5c0c
timestamp: 2026-08-14T15:42:44.942
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:42:44.942
- end: 2026-08-14T15:42:44.942
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:42:50.166
- end: 2026-08-14T15:42:50.166
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.9
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5223
- attempt_count: 1
- response_hash: 2f9d4251b192094f9a3015b4cce4fecfe88a00511464101e601d1a8e8129b4b8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:42:50.199
- end: 2026-08-14T15:42:50.199
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: accb8121f1db606b7f217c2a68782f6bd32608cde8726058abf248dffa92498d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:42:50.200
- end: 2026-08-14T15:42:50.200
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:42:50.200+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:42:50.207
- end: 2026-08-14T15:42:50.207
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:42:50.200+00:00
- result_count: 26

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:42:50.207
- end: 2026-08-14T15:42:50.207
- duration_ms: 0
- entity_id: 201001630
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:42:50.215
- end: 2026-08-14T15:42:50.215
- duration_ms: 0
- parent_id: 201001630
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:42:50.216
- end: 2026-08-14T15:42:50.216
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:42:50.224
- end: 2026-08-14T15:42:50.224
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:42:50.224
- end: 2026-08-14T15:42:50.224
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:42:50.231
- end: 2026-08-14T15:42:50.231
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:42:50.231
- end: 2026-08-14T15:42:50.231
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:42:50.239
- end: 2026-08-14T15:42:50.239
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:42:50.239
- end: 2026-08-14T15:42:50.239
- duration_ms: 0
- entity_id: 201003314
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:42:50.247
- end: 2026-08-14T15:42:50.247
- duration_ms: 0
- parent_id: 201003314
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:42:50.247
- end: 2026-08-14T15:42:50.247
- duration_ms: 0
- entity_id: 201003507
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:42:50.254
- end: 2026-08-14T15:42:50.254
- duration_ms: 0
- parent_id: 201003507
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:42:50.255
- end: 2026-08-14T15:42:50.255
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:42:50.262
- end: 2026-08-14T15:42:50.262
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:42:50.262
- end: 2026-08-14T15:42:50.262
- duration_ms: 0
- entity_id: 201003793
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:42:50.269
- end: 2026-08-14T15:42:50.269
- duration_ms: 0
- parent_id: 201003793
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 16624
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 8
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 20377
- response_chars: 776
- response_hash: ee7c24f5d41ce879

## Final Output
- answer_chars: 776
- answer_hash: ee7c24f5d41ce879
- success: True

## Request Complete
- request_end: 2026-08-14T15:43:10.648
- request_duration_ms: 25705
- success: True
- final_source: generation

