# RAG Process

audit_id: 20260811_182129_493_e28a0f66
timestamp: 2026-08-11T18:21:29.498
## Request
- original_query: 想做一道能配米饭的炖菜。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: 5b012ef904783d5f
- session_id: 2026-08-12-真实考试-001:old:S06-C-09
- request_mode: stream
- request_start: 2026-08-11T18:21:29.499
- evaluation_sample_id: 20260811_182129_493_e28a0f66
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:21:29.500
- end: 2026-08-11T18:21:29.500
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:21:29.500
- end: 2026-08-11T18:21:29.500
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 42
- enhanced_query_length: 42
- enhanced_query_hash: 5b012ef904783d5f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:21:29.500
- end: 2026-08-11T18:21:29.500
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 42
- analysis_input_query_hash: 5b012ef904783d5f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:21:29.500
- end: 2026-08-11T18:21:37.666
- duration_ms: 8165
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询的核心是基于现有资料推荐一道适合搭配米饭的炖菜，并展示推荐依据。需要检索炖菜食谱、口味特征、汤汁/酱汁特点及其与米饭搭配的明确描述或可验证证据，再对候选菜品进行轻度比较。该任务存在约束匹配和证据归纳需求，但不涉及多实体、多层级的复杂知识网络。明确实体主要为“米饭”和“炖菜”；“能配”是二者之间的搭配关系而非独立实体。建议采用 hybrid_traditional，通过关键词检索、语义召回和来源排序定位含有“下饭”“配米饭”“酱汁浓郁”等明确依据的食谱或资料；若资料未明确支持搭配结论，应标注为无法确认，而不能将常识性推测表述为事实。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 145, 'graph_rag_count': 33, 'total_queries': 178}
- route_stats_after: {'traditional_count': 146, 'graph_rag_count': 33, 'total_queries': 179}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['米饭', '炖菜']
- topic_keywords: ['下饭菜', '炖煮', '推荐依据', '资料支持']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4679

## Hybrid Branch Status / entity_level
- keywords: ['米饭', '炖菜']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 17

## Hybrid Branch Status / topic_level
- keywords: ['下饭菜', '炖煮', '推荐依据', '资料支持']
- requested_k: 10
- actual_count: 4
- fallback_count: 4
- duration_ms: 44

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 581

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 4
- vector_count: 10
- origin_len: 15

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 15
- after_count: 14
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 4
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 15
- duration_ms: 18256
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 2, '烹饪技巧': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 皮蛋瘦肉粥
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23540
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:21:29.500
- end: 2026-08-11T18:22:01.208
- duration_ms: 31707
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3377
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
- chunk_count: 331
- redacted_field: 9764
- total_duration_ms: 19681
- fallback_used: False

## Final Output
- answer_chars: 453
- answer_hash: 97625445ab2a1298
- success: True

## Request Complete
- request_end: 2026-08-11T18:22:20.940
- request_duration_ms: 51441
- success: True
- final_source: generation

