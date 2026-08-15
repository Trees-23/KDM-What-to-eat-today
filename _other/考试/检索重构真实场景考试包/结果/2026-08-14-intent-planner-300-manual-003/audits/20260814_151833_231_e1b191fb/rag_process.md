# RAG Process

audit_id: 20260814_151833_231_e1b191fb
timestamp: 2026-08-14T15:18:33.231
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:18:33.232
- end: 2026-08-14T15:18:33.232
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:18:41.331
- end: 2026-08-14T15:18:41.331
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 8099
- attempt_count: 1
- response_hash: d239209b0d0fd4158ce2e05b7763c93aecb4b8dc2dc4f15d4138c0ed4c30635d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:18:41.334
- end: 2026-08-14T15:18:41.334
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: fccf7dd3537b4ea206a3a9056457807cabb513ca6476f46c620a17fe6741f042
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:18:41.334
- end: 2026-08-14T15:18:41.334
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:18:41.334+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:18:41.336
- end: 2026-08-14T15:18:41.336
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:18:41.334+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:18:41.336
- end: 2026-08-14T15:18:41.336
- duration_ms: 0
- entity_id: 201004260
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:18:41.337
- end: 2026-08-14T15:18:41.337
- duration_ms: 0
- recipe_id: 201004260
- step_id: 201004272

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:18:41.339
- end: 2026-08-14T15:18:41.339
- duration_ms: 0
- parent_id: 201004260
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201004272
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1800
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
- duration_ms: 6607
- response_chars: 134
- response_hash: 853bc9f6f091779a

## Final Output
- answer_chars: 134
- answer_hash: 853bc9f6f091779a
- success: True

## Request Complete
- request_end: 2026-08-14T15:18:47.947
- request_duration_ms: 14715
- success: True
- final_source: generation

