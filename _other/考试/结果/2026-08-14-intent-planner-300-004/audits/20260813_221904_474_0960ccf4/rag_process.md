# RAG Process

audit_id: 20260813_221904_474_0960ccf4
timestamp: 2026-08-13T22:19:04.474
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:19:04.475
- end: 2026-08-13T22:19:04.475
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:19:08.090
- end: 2026-08-13T22:19:08.090
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3615
- attempt_count: 1
- response_hash: 0f61b9b0d265e5476904fab348e2394531c19b86df629876676592a8c75f1a30
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:19:08.104
- end: 2026-08-13T22:19:08.104
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: a064e17b7cdcf585d1ff3df8f8446642fd953ca23377da0e3049834f8a1705be
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:19:08.104
- end: 2026-08-13T22:19:08.104
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:19:08.104+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:19:08.107
- end: 2026-08-13T22:19:08.107
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:19:08.104+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:19:08.107
- end: 2026-08-13T22:19:08.107
- duration_ms: 0
- entity_id: 201000127
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:19:08.115
- end: 2026-08-13T22:19:08.115
- duration_ms: 0
- parent_id: 201000127
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:19:08.115
- end: 2026-08-13T22:19:08.115
- duration_ms: 0
- entity_id: 201000290
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:19:08.123
- end: 2026-08-13T22:19:08.123
- duration_ms: 0
- parent_id: 201000290
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:19:08.123
- end: 2026-08-13T22:19:08.123
- duration_ms: 0
- entity_id: 201000453
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:19:08.131
- end: 2026-08-13T22:19:08.131
- duration_ms: 0
- parent_id: 201000453
- build_id: pds_8ed95d0ee2ef5e64d703abd6
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
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: False
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 7417
- response_chars: 290
- response_hash: 509b8ed1064fa55a

## Final Output
- answer_chars: 290
- answer_hash: 509b8ed1064fa55a
- success: True

## Request Complete
- request_end: 2026-08-13T22:19:15.550
- request_duration_ms: 11075
- success: True
- final_source: generation

