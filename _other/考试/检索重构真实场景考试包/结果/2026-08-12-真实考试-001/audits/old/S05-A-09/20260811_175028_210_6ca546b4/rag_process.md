# RAG Process

audit_id: 20260811_175028_210_6ca546b4
timestamp: 2026-08-11T17:50:28.213
## Request
- original_query: 鲈鱼适合搭配什么蔬菜？
- original_query_hash: 71cf7a42929c2955
- session_id: 2026-08-12-真实考试-001:old:S05-A-09
- request_mode: stream
- request_start: 2026-08-11T17:50:28.213
- evaluation_sample_id: 20260811_175028_210_6ca546b4
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:50:28.214
- end: 2026-08-11T17:50:28.214
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:50:28.215
- end: 2026-08-11T17:50:28.215
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 71cf7a42929c2955

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:50:28.215
- end: 2026-08-11T17:50:28.215
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 11
- analysis_input_query_hash: 71cf7a42929c2955
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:50:28.216
- end: 2026-08-11T17:50:34.262
- duration_ms: 6046
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.55
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询是围绕“鲈鱼”与“蔬菜”之间搭配关系的直接信息检索需求。虽然需要基于口味、烹饪方式、营养均衡或食材相容性给出若干搭配建议，但通常不要求跨多个知识节点进行多跳推理，也不涉及复杂因果链或系统性对比。明确实体包括“鲈鱼”（食材/鱼类）和“蔬菜”（食材类别）。采用关键词检索、语义检索及菜谱/食材搭配知识库召回的 hybrid_traditional 策略即可有效满足需求。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 117, 'graph_rag_count': 11, 'total_queries': 128}
- route_stats_after: {'traditional_count': 118, 'graph_rag_count': 11, 'total_queries': 129}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鲈鱼', '芦笋', '西兰花', '菠菜', '娃娃菜', '番茄', '蘑菇', '胡萝卜']
- topic_keywords: ['蔬菜搭配', '鱼类搭配', '清淡', '营养均衡', '蒸鱼', '煎鱼', '去腥']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6512

## Hybrid Branch Status / entity_level
- keywords: ['鲈鱼', '芦笋', '西兰花', '菠菜', '娃娃菜', '番茄', '蘑菇', '胡萝卜']
- requested_k: 10
- actual_count: 7
- fallback_count: 0
- duration_ms: 71

## Hybrid Branch Status / topic_level
- keywords: ['蔬菜搭配', '鱼类搭配', '清淡', '营养均衡', '蒸鱼', '煎鱼', '去腥']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 77

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 485

## Hybrid Branch Summary
- entity_count: 7
- topic_count: 10
- vector_count: 10
- origin_len: 27

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 27
- after_count: 24
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 8
- doc_names: ['揭秘食材搭配的智慧：这些食物不宜同食', '如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 25
- duration_ms: 16213
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '主食': 1, '通用知识': 1, '烹饪技巧': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23233
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:50:28.215
- end: 2026-08-11T17:50:57.497
- duration_ms: 29281
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4785
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
- chunk_count: 317
- redacted_field: 4072
- total_duration_ms: 15976
- fallback_used: False

## Final Output
- answer_chars: 383
- answer_hash: 257b683599b44780
- success: True

## Request Complete
- request_end: 2026-08-11T17:51:13.484
- request_duration_ms: 45270
- success: True
- final_source: generation

