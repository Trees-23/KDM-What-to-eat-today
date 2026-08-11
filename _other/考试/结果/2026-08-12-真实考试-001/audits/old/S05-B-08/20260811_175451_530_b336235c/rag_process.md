# RAG Process

audit_id: 20260811_175451_530_b336235c
timestamp: 2026-08-11T17:54:51.532
## Request
- original_query: 做玉米相关菜时，知识图谱里有哪些蔬菜搭配？
- original_query_hash: 06b00905cb35f39d
- session_id: 2026-08-12-真实考试-001:old:S05-B-08
- request_mode: stream
- request_start: 2026-08-11T17:54:51.533
- evaluation_sample_id: 20260811_175451_530_b336235c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:54:51.534
- end: 2026-08-11T17:54:51.534
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:54:51.534
- end: 2026-08-11T17:54:51.534
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 06b00905cb35f39d

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:54:51.535
- end: 2026-08-11T17:54:51.535
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 06b00905cb35f39d
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:54:51.535
- end: 2026-08-11T17:54:59.016
- duration_ms: 7481
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.65
- reasoning_required: True
- entity_count: 2
- strategy: graph_rag
- confidence: 0.88
- reasoning: 查询的核心是从知识图谱中查找实体“玉米”与蔬菜类别实体之间的“适合搭配/可共同烹饪”关系，并返回其关联的蔬菜实体列表。该任务主要需要一跳关系检索，通常不需要多跳推理、因果分析或显式对比分析；但由于问题明确要求基于知识图谱发现搭配关系，使用graph_rag能够更准确地遍历“玉米—搭配—蔬菜”的图谱边，并支持按菜系、烹饪方式或搭配强度等关系属性进行扩展筛选。

## Routing Decision
- selected_strategy: graph_rag
- top_k: 5
- route_stats_before: {'traditional_count': 119, 'graph_rag_count': 18, 'total_queries': 137}
- route_stats_after: {'traditional_count': 119, 'graph_rag_count': 19, 'total_queries': 138}

## Graph Query Understanding
- query_type: multi_hop
- source_entities: ['玉米']
- target_entities: ['蔬菜类食材']
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- normalized_relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- max_depth: 3
- max_nodes: 50
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 1000
- duration_ms: 7519

## Graph Path Retrieval Config
- max_depth: 3
- target_labels: ['Ingredient']
- relation_types: ['REQUIRES', 'BELONGS_TO_CATEGORY']
- cypher_template_hash: graph_path_v1
- limit: 20

## Graph Retrieval Complete
- graph_total_duration_ms: 7913
- mode: path
- path_count: 20
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:54:51.535
- end: 2026-08-11T17:55:06.930
- duration_ms: 15395
- selected_strategy: graph_rag
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 899
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
- chunk_count: 127
- redacted_field: 2487
- total_duration_ms: 4967
- fallback_used: False

## Final Output
- answer_chars: 175
- answer_hash: b35935bbf65d6028
- success: True

## Request Complete
- request_end: 2026-08-11T17:55:11.911
- request_duration_ms: 20377
- success: True
- final_source: generation

