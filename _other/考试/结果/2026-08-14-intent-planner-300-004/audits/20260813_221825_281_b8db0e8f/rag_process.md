# RAG Process

audit_id: 20260813_221825_281_b8db0e8f
timestamp: 2026-08-13T22:18:25.282
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:18:25.282
- end: 2026-08-13T22:18:25.282
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:18:30.036
- end: 2026-08-13T22:18:30.036
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4754
- attempt_count: 1
- response_hash: ac0d26e34c69f42d4b945c9eb81483fa43c9747e8fc6b23c96818c465366ae85
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:18:30.039
- end: 2026-08-13T22:18:30.039
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 2554886548c3f4804defdb99b0ef8aba01b9c579ee9c456269e6589bd3118e05
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:18:30.040
- end: 2026-08-13T22:18:30.040
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:18:30.040+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:18:30.042
- end: 2026-08-13T22:18:30.042
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:18:30.040+00:00
- result_count: 12

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:18:30.042
- end: 2026-08-13T22:18:30.042
- duration_ms: 0
- entity_id: 201001698
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:18:30.048
- end: 2026-08-13T22:18:30.048
- duration_ms: 0
- parent_id: 201001698
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:18:30.048
- end: 2026-08-13T22:18:30.048
- duration_ms: 0
- entity_id: 201003296
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:18:30.057
- end: 2026-08-13T22:18:30.057
- duration_ms: 0
- parent_id: 201003296
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:18:30.057
- end: 2026-08-13T22:18:30.057
- duration_ms: 0
- entity_id: 201003336
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:18:30.065
- end: 2026-08-13T22:18:30.065
- duration_ms: 0
- parent_id: 201003336
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:18:30.065
- end: 2026-08-13T22:18:30.065
- duration_ms: 0
- entity_id: 201003902
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:18:30.073
- end: 2026-08-13T22:18:30.073
- duration_ms: 0
- parent_id: 201003902
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:18:30.073
- end: 2026-08-13T22:18:30.073
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:18:30.079
- end: 2026-08-13T22:18:30.079
- duration_ms: 0
- parent_id: 201003939
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 9164
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
- duration_ms: 7242
- response_chars: 287
- response_hash: 894a44dda9d3b6a3

## Final Output
- answer_chars: 287
- answer_hash: 894a44dda9d3b6a3
- success: True

## Request Complete
- request_end: 2026-08-13T22:18:37.323
- request_duration_ms: 12040
- success: True
- final_source: generation

