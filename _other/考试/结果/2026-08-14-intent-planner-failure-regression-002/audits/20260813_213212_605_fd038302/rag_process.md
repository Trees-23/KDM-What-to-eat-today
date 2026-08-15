# RAG Process

audit_id: 20260813_213212_605_fd038302
timestamp: 2026-08-13T21:32:12.607
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:32:12.607
- end: 2026-08-13T21:32:12.607
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:32:16.218
- end: 2026-08-13T21:32:16.218
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3611
- attempt_count: 1
- response_hash: 141eae2e48dffd4a3f3c48626c3247bbbdde7c1b7b3ac44d4171c4f9fea7b0d2
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:32:16.227
- end: 2026-08-13T21:32:16.227
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: fbd9c9128cfdafcaf9e345ddff7a7d1f342259740444d877874ba00794ec81cf
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:32:16.227
- end: 2026-08-13T21:32:16.227
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:32:16.227+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:32:16.242
- end: 2026-08-13T21:32:16.242
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:32:16.227+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:32:16.243
- end: 2026-08-13T21:32:16.243
- duration_ms: 0
- entity_id: 201003873
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T21:32:16.255
- end: 2026-08-13T21:32:16.255
- duration_ms: 0
- recipe_id: 201003873
- step_id: 201003881

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:32:16.260
- end: 2026-08-13T21:32:16.260
- duration_ms: 0
- parent_id: 201003873
- build_id: pds_39326c459e9484b27c7e43c6
- anchor_id: 201003881
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1378
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 1
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
- duration_ms: 6110
- response_chars: 118
- response_hash: 75c270c6adcad366

## Final Output
- answer_chars: 118
- answer_hash: 75c270c6adcad366
- success: True

## Request Complete
- request_end: 2026-08-13T21:32:22.372
- request_duration_ms: 9764
- success: True
- final_source: generation

