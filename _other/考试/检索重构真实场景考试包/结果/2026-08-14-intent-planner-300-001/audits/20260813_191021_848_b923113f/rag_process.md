# RAG Process

audit_id: 20260813_191021_848_b923113f
timestamp: 2026-08-13T19:10:21.848
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:10:21.848
- end: 2026-08-13T19:10:21.848
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 15

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:10:25.522
- end: 2026-08-13T19:10:25.522
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3674
- attempt_count: 1
- response_hash: f83d9a2be3f157b44adfdc1fb51a86a27f25565ed3a8c3d565dcbe53970c7c98
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:10:25.533
- end: 2026-08-13T19:10:25.533
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 4e093cb6496f758e6e39dc6ae5974ad0eca9df4f2ff95cada8cc7c8e0d3b276a
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:10:25.533
- end: 2026-08-13T19:10:25.533
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:10:25.533+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:10:25.555
- end: 2026-08-13T19:10:25.555
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:10:25.533+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:10:25.556
- end: 2026-08-13T19:10:25.556
- duration_ms: 0
- entity_id: 201002350
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T19:10:25.568
- end: 2026-08-13T19:10:25.568
- duration_ms: 0
- recipe_id: 201002350
- step_id: 201002360

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:10:25.573
- end: 2026-08-13T19:10:25.573
- duration_ms: 0
- parent_id: 201002350
- build_id: pds_2a8c0807733eb8022a623659
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
- duration_ms: 3791
- response_chars: 108
- response_hash: e1b5f32b360fed3f

## Final Output
- answer_chars: 108
- answer_hash: e1b5f32b360fed3f
- success: True

## Request Complete
- request_end: 2026-08-13T19:10:29.366
- request_duration_ms: 7517
- success: True
- final_source: generation

