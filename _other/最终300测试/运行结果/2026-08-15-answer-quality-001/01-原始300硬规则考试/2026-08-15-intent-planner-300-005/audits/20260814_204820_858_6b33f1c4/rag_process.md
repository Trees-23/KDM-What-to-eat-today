# RAG Process

audit_id: 20260814_204820_858_6b33f1c4
timestamp: 2026-08-14T20:48:20.859
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:48:20.859
- end: 2026-08-14T20:48:20.859
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:48:24.971
- end: 2026-08-14T20:48:24.971
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4112
- attempt_count: 1
- response_hash: 5348a0fbd41b950ad5e65003895e3a273dea1e2cf93caa2a0f93a936f195e13a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:48:24.982
- end: 2026-08-14T20:48:24.982
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 061d63e08a155c8e8ad9080759a4593cfae90ac673d60b1c0163f190d77f896d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:48:24.982
- end: 2026-08-14T20:48:24.982
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:48:24.982+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:48:24.984
- end: 2026-08-14T20:48:24.984
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:48:24.982+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:48:24.984
- end: 2026-08-14T20:48:24.984
- duration_ms: 0
- entity_id: 201003534
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:48:24.990
- end: 2026-08-14T20:48:24.990
- duration_ms: 0
- parent_id: 201003534
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:48:24.990
- end: 2026-08-14T20:48:24.990
- duration_ms: 0
- entity_id: 201004088
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:48:24.996
- end: 2026-08-14T20:48:24.996
- duration_ms: 0
- parent_id: 201004088
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:48:24.996
- end: 2026-08-14T20:48:24.996
- duration_ms: 0
- entity_id: 201004282
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:48:25.002
- end: 2026-08-14T20:48:25.002
- duration_ms: 0
- parent_id: 201004282
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:48:25.002
- end: 2026-08-14T20:48:25.002
- duration_ms: 0
- entity_id: 201004793
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:48:25.008
- end: 2026-08-14T20:48:25.008
- duration_ms: 0
- parent_id: 201004793
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:48:25.008
- end: 2026-08-14T20:48:25.008
- duration_ms: 0
- entity_id: 201005272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:48:25.014
- end: 2026-08-14T20:48:25.014
- duration_ms: 0
- parent_id: 201005272
- build_id: pds_51e5e228cb4a935de64e2b7a
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 12733
- response_chars: 302
- response_hash: 331f3cd96a706828

## Final Output
- answer_chars: 302
- answer_hash: 331f3cd96a706828
- success: True

## Request Complete
- request_end: 2026-08-14T20:48:37.749
- request_duration_ms: 16890
- success: True
- final_source: generation

