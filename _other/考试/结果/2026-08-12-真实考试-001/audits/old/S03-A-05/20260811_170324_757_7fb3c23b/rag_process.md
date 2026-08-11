# RAG Process

audit_id: 20260811_170324_757_7fb3c23b
timestamp: 2026-08-11T17:03:24.757
## Request
- original_query: 请说明“糖色的炒制”这个技巧的关键要点和适用情形。
- original_query_hash: 5d7f6b7f537f5508
- session_id: 2026-08-12-真实考试-001:old:S03-A-05
- request_mode: stream
- request_start: 2026-08-11T17:03:24.758
- evaluation_sample_id: 20260811_170324_757_7fb3c23b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:03:24.759
- end: 2026-08-11T17:03:24.759
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:03:24.759
- end: 2026-08-11T17:03:24.759
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 25
- enhanced_query_length: 25
- enhanced_query_hash: 5d7f6b7f537f5508

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:03:24.759
- end: 2026-08-11T17:03:24.759
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 25
- analysis_input_query_hash: 5d7f6b7f537f5508
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:03:24.760
- end: 2026-08-11T17:03:39.399
- duration_ms: 14639
- analysis_mode: llm
- query_complexity: 0.55
- relationship_intensity: 0.48
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 该查询围绕“糖色的炒制”这一烹饪技法，要求同时说明其操作关键要点（如火候、糖与油/水比例、颜色阶段、避免焦苦等）及其适用情形（如红烧、卤制、增色增香）。需要进行有限的因果分析，例如不同火候和糖色状态如何影响色泽、苦味与成品效果，但不涉及跨领域、多实体的复杂关系网络或多跳知识推理。适合通过关键词检索、菜谱/烹饪知识库召回及重排序的 hybrid_traditional 策略获取答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 64, 'graph_rag_count': 0, 'total_queries': 64}
- route_stats_after: {'traditional_count': 65, 'graph_rag_count': 0, 'total_queries': 65}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['糖色的炒制', '炒糖色', '糖色', '冰糖', '白砂糖', '油', '水']
- topic_keywords: ['烹饪技巧', '火候', '上色', '焦糖化', '红烧菜', '卤味', '炖煮', '调味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8150

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '火候', '上色', '焦糖化', '红烧菜', '卤味', '炖煮', '调味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 78

## Hybrid Branch Status / entity_level
- keywords: ['糖色的炒制', '炒糖色', '糖色', '冰糖', '白砂糖', '油', '水']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 102

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 538

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 17
- duplicate_count: 13

## Hybrid Technique Expansion
- enabled: True
- seed_count: 5
- expanded_count: 5
- doc_names: ['糖色的炒制']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 18
- duration_ms: 17655
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'烹饪技巧': 1, 'TechniqueChunk': 2, 'TechniqueDoc': 1, '调料': 1}
- deferred_count: 1
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 26392
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:03:24.760
- end: 2026-08-11T17:04:05.793
- duration_ms: 41032
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4163
- retrieval_levels: ['', 'context_expansion', 'entity']
- search_types: ['entity_level', 'technique_expansion', 'vector_enhanced']
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
- chunk_count: 1089
- redacted_field: 7951
- total_duration_ms: 40063
- fallback_used: False

## Final Output
- answer_chars: 1496
- answer_hash: 00621b573c3c6e92
- success: True

## Request Complete
- request_end: 2026-08-11T17:04:45.872
- request_duration_ms: 81113
- success: True
- final_source: generation

