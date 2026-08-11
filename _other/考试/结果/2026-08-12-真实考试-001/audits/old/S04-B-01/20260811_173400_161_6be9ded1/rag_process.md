# RAG Process

audit_id: 20260811_173400_161_6be9ded1
timestamp: 2026-08-11T17:34:00.163
## Request
- original_query: 有鳜鱼可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 99b28f6354dc7828
- session_id: 2026-08-12-真实考试-001:old:S04-B-01
- request_mode: stream
- request_start: 2026-08-11T17:34:00.163
- evaluation_sample_id: 20260811_173400_161_6be9ded1
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:34:00.164
- end: 2026-08-11T17:34:00.164
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:34:00.164
- end: 2026-08-11T17:34:00.164
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 99b28f6354dc7828

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:34:00.164
- end: 2026-08-11T17:34:00.164
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: 99b28f6354dc7828
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:34:00.164
- end: 2026-08-11T17:34:15.006
- duration_ms: 14841
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.55
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是以“鳜鱼”为主食材，检索可制作的菜品及明确在配方或食材表中包含鳜鱼的菜谱。它涉及“食材—菜品/菜谱”的一对多关系，并需要对检索结果进行食材包含性验证，但不涉及复杂的多跳知识推理、因果分析或关系网络发现。适合采用关键词检索、同义词扩展（如桂鱼、桂花鱼）与结构化食材字段过滤相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 99, 'graph_rag_count': 1, 'total_queries': 100}
- route_stats_after: {'traditional_count': 100, 'graph_rag_count': 1, 'total_queries': 101}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鳜鱼', '松鼠鳜鱼', '清蒸鳜鱼', '红烧鳜鱼', '臭鳜鱼', '鳜鱼豆腐汤']
- topic_keywords: ['鱼类菜肴', '江浙菜', '徽菜', '家常菜', '宴客菜', '菜谱']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5151

## Hybrid Branch Status / entity_level
- keywords: ['鳜鱼', '松鼠鳜鱼', '清蒸鳜鱼', '红烧鳜鱼', '臭鳜鱼', '鳜鱼豆腐汤']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 21

## Hybrid Branch Status / topic_level
- keywords: ['鱼类菜肴', '江浙菜', '徽菜', '家常菜', '宴客菜', '菜谱']
- requested_k: 10
- actual_count: 4
- fallback_count: 3
- duration_ms: 41

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 702

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 4
- vector_count: 10
- origin_len: 16

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 16
- after_count: 14
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 0
- expanded_count: 0

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 19561
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '水产': 2, 'Ingredient': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25435
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:34:00.164
- end: 2026-08-11T17:34:40.442
- duration_ms: 40277
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2694
- retrieval_levels: ['', 'entity']
- search_types: ['entity_level', 'vector_enhanced']
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
- chunk_count: 289
- redacted_field: 9062
- total_duration_ms: 15180
- fallback_used: False

## Final Output
- answer_chars: 351
- answer_hash: 16a6a72ffc38be41
- success: True

## Request Complete
- request_end: 2026-08-11T17:34:55.648
- request_duration_ms: 55485
- success: True
- final_source: generation

