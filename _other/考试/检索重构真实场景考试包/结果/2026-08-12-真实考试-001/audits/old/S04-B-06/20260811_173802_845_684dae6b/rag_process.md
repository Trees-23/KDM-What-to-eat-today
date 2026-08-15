# RAG Process

audit_id: 20260811_173802_845_684dae6b
timestamp: 2026-08-11T17:38:02.848
## Request
- original_query: 有鲤鱼可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 8a1c5e47abba7197
- session_id: 2026-08-12-真实考试-001:old:S04-B-06
- request_mode: stream
- request_start: 2026-08-11T17:38:02.849
- evaluation_sample_id: 20260811_173802_845_684dae6b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:38:02.850
- end: 2026-08-11T17:38:02.850
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:38:02.851
- end: 2026-08-11T17:38:02.851
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 8a1c5e47abba7197

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:38:02.852
- end: 2026-08-11T17:38:02.852
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: 8a1c5e47abba7197
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:38:02.853
- end: 2026-08-11T17:38:11.710
- duration_ms: 8857
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.5
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询的核心实体是“鲤鱼”（食材实体）。用户一方面希望获取可由鲤鱼制作的菜品，另一方面要求确认这些菜谱的配料表中确实包含鲤鱼，属于“食材—菜谱—配料”之间的中等强度关联检索与事实核验。无需多跳推理、因果分析或复杂对比分析；可通过关键词检索、菜谱标题召回、配料字段精确匹配及全文语义检索完成，因此推荐hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 104, 'graph_rag_count': 1, 'total_queries': 105}
- route_stats_after: {'traditional_count': 105, 'graph_rag_count': 1, 'total_queries': 106}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鲤鱼', '红烧鲤鱼', '糖醋鲤鱼', '清蒸鲤鱼', '鲤鱼汤', '鲤鱼炖豆腐', '水煮鲤鱼']
- topic_keywords: ['鱼类菜谱', '家常菜', '中式烹饪', '鲜味', '去腥']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2405

## Hybrid Branch Status / entity_level
- keywords: ['鲤鱼', '红烧鲤鱼', '糖醋鲤鱼', '清蒸鲤鱼', '鲤鱼汤', '鲤鱼炖豆腐', '水煮鲤鱼']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 33

## Hybrid Branch Status / topic_level
- keywords: ['鱼类菜谱', '家常菜', '中式烹饪', '鲜味', '去腥']
- requested_k: 10
- actual_count: 7
- fallback_count: 7
- duration_ms: 63

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 611

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 7
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 17
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 17436
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, 'Recipe': 1, 'Ingredient': 1, '汤类': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20466
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:38:02.853
- end: 2026-08-11T17:38:32.178
- duration_ms: 29325
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2636
- retrieval_levels: ['', 'entity']
- search_types: ['entity_level', 'vector_enhanced']
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
- chunk_count: 360
- redacted_field: 1993
- total_duration_ms: 9563
- fallback_used: False

## Final Output
- answer_chars: 462
- answer_hash: e5972b06f9c2fed5
- success: True

## Request Complete
- request_end: 2026-08-11T17:38:41.762
- request_duration_ms: 38912
- success: True
- final_source: generation

