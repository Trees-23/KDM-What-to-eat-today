# RAG Process

audit_id: 20260814_153205_515_fa3b41e1
timestamp: 2026-08-14T15:32:05.516
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:32:05.517
- end: 2026-08-14T15:32:05.517
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:32:10.885
- end: 2026-08-14T15:32:10.885
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5368
- attempt_count: 1
- response_hash: baea26a8bba18839ea2c0fec328de50945282c3367dcc73307f305c7e41ba52d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:32:10.890
- end: 2026-08-14T15:32:10.890
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: cd75743034fe11902cbec7152aade315d2e17d52b10a169960ef236e5547b0d8
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:32:10.890
- end: 2026-08-14T15:32:10.890
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:32:10.890+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:32:10.895
- end: 2026-08-14T15:32:10.895
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T15:32:10.890+00:00
- result_count: 9

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:32:10.895
- end: 2026-08-14T15:32:10.895
- duration_ms: 0
- entity_id: tipdoc_e5959b9d0464
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:32:10.904
- end: 2026-08-14T15:32:10.904
- duration_ms: 0
- parent_id: tipdoc_e5959b9d0464
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 19

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 7905
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
- duration_ms: 24048
- response_chars: 1035
- response_hash: bba174570dfaa15d

## Final Output
- answer_chars: 1035
- answer_hash: bba174570dfaa15d
- success: True

## Request Complete
- request_end: 2026-08-14T15:32:34.955
- request_duration_ms: 29438
- success: True
- final_source: generation

