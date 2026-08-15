# RAG Process

audit_id: 20260814_151616_834_392adb99
timestamp: 2026-08-14T15:16:16.834
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:16:16.834
- end: 2026-08-14T15:16:16.834
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:16:21.799
- end: 2026-08-14T15:16:21.799
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4965
- attempt_count: 1
- response_hash: aa878c7c02b0f227da58a3de8f379db295b958245ce62f5c1de883e21276fed4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:16:21.801
- end: 2026-08-14T15:16:21.801
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 5b34b485c052acddca08e701e99a4202c5f1f6c77616fe54331210971077fc1a
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:16:21.802
- end: 2026-08-14T15:16:21.802
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:16:21.802+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:16:21.803
- end: 2026-08-14T15:16:21.803
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:16:21.802+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:16:21.803
- end: 2026-08-14T15:16:21.803
- duration_ms: 0
- entity_id: 201002454
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:16:21.805
- end: 2026-08-14T15:16:21.805
- duration_ms: 0
- recipe_id: 201002454
- step_id: 201002477

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:16:21.806
- end: 2026-08-14T15:16:21.806
- duration_ms: 0
- parent_id: 201002454
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201002477
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1973
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
- duration_ms: 9690
- response_chars: 125
- response_hash: 6b8267f10df7dc32

## Final Output
- answer_chars: 125
- answer_hash: 6b8267f10df7dc32
- success: True

## Request Complete
- request_end: 2026-08-14T15:16:31.498
- request_duration_ms: 14663
- success: True
- final_source: generation

