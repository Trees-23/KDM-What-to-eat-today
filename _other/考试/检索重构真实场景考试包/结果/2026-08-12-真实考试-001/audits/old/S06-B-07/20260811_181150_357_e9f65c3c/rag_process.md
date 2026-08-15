# RAG Process

audit_id: 20260811_181150_357_e9f65c3c
timestamp: 2026-08-11T18:11:50.359
## Request
- original_query: 今天想吃面食，想要有味道一点，帮我找几个贴近这个需求的做法。
- original_query_hash: fdfa91900263ee52
- session_id: 2026-08-12-真实考试-001:old:S06-B-07
- request_mode: stream
- request_start: 2026-08-11T18:11:50.359
- evaluation_sample_id: 20260811_181150_357_e9f65c3c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:11:50.361
- end: 2026-08-11T18:11:50.361
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:11:50.361
- end: 2026-08-11T18:11:50.361
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 30
- enhanced_query_length: 30
- enhanced_query_hash: fdfa91900263ee52

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:11:50.362
- end: 2026-08-11T18:11:50.362
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 30
- analysis_input_query_hash: fdfa91900263ee52
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:11:50.362
- end: 2026-08-11T18:11:57.959
- duration_ms: 7597
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询目标是检索并推荐多个符合“面食”和“味道浓郁”偏好的做法，属于带有模糊偏好约束的中等简单检索任务。核心实体为“面食”和“做法”，“有味道一点”属于口味偏好/属性约束而非独立的复杂实体关系。需要进行轻量级语义理解与结果排序，例如优先召回酱香、麻辣、香辣、咖喱、肉酱、葱油等风味较浓的面食做法；但不需要多跳推理、因果分析或复杂关系图谱推理，因此推荐使用 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 133, 'graph_rag_count': 33, 'total_queries': 166}
- route_stats_after: {'traditional_count': 134, 'graph_rag_count': 33, 'total_queries': 167}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['面条', '炸酱面', '牛肉面', '油泼面', '葱油拌面', '担担面']
- topic_keywords: ['面食', '重口味', '咸香', '香辣', '浓郁', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8019

## Hybrid Branch Status / entity_level
- keywords: ['面条', '炸酱面', '牛肉面', '油泼面', '葱油拌面', '担担面']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 53

## Hybrid Branch Status / topic_level
- keywords: ['面食', '重口味', '咸香', '香辣', '浓郁', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 9
- duration_ms: 81

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 394

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 18
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 14192
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '荤菜': 2, '水产': 1}
- deferred_count: 8
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22646
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:11:50.362
- end: 2026-08-11T18:12:20.607
- duration_ms: 30245
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1283
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
- chunk_count: 870
- redacted_field: 1905
- total_duration_ms: 18538
- fallback_used: False

## Final Output
- answer_chars: 1143
- answer_hash: 984bc261cd9cb1fd
- success: True

## Request Complete
- request_end: 2026-08-11T18:12:39.172
- request_duration_ms: 48812
- success: True
- final_source: generation

