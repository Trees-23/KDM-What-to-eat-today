# RAG Process

audit_id: 20260814_204619_231_b75e55e7
timestamp: 2026-08-14T20:46:19.231
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:46:19.231
- end: 2026-08-14T20:46:19.231
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:46:22.779
- end: 2026-08-14T20:46:22.779
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.92
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3547
- attempt_count: 1
- response_hash: d95b59344728bfb61d3264de9ae55d7f56e9ff5dc7b5a98307d86b0a85c80f45
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:46:22.788
- end: 2026-08-14T20:46:22.788
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 2554886548c3f4804defdb99b0ef8aba01b9c579ee9c456269e6589bd3118e05
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:46:22.788
- end: 2026-08-14T20:46:22.788
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:46:22.788+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:46:22.790
- end: 2026-08-14T20:46:22.790
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:46:22.788+00:00
- result_count: 12

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:46:22.790
- end: 2026-08-14T20:46:22.790
- duration_ms: 0
- entity_id: 201001698
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:46:22.796
- end: 2026-08-14T20:46:22.796
- duration_ms: 0
- parent_id: 201001698
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:46:22.796
- end: 2026-08-14T20:46:22.796
- duration_ms: 0
- entity_id: 201003296
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:46:22.802
- end: 2026-08-14T20:46:22.802
- duration_ms: 0
- parent_id: 201003296
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:46:22.802
- end: 2026-08-14T20:46:22.802
- duration_ms: 0
- entity_id: 201003336
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:46:22.809
- end: 2026-08-14T20:46:22.809
- duration_ms: 0
- parent_id: 201003336
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:46:22.809
- end: 2026-08-14T20:46:22.809
- duration_ms: 0
- entity_id: 201003902
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:46:22.816
- end: 2026-08-14T20:46:22.816
- duration_ms: 0
- parent_id: 201003902
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:46:22.816
- end: 2026-08-14T20:46:22.816
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:46:22.826
- end: 2026-08-14T20:46:22.826
- duration_ms: 0
- parent_id: 201003939
- build_id: pds_51e5e228cb4a935de64e2b7a
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 9067
- response_chars: 335
- response_hash: 54f0f0f379557d11

## Final Output
- answer_chars: 335
- answer_hash: 54f0f0f379557d11
- success: True

## Request Complete
- request_end: 2026-08-14T20:46:31.894
- request_duration_ms: 12663
- success: True
- final_source: generation

