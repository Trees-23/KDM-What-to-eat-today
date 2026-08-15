# RAG Process

audit_id: 20260811_194007_529_ab9c486d
timestamp: 2026-08-11T19:40:07.530
## Request
- original_query: 日式肥牛丼饭从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 7c94b13d3ea24e4f
- session_id: 2026-08-12-真实考试-001:new:S01-B-10
- request_mode: stream
- request_start: 2026-08-11T19:40:07.530
- evaluation_sample_id: 20260811_194007_529_ab9c486d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:40:07.530
- end: 2026-08-11T19:40:07.530
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:40:07.531
- end: 2026-08-11T19:40:07.531
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 28
- enhanced_query_length: 28
- enhanced_query_hash: 7c94b13d3ea24e4f

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:40:07.535
- end: 2026-08-11T19:40:07.535
- duration_ms: 0
- entity_id: 201004544
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:40:07.535
- end: 2026-08-11T19:40:07.535
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:40:07.536
- end: 2026-08-11T19:40:07.536
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 28
- analysis_input_query_hash: 7c94b13d3ea24e4f
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:40:07.536
- end: 2026-08-11T19:40:14.232
- duration_ms: 6696
- analysis_mode: llm
- query_complexity: 0.4
- relationship_intensity: 0.35
- reasoning_required: True
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.92
- reasoning: 该查询的核心目标是从知识库中检索“日式肥牛丼饭”的标准做法，并按“备料—烹饪—出锅”的顺序组织答案。涉及的明确实体可归纳为日式肥牛丼饭、备料/食材准备、出锅/烹饪步骤。查询需要一定的流程性整合与步骤排序，但不需要多跳关系推理、因果分析或跨菜品对比分析；更适合通过关键词、菜品别名、食材及步骤字段进行混合检索。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 17, 'graph_rag_count': 0, 'total_queries': 17}
- route_stats_after: {'traditional_count': 18, 'graph_rag_count': 0, 'total_queries': 18}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['日式肥牛丼饭', '肥牛', '米饭', '洋葱', '肥牛丼']
- topic_keywords: ['日式料理', '丼饭', '备料', '烹饪步骤', '调味', '火候']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 8804

## Hybrid Branch Status / entity_level
- keywords: ['日式肥牛丼饭', '肥牛', '米饭', '洋葱', '肥牛丼']
- requested_k: 10
- actual_count: 4
- fallback_count: 0
- duration_ms: 37

## Hybrid Branch Status / topic_level
- keywords: ['日式料理', '丼饭', '备料', '烹饪步骤', '调味', '火候']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 74

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 350

## Hybrid Branch Summary
- entity_count: 4
- topic_count: 10
- vector_count: 10
- origin_len: 24

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 24
- after_count: 20
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
- candidate_count: 21
- duration_ms: 15995
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 2, '荤菜': 1, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 25179
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:40:07.536
- end: 2026-08-11T19:40:39.412
- duration_ms: 31876
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
- chunk_count: 408
- redacted_field: 2032
- total_duration_ms: 15867
- fallback_used: False

## Final Output
- answer_chars: 535
- answer_hash: 93ecba802ef1fa9a
- success: True

## Request Complete
- request_end: 2026-08-11T19:40:55.296
- request_duration_ms: 47766
- success: True
- final_source: generation

