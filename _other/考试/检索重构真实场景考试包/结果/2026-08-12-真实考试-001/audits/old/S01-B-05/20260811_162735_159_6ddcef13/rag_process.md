# RAG Process

audit_id: 20260811_162735_159_6ddcef13
timestamp: 2026-08-11T16:27:35.162
## Request
- original_query: 蚝油生菜从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: dbd35521ee182f2c
- session_id: 2026-08-12-真实考试-001:old:S01-B-05
- request_mode: stream
- request_start: 2026-08-11T16:27:35.162
- evaluation_sample_id: 20260811_162735_159_6ddcef13
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:27:35.163
- end: 2026-08-11T16:27:35.163
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:27:35.163
- end: 2026-08-11T16:27:35.163
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: dbd35521ee182f2c

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:27:35.163
- end: 2026-08-11T16:27:35.163
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: dbd35521ee182f2c
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:27:35.164
- end: 2026-08-11T16:27:44.026
- duration_ms: 8862
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.4
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询是面向特定菜品“蚝油生菜”的标准做法检索，核心诉求是按知识库内容获取从备料、处理、烹饪到出锅的线性步骤。查询中的明确实体包括“蚝油生菜”（菜品）、“蚝油”（调味料）和“生菜”（食材）。虽包含食材、调味料与制作步骤之间的基本关联，但不涉及跨文档的复杂实体网络、因果归因或对比判断，也不需要多跳推理。适合通过关键词检索、菜品标题匹配及步骤片段召回的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 14, 'graph_rag_count': 0, 'total_queries': 14}
- route_stats_after: {'traditional_count': 15, 'graph_rag_count': 0, 'total_queries': 15}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['蚝油生菜', '生菜', '蚝油']
- topic_keywords: ['家常菜', '素菜', '快手菜', '烹饪步骤', '火候', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6670

## Hybrid Branch Status / entity_level
- keywords: ['蚝油生菜', '生菜', '蚝油']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 24

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '素菜', '快手菜', '烹饪步骤', '火候', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 50

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 477

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 10
- vector_count: 10
- origin_len: 23

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 23
- after_count: 16
- duplicate_count: 7

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 8
- doc_names: ['炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 17
- duration_ms: 17193
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '水产': 1, '烹饪技巧': 1, '调料': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 炸串酱料
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24572
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:27:35.164
- end: 2026-08-11T16:28:08.600
- duration_ms: 33436
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2952
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
- chunk_count: 404
- redacted_field: 1956
- total_duration_ms: 10316
- fallback_used: False

## Final Output
- answer_chars: 568
- answer_hash: 1a9ebda2cce4a9df
- success: True

## Request Complete
- request_end: 2026-08-11T16:28:18.951
- request_duration_ms: 43788
- success: True
- final_source: generation

