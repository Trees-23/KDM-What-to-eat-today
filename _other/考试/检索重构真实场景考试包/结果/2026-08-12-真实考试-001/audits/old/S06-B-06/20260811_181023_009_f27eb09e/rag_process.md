# RAG Process

audit_id: 20260811_181023_009_f27eb09e
timestamp: 2026-08-11T18:10:23.012
## Request
- original_query: 想带便当，做什么相对合适，帮我找几个贴近这个需求的做法。
- original_query_hash: a5171b796d3628ba
- session_id: 2026-08-12-真实考试-001:old:S06-B-06
- request_mode: stream
- request_start: 2026-08-11T18:10:23.012
- evaluation_sample_id: 20260811_181023_009_f27eb09e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:10:23.013
- end: 2026-08-11T18:10:23.013
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:10:23.013
- end: 2026-08-11T18:10:23.013
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 28
- enhanced_query_length: 28
- enhanced_query_hash: a5171b796d3628ba

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:10:23.013
- end: 2026-08-11T18:10:23.013
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 28
- analysis_input_query_hash: a5171b796d3628ba
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:10:23.014
- end: 2026-08-11T18:10:31.529
- duration_ms: 8515
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询以“便当”为核心实体，目标是检索多个适合携带、保存和食用的菜品做法。需要结合便当场景下的隐含约束（如易携带、不易出水、冷却后口感、加热便利性、营养搭配等）进行筛选和轻度对比，但不涉及多个明确实体之间的复杂知识网络或多跳关系推理。适合采用hybrid_traditional，通过关键词检索、语义召回和基于便当适配度的结果排序来获取贴近需求的做法。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 132, 'graph_rag_count': 33, 'total_queries': 165}
- route_stats_after: {'traditional_count': 133, 'graph_rag_count': 33, 'total_queries': 166}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['便当', '鸡胸肉', '西兰花', '鸡蛋', '米饭', '胡萝卜', '土豆', '豆腐', '牛肉', '青椒']
- topic_keywords: ['便当菜', '午餐', '易携带', '耐放', '营养均衡', '快手菜', '荤素搭配', '食品安全']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7720

## Hybrid Branch Status / topic_level
- keywords: ['便当菜', '午餐', '易携带', '耐放', '营养均衡', '快手菜', '荤素搭配', '食品安全']
- requested_k: 10
- actual_count: 4
- fallback_count: 4
- duration_ms: 27

## Hybrid Branch Status / entity_level
- keywords: ['便当', '鸡胸肉', '西兰花', '鸡蛋', '米饭', '胡萝卜', '土豆', '豆腐', '牛肉', '青椒']
- requested_k: 10
- actual_count: 9
- fallback_count: 0
- duration_ms: 67

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 515

## Hybrid Branch Summary
- entity_count: 9
- topic_count: 4
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 22
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 14549
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 2, '烹饪技巧': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22810
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:10:23.014
- end: 2026-08-11T18:10:54.342
- duration_ms: 31327
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1764
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
- chunk_count: 1126
- redacted_field: 23610
- total_duration_ms: 55972
- fallback_used: False

## Final Output
- answer_chars: 1377
- answer_hash: 8c211e95d79b115a
- success: True

## Request Complete
- request_end: 2026-08-11T18:11:50.339
- request_duration_ms: 87327
- success: True
- final_source: generation

