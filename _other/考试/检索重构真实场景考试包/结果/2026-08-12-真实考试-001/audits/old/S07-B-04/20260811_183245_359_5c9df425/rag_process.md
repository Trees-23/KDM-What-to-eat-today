# RAG Process

audit_id: 20260811_183245_359_5c9df425
timestamp: 2026-08-11T18:32:45.361
## Request
- original_query: 想找适合夏天的轻口味川菜，有哪些做法比较贴近这种偏好？
- original_query_hash: d978c6cfeb7a7fd9
- session_id: 2026-08-12-真实考试-001:old:S07-B-04
- request_mode: stream
- request_start: 2026-08-11T18:32:45.362
- evaluation_sample_id: 20260811_183245_359_5c9df425
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:32:45.363
- end: 2026-08-11T18:32:45.363
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:32:45.363
- end: 2026-08-11T18:32:45.363
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: d978c6cfeb7a7fd9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:32:45.364
- end: 2026-08-11T18:32:45.364
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: d978c6cfeb7a7fd9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:32:45.365
- end: 2026-08-11T18:32:56.707
- duration_ms: 11342
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.55
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询属于带偏好约束的菜谱推荐与做法检索：需要将“夏天”“轻口味”两个条件映射到川菜中较清爽、少油、低辣或酸辣开胃的菜品及烹饪方式。存在一定的属性匹配和对比筛选需求，例如区分传统重油重辣川菜与凉拌、清蒸、清炒、炝拌等更贴近夏季轻口味偏好的做法，但不涉及复杂的跨领域关系网络、深层因果链或多跳知识推理。因此适合使用hybrid_traditional，通过关键词检索、语义召回和菜谱标签过滤完成。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 159, 'graph_rag_count': 33, 'total_queries': 192}
- route_stats_after: {'traditional_count': 160, 'graph_rag_count': 33, 'total_queries': 193}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['凉拌鸡丝', '凉粉', '凉面', '泡菜', '清炒时蔬', '番茄', '黄瓜', '豆腐', '木耳', '花椒', '辣椒']
- topic_keywords: ['川菜', '夏季菜', '轻口味', '清淡', '凉拌菜', '开胃', '少油', '微辣', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3572

## Hybrid Branch Status / entity_level
- keywords: ['凉拌鸡丝', '凉粉', '凉面', '泡菜', '清炒时蔬', '番茄', '黄瓜', '豆腐', '木耳', '花椒', '辣椒']
- requested_k: 10
- actual_count: 8
- fallback_count: 0
- duration_ms: 42

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '夏季菜', '轻口味', '清淡', '凉拌菜', '开胃', '少油', '微辣', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 53

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 335

## Hybrid Branch Summary
- entity_count: 8
- topic_count: 10
- vector_count: 10
- origin_len: 28

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 28
- after_count: 25
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 26
- duration_ms: 21102
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'半成品': 1, '主食': 2, '荤菜': 1, '主食,凉菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 凉粉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25041
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:32:45.364
- end: 2026-08-11T18:33:21.749
- duration_ms: 36384
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4118
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
- chunk_count: 522
- redacted_field: 11202
- total_duration_ms: 28326
- fallback_used: False

## Final Output
- answer_chars: 661
- answer_hash: c95eb0a98f5046ad
- success: True

## Request Complete
- request_end: 2026-08-11T18:33:50.097
- request_duration_ms: 64735
- success: True
- final_source: generation

