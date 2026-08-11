# RAG Process

audit_id: 20260811_174236_719_326c9d34
timestamp: 2026-08-11T17:42:36.721
## Request
- original_query: 黄瓜能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: d27ed852fdc08588
- session_id: 2026-08-12-真实考试-001:old:S04-C-03
- request_mode: stream
- request_start: 2026-08-11T17:42:36.721
- evaluation_sample_id: 20260811_174236_719_326c9d34
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:42:36.721
- end: 2026-08-11T17:42:36.721
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:42:36.722
- end: 2026-08-11T17:42:36.722
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: d27ed852fdc08588

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:42:36.722
- end: 2026-08-11T17:42:36.722
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: d27ed852fdc08588
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:42:36.722
- end: 2026-08-11T17:42:44.398
- duration_ms: 7675
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.68
- reasoning_required: True
- entity_count: 1
- strategy: graph_rag
- confidence: 0.9
- reasoning: 查询的核心实体是“黄瓜”（食材实体），目标是检索与其存在明确“食材-用于-菜谱”关系的菜谱实体。查询显式要求“只列出图关系能够证明使用了它的菜谱”，因此结果必须受知识图谱中可验证的边约束，不能依赖语言模型常识、模糊文本匹配或缺乏关系证据的候选菜名。该任务通常可通过从“黄瓜”节点沿“使用于/包含食材/主料为”等关系遍历至“菜谱”节点完成，属于关系约束型检索；不要求因果分析或对比分析，多跳推理通常非必要，但需要进行关系类型筛选、证据校验和去除无图关系支持的结果。因此推荐 graph_rag。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 3, 'total_queries': 112}
- route_stats_after: {'traditional_count': 109, 'graph_rag_count': 4, 'total_queries': 113}

## Graph Query Understanding
- query_type: entity_relation
- source_entities: ['黄瓜']
- target_entities: ['使用黄瓜的菜谱']
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- normalized_relation_types: ['REQUIRES']
- max_depth: 1
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 5953

## Graph Path Retrieval Config
- max_depth: 1
- target_labels: ['Recipe']
- relation_types: ['REQUIRES']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 6007
- mode: path
- path_count: 0
- final_count: 0

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:42:36.722
- end: 2026-08-11T17:42:50.407
- duration_ms: 13684
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
- chunk_count: 23
- redacted_field: 4385
- total_duration_ms: 4821
- fallback_used: False

## Final Output
- answer_chars: 33
- answer_hash: 4eccf6af25fb5a93
- success: True

## Request Complete
- request_end: 2026-08-11T17:42:55.268
- request_duration_ms: 18546
- success: True
- final_source: generation

