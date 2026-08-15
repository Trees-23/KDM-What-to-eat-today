# RAG Process

audit_id: 20260811_163121_231_1ffaed4d
timestamp: 2026-08-11T16:31:21.239
## Request
- original_query: 扬州炒饭从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 5b2e59aed9500e0e
- session_id: 2026-08-12-真实考试-001:old:S01-B-09
- request_mode: stream
- request_start: 2026-08-11T16:31:21.239
- evaluation_sample_id: 20260811_163121_231_1ffaed4d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:31:21.240
- end: 2026-08-11T16:31:21.240
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:31:21.240
- end: 2026-08-11T16:31:21.240
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 5b2e59aed9500e0e

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:31:21.241
- end: 2026-08-11T16:31:21.241
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 5b2e59aed9500e0e
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:31:21.241
- end: 2026-08-11T16:31:26.819
- duration_ms: 5578
- analysis_mode: llm
- query_complexity: 0.32
- relationship_intensity: 0.28
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.93
- reasoning: 该查询是面向特定菜品“扬州炒饭”的流程型做法检索，要求覆盖备料、处理、炒制到出锅等连续步骤，并限定“按知识库里的做法回答”。核心需求是从知识库中精准召回对应菜谱、食材清单与操作步骤，再按步骤顺序组织答案。虽存在食材、调料与烹饪步骤之间的基本关联，但不需要跨多个实体进行复杂关系发现、因果归因或多跳推理，也不涉及不同方案的比较。因此适合采用hybrid_traditional，通过关键词检索、语义检索及步骤字段匹配获取权威菜谱内容。明确实体主要包括：扬州炒饭（菜品）、备料（烹饪流程阶段）、出锅（烹饪流程阶段）。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 18, 'graph_rag_count': 0, 'total_queries': 18}
- route_stats_after: {'traditional_count': 19, 'graph_rag_count': 0, 'total_queries': 19}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['扬州炒饭', '米饭', '鸡蛋', '火腿', '虾仁', '豌豆', '胡萝卜', '炒锅']
- topic_keywords: ['炒饭', '淮扬菜', '烹饪技巧', '备料', '火候', '炒制']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4143

## Hybrid Branch Status / topic_level
- keywords: ['炒饭', '淮扬菜', '烹饪技巧', '备料', '火候', '炒制']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 50

## Hybrid Branch Status / entity_level
- keywords: ['扬州炒饭', '米饭', '鸡蛋', '火腿', '虾仁', '豌豆', '胡萝卜', '炒锅']
- requested_k: 10
- actual_count: 7
- fallback_count: 0
- duration_ms: 73

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 409

## Hybrid Branch Summary
- entity_count: 7
- topic_count: 10
- vector_count: 10
- origin_len: 27

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 27
- after_count: 24
- duplicate_count: 3

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
- candidate_count: 25
- duration_ms: 25921
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '烹饪技巧': 2, '半成品': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 30528
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:31:21.241
- end: 2026-08-11T16:31:57.350
- duration_ms: 36109
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3520
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
- chunk_count: 454
- redacted_field: 2025
- total_duration_ms: 11693
- fallback_used: False

## Final Output
- answer_chars: 577
- answer_hash: 1deff9e98a2de4a8
- success: True

## Request Complete
- request_end: 2026-08-11T16:32:09.059
- request_duration_ms: 47819
- success: True
- final_source: generation

