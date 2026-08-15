# RAG Process

audit_id: 20260813_191823_647_e2abfc45
timestamp: 2026-08-13T19:18:23.647
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:18:23.647
- end: 2026-08-13T19:18:23.647
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:18:27.348
- end: 2026-08-13T19:18:27.348
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3700
- attempt_count: 1
- response_hash: 2ff96e369b05da13f790b998dbdd526ed8535318f8adfff76a72ec9af54af79c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:18:27.353
- end: 2026-08-13T19:18:27.353
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 9b104414f92359e9bffc5a64aef57f82a7372507ea6426ef0cca2c8a9ec9a060
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:18:27.353
- end: 2026-08-13T19:18:27.353
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:18:27.353+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:18:27.358
- end: 2026-08-13T19:18:27.358
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:18:27.353+00:00
- result_count: 25

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:18:27.358
- end: 2026-08-13T19:18:27.358
- duration_ms: 0
- entity_id: tipdoc_fd7f557c37a7
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:18:27.376
- end: 2026-08-13T19:18:27.376
- duration_ms: 0
- parent_id: tipdoc_fd7f557c37a7
- build_id: pds_2a8c0807733eb8022a623659
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 21676
- response_chars: 1172
- response_hash: 59bdf9b498ab06d6

## Final Output
- answer_chars: 1172
- answer_hash: 59bdf9b498ab06d6
- success: True

## Request Complete
- request_end: 2026-08-13T19:18:49.053
- request_duration_ms: 25406
- success: True
- final_source: generation

