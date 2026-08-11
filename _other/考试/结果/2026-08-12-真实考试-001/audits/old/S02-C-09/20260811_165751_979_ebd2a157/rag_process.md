# RAG Process

audit_id: 20260811_165751_979_ebd2a157
timestamp: 2026-08-11T16:57:51.979
## Request
- original_query: 只回答烤蛋挞的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: e0a391406a4dc0ce
- session_id: 2026-08-12-真实考试-001:old:S02-C-09
- request_mode: stream
- request_start: 2026-08-11T16:57:51.979
- evaluation_sample_id: 20260811_165751_979_ebd2a157
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:57:51.980
- end: 2026-08-11T16:57:51.980
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:57:51.980
- end: 2026-08-11T16:57:51.980
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: e0a391406a4dc0ce

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:57:51.980
- end: 2026-08-11T16:57:51.980
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: e0a391406a4dc0ce
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:57:51.981
- end: 2026-08-11T16:58:05.901
- duration_ms: 13920
- analysis_mode: llm
- query_complexity: 0.35
- relationship_intensity: 0.45
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询属于带严格输出约束的定向信息抽取：需定位“烤蛋挞”对应菜谱中的“第1步”，并同时返回该步骤的来源标识，且过滤、禁止输出所有后续步骤。无需多跳推理、因果分析或实体间复杂关系推断，也不需要对比分析；核心是基于菜谱文本进行关键词/菜名匹配、步骤序号定位、来源字段提取和结果截断。因此适合采用 hybrid_traditional，通过关键词检索结合菜谱结构化字段（菜名、步骤序号、来源）进行精确召回与约束过滤。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 58, 'graph_rag_count': 0, 'total_queries': 58}
- route_stats_after: {'traditional_count': 59, 'graph_rag_count': 0, 'total_queries': 59}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['烤蛋挞', '蛋挞']
- topic_keywords: ['菜谱步骤', '烘焙', '步骤溯源']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4093

## Hybrid Branch Status / topic_level
- keywords: ['菜谱步骤', '烘焙', '步骤溯源']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 9

## Hybrid Branch Status / entity_level
- keywords: ['烤蛋挞', '蛋挞']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 483

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 9
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 16101
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'甜品': 2, '半成品': 1, '烹饪技巧': 1, '主食': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 披萨饼皮
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20698
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:57:51.981
- end: 2026-08-11T16:58:26.601
- duration_ms: 34619
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4666
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
- chunk_count: 38
- redacted_field: 2070
- total_duration_ms: 2877
- fallback_used: False

## Final Output
- answer_chars: 49
- answer_hash: 944d9061cdc9cfa9
- success: True

## Request Complete
- request_end: 2026-08-11T16:58:29.511
- request_duration_ms: 37531
- success: True
- final_source: generation

