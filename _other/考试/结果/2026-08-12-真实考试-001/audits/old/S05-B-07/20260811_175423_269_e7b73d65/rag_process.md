# RAG Process

audit_id: 20260811_175423_269_e7b73d65
timestamp: 2026-08-11T17:54:23.270
## Request
- original_query: 做米饭相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: d59071629e644243
- session_id: 2026-08-12-真实考试-001:old:S05-B-07
- request_mode: stream
- request_start: 2026-08-11T17:54:23.271
- evaluation_sample_id: 20260811_175423_269_e7b73d65
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:54:23.271
- end: 2026-08-11T17:54:23.271
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:54:23.272
- end: 2026-08-11T17:54:23.272
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: d59071629e644243

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:54:23.272
- end: 2026-08-11T17:54:23.272
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: d59071629e644243
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:54:23.273
- end: 2026-08-11T17:54:32.248
- duration_ms: 8974
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.72
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.86
- reasoning: 查询核心是发现“米饭相关菜肴”与“蔬菜”之间的搭配关系，而非检索某个单一实体的属性。通常需要沿知识图谱执行“米饭/米饭类菜肴 → 搭配关系 → 蔬菜”这一到两跳关系查询，并可能覆盖炒饭、盖饭、焖饭等不同菜肴子类。无需因果分析或严格对比分析，但存在关系扩展与类别归纳需求，因此推荐使用graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 17, 'total_queries': 136}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 18, 'total_queries': 137}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['米饭']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 12415

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 12535
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:54:23.273
- end: 2026-08-11T17:54:44.785
- duration_ms: 21512
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
- chunk_count: 101
- redacted_field: 5161
- total_duration_ms: 6716
- fallback_used: False

## Final Output
- answer_chars: 131
- answer_hash: 042cc7db03a43d4d
- success: True

## Request Complete
- request_end: 2026-08-11T17:54:51.518
- request_duration_ms: 28247
- success: True
- final_source: generation

