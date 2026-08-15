# RAG Process

audit_id: 20260811_170803_291_798a175a
timestamp: 2026-08-11T17:08:03.293
## Request
- original_query: 请说明“使用微波炉”这个技巧的关键要点和适用情形。
- original_query_hash: 8fb2eed441a31645
- session_id: 2026-08-12-真实考试-001:old:S03-A-09
- request_mode: stream
- request_start: 2026-08-11T17:08:03.293
- evaluation_sample_id: 20260811_170803_291_798a175a
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:08:03.294
- end: 2026-08-11T17:08:03.294
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:08:03.294
- end: 2026-08-11T17:08:03.294
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: 8fb2eed441a31645

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:08:03.294
- end: 2026-08-11T17:08:03.294
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: 8fb2eed441a31645
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:08:03.295
- end: 2026-08-11T17:08:11.995
- duration_ms: 8700
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.35
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心实体为“微波炉（使用技巧）”，目标是获取其操作关键要点及适用情形。需要将安全规范、加热原理、食物/容器类型与具体使用场景进行条件匹配，因此存在轻度的条件性推理和因果判断（例如某类容器为何不适用、不同食物为何需调整时间或功率）。但不涉及多个实体构成的复杂关系网络，也不要求多跳知识发现或跨主题对比，适合采用关键词检索、语义检索与结果重排序相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 68, 'graph_rag_count': 0, 'total_queries': 68}
- route_stats_after: {'traditional_count': 69, 'graph_rag_count': 0, 'total_queries': 69}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['微波炉', '微波加热']
- topic_keywords: ['烹饪技巧', '快速加热', '解冻', '复热', '蒸煮', '食品安全', '受热均匀']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8738

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '快速加热', '解冻', '复热', '蒸煮', '食品安全', '受热均匀']
- requested_k: 10
- actual_count: 1
- fallback_count: 1
- duration_ms: 26

## Hybrid Branch Status / entity_level
- keywords: ['微波炉', '微波加热']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 110

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 453

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 1
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 13
- duplicate_count: 8

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['使用微波炉', '厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 15645
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, 'TechniqueDoc': 2, 'TechniqueChunk': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24894
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:08:03.295
- end: 2026-08-11T17:08:36.891
- duration_ms: 33596
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6339
- retrieval_levels: ['context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion']
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
- chunk_count: 750
- redacted_field: 3140
- total_duration_ms: 17736
- fallback_used: False

## Final Output
- answer_chars: 968
- answer_hash: 6af2af5ec9c55fa5
- success: True

## Request Complete
- request_end: 2026-08-11T17:08:54.648
- request_duration_ms: 51354
- success: True
- final_source: generation

