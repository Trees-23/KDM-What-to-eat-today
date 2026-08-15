# RAG Process

audit_id: 20260811_180631_775_767494bc
timestamp: 2026-08-11T18:06:31.777
## Request
- original_query: 天气冷想喝一碗暖和的汤，帮我找几个贴近这个需求的做法。
- original_query_hash: 4742dd10be3535ce
- session_id: 2026-08-12-真实考试-001:old:S06-B-01
- request_mode: stream
- request_start: 2026-08-11T18:06:31.778
- evaluation_sample_id: 20260811_180631_775_767494bc
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:06:31.779
- end: 2026-08-11T18:06:31.779
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:06:31.780
- end: 2026-08-11T18:06:31.780
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 4742dd10be3535ce

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:06:31.780
- end: 2026-08-11T18:06:31.780
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 4742dd10be3535ce
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:06:31.781
- end: 2026-08-11T18:06:40.347
- duration_ms: 8566
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.35
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带有场景偏好约束的食谱推荐需求：用户以“天气冷”为环境条件，希望获得“暖和的汤”的多个做法。核心检索目标是匹配具有温热、易制作、适合冷天食用等语义标签的汤类菜谱，不涉及复杂的实体关系网络或跨领域知识推理。无需多跳推理、因果分析或严格的对比分析，但可在结果排序阶段根据食材易得性、烹饪时长、口味和滋补属性进行轻量筛选。明确实体主要包括“天气冷”（场景/环境条件）和“暖和的汤”（菜品类别及口味温度偏好）。建议采用 hybrid_traditional，通过关键词检索（如暖汤、冬季汤、热汤、家常汤）结合向量语义召回来覆盖表达相近的食谱内容。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 127, 'graph_rag_count': 33, 'total_queries': 160}
- route_stats_after: {'traditional_count': 128, 'graph_rag_count': 33, 'total_queries': 161}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸡汤', '排骨汤', '番茄鸡蛋汤', '菌菇豆腐汤', '牛肉汤']
- topic_keywords: ['汤品', '暖胃', '冬季饮食', '家常菜', '滋补']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5766

## Hybrid Branch Status / entity_level
- keywords: ['鸡汤', '排骨汤', '番茄鸡蛋汤', '菌菇豆腐汤', '牛肉汤']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 11

## Hybrid Branch Status / topic_level
- keywords: ['汤品', '暖胃', '冬季饮食', '家常菜', '滋补']
- requested_k: 10
- actual_count: 3
- fallback_count: 3
- duration_ms: 17

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 557

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 3
- vector_count: 10
- origin_len: 14

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 14
- after_count: 14
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 11700
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 1, '汤类': 2, '荤菜': 1, '饮料': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18041
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:06:31.781
- end: 2026-08-11T18:06:58.390
- duration_ms: 26609
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1482
- retrieval_levels: ['', 'topic']
- search_types: ['topic_level', 'vector_enhanced']
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
- chunk_count: 470
- redacted_field: 1411
- total_duration_ms: 14578
- fallback_used: False

## Final Output
- answer_chars: 628
- answer_hash: e3415d105f49314b
- success: True

## Request Complete
- request_end: 2026-08-11T18:07:12.990
- request_duration_ms: 41212
- success: True
- final_source: generation

