# RAG Process

audit_id: 20260814_204121_393_8fa3479a
timestamp: 2026-08-14T20:41:21.394
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:41:21.394
- end: 2026-08-14T20:41:21.394
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:41:24.944
- end: 2026-08-14T20:41:24.944
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3550
- attempt_count: 1
- response_hash: f04e6d69988a672284f84515d8d4bfb5041703c07cb158bdd7914b0599c14792
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:41:24.953
- end: 2026-08-14T20:41:24.953
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: e71a3c5f96904496a022cbe7edbe063a605d5ae4d4fb43f5c87aad3d053b53ee
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:41:24.953
- end: 2026-08-14T20:41:24.953
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:41:24.953+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:41:24.957
- end: 2026-08-14T20:41:24.957
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:41:24.953+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:24.957
- end: 2026-08-14T20:41:24.957
- duration_ms: 0
- entity_id: 201002146
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:24.967
- end: 2026-08-14T20:41:24.967
- duration_ms: 0
- parent_id: 201002146
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:24.967
- end: 2026-08-14T20:41:24.967
- duration_ms: 0
- entity_id: 201003534
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:24.973
- end: 2026-08-14T20:41:24.973
- duration_ms: 0
- parent_id: 201003534
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:24.973
- end: 2026-08-14T20:41:24.973
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:24.980
- end: 2026-08-14T20:41:24.980
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:24.980
- end: 2026-08-14T20:41:24.980
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:24.986
- end: 2026-08-14T20:41:24.986
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:24.986
- end: 2026-08-14T20:41:24.986
- duration_ms: 0
- entity_id: 201004793
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:24.992
- end: 2026-08-14T20:41:24.992
- duration_ms: 0
- parent_id: 201004793
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:24.992
- end: 2026-08-14T20:41:24.992
- duration_ms: 0
- entity_id: 201004885
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:24.998
- end: 2026-08-14T20:41:24.998
- duration_ms: 0
- parent_id: 201004885
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:24.998
- end: 2026-08-14T20:41:24.998
- duration_ms: 0
- entity_id: 201005272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:25.004
- end: 2026-08-14T20:41:25.004
- duration_ms: 0
- parent_id: 201005272
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 8424
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
- duration_ms: 9327
- response_chars: 335
- response_hash: c8883b5519724764

## Final Output
- answer_chars: 335
- answer_hash: c8883b5519724764
- success: True

## Request Complete
- request_end: 2026-08-14T20:41:34.332
- request_duration_ms: 12938
- success: True
- final_source: generation

