# RAG Process

audit_id: 20260811_180344_563_6192c697
timestamp: 2026-08-11T18:03:44.563
## Request
- original_query: 想吃辣一点的川味家常菜。请推荐知识库中最合适的菜，并说明依据。
- original_query_hash: 2a0d3dca731573f6
- session_id: 2026-08-12-真实考试-001:old:S06-A-07
- request_mode: stream
- request_start: 2026-08-11T18:03:44.564
- evaluation_sample_id: 20260811_180344_563_6192c697
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:03:44.564
- end: 2026-08-11T18:03:44.564
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:03:44.564
- end: 2026-08-11T18:03:44.564
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: 2a0d3dca731573f6

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:03:44.565
- end: 2026-08-11T18:03:44.565
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 31
- analysis_input_query_hash: 2a0d3dca731573f6
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:03:44.565
- end: 2026-08-11T18:03:54.395
- duration_ms: 9829
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带偏好的菜品推荐任务，需要从知识库中筛选同时满足“川味家常菜”和“辣一点”两个条件的候选菜，并按辣度、菜系归属及家常属性进行匹配排序。无需分析复杂历史、地理或食材关系网络，也不需要多跳推理或因果推理；可通过关键词检索、语义向量召回及元数据过滤完成。明确实体/约束包括“川味家常菜”（菜品类别/菜系风格）和“辣一点”（口味偏好/辣度条件）。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 124, 'graph_rag_count': 32, 'total_queries': 156}
- route_stats_after: {'traditional_count': 125, 'graph_rag_count': 32, 'total_queries': 157}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['麻婆豆腐', '回锅肉', '鱼香肉丝', '辣椒', '花椒', '豆瓣酱']
- topic_keywords: ['川菜', '川味', '家常菜', '辣', '麻辣', '香辣', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4600

## Hybrid Branch Status / entity_level
- keywords: ['麻婆豆腐', '回锅肉', '鱼香肉丝', '辣椒', '花椒', '豆瓣酱']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 26

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '川味', '家常菜', '辣', '麻辣', '香辣', '下饭菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 42

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 632

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 23
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['去腥', '如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 24
- duration_ms: 20092
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '素菜': 1, '主食': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 煮泡面加蛋
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25354
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:03:44.565
- end: 2026-08-11T18:04:19.751
- duration_ms: 35185
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1874
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
- chunk_count: 240
- redacted_field: 3255
- total_duration_ms: 7872
- fallback_used: False

## Final Output
- answer_chars: 301
- answer_hash: bcd60fabd14229ae
- success: True

## Request Complete
- request_end: 2026-08-11T18:04:27.638
- request_duration_ms: 43074
- success: True
- final_source: generation

