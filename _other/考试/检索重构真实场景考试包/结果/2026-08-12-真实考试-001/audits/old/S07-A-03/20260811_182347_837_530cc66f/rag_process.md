# RAG Process

audit_id: 20260811_182347_837_530cc66f
timestamp: 2026-08-11T18:23:47.838
## Request
- original_query: 偏好清淡一些的川菜。请推荐几个可考虑的菜。
- original_query_hash: 74269ebe589ddb51
- session_id: 2026-08-12-真实考试-001:old:S07-A-03
- request_mode: stream
- request_start: 2026-08-11T18:23:47.839
- evaluation_sample_id: 20260811_182347_837_530cc66f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:23:47.840
- end: 2026-08-11T18:23:47.840
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:23:47.841
- end: 2026-08-11T18:23:47.841
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 74269ebe589ddb51

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:23:47.841
- end: 2026-08-11T18:23:47.841
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 74269ebe589ddb51
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:23:47.842
- end: 2026-08-11T18:23:56.344
- duration_ms: 8502
- analysis_mode: llm
- query_complexity: 0.52
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带偏好约束的菜品推荐任务：用户限定了“川菜”这一菜系范围，并以“清淡一些”作为口味筛选条件，要求返回若干符合条件的菜品。它需要进行轻量级的属性匹配与排序，例如排除重油、重辣、重麻的典型菜品，优先召回口味相对清爽、可少油少辣或以鲜味为主的川菜。查询不涉及复杂历史、地理或多实体关系网络，也不需要多跳推理或因果分析；可使用关键词检索结合菜品标签、口味标签和向量语义召回完成，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 148, 'graph_rag_count': 33, 'total_queries': 181}
- route_stats_after: {'traditional_count': 149, 'graph_rag_count': 33, 'total_queries': 182}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['开水白菜', '清炒凤尾', '鸡豆花', '雪花鸡淖', '清蒸江团', '芙蓉鸡片']
- topic_keywords: ['川菜', '清淡', '少油', '少辣', '鲜味', '清爽']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3760

## Hybrid Branch Status / entity_level
- keywords: ['开水白菜', '清炒凤尾', '鸡豆花', '雪花鸡淖', '清蒸江团', '芙蓉鸡片']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 27

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '清淡', '少油', '少辣', '鲜味', '清爽']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 60

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 601

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 10
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 19
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 4
- expanded_count: 9
- doc_names: ['去腥', '如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 20
- duration_ms: 19701
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '主食': 2, '主食,凉菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蒜蓉空心菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24094
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:23:47.842
- end: 2026-08-11T18:24:20.439
- duration_ms: 32597
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1824
- retrieval_levels: ['context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level']
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
- chunk_count: 323
- redacted_field: 2142
- total_duration_ms: 8181
- fallback_used: False

## Final Output
- answer_chars: 425
- answer_hash: fa5652ea4510b8c4
- success: True

## Request Complete
- request_end: 2026-08-11T18:24:28.644
- request_duration_ms: 40804
- success: True
- final_source: generation

