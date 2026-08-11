# RAG Process

audit_id: 20260811_182841_762_e2e78643
timestamp: 2026-08-11T18:28:41.764
## Request
- original_query: 偏好蒸制或煮制风格的川味晚餐。请推荐几个可考虑的菜。
- original_query_hash: 4596e5868cbefc0e
- session_id: 2026-08-12-真实考试-001:old:S07-A-10
- request_mode: stream
- request_start: 2026-08-11T18:28:41.766
- evaluation_sample_id: 20260811_182841_762_e2e78643
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:28:41.766
- end: 2026-08-11T18:28:41.766
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:28:41.767
- end: 2026-08-11T18:28:41.767
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 4596e5868cbefc0e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:28:41.767
- end: 2026-08-11T18:28:41.767
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 4596e5868cbefc0e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:28:41.768
- end: 2026-08-11T18:28:51.908
- duration_ms: 10140
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 4
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带多重条件的菜品推荐任务，需要同时匹配“川味”地域风味、“晚餐”用餐场景以及“蒸制或煮制”烹饪方式，并排除或弱化炒、炸等不符合偏好的菜品。需要进行条件筛选与菜品适配判断，但不涉及复杂的跨实体关系网络、历史因果链或知识图谱多跳推理。明确实体包括川味（菜系/风味）、蒸制（烹饪方式）、煮制（烹饪方式）、晚餐（用餐场景）。适合通过关键词检索、菜谱标签过滤、语义召回和排序实现，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 155, 'graph_rag_count': 33, 'total_queries': 188}
- route_stats_after: {'traditional_count': 156, 'graph_rag_count': 33, 'total_queries': 189}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['清蒸鱼', '粉蒸肉', '蒸酥肉', '蒸茄子', '豆瓣鱼', '水煮牛肉', '水煮鱼', '连锅汤', '辣椒', '花椒', '豆瓣酱']
- topic_keywords: ['川菜', '川味晚餐', '蒸制', '煮制', '麻辣', '鲜香', '少油', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4805

## Hybrid Branch Status / entity_level
- keywords: ['清蒸鱼', '粉蒸肉', '蒸酥肉', '蒸茄子', '豆瓣鱼', '水煮牛肉', '水煮鱼', '连锅汤', '辣椒', '花椒', '豆瓣酱']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 75

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '川味晚餐', '蒸制', '煮制', '麻辣', '鲜香', '少油', '家常菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 80

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 621

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 24
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 25
- duration_ms: 20032
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '主食': 1, '荤菜': 1, 'Recipe': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 粉蒸肉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25482
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:28:41.768
- end: 2026-08-11T18:29:17.392
- duration_ms: 35624
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3904
- retrieval_levels: ['context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level']
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
- chunk_count: 448
- redacted_field: 2034
- total_duration_ms: 9905
- fallback_used: False

## Final Output
- answer_chars: 575
- answer_hash: ddb13f0a85d0c9ee
- success: True

## Request Complete
- request_end: 2026-08-11T18:29:27.331
- request_duration_ms: 45565
- success: True
- final_source: generation

