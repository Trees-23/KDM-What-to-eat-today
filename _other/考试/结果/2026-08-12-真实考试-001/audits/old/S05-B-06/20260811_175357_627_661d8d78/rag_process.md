# RAG Process

audit_id: 20260811_175357_627_661d8d78
timestamp: 2026-08-11T17:53:57.629
## Request
- original_query: 做普通面条相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: 8b087794b4efe023
- session_id: 2026-08-12-真实考试-001:old:S05-B-06
- request_mode: stream
- request_start: 2026-08-11T17:53:57.629
- evaluation_sample_id: 20260811_175357_627_661d8d78
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:53:57.630
- end: 2026-08-11T17:53:57.630
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:53:57.630
- end: 2026-08-11T17:53:57.630
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 8b087794b4efe023

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:53:57.631
- end: 2026-08-11T17:53:57.631
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: 8b087794b4efe023
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:53:57.631
- end: 2026-08-11T17:54:06.336
- duration_ms: 8705
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.68
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.87
- reasoning: 查询的核心目标是在知识图谱中发现“普通面条”相关菜品与“蔬菜”之间的搭配关系。通常需要沿“普通面条→相关菜品→配料/搭配蔬菜”的路径进行一到两跳关系检索，并可能聚合多个菜品节点下的蔬菜结果。该查询不需要因果分析或复杂对比分析，但具有明确的实体关系探索需求，因此更适合使用 graph_rag。明确实体包括“普通面条”（食材/主食类实体）和“蔬菜”（食材类别实体）；“相关菜”属于关系范围或菜品类别约束，而非明确的具体菜品实体。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 16, 'total_queries': 135}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 17, 'total_queries': 136}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['普通面条']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 12253

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 12282
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:53:57.631
- end: 2026-08-11T17:54:18.620
- duration_ms: 20989
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
- chunk_count: 95
- redacted_field: 2639
- total_duration_ms: 4613
- fallback_used: False

## Final Output
- answer_chars: 125
- answer_hash: ac65bf2192ddfe6d
- success: True

## Request Complete
- request_end: 2026-08-11T17:54:23.259
- request_duration_ms: 25630
- success: True
- final_source: generation

