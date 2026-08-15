# RAG Process

audit_id: 20260813_221619_742_08d4a648
timestamp: 2026-08-13T22:16:19.752
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T22:16:19.752
- end: 2026-08-13T22:16:19.752
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T22:16:23.564
- end: 2026-08-13T22:16:23.564
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3811
- attempt_count: 1
- response_hash: 633a19cdf42af60e74b9a00087247a844220c213afa7ea5360444a19d6ffb461
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T22:16:23.567
- end: 2026-08-13T22:16:23.567
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 5056be335e9efa3bb08e47649563d0f19ebc8e63c5ed84948790e6974f17d887
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T22:16:23.568
- end: 2026-08-13T22:16:23.568
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:16:23.568+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T22:16:23.570
- end: 2026-08-13T22:16:23.570
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T22:16:23.568+00:00
- result_count: 7

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:23.570
- end: 2026-08-13T22:16:23.570
- duration_ms: 0
- entity_id: 201001780
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:23.576
- end: 2026-08-13T22:16:23.576
- duration_ms: 0
- parent_id: 201001780
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:23.577
- end: 2026-08-13T22:16:23.577
- duration_ms: 0
- entity_id: 201003372
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:23.584
- end: 2026-08-13T22:16:23.584
- duration_ms: 0
- parent_id: 201003372
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T22:16:23.584
- end: 2026-08-13T22:16:23.584
- duration_ms: 0
- entity_id: 201004709
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T22:16:23.591
- end: 2026-08-13T22:16:23.591
- duration_ms: 0
- parent_id: 201004709
- build_id: pds_8ed95d0ee2ef5e64d703abd6
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 5508
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
- duration_ms: 9061
- response_chars: 321
- response_hash: 41c190fcb7fa3a27

## Final Output
- answer_chars: 321
- answer_hash: 41c190fcb7fa3a27
- success: True

## Request Complete
- request_end: 2026-08-13T22:16:32.653
- request_duration_ms: 12901
- success: True
- final_source: generation

