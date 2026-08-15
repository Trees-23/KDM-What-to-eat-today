# RAG Process

audit_id: 20260811_173002_465_93305a07
timestamp: 2026-08-11T17:30:02.466
## Request
- original_query: 家里有豆腐，知识库里能做哪些菜？
- original_query_hash: 03397afd8fd78bff
- session_id: 2026-08-12-真实考试-001:old:S04-A-05
- request_mode: stream
- request_start: 2026-08-11T17:30:02.467
- evaluation_sample_id: 20260811_173002_465_93305a07
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:30:02.467
- end: 2026-08-11T17:30:02.467
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:30:02.467
- end: 2026-08-11T17:30:02.467
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 03397afd8fd78bff

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:30:02.468
- end: 2026-08-11T17:30:02.468
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 03397afd8fd78bff
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:30:02.468
- end: 2026-08-11T17:30:12.168
- duration_ms: 9700
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.45
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询的核心明确实体是“豆腐”（食材类实体）。“知识库”属于检索范围约束，而非菜谱领域实体。用户意图是从知识库中筛选、召回包含豆腐或以豆腐为主要食材的菜谱，属于基于单一食材与菜品之间关联的条件检索。该任务不需要多跳推理、因果分析或菜品间对比，只需通过关键词检索、食材字段过滤及语义召回来匹配相关菜谱，因此推荐使用 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 93, 'graph_rag_count': 1, 'total_queries': 94}
- route_stats_after: {'traditional_count': 94, 'graph_rag_count': 1, 'total_queries': 95}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['豆腐', '麻婆豆腐', '家常豆腐', '红烧豆腐', '豆腐汤', '凉拌豆腐']
- topic_keywords: ['豆腐菜', '家常菜', '素食', '快手菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5558

## Hybrid Branch Status / entity_level
- keywords: ['豆腐', '麻婆豆腐', '家常豆腐', '红烧豆腐', '豆腐汤', '凉拌豆腐']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 46

## Hybrid Branch Status / topic_level
- keywords: ['豆腐菜', '家常菜', '素食', '快手菜']
- requested_k: 10
- actual_count: 6
- fallback_count: 6
- duration_ms: 50

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 517

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 6
- vector_count: 10
- origin_len: 19

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 19
- after_count: 14
- duplicate_count: 5

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
- duration_ms: 15153
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '素菜': 2, '主食': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21241
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:30:02.468
- end: 2026-08-11T17:30:33.410
- duration_ms: 30942
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3085
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
- chunk_count: 1
- redacted_field: 12432
- total_duration_ms: 12434
- fallback_used: False

## Final Output
- answer_chars: 358
- answer_hash: 5ea0908631da3af1
- success: True

## Request Complete
- request_end: 2026-08-11T17:30:45.854
- request_duration_ms: 43387
- success: True
- final_source: generation

