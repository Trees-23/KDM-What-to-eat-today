# RAG Process

audit_id: 20260811_165141_491_0f966cc5
timestamp: 2026-08-11T16:51:41.493
## Request
- original_query: 刚开始做红烧鲤鱼时，第一步具体要处理什么？
- original_query_hash: 5aebadeb3cdb8d77
- session_id: 2026-08-12-真实考试-001:old:S02-B-09
- request_mode: stream
- request_start: 2026-08-11T16:51:41.493
- evaluation_sample_id: 20260811_165141_491_0f966cc5
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:51:41.494
- end: 2026-08-11T16:51:41.494
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:51:41.495
- end: 2026-08-11T16:51:41.495
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 5aebadeb3cdb8d77

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:51:41.495
- end: 2026-08-11T16:51:41.495
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 5aebadeb3cdb8d77
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:51:41.495
- end: 2026-08-11T16:51:49.957
- duration_ms: 8462
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对菜谱制作流程中“起始步骤”的直接定位，核心是从红烧鲤鱼的做法文本中检索并提取第一步操作。无需多跳推理、因果分析或方案对比。明确实体包括“红烧鲤鱼”（菜品）和“第一步/刚开始”（流程阶段或步骤位置）；“具体要处理什么”属于操作内容询问。适合采用关键词检索、语义检索及步骤排序提取的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 48, 'graph_rag_count': 0, 'total_queries': 48}
- route_stats_after: {'traditional_count': 49, 'graph_rag_count': 0, 'total_queries': 49}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['红烧鲤鱼', '鲤鱼']
- topic_keywords: ['红烧', '烹饪技巧', '鱼类处理', '去腥', '清洗']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6887

## Hybrid Branch Status / entity_level
- keywords: ['红烧鲤鱼', '鲤鱼']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / topic_level
- keywords: ['红烧', '烹饪技巧', '鱼类处理', '去腥', '清洗']
- requested_k: 10
- actual_count: 9
- fallback_count: 9
- duration_ms: 52

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 572

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 9
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 18
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
- candidate_count: 18
- duration_ms: 16824
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '汤类': 1, '早餐': 1, '荤菜': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24298
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:51:41.495
- end: 2026-08-11T16:52:14.257
- duration_ms: 32761
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3492
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
- chunk_count: 37
- redacted_field: 1918
- total_duration_ms: 2749
- fallback_used: False

## Final Output
- answer_chars: 44
- answer_hash: 9408aa547528e698
- success: True

## Request Complete
- request_end: 2026-08-11T16:52:17.019
- request_duration_ms: 35525
- success: True
- final_source: generation

