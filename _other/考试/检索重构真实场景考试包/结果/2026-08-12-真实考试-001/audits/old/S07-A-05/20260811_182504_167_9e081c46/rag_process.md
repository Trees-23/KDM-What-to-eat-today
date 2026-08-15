# RAG Process

audit_id: 20260811_182504_167_9e081c46
timestamp: 2026-08-11T18:25:04.169
## Request
- original_query: 想要有蔬菜的轻口味川菜。请推荐几个可考虑的菜。
- original_query_hash: 3413b164c60cbbfa
- session_id: 2026-08-12-真实考试-001:old:S07-A-05
- request_mode: stream
- request_start: 2026-08-11T18:25:04.170
- evaluation_sample_id: 20260811_182504_167_9e081c46
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:25:04.171
- end: 2026-08-11T18:25:04.171
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:25:04.172
- end: 2026-08-11T18:25:04.172
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: 3413b164c60cbbfa

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:25:04.172
- end: 2026-08-11T18:25:04.172
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: 3413b164c60cbbfa
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:25:04.173
- end: 2026-08-11T18:25:11.531
- duration_ms: 7358
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.5
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带条件的菜品推荐：需在“川菜”范围内筛选包含“蔬菜”且符合“轻口味”偏好的菜品。需要进行基础的属性匹配与条件过滤，但不涉及复杂的多跳关系推理、因果分析或大规模知识关系发现。明确实体主要为“川菜”和“蔬菜”，“轻口味”属于口味偏好属性。适合通过关键词检索、菜品标签过滤及语义召回相结合的 hybrid_traditional 策略完成。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 150, 'graph_rag_count': 33, 'total_queries': 183}
- route_stats_after: {'traditional_count': 151, 'graph_rag_count': 33, 'total_queries': 184}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['开水白菜', '清炒豌豆尖', '炝炒莲白', '青椒土豆丝', '清炒莴笋丝', '白菜', '豌豆尖', '莲白', '土豆', '莴笋']
- topic_keywords: ['川菜', '清淡口味', '蔬菜', '素菜', '少油少盐', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 11665

## Hybrid Branch Status / entity_level
- keywords: ['开水白菜', '清炒豌豆尖', '炝炒莲白', '青椒土豆丝', '清炒莴笋丝', '白菜', '豌豆尖', '莲白', '土豆', '莴笋']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 24

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '清淡口味', '蔬菜', '素菜', '少油少盐', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 44

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 700

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 20
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['去腥', '如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 21
- duration_ms: 22469
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 1, '水产': 1, '通用知识': 1, '素菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 茄子炖土豆
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 34869
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:25:04.173
- end: 2026-08-11T18:25:46.401
- duration_ms: 42228
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2215
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
- chunk_count: 412
- redacted_field: 1811
- total_duration_ms: 9302
- fallback_used: False

## Final Output
- answer_chars: 504
- answer_hash: 6f3fdc922cde2ca5
- success: True

## Request Complete
- request_end: 2026-08-11T18:25:55.717
- request_duration_ms: 51546
- success: True
- final_source: generation

