# RAG Process

audit_id: 20260811_175226_798_550675d9
timestamp: 2026-08-11T17:52:26.800
## Request
- original_query: 做羊肉相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: 4192f0806c022a82
- session_id: 2026-08-12-真实考试-001:old:S05-B-02
- request_mode: stream
- request_start: 2026-08-11T17:52:26.800
- evaluation_sample_id: 20260811_175226_798_550675d9
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:52:26.801
- end: 2026-08-11T17:52:26.801
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:52:26.801
- end: 2026-08-11T17:52:26.801
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 4192f0806c022a82

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:52:26.801
- end: 2026-08-11T17:52:26.801
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 4192f0806c022a82
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:52:26.801
- end: 2026-08-11T17:52:39.974
- duration_ms: 13172
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.62
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.88
- reasoning: 查询的核心是从知识图谱中查找“羊肉”与“蔬菜”之间的菜品搭配关系，属于以实体关系检索为主的中等复杂度问题。明确实体包括“羊肉”（食材/肉类）和“蔬菜”（食材类别）；“做羊肉相关菜”可视为菜品制作场景约束。通常只需执行从羊肉节点沿“搭配/适配/常用配菜”等关系到蔬菜节点的一跳或有限扩展查询，不需要因果分析或对比分析，也不强依赖多跳推理。但由于用户明确要求基于知识图谱获取搭配实体，graph_rag 更适合进行关系边筛选、类别约束和结果发现。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 12, 'total_queries': 131}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 13, 'total_queries': 132}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['羊肉']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 6997

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 7104
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:52:26.801
- end: 2026-08-11T17:52:47.079
- duration_ms: 20277
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 893
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
- chunk_count: 117
- redacted_field: 2587
- total_duration_ms: 4868
- fallback_used: False

## Final Output
- answer_chars: 158
- answer_hash: b96891c4871810ca
- success: True

## Request Complete
- request_end: 2026-08-11T17:52:51.968
- request_duration_ms: 25168
- success: True
- final_source: generation

