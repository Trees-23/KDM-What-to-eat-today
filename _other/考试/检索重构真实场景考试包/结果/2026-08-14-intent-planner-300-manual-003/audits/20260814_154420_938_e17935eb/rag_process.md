# RAG Process

audit_id: 20260814_154420_938_e17935eb
timestamp: 2026-08-14T15:44:20.942
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:44:20.943
- end: 2026-08-14T15:44:20.943
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:44:26.268
- end: 2026-08-14T15:44:26.268
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5325
- attempt_count: 1
- response_hash: 946d3f5a4615f6ef01fed26caee70ee8e0cd39d5ad608e48776e13edad1fe84c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:44:26.301
- end: 2026-08-14T15:44:26.301
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 1237b3361a50c2efe25bbbdd6b02c140372db4969fa02528659299f34a60a3b4
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:44:26.302
- end: 2026-08-14T15:44:26.302
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:44:26.302+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:44:26.325
- end: 2026-08-14T15:44:26.325
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T15:44:26.302+00:00
- result_count: 36

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.326
- end: 2026-08-14T15:44:26.326
- duration_ms: 0
- entity_id: 201002122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.342
- end: 2026-08-14T15:44:26.342
- duration_ms: 0
- parent_id: 201002122
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.342
- end: 2026-08-14T15:44:26.342
- duration_ms: 0
- entity_id: 201002309
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.358
- end: 2026-08-14T15:44:26.358
- duration_ms: 0
- parent_id: 201002309
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.358
- end: 2026-08-14T15:44:26.358
- duration_ms: 0
- entity_id: 201002575
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.367
- end: 2026-08-14T15:44:26.367
- duration_ms: 0
- parent_id: 201002575
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.367
- end: 2026-08-14T15:44:26.367
- duration_ms: 0
- entity_id: 201002647
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.376
- end: 2026-08-14T15:44:26.376
- duration_ms: 0
- parent_id: 201002647
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.377
- end: 2026-08-14T15:44:26.377
- duration_ms: 0
- entity_id: 201002920
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.384
- end: 2026-08-14T15:44:26.384
- duration_ms: 0
- parent_id: 201002920
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.384
- end: 2026-08-14T15:44:26.384
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.392
- end: 2026-08-14T15:44:26.392
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.392
- end: 2026-08-14T15:44:26.392
- duration_ms: 0
- entity_id: 201003275
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.400
- end: 2026-08-14T15:44:26.400
- duration_ms: 0
- parent_id: 201003275
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.400
- end: 2026-08-14T15:44:26.400
- duration_ms: 0
- entity_id: 201003355
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.408
- end: 2026-08-14T15:44:26.408
- duration_ms: 0
- parent_id: 201003355
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.408
- end: 2026-08-14T15:44:26.408
- duration_ms: 0
- entity_id: 201004525
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.417
- end: 2026-08-14T15:44:26.417
- duration_ms: 0
- parent_id: 201004525
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.417
- end: 2026-08-14T15:44:26.417
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.428
- end: 2026-08-14T15:44:26.428
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.428
- end: 2026-08-14T15:44:26.428
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.439
- end: 2026-08-14T15:44:26.439
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.440
- end: 2026-08-14T15:44:26.440
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.447
- end: 2026-08-14T15:44:26.447
- duration_ms: 0
- parent_id: 201005195
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:44:26.447
- end: 2026-08-14T15:44:26.447
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:44:26.454
- end: 2026-08-14T15:44:26.454
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 32766
- response_chars: 617
- response_hash: 39a581cbbe0ecf5c

## Final Output
- answer_chars: 617
- answer_hash: 39a581cbbe0ecf5c
- success: True

## Request Complete
- request_end: 2026-08-14T15:44:59.223
- request_duration_ms: 38280
- success: True
- final_source: generation

