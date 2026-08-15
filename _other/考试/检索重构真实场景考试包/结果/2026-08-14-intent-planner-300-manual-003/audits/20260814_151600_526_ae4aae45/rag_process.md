# RAG Process

audit_id: 20260814_151600_526_ae4aae45
timestamp: 2026-08-14T15:16:00.527
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:16:00.527
- end: 2026-08-14T15:16:00.527
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:16:08.625
- end: 2026-08-14T15:16:08.625
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.95
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 9058
- attempt_count: 1
- response_hash: 43edd5d3882a15bf7385574d2f46ce2a74c5d2b9153537a8293b7a4a86d4b911
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:16:08.630
- end: 2026-08-14T15:16:08.630
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: b41d603b8ba07b5b9c0c52c0a34136a2f3d1653f30876b8530b0fd442420a500
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:16:08.631
- end: 2026-08-14T15:16:08.631
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:16:08.631+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:16:08.634
- end: 2026-08-14T15:16:08.634
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:16:08.631+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:16:08.634
- end: 2026-08-14T15:16:08.634
- duration_ms: 0
- entity_id: 201002073
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:16:08.637
- end: 2026-08-14T15:16:08.637
- duration_ms: 0
- recipe_id: 201002073
- step_id: 201002091

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:16:08.639
- end: 2026-08-14T15:16:08.639
- duration_ms: 0
- parent_id: 201002073
- build_id: pds_51e5e228cb4a935de64e2b7a
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 8192
- response_chars: 168
- response_hash: c6f89fe4354d5b69

## Final Output
- answer_chars: 168
- answer_hash: c6f89fe4354d5b69
- success: True

## Request Complete
- request_end: 2026-08-14T15:16:16.833
- request_duration_ms: 16306
- success: True
- final_source: generation

