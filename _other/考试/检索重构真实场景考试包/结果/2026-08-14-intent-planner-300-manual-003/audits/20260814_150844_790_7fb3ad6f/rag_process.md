# RAG Process

audit_id: 20260814_150844_790_7fb3ad6f
timestamp: 2026-08-14T15:08:44.791
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:08:44.791
- end: 2026-08-14T15:08:44.791
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 26

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:08:48.987
- end: 2026-08-14T15:08:48.987
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.92
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STIR_FRY'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4196
- attempt_count: 1
- response_hash: 7a3e48cb4994351fb6ea68b4ddb6ad7a3e22ae323ed9868c253b45efd4169d38
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:08:48.994
- end: 2026-08-14T15:08:48.994
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['STIR_FRY'], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:08:48.994
- end: 2026-08-14T15:08:48.994
- duration_ms: 0
- entity_id: 201004478
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:08:49.008
- end: 2026-08-14T15:08:49.008
- duration_ms: 0
- parent_id: 201004478
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1989
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
- duration_ms: 24823
- response_chars: 1125
- response_hash: 4b7f3aeea83c88c5

## Final Output
- answer_chars: 1125
- answer_hash: 4b7f3aeea83c88c5
- success: True

## Request Complete
- request_end: 2026-08-14T15:09:13.833
- request_duration_ms: 29042
- success: True
- final_source: generation

