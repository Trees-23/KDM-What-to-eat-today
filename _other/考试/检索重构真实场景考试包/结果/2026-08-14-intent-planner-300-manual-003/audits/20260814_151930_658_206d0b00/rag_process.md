# RAG Process

audit_id: 20260814_151930_658_206d0b00
timestamp: 2026-08-14T15:19:30.658
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:19:30.658
- end: 2026-08-14T15:19:30.658
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:19:36.949
- end: 2026-08-14T15:19:36.949
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.99
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6290
- attempt_count: 1
- response_hash: 6fc8ae116d4d5e016d506d09c058b0191f39210ff4f0c24a4ad0bdd1ac7fbee5
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:19:36.954
- end: 2026-08-14T15:19:36.954
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 656a382640f7122c43a59131a1a036f82e71b151cfb8fdc784e9a6dd33f32a8d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:19:36.954
- end: 2026-08-14T15:19:36.954
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:19:36.954+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:19:36.957
- end: 2026-08-14T15:19:36.957
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:19:36.954+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:19:36.957
- end: 2026-08-14T15:19:36.957
- duration_ms: 0
- entity_id: 201005289
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:19:36.960
- end: 2026-08-14T15:19:36.960
- duration_ms: 0
- recipe_id: 201005289
- step_id: 201005302

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:19:36.962
- end: 2026-08-14T15:19:36.962
- duration_ms: 0
- parent_id: 201005289
- build_id: pds_51e5e228cb4a935de64e2b7a
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
- model_name: gpt-5.5
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 9047
- response_chars: 129
- response_hash: e8b47cbc93dac25c

## Final Output
- answer_chars: 129
- answer_hash: e8b47cbc93dac25c
- success: True

## Request Complete
- request_end: 2026-08-14T15:19:46.011
- request_duration_ms: 15352
- success: True
- final_source: generation

