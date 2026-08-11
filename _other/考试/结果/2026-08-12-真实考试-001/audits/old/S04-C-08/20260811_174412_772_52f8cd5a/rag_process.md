# RAG Process

audit_id: 20260811_174412_772_52f8cd5a
timestamp: 2026-08-11T17:44:12.774
## Request
- original_query: 南瓜能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: c2c56607eb3c9bd1
- session_id: 2026-08-12-真实考试-001:old:S04-C-08
- request_mode: stream
- request_start: 2026-08-11T17:44:12.774
- evaluation_sample_id: 20260811_174412_772_52f8cd5a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:44:12.775
- end: 2026-08-11T17:44:12.775
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:44:12.775
- end: 2026-08-11T17:44:12.775
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: c2c56607eb3c9bd1

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:44:12.776
- end: 2026-08-11T17:44:12.776
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: c2c56607eb3c9bd1
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:44:12.776
- end: 2026-08-11T17:44:25.239
- duration_ms: 12462
- analysis_mode: llm
- query_complexity: 0.68
- relationship_intensity: 0.72
- reasoning_required: True
- entity_count: 1
- strategy: graph_rag
- confidence: 0.9
- reasoning: 查询的核心实体是“南瓜”，目标是检索与其存在明确“食材-菜谱使用”关系的菜谱实体，并要求结果必须由图关系证据证明，禁止依据常识或文本语义补全菜名。因此需要沿知识图谱中的“菜谱-使用食材-南瓜”关系进行约束检索、过滤和证据校验。通常不需要因果分析或对比分析，但需要至少一跳的关系遍历与关系真实性验证；传统混合检索可能召回含有南瓜相关描述但未建立明确食材关系的菜谱，难以满足严格证据要求。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 8, 'total_queries': 117}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 9, 'total_queries': 118}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['南瓜']
- target_entities: ['使用南瓜的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5587

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 5619
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:44:12.776
- end: 2026-08-11T17:44:30.859
- duration_ms: 18082
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
- redacted_field: 3358
- total_duration_ms: 3805
- fallback_used: False

## Final Output
- answer_chars: 34
- answer_hash: 0d9a69bcf5818cc2
- success: True

## Request Complete
- request_end: 2026-08-11T17:44:34.694
- request_duration_ms: 21920
- success: True
- final_source: generation

