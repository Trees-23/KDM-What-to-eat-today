# RAG Process

audit_id: 20260811_184916_244_abcdfe40
timestamp: 2026-08-11T18:49:16.245
## Request
- original_query: 知识库里有云岚18号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: c53067a4b7ee4de4
- session_id: 2026-08-12-真实考试-001:old:S08-B-08
- request_mode: stream
- request_start: 2026-08-11T18:49:16.245
- evaluation_sample_id: 20260811_184916_244_abcdfe40
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:49:16.246
- end: 2026-08-11T18:49:16.246
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:49:16.246
- end: 2026-08-11T18:49:16.246
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: c53067a4b7ee4de4

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:49:16.246
- end: 2026-08-11T18:49:16.246
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: c53067a4b7ee4de4
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:49:16.247
- end: 2026-08-11T18:49:22.466
- duration_ms: 6219
- analysis_mode: llm
- query_complexity: 0.3
- relationship_intensity: 0.2
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询的核心是对指定菜品“云岚18号幻味砂锅”进行知识库存在性检索；若检索命中，再从对应文档中提取其做法。虽然包含“如果有”的条件判断，但不需要多跳推理、因果分析或实体关系网络建模。明确实体包括“知识库”和“云岚18号幻味砂锅”，适合使用关键词检索与语义检索结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 182, 'graph_rag_count': 33, 'total_queries': 215}
- route_stats_after: {'traditional_count': 183, 'graph_rag_count': 33, 'total_queries': 216}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚18号幻味砂锅', '砂锅']
- topic_keywords: ['砂锅菜', '烹饪做法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4067

## Hybrid Branch Status / entity_level
- keywords: ['云岚18号幻味砂锅', '砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 7

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '烹饪做法']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 7

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 362

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 0
- vector_count: 10
- origin_len: 10

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 10
- after_count: 10
- duplicate_count: 0

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 7
- doc_names: ['去腥']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 11
- duration_ms: 16221
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 1, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20670
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:49:16.247
- end: 2026-08-11T18:49:43.137
- duration_ms: 26890
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1770
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
- chunk_count: 193
- redacted_field: 2119
- total_duration_ms: 5659
- fallback_used: False

## Final Output
- answer_chars: 243
- answer_hash: 236579ab70d8b953
- success: True

## Request Complete
- request_end: 2026-08-11T18:49:48.822
- request_duration_ms: 32576
- success: True
- final_source: generation

