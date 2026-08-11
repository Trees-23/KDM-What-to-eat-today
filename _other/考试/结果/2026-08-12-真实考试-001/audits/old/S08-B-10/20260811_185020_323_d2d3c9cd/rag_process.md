# RAG Process

audit_id: 20260811_185020_323_d2d3c9cd
timestamp: 2026-08-11T18:50:20.328
## Request
- original_query: 知识库里有云岚20号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: 1aa542cd626755b1
- session_id: 2026-08-12-真实考试-001:old:S08-B-10
- request_mode: stream
- request_start: 2026-08-11T18:50:20.328
- evaluation_sample_id: 20260811_185020_323_d2d3c9cd
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:50:20.330
- end: 2026-08-11T18:50:20.330
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:50:20.330
- end: 2026-08-11T18:50:20.330
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 1aa542cd626755b1

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:50:20.331
- end: 2026-08-11T18:50:20.331
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 1aa542cd626755b1
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:50:20.331
- end: 2026-08-11T18:50:27.902
- duration_ms: 7571
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 该查询以“云岚20号幻味砂锅”这一明确菜品实体为核心，任务是先在知识库中进行名称匹配或语义召回，确认是否存在对应菜品，再从命中文档中提取其做法。查询包含条件式回答要求（若存在则提供做法），但不涉及多实体关系关联、跨文档多跳推理、因果分析或对比分析。建议采用hybrid_traditional，通过关键词精确匹配、别名/模糊匹配与向量语义检索结合，提高对菜名变体及菜谱内容的召回效果。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 184, 'graph_rag_count': 33, 'total_queries': 217}
- route_stats_after: {'traditional_count': 185, 'graph_rag_count': 33, 'total_queries': 218}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚20号幻味砂锅']
- topic_keywords: ['砂锅菜', '菜谱', '做法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2476

## Hybrid Branch Status / entity_level
- keywords: ['云岚20号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 9

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '菜谱', '做法']
- requested_k: 10
- actual_count: 9
- fallback_count: 8
- duration_ms: 62

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 575

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 9
- vector_count: 10
- origin_len: 19

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 19
- after_count: 17
- duplicate_count: 2

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
- candidate_count: 18
- duration_ms: 18566
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, 'Recipe': 1, '主食': 1, '素菜': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蚝油生菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21639
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:50:20.331
- end: 2026-08-11T18:50:49.543
- duration_ms: 29211
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1589
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
- chunk_count: 133
- redacted_field: 978
- total_duration_ms: 3759
- fallback_used: False

## Final Output
- answer_chars: 164
- answer_hash: 9a105fb93768e23b
- success: True

## Request Complete
- request_end: 2026-08-11T18:50:53.320
- request_duration_ms: 32992
- success: True
- final_source: generation

