# RAG Process

audit_id: 20260813_204916_877_d14a2895
timestamp: 2026-08-13T20:49:16.878
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:49:16.878
- end: 2026-08-13T20:49:16.878
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:49:20.329
- end: 2026-08-13T20:49:20.329
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3451
- attempt_count: 1
- response_hash: 2c7fa08ed4bd5a2aafcd0bfae7ea4ded28bcb0406f1ca97a6b92e6fec0e83fb3
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:49:20.332
- end: 2026-08-13T20:49:20.332
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: c7f5c8ce174552bdcbaa7c555b482b92f4c96d4e52a49f61c050f084b9b50d96
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:49:20.332
- end: 2026-08-13T20:49:20.332
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:49:20.332+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:49:20.334
- end: 2026-08-13T20:49:20.334
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:49:20.332+00:00
- result_count: 6

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:49:20.334
- end: 2026-08-13T20:49:20.334
- duration_ms: 0
- entity_id: 201001428
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:49:20.341
- end: 2026-08-13T20:49:20.341
- duration_ms: 0
- parent_id: 201001428
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:49:20.341
- end: 2026-08-13T20:49:20.341
- duration_ms: 0
- entity_id: 201002327
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:49:20.348
- end: 2026-08-13T20:49:20.348
- duration_ms: 0
- parent_id: 201002327
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4273
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 2
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
- duration_ms: 8526
- response_chars: 242
- response_hash: 213850306515855e

## Final Output
- answer_chars: 242
- answer_hash: 213850306515855e
- success: True

## Request Complete
- request_end: 2026-08-13T20:49:28.876
- request_duration_ms: 11998
- success: True
- final_source: generation

