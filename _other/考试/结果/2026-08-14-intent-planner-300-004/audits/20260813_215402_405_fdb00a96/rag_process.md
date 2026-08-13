# RAG Process

audit_id: 20260813_215402_405_fdb00a96
timestamp: 2026-08-13T21:54:02.406
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:54:02.407
- end: 2026-08-13T21:54:02.407
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 15

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:54:05.940
- end: 2026-08-13T21:54:05.940
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3533
- attempt_count: 1
- response_hash: f83d9a2be3f157b44adfdc1fb51a86a27f25565ed3a8c3d565dcbe53970c7c98
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:54:05.947
- end: 2026-08-13T21:54:05.947
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 4e093cb6496f758e6e39dc6ae5974ad0eca9df4f2ff95cada8cc7c8e0d3b276a
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:54:05.947
- end: 2026-08-13T21:54:05.947
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:54:05.947+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:54:05.952
- end: 2026-08-13T21:54:05.952
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:54:05.947+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:54:05.953
- end: 2026-08-13T21:54:05.953
- duration_ms: 0
- entity_id: 201002350
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T21:54:05.956
- end: 2026-08-13T21:54:05.956
- duration_ms: 0
- recipe_id: 201002350
- step_id: 201002360

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:54:05.960
- end: 2026-08-13T21:54:05.960
- duration_ms: 0
- parent_id: 201002350
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- anchor_id: 201002360
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1774
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
- duration_ms: 4364
- response_chars: 95
- response_hash: caebb3782498c907

## Final Output
- answer_chars: 95
- answer_hash: caebb3782498c907
- success: True

## Request Complete
- request_end: 2026-08-13T21:54:10.327
- request_duration_ms: 7920
- success: True
- final_source: generation

