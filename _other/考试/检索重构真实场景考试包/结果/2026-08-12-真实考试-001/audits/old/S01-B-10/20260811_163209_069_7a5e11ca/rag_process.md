# RAG Process

audit_id: 20260811_163209_069_7a5e11ca
timestamp: 2026-08-11T16:32:09.070
## Request
- original_query: 日式肥牛丼饭从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 7c94b13d3ea24e4f
- session_id: 2026-08-12-真实考试-001:old:S01-B-10
- request_mode: stream
- request_start: 2026-08-11T16:32:09.070
- evaluation_sample_id: 20260811_163209_069_7a5e11ca
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:32:09.070
- end: 2026-08-11T16:32:09.070
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:32:09.071
- end: 2026-08-11T16:32:09.071
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 28
- enhanced_query_length: 28
- enhanced_query_hash: 7c94b13d3ea24e4f

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:32:09.072
- end: 2026-08-11T16:32:09.072
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 28
- analysis_input_query_hash: 7c94b13d3ea24e4f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:32:09.072
- end: 2026-08-11T16:32:20.397
- duration_ms: 11325
- analysis_mode: llm
- query_complexity: 0.32
- relationship_intensity: 0.28
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询的核心目标是从知识库中检索“日式肥牛丼饭”的标准制作流程，覆盖备料、调味、烹制和出锅等连续步骤。虽然需要按步骤组织答案，但本质上属于单一菜品的操作型信息查找，不涉及跨实体的复杂关系网络、因果解释或方案对比。明确实体主要包括“日式肥牛丼饭”（菜品）、“备料”（制作阶段）和“出锅”（制作阶段）。建议采用hybrid_traditional，通过关键词/语义检索定位知识库中的对应菜谱、食材配比及烹饪步骤，并优先匹配带有完整制作流程的文档。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 19, 'graph_rag_count': 0, 'total_queries': 19}
- route_stats_after: {'traditional_count': 20, 'graph_rag_count': 0, 'total_queries': 20}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['日式肥牛丼饭', '肥牛', '牛肉片', '米饭', '洋葱', '日式酱油', '味醂', '清酒', '砂糖', '出锅']
- topic_keywords: ['日式料理', '丼饭', '备料', '烹饪步骤', '调味', '火候', '快手菜']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3755

## Hybrid Branch Status / entity_level
- keywords: ['日式肥牛丼饭', '肥牛', '牛肉片', '米饭', '洋葱', '日式酱油', '味醂', '清酒', '砂糖', '出锅']
- requested_k: 10
- actual_count: 6
- fallback_count: 0
- duration_ms: 41

## Hybrid Branch Status / topic_level
- keywords: ['日式料理', '丼饭', '备料', '烹饪步骤', '调味', '火候', '快手菜']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 50

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 582

## Hybrid Branch Summary
- entity_count: 6
- topic_count: 10
- vector_count: 10
- origin_len: 26

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 26
- after_count: 22
- duplicate_count: 4

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
- candidate_count: 23
- duration_ms: 20406
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '荤菜': 1, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 24769
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:32:09.072
- end: 2026-08-11T16:32:45.168
- duration_ms: 36095
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3248
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
- chunk_count: 372
- redacted_field: 2571
- total_duration_ms: 10310
- fallback_used: False

## Final Output
- answer_chars: 481
- answer_hash: a2cd5470c6a366fc
- success: True

## Request Complete
- request_end: 2026-08-11T16:32:55.494
- request_duration_ms: 46424
- success: True
- final_source: generation

