# RAG Process

audit_id: 20260814_151315_814_0fa14b18
timestamp: 2026-08-14T15:13:15.815
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:13:15.815
- end: 2026-08-14T15:13:15.815
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 39

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:13:19.926
- end: 2026-08-14T15:13:19.926
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.92
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': ['STEW'], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4111
- attempt_count: 1
- response_hash: 79b4c790200d7b88aaa896f5876fda10cef56f4f385c7b14e16530ad39014893
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:13:19.931
- end: 2026-08-14T15:13:19.931
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['STEW'], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:13:19.932
- end: 2026-08-14T15:13:19.932
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:13:19.942
- end: 2026-08-14T15:13:19.942
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1736
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
- duration_ms: 21705
- response_chars: 887
- response_hash: 7644abad815ae59c

## Final Output
- answer_chars: 887
- answer_hash: 7644abad815ae59c
- success: True

## Request Complete
- request_end: 2026-08-14T15:13:41.649
- request_duration_ms: 25833
- success: True
- final_source: generation

