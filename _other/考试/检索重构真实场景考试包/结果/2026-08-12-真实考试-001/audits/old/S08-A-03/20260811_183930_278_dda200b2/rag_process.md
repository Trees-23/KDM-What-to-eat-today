# RAG Process

audit_id: 20260811_183930_278_dda200b2
timestamp: 2026-08-11T18:39:30.279
## Request
- original_query: 云岚03号幻味砂锅怎么做？
- original_query_hash: 27a78b4acc02eb88
- session_id: 2026-08-12-真实考试-001:old:S08-A-03
- request_mode: stream
- request_start: 2026-08-11T18:39:30.279
- evaluation_sample_id: 20260811_183930_278_dda200b2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:39:30.280
- end: 2026-08-11T18:39:30.280
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:39:30.281
- end: 2026-08-11T18:39:30.281
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 13
- enhanced_query_length: 13
- enhanced_query_hash: 27a78b4acc02eb88

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:39:30.282
- end: 2026-08-11T18:39:30.282
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 13
- analysis_input_query_hash: 27a78b4acc02eb88
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:39:30.282
- end: 2026-08-11T18:39:37.271
- duration_ms: 6989
- analysis_mode: llm
- query_complexity: 0.22
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询本质上是对“云岚03号幻味砂锅”这一具体菜品/配方名称的制作方法进行直接查找，目标明确，预期答案为食材、步骤、火候和调味等操作信息。查询中虽可能存在菜名非标准、品牌化或编码化导致的实体消歧需求，但不涉及多个实体之间的复杂关联、多跳推理、因果分析或对比分析，适合采用关键词检索与语义检索结合的hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 167, 'graph_rag_count': 33, 'total_queries': 200}
- route_stats_after: {'traditional_count': 168, 'graph_rag_count': 33, 'total_queries': 201}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚03号幻味砂锅', '砂锅']
- topic_keywords: ['砂锅菜', '烹饪方法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5857

## Hybrid Branch Status / entity_level
- keywords: ['云岚03号幻味砂锅', '砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 9

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '烹饪方法']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 9

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 430

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
- duration_ms: 15562
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, '半成品': 1, '高级技巧': 1, '荤菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 西红柿牛腩
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21869
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:39:30.282
- end: 2026-08-11T18:39:59.142
- duration_ms: 28859
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3529
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
- chunk_count: 608
- redacted_field: 4534
- total_duration_ms: 16789
- fallback_used: False

## Final Output
- answer_chars: 795
- answer_hash: 335913f28e894e77
- success: True

## Request Complete
- request_end: 2026-08-11T18:40:15.956
- request_duration_ms: 45676
- success: True
- final_source: generation

