# RAG Process

audit_id: 20260814_173500_302_ea7c3e47
timestamp: 2026-08-14T17:35:00.302
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T17:35:00.302
- end: 2026-08-14T17:35:00.302
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T17:35:03.326
- end: 2026-08-14T17:35:03.326
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['排骨'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4566
- attempt_count: 1
- response_hash: 775c9b64d96a4427a89357b906301818e6a3419076754b9b5590ecfcd2ae10de
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T17:35:03.343
- end: 2026-08-14T17:35:03.343
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 110a18a4c5639d69a5e6c3191e82653acaaf393d8241c48c80442ed42c462a8d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T17:35:03.344
- end: 2026-08-14T17:35:03.344
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:35:03.344+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T17:35:03.346
- end: 2026-08-14T17:35:03.346
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:35:03.344+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:35:03.346
- end: 2026-08-14T17:35:03.346
- duration_ms: 0
- entity_id: 201001698
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:35:03.355
- end: 2026-08-14T17:35:03.355
- duration_ms: 0
- parent_id: 201001698
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:35:03.355
- end: 2026-08-14T17:35:03.355
- duration_ms: 0
- entity_id: 201002937
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:35:03.362
- end: 2026-08-14T17:35:03.361
- duration_ms: 0
- parent_id: 201002937
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:35:03.362
- end: 2026-08-14T17:35:03.362
- duration_ms: 0
- entity_id: 201003296
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:35:03.368
- end: 2026-08-14T17:35:03.368
- duration_ms: 0
- parent_id: 201003296
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:35:03.368
- end: 2026-08-14T17:35:03.368
- duration_ms: 0
- entity_id: 201003336
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:35:03.374
- end: 2026-08-14T17:35:03.374
- duration_ms: 0
- parent_id: 201003336
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:35:03.374
- end: 2026-08-14T17:35:03.374
- duration_ms: 0
- entity_id: 201003873
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:35:03.381
- end: 2026-08-14T17:35:03.381
- duration_ms: 0
- parent_id: 201003873
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:35:03.381
- end: 2026-08-14T17:35:03.381
- duration_ms: 0
- entity_id: 201003902
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:35:03.388
- end: 2026-08-14T17:35:03.388
- duration_ms: 0
- parent_id: 201003902
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:35:03.388
- end: 2026-08-14T17:35:03.388
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:35:03.396
- end: 2026-08-14T17:35:03.396
- duration_ms: 0
- parent_id: 201003939
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 8788
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 7
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
- duration_ms: 13335
- response_chars: 557
- response_hash: b239b93d6c63ea70

## Final Output
- answer_chars: 557
- answer_hash: b239b93d6c63ea70
- success: True

## Request Complete
- request_end: 2026-08-14T17:35:16.732
- request_duration_ms: 16430
- success: True
- final_source: generation

