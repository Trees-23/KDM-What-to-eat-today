# RAG Process

audit_id: 20260811_182629_394_b77a43f0
timestamp: 2026-08-11T18:26:29.395
## Request
- original_query: 想吃辣但不希望太油重的川菜。请推荐几个可考虑的菜。
- original_query_hash: ba89600eb411ce2b
- session_id: 2026-08-12-真实考试-001:old:S07-A-07
- request_mode: stream
- request_start: 2026-08-11T18:26:29.396
- evaluation_sample_id: 20260811_182629_394_b77a43f0
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:26:29.396
- end: 2026-08-11T18:26:29.396
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:26:29.396
- end: 2026-08-11T18:26:29.396
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: ba89600eb411ce2b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:26:29.397
- end: 2026-08-11T18:26:29.397
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: ba89600eb411ce2b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:26:29.397
- end: 2026-08-11T18:26:37.343
- duration_ms: 7946
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带偏好约束的菜品推荐：用户限定菜系为“川菜”，口味要求“想吃辣”，同时排除“油重”的菜品。需要从川菜菜品中检索并筛选出辣度适中或明显、但烹饪方式较清爽（如蒸、煮、炝拌、清炒）的候选菜，再进行排序推荐。它涉及菜品与口味、油脂程度、烹饪方式之间的属性匹配，但不需要复杂的跨领域关系网络或因果推理，因此更适合使用 hybrid_traditional，通过关键词检索、菜品属性标签过滤和语义召回来完成。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 152, 'graph_rag_count': 33, 'total_queries': 185}
- route_stats_after: {'traditional_count': 153, 'graph_rag_count': 33, 'total_queries': 186}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['麻婆豆腐', '鱼香肉丝', '宫保鸡丁', '泡椒鸡杂', '凉拌鸡丝', '辣椒', '花椒']
- topic_keywords: ['川菜', '香辣', '麻辣', '少油', '清爽', '低脂', '开胃菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3482

## Hybrid Branch Status / entity_level
- keywords: ['麻婆豆腐', '鱼香肉丝', '宫保鸡丁', '泡椒鸡杂', '凉拌鸡丝', '辣椒', '花椒']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 34

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '香辣', '麻辣', '少油', '清爽', '低脂', '开胃菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 50

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 670

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 21
- duplicate_count: 5

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
- candidate_count: 22
- duration_ms: 21095
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 2, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 凉粉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25277
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:26:29.397
- end: 2026-08-11T18:27:02.622
- duration_ms: 33225
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3548
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
- chunk_count: 374
- redacted_field: 2074
- total_duration_ms: 9264
- fallback_used: False

## Final Output
- answer_chars: 486
- answer_hash: 851657ad3d2d4a7f
- success: True

## Request Complete
- request_end: 2026-08-11T18:27:11.900
- request_duration_ms: 42504
- success: True
- final_source: generation

