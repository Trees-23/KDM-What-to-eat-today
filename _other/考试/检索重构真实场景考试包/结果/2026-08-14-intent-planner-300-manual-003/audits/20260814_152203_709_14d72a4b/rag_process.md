# RAG Process

audit_id: 20260814_152203_709_14d72a4b
timestamp: 2026-08-14T15:22:03.709
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:22:03.710
- end: 2026-08-14T15:22:03.710
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 24

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:22:08.337
- end: 2026-08-14T15:22:08.337
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4627
- attempt_count: 1
- response_hash: c2d05d2b7e090651b92f472b17f69ea039b79f29bc9b2ab13ef1cc321a654b31
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:22:08.340
- end: 2026-08-14T15:22:08.340
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: a7b8763e355e86933f9b8c976f6603cc3b34187db7dfe9036c3a0654d6bc8546
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:22:08.340
- end: 2026-08-14T15:22:08.340
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:22:08.340+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:22:08.342
- end: 2026-08-14T15:22:08.342
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:22:08.340+00:00
- result_count: 2

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:22:08.342
- end: 2026-08-14T15:22:08.342
- duration_ms: 0
- entity_id: tipdoc_42a8d9f8ff95
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:22:08.348
- end: 2026-08-14T15:22:08.348
- duration_ms: 0
- parent_id: tipdoc_42a8d9f8ff95
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2453
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
- duration_ms: 24203
- response_chars: 1025
- response_hash: e0791e722a3a88ef

## Final Output
- answer_chars: 1025
- answer_hash: e0791e722a3a88ef
- success: True

## Request Complete
- request_end: 2026-08-14T15:22:32.553
- request_duration_ms: 28843
- success: True
- final_source: generation

