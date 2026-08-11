# RAG Process

audit_id: 20260811_194803_914_629279c2
timestamp: 2026-08-11T19:48:03.914
## Request
- original_query: 有鸭肉可以做什么菜？哪些菜谱确实包含它？
- original_query_hash: 7b066efcaf46ec37
- session_id: 2026-08-12-真实考试-001:new:S04-B-04
- request_mode: stream
- request_start: 2026-08-11T19:48:03.914
- evaluation_sample_id: 20260811_194803_914_629279c2
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:48:03.915
- end: 2026-08-11T19:48:03.915
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:48:03.916
- end: 2026-08-11T19:48:03.916
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 20
- enhanced_query_length: 20
- enhanced_query_hash: 7b066efcaf46ec37

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:48:03.919
- end: 2026-08-11T19:48:03.919
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:03.919+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:48:03.921
- end: 2026-08-11T19:48:03.921
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:03.919+00:00
- result_count: 2

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:48:03.921
- end: 2026-08-11T19:48:03.921
- duration_ms: 0
- template_id: ingredient_recipes_v1
- graph_fact_status: verified
- graph_fact_count: 1
- limitations: []
- vector_search_calls: 0

## Prompt Assembly
- prompt_template_name: cooking_assistant_evidence
- prompt_template_version: evidence_v1
- prompt_template_hash: cdfbc1c106e93d1c
- context_doc_count: 0
- context_chars: 720
- retrieval_levels: []
- search_types: []
- stream: True
- max_retries: 3
- evidence_bundle: True
- verified_graph_fact_count: 1
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
- chunk_count: 111
- redacted_field: 2089
- total_duration_ms: 4781
- fallback_used: False

## Final Output
- answer_chars: 156
- answer_hash: 6af70a65927e3ea7
- success: True

## Request Complete
- request_end: 2026-08-11T19:48:08.713
- request_duration_ms: 4798
- success: True
- final_source: generation

