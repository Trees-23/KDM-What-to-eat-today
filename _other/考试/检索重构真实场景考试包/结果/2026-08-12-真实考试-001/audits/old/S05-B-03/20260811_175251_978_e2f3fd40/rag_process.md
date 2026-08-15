# RAG Process

audit_id: 20260811_175251_978_e2f3fd40
timestamp: 2026-08-11T17:52:51.979
## Request
- original_query: 做鸭肉相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: 28c3cddfe4ffa5ef
- session_id: 2026-08-12-真实考试-001:old:S05-B-03
- request_mode: stream
- request_start: 2026-08-11T17:52:51.979
- evaluation_sample_id: 20260811_175251_978_e2f3fd40
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:52:51.981
- end: 2026-08-11T17:52:51.981
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:52:51.982
- end: 2026-08-11T17:52:51.982
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 28c3cddfe4ffa5ef

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:52:51.982
- end: 2026-08-11T17:52:51.982
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 28c3cddfe4ffa5ef
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:52:51.983
- end: 2026-08-11T17:53:01.077
- duration_ms: 9093
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.68
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.88
- reasoning: 查询核心是识别“鸭肉”与“蔬菜”类别之间的食材搭配关系，并从知识图谱中枚举满足该关系的具体蔬菜实体。通常需要沿“鸭肉→菜品/烹饪搭配→蔬菜”关系进行一到两跳检索与聚合，不涉及因果分析或多方案优劣对比，但图谱关系查询比纯文本检索更适合发现和归纳可搭配的蔬菜。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 13, 'total_queries': 132}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 14, 'total_queries': 133}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['鸭肉']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5407

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5439
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:52:51.983
- end: 2026-08-11T17:53:06.517
- duration_ms: 14534
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 905
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
- chunk_count: 83
- redacted_field: 4490
- total_duration_ms: 6467
- fallback_used: False

## Final Output
- answer_chars: 112
- answer_hash: b59f35cd68e9cfe5
- success: True

## Request Complete
- request_end: 2026-08-11T17:53:13.004
- request_duration_ms: 21024
- success: True
- final_source: generation

