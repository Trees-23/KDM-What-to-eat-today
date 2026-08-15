# RAG Process

audit_id: 20260814_204101_575_c8cbdb5c
timestamp: 2026-08-14T20:41:01.576
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:41:01.576
- end: 2026-08-14T20:41:01.576
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:41:05.939
- end: 2026-08-14T20:41:05.939
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['花菜'], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4363
- attempt_count: 1
- response_hash: 829cd3d0a60d03463a517afaccc6637f1ecb950938ea4888b260db33dcac6332
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:41:05.949
- end: 2026-08-14T20:41:05.949
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 97b08cfe77feae6bbfc35a14cee179b916ea17421914ab40d814ace6d4810855
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:41:05.949
- end: 2026-08-14T20:41:05.949
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:41:05.949+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:41:05.953
- end: 2026-08-14T20:41:05.953
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T20:41:05.949+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:05.953
- end: 2026-08-14T20:41:05.953
- duration_ms: 0
- entity_id: 201004974
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:05.966
- end: 2026-08-14T20:41:05.966
- duration_ms: 0
- parent_id: 201004974
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:41:05.966
- end: 2026-08-14T20:41:05.966
- duration_ms: 0
- entity_id: 201005383
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:41:05.974
- end: 2026-08-14T20:41:05.974
- duration_ms: 0
- parent_id: 201005383
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2832
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 2
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
- duration_ms: 4857
- response_chars: 91
- response_hash: 367cfe270594f8ff

## Final Output
- answer_chars: 91
- answer_hash: 367cfe270594f8ff
- success: True

## Request Complete
- request_end: 2026-08-14T20:41:10.833
- request_duration_ms: 9257
- success: True
- final_source: generation

