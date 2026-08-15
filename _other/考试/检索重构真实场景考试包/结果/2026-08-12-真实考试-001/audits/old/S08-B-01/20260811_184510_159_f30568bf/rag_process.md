# RAG Process

audit_id: 20260811_184510_159_f30568bf
timestamp: 2026-08-11T18:45:10.165
## Request
- original_query: 知识库里有云岚11号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: 943b79908b573c8a
- session_id: 2026-08-12-真实考试-001:old:S08-B-01
- request_mode: stream
- request_start: 2026-08-11T18:45:10.165
- evaluation_sample_id: 20260811_184510_159_f30568bf
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:45:10.166
- end: 2026-08-11T18:45:10.166
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:45:10.166
- end: 2026-08-11T18:45:10.166
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 943b79908b573c8a

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:45:10.166
- end: 2026-08-11T18:45:10.166
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 943b79908b573c8a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:45:10.166
- end: 2026-08-11T18:45:16.725
- duration_ms: 6558
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 查询以“云岚11号幻味砂锅”这一明确菜品名称为核心，目标是先确认知识库中是否存在该菜品，再直接获取其做法。该任务属于精确实体检索与属性信息提取，不涉及多个实体之间的复杂关联、多跳推理、因果分析或对比分析。建议采用hybrid_traditional，通过关键词/倒排索引进行精确召回，并结合向量检索处理菜名可能存在的别名、错别字或表述变体。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 175, 'graph_rag_count': 33, 'total_queries': 208}
- route_stats_after: {'traditional_count': 176, 'graph_rag_count': 33, 'total_queries': 209}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚11号幻味砂锅']
- topic_keywords: ['砂锅菜', '做法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2459

## Hybrid Branch Status / entity_level
- keywords: ['云岚11号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 4

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '做法']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 44

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 404

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 8
- vector_count: 10
- origin_len: 18

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 18
- after_count: 16
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
- candidate_count: 17
- duration_ms: 17096
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 1, '素菜': 1, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蚝油生菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 19980
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:45:10.166
- end: 2026-08-11T18:45:36.706
- duration_ms: 26539
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
- chunk_count: 219
- redacted_field: 2839
- total_duration_ms: 7323
- fallback_used: False

## Final Output
- answer_chars: 273
- answer_hash: e29751df759ea5b0
- success: True

## Request Complete
- request_end: 2026-08-11T18:45:44.053
- request_duration_ms: 33888
- success: True
- final_source: generation

