# RAG Process

audit_id: 20260813_191421_595_2ce84f66
timestamp: 2026-08-13T19:14:21.596
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:14:21.596
- end: 2026-08-13T19:14:21.596
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 37

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:14:25.218
- end: 2026-08-13T19:14:25.218
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3622
- attempt_count: 1
- response_hash: 1ab3dce8ac505deebbb3aa83bc64b7602697d70270408e1c6f9c2f28ffef1bf9
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:14:25.228
- end: 2026-08-13T19:14:25.228
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 99eb1f85e211ce26e0a873bfe11379673a85c7c3ee99185795d0307a4b9f41a6
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:14:25.229
- end: 2026-08-13T19:14:25.229
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:14:25.229+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:14:25.231
- end: 2026-08-13T19:14:25.231
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:14:25.229+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:14:25.231
- end: 2026-08-13T19:14:25.231
- duration_ms: 0
- entity_id: 201000922
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T19:14:25.234
- end: 2026-08-13T19:14:25.234
- duration_ms: 0
- recipe_id: 201000922
- step_id: 201000929

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:14:25.236
- end: 2026-08-13T19:14:25.236
- duration_ms: 0
- parent_id: 201000922
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201000929
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1566
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
- duration_ms: 5064
- response_chars: 142
- response_hash: ef2012cdb743d644

## Final Output
- answer_chars: 142
- answer_hash: ef2012cdb743d644
- success: True

## Request Complete
- request_end: 2026-08-13T19:14:30.302
- request_duration_ms: 8706
- success: True
- final_source: generation

