# RAG Process

audit_id: 20260811_175617_419_1ed5e5a4
timestamp: 2026-08-11T17:56:17.420
## Request
- original_query: 只给出图中能验证的大白菜与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: 9e10d86435b5caa9
- session_id: 2026-08-12-真实考试-001:old:S05-C-02
- request_mode: stream
- request_start: 2026-08-11T17:56:17.421
- evaluation_sample_id: 20260811_175617_419_1ed5e5a4
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:56:17.421
- end: 2026-08-11T17:56:17.421
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:56:17.421
- end: 2026-08-11T17:56:17.421
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: 9e10d86435b5caa9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:56:17.422
- end: 2026-08-11T17:56:17.422
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 31
- analysis_input_query_hash: 9e10d86435b5caa9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:56:17.422
- end: 2026-08-11T17:56:27.320
- duration_ms: 9897
- analysis_mode: llm
- query_complexity: 0.84
- relationship_intensity: 0.88
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.94
- reasoning: 查询以“大白菜”和“蔬菜”为核心实体，要求仅输出图中存在可验证路径支撑的搭配关系，并在缺少路径时明确说明无法证明。这需要进行图谱中的实体定位、关系路径检索与证据校验，可能涉及多跳关系推理；不需要因果分析或对比分析。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 22, 'total_queries': 141}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 23, 'total_queries': 142}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['大白菜']
- target_entities: ['可与大白菜共同用于同一菜谱的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 7833

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 7877
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:56:17.422
- end: 2026-08-11T17:56:35.199
- duration_ms: 17776
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
- chunk_count: 71
- redacted_field: 2098
- total_duration_ms: 3535
- fallback_used: False

## Final Output
- answer_chars: 99
- answer_hash: bf629f6a3429d0dd
- success: True

## Request Complete
- request_end: 2026-08-11T17:56:38.769
- request_duration_ms: 21348
- success: True
- final_source: generation

