# RAG Process

audit_id: 20260811_184810_220_5985310f
timestamp: 2026-08-11T18:48:10.223
## Request
- original_query: 知识库里有云岚16号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: d24c3395aad447ec
- session_id: 2026-08-12-真实考试-001:old:S08-B-06
- request_mode: stream
- request_start: 2026-08-11T18:48:10.224
- evaluation_sample_id: 20260811_184810_220_5985310f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:48:10.225
- end: 2026-08-11T18:48:10.225
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:48:10.225
- end: 2026-08-11T18:48:10.225
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: d24c3395aad447ec

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:48:10.226
- end: 2026-08-11T18:48:10.226
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: d24c3395aad447ec
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:48:10.226
- end: 2026-08-11T18:48:15.918
- duration_ms: 5692
- analysis_mode: llm
- query_complexity: 0.28
- relationship_intensity: 0.18
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询的核心是对单一菜品实体“云岚16号幻味砂锅”进行存在性检索；若知识库中存在该菜品，再直接提取其关联的做法信息。查询包含条件式需求（“如果有请给做法”），但不要求多跳推理、因果分析或实体间对比。适合采用关键词精确匹配、向量语义召回及字段过滤相结合的 hybrid_traditional 策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 180, 'graph_rag_count': 33, 'total_queries': 213}
- route_stats_after: {'traditional_count': 181, 'graph_rag_count': 33, 'total_queries': 214}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚16号幻味砂锅']
- topic_keywords: ['砂锅菜', '做法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2564

## Hybrid Branch Status / entity_level
- keywords: ['云岚16号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 5

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '做法']
- requested_k: 10
- actual_count: 8
- fallback_count: 8
- duration_ms: 35

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 460

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
- duration_ms: 17905
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '主食': 1, '素菜': 1, '烹饪技巧': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 蚝油生菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 20951
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:48:10.226
- end: 2026-08-11T18:48:36.871
- duration_ms: 26644
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1747
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
- chunk_count: 153
- redacted_field: 2624
- total_duration_ms: 5917
- fallback_used: False

## Final Output
- answer_chars: 195
- answer_hash: c976bba5158aadc7
- success: True

## Request Complete
- request_end: 2026-08-11T18:48:42.810
- request_duration_ms: 32585
- success: True
- final_source: generation

