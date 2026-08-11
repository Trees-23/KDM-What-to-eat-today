# RAG Process

audit_id: 20260811_175852_783_c3f6b53f
timestamp: 2026-08-11T17:58:52.784
## Request
- original_query: 只给出图中能验证的西兰花与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: df0ff0db6941928c
- session_id: 2026-08-12-真实考试-001:old:S05-C-08
- request_mode: stream
- request_start: 2026-08-11T17:58:52.785
- evaluation_sample_id: 20260811_175852_783_c3f6b53f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:58:52.786
- end: 2026-08-11T17:58:52.786
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:58:52.787
- end: 2026-08-11T17:58:52.787
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: df0ff0db6941928c

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:58:52.788
- end: 2026-08-11T17:58:52.788
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 31
- analysis_input_query_hash: df0ff0db6941928c
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:58:52.788
- end: 2026-08-11T17:59:04.867
- duration_ms: 12078
- analysis_mode: llm
- query_complexity: 0.78
- relationship_intensity: 0.86
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.93
- reasoning: 查询的核心约束是“只给出图中能验证”的西兰花与蔬菜搭配，并要求在不存在关系路径时明确输出“无法证明”。这不是简单的关键词匹配，而是需要在图结构中识别实体“西兰花”与其他“蔬菜”之间的搭配关系，并验证二者是否存在可追溯、满足条件的关系路径。该任务通常需要至少一步关系检索，若搭配关系通过中间节点表达，则需要多跳路径验证；不需要因果分析，也不以比较不同对象优劣为目标。明确实体为2个：西兰花（具体食材/蔬菜实体）和蔬菜（食材类别实体）。由于查询强调图内证据、路径存在性与不可证明时的保守回答，应选择graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 28, 'total_queries': 147}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 29, 'total_queries': 148}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['西兰花']
- target_entities: ['与西兰花共同被菜谱使用的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 8010

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY', 'BELONGS_TO']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 8088
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:58:52.788
- end: 2026-08-11T17:59:12.957
- duration_ms: 20168
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 908
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
- chunk_count: 1
- redacted_field: 8399
- total_duration_ms: 8402
- fallback_used: False

## Final Output
- answer_chars: 114
- answer_hash: d4ce7ea2e9afbd21
- success: True

## Request Complete
- request_end: 2026-08-11T17:59:21.390
- request_duration_ms: 28605
- success: True
- final_source: generation

