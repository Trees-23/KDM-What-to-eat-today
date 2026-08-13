# RAG Process

audit_id: 20260813_204632_871_60fe887d
timestamp: 2026-08-13T20:46:32.871
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:46:32.872
- end: 2026-08-13T20:46:32.872
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 11

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:46:36.887
- end: 2026-08-13T20:46:36.887
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_VEGETABLE_PAIRS
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 4014
- attempt_count: 1
- response_hash: e01ec6b7e07a8ee873c08294e5bfa488ae1616f09033c7a29ac8e9fd87ea0748
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:46:36.893
- end: 2026-08-13T20:46:36.893
- duration_ms: 0
- compile_action: INGREDIENT_VEGETABLE_PAIRS
- reason: None
- query_plan_hash: accb8121f1db606b7f217c2a68782f6bd32608cde8726058abf248dffa92498d
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:46:36.894
- end: 2026-08-13T20:46:36.894
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:46:36.894+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:46:36.902
- end: 2026-08-13T20:46:36.902
- duration_ms: 0
- template_id: ingredient_vegetable_pairs_v1
- intent: INGREDIENT_VEGETABLE_PAIRS
- database_timestamp: 2026-08-13T20:46:36.894+00:00
- result_count: 26

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:36.903
- end: 2026-08-13T20:46:36.903
- duration_ms: 0
- entity_id: 201001630
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:36.915
- end: 2026-08-13T20:46:36.915
- duration_ms: 0
- parent_id: 201001630
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:36.915
- end: 2026-08-13T20:46:36.915
- duration_ms: 0
- entity_id: 201002555
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:36.931
- end: 2026-08-13T20:46:36.931
- duration_ms: 0
- parent_id: 201002555
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:36.932
- end: 2026-08-13T20:46:36.932
- duration_ms: 0
- entity_id: 201002797
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:36.947
- end: 2026-08-13T20:46:36.947
- duration_ms: 0
- parent_id: 201002797
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:36.947
- end: 2026-08-13T20:46:36.947
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:36.956
- end: 2026-08-13T20:46:36.956
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:36.957
- end: 2026-08-13T20:46:36.957
- duration_ms: 0
- entity_id: 201003314
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:36.964
- end: 2026-08-13T20:46:36.964
- duration_ms: 0
- parent_id: 201003314
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:36.964
- end: 2026-08-13T20:46:36.964
- duration_ms: 0
- entity_id: 201003507
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:36.971
- end: 2026-08-13T20:46:36.971
- duration_ms: 0
- parent_id: 201003507
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:36.971
- end: 2026-08-13T20:46:36.971
- duration_ms: 0
- entity_id: 201003726
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:36.977
- end: 2026-08-13T20:46:36.977
- duration_ms: 0
- parent_id: 201003726
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:46:36.977
- end: 2026-08-13T20:46:36.977
- duration_ms: 0
- entity_id: 201003793
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:46:36.984
- end: 2026-08-13T20:46:36.984
- duration_ms: 0
- parent_id: 201003793
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 16624
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 8
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
- duration_ms: 10071
- response_chars: 413
- response_hash: 705ddc580f14fb73

## Final Output
- answer_chars: 413
- answer_hash: 705ddc580f14fb73
- success: True

## Request Complete
- request_end: 2026-08-13T20:46:47.057
- request_duration_ms: 14184
- success: True
- final_source: generation

