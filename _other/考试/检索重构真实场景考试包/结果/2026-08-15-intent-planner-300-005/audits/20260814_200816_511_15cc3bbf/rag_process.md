# RAG Process

audit_id: 20260814_200816_511_15cc3bbf
timestamp: 2026-08-14T20:08:16.511
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:08:16.511
- end: 2026-08-14T20:08:16.511
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 26

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:08:23.138
- end: 2026-08-14T20:08:23.138
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: RECIPE_DETAIL
- confidence: 0.96
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['黑鳕鱼'], 'flavor_ingredients': ['葱', '姜'], 'preferences': [], 'meal_context': [], 'tools': ['MICROWAVE'], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6626
- attempt_count: 1
- response_hash: 07ff52f9cd02431da583f693e18e6dfc1c16e4a9755b5443b579d65244b497bb
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:08:23.145
- end: 2026-08-14T20:08:23.144
- duration_ms: 0
- compile_action: PDS_ENTITY_DETAIL
- reason: None
- query_plan_hash: None
- claim_policy: {'hard_constraints': [], 'soft_preferences': ['MICROWAVE', '葱', '姜'], 'display_requests': ['正文'], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-14T20:08:23.145
- end: 2026-08-14T20:08:23.145
- duration_ms: 0
- entity_id: 201000023
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: verified
- start: 2026-08-14T20:08:23.163
- end: 2026-08-14T20:08:23.163
- duration_ms: 0
- parent_id: 201000023
- build_id: pds_51e5e228cb4a935de64e2b7a
- chunk_count: 4

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 1379
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
- timeout: 45.0
- max_retries: 0

## Generation Non-Stream
- status: success
- duration_ms: 18333
- response_chars: 656
- response_hash: 92be02801e7b37f0

## Final Output
- answer_chars: 656
- answer_hash: 92be02801e7b37f0
- success: True

## Request Complete
- request_end: 2026-08-14T20:08:41.498
- request_duration_ms: 24987
- success: True
- final_source: generation

