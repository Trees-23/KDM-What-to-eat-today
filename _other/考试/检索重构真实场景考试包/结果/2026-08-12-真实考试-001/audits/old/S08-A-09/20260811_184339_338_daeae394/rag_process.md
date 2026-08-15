# RAG Process

audit_id: 20260811_184339_338_daeae394
timestamp: 2026-08-11T18:43:39.346
## Request
- original_query: 云岚09号幻味砂锅怎么做？
- original_query_hash: ab84dffd67ef3be7
- session_id: 2026-08-12-真实考试-001:old:S08-A-09
- request_mode: stream
- request_start: 2026-08-11T18:43:39.347
- evaluation_sample_id: 20260811_184339_338_daeae394
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:43:39.348
- end: 2026-08-11T18:43:39.348
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:43:39.348
- end: 2026-08-11T18:43:39.348
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 13
- enhanced_query_length: 13
- enhanced_query_hash: ab84dffd67ef3be7

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:43:39.348
- end: 2026-08-11T18:43:39.348
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 13
- analysis_input_query_hash: ab84dffd67ef3be7
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:43:39.349
- end: 2026-08-11T18:43:48.248
- duration_ms: 8899
- analysis_mode: llm
- query_complexity: 0.22
- relationship_intensity: 0.15
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询的核心意图是获取“云岚09号幻味砂锅”这一特定菜品或产品的制作方法，属于直接的信息查找与步骤型问答，不需要多跳推理、因果分析或多方案对比。查询中“云岚09号幻味砂锅”可整体视为一个明确的菜品/产品实体，其中可能包含品牌、编号或菜名修饰信息。建议采用 hybrid_traditional，通过关键词精确匹配、别名扩展及向量语义检索召回配方、菜单说明、烹饪步骤等相关文档。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 173, 'graph_rag_count': 33, 'total_queries': 206}
- route_stats_after: {'traditional_count': 174, 'graph_rag_count': 33, 'total_queries': 207}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚09号幻味砂锅', '砂锅']
- topic_keywords: ['砂锅料理', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4573

## Hybrid Branch Status / topic_level
- keywords: ['砂锅料理', '烹饪技巧']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / entity_level
- keywords: ['云岚09号幻味砂锅', '砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 15

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 475

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
- expanded_count: 8
- doc_names: ['炒/煎']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 11
- duration_ms: 16080
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 2, '半成品': 1, '荤菜': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21148
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:43:39.349
- end: 2026-08-11T18:44:09.397
- duration_ms: 30048
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 2691
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
- chunk_count: 656
- redacted_field: 7780
- total_duration_ms: 19360
- fallback_used: False

## Final Output
- answer_chars: 846
- answer_hash: a4aa43609a9a90ee
- success: True

## Request Complete
- request_end: 2026-08-11T18:44:28.782
- request_duration_ms: 49435
- success: True
- final_source: generation

