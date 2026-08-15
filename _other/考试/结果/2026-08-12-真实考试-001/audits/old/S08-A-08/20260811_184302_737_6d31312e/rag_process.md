# RAG Process

audit_id: 20260811_184302_737_6d31312e
timestamp: 2026-08-11T18:43:02.740
## Request
- original_query: 云岚08号幻味砂锅怎么做？
- original_query_hash: 48be6af2f4575257
- session_id: 2026-08-12-真实考试-001:old:S08-A-08
- request_mode: stream
- request_start: 2026-08-11T18:43:02.740
- evaluation_sample_id: 20260811_184302_737_6d31312e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:43:02.741
- end: 2026-08-11T18:43:02.741
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:43:02.741
- end: 2026-08-11T18:43:02.741
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 13
- enhanced_query_length: 13
- enhanced_query_hash: 48be6af2f4575257

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:43:02.742
- end: 2026-08-11T18:43:02.742
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 13
- analysis_input_query_hash: 48be6af2f4575257
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:43:02.743
- end: 2026-08-11T18:43:09.959
- duration_ms: 7216
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.82
- reasoning: 该查询核心是获取特定菜品“云岚08号幻味砂锅”的制作方法，属于直接的步骤/配方信息查找，不需要多跳推理、因果分析或对比分析。实体可整体识别为一个菜品或菜单名称；由于名称可能为品牌菜、创意菜或非标准菜名，适合采用关键词检索结合语义检索的 hybrid_traditional 策略，以匹配菜谱、菜单说明、短视频文本或相关制作教程。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 172, 'graph_rag_count': 33, 'total_queries': 205}
- route_stats_after: {'traditional_count': 173, 'graph_rag_count': 33, 'total_queries': 206}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚08号幻味砂锅', '砂锅']
- topic_keywords: ['砂锅菜', '烹饪方法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3847

## Hybrid Branch Status / entity_level
- keywords: ['云岚08号幻味砂锅', '砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 7

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '烹饪方法']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 7

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 542

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 0
- vector_count: 10
- origin_len: 10

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 10
- after_count: 10
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['糖色的炒制', '炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 11
- duration_ms: 16189
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, '半成品': 1, '荤菜': 2, '高级技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 西红柿土豆炖牛肉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20597
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:43:02.743
- end: 2026-08-11T18:43:30.558
- duration_ms: 27814
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3520
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
- chunk_count: 318
- redacted_field: 2596
- total_duration_ms: 8759
- fallback_used: False

## Final Output
- answer_chars: 426
- answer_hash: 7c97a57b8bd0641d
- success: True

## Request Complete
- request_end: 2026-08-11T18:43:39.328
- request_duration_ms: 36587
- success: True
- final_source: generation

