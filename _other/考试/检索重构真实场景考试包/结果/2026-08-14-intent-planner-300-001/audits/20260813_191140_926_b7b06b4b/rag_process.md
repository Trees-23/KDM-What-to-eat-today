# RAG Process

audit_id: 20260813_191140_926_b7b06b4b
timestamp: 2026-08-13T19:11:40.927
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:11:40.928
- end: 2026-08-13T19:11:40.928
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:11:44.575
- end: 2026-08-13T19:11:44.575
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3647
- attempt_count: 1
- response_hash: 93e2319620c9af6a21efb662ffbd52bc97f27e36f8deaf9b14364fb206f5116e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:11:44.588
- end: 2026-08-13T19:11:44.588
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: b41d603b8ba07b5b9c0c52c0a34136a2f3d1653f30876b8530b0fd442420a500
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:11:44.589
- end: 2026-08-13T19:11:44.589
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:11:44.589+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:11:44.594
- end: 2026-08-13T19:11:44.594
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:11:44.589+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:11:44.594
- end: 2026-08-13T19:11:44.594
- duration_ms: 0
- entity_id: 201002073
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T19:11:44.600
- end: 2026-08-13T19:11:44.600
- duration_ms: 0
- recipe_id: 201002073
- step_id: 201002091

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:11:44.602
- end: 2026-08-13T19:11:44.602
- duration_ms: 0
- parent_id: 201002073
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201002091
- chunk_count: 2

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1987
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
- duration_ms: 6023
- response_chars: 133
- response_hash: bee75ed13b9fc80f

## Final Output
- answer_chars: 133
- answer_hash: bee75ed13b9fc80f
- success: True

## Request Complete
- request_end: 2026-08-13T19:11:50.627
- request_duration_ms: 9699
- success: True
- final_source: generation

