# RAG Process

audit_id: 20260814_160338_206_89633c43
timestamp: 2026-08-14T16:03:38.207
## Event / acceptance_input_boundary
- stage: acceptance_input_boundary
- status: isolated
- start: 2026-08-14T16:03:38.208
- end: 2026-08-14T16:03:38.208
- duration_ms: 0
- evaluation_constraints_present: True
- user_message_chars: 17

## Event / intent_planner
- stage: intent_planner
- status: VALID
- start: 2026-08-14T16:03:45.108
- end: 2026-08-14T16:03:45.108
- duration_ms: 0
- planner_version: v1
- planner_model: gpt-5.5
- candidate_version: v1
- candidate_intent: PREFERENCE_RECOMMEND
- confidence: 0.86
- normalized_slots: {'step_number': None, 'cuisines': [], 'ingredients': ['番茄'], 'preferences': [], 'meal_context': [], 'tools': [], 'methods': [], 'servings': None, 'time_budget_minutes': None, 'nutrition_constraint': None}
- latency_ms: 6900
- attempt_count: 1
- response_hash: 460999daf682e7729ff15626dc2c6bf11ba04dcaaf31420edba9d68c6d5ebcae
- response_format: [BODY_REDACTED chars=11 sha256_16=1605dd5aea920e35]
- reason: None

## Event / recommendation_constraints
- stage: recommendation_constraints
- status: compiled
- start: 2026-08-14T16:03:45.163
- end: 2026-08-14T16:03:45.163
- duration_ms: 0
- policy_version: recommendation_constraints_v1
- hard_filters: {'cuisines': [], 'verified_ingredient_ids': ['201003210'], 'methods': [], 'excluded_methods': [], 'required_cooking_appliances': [], 'excluded_cooking_appliances': [], 'exclusive_cooking_appliances': [], 'max_total_minutes': None}
- soft_preferences: {'methods': [], 'tools': [], 'preferences': [], 'meal_context': [], 'prefer_shorter_time': False, 'target_servings': None}
- decisions: []
- clarification_reason: None

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-14T16:03:45.181
- end: 2026-08-14T16:03:45.181
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:03:45.180+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-14T16:03:45.188
- end: 2026-08-14T16:03:45.188
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-14T16:03:45.180+00:00
- result_count: 12

## Event / intent_compile
- stage: intent_compile
- status: EXECUTE
- start: 2026-08-14T16:03:45.191
- end: 2026-08-14T16:03:45.191
- duration_ms: 0
- compile_action: PREFERENCE_RECOMMEND
- reason: None
- query_plan_hash: 63fe72569313df34d5eda2158ed8d706ca6bc8327c1583bfd4c409b157810343
- claim_policy: {'hard_constraints': ['validated_recipe_scope'], 'soft_preferences': [], 'display_requests': [], 'forbidden_claims': ['低脂', '低热量', '低盐', '医疗适用']}

## Event / recommendation_vector
- stage: recommendation_vector
- status: selected
- start: 2026-08-14T16:03:45.479
- end: 2026-08-14T16:03:45.479
- duration_ms: 0
- rerank_version: recommendation_rerank_v1
- candidate_count: 12
- answer_count: 5
- candidate_top30: [{'parent_id': '201003224', 'title': '西红柿牛腩', 'retrieval_score': 0.649044336605072, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '荤菜', 'cook_minutes': 90, 'cook_time': '90分钟', 'cuisine_type': '未知', 'difficulty': 5.0, 'doc_type': 'recipe', 'ingredients_count': 13, 'node_id': '201003224', 'node_type': 'Recipe', 'prep_minutes': 20, 'prep_time': '20分钟', 'recipe_cooking_appliances': ['PRESSURE_COOKER', 'STOVE', 'WOK'], 'recipe_methods': ['BOIL', 'STEW', 'STIR_FRY'], 'recipe_name': '西红柿牛腩', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '锅', '砂锅/高压锅/铝锅', '筷子', '筷子/刀叉', '煤气灶', '炒锅', '锅铲'], 'servings': '1份', 'servings_count': 1, 'source': 'neo4j', 'step_count': 7, 'steps_count': 7, 'total_minutes': 110, 'unknown_cooking_appliance': False}}, {'parent_id': '201003726', 'title': '番茄牛肉蛋花汤', 'retrieval_score': 0.6388193982124328, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '汤类', 'cook_minutes': 10, 'cook_time': '约10分钟', 'cuisine_type': '未知', 'difficulty': 3.0, 'doc_type': 'recipe', 'ingredients_count': 8, 'node_id': '201003726', 'node_type': 'Recipe', 'prep_minutes': 20, 'prep_time': '20-25分钟（含腌制15-20分钟）', 'recipe_cooking_appliances': ['WOK'], 'recipe_methods': ['BOIL'], 'recipe_name': '番茄牛肉蛋花汤', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '碗', '锅', '筷子', '勺子'], 'servings': '1份（基础批次）', 'servings_count': 1, 'source': 'neo4j', 'step_count': 10, 'steps_count': 10, 'total_minutes': 30, 'unknown_cooking_appliance': False}}, {'parent_id': '201005226', 'title': '陕北熬豆角', 'retrieval_score': 0.6355500238418579, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '素菜', 'cook_minutes': 20, 'cook_time': '约20-25分钟', 'cuisine_type': '西北菜', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 13, 'node_id': '201005226', 'node_type': 'Recipe', 'prep_minutes': 10, 'prep_time': '约10分钟', 'recipe_cooking_appliances': ['WOK'], 'recipe_methods': ['BOIL', 'STIR_FRY'], 'recipe_name': '陕北熬豆角', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '炒锅', '锅铲', '锅盖', '筷子'], 'servings': '2人份', 'servings_count': 2, 'source': 'neo4j', 'step_count': 11, 'steps_count': 11, 'total_minutes': 30, 'unknown_cooking_appliance': False}}, {'parent_id': '201005049', 'title': '红烧茄子', 'retrieval_score': 0.6354857104301452, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '素菜', 'cook_minutes': 20, 'cook_time': '约20分钟', 'cuisine_type': '未知', 'difficulty': 4.0, 'doc_type': 'recipe', 'ingredients_count': 12, 'node_id': '201005049', 'node_type': 'Recipe', 'prep_minutes': 15, 'prep_time': '约15分钟', 'recipe_cooking_appliances': ['WOK'], 'recipe_methods': ['FRY', 'STIR_FRY'], 'recipe_name': '红烧茄子', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['水盆', '刀', '案板', '盆', '筷子或打蛋器', '筷子', '炒锅', '漏勺', '锅铲', '盘子'], 'servings': '2人份', 'servings_count': 2, 'source': 'neo4j', 'step_count': 12, 'steps_count': 12, 'total_minutes': 35, 'unknown_cooking_appliance': False}}, {'parent_id': '201005181', 'title': '西红柿炒鸡蛋', 'retrieval_score': 0.6347050087928772, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '素菜', 'cook_minutes': 5, 'cook_time': '5分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 6, 'node_id': '201005181', 'node_type': 'Recipe', 'prep_minutes': 5, 'prep_time': '5分钟', 'recipe_cooking_appliances': ['WOK'], 'recipe_methods': ['STIR_FRY'], 'recipe_name': '西红柿炒鸡蛋', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '锅', '碗', '筷子', '炒锅', '锅铲', '盘子'], 'servings': '1人/份', 'servings_count': 1, 'source': 'neo4j', 'step_count': 7, 'steps_count': 7, 'total_minutes': 10, 'unknown_cooking_appliance': False}}, {'parent_id': '201005669', 'title': '西葫芦炒鸡蛋', 'retrieval_score': 0.6318401748657226, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '素菜', 'cook_minutes': 8, 'cook_time': '约8-9分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 5, 'node_id': '201005669', 'node_type': 'Recipe', 'prep_minutes': 5, 'prep_time': '约5分钟', 'recipe_cooking_appliances': ['WOK'], 'recipe_methods': ['STEW', 'STIR_FRY'], 'recipe_name': '西葫芦炒鸡蛋', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '碗', '筷子', '炒锅', '锅铲'], 'servings': '2人', 'servings_count': 2, 'source': 'neo4j', 'step_count': 9, 'steps_count': 9, 'total_minutes': 13, 'unknown_cooking_appliance': False}}, {'parent_id': '201003196', 'title': '西红柿土豆炖牛肉', 'retrieval_score': 0.6318086402893066, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '荤菜', 'cook_minutes': 60, 'cook_time': '60-90分钟', 'cuisine_type': '未知', 'difficulty': 4.0, 'doc_type': 'recipe', 'ingredients_count': 15, 'node_id': '201003196', 'node_type': 'Recipe', 'prep_minutes': 20, 'prep_time': '约20分钟', 'recipe_cooking_appliances': ['PRESSURE_COOKER', 'WOK'], 'recipe_methods': ['STEW', 'STIR_FRY'], 'recipe_name': '西红柿土豆炖牛肉', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '盆', '锅', '漏勺', '高压锅', '碗', '炒锅', '锅铲', '筷子'], 'servings': '3-4人', 'servings_count': 3, 'source': 'neo4j', 'step_count': 12, 'steps_count': 12, 'total_minutes': 80, 'unknown_cooking_appliance': False}}, {'parent_id': '201003844', 'title': '西红柿鸡蛋汤', 'retrieval_score': 0.6213916557312011, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '汤类', 'cook_minutes': 5, 'cook_time': '约5分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 9, 'node_id': '201003844', 'node_type': 'Recipe', 'prep_minutes': 5, 'prep_time': '约5分钟', 'recipe_cooking_appliances': ['WOK'], 'recipe_methods': ['BOIL', 'STIR_FRY'], 'recipe_name': '西红柿鸡蛋汤', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '碗', '筷子或打蛋器', '炒锅', '锅铲', '筷子'], 'servings': '1人份', 'servings_count': 1, 'source': 'neo4j', 'step_count': 8, 'steps_count': 8, 'total_minutes': 10, 'unknown_cooking_appliance': False}}, {'parent_id': '201005528', 'title': '糖拌西红柿', 'retrieval_score': 0.6187534349441528, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '素菜', 'cook_minutes': 0, 'cook_time': '0分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 2, 'node_id': '201005528', 'node_type': 'Recipe', 'prep_minutes': 5, 'prep_time': '5分钟', 'recipe_cooking_appliances': [], 'recipe_methods': [], 'recipe_name': '糖拌西红柿', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '筷子', '燃气', '开水', '手', '盘子', '冰箱'], 'servings': '2人', 'servings_count': 2, 'source': 'neo4j', 'step_count': 7, 'steps_count': 7, 'total_minutes': 5, 'unknown_cooking_appliance': False}}, {'parent_id': '201005653', 'title': '西红柿豆腐汤羹', 'retrieval_score': 0.6095094139099121, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '素菜', 'cook_minutes': 3, 'cook_time': '3分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 10, 'node_id': '201005653', 'node_type': 'Recipe', 'prep_minutes': 5, 'prep_time': '5分钟', 'recipe_cooking_appliances': ['WOK'], 'recipe_methods': ['BOIL', 'STIR_FRY'], 'recipe_name': '西红柿豆腐汤羹', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '碗', '炒锅', '锅铲'], 'servings': '1人份', 'servings_count': 1, 'source': 'neo4j', 'step_count': 5, 'steps_count': 5, 'total_minutes': 8, 'unknown_cooking_appliance': False}}, {'parent_id': '201002555', 'title': '巴基斯坦牛肉咖喱', 'retrieval_score': 0.6071569936752319, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '荤菜', 'cook_minutes': 2, 'cook_time': '2-3小时', 'cuisine_type': '巴基斯坦菜', 'difficulty': 5.0, 'doc_type': 'recipe', 'ingredients_count': 9, 'node_id': '201002555', 'node_type': 'Recipe', 'prep_minutes': 15, 'prep_time': '约15分钟', 'recipe_cooking_appliances': ['ELECTRIC_COOKER', 'RICE_COOKER', 'WOK'], 'recipe_methods': ['STEW', 'STIR_FRY'], 'recipe_name': '巴基斯坦牛肉咖喱', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '搅拌机', '盆', '炒锅', '锅铲', '电饭煲', '电炖锅', '筷子'], 'servings': '5人', 'servings_count': 5, 'source': 'neo4j', 'step_count': 10, 'steps_count': 10, 'total_minutes': 17, 'unknown_cooking_appliance': True}}, {'parent_id': '201004746', 'title': '西红柿鸡蛋挂面', 'retrieval_score': 0.6001335995674133, 'metadata': {'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'category': '主食', 'cook_minutes': 15, 'cook_time': '15分钟', 'cuisine_type': '未知', 'difficulty': 2.0, 'doc_type': 'recipe', 'ingredients_count': 15, 'node_id': '201004746', 'node_type': 'Recipe', 'prep_minutes': 5, 'prep_time': '5分钟', 'recipe_cooking_appliances': ['WOK'], 'recipe_methods': ['BOIL', 'STIR_FRY'], 'recipe_name': '西红柿鸡蛋挂面', 'recipe_optional_cooking_appliances': [], 'recipe_tools': ['刀', '案板', '碗', '炒锅', '锅铲', '锅', '筷子'], 'servings': '1人', 'servings_count': 1, 'source': 'neo4j', 'step_count': 4, 'steps_count': 4, 'total_minutes': 20, 'unknown_cooking_appliance': False}}]
- final_top5: [{'parent_id': '201003224', 'best_chunk_score': 0.644744336605072, 'coverage_bonus': 0.0043, 'retrieval_score': 0.649044336605072, 'rerank_adjustments': {'base_retrieval': 70.0}, 'final_score': 70.0, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}, {'parent_id': '201003726', 'best_chunk_score': 0.6345193982124329, 'coverage_bonus': 0.0043, 'retrieval_score': 0.6388193982124328, 'rerank_adjustments': {'base_retrieval': 55.36628701927647}, 'final_score': 55.36628701927647, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}, {'parent_id': '201005226', 'best_chunk_score': 0.6312500238418579, 'coverage_bonus': 0.0043, 'retrieval_score': 0.6355500238418579, 'rerank_adjustments': {'base_retrieval': 50.6872283953175}, 'final_score': 50.6872283953175, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}, {'parent_id': '201005049', 'best_chunk_score': 0.6311857104301453, 'coverage_bonus': 0.0043, 'retrieval_score': 0.6354857104301452, 'rerank_adjustments': {'base_retrieval': 50.59518441698981}, 'final_score': 50.59518441698981, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}, {'parent_id': '201005181', 'best_chunk_score': 0.6304050087928772, 'coverage_bonus': 0.0043, 'retrieval_score': 0.6347050087928772, 'rerank_adjustments': {'base_retrieval': 49.47786094327712}, 'final_score': 49.47786094327712, 'attribute_provenance': {'cook_minutes': 'graph_recipe.cookTime', 'prep_minutes': 'graph_recipe.prepTime', 'recipe_cooking_appliances': 'graph_step.tools', 'recipe_methods': 'graph_step.methods', 'recipe_tools': 'graph_step.tools', 'servings_count': 'graph_recipe.servings', 'step_count': 'graph_recipe.CONTAINS_STEP'}, 'unknown_cooking_appliance': False}]

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 5795
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
- timeout: 60.0
- max_retries: 1

## Generation Non-Stream
- status: success
- duration_ms: 32863
- response_chars: 1049
- response_hash: 6609e39523a48852

## Final Output
- answer_chars: 1049
- answer_hash: 6609e39523a48852
- success: True

## Request Complete
- request_end: 2026-08-14T16:04:18.346
- request_duration_ms: 40138
- success: True
- final_source: generation

