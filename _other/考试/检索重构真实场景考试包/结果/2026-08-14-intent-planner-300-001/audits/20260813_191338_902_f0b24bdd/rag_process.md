# RAG Process

audit_id: 20260813_191338_902_f0b24bdd
timestamp: 2026-08-13T19:13:38.902
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T19:13:38.902
- end: 2026-08-13T19:13:38.902
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T19:13:42.437
- end: 2026-08-13T19:13:42.437
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3535
- attempt_count: 1
- response_hash: 0ffef5ae3099d8bf22ff6ba0f9d8f6c03fa9dc66da00e369712d2b86598b8e50
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T19:13:42.444
- end: 2026-08-13T19:13:42.444
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 656a382640f7122c43a59131a1a036f82e71b151cfb8fdc784e9a6dd33f32a8d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T19:13:42.444
- end: 2026-08-13T19:13:42.444
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:13:42.444+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T19:13:42.446
- end: 2026-08-13T19:13:42.446
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T19:13:42.444+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T19:13:42.447
- end: 2026-08-13T19:13:42.447
- duration_ms: 0
- entity_id: 201005289
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T19:13:42.450
- end: 2026-08-13T19:13:42.450
- duration_ms: 0
- recipe_id: 201005289
- step_id: 201005302

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T19:13:42.452
- end: 2026-08-13T19:13:42.452
- duration_ms: 0
- parent_id: 201005289
- build_id: pds_2a8c0807733eb8022a623659
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
- duration_ms: 4166
- response_chars: 189
- response_hash: 15386bb905654666

## Final Output
- answer_chars: 189
- answer_hash: 15386bb905654666
- success: True

## Request Complete
- request_end: 2026-08-13T19:13:46.619
- request_duration_ms: 7716
- success: True
- final_source: generation

