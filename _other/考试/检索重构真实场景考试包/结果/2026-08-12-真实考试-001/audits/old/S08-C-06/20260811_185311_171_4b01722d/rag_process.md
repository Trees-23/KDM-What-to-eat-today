# RAG Process

audit_id: 20260811_185311_171_4b01722d
timestamp: 2026-08-11T18:53:11.172
## Request
- original_query: 请查云岚26号幻味砂锅的做法；未收录时只说明未找到，不要根据名称猜配方。
- original_query_hash: 34c4e20792d3fc5f
- session_id: 2026-08-12-真实考试-001:old:S08-C-06
- request_mode: stream
- request_start: 2026-08-11T18:53:11.172
- evaluation_sample_id: 20260811_185311_171_4b01722d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:53:11.173
- end: 2026-08-11T18:53:11.173
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:53:11.173
- end: 2026-08-11T18:53:11.173
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 36
- enhanced_query_length: 36
- enhanced_query_hash: 34c4e20792d3fc5f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:53:11.174
- end: 2026-08-11T18:53:11.174
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 36
- analysis_input_query_hash: 34c4e20792d3fc5f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:53:11.174
- end: 2026-08-11T18:53:19.610
- duration_ms: 8436
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.12
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.96
- reasoning: 查询目标是精确查找名为“云岚26号幻味砂锅”的单一菜品实体及其做法，属于直接事实检索。用户明确要求在知识库未收录时仅返回“未找到”，因此检索过程应优先进行精确名称匹配、别名/分词匹配及文档级验证，不应基于菜名语义扩展、关联菜品或常见砂锅做法生成推断配方。该查询不涉及多实体关系网络、因果分析、对比分析或多跳推理，适合采用 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 190, 'graph_rag_count': 33, 'total_queries': 223}
- route_stats_after: {'traditional_count': 191, 'graph_rag_count': 33, 'total_queries': 224}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚26号幻味砂锅']
- topic_keywords: ['菜谱']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3992

## Hybrid Branch Status / entity_level
- keywords: ['云岚26号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / topic_level
- keywords: ['菜谱']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 17

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 458

## Hybrid Branch Summary
- entity_count: 0
- topic_count: 1
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 11
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
- candidate_count: 12
- duration_ms: 15691
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '烹饪技巧': 1, '汤类': 1, '主食': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 韭菜盒子
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20158
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:53:11.174
- end: 2026-08-11T18:53:39.770
- duration_ms: 28595
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1739
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
- chunk_count: 17
- redacted_field: 2628
- total_duration_ms: 3070
- fallback_used: False

## Final Output
- answer_chars: 20
- answer_hash: 0c802fb2f61cc1be
- success: True

## Request Complete
- request_end: 2026-08-11T18:53:42.872
- request_duration_ms: 31700
- success: True
- final_source: generation

