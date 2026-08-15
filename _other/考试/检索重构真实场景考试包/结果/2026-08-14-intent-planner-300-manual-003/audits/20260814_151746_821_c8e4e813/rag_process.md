# RAG Process

audit_id: 20260814_151746_821_c8e4e813
timestamp: 2026-08-14T15:17:46.821
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:17:46.821
- end: 2026-08-14T15:17:46.821
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:17:53.755
- end: 2026-08-14T15:17:53.755
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.89
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6933
- attempt_count: 1
- response_hash: cd423ed88bf8848ceb41cc2a4ea2ba15e6d40fb5972a4844775ab9fb5f4c331a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:17:53.763
- end: 2026-08-14T15:17:53.763
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: b523a832887435f7352d45ba49b7e86ac4d87716e2e65563fc25833811eb99a3
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:17:53.764
- end: 2026-08-14T15:17:53.764
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:17:53.764+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:17:53.768
- end: 2026-08-14T15:17:53.768
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:17:53.764+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:17:53.769
- end: 2026-08-14T15:17:53.769
- duration_ms: 0
- entity_id: 201000160
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:17:53.773
- end: 2026-08-14T15:17:53.773
- duration_ms: 0
- recipe_id: 201000160
- step_id: 201000177

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:17:53.778
- end: 2026-08-14T15:17:53.778
- duration_ms: 0
- parent_id: 201000160
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201000177
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1578
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
- duration_ms: 8956
- response_chars: 142
- response_hash: b8a6e31dc32e41d4

## Final Output
- answer_chars: 142
- answer_hash: b8a6e31dc32e41d4
- success: True

## Request Complete
- request_end: 2026-08-14T15:18:02.736
- request_duration_ms: 15915
- success: True
- final_source: generation

