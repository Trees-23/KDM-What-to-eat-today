# RAG Process

audit_id: 20260811_194839_811_ac0091b0
timestamp: 2026-08-11T19:48:39.811
## Request
- original_query: 西兰花能做什么菜？请只列出图关系能够证明使用了它的菜谱，不要按常识补菜名。
- original_query_hash: ee54715779723749
- session_id: 2026-08-12-真实考试-001:new:S04-C-02
- request_mode: stream
- request_start: 2026-08-11T19:48:39.812
- evaluation_sample_id: 20260811_194839_811_ac0091b0
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:48:39.812
- end: 2026-08-11T19:48:39.812
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:48:39.813
- end: 2026-08-11T19:48:39.813
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 37
- enhanced_query_length: 37
- enhanced_query_hash: ee54715779723749

## Event / targeted_graph
- stage: targeted_graph
- status: started
- start: 2026-08-11T19:48:39.816
- end: 2026-08-11T19:48:39.816
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:39.816+00:00

## Event / targeted_graph
- stage: targeted_graph
- status: verified
- start: 2026-08-11T19:48:39.818
- end: 2026-08-11T19:48:39.818
- duration_ms: 0
- template_id: ingredient_recipes_v1
- intent: INGREDIENT_RECIPES
- database_timestamp: 2026-08-11T19:48:39.816+00:00
- result_count: 1

## Event / targeted_graph_selection
- stage: targeted_graph_selection
- status: verified
- start: 2026-08-11T19:48:39.818
- end: 2026-08-11T19:48:39.818
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
- context_chars: 533
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
- chunk_count: 63
- redacted_field: 1789
- total_duration_ms: 3107
- fallback_used: False

## Final Output
- answer_chars: 79
- answer_hash: e5d1c31fe10ef73a
- success: True

## Request Complete
- request_end: 2026-08-11T19:48:42.961
- request_duration_ms: 3149
- success: True
- final_source: generation

