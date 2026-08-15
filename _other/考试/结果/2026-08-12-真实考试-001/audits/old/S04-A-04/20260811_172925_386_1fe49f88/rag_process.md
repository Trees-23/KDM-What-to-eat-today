# RAG Process

audit_id: 20260811_172925_386_1fe49f88
timestamp: 2026-08-11T17:29:25.387
## Request
- original_query: 家里有鸡蛋，知识库里能做哪些菜？
- original_query_hash: 6936e0106f1293ae
- session_id: 2026-08-12-真实考试-001:old:S04-A-04
- request_mode: stream
- request_start: 2026-08-11T17:29:25.387
- evaluation_sample_id: 20260811_172925_386_1fe49f88
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:29:25.388
- end: 2026-08-11T17:29:25.388
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:29:25.388
- end: 2026-08-11T17:29:25.388
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 16
- enhanced_query_length: 16
- enhanced_query_hash: 6936e0106f1293ae

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:29:25.388
- end: 2026-08-11T17:29:25.388
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 16
- analysis_input_query_hash: 6936e0106f1293ae
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:29:25.389
- end: 2026-08-11T17:29:33.071
- duration_ms: 7682
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.4
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询的核心是以“鸡蛋”这一食材实体为条件，从知识库中检索包含该食材或以其为主要原料的菜谱。该任务主要涉及“食材—菜品”的直接关联与条件过滤，不需要多跳推理、因果分析或多方案对比。可通过关键词检索、食材字段过滤及语义召回实现，适合使用 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 92, 'graph_rag_count': 1, 'total_queries': 93}
- route_stats_after: {'traditional_count': 93, 'graph_rag_count': 1, 'total_queries': 94}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鸡蛋', '西红柿炒鸡蛋', '鸡蛋羹', '煎蛋', '炒鸡蛋', '蛋炒饭']
- topic_keywords: ['家常菜', '快手菜', '鸡蛋料理']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5356

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '快手菜', '鸡蛋料理']
- requested_k: 10
- actual_count: 6
- fallback_count: 6
- duration_ms: 53

## Hybrid Branch Status / entity_level
- keywords: ['鸡蛋', '西红柿炒鸡蛋', '鸡蛋羹', '煎蛋', '炒鸡蛋', '蛋炒饭']
- requested_k: 10
- actual_count: 5
- fallback_count: 0
- duration_ms: 57

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 389

## Hybrid Branch Summary
- entity_count: 5
- topic_count: 6
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 19
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 19
- duration_ms: 12503
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'Ingredient': 1, '主食': 2, '水产': 1, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18269
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:29:25.389
- end: 2026-08-11T17:29:51.342
- duration_ms: 25953
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1536
- retrieval_levels: ['', 'entity', 'topic']
- search_types: ['entity_level', 'topic_level', 'vector_enhanced']
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
- chunk_count: 267
- redacted_field: 5538
- total_duration_ms: 11095
- fallback_used: False

## Final Output
- answer_chars: 345
- answer_hash: e489e90e36baff33
- success: True

## Request Complete
- request_end: 2026-08-11T17:30:02.454
- request_duration_ms: 37067
- success: True
- final_source: generation

