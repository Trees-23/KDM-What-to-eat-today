# RAG Process

audit_id: 20260814_151715_044_91f07447
timestamp: 2026-08-14T15:17:15.045
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:17:15.045
- end: 2026-08-14T15:17:15.045
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 19

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:17:21.077
- end: 2026-08-14T15:17:21.077
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.95
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6031
- attempt_count: 1
- response_hash: abca7791ac6db28db2d227819bc47706d6b6479a2e9afb0cd30dbd08069317e8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:17:21.080
- end: 2026-08-14T15:17:21.080
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 4d623f76970199f80fe6dc1add4b4dc45e848ac19c62e4a5c8bfdf44a6cc5624
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:17:21.080
- end: 2026-08-14T15:17:21.080
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:17:21.080+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:17:21.081
- end: 2026-08-14T15:17:21.081
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:17:21.080+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:17:21.082
- end: 2026-08-14T15:17:21.082
- duration_ms: 0
- entity_id: 201002876
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:17:21.083
- end: 2026-08-14T15:17:21.083
- duration_ms: 0
- recipe_id: 201002876
- step_id: 201002887

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:17:21.084
- end: 2026-08-14T15:17:21.084
- duration_ms: 0
- parent_id: 201002876
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201002887
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1970
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 7565
- response_chars: 139
- response_hash: a13aaf1dc7450e34

## Final Output
- answer_chars: 139
- answer_hash: a13aaf1dc7450e34
- success: True

## Request Complete
- request_end: 2026-08-14T15:17:28.651
- request_duration_ms: 13605
- success: True
- final_source: generation

