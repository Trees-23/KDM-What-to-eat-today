# RAG Process

audit_id: 20260814_200631_459_f41881ee
timestamp: 2026-08-14T20:06:31.459
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:06:31.460
- end: 2026-08-14T20:06:31.460
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 24

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:06:36.814
- end: 2026-08-14T20:06:36.814
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STEW'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5354
- attempt_count: 1
- response_hash: 70c4e32ce02c1bea043af423efa528834f3c85bcd888781bd7d6297ddf32fab3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:06:36.827
- end: 2026-08-14T20:06:36.827
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['STEW'], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:06:36.828
- end: 2026-08-14T20:06:36.828
- duration_ms: 0
- entity_id: 201000472
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:06:36.840
- end: 2026-08-14T20:06:36.840
- duration_ms: 0
- parent_id: 201000472
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1362
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
- timeout: 45.0
- max_retries: 0

## Errors
- stage: generation_non_stream
- status: error
- error_type: ReadTimeout
- error_message: HTTPSConnectionPool(host='downstream.jbbtoken.cn', port=443): Read timed out. (read timeout=45.0)
- attempt: 1

## Event / generation_fallback
- stage: generation_fallback
- status: evidence_only
- start: 2026-08-14T20:07:22.244
- end: 2026-08-14T20:07:22.244
- duration_ms: 0
- reason: ReadTimeout
- answer_chars: 35

## Final Output
- answer_chars: 35
- answer_hash: 444bf31bc9827d28
- success: True
- source: generation_failed_fallback

## Request Complete
- request_end: 2026-08-14T20:07:22.244
- request_duration_ms: 50784
- success: True
- final_source: generation

