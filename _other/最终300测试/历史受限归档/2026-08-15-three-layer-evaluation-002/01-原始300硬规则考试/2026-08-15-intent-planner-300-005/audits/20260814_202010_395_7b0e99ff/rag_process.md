# RAG Process

audit_id: 20260814_202010_395_7b0e99ff
timestamp: 2026-08-14T20:20:10.395
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:20:10.395
- end: 2026-08-14T20:20:10.395
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:20:15.600
- end: 2026-08-14T20:20:15.600
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.96
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 5204
- attempt_count: 1
- response_hash: 00a6b22930655be6efe62140389d33d0acab8dc05e5109e8eee8028e0568db92
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:20:15.604
- end: 2026-08-14T20:20:15.604
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 6fae0412f57270b00700e0c6f4cdf1ba702d6c4700f03ae3281c89e837a1949d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:20:15.605
- end: 2026-08-14T20:20:15.605
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:20:15.605+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:20:15.608
- end: 2026-08-14T20:20:15.608
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:20:15.605+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:20:15.608
- end: 2026-08-14T20:20:15.608
- duration_ms: 0
- entity_id: 201004766
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:20:15.612
- end: 2026-08-14T20:20:15.612
- duration_ms: 0
- recipe_id: 201004766
- step_id: 201004782

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:20:15.615
- end: 2026-08-14T20:20:15.615
- duration_ms: 0
- parent_id: 201004766
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201004782
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1937
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
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 6779
- response_chars: 106
- response_hash: 25cd9902ca0968ff

## Final Output
- answer_chars: 106
- answer_hash: 25cd9902ca0968ff
- success: True

## Request Complete
- request_end: 2026-08-14T20:20:22.395
- request_duration_ms: 11999
- success: True
- final_source: generation

