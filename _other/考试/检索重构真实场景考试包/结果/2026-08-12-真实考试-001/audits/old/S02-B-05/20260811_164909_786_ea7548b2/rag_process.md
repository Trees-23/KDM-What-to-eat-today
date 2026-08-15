# RAG Process

audit_id: 20260811_164909_786_ea7548b2
timestamp: 2026-08-11T16:49:09.786
## Request
- original_query: 刚开始做水煮肉片时，第一步具体要处理什么？
- original_query_hash: 49fac9c5af34e732
- session_id: 2026-08-12-真实考试-001:old:S02-B-05
- request_mode: stream
- request_start: 2026-08-11T16:49:09.787
- evaluation_sample_id: 20260811_164909_786_ea7548b2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:49:09.787
- end: 2026-08-11T16:49:09.787
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:49:09.788
- end: 2026-08-11T16:49:09.788
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 49fac9c5af34e732

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:49:09.789
- end: 2026-08-11T16:49:09.789
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: 49fac9c5af34e732
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:49:09.789
- end: 2026-08-11T16:49:17.283
- duration_ms: 7493
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对“水煮肉片”制作流程中起始步骤的直接事实查找，目标明确且答案通常位于菜谱的步骤开头。查询不涉及多个实体之间的复杂关系、跨文档多跳推理、因果归因或方案对比。明确实体包括菜品“水煮肉片”和流程阶段“第一步/刚开始处理”，适合通过关键词检索、菜谱步骤定位与语义匹配实现。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 44, 'graph_rag_count': 0, 'total_queries': 44}
- route_stats_after: {'traditional_count': 45, 'graph_rag_count': 0, 'total_queries': 45}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['水煮肉片', '猪里脊肉', '腌肉']
- topic_keywords: ['川菜', '烹饪技巧', '食材预处理', '腌制', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6943

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '烹饪技巧', '食材预处理', '腌制', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 90

## Hybrid Branch Status / entity_level
- keywords: ['水煮肉片', '猪里脊肉', '腌肉']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 97

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 787

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 26
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 10
- expanded_count: 9
- doc_names: ['去腥', '焯水']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 27
- duration_ms: 28617
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '烹饪技巧': 2, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 汤面
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 36401
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:49:09.789
- end: 2026-08-11T16:49:53.685
- duration_ms: 43896
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3806
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
- chunk_count: 102
- redacted_field: 2057
- total_duration_ms: 4232
- fallback_used: False

## Final Output
- answer_chars: 130
- answer_hash: 3cd25681320668c0
- success: True

## Request Complete
- request_end: 2026-08-11T16:49:57.949
- request_duration_ms: 48162
- success: True
- final_source: generation

