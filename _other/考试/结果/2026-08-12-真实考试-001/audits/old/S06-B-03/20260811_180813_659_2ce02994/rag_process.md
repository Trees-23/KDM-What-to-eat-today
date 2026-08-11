# RAG Process

audit_id: 20260811_180813_659_2ce02994
timestamp: 2026-08-11T18:08:13.661
## Request
- original_query: 家里人不太能吃辣，晚餐有什么选择，帮我找几个贴近这个需求的做法。
- original_query_hash: c6d5cce12fe86efa
- session_id: 2026-08-12-真实考试-001:old:S06-B-03
- request_mode: stream
- request_start: 2026-08-11T18:08:13.661
- evaluation_sample_id: 20260811_180813_659_2ce02994
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:08:13.662
- end: 2026-08-11T18:08:13.662
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:08:13.662
- end: 2026-08-11T18:08:13.662
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 32
- enhanced_query_length: 32
- enhanced_query_hash: c6d5cce12fe86efa

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:08:13.663
- end: 2026-08-11T18:08:13.663
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 32
- analysis_input_query_hash: c6d5cce12fe86efa
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:08:13.663
- end: 2026-08-11T18:08:21.672
- duration_ms: 8009
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询属于带约束的餐食推荐需求：核心目标是为晚餐寻找多个做法，并需满足“家里人不太能吃辣”的口味限制。查询需要从菜谱、食材和口味标签中筛选、排序并生成贴近家庭晚餐场景的候选方案，存在轻量的条件匹配与推荐推理，但不涉及复杂的多跳知识关系、因果机制或大规模实体网络分析。明确实体可归纳为“家里人（人群/用餐者）”“晚餐（用餐场景）”“辣度/不太能吃辣（饮食口味约束）”。适合采用关键词检索、语义召回及口味标签过滤相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 129, 'graph_rag_count': 33, 'total_queries': 162}
- route_stats_after: {'traditional_count': 130, 'graph_rag_count': 33, 'total_queries': 163}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['清蒸鱼', '番茄炒蛋', '红烧排骨', '鸡蛋羹', '清炒时蔬', '冬瓜汤', '土豆炖牛肉', '蒸鸡腿']
- topic_keywords: ['晚餐', '不辣', '清淡', '家常菜', '适合家人', '营养均衡', '少油少盐']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6452

## Hybrid Branch Status / entity_level
- keywords: ['清蒸鱼', '番茄炒蛋', '红烧排骨', '鸡蛋羹', '清炒时蔬', '冬瓜汤', '土豆炖牛肉', '蒸鸡腿']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 21

## Hybrid Branch Status / topic_level
- keywords: ['晚餐', '不辣', '清淡', '家常菜', '适合家人', '营养均衡', '少油少盐']
- requested_k: 10
- actual_count: 4
- fallback_count: 4
- duration_ms: 32

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 659

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 4
- vector_count: 10
- origin_len: 15

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 15
- after_count: 15
- duplicate_count: 0

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
- candidate_count: 16
- duration_ms: 11086
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'通用知识': 1, '主食': 2, '荤菜': 1, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18220
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:08:13.663
- end: 2026-08-11T18:08:39.894
- duration_ms: 26231
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1620
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
- chunk_count: 490
- redacted_field: 5730
- total_duration_ms: 17403
- fallback_used: False

## Final Output
- answer_chars: 623
- answer_hash: 430f76f06c2c564c
- success: True

## Request Complete
- request_end: 2026-08-11T18:08:57.324
- request_duration_ms: 43662
- success: True
- final_source: generation

