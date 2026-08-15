# RAG Process

audit_id: 20260813_221403_230_30c3b04a
timestamp: 2026-08-13T22:14:03.230
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:14:03.230
- end: 2026-08-13T22:14:03.230
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:14:06.934
- end: 2026-08-13T22:14:06.934
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['米饭'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3704
- attempt_count: 1
- response_hash: 58aedb6784fdbd9b4a61305ca525e7d531097715832fbbecdfbb1247feef5ef6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:14:06.942
- end: 2026-08-13T22:14:06.942
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 9aedaa8d2d7664e5c2bd13246518a7450b6d35d3b197ac0eb2e609255f2d5578
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:14:06.942
- end: 2026-08-13T22:14:06.942
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:14:06.942+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:14:06.947
- end: 2026-08-13T22:14:06.947
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:14:06.942+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:06.948
- end: 2026-08-13T22:14:06.948
- duration_ms: 0
- entity_id: 201002282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:06.968
- end: 2026-08-13T22:14:06.968
- duration_ms: 0
- parent_id: 201002282
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:06.969
- end: 2026-08-13T22:14:06.969
- duration_ms: 0
- entity_id: 201004196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:06.979
- end: 2026-08-13T22:14:06.979
- duration_ms: 0
- parent_id: 201004196
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:06.979
- end: 2026-08-13T22:14:06.979
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:06.987
- end: 2026-08-13T22:14:06.987
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:06.987
- end: 2026-08-13T22:14:06.987
- duration_ms: 0
- entity_id: 201004588
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:06.995
- end: 2026-08-13T22:14:06.995
- duration_ms: 0
- parent_id: 201004588
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:06.995
- end: 2026-08-13T22:14:06.995
- duration_ms: 0
- entity_id: 201004801
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:07.002
- end: 2026-08-13T22:14:07.002
- duration_ms: 0
- parent_id: 201004801
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 6469
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 5
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
- duration_ms: 10722
- response_chars: 332
- response_hash: f7bedd699d3fb835

## Final Output
- answer_chars: 332
- answer_hash: f7bedd699d3fb835
- success: True

## Request Complete
- request_end: 2026-08-13T22:14:17.726
- request_duration_ms: 14495
- success: True
- final_source: generation

