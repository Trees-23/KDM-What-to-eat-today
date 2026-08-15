# RAG Process

audit_id: 20260811_193744_990_1ed1b343
timestamp: 2026-08-11T19:37:44.991
## Request
- original_query: 红烧茄子从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 65f7c47f22bf3c7a
- session_id: 2026-08-12-真实考试-001:new:S01-B-06
- request_mode: stream
- request_start: 2026-08-11T19:37:45.001
- evaluation_sample_id: 20260811_193744_990_1ed1b343
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:37:45.002
- end: 2026-08-11T19:37:45.002
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:37:45.002
- end: 2026-08-11T19:37:45.002
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 65f7c47f22bf3c7a

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:37:45.009
- end: 2026-08-11T19:37:45.009
- duration_ms: 0
- entity_id: 201005049
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:37:45.010
- end: 2026-08-11T19:37:45.010
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:37:45.010
- end: 2026-08-11T19:37:45.010
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 65f7c47f22bf3c7a
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:37:45.010
- end: 2026-08-11T19:37:51.359
- duration_ms: 6348
- analysis_mode: llm
- query_complexity: 0.32
- relationship_intensity: 0.28
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询是面向特定菜品“红烧茄子”的流程型事实检索，核心诉求是依据知识库获取从备料、处理、烹饪到出锅的标准做法。虽然包含“备料—烹制—出锅”的步骤顺序，但属于单一菜品制作流程的线性信息整合，不需要跨实体的复杂关系推理、多跳推理、因果分析或方案对比。明确实体主要包括“红烧茄子”（菜品）、“茄子”（食材）和“知识库中的做法”（知识来源/约束）。建议采用 hybrid_traditional，通过关键词检索、语义检索和步骤字段匹配定位知识库中的权威食谱，再按流程顺序组织答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 14, 'graph_rag_count': 0, 'total_queries': 14}
- route_stats_after: {'traditional_count': 15, 'graph_rag_count': 0, 'total_queries': 15}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['红烧茄子', '茄子', '蒜', '生抽', '老抽', '蚝油', '白糖', '淀粉', '食用油']
- topic_keywords: ['家常菜', '红烧', '下饭菜', '烹饪技巧', '备料', '火候', '入味']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3384

## Hybrid Branch Status / entity_level
- keywords: ['红烧茄子', '茄子', '蒜', '生抽', '老抽', '蚝油', '白糖', '淀粉', '食用油']
- requested_k: 10
- actual_count: 10
- fallback_count: 1
- duration_ms: 76

## Hybrid Branch Status / topic_level
- keywords: ['家常菜', '红烧', '下饭菜', '烹饪技巧', '备料', '火候', '入味']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 77

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 320

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 28
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
- candidate_count: 29
- duration_ms: 25128
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '荤菜': 1, '烹饪技巧': 1, '主食': 1}
- deferred_count: 4
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 茄子肉煎饼
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 28855
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:37:45.010
- end: 2026-08-11T19:38:20.216
- duration_ms: 35205
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3823
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
- chunk_count: 571
- redacted_field: 2006
- total_duration_ms: 13869
- fallback_used: False

## Final Output
- answer_chars: 742
- answer_hash: f8b1059cdfb6c57d
- success: True

## Request Complete
- request_end: 2026-08-11T19:38:34.106
- request_duration_ms: 49105
- success: True
- final_source: generation

