# RAG Process

audit_id: 20260814_151946_011_60a58b62
timestamp: 2026-08-14T15:19:46.012
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T15:19:46.012
- end: 2026-08-14T15:19:46.012
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 38

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T15:19:52.783
- end: 2026-08-14T15:19:52.783
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_STEP
- confidence: 0.98
- normalized_slots: {'step_number': 1, 'cuisines': [], 'ingredients': [], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6772
- attempt_count: 1
- response_hash: cd2338d30428ec75ab7e6c45abd09fcb8be225b748e52d287d9b866fae00aa42
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T15:19:52.786
- end: 2026-08-14T15:19:52.786
- duration_ms: 0
- compile_action: RECIPE_STEP
- reason: None
- query_plan_hash: 42fd219a21adb874cbb0ab804c6bd0903ed07d7a86e4593166771a87814974a9
- claim_policy: {'hard_constraints': ['verified_graph_relation'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T15:19:52.787
- end: 2026-08-14T15:19:52.787
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:19:52.787+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T15:19:52.788
- end: 2026-08-14T15:19:52.788
- duration_ms: 0
- template_id: recipe_step_anchor_v1
- intent: RECIPE_STEP
- database_timestamp: 2026-08-14T15:19:52.787+00:00
- result_count: 1

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T15:19:52.788
- end: 2026-08-14T15:19:52.788
- duration_ms: 0
- entity_id: 201004863
- scope: RECIPE_STEP

## Event / recipe_step_anchor
- stage: recipe_step_anchor
- status: verified
- start: 2026-08-14T15:19:52.789
- end: 2026-08-14T15:19:52.789
- duration_ms: 0
- recipe_id: 201004863
- step_id: 201004872

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T15:19:52.791
- end: 2026-08-14T15:19:52.791
- duration_ms: 0
- parent_id: 201004863
- build_id: pds_51e5e228cb4a935de64e2b7a
- anchor_id: 201004872
- chunk_count: 3

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1811
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 9725
- response_chars: 127
- response_hash: 6186ab0a38f305cf

## Final Output
- answer_chars: 127
- answer_hash: 6186ab0a38f305cf
- success: True

## Request Complete
- request_end: 2026-08-14T15:20:02.517
- request_duration_ms: 16505
- success: True
- final_source: generation

