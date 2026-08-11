# RAG Process

audit_id: 20260811_183809_513_992af609
timestamp: 2026-08-11T18:38:09.515
## Request
- original_query: 云岚01号幻味砂锅怎么做？
- original_query_hash: 05d5c8c7513389a1
- session_id: 2026-08-12-真实考试-001:old:S08-A-01
- request_mode: stream
- request_start: 2026-08-11T18:38:09.516
- evaluation_sample_id: 20260811_183809_513_992af609
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:38:09.516
- end: 2026-08-11T18:38:09.516
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:38:09.516
- end: 2026-08-11T18:38:09.516
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 13
- enhanced_query_length: 13
- enhanced_query_hash: 05d5c8c7513389a1

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:38:09.517
- end: 2026-08-11T18:38:09.517
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 13
- analysis_input_query_hash: 05d5c8c7513389a1
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:38:09.517
- end: 2026-08-11T18:38:16.544
- duration_ms: 7026
- analysis_mode: llm
- query_complexity: 0.2
- relationship_intensity: 0.1
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询的核心意图是获取“云岚01号幻味砂锅”这一特定菜品或配方的制作方法，属于直接的操作步骤与配料信息查找。查询中仅包含一个可视为整体的菜品/产品名称实体，不涉及多个实体之间的关联、因果解释或对比判断，因此无需多跳推理、因果分析或图谱关系推理。建议采用hybrid_traditional，通过关键词检索结合语义检索召回菜谱、菜单说明、制作教程或相关产品资料。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 165, 'graph_rag_count': 33, 'total_queries': 198}
- route_stats_after: {'traditional_count': 166, 'graph_rag_count': 33, 'total_queries': 199}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚01号幻味砂锅', '砂锅']
- topic_keywords: ['砂锅菜', '烹饪方法', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3666

## Hybrid Branch Status / entity_level
- keywords: ['云岚01号幻味砂锅', '砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 28

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '烹饪方法', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 79

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 462

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 10
- vector_count: 10
- origin_len: 20

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 20
- after_count: 18
- duplicate_count: 2

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
- candidate_count: 19
- duration_ms: 17791
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, '荤菜': 2, '半成品': 1}
- deferred_count: 2
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21962
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:38:09.517
- end: 2026-08-11T18:38:38.507
- duration_ms: 28990
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2668
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
- chunk_count: 574
- redacted_field: 4577
- total_duration_ms: 14918
- fallback_used: False

## Final Output
- answer_chars: 731
- answer_hash: e05e1826b44d573b
- success: True

## Request Complete
- request_end: 2026-08-11T18:38:53.441
- request_duration_ms: 43925
- success: True
- final_source: generation

