# RAG Process

audit_id: 20260813_220028_227_50cc8ba8
timestamp: 2026-08-13T22:00:28.227
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:00:28.227
- end: 2026-08-13T22:00:28.227
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 25

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:00:31.700
- end: 2026-08-13T22:00:31.700
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3472
- attempt_count: 1
- response_hash: aff9af765c8c612938f290e1feb22aad40c946dde72754bb35344bb924856154
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:00:31.702
- end: 2026-08-13T22:00:31.702
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: a471ede014bfb5358f39ba92efc45021480b0cd81cd34bcd7a339d53f82ec453
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:00:31.702
- end: 2026-08-13T22:00:31.702
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:00:31.702+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:00:31.704
- end: 2026-08-13T22:00:31.704
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:00:31.702+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:00:31.704
- end: 2026-08-13T22:00:31.704
- duration_ms: 0
- entity_id: tipdoc_0f28e4976868
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:00:31.712
- end: 2026-08-13T22:00:31.712
- duration_ms: 0
- parent_id: tipdoc_0f28e4976868
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 20313
- response_chars: 1265
- response_hash: d74b090bbed7c723

## Final Output
- answer_chars: 1265
- answer_hash: d74b090bbed7c723
- success: True

## Request Complete
- request_end: 2026-08-13T22:00:52.027
- request_duration_ms: 23799
- success: True
- final_source: generation

