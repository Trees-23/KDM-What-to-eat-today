# RAG Process

audit_id: 20260813_222005_680_7e69e229
timestamp: 2026-08-13T22:20:05.681
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:20:05.681
- end: 2026-08-13T22:20:05.681
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:20:13.047
- end: 2026-08-13T22:20:13.047
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 8122
- attempt_count: 1
- response_hash: 98695cc737865c8540a9f75dbb23025b81a7b0e0281c331397ac15843a4c8769
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:20:13.053
- end: 2026-08-13T22:20:13.053
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 061d63e08a155c8e8ad9080759a4593cfae90ac673d60b1c0163f190d77f896d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:20:13.053
- end: 2026-08-13T22:20:13.053
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:20:13.053+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:20:13.057
- end: 2026-08-13T22:20:13.057
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:20:13.053+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:20:13.057
- end: 2026-08-13T22:20:13.057
- duration_ms: 0
- entity_id: 201003534
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:20:13.069
- end: 2026-08-13T22:20:13.069
- duration_ms: 0
- parent_id: 201003534
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:20:13.070
- end: 2026-08-13T22:20:13.070
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:20:13.077
- end: 2026-08-13T22:20:13.077
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:20:13.077
- end: 2026-08-13T22:20:13.077
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:20:13.085
- end: 2026-08-13T22:20:13.085
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:20:13.086
- end: 2026-08-13T22:20:13.086
- duration_ms: 0
- entity_id: 201004793
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:20:13.092
- end: 2026-08-13T22:20:13.092
- duration_ms: 0
- parent_id: 201004793
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:20:13.092
- end: 2026-08-13T22:20:13.092
- duration_ms: 0
- entity_id: 201005272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:20:13.111
- end: 2026-08-13T22:20:13.111
- duration_ms: 0
- parent_id: 201005272
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 7926
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
- duration_ms: 14679
- response_chars: 405
- response_hash: f88d02bc0928699a

## Final Output
- answer_chars: 405
- answer_hash: f88d02bc0928699a
- success: True

## Request Complete
- request_end: 2026-08-13T22:20:27.793
- request_duration_ms: 22111
- success: True
- final_source: generation

