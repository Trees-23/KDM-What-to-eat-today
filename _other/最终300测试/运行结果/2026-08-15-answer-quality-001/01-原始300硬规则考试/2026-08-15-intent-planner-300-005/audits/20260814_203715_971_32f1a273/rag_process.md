# RAG Process

audit_id: 20260814_203715_971_32f1a273
timestamp: 2026-08-14T20:37:15.971
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:37:15.971
- end: 2026-08-14T20:37:15.971
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:37:19.735
- end: 2026-08-14T20:37:19.735
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['茄子'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3764
- attempt_count: 1
- response_hash: 70e7a54405046acf776d39dc485f1a6bd9bc44b0db0824a8deab214c00747702
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:37:19.752
- end: 2026-08-14T20:37:19.752
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 26f67e4276e5e3ae393e720125ec5c97e34bdb546f1c1818614d295d6f37a8ea
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:37:19.753
- end: 2026-08-14T20:37:19.753
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:37:19.753+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:37:19.756
- end: 2026-08-14T20:37:19.756
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:37:19.753+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:19.756
- end: 2026-08-14T20:37:19.756
- duration_ms: 0
- entity_id: 201003459
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:19.770
- end: 2026-08-14T20:37:19.770
- duration_ms: 0
- parent_id: 201003459
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:19.770
- end: 2026-08-14T20:37:19.770
- duration_ms: 0
- entity_id: 201004731
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:19.780
- end: 2026-08-14T20:37:19.780
- duration_ms: 0
- parent_id: 201004731
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:19.780
- end: 2026-08-14T20:37:19.780
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:19.786
- end: 2026-08-14T20:37:19.786
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:19.786
- end: 2026-08-14T20:37:19.786
- duration_ms: 0
- entity_id: 201005001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:19.792
- end: 2026-08-14T20:37:19.792
- duration_ms: 0
- parent_id: 201005001
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:19.792
- end: 2026-08-14T20:37:19.792
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:19.798
- end: 2026-08-14T20:37:19.798
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:19.798
- end: 2026-08-14T20:37:19.798
- duration_ms: 0
- entity_id: 201005146
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:19.805
- end: 2026-08-14T20:37:19.805
- duration_ms: 0
- parent_id: 201005146
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:37:19.805
- end: 2026-08-14T20:37:19.805
- duration_ms: 0
- entity_id: 201005492
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:37:19.812
- end: 2026-08-14T20:37:19.812
- duration_ms: 0
- parent_id: 201005492
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 9036
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
- duration_ms: 12347
- response_chars: 492
- response_hash: 2920d7ff258a11cb

## Final Output
- answer_chars: 492
- answer_hash: 2920d7ff258a11cb
- success: True

## Request Complete
- request_end: 2026-08-14T20:37:32.160
- request_duration_ms: 16189
- success: True
- final_source: generation

