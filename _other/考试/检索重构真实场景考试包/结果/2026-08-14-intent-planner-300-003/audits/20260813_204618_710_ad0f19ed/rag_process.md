# RAG Process

audit_id: 20260813_204618_710_ad0f19ed
timestamp: 2026-08-13T20:46:18.711
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:46:18.711
- end: 2026-08-13T20:46:18.711
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 36

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:46:22.130
- end: 2026-08-13T20:46:22.130
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3418
- attempt_count: 1
- response_hash: 0b760db0cd70370cbd5d6b3d485bcd8f33671ac415bb423735595c6062e74750
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:46:22.133
- end: 2026-08-13T20:46:22.133
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: 2772892dfb4d87f8a38115265dc4bac51f60809ee2740138c36b4d5169d5c78d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:46:22.133
- end: 2026-08-13T20:46:22.133
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:46:22.133+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:46:22.135
- end: 2026-08-13T20:46:22.135
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:46:22.133+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:22.135
- end: 2026-08-13T20:46:22.135
- duration_ms: 0
- entity_id: 201005583
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:22.142
- end: 2026-08-13T20:46:22.142
- duration_ms: 0
- parent_id: 201005583
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1445
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
- duration_ms: 3050
- response_chars: 74
- response_hash: 420bdee28c652b9d

## Final Output
- answer_chars: 74
- answer_hash: 420bdee28c652b9d
- success: True

## Request Complete
- request_end: 2026-08-13T20:46:25.193
- request_duration_ms: 6481
- success: True
- final_source: generation

