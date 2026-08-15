# RAG Process

audit_id: 20260814_150452_156_f2e9a161
timestamp: 2026-08-14T15:04:52.156
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:04:52.157
- end: 2026-08-14T15:04:52.157
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 26

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:04:59.884
- end: 2026-08-14T15:04:59.884
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['葱', '姜', '黑鳕鱼'], 'preferences': [], 'meal_context': [], 'tools': ['MICROWAVE'], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7727
- attempt_count: 1
- response_hash: b29f42fde2b74febb2b8bef307b0981ad46f9abbfa8a3de0b87a5de9d68a7734
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:04:59.891
- end: 2026-08-14T15:04:59.890
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['MICROWAVE'], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:04:59.891
- end: 2026-08-14T15:04:59.891
- duration_ms: 0
- entity_id: 201000023
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:04:59.904
- end: 2026-08-14T15:04:59.904
- duration_ms: 0
- parent_id: 201000023
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1369
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

## Errors
- stage: generation_non_stream
- status: error
- error_type: SSLError
- error_message: HTTPSConnectionPool(host='downstream.jbbtoken.cn', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1016)')))
- attempt: 1

## Generation Non-Stream
- status: success
- duration_ms: 19449
- response_chars: 747
- response_hash: 5e17054d5cc52ffb

## Final Output
- answer_chars: 747
- answer_hash: 5e17054d5cc52ffb
- success: True

## Request Complete
- request_end: 2026-08-14T15:05:19.356
- request_duration_ms: 27199
- success: True
- final_source: generation

