# RAG Process

audit_id: 20260813_215750_099_2da9e364
timestamp: 2026-08-13T21:57:50.099
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:57:50.100
- end: 2026-08-13T21:57:50.100
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:57:53.491
- end: 2026-08-13T21:57:53.491
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3391
- attempt_count: 1
- response_hash: 0ffef5ae3099d8bf22ff6ba0f9d8f6c03fa9dc66da00e369712d2b86598b8e50
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:57:53.496
- end: 2026-08-13T21:57:53.496
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 656a382640f7122c43a59131a1a036f82e71b151cfb8fdc784e9a6dd33f32a8d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:57:53.496
- end: 2026-08-13T21:57:53.496
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:57:53.496+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:57:53.499
- end: 2026-08-13T21:57:53.499
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:57:53.496+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:57:53.500
- end: 2026-08-13T21:57:53.500
- duration_ms: 0
- entity_id: 201005289
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T21:57:53.503
- end: 2026-08-13T21:57:53.503
- duration_ms: 0
- recipe_id: 201005289
- step_id: 201005302

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:57:53.505
- end: 2026-08-13T21:57:53.505
- duration_ms: 0
- parent_id: 201005289
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- anchor_id: 201005302
- chunk_count: 2

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1700
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
- duration_ms: 3291
- response_chars: 171
- response_hash: d55017aafc2612e6

## Final Output
- answer_chars: 171
- answer_hash: d55017aafc2612e6
- success: True

## Request Complete
- request_end: 2026-08-13T21:57:56.798
- request_duration_ms: 6698
- success: True
- final_source: generation

