# RAG Process

audit_id: 20260814_203639_902_d45623ea
timestamp: 2026-08-14T20:36:39.902
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:36:39.903
- end: 2026-08-14T20:36:39.903
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:36:43.506
- end: 2026-08-14T20:36:43.506
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['豆腐'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3603
- attempt_count: 1
- response_hash: 2a0e79861798e5888bccbe7b2386036e590ec73b9918eaf2d1ba852ed4a8d93a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:36:43.521
- end: 2026-08-14T20:36:43.521
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 890120a2c84ebcc96303fb60436e87ae67dcaf7fe8cdee30bdb0c5058265a249
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:36:43.521
- end: 2026-08-14T20:36:43.521
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:36:43.521+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:36:43.523
- end: 2026-08-14T20:36:43.523
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:36:43.521+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:43.523
- end: 2026-08-14T20:36:43.523
- duration_ms: 0
- entity_id: 201003916
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:43.535
- end: 2026-08-14T20:36:43.535
- duration_ms: 0
- parent_id: 201003916
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:43.536
- end: 2026-08-14T20:36:43.536
- duration_ms: 0
- entity_id: 201004841
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:43.544
- end: 2026-08-14T20:36:43.544
- duration_ms: 0
- parent_id: 201004841
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:36:43.544
- end: 2026-08-14T20:36:43.544
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:36:43.550
- end: 2026-08-14T20:36:43.550
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 3771
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 3
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
- duration_ms: 10769
- response_chars: 462
- response_hash: f9aa4c0001bcb1ed

## Final Output
- answer_chars: 462
- answer_hash: f9aa4c0001bcb1ed
- success: True

## Request Complete
- request_end: 2026-08-14T20:36:54.321
- request_duration_ms: 14418
- success: True
- final_source: generation

