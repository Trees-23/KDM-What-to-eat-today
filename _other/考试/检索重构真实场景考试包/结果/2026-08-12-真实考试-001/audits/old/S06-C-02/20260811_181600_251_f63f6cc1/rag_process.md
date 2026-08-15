# RAG Process

audit_id: 20260811_181600_251_f63f6cc1
timestamp: 2026-08-11T18:16:00.260
## Request
- original_query: 想做一道适合夏天的凉菜。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: c2268069bb0a9925
- session_id: 2026-08-12-真实考试-001:old:S06-C-02
- request_mode: stream
- request_start: 2026-08-11T18:16:00.260
- evaluation_sample_id: 20260811_181600_251_f63f6cc1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:16:00.262
- end: 2026-08-11T18:16:00.262
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:16:00.263
- end: 2026-08-11T18:16:00.263
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 42
- enhanced_query_length: 42
- enhanced_query_hash: c2268069bb0a9925

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:16:00.263
- end: 2026-08-11T18:16:00.263
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 42
- analysis_input_query_hash: c2268069bb0a9925
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:16:00.264
- end: 2026-08-11T18:16:08.767
- duration_ms: 8502
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.56
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询目标是根据“夏天”和“凉菜”两个条件推荐菜品，并明确要求展示推荐依据、避免将无资料支撑的推测表述为事实。该任务需要检索菜谱、食材特性、时令或适宜食用场景等证据，并对候选凉菜进行有限的匹配与对比。虽然存在“季节—菜品—食材/口感/烹饪方式—依据”的关系，但关系网络规模有限，不需要复杂的跨实体图谱发现或深层多跳推理。更适合采用 hybrid_traditional，通过关键词、语义检索和来源排序召回可靠资料，再基于明确证据生成带依据的推荐；对于资料未明确支持的部分，应标记为建议或不予断言。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 138, 'graph_rag_count': 33, 'total_queries': 171}
- route_stats_after: {'traditional_count': 139, 'graph_rag_count': 33, 'total_queries': 172}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['凉菜']
- topic_keywords: ['夏季', '清爽', '冷菜', '推荐依据', '资料支持']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3608

## Hybrid Branch Status / entity_level
- keywords: ['凉菜']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / topic_level
- keywords: ['夏季', '清爽', '冷菜', '推荐依据', '资料支持']
- requested_k: 10
- actual_count: 1
- fallback_count: 1
- duration_ms: 11

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 409

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 1
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 6
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['如何决策吃什么', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 7
- duration_ms: 10771
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'半成品': 1, '烹饪技巧': 2, '主食': 1, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 14814
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:16:00.264
- end: 2026-08-11T18:16:23.582
- duration_ms: 23318
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2158
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
- chunk_count: 333
- redacted_field: 2580
- total_duration_ms: 9368
- fallback_used: False

## Final Output
- answer_chars: 424
- answer_hash: b1f17691778ac328
- success: True

## Request Complete
- request_end: 2026-08-11T18:16:32.971
- request_duration_ms: 32710
- success: True
- final_source: generation

