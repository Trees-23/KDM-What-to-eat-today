# RAG Process

audit_id: 20260813_203055_426_f839878d
timestamp: 2026-08-13T20:30:55.426
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:30:55.427
- end: 2026-08-13T20:30:55.427
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 25

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:30:58.743
- end: 2026-08-13T20:30:58.743
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: TECHNIQUE_SECTION
- confidence: 0.99
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3928
- attempt_count: 1
- response_hash: ee058363af067ec635e26533b19d8ada4561818e3c3e76a66541db7a3efa6018
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:30:58.747
- end: 2026-08-13T20:30:58.747
- duration_ms: 0
- compile_action: TECHNIQUE_SECTION
- reason: None
- query_plan_hash: 8eaae08d41838c3cdaa971674310f2e67413ef1a1e3969d6ddcec54b6f215389
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:30:58.747
- end: 2026-08-13T20:30:58.747
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:30:58.747+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:30:58.749
- end: 2026-08-13T20:30:58.749
- duration_ms: 0
- template_id: technique_chunks_v1
- intent: TECHNIQUE_CHUNKS
- database_timestamp: 2026-08-13T20:30:58.747+00:00
- result_count: 5

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:30:58.749
- end: 2026-08-13T20:30:58.749
- duration_ms: 0
- entity_id: tipdoc_5e4d6d67fc39
- scope: TECHNIQUE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:30:58.764
- end: 2026-08-13T20:30:58.764
- duration_ms: 0
- parent_id: tipdoc_5e4d6d67fc39
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 10

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 3729
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
- duration_ms: 26444
- response_chars: 904
- response_hash: b0edbd5c38999d7b

## Final Output
- answer_chars: 904
- answer_hash: b0edbd5c38999d7b
- success: True

## Request Complete
- request_end: 2026-08-13T20:31:25.210
- request_duration_ms: 29783
- success: True
- final_source: generation

