# RAG Process

audit_id: 20260811_185243_394_8eab0b95
timestamp: 2026-08-11T18:52:43.395
## Request
- original_query: 请查云岚25号幻味砂锅的做法；未收录时只说明未找到，不要根据名称猜配方。
- original_query_hash: 8e3cdebea1faafb8
- session_id: 2026-08-12-真实考试-001:old:S08-C-05
- request_mode: stream
- request_start: 2026-08-11T18:52:43.395
- evaluation_sample_id: 20260811_185243_394_8eab0b95
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:52:43.396
- end: 2026-08-11T18:52:43.396
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:52:43.396
- end: 2026-08-11T18:52:43.396
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 8e3cdebea1faafb8

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:52:43.397
- end: 2026-08-11T18:52:43.397
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 8e3cdebea1faafb8
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:52:43.397
- end: 2026-08-11T18:52:50.360
- duration_ms: 6962
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.1
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对明确菜品实体“云岚25号幻味砂锅”的做法进行精确检索，核心需求为判断知识库中是否收录并返回对应内容。用户明确要求未收录时仅说明未找到，禁止依据名称进行配方猜测，因此应采用关键词精确匹配、别名匹配与语义检索相结合的传统混合检索策略，并设置严格的证据阈值与无结果兜底。查询不涉及多实体关系、因果分析、对比分析或多跳推理。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 189, 'graph_rag_count': 33, 'total_queries': 222}
- route_stats_after: {'traditional_count': 190, 'graph_rag_count': 33, 'total_queries': 223}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚25号幻味砂锅']
- topic_keywords: []
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3407

## Hybrid Branch Status / topic_level
- keywords: []
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 1

## Hybrid Branch Status / entity_level
- keywords: ['云岚25号幻味砂锅']
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
- duration_ms: 657

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
- duration_ms: 14441
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '烹饪技巧': 1, '汤类': 1, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 韭菜盒子
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18525
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:52:43.397
- end: 2026-08-11T18:53:08.886
- duration_ms: 25489
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
- redacted_field: 1835
- total_duration_ms: 2249
- fallback_used: False

## Final Output
- answer_chars: 20
- answer_hash: 3c305469192d035f
- success: True

## Request Complete
- request_end: 2026-08-11T18:53:11.158
- request_duration_ms: 27762
- success: True
- final_source: generation

