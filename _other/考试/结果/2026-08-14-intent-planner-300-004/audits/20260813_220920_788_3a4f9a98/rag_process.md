# RAG Process

audit_id: 20260813_220920_788_3a4f9a98
timestamp: 2026-08-13T22:09:20.788
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:09:20.789
- end: 2026-08-13T22:09:20.789
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:09:24.386
- end: 2026-08-13T22:09:24.386
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3596
- attempt_count: 1
- response_hash: ce17ecdc2b5ec9449d43677ffd294072d5c9c77771014d38a65d3d20f1a57fdf
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:09:24.392
- end: 2026-08-13T22:09:24.392
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 24214433c22fcf516e5bea29da501117a5004d68231068bd66ebe14e12d2bc9c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:09:24.393
- end: 2026-08-13T22:09:24.393
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:09:24.393+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:09:24.397
- end: 2026-08-13T22:09:24.397
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:09:24.393+00:00
- result_count: 10

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:09:24.398
- end: 2026-08-13T22:09:24.398
- duration_ms: 0
- entity_id: tipdoc_a9973e4a7693
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:09:24.414
- end: 2026-08-13T22:09:24.414
- duration_ms: 0
- parent_id: tipdoc_a9973e4a7693
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 15282
- response_chars: 802
- response_hash: 3bda09362a2e86c4

## Final Output
- answer_chars: 802
- answer_hash: 3bda09362a2e86c4
- success: True

## Request Complete
- request_end: 2026-08-13T22:09:39.698
- request_duration_ms: 18909
- success: True
- final_source: generation

