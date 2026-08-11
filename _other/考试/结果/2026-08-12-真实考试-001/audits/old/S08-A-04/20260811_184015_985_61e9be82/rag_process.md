# RAG Process

audit_id: 20260811_184015_985_61e9be82
timestamp: 2026-08-11T18:40:15.985
## Request
- original_query: 云岚04号幻味砂锅怎么做？
- original_query_hash: 1388160065dc9c0a
- session_id: 2026-08-12-真实考试-001:old:S08-A-04
- request_mode: stream
- request_start: 2026-08-11T18:40:15.986
- evaluation_sample_id: 20260811_184015_985_61e9be82
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:40:15.988
- end: 2026-08-11T18:40:15.988
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:40:15.989
- end: 2026-08-11T18:40:15.989
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 13
- enhanced_query_length: 13
- enhanced_query_hash: 1388160065dc9c0a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:40:15.990
- end: 2026-08-11T18:40:15.990
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 13
- analysis_input_query_hash: 1388160065dc9c0a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:40:15.990
- end: 2026-08-11T18:40:22.846
- duration_ms: 6855
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询核心是获取“云岚04号幻味砂锅”的制作方法，属于针对单一菜品或特定命名配方的直接信息查找，不涉及多个实体之间的复杂关联、因果解释或多跳推理。由于菜名具有较强的专有性和可能的非标准命名特征，建议采用关键词检索与向量语义检索结合的 hybrid_traditional 策略，以提高精确召回菜谱、配料和制作步骤的能力。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 168, 'graph_rag_count': 33, 'total_queries': 201}
- route_stats_after: {'traditional_count': 169, 'graph_rag_count': 33, 'total_queries': 202}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚04号幻味砂锅', '砂锅']
- topic_keywords: ['砂锅菜', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4203

## Hybrid Branch Status / entity_level
- keywords: ['云岚04号幻味砂锅', '砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 8

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '烹饪技巧']
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
- duration_ms: 380

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
- duration_ms: 15623
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
- hybrid_total_duration_ms: 20225
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:40:15.990
- end: 2026-08-11T18:40:43.072
- duration_ms: 27082
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
- chunk_count: 318
- redacted_field: 2481
- total_duration_ms: 8939
- fallback_used: False

## Final Output
- answer_chars: 429
- answer_hash: 2e72b50a5671c295
- success: True

## Request Complete
- request_end: 2026-08-11T18:40:52.026
- request_duration_ms: 36039
- success: True
- final_source: generation

