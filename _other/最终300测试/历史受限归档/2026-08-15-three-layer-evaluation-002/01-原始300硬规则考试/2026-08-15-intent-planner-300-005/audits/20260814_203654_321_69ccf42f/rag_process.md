# RAG Process

audit_id: 20260814_203654_321_69ccf42f
timestamp: 2026-08-14T20:36:54.322
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:36:54.322
- end: 2026-08-14T20:36:54.322
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:36:58.926
- end: 2026-08-14T20:36:58.926
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['土豆'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4604
- attempt_count: 1
- response_hash: 2e24f9ea6ad28b4b3cf5f3a18b2558b17f8158eea10bdc5cf5d0a471720cd253
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:36:58.942
- end: 2026-08-14T20:36:58.942
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 0c4d511ef3bb366ebc11daa4919872543eb40da4eda5a78aa74eb53b4f1aefba
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:36:58.943
- end: 2026-08-14T20:36:58.943
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:36:58.943+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:36:58.956
- end: 2026-08-14T20:36:58.956
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:36:58.943+00:00
- result_count: 16

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:58.956
- end: 2026-08-14T20:36:58.956
- duration_ms: 0
- entity_id: 201001891
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:58.968
- end: 2026-08-14T20:36:58.968
- duration_ms: 0
- parent_id: 201001891
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:58.969
- end: 2026-08-14T20:36:58.968
- duration_ms: 0
- entity_id: 201002122
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:58.978
- end: 2026-08-14T20:36:58.978
- duration_ms: 0
- parent_id: 201002122
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:58.978
- end: 2026-08-14T20:36:58.978
- duration_ms: 0
- entity_id: 201002309
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:58.989
- end: 2026-08-14T20:36:58.989
- duration_ms: 0
- parent_id: 201002309
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:58.990
- end: 2026-08-14T20:36:58.990
- duration_ms: 0
- entity_id: 201002369
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:58.996
- end: 2026-08-14T20:36:58.996
- duration_ms: 0
- parent_id: 201002369
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:58.996
- end: 2026-08-14T20:36:58.996
- duration_ms: 0
- entity_id: 201002575
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.002
- end: 2026-08-14T20:36:59.002
- duration_ms: 0
- parent_id: 201002575
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.003
- end: 2026-08-14T20:36:59.003
- duration_ms: 0
- entity_id: 201002647
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.009
- end: 2026-08-14T20:36:59.009
- duration_ms: 0
- parent_id: 201002647
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.009
- end: 2026-08-14T20:36:59.009
- duration_ms: 0
- entity_id: 201002920
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.016
- end: 2026-08-14T20:36:59.016
- duration_ms: 0
- parent_id: 201002920
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.016
- end: 2026-08-14T20:36:59.016
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.022
- end: 2026-08-14T20:36:59.022
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.023
- end: 2026-08-14T20:36:59.023
- duration_ms: 0
- entity_id: 201003275
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.029
- end: 2026-08-14T20:36:59.029
- duration_ms: 0
- parent_id: 201003275
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.029
- end: 2026-08-14T20:36:59.029
- duration_ms: 0
- entity_id: 201003355
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.035
- end: 2026-08-14T20:36:59.035
- duration_ms: 0
- parent_id: 201003355
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.035
- end: 2026-08-14T20:36:59.035
- duration_ms: 0
- entity_id: 201004525
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.041
- end: 2026-08-14T20:36:59.041
- duration_ms: 0
- parent_id: 201004525
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.041
- end: 2026-08-14T20:36:59.041
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.047
- end: 2026-08-14T20:36:59.047
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.047
- end: 2026-08-14T20:36:59.047
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.053
- end: 2026-08-14T20:36:59.053
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.053
- end: 2026-08-14T20:36:59.053
- duration_ms: 0
- entity_id: 201005195
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.059
- end: 2026-08-14T20:36:59.059
- duration_ms: 0
- parent_id: 201005195
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.059
- end: 2026-08-14T20:36:59.059
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.065
- end: 2026-08-14T20:36:59.065
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:59.065
- end: 2026-08-14T20:36:59.065
- duration_ms: 0
- entity_id: 201005422
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:59.071
- end: 2026-08-14T20:36:59.071
- duration_ms: 0
- parent_id: 201005422
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 20976
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 16
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
- duration_ms: 16898
- response_chars: 800
- response_hash: 3fb2b42497e5851a

## Final Output
- answer_chars: 800
- answer_hash: 3fb2b42497e5851a
- success: True

## Request Complete
- request_end: 2026-08-14T20:37:15.971
- request_duration_ms: 21648
- success: True
- final_source: generation

