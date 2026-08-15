# RAG Process

audit_id: 20260811_173931_169_686b9dbf
timestamp: 2026-08-11T17:39:31.170
## Request
- original_query: 有米饭可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 57534d04268415b3
- session_id: 2026-08-12-真实考试-001:old:S04-B-08
- request_mode: stream
- request_start: 2026-08-11T17:39:31.170
- evaluation_sample_id: 20260811_173931_169_686b9dbf
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:39:31.170
- end: 2026-08-11T17:39:31.170
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:39:31.171
- end: 2026-08-11T17:39:31.171
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 57534d04268415b3

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:39:31.171
- end: 2026-08-11T17:39:31.171
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 20
- analysis_input_query_hash: 57534d04268415b3
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:39:31.171
- end: 2026-08-11T17:39:45.918
- duration_ms: 14746
- analysis_mode: llm
- query_complexity: 0.48
- relationship_intensity: 0.52
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询的核心实体是“米饭”和“菜谱/菜品”。用户一方面希望发现可由米饭制作的菜品，另一方面要求验证推荐菜谱的配料表中确实包含米饭。这属于带有配料约束和结果验证的中等复杂度检索任务，但不涉及多跳知识推理、因果分析或多实体关系网络建模。适合使用关键词检索结合语义召回，并通过菜谱结构化字段或正文中的配料清单进行过滤与证据校验，因此推荐 hybrid_traditional。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 106, 'graph_rag_count': 1, 'total_queries': 107}
- route_stats_after: {'traditional_count': 107, 'graph_rag_count': 1, 'total_queries': 108}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['米饭', '炒饭', '焗饭', '饭团', '盖浇饭', '蛋炒饭']
- topic_keywords: ['剩饭利用', '主食', '快手菜', '米饭食谱']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 7927

## Hybrid Branch Status / entity_level
- keywords: ['米饭', '炒饭', '焗饭', '饭团', '盖浇饭', '蛋炒饭']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 16

## Hybrid Branch Status / topic_level
- keywords: ['剩饭利用', '主食', '快手菜', '米饭食谱']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 32

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 289

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 10
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 20
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 6
- doc_names: ['蒸（米）/炖（使用电饭煲/高压锅/电压力锅）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 21
- duration_ms: 17366
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '烹饪技巧': 2, 'Ingredient': 1}
- deferred_count: 6
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25606
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:39:31.171
- end: 2026-08-11T17:40:11.525
- duration_ms: 40354
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2707
- retrieval_levels: ['', 'context_expansion', 'entity', 'topic']
- search_types: ['entity_level', 'technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 371
- redacted_field: 6213
- total_duration_ms: 13654
- fallback_used: False

## Final Output
- answer_chars: 435
- answer_hash: 60eb6f84b6c85841
- success: True

## Request Complete
- request_end: 2026-08-11T17:40:25.202
- request_duration_ms: 54032
- success: True
- final_source: generation

