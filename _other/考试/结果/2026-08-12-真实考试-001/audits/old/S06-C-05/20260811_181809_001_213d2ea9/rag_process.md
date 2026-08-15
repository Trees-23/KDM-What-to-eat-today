# RAG Process

audit_id: 20260811_181809_001_213d2ea9
timestamp: 2026-08-11T18:18:09.005
## Request
- original_query: 冰箱食材不多，想先看看容易上手的菜。请展示推荐依据；如果意图无法由资料支持，不要把推测写成事实。
- original_query_hash: 454e57f69edac390
- session_id: 2026-08-12-真实考试-001:old:S06-C-05
- request_mode: stream
- request_start: 2026-08-11T18:18:09.006
- evaluation_sample_id: 20260811_181809_001_213d2ea9
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:18:09.007
- end: 2026-08-11T18:18:09.007
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:18:09.007
- end: 2026-08-11T18:18:09.007
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 48
- enhanced_query_length: 48
- enhanced_query_hash: 454e57f69edac390

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:18:09.008
- end: 2026-08-11T18:18:09.008
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 48
- analysis_input_query_hash: 454e57f69edac390
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:18:09.009
- end: 2026-08-11T18:18:26.497
- duration_ms: 17487
- analysis_mode: llm
- query_complexity: 0.58
- relationship_intensity: 0.46
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.88
- reasoning: 查询的核心目标是筛选“食材需求较少、容易上手”的菜品，并要求展示推荐依据与区分资料事实和推测。它需要从菜谱资料中检索并比对食材数量、步骤复杂度、烹饪时间或技巧要求等属性，属于带约束条件的中等复杂度检索与排序任务。查询中的明确实体/概念主要包括“冰箱食材”“菜品/菜谱”“容易上手”，但未给出具体食材、菜名或设备型号，因此不具备复杂实体网络或多跳知识发现需求。适合使用 hybrid_traditional，通过关键词检索、语义召回和基于菜谱字段的排序，输出可被来源资料支撑的推荐理由；对于资料未明确说明的‘简单’或食材存量情况，应以条件化表述说明，不应作为事实断言。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 141, 'graph_rag_count': 33, 'total_queries': 174}
- route_stats_after: {'traditional_count': 142, 'graph_rag_count': 33, 'total_queries': 175}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['冰箱']
- topic_keywords: ['食材有限', '新手菜', '简单易做', '烹饪难度', '推荐依据']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4839

## Hybrid Branch Status / entity_level
- keywords: ['冰箱']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / topic_level
- keywords: ['食材有限', '新手菜', '简单易做', '烹饪难度', '推荐依据']
- requested_k: 10
- actual_count: 1
- fallback_count: 1
- duration_ms: 9

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 744

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 1
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 7
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 4
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 8
- duration_ms: 15757
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, '主食': 2, '荤菜': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 汤面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21397
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:18:09.009
- end: 2026-08-11T18:18:47.895
- duration_ms: 38886
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3375
- retrieval_levels: ['', 'context_expansion', 'topic']
- search_types: ['technique_expansion', 'topic_level', 'vector_enhanced']
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
- chunk_count: 492
- redacted_field: 6710
- total_duration_ms: 18731
- fallback_used: False

## Final Output
- answer_chars: 652
- answer_hash: 0511a78ea55899ef
- success: True

## Request Complete
- request_end: 2026-08-11T18:19:06.680
- request_duration_ms: 57674
- success: True
- final_source: generation

