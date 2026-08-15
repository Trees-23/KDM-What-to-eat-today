# RAG Process

audit_id: 20260813_221111_365_a353cf99
timestamp: 2026-08-13T22:11:11.365
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:11:11.365
- end: 2026-08-13T22:11:11.365
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:11:14.605
- end: 2026-08-13T22:11:14.605
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['豆腐'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3239
- attempt_count: 1
- response_hash: a3a86f65b320a6d10931f8dc9d41529ebbbfb38b8a12261ccd435c5c733e0b7d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:11:14.610
- end: 2026-08-13T22:11:14.610
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 890120a2c84ebcc96303fb60436e87ae67dcaf7fe8cdee30bdb0c5058265a249
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:11:14.611
- end: 2026-08-13T22:11:14.611
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:11:14.611+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:11:14.614
- end: 2026-08-13T22:11:14.614
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:11:14.611+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:14.615
- end: 2026-08-13T22:11:14.615
- duration_ms: 0
- entity_id: 201003916
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:14.628
- end: 2026-08-13T22:11:14.628
- duration_ms: 0
- parent_id: 201003916
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:14.629
- end: 2026-08-13T22:11:14.629
- duration_ms: 0
- entity_id: 201004841
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:14.644
- end: 2026-08-13T22:11:14.644
- duration_ms: 0
- parent_id: 201004841
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:11:14.644
- end: 2026-08-13T22:11:14.644
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:11:14.659
- end: 2026-08-13T22:11:14.659
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 11129
- response_chars: 473
- response_hash: 7972f993fb044c3f

## Final Output
- answer_chars: 473
- answer_hash: 7972f993fb044c3f
- success: True

## Request Complete
- request_end: 2026-08-13T22:11:25.790
- request_duration_ms: 14425
- success: True
- final_source: generation

