# RAG Process

audit_id: 20260811_182303_002_c2e02414
timestamp: 2026-08-11T18:23:03.003
## Request
- original_query: 想找少油感觉的川味晚餐。请推荐几个可考虑的菜。
- original_query_hash: f7cb8317eb782f37
- session_id: 2026-08-12-真实考试-001:old:S07-A-02
- request_mode: stream
- request_start: 2026-08-11T18:23:03.003
- evaluation_sample_id: 20260811_182303_002_c2e02414
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:23:03.003
- end: 2026-08-11T18:23:03.003
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:23:03.004
- end: 2026-08-11T18:23:03.004
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 23
- enhanced_query_length: 23
- enhanced_query_hash: f7cb8317eb782f37

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:23:03.004
- end: 2026-08-11T18:23:03.004
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 23
- analysis_input_query_hash: f7cb8317eb782f37
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:23:03.004
- end: 2026-08-11T18:23:13.067
- duration_ms: 10062
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带偏好约束的菜品推荐：核心目标是寻找适合晚餐的川味菜，并满足“少油感觉”的口味/烹饪方式偏好。需要进行轻量级的属性匹配与筛选，例如识别川味菜品、判断其通常油脂使用程度，以及是否适合作为晚餐菜肴。无需多跳推理或复杂因果分析；可进行轻量对比，如在水煮、干煸、回锅等常见高油做法之外，优先检索清蒸、清炒、炖煮、凉拌或少油改良的川味菜。明确实体包括“川味/川菜”（菜系）、“晚餐”（用餐场景）和“菜”（推荐对象）；“少油感觉”属于关键属性约束而非独立实体。适合使用关键词检索结合语义检索和元数据过滤的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 147, 'graph_rag_count': 33, 'total_queries': 180}
- route_stats_after: {'traditional_count': 148, 'graph_rag_count': 33, 'total_queries': 181}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['麻婆豆腐', '鱼香肉丝', '宫保鸡丁', '回锅肉', '水煮鱼', '辣椒', '花椒']
- topic_keywords: ['川菜', '川味', '少油', '低脂', '清淡', '晚餐', '麻辣', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3459

## Hybrid Branch Status / entity_level
- keywords: ['麻婆豆腐', '鱼香肉丝', '宫保鸡丁', '回锅肉', '水煮鱼', '辣椒', '花椒']
- requested_k: 10
- actual_count: 7
- fallback_count: 0
- duration_ms: 64

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '川味', '少油', '低脂', '清淡', '晚餐', '麻辣', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 82

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: -272

## Hybrid Branch Summary
- entity_count: 7
- topic_count: 10
- vector_count: 10
- origin_len: 27

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 27
- after_count: 23
- duplicate_count: 4

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
- candidate_count: 24
- duration_ms: 21434
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 2, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蒜蓉空心菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24657
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:23:03.004
- end: 2026-08-11T18:23:37.726
- duration_ms: 34721
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3550
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
- chunk_count: 399
- redacted_field: 2161
- total_duration_ms: 10080
- fallback_used: False

## Final Output
- answer_chars: 523
- answer_hash: 5cb5030fce382644
- success: True

## Request Complete
- request_end: 2026-08-11T18:23:47.822
- request_duration_ms: 44819
- success: True
- final_source: generation

