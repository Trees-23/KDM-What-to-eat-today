# RAG Process

audit_id: 20260811_171033_396_97344a42
timestamp: 2026-08-11T17:10:33.397
## Request
- original_query: 我想学焯水，它的关键要点和适用场景是什么？
- original_query_hash: f544a0ddb9080fb2
- session_id: 2026-08-12-真实考试-001:old:S03-B-02
- request_mode: stream
- request_start: 2026-08-11T17:10:33.397
- evaluation_sample_id: 20260811_171033_396_97344a42
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:10:33.397
- end: 2026-08-11T17:10:33.397
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:10:33.398
- end: 2026-08-11T17:10:33.398
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: f544a0ddb9080fb2

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:10:33.398
- end: 2026-08-11T17:10:33.398
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: f544a0ddb9080fb2
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:10:33.398
- end: 2026-08-11T17:10:41.195
- duration_ms: 7796
- analysis_mode: llm
- query_complexity: 0.42
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询围绕“焯水”这一烹饪技法，要求获取其“关键要点”与“适用场景”。需要建立技法、操作要点、食材类别及使用目的之间的基本关联，并包含轻度因果判断（例如不同食材为何需要焯水、焯水如何去腥去杂质或控制口感）和有限对比（不同食材的焯水时长、冷水下锅与沸水下锅的区别）。但该任务本质上是结构化的知识说明与直接信息检索，不涉及跨领域、多实体、多跳的复杂关系网络推理。明确实体主要为“焯水”（烹饪技法）和“适用场景/食材”（烹饪应用类别），因此推荐使用 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 71, 'graph_rag_count': 0, 'total_queries': 71}
- route_stats_after: {'traditional_count': 72, 'graph_rag_count': 0, 'total_queries': 72}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['焯水']
- topic_keywords: ['烹饪技巧', '去腥', '去血沫', '去杂质', '定色', '保持口感', '预处理', '火候', '适用场景']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7394

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '去腥', '去血沫', '去杂质', '定色', '保持口感', '预处理', '火候', '适用场景']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 92

## Hybrid Branch Status / entity_level
- keywords: ['焯水']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 174

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 570

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 22
- duplicate_count: 8

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['去腥', '揭秘食材搭配的智慧：这些食物不宜同食']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 21784
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 2, 'TechniqueChunk': 2, '烹饪技巧': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 29800
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:10:33.398
- end: 2026-08-11T17:11:10.996
- duration_ms: 37597
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 6713
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
- chunk_count: 1166
- redacted_field: 4277
- total_duration_ms: 27790
- fallback_used: False

## Final Output
- answer_chars: 1499
- answer_hash: 56d94f303c603ac8
- success: True

## Request Complete
- request_end: 2026-08-11T17:11:38.813
- request_duration_ms: 65416
- success: True
- final_source: generation

