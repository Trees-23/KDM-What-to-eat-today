# RAG Process

audit_id: 20260813_221709_483_5b3710a7
timestamp: 2026-08-13T22:17:09.484
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:17:09.484
- end: 2026-08-13T22:17:09.484
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:17:13.433
- end: 2026-08-13T22:17:13.433
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3949
- attempt_count: 1
- response_hash: 09801607262baf2dfd3cffd6a6b0c46000def50ea56f31cb2e0129ee110ac56c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:17:13.437
- end: 2026-08-13T22:17:13.437
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 1237b3361a50c2efe25bbbdd6b02c140372db4969fa02528659299f34a60a3b4
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:17:13.437
- end: 2026-08-13T22:17:13.437
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:17:13.437+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:17:13.446
- end: 2026-08-13T22:17:13.446
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:17:13.437+00:00
- result_count: 36

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.447
- end: 2026-08-13T22:17:13.447
- duration_ms: 0
- entity_id: 201002122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.455
- end: 2026-08-13T22:17:13.455
- duration_ms: 0
- parent_id: 201002122
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.455
- end: 2026-08-13T22:17:13.455
- duration_ms: 0
- entity_id: 201002309
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.461
- end: 2026-08-13T22:17:13.461
- duration_ms: 0
- parent_id: 201002309
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.462
- end: 2026-08-13T22:17:13.462
- duration_ms: 0
- entity_id: 201002575
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.468
- end: 2026-08-13T22:17:13.468
- duration_ms: 0
- parent_id: 201002575
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.468
- end: 2026-08-13T22:17:13.468
- duration_ms: 0
- entity_id: 201002647
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.475
- end: 2026-08-13T22:17:13.475
- duration_ms: 0
- parent_id: 201002647
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.475
- end: 2026-08-13T22:17:13.475
- duration_ms: 0
- entity_id: 201002920
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.481
- end: 2026-08-13T22:17:13.481
- duration_ms: 0
- parent_id: 201002920
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.481
- end: 2026-08-13T22:17:13.481
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.488
- end: 2026-08-13T22:17:13.488
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.488
- end: 2026-08-13T22:17:13.488
- duration_ms: 0
- entity_id: 201003275
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.494
- end: 2026-08-13T22:17:13.494
- duration_ms: 0
- parent_id: 201003275
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.494
- end: 2026-08-13T22:17:13.494
- duration_ms: 0
- entity_id: 201003355
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.501
- end: 2026-08-13T22:17:13.501
- duration_ms: 0
- parent_id: 201003355
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.501
- end: 2026-08-13T22:17:13.501
- duration_ms: 0
- entity_id: 201004525
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.507
- end: 2026-08-13T22:17:13.507
- duration_ms: 0
- parent_id: 201004525
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.508
- end: 2026-08-13T22:17:13.508
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.515
- end: 2026-08-13T22:17:13.515
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.515
- end: 2026-08-13T22:17:13.515
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.523
- end: 2026-08-13T22:17:13.523
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.524
- end: 2026-08-13T22:17:13.524
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.533
- end: 2026-08-13T22:17:13.533
- duration_ms: 0
- parent_id: 201005195
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:17:13.533
- end: 2026-08-13T22:17:13.533
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:17:13.540
- end: 2026-08-13T22:17:13.540
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 18274
- response_chars: 711
- response_hash: 4b0948f31c43236d

## Final Output
- answer_chars: 711
- answer_hash: 4b0948f31c43236d
- success: True

## Request Complete
- request_end: 2026-08-13T22:17:31.816
- request_duration_ms: 22331
- success: True
- final_source: generation

