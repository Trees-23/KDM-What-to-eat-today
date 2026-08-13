# RAG Process

audit_id: 20260813_202439_649_b5a0ea78
timestamp: 2026-08-13T20:24:39.649
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:24:39.650
- end: 2026-08-13T20:24:39.650
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:24:43.023
- end: 2026-08-13T20:24:43.023
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3372
- attempt_count: 1
- response_hash: 93e2319620c9af6a21efb662ffbd52bc97f27e36f8deaf9b14364fb206f5116e
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:24:43.028
- end: 2026-08-13T20:24:43.028
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: b41d603b8ba07b5b9c0c52c0a34136a2f3d1653f30876b8530b0fd442420a500
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:24:43.029
- end: 2026-08-13T20:24:43.029
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:24:43.029+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:24:43.032
- end: 2026-08-13T20:24:43.032
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:24:43.029+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:24:43.033
- end: 2026-08-13T20:24:43.033
- duration_ms: 0
- entity_id: 201002073
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T20:24:43.037
- end: 2026-08-13T20:24:43.037
- duration_ms: 0
- recipe_id: 201002073
- step_id: 201002091

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:24:43.039
- end: 2026-08-13T20:24:43.039
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
- duration_ms: 6083
- response_chars: 143
- response_hash: def2964dd12bd065

## Final Output
- answer_chars: 143
- answer_hash: def2964dd12bd065
- success: True

## Request Complete
- request_end: 2026-08-13T20:24:49.124
- request_duration_ms: 9473
- success: True
- final_source: generation

