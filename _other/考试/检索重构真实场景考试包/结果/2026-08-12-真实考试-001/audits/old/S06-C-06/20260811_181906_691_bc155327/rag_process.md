# RAG Process

audit_id: 20260811_181906_691_bc155327
timestamp: 2026-08-11T18:19:06.698
## Request
- original_query: 想找一道适合电饭煲的主食。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: 2abdc81fc47231d9
- session_id: 2026-08-12-真实考试-001:old:S06-C-06
- request_mode: stream
- request_start: 2026-08-11T18:19:06.698
- evaluation_sample_id: 20260811_181906_691_bc155327
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:19:06.699
- end: 2026-08-11T18:19:06.699
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:19:06.699
- end: 2026-08-11T18:19:06.699
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 43
- enhanced_query_length: 43
- enhanced_query_hash: 2abdc81fc47231d9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:19:06.700
- end: 2026-08-11T18:19:06.700
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 43
- analysis_input_query_hash: 2abdc81fc47231d9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:19:06.700
- end: 2026-08-11T18:19:20.050
- duration_ms: 13349
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.5
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询的核心是从资料中检索并筛选“适合电饭煲制作”的主食食谱，并抽取可验证的推荐依据（如食谱明确标注使用电饭煲、烹饪步骤和所需模式）。需要进行轻量级的条件匹配与证据归纳，但不涉及跨多实体的复杂关系网络或多跳知识发现。查询还明确要求区分资料支持的事实与推测，因此应优先检索包含设备适配说明和明确制作步骤的权威食谱来源；若资料未说明适配性，不应将其表述为确定事实。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 142, 'graph_rag_count': 33, 'total_queries': 175}
- route_stats_after: {'traditional_count': 143, 'graph_rag_count': 33, 'total_queries': 176}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['电饭煲']
- topic_keywords: ['主食', '电饭煲烹饪']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3921

## Hybrid Branch Status / entity_level
- keywords: ['电饭煲']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / topic_level
- keywords: ['主食', '电饭煲烹饪']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 55

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 622

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 10
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 16
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['蒸（米）/炖（使用电饭煲/高压锅/电压力锅）', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 18342
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '烹饪技巧': 2, '荤菜': 1}
- deferred_count: 12
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22907
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:19:06.700
- end: 2026-08-11T18:19:42.958
- duration_ms: 36257
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2880
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 209
- redacted_field: 1677
- total_duration_ms: 5983
- fallback_used: False

## Final Output
- answer_chars: 282
- answer_hash: fa7b217c34ed0f80
- success: True

## Request Complete
- request_end: 2026-08-11T18:19:48.963
- request_duration_ms: 42264
- success: True
- final_source: generation

