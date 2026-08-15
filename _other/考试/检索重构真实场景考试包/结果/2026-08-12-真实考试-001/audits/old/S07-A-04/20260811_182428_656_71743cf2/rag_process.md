# RAG Process

audit_id: 20260811_182428_656_71743cf2
timestamp: 2026-08-11T18:24:28.657
## Request
- original_query: 不想吃太腻，想吃川味配米饭的菜。请推荐几个可考虑的菜。
- original_query_hash: 0f304b0d2674b3df
- session_id: 2026-08-12-真实考试-001:old:S07-A-04
- request_mode: stream
- request_start: 2026-08-11T18:24:28.657
- evaluation_sample_id: 20260811_182428_656_71743cf2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:24:28.658
- end: 2026-08-11T18:24:28.658
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:24:28.658
- end: 2026-08-11T18:24:28.658
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 0f304b0d2674b3df

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:24:28.659
- end: 2026-08-11T18:24:28.659
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 0f304b0d2674b3df
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:24:28.659
- end: 2026-08-11T18:24:36.341
- duration_ms: 7681
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带有多重饮食偏好的菜品推荐：用户要求菜品具备“川味”“不太腻”“适合配米饭”三个核心约束，需要从川菜菜品中筛选并匹配口味、油腻程度和下饭属性。无需多跳推理或复杂因果分析，但需要进行轻量级的属性匹配与候选菜品排序，可通过关键词检索、菜品标签过滤和语义召回实现。明确实体主要为“川味/川菜”“米饭”“菜品”，其中“不太腻”属于口味偏好与筛选属性。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 149, 'graph_rag_count': 33, 'total_queries': 182}
- route_stats_after: {'traditional_count': 150, 'graph_rag_count': 33, 'total_queries': 183}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鱼香肉丝', '宫保鸡丁', '回锅肉', '麻婆豆腐', '青椒肉丝', '蒜苗炒肉', '豆豉鲮鱼油麦菜', '酸辣土豆丝']
- topic_keywords: ['川菜', '川味', '下饭菜', '配米饭', '不油腻', '清爽', '微辣', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4038

## Hybrid Branch Status / entity_level
- keywords: ['鱼香肉丝', '宫保鸡丁', '回锅肉', '麻婆豆腐', '青椒肉丝', '蒜苗炒肉', '豆豉鲮鱼油麦菜', '酸辣土豆丝']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 38

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '川味', '下饭菜', '配米饭', '不油腻', '清爽', '微辣', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 45

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 648

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 22
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 5
- doc_names: ['如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 15976
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 1, '通用知识': 1, '素菜': 2, '荤菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 口水鸡
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20689
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:24:28.659
- end: 2026-08-11T18:24:57.031
- duration_ms: 28371
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1490
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
- chunk_count: 241
- redacted_field: 2150
- total_duration_ms: 7106
- fallback_used: False

## Final Output
- answer_chars: 300
- answer_hash: ef0ae61a291752d0
- success: True

## Request Complete
- request_end: 2026-08-11T18:25:04.153
- request_duration_ms: 35496
- success: True
- final_source: generation

