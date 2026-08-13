# RAG Process

audit_id: 20260813_203209_900_09549ae2
timestamp: 2026-08-13T20:32:09.901
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:32:09.901
- end: 2026-08-13T20:32:09.901
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:32:16.954
- end: 2026-08-13T20:32:16.954
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 7053
- attempt_count: 1
- response_hash: 893ac09c2264b85e697819820efee34e44909ed9ce7bf087621327daa6502c10
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:32:16.965
- end: 2026-08-13T20:32:16.965
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: d645ffae2eaeacec93999b701e410f2b15deff069747466a0340b8eee613d264
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:32:16.966
- end: 2026-08-13T20:32:16.966
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:32:16.966+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:32:16.971
- end: 2026-08-13T20:32:16.971
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:32:16.966+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:32:16.971
- end: 2026-08-13T20:32:16.971
- duration_ms: 0
- entity_id: tipdoc_897acc483178
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:32:16.981
- end: 2026-08-13T20:32:16.981
- duration_ms: 0
- parent_id: tipdoc_897acc483178
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 11

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4342
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
- duration_ms: 19946
- response_chars: 945
- response_hash: 08622f4eacb4fc35

## Final Output
- answer_chars: 945
- answer_hash: 08622f4eacb4fc35
- success: True

## Request Complete
- request_end: 2026-08-13T20:32:36.929
- request_duration_ms: 27027
- success: True
- final_source: generation

