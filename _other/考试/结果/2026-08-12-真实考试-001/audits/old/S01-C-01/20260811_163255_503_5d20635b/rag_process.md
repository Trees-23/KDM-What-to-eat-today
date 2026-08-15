# RAG Process

audit_id: 20260811_163255_503_5d20635b
timestamp: 2026-08-11T16:32:55.507
## Request
- original_query: 我只要知识库能证明的手工水饺做法；不要补充未引用的替代方案或营养结论。
- original_query_hash: f595486f4bf2239b
- session_id: 2026-08-12-真实考试-001:old:S01-C-01
- request_mode: stream
- request_start: 2026-08-11T16:32:55.507
- evaluation_sample_id: 20260811_163255_503_5d20635b
- experiment_id: 2026-08-12-真实考试-001
- variant_name: old
- config_hash: d0e8a20ad765d57a

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T16:32:55.508
- end: 2026-08-11T16:32:55.508
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T16:32:55.508
- end: 2026-08-11T16:32:55.508
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 35
- enhanced_query_length: 35
- enhanced_query_hash: f595486f4bf2239b

## Event / retrieval_rollout
- stage: retrieval_rollout
- status: legacy
- start: 2026-08-11T16:32:55.508
- end: 2026-08-11T16:32:55.508
- duration_ms: 0
- reason: not_selected

## Query Analysis Input
- analysis_input_query_length: 35
- analysis_input_query_hash: f595486f4bf2239b
- llm_model: gpt-5.6-terra
- temperature: 0.1
- redacted_field: 800

## Event / query_analysis
- stage: query_analysis
- status: completed
- start: 2026-08-11T16:32:55.508
- end: 2026-08-11T16:33:26.101
- duration_ms: 30592
- analysis_mode: llm
- query_complexity: 0.45
- relationship_intensity: 0.3
- reasoning_required: True
- entity_count: 2
- strategy: hybrid_traditional
- confidence: 0.91
- reasoning: 查询的核心目标是检索知识库中可明确引用和验证的“手工水饺做法”，属于以事实/步骤抽取为主的定向信息查找。额外约束包括：答案必须由知识库证据支持、不得补充无引用的替代方案、不得输出未被引用支持的营养结论。这需要进行检索结果的证据对齐、引用覆盖校验和生成约束控制，但通常不需要跨多个实体构建复杂关系网络或进行多跳知识推理。明确实体主要为“手工水饺”（菜品/制作对象）和“知识库”（证据来源/数据资源）。建议采用 hybrid_traditional，通过关键词检索、语义检索与重排序定位做法步骤、配料及证据片段，并仅基于已检索到的引用内容生成答案。

## Routing Decision
- selected_strategy: hybrid_traditional
- top_k: 5
- route_stats_before: {'traditional_count': 20, 'graph_rag_count': 0, 'total_queries': 20}
- route_stats_after: {'traditional_count': 21, 'graph_rag_count': 0, 'total_queries': 21}

## Hybrid Retrieval Config
- top_k: 5
- candidate_k: 10
- enable_rerank: True
- rerank_model: /app/bge-reranker-v2-m3
- rerank_batch_size: 8
- embedding_model: /app/bge-small-zh-v1.5

## Hybrid Keyword Extraction
- entity_keywords: ['手工水饺', '水饺']
- topic_keywords: ['水饺做法', '烹饪技巧', '知识库依据', '引用证据']
- prompt_template_hash: 4d1b8c6d6f80a734
- duration_ms: 4185

## Hybrid Branch Status / topic_level
- keywords: ['水饺做法', '烹饪技巧', '知识库依据', '引用证据']
- requested_k: 10
- actual_count: 0
- fallback_count: 0
- duration_ms: 12

## Hybrid Branch Status / entity_level
- keywords: ['手工水饺', '水饺']
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
- duration_ms: 605

## Hybrid Branch Summary
- entity_count: 1
- topic_count: 0
- vector_count: 10
- origin_len: 11

## Hybrid Merge Dedup
- dedupe_key: node_id -> recipe_name -> hash(page_content[:300])
- before_count: 11
- after_count: 6
- duplicate_count: 5

## Hybrid Technique Expansion
- enabled: True
- seed_count: 2
- expanded_count: 9
- doc_names: ['焯水', '凉拌']

## Hybrid Rerank
- enabled: True
- model: /app/bge-reranker-v2-m3
- load_success: True
- batch_size: 8
- candidate_count: 7
- duration_ms: 13798
- fallback_used: False

## Hybrid Diversity
- max_per_category: 2
- category_counts: {'主食': 1, '半成品': 1, '早餐': 1, '烹饪技巧': 2}
- deferred_count: 0
- selected_count: 5

## Hybrid Retrieval Complete
- hybrid_total_duration_ms: 18618
- final_count: 5

## Event / route_query
- stage: route_query
- status: completed
- start: 2026-08-11T16:32:55.508
- end: 2026-08-11T16:33:44.720
- duration_ms: 49211
- selected_strategy: hybrid_traditional
- document_count: 5

## Prompt Assembly
- prompt_template_name: cooking_assistant_default
- prompt_template_version: v1
- prompt_template_hash: c95588d3477d7cf8
- context_doc_count: 5
- context_chars: 3553
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
- chunk_count: 650
- redacted_field: 1944
- total_duration_ms: 17918
- fallback_used: False

## Final Output
- answer_chars: 854
- answer_hash: b2acbc6f8f7ad1dd
- success: True

## Request Complete
- request_end: 2026-08-11T16:34:02.670
- request_duration_ms: 67163
- success: True
- final_source: generation

