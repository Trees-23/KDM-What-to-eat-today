# RAG Process

audit_id: 20260811_185213_990_8f2a55d8
timestamp: 2026-08-11T18:52:13.992
## Request
- original_query: 请查云岚24号幻味砂锅的做法；未收录时只说明未找到，不要根据名称猜配方。
- original_query_hash: 825b2a1ef103ea5f
- session_id: 2026-08-12-真实考试-001:old:S08-C-04
- request_mode: stream
- request_start: 2026-08-11T18:52:13.993
- evaluation_sample_id: 20260811_185213_990_8f2a55d8
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:52:13.993
- end: 2026-08-11T18:52:13.993
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:52:13.993
- end: 2026-08-11T18:52:13.993
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 825b2a1ef103ea5f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:52:13.994
- end: 2026-08-11T18:52:13.994
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 825b2a1ef103ea5f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:52:13.994
- end: 2026-08-11T18:52:21.934
- duration_ms: 7940
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对“云岚24号”与“幻味砂锅”这一特定菜品/记录的精确做法检索，核心需求是确认知识库是否收录并返回原始配方信息。查询明确要求未收录时仅返回未找到，禁止依据菜名进行语义补全或配方猜测，因此不需要多跳推理、因果分析或对比分析。建议采用 hybrid_traditional，通过关键词精确匹配、别名匹配及向量召回后进行严格的实体一致性校验；若无可靠收录结果则执行拒答/未找到策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 188, 'graph_rag_count': 33, 'total_queries': 221}
- route_stats_after: {'traditional_count': 189, 'graph_rag_count': 33, 'total_queries': 222}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚24号幻味砂锅']
- topic_keywords: ['菜谱']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2353

## Hybrid Branch Status / entity_level
- keywords: ['云岚24号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 3

## Hybrid Branch Status / topic_level
- keywords: ['菜谱']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 8

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 536

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 1
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 11
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
- candidate_count: 12
- duration_ms: 16385
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
- hybrid_total_duration_ms: 19293
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:52:13.994
- end: 2026-08-11T18:52:41.228
- duration_ms: 27234
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
- redacted_field: 1732
- total_duration_ms: 2132
- fallback_used: False

## Final Output
- answer_chars: 20
- answer_hash: cec9b0a55170a230
- success: True

## Request Complete
- request_end: 2026-08-11T18:52:43.379
- request_duration_ms: 29386
- success: True
- final_source: generation

