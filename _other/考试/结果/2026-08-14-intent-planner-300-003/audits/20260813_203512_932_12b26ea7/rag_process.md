# RAG Process

audit_id: 20260813_203512_932_12b26ea7
timestamp: 2026-08-13T20:35:12.933
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:35:12.933
- end: 2026-08-13T20:35:12.933
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:35:31.027
- end: 2026-08-13T20:35:31.027
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 18750
- attempt_count: 1
- response_hash: 61888af99aa02feec32e5478a59c6d76d34bb3f1faead7e1fbcf0c101d5e72ec
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:35:31.041
- end: 2026-08-13T20:35:31.041
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: ab2f651a81dec193f0fa096a575ae486bd2762643f3c83b84c33a7e8acad9ba9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:35:31.041
- end: 2026-08-13T20:35:31.041
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:35:31.041+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:35:31.043
- end: 2026-08-13T20:35:31.043
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:35:31.041+00:00
- result_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:35:31.043
- end: 2026-08-13T20:35:31.043
- duration_ms: 0
- entity_id: tipdoc_7e937e95d07f
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:35:31.051
- end: 2026-08-13T20:35:31.051
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
- duration_ms: 25756
- response_chars: 1555
- response_hash: f8edfec5de944477

## Final Output
- answer_chars: 1555
- answer_hash: f8edfec5de944477
- success: True

## Request Complete
- request_end: 2026-08-13T20:35:56.808
- request_duration_ms: 43874
- success: True
- final_source: generation

