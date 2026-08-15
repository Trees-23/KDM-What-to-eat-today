# RAG Process

audit_id: 20260814_202639_174_4c321b8e
timestamp: 2026-08-14T20:26:39.175
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:26:39.175
- end: 2026-08-14T20:26:39.175
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:26:43.054
- end: 2026-08-14T20:26:43.054
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3879
- attempt_count: 1
- response_hash: 4ef4c18bcd2602a29df1903e42a4a6ac0db77cb0472cb2a3280be9e1c018e913
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:26:43.058
- end: 2026-08-14T20:26:43.058
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 9b104414f92359e9bffc5a64aef57f82a7372507ea6426ef0cca2c8a9ec9a060
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:26:43.058
- end: 2026-08-14T20:26:43.058
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:26:43.058+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:26:43.065
- end: 2026-08-14T20:26:43.065
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-14T20:26:43.058+00:00
- result_count: 25

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:26:43.065
- end: 2026-08-14T20:26:43.065
- duration_ms: 0
- entity_id: tipdoc_fd7f557c37a7
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:26:43.078
- end: 2026-08-14T20:26:43.078
- duration_ms: 0
- parent_id: tipdoc_fd7f557c37a7
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 30

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 11149
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
- duration_ms: 28207
- response_chars: 1382
- response_hash: 7ddde24cd00ba691

## Final Output
- answer_chars: 1382
- answer_hash: 7ddde24cd00ba691
- success: True

## Request Complete
- request_end: 2026-08-14T20:27:11.287
- request_duration_ms: 32111
- success: True
- final_source: generation

