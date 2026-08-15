# RAG Process

audit_id: 20260811_175556_216_306a7613
timestamp: 2026-08-11T17:55:56.217
## Request
- original_query: 只给出图中能验证的南瓜与蔬菜搭配；没有路径时请说明无法证明。
- original_query_hash: 2047587b1392fb16
- session_id: 2026-08-12-真实考试-001:old:S05-C-01
- request_mode: stream
- request_start: 2026-08-11T17:55:56.217
- evaluation_sample_id: 20260811_175556_216_306a7613
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:55:56.217
- end: 2026-08-11T17:55:56.217
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:55:56.218
- end: 2026-08-11T17:55:56.218
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 30
- enhanced_query_length: 30
- enhanced_query_hash: 2047587b1392fb16

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:55:56.218
- end: 2026-08-11T17:55:56.218
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 30
- analysis_input_query_hash: 2047587b1392fb16
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:55:56.218
- end: 2026-08-11T17:56:04.221
- duration_ms: 8002
- analysis_mode: llm
- query_complexity: 0.82
- relationship_intensity: 0.88
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.91
- reasoning: 查询要求仅输出“图中能验证”的南瓜与蔬菜搭配，且必须依据图内实体关系路径进行证据约束；若不存在可达路径，还需显式判断并说明无法证明。这不是简单的实体检索，而是需要从图结构中识别“南瓜”与具体蔬菜实体之间的搭配关系、验证关系边或多跳路径，并避免基于常识补全未在图中出现的关联。查询不要求因果或对比分析，但需要关系路径验证，适合采用graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 21, 'total_queries': 140}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 22, 'total_queries': 141}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['南瓜']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 8076

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 8139
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:55:56.218
- end: 2026-08-11T17:56:12.361
- duration_ms: 16142
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
- chunk_count: 83
- redacted_field: 3394
- total_duration_ms: 5026
- fallback_used: False

## Final Output
- answer_chars: 114
- answer_hash: decc8a1c9629b75a
- success: True

## Request Complete
- request_end: 2026-08-11T17:56:17.410
- request_duration_ms: 21193
- success: True
- final_source: generation

