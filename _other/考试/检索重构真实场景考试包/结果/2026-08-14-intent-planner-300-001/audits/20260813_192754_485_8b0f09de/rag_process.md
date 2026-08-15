# RAG Process

audit_id: 20260813_192754_485_8b0f09de
timestamp: 2026-08-13T19:27:54.486
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:27:54.486
- end: 2026-08-13T19:27:54.486
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:27:57.916
- end: 2026-08-13T19:27:57.916
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3430
- attempt_count: 1
- response_hash: 7dfe4e45c323093f204809da62f7334579cbe37b4d7cc83e4a96fd2b59a9dc6d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:27:57.921
- end: 2026-08-13T19:27:57.921
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: dc18a1b1340818bc8ba14689731d3932a55ed07d2d3f03a8f230b38a6770e0ff
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:27:57.921
- end: 2026-08-13T19:27:57.921
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:27:57.921+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:27:57.923
- end: 2026-08-13T19:27:57.923
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T19:27:57.921+00:00
- result_count: 10

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.924
- end: 2026-08-13T19:27:57.924
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.931
- end: 2026-08-13T19:27:57.931
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.931
- end: 2026-08-13T19:27:57.931
- duration_ms: 0
- entity_id: 201003224
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.938
- end: 2026-08-13T19:27:57.938
- duration_ms: 0
- parent_id: 201003224
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.938
- end: 2026-08-13T19:27:57.938
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.944
- end: 2026-08-13T19:27:57.944
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.944
- end: 2026-08-13T19:27:57.944
- duration_ms: 0
- entity_id: 201004746
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.950
- end: 2026-08-13T19:27:57.950
- duration_ms: 0
- parent_id: 201004746
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.951
- end: 2026-08-13T19:27:57.951
- duration_ms: 0
- entity_id: 201005049
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.966
- end: 2026-08-13T19:27:57.966
- duration_ms: 0
- parent_id: 201005049
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.966
- end: 2026-08-13T19:27:57.966
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.972
- end: 2026-08-13T19:27:57.972
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.972
- end: 2026-08-13T19:27:57.972
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.978
- end: 2026-08-13T19:27:57.978
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.978
- end: 2026-08-13T19:27:57.978
- duration_ms: 0
- entity_id: 201005528
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.984
- end: 2026-08-13T19:27:57.984
- duration_ms: 0
- parent_id: 201005528
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.984
- end: 2026-08-13T19:27:57.984
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.991
- end: 2026-08-13T19:27:57.991
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:27:57.991
- end: 2026-08-13T19:27:57.991
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:27:57.997
- end: 2026-08-13T19:27:57.997
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 12355
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 10
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
- duration_ms: 11907
- response_chars: 421
- response_hash: 7b46324d511e3523

## Final Output
- answer_chars: 421
- answer_hash: 7b46324d511e3523
- success: True

## Request Complete
- request_end: 2026-08-13T19:28:09.906
- request_duration_ms: 15420
- success: True
- final_source: generation

