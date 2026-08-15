# RAG Process

audit_id: 20260814_205205_035_c2ef390d
timestamp: 2026-08-14T20:52:05.036
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T20:52:05.036
- end: 2026-08-14T20:52:05.036
- duration_ms: 0
- evaluation_constraints_present: False
- user_message_chars: 31

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T20:52:08.150
- end: 2026-08-14T20:52:08.150
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.9
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': [], 'flavor_ingredients': [], 'preferences': [], 'meal_context': [], 'tools': ['MICROWAVE'], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 3114
- attempt_count: 1
- response_hash: 356c19703a282ff8180ebb2023fa33bfd55cfcbac67d3395848ca94c4110ba9c
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / recommendation_constraints
- stage: recommendation_constraints
- status: compiled
- start: 2026-08-14T20:52:08.163
- end: 2026-08-14T20:52:08.163
- duration_ms: 0
- policy_version: recommendation_constraints_v1
- hard_filters: {'cuisines': [], 'verified_ingredient_ids': [], 'methods': [], 'excluded_methods': [], 'required_cooking_appliances': ['MICROWAVE'], 'excluded_cooking_appliances': [], 'exclusive_cooking_appliances': ['MICROWAVE'], 'max_total_minutes': None}
- soft_preferences: {'methods': [], 'tools': [], 'preferences': [], 'meal_context': [], 'prefer_shorter_time': False, 'target_servings': None, 'flavor_terms': []}
- decisions: [{'field': 'tool', 'value': 'MICROWAVE', 'strength': 'positive_hard', 'marker': '排他设备'}]
- clarification_reason: None

## Event / recommendation_scope
- stage: recommendation_scope
- status: resolved
- start: 2026-08-14T20:52:08.173
- end: 2026-08-14T20:52:08.173
- duration_ms: 0
- build_id: pds_51e5e228cb4a935de64e2b7a
- parent_count: 6
- hard_filter_counts: {'initial': 321, 'required_cooking_appliances': 10, 'exclusive_cooking_appliances': 6}

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T20:52:08.173
- end: 2026-08-14T20:52:08.173
- duration_ms: 0
- compile_action: PREFERENCE_RECOMMEND
- reason: None
- query_plan_hash: eb8843b344d2ca52883ef25a6b05c6522690b71070fee58c1f6ad907f2fa1eef
- claim_policy: {'hard_constraints': ['validated_recipe_scope'], 'soft_preferences': ['MICROWAVE'], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / recommendation_vector
- stage: recommendation_vector
- status: selected
- start: 2026-08-14T20:52:08.413
- end: 2026-08-14T20:52:08.413
- duration_ms: 0
- rerank_version: recommendation_rerank_v1
- candidate_count: 6
- answer_count: 5
- candidate_top30: [{'parent_id': '201000550', 'title': '微波炉蛋糕', 'retrieval_score': 0.6553682702064514, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '早餐', 'cook_minutes': 2, 'cook_time': '2分钟', 'cuisine_type': '未知', 'difficulty': 1.0, 'doc_type': 'recipe', 'ingredients_count': 13, 'node_id': '201000550', 'node_type': 'Recipe', 'prep_minutes': 20, 'prep_time': '20分钟（初学者）', 'recipe_cooking_appliances': ['MICROWAVE'], 'recipe_methods': [], 'recipe_name': '微波炉蛋糕', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['微波炉', '容器'], 'servings': '1人份', 'servings_count': 1, 'source': 'neo4j', 'step_count': 7, 'steps_count': 7, 'total_minutes': 22, 'unknown_cooking_appliance': False}}, {'parent_id': '201005691', 'title': '微波炉鸡蛋羹', 'retrieval_score': 0.6535039561271667, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '素菜', 'cook_minutes': 4, 'cook_time': '4分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 7, 'node_id': '201005691', 'node_type': 'Recipe', 'prep_minutes': 3, 'prep_time': '3分钟', 'recipe_cooking_appliances': ['MICROWAVE'], 'recipe_methods': [], 'recipe_name': '微波炉鸡蛋羹', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['陶瓷碗', '筷子', '刀', '微波炉', '保鲜膜', '瓷盘'], 'servings': '1人/份', 'servings_count': 1, 'source': 'neo4j', 'step_count': 10, 'steps_count': 10, 'total_minutes': 7, 'unknown_cooking_appliance': False}}, {'parent_id': '201004446', 'title': '微波炉腊肠煲仔饭', 'retrieval_score': 0.6321610229492187, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '主食', 'cook_minutes': 15, 'cook_time': '15分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 9, 'node_id': '201004446', 'node_type': 'Recipe', 'prep_minutes': 6, 'prep_time': '6分钟（切配腊肠、青菜、红萝卜、葱花）', 'recipe_cooking_appliances': ['MICROWAVE'], 'recipe_methods': [], 'recipe_name': '微波炉腊肠煲仔饭', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['饭碗', '微波炉专用盖', '微波炉', '刀', '案板', '青菜碗', '小碗', '隔热手套'], 'servings': '1人份', 'servings_count': 1, 'source': 'neo4j', 'step_count': 10, 'steps_count': 10, 'total_minutes': 21, 'unknown_cooking_appliance': False}}, {'parent_id': '201000539', 'title': '微波炉荷包蛋', 'retrieval_score': 0.6307927498817444, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '早餐', 'cook_minutes': 80, 'cook_time': '80秒', 'cuisine_type': '未知', 'difficulty': 1.0, 'doc_type': 'recipe', 'ingredients_count': 4, 'node_id': '201000539', 'node_type': 'Recipe', 'prep_minutes': 1, 'prep_time': '1分钟', 'recipe_cooking_appliances': ['MICROWAVE'], 'recipe_methods': [], 'recipe_name': '微波炉荷包蛋', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['小碗', '筷子', '微波炉', '碗', '抹布'], 'servings': '1人', 'servings_count': 1, 'source': 'neo4j', 'step_count': 6, 'steps_count': 6, 'total_minutes': 81, 'unknown_cooking_appliance': False}}, {'parent_id': '201000519', 'title': '太阳蛋', 'retrieval_score': 0.5737920532226563, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '早餐', 'cook_minutes': 3, 'cook_time': '3-5分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 3, 'node_id': '201000519', 'node_type': 'Recipe', 'prep_minutes': 2, 'prep_time': '2分钟', 'recipe_cooking_appliances': ['MICROWAVE'], 'recipe_methods': [], 'recipe_name': '太阳蛋', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['小碗', '筷子或牙签', '牙签或筷子', '微波炉'], 'servings': '1人', 'servings_count': 1, 'source': 'neo4j', 'step_count': 4, 'steps_count': 4, 'total_minutes': 5, 'unknown_cooking_appliance': False}}, {'parent_id': '201003676', 'title': '速冻汤圆', 'retrieval_score': 0.5473953614234924, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '半成品', 'cook_minutes': 4, 'cook_time': '4-5分钟', 'cuisine_type': '未知', 'difficulty': 1.0, 'doc_type': 'recipe', 'ingredients_count': 2, 'node_id': '201003676', 'node_type': 'Recipe', 'prep_minutes': 1, 'prep_time': '1分钟', 'recipe_cooking_appliances': ['MICROWAVE'], 'recipe_methods': [], 'recipe_name': '速冻汤圆', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['碗', '微波炉'], 'servings': '1人份', 'servings_count': 1, 'source': 'neo4j', 'step_count': 4, 'steps_count': 4, 'total_minutes': 5, 'unknown_cooking_appliance': False}}]
- final_top5: [{'parent_id': '201000550', 'best_chunk_score': 0.6510682702064514, 'coverage_bonus': 0.0043, 'retrieval_score': 0.6553682702064514, 'rerank_adjustments': {'base_retrieval': 70.0}, 'final_score': 70.0, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}, {'parent_id': '201005691', 'best_chunk_score': 0.6492039561271667, 'coverage_bonus': 0.0043, 'retrieval_score': 0.6535039561271667, 'rerank_adjustments': {'base_retrieval': 68.79134509738684}, 'final_score': 68.79134509738684, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}, {'parent_id': '201004446', 'best_chunk_score': 0.6278610229492188, 'coverage_bonus': 0.0043, 'retrieval_score': 0.6321610229492187, 'rerank_adjustments': {'base_retrieval': 54.95449158203398}, 'final_score': 54.95449158203398, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}, {'parent_id': '201000539', 'best_chunk_score': 0.6297927498817444, 'coverage_bonus': 0.001, 'retrieval_score': 0.6307927498817444, 'rerank_adjustments': {'base_retrieval': 54.06742541142878}, 'final_score': 54.06742541142878, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}, {'parent_id': '201000519', 'best_chunk_score': 0.5727920532226562, 'coverage_bonus': 0.001, 'retrieval_score': 0.5737920532226563, 'rerank_adjustments': {'base_retrieval': 17.113259675681675}, 'final_score': 17.113259675681675, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}]

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 4308
- retrieval_levels: []
- search_types: []
- stream: False
- max_retries: 0
- evidence_bundle: True
- verified_graph_fact_count: 0
- text_evidence_count: 5
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
- duration_ms: 17294
- response_chars: 528
- response_hash: b155028ae1dfb013

## Final Output
- answer_chars: 528
- answer_hash: b155028ae1dfb013
- success: True

## Request Complete
- request_end: 2026-08-14T20:52:25.710
- request_duration_ms: 20674
- success: True
- final_source: generation

