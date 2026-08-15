# RAG Process

audit_id: 20260814_152926_786_8d54764d
timestamp: 2026-08-14T15:29:26.786
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:29:26.786
- end: 2026-08-14T15:29:26.786
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 23

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:29:31.459
- end: 2026-08-14T15:29:31.459
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4673
- attempt_count: 1
- response_hash: 4ea85e27c8acab4dee0605d6f4d983cbecb4a851feb50e568d78a3da9ce4ec4c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:29:31.465
- end: 2026-08-14T15:29:31.465
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 1247acfdd5c21718a3bb3abfef8cb6e3482e5292b93e7e1e376700ad22c6ec3c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:29:31.466
- end: 2026-08-14T15:29:31.466
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:29:31.466+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:29:31.472
- end: 2026-08-14T15:29:31.472
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:29:31.466+00:00
- result_count: 8

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:29:31.472
- end: 2026-08-14T15:29:31.472
- duration_ms: 0
- entity_id: tipdoc_7ce59b628288
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:29:31.491
- end: 2026-08-14T15:29:31.491
- duration_ms: 0
- parent_id: tipdoc_7ce59b628288
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 17

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 5622
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
- duration_ms: 35546
- response_chars: 1837
- response_hash: c13e6c4b64e2a19d

## Final Output
- answer_chars: 1837
- answer_hash: c13e6c4b64e2a19d
- success: True

## Request Complete
- request_end: 2026-08-14T15:30:07.039
- request_duration_ms: 40252
- success: True
- final_source: generation

