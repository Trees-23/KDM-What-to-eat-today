# RAG Process

audit_id: 20260813_220247_060_8b0963ea
timestamp: 2026-08-13T22:02:47.061
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:02:47.061
- end: 2026-08-13T22:02:47.061
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:02:50.707
- end: 2026-08-13T22:02:50.707
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3646
- attempt_count: 1
- response_hash: 2ff96e369b05da13f790b998dbdd526ed8535318f8adfff76a72ec9af54af79c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:02:50.712
- end: 2026-08-13T22:02:50.712
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 9b104414f92359e9bffc5a64aef57f82a7372507ea6426ef0cca2c8a9ec9a060
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:02:50.712
- end: 2026-08-13T22:02:50.712
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:02:50.712+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:02:50.717
- end: 2026-08-13T22:02:50.717
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T22:02:50.712+00:00
- result_count: 25

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:02:50.718
- end: 2026-08-13T22:02:50.718
- duration_ms: 0
- entity_id: tipdoc_fd7f557c37a7
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:02:50.731
- end: 2026-08-13T22:02:50.731
- duration_ms: 0
- parent_id: tipdoc_fd7f557c37a7
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- duration_ms: 21037
- response_chars: 1079
- response_hash: 5915f9d6f28b3333

## Final Output
- answer_chars: 1079
- answer_hash: 5915f9d6f28b3333
- success: True

## Request Complete
- request_end: 2026-08-13T22:03:11.770
- request_duration_ms: 24709
- success: True
- final_source: generation

