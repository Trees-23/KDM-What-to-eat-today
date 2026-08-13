# RAG Process

audit_id: 20260813_204207_379_aa6f6c0c
timestamp: 2026-08-13T20:42:07.379
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-13T20:42:07.380
- end: 2026-08-13T20:42:07.380
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-13T20:42:10.718
- end: 2026-08-13T20:42:10.718
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.6-terra
- candidate_version: v1
- candidate_intent: INGREDIENT_RECIPES
- confidence: 0.98
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['西红柿'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3338
- attempt_count: 1
- response_hash: 31176d5daac50705c1b539fdca467851d57b71d2bd8fd58b5ab0f5641543c25d
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-13T20:42:10.724
- end: 2026-08-13T20:42:10.724
- duration_ms: 0
- compile_action: INGREDIENT_RECIPES
- reason: None
- query_plan_hash: dc18a1b1340818bc8ba14689731d3932a55ed07d2d3f03a8f230b38a6770e0ff
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-13T20:42:10.725
- end: 2026-08-13T20:42:10.725
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:42:10.725+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-13T20:42:10.728
- end: 2026-08-13T20:42:10.728
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-13T20:42:10.725+00:00
- result_count: 10

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.728
- end: 2026-08-13T20:42:10.728
- duration_ms: 0
- entity_id: 201003196
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.743
- end: 2026-08-13T20:42:10.743
- duration_ms: 0
- parent_id: 201003196
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.744
- end: 2026-08-13T20:42:10.744
- duration_ms: 0
- entity_id: 201003224
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.759
- end: 2026-08-13T20:42:10.759
- duration_ms: 0
- parent_id: 201003224
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.759
- end: 2026-08-13T20:42:10.759
- duration_ms: 0
- entity_id: 201003844
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.770
- end: 2026-08-13T20:42:10.770
- duration_ms: 0
- parent_id: 201003844
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.770
- end: 2026-08-13T20:42:10.770
- duration_ms: 0
- entity_id: 201004746
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.777
- end: 2026-08-13T20:42:10.777
- duration_ms: 0
- parent_id: 201004746
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.778
- end: 2026-08-13T20:42:10.778
- duration_ms: 0
- entity_id: 201005049
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.787
- end: 2026-08-13T20:42:10.787
- duration_ms: 0
- parent_id: 201005049
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.787
- end: 2026-08-13T20:42:10.787
- duration_ms: 0
- entity_id: 201005181
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.799
- end: 2026-08-13T20:42:10.799
- duration_ms: 0
- parent_id: 201005181
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.800
- end: 2026-08-13T20:42:10.800
- duration_ms: 0
- entity_id: 201005226
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.813
- end: 2026-08-13T20:42:10.813
- duration_ms: 0
- parent_id: 201005226
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.814
- end: 2026-08-13T20:42:10.814
- duration_ms: 0
- entity_id: 201005528
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.822
- end: 2026-08-13T20:42:10.822
- duration_ms: 0
- parent_id: 201005528
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 4

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.822
- end: 2026-08-13T20:42:10.822
- duration_ms: 0
- entity_id: 201005653
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.830
- end: 2026-08-13T20:42:10.830
- duration_ms: 0
- parent_id: 201005653
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-13T20:42:10.830
- end: 2026-08-13T20:42:10.830
- duration_ms: 0
- entity_id: 201005669
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-13T20:42:10.836
- end: 2026-08-13T20:42:10.836
- duration_ms: 0
- parent_id: 201005669
- build_id: pds_2a8c0807733eb8022a623659
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 12355
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 1
- text_evidence_count: 10
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
- duration_ms: 8970
- response_chars: 366
- response_hash: 92709702093d4818

## Final Output
- answer_chars: 366
- answer_hash: 92709702093d4818
- success: True

## Request Complete
- request_end: 2026-08-13T20:42:19.808
- request_duration_ms: 12428
- success: True
- final_source: generation

