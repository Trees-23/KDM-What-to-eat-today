# RAG Process

audit_id: 20260811_171729_855_fa310729
timestamp: 2026-08-11T17:17:29.857
## Request
- original_query: 我想学揭秘食材搭配的智慧：这些食物不宜同食，它的关键要点和适用场景是什么？
- original_query_hash: 27a23a94b8118a4a
- session_id: 2026-08-12-真实考试-001:old:S03-B-08
- request_mode: stream
- request_start: 2026-08-11T17:17:29.858
- evaluation_sample_id: 20260811_171729_855_fa310729
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:17:29.859
- end: 2026-08-11T17:17:29.859
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:17:29.859
- end: 2026-08-11T17:17:29.859
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: 27a23a94b8118a4a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:17:29.860
- end: 2026-08-11T17:17:29.860
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: 27a23a94b8118a4a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:17:29.860
- end: 2026-08-11T17:17:40.910
- duration_ms: 11049
- analysis_mode: llm
- query_complexity: 0.72
- relationship_intensity: 0.78
- reasoning_required: True
- entity_count: 3
- strategy: graph_rag
- confidence: 0.86
- reasoning: 该查询围绕“食材搭配”“不宜同食的食物组合”及其“关键要点/适用场景”展开，虽然未明确列出具体食材，但隐含需要识别多种食材之间的禁忌或风险关系，并结合营养学、消化吸收、个体健康状况及饮食场景进行解释。回答通常需要多跳推理：先定位食物组合，再分析不宜同食的依据或因果机制，最后区分其适用人群与场景；同时可能需要对传统饮食禁忌与现代医学证据进行对比。因此更适合使用graph_rag进行关系检索、证据关联与知识发现。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 77, 'graph_rag_count': 0, 'total_queries': 77}
- route_stats_after: {'traditional_count': 77, 'graph_rag_count': 1, 'total_queries': 78}

## Graph Query Understanding
- query_type: subgraph
- source_entities: ['这些食物不宜同食', '食材搭配']
- target_entities: ['关键要点', '适用场景', '食材搭配禁忌知识章节']
- target_labels: ['TechniqueDoc', 'TechniqueChunk']
- relation_types: ['HAS_CHUNK']
- normalized_relation_types: ['HAS_CHUNK']
- max_depth: 2
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 7029

## Graph Subgraph Extraction Config
- source_entities: ['这些食物不宜同食', '食材搭配']
- max_depth: 2
- max_nodes: 50
- target_labels: ['TechniqueDoc', 'TechniqueChunk', 'Ingredient']
- relation_types: ['HAS_CHUNK', 'REQUIRES']

## Graph Subgraph Status
- central_count: 4
- connected_count: 70
- relationship_count: 79
- density: 0.08621679681830056
- dedupe_count: 0

## Graph Reasoning Patterns
- reasoning_patterns: ['分类归属']

## Graph Reasoning Validation
- judge_model: gpt-5.6-terra
- candidate_count: 0
- accepted_count: 3
- fallback_used: False
- duration_ms: 5949

## Graph Retrieval Complete
- graph_total_duration_ms: 14928
- mode: subgraph
- final_count: 1

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:17:29.860
- end: 2026-08-11T17:17:55.843
- duration_ms: 25982
- selected_strategy: graph_rag
- document_count: 1

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 1
- context_chars: 4910
- retrieval_levels: ['']
- search_types: ['knowledge_subgraph']
- stream: True
- max_retries: 3
- evidence_bundle: False
- verified_graph_fact_count: 0
- text_evidence_count: 0
- limitation_count: 0
- recommendation_evidence_level: None
- recommendation_policy_version: None

## Generation Config
- model_name: gpt-5.6-terra
- base_url_host: downstream.jbbtoken.cn
- temperature: 0.1
- redacted_field: 2048
- stream: True
- timeout: 60
- max_retries: 3

## Generation Stream
- status: success
- chunk_count: 1448
- redacted_field: 3884
- total_duration_ms: 31107
- fallback_used: False

## Final Output
- answer_chars: 1917
- answer_hash: 66aa2dee1298f86a
- success: True

## Request Complete
- request_end: 2026-08-11T17:18:27.003
- request_duration_ms: 57145
- success: True
- final_source: generation

