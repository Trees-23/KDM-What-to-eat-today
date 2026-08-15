# RAG Process

audit_id: 20260811_163605_991_677fbb13
timestamp: 2026-08-11T16:36:05.994
## Request
- original_query: 我只要知识库能证明的西红柿鸡蛋汤做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: 5ea0bfc40944e677
- session_id: 2026-08-12-真实考试-001:old:S01-C-05
- request_mode: stream
- request_start: 2026-08-11T16:36:05.995
- evaluation_sample_id: 20260811_163605_991_677fbb13
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:36:05.995
- end: 2026-08-11T16:36:05.995
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:36:05.995
- end: 2026-08-11T16:36:05.995
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: 5ea0bfc40944e677

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:36:05.996
- end: 2026-08-11T16:36:05.996
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 37
- analysis_input_query_hash: 5ea0bfc40944e677
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:36:05.996
- end: 2026-08-11T16:36:14.049
- duration_ms: 8052
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心是对“西红柿鸡蛋汤”做法进行直接检索，并要求所有步骤均可由知识库证据支持。明确实体包括西红柿、鸡蛋和西红柿鸡蛋汤。无需多跳推理、因果分析或不同方案的对比分析；但需要进行证据约束校验：仅保留可检索到引用依据的做法内容，过滤未经引用支持的替代方案和营养结论。因此适合使用 hybrid_traditional，通过关键词/语义检索召回菜谱与步骤，再依据来源证据进行引用覆盖筛选。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 24, 'graph_rag_count': 0, 'total_queries': 24}
- route_stats_after: {'traditional_count': 25, 'graph_rag_count': 0, 'total_queries': 25}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['西红柿鸡蛋汤', '西红柿', '鸡蛋']
- topic_keywords: ['做法', '知识库依据', '引用', '可验证性']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4098

## Hybrid Branch Status / entity_level
- keywords: ['西红柿鸡蛋汤', '西红柿', '鸡蛋']
- requested_k: 10
- actual_count: 3
- fallback_count: 0
- duration_ms: 25

## Hybrid Branch Status / topic_level
- keywords: ['做法', '知识库依据', '引用', '可验证性']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 49

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 697

## Hybrid Branch Summary
- entity_count: 3
- topic_count: 8
- vector_count: 10
- origin_len: 21

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 21
- after_count: 16
- duplicate_count: 5

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
- candidate_count: 17
- duration_ms: 13737
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'汤类': 2, '素菜': 2, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 番茄牛肉蛋花汤
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18551
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:36:05.996
- end: 2026-08-11T16:36:32.601
- duration_ms: 26605
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2211
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
- chunk_count: 245
- redacted_field: 8731
- total_duration_ms: 12622
- fallback_used: False

## Final Output
- answer_chars: 316
- answer_hash: 24a7f99ed04b37fe
- success: True

## Request Complete
- request_end: 2026-08-11T16:36:45.251
- request_duration_ms: 39256
- success: True
- final_source: generation

