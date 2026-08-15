# RAG Process

audit_id: 20260811_182927_346_9235f07d
timestamp: 2026-08-11T18:29:27.347
## Request
- original_query: 想吃口感清爽的川味凉菜，有哪些做法比较贴近这种偏好？
- original_query_hash: 1c9d78a37f913ffb
- session_id: 2026-08-12-真实考试-001:old:S07-B-01
- request_mode: stream
- request_start: 2026-08-11T18:29:27.347
- evaluation_sample_id: 20260811_182927_346_9235f07d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:29:27.349
- end: 2026-08-11T18:29:27.349
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:29:27.350
- end: 2026-08-11T18:29:27.350
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 1c9d78a37f913ffb

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:29:27.351
- end: 2026-08-11T18:29:27.351
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 1c9d78a37f913ffb
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:29:27.351
- end: 2026-08-11T18:29:39.021
- duration_ms: 11669
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询的核心是从“川味凉菜”候选做法中，依据“口感清爽”的偏好进行筛选和排序。需要将川味凉菜的菜品/食材、调味方式与口感特征建立匹配，并对不同做法进行轻度对比；但不涉及跨领域、多实体、多层级的复杂关系网络或深层因果推理。适合采用关键词检索结合语义检索的 hybrid_traditional 策略，召回如凉拌黄瓜、凉拌木耳、伤心凉粉、凉拌鸡丝等候选，再按少油、少糖、酸辣开胃、蔬菜或凉粉主料等“清爽”特征进行排序。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 156, 'graph_rag_count': 33, 'total_queries': 189}
- route_stats_after: {'traditional_count': 157, 'graph_rag_count': 33, 'total_queries': 190}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['凉拌黄瓜', '凉拌木耳', '凉拌鸡丝', '凉拌豆腐皮', '凉粉', '折耳根', '花椒', '辣椒油', '醋']
- topic_keywords: ['川味凉菜', '川菜', '清爽口感', '凉拌', '酸辣', '麻辣', '开胃菜', '夏季菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 10109

## Hybrid Branch Status / entity_level
- keywords: ['凉拌黄瓜', '凉拌木耳', '凉拌鸡丝', '凉拌豆腐皮', '凉粉', '折耳根', '花椒', '辣椒油', '醋']
- requested_k: 10
- actual_count: 10
- fallback_count: 3
- duration_ms: 83

## Hybrid Branch Status / topic_level
- keywords: ['川味凉菜', '川菜', '清爽口感', '凉拌', '酸辣', '麻辣', '开胃菜', '夏季菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 83

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 674

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 21
- duplicate_count: 9

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['去腥', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 22
- duration_ms: 17878
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食,凉菜': 1, '半成品': 1, '素菜': 2, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蒜蓉空心菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 28699
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:29:27.351
- end: 2026-08-11T18:30:07.722
- duration_ms: 40370
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2327
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
- chunk_count: 606
- redacted_field: 1954
- total_duration_ms: 14106
- fallback_used: False

## Final Output
- answer_chars: 747
- answer_hash: 680615839243b878
- success: True

## Request Complete
- request_end: 2026-08-11T18:30:21.842
- request_duration_ms: 54494
- success: True
- final_source: generation

