# RAG Process

audit_id: 20260813_204824_342_7b815f1b
timestamp: 2026-08-13T20:48:24.342
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:48:24.342
- end: 2026-08-13T20:48:24.342
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 10

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:48:27.998
- end: 2026-08-13T20:48:27.998
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3655
- attempt_count: 1
- response_hash: ab69209f7c38985f90af1f9254b75f689fc79f82de81d8ad861e198bc920767a
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:48:28.001
- end: 2026-08-13T20:48:28.001
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 4062df9525f0148c7eac69740706ace8e3b824994a13b40d182600131ed2461b
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:48:28.002
- end: 2026-08-13T20:48:28.002
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:48:28.002+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:48:28.003
- end: 2026-08-13T20:48:28.003
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:48:28.002+00:00
- result_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:28.003
- end: 2026-08-13T20:48:28.003
- duration_ms: 0
- entity_id: 201000272
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:28.011
- end: 2026-08-13T20:48:28.011
- duration_ms: 0
- parent_id: 201000272
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 2565
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
- duration_ms: 5229
- response_chars: 156
- response_hash: c0f1e74b64879ade

## Final Output
- answer_chars: 156
- answer_hash: c0f1e74b64879ade
- success: True

## Request Complete
- request_end: 2026-08-13T20:48:33.242
- request_duration_ms: 8899
- success: True
- final_source: generation

