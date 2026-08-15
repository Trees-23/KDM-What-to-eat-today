# RAG Process

audit_id: 20260814_202437_037_0d2be321
timestamp: 2026-08-14T20:24:37.037
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:24:37.038
- end: 2026-08-14T20:24:37.037
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 24

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:24:42.097
- end: 2026-08-14T20:24:42.097
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5060
- attempt_count: 1
- response_hash: 92513508561180f2e7d0bd1dc086a74c460772477fa880590d9abe30f742d1a2
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:24:42.111
- end: 2026-08-14T20:24:42.111
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 24214433c22fcf516e5bea29da501117a5004d68231068bd66ebe14e12d2bc9c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:24:42.112
- end: 2026-08-14T20:24:42.112
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:24:42.112+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:24:42.116
- end: 2026-08-14T20:24:42.116
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:24:42.112+00:00
- result_count: 10

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:24:42.117
- end: 2026-08-14T20:24:42.117
- duration_ms: 0
- entity_id: tipdoc_a9973e4a7693
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:24:42.130
- end: 2026-08-14T20:24:42.130
- duration_ms: 0
- parent_id: tipdoc_a9973e4a7693
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 13

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 7157
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

## Generation Non-Stream
- status: success
- duration_ms: 23563
- response_chars: 1267
- response_hash: b44edf38fc196b7e

## Final Output
- answer_chars: 1267
- answer_hash: b44edf38fc196b7e
- success: True

## Request Complete
- request_end: 2026-08-14T20:25:05.695
- request_duration_ms: 28657
- success: True
- final_source: generation

