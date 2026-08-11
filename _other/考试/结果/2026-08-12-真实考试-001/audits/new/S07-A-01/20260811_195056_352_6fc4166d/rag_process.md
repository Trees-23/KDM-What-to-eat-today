# RAG Process

audit_id: 20260811_195056_352_6fc4166d
timestamp: 2026-08-11T19:50:56.353
## Request
- original_query: 想吃川菜但口感清爽。请推荐几个可考虑的菜。
- original_query_hash: 821badeb7b47a5d5
- session_id: 2026-08-12-真实考试-001:new:S07-A-01
- request_mode: stream
- request_start: 2026-08-11T19:50:56.354
- evaluation_sample_id: 20260811_195056_352_6fc4166d
- experiment_id: 2026-08-12-真实考试-001
- variant_name: new
- config_hash: 809c44f80acbae2f

## Event / cache_check
- stage: cache_check
- status: completed
- start: 2026-08-11T19:50:56.354
- end: 2026-08-11T19:50:56.354
- duration_ms: 0
- cache_hit: False
- cached_response_chars: 0

## Event / context_enhancement
- stage: context_enhancement
- status: completed
- start: 2026-08-11T19:50:56.355
- end: 2026-08-11T19:50:56.355
- duration_ms: 0
- enhanced: False
- history_count: 0
- original_query_length: 21
- enhanced_query_length: 21
- enhanced_query_hash: 821badeb7b47a5d5

## Errors
- stage: stream_request
- status: error
- error_type: ProgrammingError
- error_message: SQLite objects created in a thread can only be used in that same thread. The object was created in thread id 123672818324224 and this is thread id 123666372220608.

## Request Complete
- request_end: 2026-08-11T19:50:56.355
- request_duration_ms: 1
- success: False
- final_source: error

