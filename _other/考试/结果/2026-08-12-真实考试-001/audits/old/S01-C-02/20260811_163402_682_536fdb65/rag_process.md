# RAG Process

audit_id: 20260811_163402_682_536fdb65
timestamp: 2026-08-11T16:34:02.682
## Request
- original_query: 我只要知识库能证明的炸酱面做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: d0798846537321a5
- session_id: 2026-08-12-真实考试-001:old:S01-C-02
- request_mode: stream
- request_start: 2026-08-11T16:34:02.682
- evaluation_sample_id: 20260811_163402_682_536fdb65
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:34:02.683
- end: 2026-08-11T16:34:02.683
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:34:02.683
- end: 2026-08-11T16:34:02.683
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 34
- enhanced_query_length: 34
- enhanced_query_hash: d0798846537321a5

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:34:02.684
- end: 2026-08-11T16:34:02.684
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 34
- analysis_input_query_hash: d0798846537321a5
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:34:02.684
- end: 2026-08-11T16:34:13.893
- duration_ms: 11208
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.2
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询的核心目标是检索“炸酱面做法”，属于单一菜品的直接事实查找；同时带有严格的证据约束：回答中的步骤、配料和结论必须能够由知识库内容明确支持，且不得补充无引用的替代方案或营养结论。该任务需要进行检索结果筛选、证据对齐与引用完整性校验，但不需要多跳关系推理、因果分析或跨实体对比。明确实体包括“炸酱面”（菜品）和“知识库”（证据来源/信息资源）。建议采用hybrid_traditional，通过关键词检索与语义检索召回做法文档，再仅抽取有明确知识库依据的内容生成答案并附带引用。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 21, 'graph_rag_count': 0, 'total_queries': 21}
- route_stats_after: {'traditional_count': 22, 'graph_rag_count': 0, 'total_queries': 22}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['我只要知识库能证明的炸酱面做法；不要补充未引用的替代方案或营养结论。']
- topic_keywords: ['我只要知识库能证明的炸酱面做法；不要补充未引用的替代方案或营养结论。']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8335

## Hybrid Branch Status / entity_level
- keywords: ['我只要知识库能证明的炸酱面做法；不要补充未引用的替代方案或营养结论。']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 90

## Hybrid Branch Status / topic_level
- keywords: ['我只要知识库能证明的炸酱面做法；不要补充未引用的替代方案或营养结论。']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 168

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 658

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 0
- vector_count: 10
- origin_len: 10

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 10
- after_count: 9
- duplicate_count: 1

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['去腥', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 16232
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '烹饪技巧': 2, '荤菜': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25249
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:34:02.684
- end: 2026-08-11T16:34:39.145
- duration_ms: 36460
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2247
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
- chunk_count: 216
- redacted_field: 4590
- total_duration_ms: 9142
- fallback_used: False

## Final Output
- answer_chars: 319
- answer_hash: 814e120396d878a5
- success: True

## Request Complete
- request_end: 2026-08-11T16:34:48.334
- request_duration_ms: 45651
- success: True
- final_source: generation

