# RAG Process

audit_id: 20260811_181513_248_71655a91
timestamp: 2026-08-11T18:15:13.249
## Request
- original_query: 想做一人份的简单晚餐。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: b7e4073e03969412
- session_id: 2026-08-12-真实考试-001:old:S06-C-01
- request_mode: stream
- request_start: 2026-08-11T18:15:13.249
- evaluation_sample_id: 20260811_181513_248_71655a91
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:15:13.250
- end: 2026-08-11T18:15:13.250
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:15:13.250
- end: 2026-08-11T18:15:13.250
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 41
- enhanced_query_length: 41
- enhanced_query_hash: b7e4073e03969412

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:15:13.251
- end: 2026-08-11T18:15:13.251
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 41
- analysis_input_query_hash: b7e4073e03969412
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:15:13.251
- end: 2026-08-11T18:15:20.791
- duration_ms: 7540
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.87
- reasoning: 查询核心是为“一人份”和“简单晚餐”两个约束寻找可执行的推荐，并要求展示推荐依据、避免将资料未支持的推测表述为事实。需要从资料中检索菜谱的份量、食材数量、步骤、耗时或难度等明确字段，再依据这些可验证信息进行筛选和排序。该任务存在轻度约束匹配与证据归纳需求，但不涉及多实体、多层关系网络或复杂知识发现，因此适合采用 hybrid_traditional：结合关键词检索（如“一人份、快手、简单晚餐”）与结构化字段/语义召回，并在生成时绑定原始资料证据。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 137, 'graph_rag_count': 33, 'total_queries': 170}
- route_stats_after: {'traditional_count': 138, 'graph_rag_count': 33, 'total_queries': 171}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: []
- topic_keywords: ['一人份', '简单晚餐', '快手菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6616

## Hybrid Branch Status / entity_level
- keywords: []
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 6

## Hybrid Branch Status / topic_level
- keywords: ['一人份', '简单晚餐', '快手菜']
- requested_k: 10
- actual_count: 4
- fallback_count: 4
- duration_ms: 20

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 675

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 4
- vector_count: 10
- origin_len: 14

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 14
- after_count: 11
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 12
- duration_ms: 15073
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '荤菜': 2, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 姜炒鸡
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22385
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:15:13.251
- end: 2026-08-11T18:15:43.177
- duration_ms: 29926
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3411
- retrieval_levels: ['', 'context_expansion']
- search_types: ['technique_expansion', 'vector_enhanced']
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
- chunk_count: 639
- redacted_field: 2852
- total_duration_ms: 17022
- fallback_used: False

## Final Output
- answer_chars: 844
- answer_hash: 28e8be62f4098fd2
- success: True

## Request Complete
- request_end: 2026-08-11T18:16:00.228
- request_duration_ms: 46978
- success: True
- final_source: generation

