# RAG Process

audit_id: 20260811_170445_881_e93db67f
timestamp: 2026-08-11T17:04:45.882
## Request
- original_query: 请说明“厨房准备”这个技巧的关键要点和适用情形。
- original_query_hash: ae02d876d1a4fd29
- session_id: 2026-08-12-真实考试-001:old:S03-A-06
- request_mode: stream
- request_start: 2026-08-11T17:04:45.882
- evaluation_sample_id: 20260811_170445_881_e93db67f
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:04:45.883
- end: 2026-08-11T17:04:45.883
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:04:45.883
- end: 2026-08-11T17:04:45.883
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 24
- enhanced_query_length: 24
- enhanced_query_hash: ae02d876d1a4fd29

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:04:45.884
- end: 2026-08-11T17:04:45.884
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 24
- analysis_input_query_hash: ae02d876d1a4fd29
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:04:45.884
- end: 2026-08-11T17:04:53.144
- duration_ms: 7260
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.25
- reasoning_required: False
- entity_count: 1
- strategy: hybrid_traditional
- confidence: 0.9
- reasoning: 查询核心实体为“厨房准备”技巧，目标是获取其关键要点及适用情形，属于对单一概念的定义、实践步骤和场景说明。虽然需要将技巧要点与不同烹饪场景进行基础匹配，但通常不需要多跳推理、复杂因果链分析或多实体关系网络建模。适合采用关键词检索结合语义检索的 hybrid_traditional 策略，以覆盖“厨房准备”“备料”“mise en place”“烹饪前准备”等相关表述。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 65, 'graph_rag_count': 0, 'total_queries': 65}
- route_stats_after: {'traditional_count': 66, 'graph_rag_count': 0, 'total_queries': 66}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['厨房准备', '备料', 'mise en place']
- topic_keywords: ['烹饪技巧', '食材预处理', '流程规划', '时间管理', '食品安全', '烹饪效率', '家常菜', '宴客菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3503

## Hybrid Branch Status / topic_level
- keywords: ['烹饪技巧', '食材预处理', '流程规划', '时间管理', '食品安全', '烹饪效率', '家常菜', '宴客菜']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 30

## Hybrid Branch Status / entity_level
- keywords: ['厨房准备', '备料', 'mise en place']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 115

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 712

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 2
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 18
- duplicate_count: 4

## Hybrid Technique Expansion
- enabled: True
- seed_count: 14
- expanded_count: 9
- doc_names: ['使用空气炸锅']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 19
- duration_ms: 23706
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'TechniqueDoc': 1, 'TechniqueChunk': 2, '烹饪技巧': 2}
- deferred_count: 7
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 去腥
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 28340
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:04:45.884
- end: 2026-08-11T17:05:21.486
- duration_ms: 35602
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 4778
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
- chunk_count: 1123
- redacted_field: 3545
- total_duration_ms: 25287
- fallback_used: False

## Final Output
- answer_chars: 1453
- answer_hash: 017d811f72ac3a83
- success: True

## Request Complete
- request_end: 2026-08-11T17:05:46.794
- request_duration_ms: 60911
- success: True
- final_source: generation

