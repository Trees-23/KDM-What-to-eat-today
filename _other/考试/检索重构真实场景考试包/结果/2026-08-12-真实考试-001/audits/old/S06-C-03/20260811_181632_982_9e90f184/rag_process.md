# RAG Process

audit_id: 20260811_181632_982_9e90f184
timestamp: 2026-08-11T18:16:32.982
## Request
- original_query: 想吃豆腐类菜，又不想太寡淡。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: 7e495a682471ff38
- session_id: 2026-08-12-真实考试-001:old:S06-C-03
- request_mode: stream
- request_start: 2026-08-11T18:16:32.983
- evaluation_sample_id: 20260811_181632_982_9e90f184
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:16:32.984
- end: 2026-08-11T18:16:32.984
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:16:32.984
- end: 2026-08-11T18:16:32.984
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 44
- enhanced_query_length: 44
- enhanced_query_hash: 7e495a682471ff38

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:16:32.985
- end: 2026-08-11T18:16:32.985
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 44
- analysis_input_query_hash: 7e495a682471ff38
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:16:32.985
- end: 2026-08-11T18:16:42.900
- duration_ms: 9915
- analysis_mode: llm
- query_complexity: 0.62
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 该查询以“豆腐类菜”为核心对象，并附加“不要太寡淡”的口味约束，要求系统从菜品资料中筛选同时满足食材类别与风味特征的候选项，并为每项提供可追溯的推荐依据。推理主要是基于文档字段、菜品描述、调味料和烹饪方式进行约束匹配与候选对比，不需要构建跨多实体的复杂关系网络或进行多跳知识发现。应优先检索包含豆腐、调味方式、口味描述及菜品做法的信息，并仅将资料明确支持的“咸鲜、香辣、酱香、麻辣、浓郁”等特征作为依据；资料未说明风味时，应标注信息不足而非推断其不寡淡。因此更适合采用 hybrid_traditional，通过关键词/结构化字段过滤结合语义检索与证据重排序实现。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 139, 'graph_rag_count': 33, 'total_queries': 172}
- route_stats_after: {'traditional_count': 140, 'graph_rag_count': 33, 'total_queries': 173}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['豆腐']
- topic_keywords: ['豆腐菜', '浓郁风味', '咸香', '香辣', '下饭菜', '推荐依据']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 5128

## Hybrid Branch Status / entity_level
- keywords: ['豆腐']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 12

## Hybrid Branch Status / topic_level
- keywords: ['豆腐菜', '浓郁风味', '咸香', '香辣', '下饭菜', '推荐依据']
- requested_k: 10
- actual_count: 4
- fallback_count: 4
- duration_ms: 21

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 536

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 4
- vector_count: 10
- origin_len: 15

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 15
- after_count: 13
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['去腥', '如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 14
- duration_ms: 15251
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 1, '通用知识': 1, '主食': 2, '素菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 凉拌豆腐
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20941
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:16:32.985
- end: 2026-08-11T18:17:03.843
- duration_ms: 30857
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2089
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
- chunk_count: 636
- redacted_field: 4603
- total_duration_ms: 17302
- fallback_used: False

## Final Output
- answer_chars: 804
- answer_hash: 6fb00bb5e42c7e25
- success: True

## Request Complete
- request_end: 2026-08-11T18:17:21.163
- request_duration_ms: 48180
- success: True
- final_source: generation

