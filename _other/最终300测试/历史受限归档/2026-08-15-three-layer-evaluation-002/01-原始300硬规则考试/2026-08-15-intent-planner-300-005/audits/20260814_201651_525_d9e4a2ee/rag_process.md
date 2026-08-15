# RAG Process

audit_id: 20260814_201651_525_d9e4a2ee
timestamp: 2026-08-14T20:16:51.525
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:16:51.525
- end: 2026-08-14T20:16:51.525
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 16

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:16:55.328
- end: 2026-08-14T20:16:55.328
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3803
- attempt_count: 1
- response_hash: bde731024a8606e90f690c70a27093cf9aade77e75f478323bce5c8972059ff4
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:16:55.334
- end: 2026-08-14T20:16:55.334
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 4a1b3ee6344135f747eb05a0ea356ad30899c9b1fa4f36b6386f70d51b7065c6
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:16:55.335
- end: 2026-08-14T20:16:55.335
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:16:55.335+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:16:55.337
- end: 2026-08-14T20:16:55.337
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T20:16:55.335+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:16:55.337
- end: 2026-08-14T20:16:55.337
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T20:16:55.339
- end: 2026-08-14T20:16:55.339
- duration_ms: 0
- recipe_id: 201002797
- step_id: 201002810

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:16:55.341
- end: 2026-08-14T20:16:55.341
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201002810
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1777
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
- duration_ms: 7233
- response_chars: 122
- response_hash: cce82693d44615c9

## Final Output
- answer_chars: 122
- answer_hash: cce82693d44615c9
- success: True

## Request Complete
- request_end: 2026-08-14T20:17:02.575
- request_duration_ms: 11050
- success: True
- final_source: generation

