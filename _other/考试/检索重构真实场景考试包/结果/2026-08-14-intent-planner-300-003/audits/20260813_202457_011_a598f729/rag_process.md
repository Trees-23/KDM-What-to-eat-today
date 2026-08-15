# RAG Process

audit_id: 20260813_202457_011_a598f729
timestamp: 2026-08-13T20:24:57.012
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:24:57.012
- end: 2026-08-13T20:24:57.012
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 20

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:25:00.415
- end: 2026-08-13T20:25:00.415
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3403
- attempt_count: 1
- response_hash: 3eb06fe7ea9d64d4c27e0d9c96db36db048689b77fc72e37f61b00b4c96794d1
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:25:00.421
- end: 2026-08-13T20:25:00.421
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: ea019547707c2fd261de7aaf4ae016770d5d18c28082ee40239fb0ffa5cfe8f9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:25:00.421
- end: 2026-08-13T20:25:00.421
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:25:00.421+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:25:00.425
- end: 2026-08-13T20:25:00.425
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:25:00.421+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:25:00.425
- end: 2026-08-13T20:25:00.425
- duration_ms: 0
- entity_id: 201001891
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T20:25:00.431
- end: 2026-08-13T20:25:00.431
- duration_ms: 0
- recipe_id: 201001891
- step_id: 201001903

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:25:00.434
- end: 2026-08-13T20:25:00.434
- duration_ms: 0
- parent_id: 201001891
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201001903
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2052
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
- duration_ms: 3625
- response_chars: 101
- response_hash: 9fde7a7322af3c42

## Final Output
- answer_chars: 101
- answer_hash: 9fde7a7322af3c42
- success: True

## Request Complete
- request_end: 2026-08-13T20:25:04.062
- request_duration_ms: 7050
- success: True
- final_source: generation

