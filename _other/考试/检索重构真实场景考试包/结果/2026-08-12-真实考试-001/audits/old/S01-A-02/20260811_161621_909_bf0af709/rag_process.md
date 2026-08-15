# RAG Process

audit_id: 20260811_161621_909_bf0af709
timestamp: 2026-08-11T16:16:21.909
## Request
- original_query: 请给出油焖大虾的完整做法，包括主要食材和步骤。
- original_query_hash: baf5975e093e69e6
- session_id: 2026-08-12-真实考试-001:old:S01-A-02
- request_mode: stream
- request_start: 2026-08-11T16:16:21.910
- evaluation_sample_id: 20260811_161621_909_bf0af709
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:16:21.911
- end: 2026-08-11T16:16:21.911
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:16:21.912
- end: 2026-08-11T16:16:21.912
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: baf5975e093e69e6

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:16:21.912
- end: 2026-08-11T16:16:21.912
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: baf5975e093e69e6
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:16:21.913
- end: 2026-08-11T16:16:29.457
- duration_ms: 7544
- analysis_mode: llm
- query_complexity: 0.22
- relationship_intensity: 0.18
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是针对单一道菜“油焖大虾”的直接操作型信息请求，核心目标是获取主要食材及线性烹饪步骤。虽然食材与步骤之间存在基本的组成和顺序关系，但不涉及跨实体的复杂关联、多跳推理、因果解释或方案对比。适合通过关键词检索、菜谱文档召回及排序的hybrid_traditional策略完成。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 1, 'graph_rag_count': 0, 'total_queries': 1}
- route_stats_after: {'traditional_count': 2, 'graph_rag_count': 0, 'total_queries': 2}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['油焖大虾', '大虾', '葱', '姜', '蒜', '料酒', '生抽', '白糖', '盐', '食用油']
- topic_keywords: ['鲁菜', '家常菜', '海鲜', '油焖', '去腥', '入味', '火候', '鲜香']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8879

## Hybrid Branch Status / entity_level
- keywords: ['油焖大虾', '大虾', '葱', '姜', '蒜', '料酒', '生抽', '白糖', '盐', '食用油']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 56

## Hybrid Branch Status / topic_level
- keywords: ['鲁菜', '家常菜', '海鲜', '油焖', '去腥', '入味', '火候', '鲜香']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 89

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 523

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 28
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
- candidate_count: 28
- duration_ms: 26837
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'水产': 2, '荤菜': 2, 'Ingredient': 1}
- deferred_count: 7
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 36267
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:16:21.912
- end: 2026-08-11T16:17:05.725
- duration_ms: 43812
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2451
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
- chunk_count: 424
- redacted_field: 6200
- total_duration_ms: 16256
- fallback_used: False

## Final Output
- answer_chars: 548
- answer_hash: c32457569945edb7
- success: True

## Request Complete
- request_end: 2026-08-11T16:17:22.000
- request_duration_ms: 60090
- success: True
- final_source: generation

