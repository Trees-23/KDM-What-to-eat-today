# RAG Process

audit_id: 20260813_202354_835_604eda4f
timestamp: 2026-08-13T20:23:54.835
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:23:54.835
- end: 2026-08-13T20:23:54.835
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 15

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:23:58.385
- end: 2026-08-13T20:23:58.385
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3549
- attempt_count: 1
- response_hash: fb3c1ebb70e4093d81a40b9fc686f23eb85a824978206279ad259e1b611ff215
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:23:58.391
- end: 2026-08-13T20:23:58.391
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 60515d3d2a99e418dccf26b813d647304219bc3be711b54ebb1101f449d42a69
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:23:58.391
- end: 2026-08-13T20:23:58.391
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:23:58.391+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:23:58.398
- end: 2026-08-13T20:23:58.398
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T20:23:58.391+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:23:58.398
- end: 2026-08-13T20:23:58.398
- duration_ms: 0
- entity_id: 201002327
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T20:23:58.401
- end: 2026-08-13T20:23:58.401
- duration_ms: 0
- recipe_id: 201002327
- step_id: 201002344

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:23:58.402
- end: 2026-08-13T20:23:58.402
- duration_ms: 0
- parent_id: 201002327
- build_id: pds_2a8c0807733eb8022a623659
- anchor_id: 201002344
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1604
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
- duration_ms: 3782
- response_chars: 99
- response_hash: bf3ee56890e11a8f

## Final Output
- answer_chars: 99
- answer_hash: bf3ee56890e11a8f
- success: True

## Request Complete
- request_end: 2026-08-13T20:24:02.187
- request_duration_ms: 7351
- success: True
- final_source: generation

