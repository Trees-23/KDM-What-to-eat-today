# RAG Process

audit_id: 20260814_204446_323_55a0d781
timestamp: 2026-08-14T20:44:46.323
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:44:46.324
- end: 2026-08-14T20:44:46.324
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:44:50.490
- end: 2026-08-14T20:44:50.490
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4166
- attempt_count: 1
- response_hash: ee748e01f3ca9ff7e3c17ab17bbd3aa2d70e6b1131af7b79aefd8b753e94107b
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:44:50.506
- end: 2026-08-14T20:44:50.506
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 9cb6f2919dade2c3198014703353b0050855fc4f908ffb68ede50d59ce152d1e
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:44:50.506
- end: 2026-08-14T20:44:50.506
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:44:50.506+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:44:50.509
- end: 2026-08-14T20:44:50.509
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:44:50.506+00:00
- result_count: 14

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:50.510
- end: 2026-08-14T20:44:50.510
- duration_ms: 0
- entity_id: 201003459
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:50.521
- end: 2026-08-14T20:44:50.521
- duration_ms: 0
- parent_id: 201003459
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:50.521
- end: 2026-08-14T20:44:50.521
- duration_ms: 0
- entity_id: 201004898
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:50.530
- end: 2026-08-14T20:44:50.530
- duration_ms: 0
- parent_id: 201004898
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:50.530
- end: 2026-08-14T20:44:50.530
- duration_ms: 0
- entity_id: 201005001
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:50.536
- end: 2026-08-14T20:44:50.536
- duration_ms: 0
- parent_id: 201005001
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:50.536
- end: 2026-08-14T20:44:50.536
- duration_ms: 0
- entity_id: 201005092
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:50.542
- end: 2026-08-14T20:44:50.542
- duration_ms: 0
- parent_id: 201005092
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:50.543
- end: 2026-08-14T20:44:50.543
- duration_ms: 0
- entity_id: 201005146
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:50.549
- end: 2026-08-14T20:44:50.549
- duration_ms: 0
- parent_id: 201005146
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:44:50.549
- end: 2026-08-14T20:44:50.549
- duration_ms: 0
- entity_id: 201005492
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:44:50.555
- end: 2026-08-14T20:44:50.555
- duration_ms: 0
- parent_id: 201005492
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 11141
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 6
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
- duration_ms: 18914
- response_chars: 502
- response_hash: 8e1b3620060263d5

## Final Output
- answer_chars: 502
- answer_hash: 8e1b3620060263d5
- success: True

## Request Complete
- request_end: 2026-08-14T20:45:09.471
- request_duration_ms: 23147
- success: True
- final_source: generation

