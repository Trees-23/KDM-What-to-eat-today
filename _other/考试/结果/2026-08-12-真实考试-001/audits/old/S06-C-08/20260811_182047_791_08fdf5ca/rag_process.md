# RAG Process

audit_id: 20260811_182047_791_08fdf5ca
timestamp: 2026-08-11T18:20:47.792
## Request
- original_query: 想做偏清淡的海鲜。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: 3b9eaa0a215edd56
- session_id: 2026-08-12-真实考试-001:old:S06-C-08
- request_mode: stream
- request_start: 2026-08-11T18:20:47.792
- evaluation_sample_id: 20260811_182047_791_08fdf5ca
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:20:47.794
- end: 2026-08-11T18:20:47.794
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:20:47.794
- end: 2026-08-11T18:20:47.794
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 39
- enhanced_query_length: 39
- enhanced_query_hash: 3b9eaa0a215edd56

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:20:47.795
- end: 2026-08-11T18:20:47.795
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 39
- analysis_input_query_hash: 3b9eaa0a215edd56
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:20:47.796
- end: 2026-08-11T18:20:56.723
- duration_ms: 8927
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询核心是“海鲜”菜品推荐，并受“偏清淡”这一口味/烹饪约束限制；同时要求展示推荐依据，并明确要求资料不足时不能将推测表述为事实。需要从菜谱、菜单或食材资料中检索海鲜菜品，匹配清蒸、白灼、清汤、少油少辛香料等可被资料直接支持的特征，再对候选结果进行依据摘取和保守表述。该任务主要是带条件的检索、排序与证据对齐，不涉及多实体、多层级的复杂关系网络或深度因果推理，因此适合 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 144, 'graph_rag_count': 33, 'total_queries': 177}
- route_stats_after: {'traditional_count': 145, 'graph_rag_count': 33, 'total_queries': 178}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['海鲜']
- topic_keywords: ['清淡饮食', '清淡口味', '海鲜菜', '推荐依据', '资料支持']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5695

## Hybrid Branch Status / entity_level
- keywords: ['海鲜']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / topic_level
- keywords: ['清淡饮食', '清淡口味', '海鲜菜', '推荐依据', '资料支持']
- requested_k: 10
- actual_count: 1
- fallback_count: 1
- duration_ms: 21

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 655

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 1
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 9
- duplicate_count: 2

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
- candidate_count: 10
- duration_ms: 15410
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 1, '主食': 1, '水产': 1, '通用知识': 1, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 葱油桂鱼
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21798
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:20:47.796
- end: 2026-08-11T18:21:18.522
- duration_ms: 30726
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2112
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
- chunk_count: 333
- redacted_field: 4267
- total_duration_ms: 10940
- fallback_used: False

## Final Output
- answer_chars: 440
- answer_hash: d321fdbd5a1883e5
- success: True

## Request Complete
- request_end: 2026-08-11T18:21:29.481
- request_duration_ms: 41689
- success: True
- final_source: generation

