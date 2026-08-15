# RAG Process

audit_id: 20260813_192121_032_5ae2912a
timestamp: 2026-08-13T19:21:21.032
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:21:21.032
- end: 2026-08-13T19:21:21.032
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:21:25.128
- end: 2026-08-13T19:21:25.128
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.94
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4096
- attempt_count: 1
- response_hash: 679cb8270bcc43537cfe8847631ab19b04e0797344b51b9d6bfa272a2712d077
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:21:26.130
- end: 2026-08-13T19:21:26.130
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: ab2f651a81dec193f0fa096a575ae486bd2762643f3c83b84c33a7e8acad9ba9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:21:26.131
- end: 2026-08-13T19:21:26.131
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:21:26.131+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:21:26.133
- end: 2026-08-13T19:21:26.133
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T19:21:26.131+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:21:26.133
- end: 2026-08-13T19:21:26.133
- duration_ms: 0
- entity_id: tipdoc_7e937e95d07f
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:21:26.140
- end: 2026-08-13T19:21:26.140
- duration_ms: 0
- parent_id: tipdoc_7e937e95d07f
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 7

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4662
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
- duration_ms: 22449
- response_chars: 1289
- response_hash: 1d8e0df055727d5e

## Final Output
- answer_chars: 1289
- answer_hash: 1d8e0df055727d5e
- success: True

## Request Complete
- request_end: 2026-08-13T19:21:48.591
- request_duration_ms: 27558
- success: True
- final_source: generation

