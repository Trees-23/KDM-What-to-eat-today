# RAG Process

audit_id: 20260813_221454_615_a3ee806e
timestamp: 2026-08-13T22:14:54.616
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:14:54.616
- end: 2026-08-13T22:14:54.616
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:14:58.030
- end: 2026-08-13T22:14:58.029
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3413
- attempt_count: 1
- response_hash: 0dde797f01db7ad9b2df6d2d3131bc3f06306117d7c3c0abf12d3df81a389ab9
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:14:58.036
- end: 2026-08-13T22:14:58.036
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: e71a3c5f96904496a022cbe7edbe063a605d5ae4d4fb43f5c87aad3d053b53ee
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:14:58.037
- end: 2026-08-13T22:14:58.037
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:14:58.037+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:14:58.041
- end: 2026-08-13T22:14:58.041
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T22:14:58.037+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:58.041
- end: 2026-08-13T22:14:58.041
- duration_ms: 0
- entity_id: 201002146
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:58.056
- end: 2026-08-13T22:14:58.056
- duration_ms: 0
- parent_id: 201002146
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:58.057
- end: 2026-08-13T22:14:58.057
- duration_ms: 0
- entity_id: 201003534
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:58.069
- end: 2026-08-13T22:14:58.069
- duration_ms: 0
- parent_id: 201003534
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:58.069
- end: 2026-08-13T22:14:58.069
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:58.076
- end: 2026-08-13T22:14:58.076
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:58.076
- end: 2026-08-13T22:14:58.076
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:58.082
- end: 2026-08-13T22:14:58.082
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:58.083
- end: 2026-08-13T22:14:58.083
- duration_ms: 0
- entity_id: 201004793
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:58.090
- end: 2026-08-13T22:14:58.090
- duration_ms: 0
- parent_id: 201004793
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:58.090
- end: 2026-08-13T22:14:58.090
- duration_ms: 0
- entity_id: 201004885
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:58.100
- end: 2026-08-13T22:14:58.100
- duration_ms: 0
- parent_id: 201004885
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:14:58.100
- end: 2026-08-13T22:14:58.100
- duration_ms: 0
- entity_id: 201005272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:14:58.112
- end: 2026-08-13T22:14:58.112
- duration_ms: 0
- parent_id: 201005272
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 4557
- response_chars: 163
- response_hash: 13071586d79cc4ac

## Final Output
- answer_chars: 163
- answer_hash: 13071586d79cc4ac
- success: True

## Request Complete
- request_end: 2026-08-13T22:15:02.673
- request_duration_ms: 8056
- success: True
- final_source: generation

