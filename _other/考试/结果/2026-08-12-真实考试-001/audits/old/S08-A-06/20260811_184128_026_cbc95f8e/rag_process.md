# RAG Process

audit_id: 20260811_184128_026_cbc95f8e
timestamp: 2026-08-11T18:41:28.028
## Request
- original_query: 云岚06号幻味砂锅怎么做？
- original_query_hash: 866349bc6c1f3fa8
- session_id: 2026-08-12-真实考试-001:old:S08-A-06
- request_mode: stream
- request_start: 2026-08-11T18:41:28.028
- evaluation_sample_id: 20260811_184128_026_cbc95f8e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:41:28.030
- end: 2026-08-11T18:41:28.030
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:41:28.031
- end: 2026-08-11T18:41:28.031
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 13
- enhanced_query_length: 13
- enhanced_query_hash: 866349bc6c1f3fa8

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:41:28.032
- end: 2026-08-11T18:41:28.032
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 13
- analysis_input_query_hash: 866349bc6c1f3fa8
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:41:28.032
- end: 2026-08-11T18:41:34.379
- duration_ms: 6346
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询本质上是在询问明确对象“云岚06号幻味砂锅”的制作方法，属于单一实体的直接信息查找。虽然该名称可能是特定游戏、餐厅菜单或内容体系中的专有名称，需要通过关键词匹配、别名召回和语义检索定位对应配方，但通常不需要多跳推理、因果分析或多对象对比，因此推荐使用 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 170, 'graph_rag_count': 33, 'total_queries': 203}
- route_stats_after: {'traditional_count': 171, 'graph_rag_count': 33, 'total_queries': 204}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚06号幻味砂锅', '砂锅']
- topic_keywords: ['砂锅菜', '烹饪方法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4379

## Hybrid Branch Status / entity_level
- keywords: ['云岚06号幻味砂锅', '砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 3

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '烹饪方法']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 3

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 362

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
- seed_count: 1
- expanded_count: 8
- doc_names: ['炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 11
- duration_ms: 15700
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, '荤菜': 2, '半成品': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20454
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:41:28.032
- end: 2026-08-11T18:41:54.834
- duration_ms: 26801
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2668
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
- chunk_count: 738
- redacted_field: 3667
- total_duration_ms: 18362
- fallback_used: False

## Final Output
- answer_chars: 981
- answer_hash: 87076c5e5e97ae37
- success: True

## Request Complete
- request_end: 2026-08-11T18:42:13.210
- request_duration_ms: 45181
- success: True
- final_source: generation

