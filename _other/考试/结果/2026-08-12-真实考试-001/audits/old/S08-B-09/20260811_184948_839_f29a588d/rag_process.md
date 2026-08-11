# RAG Process

audit_id: 20260811_184948_839_f29a588d
timestamp: 2026-08-11T18:49:48.848
## Request
- original_query: 知识库里有云岚19号幻味砂锅这道菜吗？如果有请给做法。
- original_query_hash: 1829a6cfaceb5ea5
- session_id: 2026-08-12-真实考试-001:old:S08-B-09
- request_mode: stream
- request_start: 2026-08-11T18:49:48.848
- evaluation_sample_id: 20260811_184948_839_f29a588d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T18:49:48.849
- end: 2026-08-11T18:49:48.849
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T18:49:48.849
- end: 2026-08-11T18:49:48.849
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 27
- enhanced_query_length: 27
- enhanced_query_hash: 1829a6cfaceb5ea5

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T18:49:48.849
- end: 2026-08-11T18:49:48.849
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 27
- analysis_input_query_hash: 1829a6cfaceb5ea5
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T18:49:48.850
- end: 2026-08-11T18:49:57.310
- duration_ms: 8460
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.2
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.95
- reasoning: 查询的核心是精确菜品实体“云岚19号幻味砂锅”的存在性检索，并在命中后提取其关联的做法内容。虽然包含“如果有”的条件分支，但这属于检索结果后的简单条件处理，不需要多跳推理、因果分析或实体关系网络推断。建议采用关键词精确匹配、别名/模糊匹配与向量语义召回相结合的 hybrid_traditional 策略，以应对菜名可能存在的编号、命名变体或录入误差。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 183, 'graph_rag_count': 33, 'total_queries': 216}
- route_stats_after: {'traditional_count': 184, 'graph_rag_count': 33, 'total_queries': 217}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['云岚19号幻味砂锅']
- topic_keywords: ['砂锅菜', '菜谱', '烹饪做法']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 2462

## Hybrid Branch Status / entity_level
- keywords: ['云岚19号幻味砂锅']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 9

## Hybrid Branch Status / topic_level
- keywords: ['砂锅菜', '菜谱', '烹饪做法']
- requested_k: 10
- actual_count: 1
- fallback_count: 0
- duration_ms: 20

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 290

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
- expanded_count: 7
- doc_names: ['去腥']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 12
- duration_ms: 15939
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, 'Recipe': 1, '主食': 1, '烹饪技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 西红柿牛腩
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18708
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T18:49:48.850
- end: 2026-08-11T18:50:16.020
- duration_ms: 27170
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 1660
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
- chunk_count: 140
- redacted_field: 2494
- total_duration_ms: 4245
- fallback_used: False

## Final Output
- answer_chars: 186
- answer_hash: d3c845da2a3f3386
- success: True

## Request Complete
- request_end: 2026-08-11T18:50:20.298
- request_duration_ms: 31449
- success: True
- final_source: generation

