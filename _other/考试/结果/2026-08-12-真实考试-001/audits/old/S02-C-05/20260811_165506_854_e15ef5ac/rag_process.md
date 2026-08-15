# RAG Process

audit_id: 20260811_165506_854_e15ef5ac
timestamp: 2026-08-11T16:55:06.856
## Request
- original_query: 只回答上汤娃娃菜的第 1 步，并说明它来自哪一条菜谱步骤；不要混入后续步骤。
- original_query_hash: ede81901d86c8e40
- session_id: 2026-08-12-真实考试-001:old:S02-C-05
- request_mode: stream
- request_start: 2026-08-11T16:55:06.857
- evaluation_sample_id: 20260811_165506_854_e15ef5ac
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:55:06.858
- end: 2026-08-11T16:55:06.858
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:55:06.858
- end: 2026-08-11T16:55:06.858
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 38
- enhanced_query_length: 38
- enhanced_query_hash: ede81901d86c8e40

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:55:06.859
- end: 2026-08-11T16:55:06.859
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 38
- analysis_input_query_hash: ede81901d86c8e40
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:55:06.859
- end: 2026-08-11T16:55:14.916
- duration_ms: 8056
- analysis_mode: llm
- query_complexity: 0.32
- relationship_intensity: 0.28
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询的核心是对“上汤娃娃菜”菜谱进行精确的步骤定位与受约束摘取：仅返回第1步、明确标注其所属菜谱步骤，并排除所有后续步骤内容。它不需要多跳推理、因果分析或实体间复杂关系推断，但需要执行顺序/位置识别和输出边界控制。明确实体包括“上汤娃娃菜”（菜品）、“第1步”（步骤序号/位置实体）和“菜谱步骤”（文档结构实体）。适合使用 hybrid_traditional，通过关键词检索定位目标菜谱后，按步骤编号进行精确抽取。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 54, 'graph_rag_count': 0, 'total_queries': 54}
- route_stats_after: {'traditional_count': 55, 'graph_rag_count': 0, 'total_queries': 55}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['上汤娃娃菜']
- topic_keywords: ['菜谱步骤', '步骤顺序']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6804

## Hybrid Branch Status / topic_level
- keywords: ['菜谱步骤', '步骤顺序']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 6

## Hybrid Branch Status / entity_level
- keywords: ['上汤娃娃菜']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 16

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 496

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
- seed_count: 4
- expanded_count: 9
- doc_names: ['炒/煎', '如何决策吃什么']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 10
- duration_ms: 14946
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'减肥餐': 1, '主食': 2, '水产': 1, '烹饪技巧': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 螺蛳粉
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 22273
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:55:06.859
- end: 2026-08-11T16:55:37.191
- duration_ms: 30331
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3217
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
- chunk_count: 51
- redacted_field: 2752
- total_duration_ms: 3705
- fallback_used: False

## Final Output
- answer_chars: 61
- answer_hash: 7ba6b56f3e1a1421
- success: True

## Request Complete
- request_end: 2026-08-11T16:55:40.915
- request_duration_ms: 34058
- success: True
- final_source: generation

