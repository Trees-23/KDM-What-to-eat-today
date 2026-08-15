# RAG Process

audit_id: 20260811_174025_218_779479bf
timestamp: 2026-08-11T17:40:25.219
## Request
- original_query: 有玉米可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: b2eb3ae207313ef8
- session_id: 2026-08-12-真实考试-001:old:S04-B-09
- request_mode: stream
- request_start: 2026-08-11T17:40:25.219
- evaluation_sample_id: 20260811_174025_218_779479bf
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:40:25.220
- end: 2026-08-11T17:40:25.220
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:40:25.220
- end: 2026-08-11T17:40:25.220
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: b2eb3ae207313ef8

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:40:25.221
- end: 2026-08-11T17:40:25.221
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: b2eb3ae207313ef8
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:40:25.221
- end: 2026-08-11T17:40:34.887
- duration_ms: 9665
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.55
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是围绕明确食材实体“玉米”检索可制作的菜品，并筛选或验证菜谱配料表中确实包含玉米。该任务涉及“食材—菜谱”的关联和配料存在性校验，属于中等复杂度的信息检索与轻量筛选；不需要多跳推理、因果分析或复杂关系网络建模。适合使用关键词检索、菜谱字段/配料表过滤及语义召回来完成，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 107, 'graph_rag_count': 1, 'total_queries': 108}
- route_stats_after: {'traditional_count': 108, 'graph_rag_count': 1, 'total_queries': 109}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['玉米', '松仁玉米', '玉米排骨汤', '玉米烙', '玉米炒蛋', '玉米沙拉', '玉米饼', '玉米炒虾仁']
- topic_keywords: ['家常菜', '玉米菜谱', '快手菜', '汤品', '素食']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5899

## Hybrid Branch Status / entity_level
- keywords: ['玉米', '松仁玉米', '玉米排骨汤', '玉米烙', '玉米炒蛋', '玉米沙拉', '玉米饼', '玉米炒虾仁']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 19

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '玉米菜谱', '快手菜', '汤品', '素食']
- requested_k: 10
- actual_count: 6
- fallback_count: 6
- duration_ms: 30

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 294

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 6
- vector_count: 10
- origin_len: 19

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 19
- after_count: 16
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
- candidate_count: 16
- duration_ms: 12478
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '早餐': 1, '荤菜': 1, 'Recipe': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18685
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:40:25.221
- end: 2026-08-11T17:40:53.574
- duration_ms: 28352
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2052
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
- chunk_count: 1
- redacted_field: 14198
- total_duration_ms: 14199
- fallback_used: False

## Final Output
- answer_chars: 715
- answer_hash: 5d4e2cb014ce1eb6
- success: True

## Request Complete
- request_end: 2026-08-11T17:41:07.784
- request_duration_ms: 42565
- success: True
- final_source: generation

