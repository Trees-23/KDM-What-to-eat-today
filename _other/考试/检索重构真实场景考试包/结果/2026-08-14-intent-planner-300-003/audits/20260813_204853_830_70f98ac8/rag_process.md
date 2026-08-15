# RAG Process

audit_id: 20260813_204853_830_70f98ac8
timestamp: 2026-08-13T20:48:53.830
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:48:53.831
- end: 2026-08-13T20:48:53.831
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 21

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:48:57.545
- end: 2026-08-13T20:48:57.545
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.97
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3714
- attempt_count: 1
- response_hash: 530b11cedb539dc8b3018855105295a42a22bba27a11745f72647d7dfeb8c392
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:48:57.551
- end: 2026-08-13T20:48:57.551
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: 2554886548c3f4804defdb99b0ef8aba01b9c579ee9c456269e6589bd3118e05
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:48:57.551
- end: 2026-08-13T20:48:57.551
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:48:57.551+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:48:57.556
- end: 2026-08-13T20:48:57.556
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:48:57.551+00:00
- result_count: 12

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:57.556
- end: 2026-08-13T20:48:57.556
- duration_ms: 0
- entity_id: 201001698
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:57.573
- end: 2026-08-13T20:48:57.573
- duration_ms: 0
- parent_id: 201001698
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:57.573
- end: 2026-08-13T20:48:57.573
- duration_ms: 0
- entity_id: 201003296
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:57.584
- end: 2026-08-13T20:48:57.584
- duration_ms: 0
- parent_id: 201003296
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:57.584
- end: 2026-08-13T20:48:57.584
- duration_ms: 0
- entity_id: 201003336
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:57.592
- end: 2026-08-13T20:48:57.592
- duration_ms: 0
- parent_id: 201003336
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:57.592
- end: 2026-08-13T20:48:57.592
- duration_ms: 0
- entity_id: 201003902
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:57.598
- end: 2026-08-13T20:48:57.598
- duration_ms: 0
- parent_id: 201003902
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:48:57.598
- end: 2026-08-13T20:48:57.598
- duration_ms: 0
- entity_id: 201003939
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:48:57.604
- end: 2026-08-13T20:48:57.604
- duration_ms: 0
- parent_id: 201003939
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 9164
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 5
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
- duration_ms: 7197
- response_chars: 268
- response_hash: 215391e6b97dfd51

## Final Output
- answer_chars: 268
- answer_hash: 215391e6b97dfd51
- success: True

## Request Complete
- request_end: 2026-08-13T20:49:04.803
- request_duration_ms: 10972
- success: True
- final_source: generation

