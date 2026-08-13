# RAG Process

audit_id: 20260813_215611_027_026a30d0
timestamp: 2026-08-13T21:56:11.027
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T21:56:11.028
- end: 2026-08-13T21:56:11.028
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T21:56:14.975
- end: 2026-08-13T21:56:14.975
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3947
- attempt_count: 1
- response_hash: b4c1a62e4312d49d7ec32945db3ed6f34b9698cb7275e2d1b786c50d7a32a1ba
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T21:56:14.980
- end: 2026-08-13T21:56:14.980
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 1b34cc6b3862ac299bdf73a21799befbb8c28f1572b42091f67cc155b46d2e4c
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T21:56:14.980
- end: 2026-08-13T21:56:14.980
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:56:14.980+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T21:56:14.983
- end: 2026-08-13T21:56:14.983
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-13T21:56:14.980+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T21:56:14.984
- end: 2026-08-13T21:56:14.984
- duration_ms: 0
- entity_id: 201002035
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-13T21:56:14.986
- end: 2026-08-13T21:56:14.986
- duration_ms: 0
- recipe_id: 201002035
- step_id: 201002046

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T21:56:14.989
- end: 2026-08-13T21:56:14.989
- duration_ms: 0
- parent_id: 201002035
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- anchor_id: 201002046
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1771
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
- duration_ms: 4181
- response_chars: 97
- response_hash: 3e26f27fe9727df1

## Final Output
- answer_chars: 97
- answer_hash: 3e26f27fe9727df1
- success: True

## Request Complete
- request_end: 2026-08-13T21:56:19.172
- request_duration_ms: 8144
- success: True
- final_source: generation

