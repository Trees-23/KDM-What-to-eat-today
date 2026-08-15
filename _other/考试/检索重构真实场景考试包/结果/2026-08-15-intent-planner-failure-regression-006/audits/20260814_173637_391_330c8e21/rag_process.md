# RAG Process

audit_id: 20260814_173637_391_330c8e21
timestamp: 2026-08-14T17:36:37.391
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T17:36:37.391
- end: 2026-08-14T17:36:37.391
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T17:36:42.360
- end: 2026-08-14T17:36:42.360
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['鲤鱼'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4968
- attempt_count: 1
- response_hash: 233de1dcfd542c9b374d198f38c2cf80e0a1182dbefe5be66076c1ee2dceb6e3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T17:36:42.382
- end: 2026-08-14T17:36:42.382
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 370144f87365ea87eb0e31aac0ddee6c40cf6a652df6dd418e5c3a8c3a2dbf20
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T17:36:42.382
- end: 2026-08-14T17:36:42.382
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:36:42.382+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T17:36:42.387
- end: 2026-08-14T17:36:42.387
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T17:36:42.382+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:36:42.387
- end: 2026-08-14T17:36:42.387
- duration_ms: 0
- entity_id: 201000127
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:36:42.398
- end: 2026-08-14T17:36:42.398
- duration_ms: 0
- parent_id: 201000127
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:36:42.399
- end: 2026-08-14T17:36:42.399
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:36:42.408
- end: 2026-08-14T17:36:42.408
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T17:36:42.408
- end: 2026-08-14T17:36:42.408
- duration_ms: 0
- entity_id: 201000453
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T17:36:42.415
- end: 2026-08-14T17:36:42.415
- duration_ms: 0
- parent_id: 201000453
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4850
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
- duration_ms: 13513
- response_chars: 491
- response_hash: 709bec8668810b60

## Final Output
- answer_chars: 491
- answer_hash: 709bec8668810b60
- success: True

## Request Complete
- request_end: 2026-08-14T17:36:55.929
- request_duration_ms: 18537
- success: True
- final_source: generation

