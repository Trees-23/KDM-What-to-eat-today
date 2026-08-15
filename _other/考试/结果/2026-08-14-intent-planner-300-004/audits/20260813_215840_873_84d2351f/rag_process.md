# RAG Process

audit_id: 20260813_215840_873_84d2351f
timestamp: 2026-08-13T21:58:40.874
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:58:40.874
- end: 2026-08-13T21:58:40.874
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 27

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:58:44.320
- end: 2026-08-13T21:58:44.320
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3445
- attempt_count: 1
- response_hash: f3b91dd457a805bde4d136b0be43eb13627adbbbff62a1ac7a46f4c0b56b0a55
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:58:44.325
- end: 2026-08-13T21:58:44.325
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 50dbba5a679154f5d3b8fdb52f5d46ff7bfe988945b3af42c217f17424d49ed1
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:58:44.326
- end: 2026-08-13T21:58:44.326
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T21:58:44.326+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:58:44.327
- end: 2026-08-13T21:58:44.327
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T21:58:44.326+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:58:44.328
- end: 2026-08-13T21:58:44.328
- duration_ms: 0
- entity_id: tipdoc_820d789ff48e
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:58:44.337
- end: 2026-08-13T21:58:44.337
- duration_ms: 0
- parent_id: tipdoc_820d789ff48e
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 8

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 3074
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
- duration_ms: 14840
- response_chars: 770
- response_hash: 17f3feb7195ef242

## Final Output
- answer_chars: 770
- answer_hash: 17f3feb7195ef242
- success: True

## Request Complete
- request_end: 2026-08-13T21:58:59.179
- request_duration_ms: 18304
- success: True
- final_source: generation

