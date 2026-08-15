# RAG Process

audit_id: 20260813_203236_929_612c857e
timestamp: 2026-08-13T20:32:36.930
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:32:36.930
- end: 2026-08-13T20:32:36.930
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:32:43.220
- end: 2026-08-13T20:32:43.220
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6290
- attempt_count: 1
- response_hash: eb4600a026c1e355def122bbb37a21ca2ca823eb2db162e91f76a4130e821705
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:32:43.222
- end: 2026-08-13T20:32:43.222
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: d9fbd99932a537828ded0562905cc6c1f18d12c934b5e096b9da48c139e9f7c2
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:32:43.222
- end: 2026-08-13T20:32:43.222
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:32:43.222+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:32:43.224
- end: 2026-08-13T20:32:43.224
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:32:43.222+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:32:43.224
- end: 2026-08-13T20:32:43.224
- duration_ms: 0
- entity_id: tipdoc_605102de4ff3
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:32:43.231
- end: 2026-08-13T20:32:43.231
- duration_ms: 0
- parent_id: tipdoc_605102de4ff3
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 10

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4127
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
- duration_ms: 25509
- response_chars: 934
- response_hash: 65e2aa5c225306e9

## Final Output
- answer_chars: 934
- answer_hash: 65e2aa5c225306e9
- success: True

## Request Complete
- request_end: 2026-08-13T20:33:08.741
- request_duration_ms: 31811
- success: True
- final_source: generation

