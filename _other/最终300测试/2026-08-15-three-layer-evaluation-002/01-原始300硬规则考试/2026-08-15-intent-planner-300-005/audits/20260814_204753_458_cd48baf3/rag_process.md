# RAG Process

audit_id: 20260814_204753_458_cd48baf3
timestamp: 2026-08-14T20:47:53.458
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:47:53.458
- end: 2026-08-14T20:47:53.458
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:47:57.180
- end: 2026-08-14T20:47:57.180
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.93
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3722
- attempt_count: 1
- response_hash: 1960601b048337115512d6625428229ac711b45ca00ef1c3b4b04333aeaded0b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:47:57.198
- end: 2026-08-14T20:47:57.198
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: ad6cdc81a46632bb749ec6fb05dfefbba1fd84ffe9d48fecaedf76505984bccf
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:47:57.198
- end: 2026-08-14T20:47:57.198
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:47:57.198+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:47:57.200
- end: 2026-08-14T20:47:57.200
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:47:57.198+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:57.200
- end: 2026-08-14T20:47:57.200
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:57.208
- end: 2026-08-14T20:47:57.208
- duration_ms: 0
- parent_id: 201003939
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:57.208
- end: 2026-08-14T20:47:57.208
- duration_ms: 0
- entity_id: 201003977
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:57.217
- end: 2026-08-14T20:47:57.217
- duration_ms: 0
- parent_id: 201003977
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 3687
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
- duration_ms: 10862
- response_chars: 238
- response_hash: 6dc01c4daa73509e

## Final Output
- answer_chars: 238
- answer_hash: 6dc01c4daa73509e
- success: True

## Request Complete
- request_end: 2026-08-14T20:48:08.082
- request_duration_ms: 14623
- success: True
- final_source: generation

