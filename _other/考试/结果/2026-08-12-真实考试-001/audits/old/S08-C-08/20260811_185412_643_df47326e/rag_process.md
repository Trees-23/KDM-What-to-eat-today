# RAG Process

audit_id: 20260811_185412_643_df47326e
timestamp: 2026-08-11T18:54:12.644
## Request
- original_query: 请查云岚28号幻味砂锅的做法；未收录时只说明未找到，不要根据名称猜配方。
- original_query_hash: 15a46db7763fd499
- session_id: 2026-08-12-真实考试-001:old:S08-C-08
- request_mode: stream
- request_start: 2026-08-11T18:54:12.646
- evaluation_sample_id: 20260811_185412_643_df47326e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:54:12.647
- end: 2026-08-11T18:54:12.647
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:54:12.648
- end: 2026-08-11T18:54:12.648
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 15a46db7763fd499

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:54:12.649
- end: 2026-08-11T18:54:12.649
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 15a46db7763fd499
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:54:12.650
- end: 2026-08-11T18:54:19.660
- duration_ms: 7010
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.1
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是针对“云岚28号幻味砂锅”这一特定菜品名称的精确做法检索，目标明确，不涉及多实体关系、多跳推理、因果分析或对比分析。查询还明确要求在知识库未收录时仅返回未找到，因此应优先采用关键词精确匹配、别名匹配与向量语义召回结合的 hybrid_traditional 策略；若检索结果无法确认该菜品及其做法，应输出未找到，避免基于名称生成或猜测配方。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 192, 'graph_rag_count': 33, 'total_queries': 225}
- route_stats_after: {'traditional_count': 193, 'graph_rag_count': 33, 'total_queries': 226}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚28号幻味砂锅']
- topic_keywords: []
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3509

## Hybrid Branch Status / entity_level
- keywords: ['云岚28号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / topic_level
- keywords: []
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 386

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
- duration_ms: 14827
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '烹饪技巧': 1, '汤类': 1, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 水油焖蔬菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18743
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:54:12.650
- end: 2026-08-11T18:54:38.404
- duration_ms: 25754
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1739
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
- chunk_count: 17
- redacted_field: 2617
- total_duration_ms: 3113
- fallback_used: False

## Final Output
- answer_chars: 20
- answer_hash: 7c56c6995667c592
- success: True

## Request Complete
- request_end: 2026-08-11T18:54:41.545
- request_duration_ms: 28899
- success: True
- final_source: generation

