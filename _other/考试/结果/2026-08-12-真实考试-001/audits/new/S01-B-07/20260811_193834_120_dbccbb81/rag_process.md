# RAG Process

audit_id: 20260811_193834_120_dbccbb81
timestamp: 2026-08-11T19:38:34.121
## Request
- original_query: 干锅花菜从备料到出锅怎么做？请按知识库里的做法回答。
- original_query_hash: 47574e889fb5ff45
- session_id: 2026-08-12-真实考试-001:new:S01-B-07
- request_mode: stream
- request_start: 2026-08-11T19:38:34.121
- evaluation_sample_id: 20260811_193834_120_dbccbb81
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:38:34.122
- end: 2026-08-11T19:38:34.122
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:38:34.123
- end: 2026-08-11T19:38:34.123
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 26
- enhanced_query_length: 26
- enhanced_query_hash: 47574e889fb5ff45

## Event / entity_direct_request
- stage: entity_direct_request
- status: started
- start: 2026-08-11T19:38:34.129
- end: 2026-08-11T19:38:34.129
- duration_ms: 0
- entity_id: 201005383
- scope: RECIPE_FULL

## Event / entity_direct_pds
- stage: entity_direct_pds
- status: unavailable
- start: 2026-08-11T19:38:34.129
- end: 2026-08-11T19:38:34.129
- duration_ms: 0
- error_type: ProgrammingError

## Event / entity_direct
- stage: entity_direct
- status: fallback
- start: 2026-08-11T19:38:34.129
- end: 2026-08-11T19:38:34.129
- duration_ms: 0
- candidate_count: 1
- graph_fact_statuses: ['verified']
- text_evidence_count: 0
- limitations: ['parent-store-unavailable', '父文档库不可用，已关闭实体直达并应回退旧检索路径。']
- vector_search_calls: 0

## Query Analysis Input
- analysis_input_query_length: 26
- analysis_input_query_hash: 47574e889fb5ff45
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T19:38:34.129
- end: 2026-08-11T19:38:43.666
- duration_ms: 9536
- analysis_mode: llm
- query_complexity: 0.25
- relationship_intensity: 0.3
- reasoning_required: False
- entity_count: 3
- strategy: hybrid_traditional
- confidence: 0.94
- reasoning: 该查询属于明确的菜谱步骤检索，核心目标是从知识库中获取“干锅花菜”的标准做法，并按“备料—烹饪—出锅”的顺序组织回答。查询中的明确实体可识别为“干锅花菜”（菜品）、“备料”（烹饪阶段）和“出锅”（烹饪阶段）。虽然存在食材准备与烹饪步骤之间的顺序关系，但不涉及跨实体的复杂关联、因果解释或多方案比较，不需要多跳推理、因果分析或对比分析。因此适合使用 hybrid_traditional，通过关键词匹配、语义检索及菜谱字段过滤定位知识库中的对应做法。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 15, 'graph_rag_count': 0, 'total_queries': 15}
- route_stats_after: {'traditional_count': 16, 'graph_rag_count': 0, 'total_queries': 16}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['干锅花菜', '花菜', '五花肉', '干辣椒', '青椒', '蒜', '干锅']
- topic_keywords: ['川菜', '香辣', '下饭菜', '家常菜', '火候', '烹饪技巧']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 3201

## Hybrid Branch Status / topic_level
- keywords: ['川菜', '香辣', '下饭菜', '家常菜', '火候', '烹饪技巧']
- requested_k: 10
- actual_count: 10
- fallback_count: 10
- duration_ms: 76

## Hybrid Branch Status / entity_level
- keywords: ['干锅花菜', '花菜', '五花肉', '干辣椒', '青椒', '蒜', '干锅']
- requested_k: 10
- actual_count: 10
- fallback_count: 4
- duration_ms: 78

## Hybrid Branch Status / vector_enhanced
- requested_k: 10
- actual_count: 10
- collection: cooking_knowledge
- metric: default
- ef: default
- embedding_model: /app/bge-small-zh-v1.5
- duration_ms: 476

## Hybrid Branch Summary
- entity_count: 10
- topic_count: 10
- vector_count: 10
- origin_len: 30

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 30
- after_count: 25
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 3
- expanded_count: 9
- doc_names: ['炒/煎', '辅料技巧']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 26
- duration_ms: 18120
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'素菜': 2, '烹饪技巧': 2, '高级技巧': 1}
- deferred_count: 0
- selected_count: 5

## Hybrid Technique Expansion Final Guard
- enabled: True
- inserted: True
- replaced_recipe_name: 清炒花菜
- final_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 21835
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T19:38:34.129
- end: 2026-08-11T19:39:05.502
- duration_ms: 31372
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3331
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
- chunk_count: 499
- redacted_field: 3754
- total_duration_ms: 13902
- fallback_used: False

## Final Output
- answer_chars: 693
- answer_hash: 6363c37f8c70e041
- success: True

## Request Complete
- request_end: 2026-08-11T19:39:19.416
- request_duration_ms: 45294
- success: True
- final_source: generation

