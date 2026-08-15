# RAG Process

audit_id: 20260811_175203_152_cf0bf41e
timestamp: 2026-08-11T17:52:03.153
## Request
- original_query: 做排骨相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: af8e25fe34ad09e9
- session_id: 2026-08-12-真实考试-001:old:S05-B-01
- request_mode: stream
- request_start: 2026-08-11T17:52:03.153
- evaluation_sample_id: 20260811_175203_152_cf0bf41e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:52:03.154
- end: 2026-08-11T17:52:03.154
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:52:03.154
- end: 2026-08-11T17:52:03.154
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: af8e25fe34ad09e9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:52:03.155
- end: 2026-08-11T17:52:03.155
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: af8e25fe34ad09e9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:52:03.155
- end: 2026-08-11T17:52:13.690
- duration_ms: 10535
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.68
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.88
- reasoning: 查询的核心意图是从知识图谱中查找“排骨”与“蔬菜”之间的菜品搭配关系，而非获取单一实体属性。明确实体包括“排骨”（食材/肉类）和“蔬菜”（食材类别）；“相关菜”可视为菜品场景或隐含关系约束。该任务通常需要沿知识图谱执行“排骨→适合搭配/共同烹饪→蔬菜”的一跳或有限多跳关系查询，并可能对蔬菜类别下的具体实体进行聚合和筛选。无需因果分析，也不要求不同搭配方案的显式对比，但存在基于关系边的关联检索需求，因此选择 graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 11, 'total_queries': 130}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 12, 'total_queries': 131}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['排骨']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 4344

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5959
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:52:03.155
- end: 2026-08-11T17:52:19.651
- duration_ms: 16496
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 923
- retrieval_levels: ['']
- search_types: ['graph_path']
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
- chunk_count: 92
- redacted_field: 3904
- total_duration_ms: 7118
- fallback_used: False

## Final Output
- answer_chars: 125
- answer_hash: 49715a5f000fb295
- success: True

## Request Complete
- request_end: 2026-08-11T17:52:26.791
- request_duration_ms: 23637
- success: True
- final_source: generation

