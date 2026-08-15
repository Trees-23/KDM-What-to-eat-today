# RAG Process

audit_id: 20260814_152503_367_4fe281e4
timestamp: 2026-08-14T15:25:03.367
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:25:03.368
- end: 2026-08-14T15:25:03.368
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 25

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:25:07.426
- end: 2026-08-14T15:25:07.426
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4058
- attempt_count: 1
- response_hash: d1fc39bfe7161267141b0c3e06a14d0799f134e4eca11ebf638407e29bf786f6
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:25:07.431
- end: 2026-08-14T15:25:07.431
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 8eaae08d41838c3cdaa971674310f2e67413ef1a1e3969d6ddcec54b6f215389
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:25:07.431
- end: 2026-08-14T15:25:07.431
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:25:07.431+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:25:07.435
- end: 2026-08-14T15:25:07.435
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:25:07.431+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:25:07.435
- end: 2026-08-14T15:25:07.435
- duration_ms: 0
- entity_id: tipdoc_5e4d6d67fc39
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:25:07.448
- end: 2026-08-14T15:25:07.448
- duration_ms: 0
- parent_id: tipdoc_5e4d6d67fc39
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 10

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 3729
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
- duration_ms: 18949
- response_chars: 1032
- response_hash: f54ca34378090693

## Final Output
- answer_chars: 1032
- answer_hash: f54ca34378090693
- success: True

## Request Complete
- request_end: 2026-08-14T15:25:26.399
- request_duration_ms: 23031
- success: True
- final_source: generation

