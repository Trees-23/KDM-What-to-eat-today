# RAG Process

audit_id: 20260811_182555_730_aebca938
timestamp: 2026-08-11T18:25:55.731
## Request
- original_query: 今天想吃川味但口味温和些。请推荐几个可考虑的菜。
- original_query_hash: 8983f371ca99f31b
- session_id: 2026-08-12-真实考试-001:old:S07-A-06
- request_mode: stream
- request_start: 2026-08-11T18:25:55.732
- evaluation_sample_id: 20260811_182555_730_aebca938
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:25:55.733
- end: 2026-08-11T18:25:55.733
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:25:55.734
- end: 2026-08-11T18:25:55.734
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 24
- enhanced_query_length: 24
- enhanced_query_hash: 8983f371ca99f31b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:25:55.734
- end: 2026-08-11T18:25:55.734
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 24
- analysis_input_query_hash: 8983f371ca99f31b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:25:55.735
- end: 2026-08-11T18:26:04.810
- duration_ms: 9075
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带偏好约束的菜品推荐：核心需求是“川味”菜系与“口味温和”口味条件的匹配，并需要从候选菜品中筛选出麻辣度较低、风味仍具川菜特色的菜。无需多跳推理或因果分析，但需要进行轻量级的属性匹配与候选对比。明确实体/概念包括：川味（菜系/风味类型）、口味温和（口味偏好属性）、菜（推荐对象/菜品类别）。适合通过关键词、菜系标签、口味标签及向量语义召回进行检索，再按辣度、麻度和用户偏好排序，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 151, 'graph_rag_count': 33, 'total_queries': 184}
- route_stats_after: {'traditional_count': 152, 'graph_rag_count': 33, 'total_queries': 185}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鱼香肉丝', '宫保鸡丁', '回锅肉', '麻婆豆腐', '甜皮鸭', '辣椒', '花椒']
- topic_keywords: ['川菜', '川味', '口味温和', '微辣', '咸鲜', '酸甜', '下饭菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3477

## Hybrid Branch Status / entity_level
- keywords: ['鱼香肉丝', '宫保鸡丁', '回锅肉', '麻婆豆腐', '甜皮鸭', '辣椒', '花椒']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 55

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '川味', '口味温和', '微辣', '咸鲜', '酸甜', '下饭菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 67

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 368

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 23
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 5
- doc_names: ['如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 24
- duration_ms: 14724
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '通用知识': 1, '主食,凉菜': 1, '荤菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 凉粉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18604
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:25:55.734
- end: 2026-08-11T18:26:23.415
- duration_ms: 27680
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1489
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
- chunk_count: 247
- redacted_field: 2055
- total_duration_ms: 5951
- fallback_used: False

## Final Output
- answer_chars: 307
- answer_hash: 00778a21735b1ee7
- success: True

## Request Complete
- request_end: 2026-08-11T18:26:29.381
- request_duration_ms: 33648
- success: True
- final_source: generation

