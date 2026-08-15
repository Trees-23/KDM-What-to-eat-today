# RAG Process

audit_id: 20260811_181239_193_64a21f26
timestamp: 2026-08-11T18:12:39.196
## Request
- original_query: 想做一道有蔬菜的快手菜，帮我找几个贴近这个需求的做法。
- original_query_hash: 61270cca710295bf
- session_id: 2026-08-12-真实考试-001:old:S06-B-08
- request_mode: stream
- request_start: 2026-08-11T18:12:39.196
- evaluation_sample_id: 20260811_181239_193_64a21f26
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:12:39.197
- end: 2026-08-11T18:12:39.197
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:12:39.197
- end: 2026-08-11T18:12:39.197
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 61270cca710295bf

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:12:39.198
- end: 2026-08-11T18:12:39.198
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 61270cca710295bf
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:12:39.198
- end: 2026-08-11T18:12:50.260
- duration_ms: 11061
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.4
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询目标明确，核心是检索并筛选符合“含蔬菜”和“快手菜”两个条件的多个菜谱做法。虽然需要对候选菜谱进行属性匹配与轻度排序（如烹饪时间、食材复杂度、步骤数量），但不涉及多跳知识推理、因果分析或复杂关系网络。明确实体主要为“蔬菜”，其余为菜谱属性和需求约束。因此适合使用关键词检索结合语义检索与结果排序的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 134, 'graph_rag_count': 33, 'total_queries': 167}
- route_stats_after: {'traditional_count': 135, 'graph_rag_count': 33, 'total_queries': 168}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西兰花', '番茄', '鸡蛋', '青椒', '土豆', '黄瓜', '豆腐']
- topic_keywords: ['快手菜', '蔬菜', '家常菜', '简单易做', '健康饮食', '素食']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7263

## Hybrid Branch Status / entity_level
- keywords: ['西兰花', '番茄', '鸡蛋', '青椒', '土豆', '黄瓜', '豆腐']
- requested_k: 10
- actual_count: 7
- fallback_count: 0
- duration_ms: 47

## Hybrid Branch Status / topic_level
- keywords: ['快手菜', '蔬菜', '家常菜', '简单易做', '健康饮食', '素食']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 96

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 481

## Hybrid Branch Summary
- entity_count: 7
- topic_count: 10
- vector_count: 10
- origin_len: 27

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 27
- after_count: 24
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['如何决策吃什么', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 25
- duration_ms: 16838
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食,凉菜': 1, '主食': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 凉拌鸡丝
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24627
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:12:39.198
- end: 2026-08-11T18:13:14.888
- duration_ms: 35689
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1684
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
- chunk_count: 449
- redacted_field: 1930
- total_duration_ms: 10787
- fallback_used: False

## Final Output
- answer_chars: 570
- answer_hash: 00408e8de7ee3f7a
- success: True

## Request Complete
- request_end: 2026-08-11T18:13:25.691
- request_duration_ms: 46494
- success: True
- final_source: generation

