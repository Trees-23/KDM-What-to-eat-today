# RAG Process

audit_id: 20260811_183614_942_e609bf0c
timestamp: 2026-08-11T18:36:14.942
## Request
- original_query: 想找适合午餐的轻负担川菜，有哪些做法比较贴近这种偏好？
- original_query_hash: d164ccd11b78a1e9
- session_id: 2026-08-12-真实考试-001:old:S07-B-08
- request_mode: stream
- request_start: 2026-08-11T18:36:14.943
- evaluation_sample_id: 20260811_183614_942_e609bf0c
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:36:14.943
- end: 2026-08-11T18:36:14.943
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:36:14.944
- end: 2026-08-11T18:36:14.944
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: d164ccd11b78a1e9

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:36:14.944
- end: 2026-08-11T18:36:14.944
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: d164ccd11b78a1e9
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:36:14.944
- end: 2026-08-11T18:36:24.741
- duration_ms: 9796
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.57
- reasoning_required: True
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询核心是从川菜做法中筛选并推荐符合“午餐”“轻负担”偏好的选项，涉及川菜风味、烹饪方式、油盐辣度控制及午餐适配性之间的属性匹配与轻度对比。虽然需要结合偏好进行归纳判断，但不依赖跨多实体的复杂关系网络、多跳知识发现或因果链推理，因此更适合采用关键词检索结合向量语义召回的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 163, 'graph_rag_count': 33, 'total_queries': 196}
- route_stats_after: {'traditional_count': 164, 'graph_rag_count': 33, 'total_queries': 197}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['麻婆豆腐', '鱼香茄子', '宫保鸡丁', '回锅肉', '水煮鱼', '凉拌鸡丝', '凉拌木耳', '清炒时蔬', '豆腐', '鸡胸肉', '鱼片', '菌菇', '辣椒', '花椒']
- topic_keywords: ['川菜', '午餐', '轻负担', '低油', '低脂', '低热量', '少盐', '清淡', '高蛋白', '蔬菜', '快手菜', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4067

## Hybrid Branch Status / entity_level
- keywords: ['麻婆豆腐', '鱼香茄子', '宫保鸡丁', '回锅肉', '水煮鱼', '凉拌鸡丝', '凉拌木耳', '清炒时蔬', '豆腐', '鸡胸肉', '鱼片', '菌菇', '辣椒', '花椒']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 47

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 293

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '午餐', '轻负担', '低油', '低脂', '低热量', '少盐', '清淡', '高蛋白', '蔬菜', '快手菜', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 1142

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 24
- duplicate_count: 6

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
- candidate_count: 25
- duration_ms: 19239
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '素菜': 2, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 口水鸡
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24468
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:36:14.944
- end: 2026-08-11T18:36:49.210
- duration_ms: 34265
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3547
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
- chunk_count: 900
- redacted_field: 5168
- total_duration_ms: 22984
- fallback_used: False

## Final Output
- answer_chars: 1123
- answer_hash: ea55b28d771c0572
- success: True

## Request Complete
- request_end: 2026-08-11T18:37:12.213
- request_duration_ms: 57270
- success: True
- final_source: generation

