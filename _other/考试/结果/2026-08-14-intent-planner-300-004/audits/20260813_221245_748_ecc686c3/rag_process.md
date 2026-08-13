# RAG Process

audit_id: 20260813_221245_748_ecc686c3
timestamp: 2026-08-13T22:12:45.748
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:12:45.749
- end: 2026-08-13T22:12:45.749
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:12:49.607
- end: 2026-08-13T22:12:49.607
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3858
- attempt_count: 1
- response_hash: 197dd49e090f07c932d38915ee381cc2a1efb7647a07b0f8ace94d698b5c5b37
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:12:49.613
- end: 2026-08-13T22:12:49.613
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 110a18a4c5639d69a5e6c3191e82653acaaf393d8241c48c80442ed42c462a8d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:12:49.613
- end: 2026-08-13T22:12:49.613
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:12:49.613+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:12:49.617
- end: 2026-08-13T22:12:49.617
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:12:49.613+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:49.617
- end: 2026-08-13T22:12:49.617
- duration_ms: 0
- entity_id: 201001698
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:49.630
- end: 2026-08-13T22:12:49.630
- duration_ms: 0
- parent_id: 201001698
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:49.631
- end: 2026-08-13T22:12:49.631
- duration_ms: 0
- entity_id: 201002937
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:49.640
- end: 2026-08-13T22:12:49.640
- duration_ms: 0
- parent_id: 201002937
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:49.641
- end: 2026-08-13T22:12:49.641
- duration_ms: 0
- entity_id: 201003296
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:49.656
- end: 2026-08-13T22:12:49.656
- duration_ms: 0
- parent_id: 201003296
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:49.656
- end: 2026-08-13T22:12:49.656
- duration_ms: 0
- entity_id: 201003336
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:49.663
- end: 2026-08-13T22:12:49.663
- duration_ms: 0
- parent_id: 201003336
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:49.663
- end: 2026-08-13T22:12:49.663
- duration_ms: 0
- entity_id: 201003873
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:49.672
- end: 2026-08-13T22:12:49.672
- duration_ms: 0
- parent_id: 201003873
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:49.672
- end: 2026-08-13T22:12:49.672
- duration_ms: 0
- entity_id: 201003902
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:49.680
- end: 2026-08-13T22:12:49.680
- duration_ms: 0
- parent_id: 201003902
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:12:49.680
- end: 2026-08-13T22:12:49.680
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:12:49.687
- end: 2026-08-13T22:12:49.687
- duration_ms: 0
- parent_id: 201003939
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 11537
- response_chars: 567
- response_hash: 3c2e39c328ad2540

## Final Output
- answer_chars: 567
- answer_hash: 3c2e39c328ad2540
- success: True

## Request Complete
- request_end: 2026-08-13T22:13:01.226
- request_duration_ms: 15477
- success: True
- final_source: generation

