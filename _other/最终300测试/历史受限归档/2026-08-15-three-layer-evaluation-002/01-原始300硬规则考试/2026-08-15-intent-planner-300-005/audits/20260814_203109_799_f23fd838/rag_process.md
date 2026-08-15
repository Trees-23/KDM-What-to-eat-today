# RAG Process

audit_id: 20260814_203109_799_f23fd838
timestamp: 2026-08-14T20:31:09.799
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:31:09.799
- end: 2026-08-14T20:31:09.799
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 24

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:31:13.365
- end: 2026-08-14T20:31:13.365
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3565
- attempt_count: 1
- response_hash: 5e425326e63338de69f80c5c4731675062df14d304bc5d04da84d249a10a6103
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:31:13.368
- end: 2026-08-14T20:31:13.368
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: a471ede014bfb5358f39ba92efc45021480b0cd81cd34bcd7a339d53f82ec453
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:31:13.369
- end: 2026-08-14T20:31:13.369
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:31:13.369+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:31:13.372
- end: 2026-08-14T20:31:13.372
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:31:13.369+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:31:13.372
- end: 2026-08-14T20:31:13.372
- duration_ms: 0
- entity_id: tipdoc_0f28e4976868
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:31:13.386
- end: 2026-08-14T20:31:13.386
- duration_ms: 0
- parent_id: tipdoc_0f28e4976868
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 11

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 3811
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
- duration_ms: 24569
- response_chars: 1356
- response_hash: 15d4da7735eb4f69

## Final Output
- answer_chars: 1356
- answer_hash: 15d4da7735eb4f69
- success: True

## Request Complete
- request_end: 2026-08-14T20:31:37.958
- request_duration_ms: 28158
- success: True
- final_source: generation

