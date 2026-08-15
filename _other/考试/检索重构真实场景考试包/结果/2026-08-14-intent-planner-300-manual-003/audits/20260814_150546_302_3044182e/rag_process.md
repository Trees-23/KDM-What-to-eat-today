# RAG Process

audit_id: 20260814_150546_302_3044182e
timestamp: 2026-08-14T15:05:46.302
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:05:46.303
- end: 2026-08-14T15:05:46.303
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 28

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:05:50.773
- end: 2026-08-14T15:05:50.773
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.95
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STIR_FRY'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4470
- attempt_count: 1
- response_hash: a5feac59e7ce5ce86d1c3f75e89614b9a42691abc2e72b7343b45948eb6c44e8
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:05:50.779
- end: 2026-08-14T15:05:50.779
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['STIR_FRY'], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:05:50.780
- end: 2026-08-14T15:05:50.780
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:05:50.789
- end: 2026-08-14T15:05:50.789
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1298
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 15960
- response_chars: 731
- response_hash: bca22addb5535f7a

## Final Output
- answer_chars: 731
- answer_hash: bca22addb5535f7a
- success: True

## Request Complete
- request_end: 2026-08-14T15:06:06.751
- request_duration_ms: 20448
- success: True
- final_source: generation

