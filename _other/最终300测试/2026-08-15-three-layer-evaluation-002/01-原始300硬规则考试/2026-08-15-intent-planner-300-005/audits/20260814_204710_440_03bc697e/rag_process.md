# RAG Process

audit_id: 20260814_204710_440_03bc697e
timestamp: 2026-08-14T20:47:10.441
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:47:10.441
- end: 2026-08-14T20:47:10.441
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:47:14.646
- end: 2026-08-14T20:47:14.646
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.94
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4205
- attempt_count: 1
- response_hash: 56db8b38dcc94353d8e3035cb8c1da283db49777eef2fbdb6890368860bb4014
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:47:14.674
- end: 2026-08-14T20:47:14.674
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: a064e17b7cdcf585d1ff3df8f8446642fd953ca23377da0e3049834f8a1705be
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T20:47:14.674
- end: 2026-08-14T20:47:14.674
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:47:14.674+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T20:47:14.685
- end: 2026-08-14T20:47:14.685
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-14T20:47:14.674+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:14.685
- end: 2026-08-14T20:47:14.685
- duration_ms: 0
- entity_id: 201000127
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:14.692
- end: 2026-08-14T20:47:14.692
- duration_ms: 0
- parent_id: 201000127
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:14.692
- end: 2026-08-14T20:47:14.692
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:14.698
- end: 2026-08-14T20:47:14.698
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:47:14.699
- end: 2026-08-14T20:47:14.699
- duration_ms: 0
- entity_id: 201000453
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:47:14.705
- end: 2026-08-14T20:47:14.705
- duration_ms: 0
- parent_id: 201000453
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 6428
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 3
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
- duration_ms: 9281
- response_chars: 253
- response_hash: 6f486b6f83b1e8b7

## Final Output
- answer_chars: 253
- answer_hash: 6f486b6f83b1e8b7
- success: True

## Request Complete
- request_end: 2026-08-14T20:47:23.988
- request_duration_ms: 13546
- success: True
- final_source: generation

