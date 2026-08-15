# RAG Process

audit_id: 20260811_175535_772_e55a0819
timestamp: 2026-08-11T17:55:35.773
## Request
- original_query: 做黄瓜相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: 92b5208ca3dbaba4
- session_id: 2026-08-12-真实考试-001:old:S05-B-10
- request_mode: stream
- request_start: 2026-08-11T17:55:35.773
- evaluation_sample_id: 20260811_175535_772_e55a0819
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:55:35.774
- end: 2026-08-11T17:55:35.774
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:55:35.774
- end: 2026-08-11T17:55:35.774
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 92b5208ca3dbaba4

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:55:35.775
- end: 2026-08-11T17:55:35.775
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 92b5208ca3dbaba4
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:55:35.776
- end: 2026-08-11T17:55:44.436
- duration_ms: 8660
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.62
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.88
- reasoning: 查询核心是从知识图谱中检索“黄瓜”与其他“蔬菜”之间的菜品搭配关系，属于以单一核心实体为中心的一跳关系扩展与结果枚举。通常不需要多跳推理、因果分析或对比分析，但需要识别“黄瓜”实体、限定搭配对象为“蔬菜”类型，并沿“可搭配/常搭配”等关系边进行图谱查询，因此推荐使用graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 20, 'total_queries': 139}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 21, 'total_queries': 140}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['黄瓜']
- target_entities: ['与黄瓜共同用于菜谱的蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 6360

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 6585
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:55:35.776
- end: 2026-08-11T17:55:51.022
- duration_ms: 15245
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 968
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
- chunk_count: 142
- redacted_field: 2048
- total_duration_ms: 5159
- fallback_used: False

## Final Output
- answer_chars: 199
- answer_hash: 5bde29bb140d72dd
- success: True

## Request Complete
- request_end: 2026-08-11T17:55:56.207
- request_duration_ms: 20433
- success: True
- final_source: generation

