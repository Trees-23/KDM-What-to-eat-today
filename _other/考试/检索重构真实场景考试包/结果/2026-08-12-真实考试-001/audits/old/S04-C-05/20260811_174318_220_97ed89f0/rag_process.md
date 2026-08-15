# RAG Process

audit_id: 20260811_174318_220_97ed89f0
timestamp: 2026-08-11T17:43:18.220
## Request
- original_query: 蘑菇能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: 0686986f099d4633
- session_id: 2026-08-12-真实考试-001:old:S04-C-05
- request_mode: stream
- request_start: 2026-08-11T17:43:18.221
- evaluation_sample_id: 20260811_174318_220_97ed89f0
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:43:18.222
- end: 2026-08-11T17:43:18.222
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:43:18.223
- end: 2026-08-11T17:43:18.223
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 0686986f099d4633

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:43:18.224
- end: 2026-08-11T17:43:18.224
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 0686986f099d4633
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:43:18.225
- end: 2026-08-11T17:43:25.767
- duration_ms: 7542
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.78
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.92
- reasoning: 查询核心不是泛化地询问“蘑菇能做哪些菜”，而是要求仅返回知识图谱中存在明确“菜谱/菜品—使用食材—蘑菇”关系证据的结果，并禁止依据常识补全菜名。该任务需要从“蘑菇”实体出发，沿“被使用于/食材为/包含食材”等关系定位关联菜谱，再对关系证据进行约束和筛选。通常只需一跳或少量关系归一化推理，不需要因果分析或对比分析；但结果正确性高度依赖图关系的可追溯性，因此推荐 graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 5, 'total_queries': 114}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 6, 'total_queries': 115}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['蘑菇']
- target_entities: ['使用蘑菇的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 8175

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 8200
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:43:18.225
- end: 2026-08-11T17:43:33.969
- duration_ms: 15744
- selected_strategy: graph_rag
- document_count: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 0
- context_chars: 0
- retrieval_levels: []
- search_types: []
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
- chunk_count: 25
- redacted_field: 2632
- total_duration_ms: 3215
- fallback_used: False

## Final Output
- answer_chars: 34
- answer_hash: 6c2af0ff3a0f0753
- success: True

## Request Complete
- request_end: 2026-08-11T17:43:37.211
- request_duration_ms: 18990
- success: True
- final_source: generation

