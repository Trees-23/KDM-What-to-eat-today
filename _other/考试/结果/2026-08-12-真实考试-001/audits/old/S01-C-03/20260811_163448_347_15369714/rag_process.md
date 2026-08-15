# RAG Process

audit_id: 20260811_163448_347_15369714
timestamp: 2026-08-11T16:34:48.348
## Request
- original_query: 我只要知识库能证明的牛奶燕麦做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 51bed27bd3e54479
- session_id: 2026-08-12-真实考试-001:old:S01-C-03
- request_mode: stream
- request_start: 2026-08-11T16:34:48.348
- evaluation_sample_id: 20260811_163448_347_15369714
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:34:48.348
- end: 2026-08-11T16:34:48.348
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:34:48.349
- end: 2026-08-11T16:34:48.349
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: 51bed27bd3e54479

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:34:48.349
- end: 2026-08-11T16:34:48.349
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: 51bed27bd3e54479
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:34:48.349
- end: 2026-08-11T16:34:57.167
- duration_ms: 8817
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 查询核心是检索知识库中关于“牛奶燕麦做法”的明确证据，并严格满足“仅输出可被知识库引用证明的内容、不得补充替代方案或营养结论”的证据约束。其重点是关键词/语义召回、文档片段定位、引用可追溯性校验与生成时的事实约束，而非多个实体之间的复杂关系发现或多跳图推理。明确实体包括牛奶、燕麦和做法（食谱/制作步骤）；“知识库证明”和“引用”属于检索与证据要求。虽然需要进行引用一致性过滤，因此存在轻度证据校验推理，但不需要因果分析、对比分析或多跳推理，适合采用hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 22, 'graph_rag_count': 0, 'total_queries': 22}
- route_stats_after: {'traditional_count': 23, 'graph_rag_count': 0, 'total_queries': 23}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['牛奶', '燕麦']
- topic_keywords: ['牛奶燕麦做法', '知识库依据', '引用证据', '可验证性']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4588

## Hybrid Branch Status / topic_level
- keywords: ['牛奶燕麦做法', '知识库依据', '引用证据', '可验证性']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 11

## Hybrid Branch Status / entity_level
- keywords: ['牛奶', '燕麦']
- requested_k: 10
- actual_count: 2
- fallback_count: 0
- duration_ms: 21

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 543

## Hybrid Branch Summary
- entity_count: 2
- topic_count: 0
- vector_count: 10
- origin_len: 12

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 12
- after_count: 9
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 11412
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'早餐': 2, '烹饪技巧': 2, 'Ingredient': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 16561
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:34:48.349
- end: 2026-08-11T16:35:13.730
- duration_ms: 25381
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2320
- retrieval_levels: ['', 'context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion', 'vector_enhanced']
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
- chunk_count: 451
- redacted_field: 5913
- total_duration_ms: 16880
- fallback_used: False

## Final Output
- answer_chars: 556
- answer_hash: 386bac737abd86bd
- success: True

## Request Complete
- request_end: 2026-08-11T16:35:30.629
- request_duration_ms: 42281
- success: True
- final_source: generation

