# RAG Process

audit_id: 20260814_200722_245_8965f579
timestamp: 2026-08-14T20:07:22.246
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:07:22.246
- end: 2026-08-14T20:07:22.246
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 22

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:07:27.659
- end: 2026-08-14T20:07:27.659
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5413
- attempt_count: 1
- response_hash: 936e45ced2a7b6f491db443fb231f982c9056dc67bc9ca863b4ce4c9f3c29e54
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:07:27.662
- end: 2026-08-14T20:07:27.662
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': [], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:07:27.662
- end: 2026-08-14T20:07:27.662
- duration_ms: 0
- entity_id: 201000386
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:07:27.669
- end: 2026-08-14T20:07:27.669
- duration_ms: 0
- parent_id: 201000386
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 1

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 870
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
- error_type: ConnectionError
- error_message: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- attempt: 1

## Event / generation_fallback
- stage: generation_fallback
- status: evidence_only
- start: 2026-08-14T20:07:35.753
- end: 2026-08-14T20:07:35.753
- duration_ms: 0
- reason: ConnectionError
- answer_chars: 33

## Final Output
- answer_chars: 33
- answer_hash: 307ca88da86a853e
- success: True
- source: generation_failed_fallback

## Request Complete
- request_end: 2026-08-14T20:07:35.754
- request_duration_ms: 13507
- success: True
- final_source: generation

