# RAG Process

audit_id: 20260811_183528_569_73a06001
timestamp: 2026-08-11T18:35:28.574
## Request
- original_query: 希望是一道川味素菜或蔬菜占主的菜，有哪些做法比较贴近这种偏好？
- original_query_hash: b755180abbc9c547
- session_id: 2026-08-12-真实考试-001:old:S07-B-07
- request_mode: stream
- request_start: 2026-08-11T18:35:28.574
- evaluation_sample_id: 20260811_183528_569_73a06001
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:35:28.575
- end: 2026-08-11T18:35:28.575
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:35:28.575
- end: 2026-08-11T18:35:28.575
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: b755180abbc9c547

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:35:28.576
- end: 2026-08-11T18:35:28.576
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 31
- analysis_input_query_hash: b755180abbc9c547
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:35:28.576
- end: 2026-08-11T18:35:36.233
- duration_ms: 7657
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询属于带条件的菜谱推荐：需要同时满足“川味”“素菜或蔬菜为主”“做法贴近偏好”三个约束，并从候选菜品中筛选和排序。需要轻度对比分析，例如区分纯素菜、含少量动物性调料的蔬菜菜，以及不同川味做法（鱼香、家常、干煸、炝炒等）与用户偏好的匹配度；但不涉及跨领域、多跳因果或复杂知识网络推理。明确实体主要包括“川味/川菜”“素菜或蔬菜”“做法（烹饪方式）”。因此适合采用关键词检索、菜谱语义召回和条件过滤相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 162, 'graph_rag_count': 33, 'total_queries': 195}
- route_stats_after: {'traditional_count': 163, 'graph_rag_count': 33, 'total_queries': 196}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['麻婆豆腐', '鱼香茄子', '干煸四季豆', '炝炒莲白', '酸辣土豆丝', '手撕包菜', '地三鲜', '豆腐', '茄子', '四季豆', '莲白', '土豆']
- topic_keywords: ['川味', '川菜', '素菜', '素食', '蔬菜为主', '麻辣', '香辣', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3844

## Hybrid Branch Status / entity_level
- keywords: ['麻婆豆腐', '鱼香茄子', '干煸四季豆', '炝炒莲白', '酸辣土豆丝', '手撕包菜', '地三鲜', '豆腐', '茄子', '四季豆', '莲白', '土豆']
- requested_k: 10
- actual_count: 9
- fallback_count: 0
- duration_ms: 81

## Hybrid Branch Status / topic_level
- keywords: ['川味', '川菜', '素菜', '素食', '蔬菜为主', '麻辣', '香辣', '下饭菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 88

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 515

## Hybrid Branch Summary
- entity_count: 9
- topic_count: 10
- vector_count: 10
- origin_len: 29

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 29
- after_count: 27
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['去腥', '揭秘食材搭配的智慧：这些食物不宜同食']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 28
- duration_ms: 20709
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '水产': 1, 'Recipe': 1, '主食': 1}
- deferred_count: 9
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 汤面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25114
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:35:28.576
- end: 2026-08-11T18:36:01.349
- duration_ms: 32772
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2880
- retrieval_levels: ['', 'context_expansion', 'entity', 'topic']
- search_types: ['entity_level', 'technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 508
- redacted_field: 2037
- total_duration_ms: 13559
- fallback_used: False

## Final Output
- answer_chars: 644
- answer_hash: 03ce97662a669d8e
- success: True

## Request Complete
- request_end: 2026-08-11T18:36:14.919
- request_duration_ms: 46345
- success: True
- final_source: generation

