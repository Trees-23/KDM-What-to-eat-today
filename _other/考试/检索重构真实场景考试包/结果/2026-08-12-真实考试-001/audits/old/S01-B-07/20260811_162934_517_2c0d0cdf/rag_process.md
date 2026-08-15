# RAG Process

audit_id: 20260811_162934_517_2c0d0cdf
timestamp: 2026-08-11T16:29:34.519
## Request
- original_query: 干锅花菜从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 47574e889fb5ff45
- session_id: 2026-08-12-真实考试-001:old:S01-B-07
- request_mode: stream
- request_start: 2026-08-11T16:29:34.520
- evaluation_sample_id: 20260811_162934_517_2c0d0cdf
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:29:34.521
- end: 2026-08-11T16:29:34.521
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:29:34.521
- end: 2026-08-11T16:29:34.521
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 47574e889fb5ff45

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:29:34.522
- end: 2026-08-11T16:29:34.522
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 47574e889fb5ff45
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:29:34.522
- end: 2026-08-11T16:29:47.242
- duration_ms: 12720
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询是针对“干锅花菜”单一道菜的标准制作流程检索，用户明确要求按知识库中的做法回答。核心需求是获取从“备料”到“出锅”的顺序化步骤，而非进行跨实体关联、因果解释或菜品对比。明确实体包括：干锅花菜（菜品）、备料（烹饪阶段）、出锅（烹饪阶段）。适合通过关键词检索、菜品名称匹配及步骤字段召回的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 16, 'graph_rag_count': 0, 'total_queries': 16}
- route_stats_after: {'traditional_count': 17, 'graph_rag_count': 0, 'total_queries': 17}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['干锅花菜', '花菜', '五花肉', '干辣椒', '蒜苗', '豆瓣酱', '干锅']
- topic_keywords: ['川菜', '香辣', '下饭菜', '家常菜', '烹饪技巧', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3949

## Hybrid Branch Status / entity_level
- keywords: ['干锅花菜', '花菜', '五花肉', '干辣椒', '蒜苗', '豆瓣酱', '干锅']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 90

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '香辣', '下饭菜', '家常菜', '烹饪技巧', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 98

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 505

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 22
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['炒/煎', '辅料技巧']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 23
- duration_ms: 18997
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '烹饪技巧': 2, '高级技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 清炒花菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 23478
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:29:34.522
- end: 2026-08-11T16:30:10.722
- duration_ms: 36200
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3331
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
- chunk_count: 479
- redacted_field: 4797
- total_duration_ms: 16082
- fallback_used: False

## Final Output
- answer_chars: 645
- answer_hash: 806e2080c1c61dc8
- success: True

## Request Complete
- request_end: 2026-08-11T16:30:26.844
- request_duration_ms: 52324
- success: True
- final_source: generation

