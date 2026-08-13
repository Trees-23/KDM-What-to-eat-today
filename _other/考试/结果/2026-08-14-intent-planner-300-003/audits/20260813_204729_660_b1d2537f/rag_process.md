# RAG Process

audit_id: 20260813_204729_660_b1d2537f
timestamp: 2026-08-13T20:47:29.660
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:47:29.660
- end: 2026-08-13T20:47:29.660
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:47:33.469
- end: 2026-08-13T20:47:33.469
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3809
- attempt_count: 1
- response_hash: 09801607262baf2dfd3cffd6a6b0c46000def50ea56f31cb2e0129ee110ac56c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:47:33.486
- end: 2026-08-13T20:47:33.486
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 1237b3361a50c2efe25bbbdd6b02c140372db4969fa02528659299f34a60a3b4
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:47:33.486
- end: 2026-08-13T20:47:33.486
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:47:33.486+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:47:33.497
- end: 2026-08-13T20:47:33.497
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:47:33.486+00:00
- result_count: 36

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.497
- end: 2026-08-13T20:47:33.497
- duration_ms: 0
- entity_id: 201002122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.512
- end: 2026-08-13T20:47:33.512
- duration_ms: 0
- parent_id: 201002122
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.512
- end: 2026-08-13T20:47:33.512
- duration_ms: 0
- entity_id: 201002309
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.520
- end: 2026-08-13T20:47:33.520
- duration_ms: 0
- parent_id: 201002309
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.521
- end: 2026-08-13T20:47:33.521
- duration_ms: 0
- entity_id: 201002575
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.529
- end: 2026-08-13T20:47:33.529
- duration_ms: 0
- parent_id: 201002575
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.529
- end: 2026-08-13T20:47:33.529
- duration_ms: 0
- entity_id: 201002647
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.536
- end: 2026-08-13T20:47:33.536
- duration_ms: 0
- parent_id: 201002647
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.536
- end: 2026-08-13T20:47:33.536
- duration_ms: 0
- entity_id: 201002920
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.542
- end: 2026-08-13T20:47:33.542
- duration_ms: 0
- parent_id: 201002920
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.543
- end: 2026-08-13T20:47:33.543
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.549
- end: 2026-08-13T20:47:33.549
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.549
- end: 2026-08-13T20:47:33.549
- duration_ms: 0
- entity_id: 201003275
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.557
- end: 2026-08-13T20:47:33.557
- duration_ms: 0
- parent_id: 201003275
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.557
- end: 2026-08-13T20:47:33.557
- duration_ms: 0
- entity_id: 201003355
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.564
- end: 2026-08-13T20:47:33.564
- duration_ms: 0
- parent_id: 201003355
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.564
- end: 2026-08-13T20:47:33.564
- duration_ms: 0
- entity_id: 201004525
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.572
- end: 2026-08-13T20:47:33.572
- duration_ms: 0
- parent_id: 201004525
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.572
- end: 2026-08-13T20:47:33.572
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.581
- end: 2026-08-13T20:47:33.581
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.581
- end: 2026-08-13T20:47:33.581
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.590
- end: 2026-08-13T20:47:33.590
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.590
- end: 2026-08-13T20:47:33.590
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.599
- end: 2026-08-13T20:47:33.599
- duration_ms: 0
- parent_id: 201005195
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:47:33.600
- end: 2026-08-13T20:47:33.600
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:47:33.607
- end: 2026-08-13T20:47:33.607
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_2a8c0807733eb8022a623659
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
- duration_ms: 18778
- response_chars: 746
- response_hash: 4cf02528a0a6b9a1

## Final Output
- answer_chars: 746
- answer_hash: 4cf02528a0a6b9a1
- success: True

## Request Complete
- request_end: 2026-08-13T20:47:52.386
- request_duration_ms: 22726
- success: True
- final_source: generation

