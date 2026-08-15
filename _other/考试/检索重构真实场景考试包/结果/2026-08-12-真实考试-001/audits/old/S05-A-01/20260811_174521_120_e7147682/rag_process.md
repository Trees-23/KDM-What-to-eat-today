# RAG Process

audit_id: 20260811_174521_120_e7147682
timestamp: 2026-08-11T17:45:21.122
## Request
- original_query: 牛肉适合搭配什么蔬菜？
- original_query_hash: 1b8dadc5fd66eafa
- session_id: 2026-08-12-真实考试-001:old:S05-A-01
- request_mode: stream
- request_start: 2026-08-11T17:45:21.122
- evaluation_sample_id: 20260811_174521_120_e7147682
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T17:45:21.123
- end: 2026-08-11T17:45:21.123
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T17:45:21.124
- end: 2026-08-11T17:45:21.124
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 11
- enhanced_query_length: 11
- enhanced_query_hash: 1b8dadc5fd66eafa

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T17:45:21.124
- end: 2026-08-11T17:45:21.124
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 11
- analysis_input_query_hash: 1b8dadc5fd66eafa
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T17:45:21.124
- end: 2026-08-11T17:45:28.340
- duration_ms: 7215
- analysis_mode: llm
- query_complexity: 0.32
- relationship_intensity: 0.58
- reasoning_required: False
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 该查询是围绕“牛肉”与“蔬菜”之间搭配关系的直接信息检索，核心目标是获得适合搭配牛肉的蔬菜列表及可能的烹饪建议。查询包含两个明确实体：牛肉（食材/肉类）和蔬菜（食材类别）。虽然存在实体间的搭配关系，但通常不需要多跳推理、因果分析或复杂的跨实体关系网络推断；可通过关键词检索、菜谱文档召回及语义排序直接获得答案，因此推荐使用hybrid_traditional策略。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 109, 'graph_rag_count': 11, 'total_queries': 120}
- route_stats_after: {'traditional_count': 110, 'graph_rag_count': 11, 'total_queries': 121}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['牛肉', '西兰花', '胡萝卜', '土豆', '洋葱', '芹菜', '青椒', '番茄', '白萝卜', '蘑菇']
- topic_keywords: ['荤素搭配', '营养均衡', '高蛋白', '家常菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4610

## Hybrid Branch Status / topic_level
- keywords: ['荤素搭配', '营养均衡', '高蛋白', '家常菜']
- requested_k: 10
- actual_count: 2
- fallback_count: 2
- duration_ms: 23

## Hybrid Branch Status / entity_level
- keywords: ['牛肉', '西兰花', '胡萝卜', '土豆', '洋葱', '芹菜', '青椒', '番茄', '白萝卜', '蘑菇']
- requested_k: 10
- actual_count: 10
- fallback_count: 0
- duration_ms: 63

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 593

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 2
- vector_count: 10
- origin_len: 22

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 22
- after_count: 20
- duplicate_count: 2

## Hybrid Technique Expansion
- enabled: True
- seed_count: 1
- expanded_count: 9
- doc_names: ['腌（肉）']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 21
- duration_ms: 16141
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'荤菜': 2, '烹饪技巧': 1, '汤类': 1, 'Ingredient': 1}
- deferred_count: 3
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 西兰花
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21372
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T17:45:21.124
- end: 2026-08-11T17:45:49.713
- duration_ms: 28588
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 5366
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
- chunk_count: 271
- redacted_field: 2142
- total_duration_ms: 7555
- fallback_used: False

## Final Output
- answer_chars: 336
- answer_hash: c72566fa17cfed39
- success: True

## Request Complete
- request_end: 2026-08-11T17:45:57.281
- request_duration_ms: 36158
- success: True
- final_source: generation

