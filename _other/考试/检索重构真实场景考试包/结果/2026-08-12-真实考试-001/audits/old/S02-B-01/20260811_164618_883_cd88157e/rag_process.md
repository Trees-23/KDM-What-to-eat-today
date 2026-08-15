# RAG Process

audit_id: 20260811_164618_883_cd88157e
timestamp: 2026-08-11T16:46:18.884
## Request
- original_query: 刚开始做鱼香肉丝时，第一步具体要处理什么？
- original_query_hash: bb322b618f67d296
- session_id: 2026-08-12-真实考试-001:old:S02-B-01
- request_mode: stream
- request_start: 2026-08-11T16:46:18.884
- evaluation_sample_id: 20260811_164618_883_cd88157e
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:46:18.885
- end: 2026-08-11T16:46:18.885
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:46:18.885
- end: 2026-08-11T16:46:18.885
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: bb322b618f67d296

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:46:18.886
- end: 2026-08-11T16:46:18.886
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 21
- analysis_input_query_hash: bb322b618f67d296
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:46:18.886
- end: 2026-08-11T16:46:24.772
- duration_ms: 5885
- analysis_mode: llm
- query_complexity: 0.18
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 该查询是对菜品“鱼香肉丝”制作流程中首个步骤的直接定位，目标明确、答案通常存在于单一食谱或烹饪步骤文档中。无需多跳推理、因果分析或不同方案对比；仅需检索并抽取与“第一步/开始处理”相关的步骤信息。明确实体为“鱼香肉丝”，实体类型为菜品。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 40, 'graph_rag_count': 0, 'total_queries': 40}
- route_stats_after: {'traditional_count': 41, 'graph_rag_count': 0, 'total_queries': 41}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['鱼香肉丝', '猪肉', '腌肉']
- topic_keywords: ['川菜', '烹饪技巧', '食材预处理', '去腥', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 6138

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '烹饪技巧', '食材预处理', '去腥', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 91

## Hybrid Branch Status / entity_level
- keywords: ['鱼香肉丝', '猪肉', '腌肉']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 103

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 508

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 27
- duplicate_count: 3

## Hybrid Technique Expansion
- enabled: True
- seed_count: 9
- expanded_count: 9
- doc_names: ['去腥', '腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 28
- duration_ms: 28728
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '水产': 1, '调料': 1, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 葱油
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 35443
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:46:18.886
- end: 2026-08-11T16:47:00.217
- duration_ms: 41330
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3866
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
- chunk_count: 98
- redacted_field: 4131
- total_duration_ms: 6084
- fallback_used: False

## Final Output
- answer_chars: 130
- answer_hash: ba2bbdb548319c31
- success: True

## Request Complete
- request_end: 2026-08-11T16:47:06.312
- request_duration_ms: 47428
- success: True
- final_source: generation

