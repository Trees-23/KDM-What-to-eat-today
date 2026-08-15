# RAG Process

audit_id: 20260811_183350_120_07f49f78
timestamp: 2026-08-11T18:33:50.122
## Request
- original_query: 口味偏清淡，但可以有一点川味酸辣，有哪些做法比较贴近这种偏好？
- original_query_hash: a721a369397d363c
- session_id: 2026-08-12-真实考试-001:old:S07-B-05
- request_mode: stream
- request_start: 2026-08-11T18:33:50.123
- evaluation_sample_id: 20260811_183350_120_07f49f78
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:33:50.124
- end: 2026-08-11T18:33:50.124
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:33:50.126
- end: 2026-08-11T18:33:50.126
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 31
- enhanced_query_length: 31
- enhanced_query_hash: a721a369397d363c

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:33:50.128
- end: 2026-08-11T18:33:50.128
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 31
- analysis_input_query_hash: a721a369397d363c
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:33:50.128
- end: 2026-08-11T18:33:57.776
- duration_ms: 7648
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.55
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询属于带有多重口味约束的菜谱/做法推荐：核心条件是“清淡”为主，同时允许少量“川味酸辣”。需要从做法、调味料用量和菜系风格中筛选并排序，但不涉及复杂历史、因果或跨领域关系网络。可使用关键词检索结合向量语义召回，匹配“清淡”“微酸辣”“川味”“少油少麻少辣”等近义表达，再通过规则过滤重油重麻重辣菜式。无需多跳推理或因果分析，但需要一定的偏好约束对比与适配判断。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 160, 'graph_rag_count': 33, 'total_queries': 193}
- route_stats_after: {'traditional_count': 161, 'graph_rag_count': 33, 'total_queries': 194}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['泡椒', '泡菜', '醋', '辣椒', '酸辣汤', '泡椒鸡丝', '酸辣土豆丝', '泡菜豆腐汤']
- topic_keywords: ['清淡口味', '川味', '酸辣味', '微辣', '开胃菜', '少油少盐']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6545

## Hybrid Branch Status / topic_level
- keywords: ['清淡口味', '川味', '酸辣味', '微辣', '开胃菜', '少油少盐']
- requested_k: 10
- actual_count: 3
- fallback_count: 3
- duration_ms: 23

## Hybrid Branch Status / entity_level
- keywords: ['泡椒', '泡菜', '醋', '辣椒', '酸辣汤', '泡椒鸡丝', '酸辣土豆丝', '泡菜豆腐汤']
- requested_k: 10
- actual_count: 10
- fallback_count: 6
- duration_ms: 62

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 331

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 3
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 19
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['去腥', '厨房准备']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 20
- duration_ms: 19348
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 1, '主食': 1, 'Recipe': 1, '半成品': 1, '荤菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 甜辣烤全翅
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26258
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:33:50.128
- end: 2026-08-11T18:34:24.036
- duration_ms: 33907
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3321
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
- chunk_count: 422
- redacted_field: 4089
- total_duration_ms: 11997
- fallback_used: False

## Final Output
- answer_chars: 559
- answer_hash: b54cab9f9123ead1
- success: True

## Request Complete
- request_end: 2026-08-11T18:34:36.047
- request_duration_ms: 45924
- success: True
- final_source: generation

