# 新路径统一意图规划独立调研提示词

你是本仓库检索重构的独立架构调研 AI。你的任务是只读调研“new 路径为何缺少
前置 LLM 意图规划层，以及应如何在保留证据和安全边界的前提下修复”。不要直接
修改代码或数据，也不要把关键词扩充当作最终方案。

## 仓库与输出

项目根目录：

```text
/home/kdm/MyWorkSpace/AgentLearnSpace/AllProjects/What-to-eat-today-main/What-to-eat-today-main
```

请在最终答复中给出一份中文调研报告。除非用户明确授权，不创建、修改、删除或
提交任何文件。所有结论必须附带可复核的文件路径、函数名、行号或审计位置。

## 已知症状

1. S06-A-02：

```text
下班很晚，想找准备步骤少的家常菜。请推荐知识库中最合适的菜，并说明依据。
```

实际走 `entity_not_found`，没有候选、没有 PDS 正文证据；预期应是受控的偏好
推荐检索。

2. S07-A-02：

```text
想找少油感觉的川味晚餐。请推荐几个可考虑的菜。
```

实际走 `entity_not_found`；代码只识别精确“川菜”和很少的软偏好词，无法理解
“川味”“少油感觉”等释义。

3. S07-C 组题目中附带“不要断言低脂”等安全约束文字时，当前营养规则会把它当成
用户正在请求严格营养结论，导致提前返回 `NUTRITION_EVIDENCE_INSUFFICIENT`，不
检索候选。

4. S05-A-02：检索已获得 verified 图路径和 PDS 回补，但 SSE 只返回 `[DONE]`；
审计显示 `chunk_count=0`、`answer_chars=0`，却仍记录为成功。

## 已知实际调用链

当前 `main.py` 的 `AdvancedGraphRAGSystem.retrieve_for_generation()` 大致执行：

```text
用户问题
  -> _try_nutrition_recommendation（字面规则）
  -> _new_path_rollout_stage
  -> _try_targeted_graph（字面规则 + 实体解析）
  -> _preference_plan（短关键词表）
  -> _try_entity_direct（从整句中找菜谱/技巧实体）
       无候选且 allow_generalized_advice=false -> ENTITY_NOT_FOUND 并结束
  -> _legacy_fallback_or_decline（只在前面没有提前返回时）
```

旧 `IntelligentQueryRouter` 有 LLM 的 `analyze_query()`，但 new 路径正常执行时不会
调用它。请不要简单建议“开启旧路径”；目标是 new 路径自己拥有受控的意图规划。

## 原始设计意图

阅读并核对：

- `_other/RETRIEVAL_REFACTOR_IMPLEMENTATION_PLAN_V1.md`
- `_other/RETRIEVAL_REFACTOR_EXECUTION_AGENT_PROMPT_V1.md`
- `main.py`
- `rag_modules/query_plan.py`
- `rag_modules/query_plan_validator.py`
- `rag_modules/entity_resolver.py`
- `rag_modules/nutrition_policy.py`
- `rag_modules/targeted_graph_retrieval.py`
- `rag_modules/restricted_vector_retrieval.py`
- `rag_modules/generation_integration.py`
- `rag_modules/web_service_handler.py`

原方案要求：用户问题先形成经 schema 校验的 `QueryPlan`；LLM 如参与，只能提出 JSON
候选计划，validator 只能允许固定 intent/template/实体类型/参数上限，拒绝任意 Cypher。
当前 `QueryPlanValidator` 已接受 `source="llm_candidate"`。请核查这是否是未完成的
设计、被后续规则绕开，还是另有原因。

## 调研问题

请逐项回答，不要跳过：

1. 当前 new 路径的完整真实调用顺序是什么？哪些步骤使用关键词，哪些调用 LLM，
   哪些条件会提前返回并阻止后续 Router？
2. 原始设计与当前实现的偏差是什么？精确指出已有但未接入的能力。
3. 是否应增加前置 LLM Intent Planner？请从正确性、延迟、成本、可审计性、注入风险、
   失败降级和测试稳定性给出论证，而非只表达赞成或反对。
4. 设计一个最小 `IntentCandidate` JSON schema。LLM 可以输出哪些字段？绝不能输出
   哪些字段？为什么不应直接把 LLM JSON 当执行 `QueryPlan`？
5. 给出“意图 -> 本地编译 -> 已有白名单执行器 -> 证据要求 -> 错误状态”的映射表。
   至少覆盖：实体查找、菜谱详情、步骤、技巧章节、食材到菜谱、食材到蔬菜、场景/偏好
   推荐、软口味偏好、严格营养约束、不清楚/超范围请求。
6. 明确 `ENTITY_NOT_FOUND` 的正确语义和触发时机，解释为什么 S06/S07 不能落入该状态。
7. 现有关键词规则哪些应保留为硬安全门，哪些应降级为偏好槽位抽取/会话记忆/LLM 后校验？
8. 如何防止“不要断言低脂”之类系统或评测约束污染用户意图？需要什么输入边界？
9. 如何保证 LLM planner 不会造成任意 Cypher、任意向量范围、伪造 nodeId、图关系伪证
   或严格营养误报？
10. S05 的空 SSE 成功应如何独立修复和测试？它与意图规划应如何在实施计划中解耦。
11. 以正式 300 题为基础，提出 planner-only、检索层、生成层三层测试方案，并特别涵盖
   S06/S07 的释义改写和失败注入。
12. 给出至少三种方案及取舍：
    - 仅扩关键词；
    - 前置 LLM 意图规划 + 本地计划编译；
    - 复用/改造旧 Router。
    明确推荐方案和不推荐方案的具体原因。

## 必须保留的约束

- 不允许 LLM 生成或执行任意 Cypher、SQL、Milvus filter、collection 名、nodeId 或
  parent_id。
- 图关系只能由固定 QueryPlan + 白名单模板得到，并且只有 `GraphFact.status=verified`
  才可在回答中当作关系事实。
- 向量检索必须受 QueryPlan scope 限制，命中必须 PDS 回补；不得退回旧的未受限向量检索。
- 严格低脂、热量、医疗饮食等断言必须有受治理来源；没有来源时必须明确证据不足。
- 不得通过为每道题添加专用词或题干 allowlist 来伪造泛化能力。
- 对非法 JSON、未知意图、低置信度、planner 超时/空响应，必须设计 fail-closed 行为，
  但不得把泛化推荐误写成“实体不存在”。
- `chunk_count=0` 或 `answer_chars=0` 的生成流不得被记为成功。

## 可复核证据

本次监考审计：

- `_other/考试/测试试卷2/结果/2026-08-12-new-smoke-004/audits/new/S05-A-02/20260812_061725_654_af9dbc9c/`
- `_other/考试/测试试卷2/结果/2026-08-12-new-smoke-004/audits/new/S06-A-02/20260812_062254_062_b99fa6f5/`
- `_other/考试/测试试卷2/结果/2026-08-12-new-smoke-004/audits/new/S07-A-02/20260812_062329_410_8c59c2a2/`

正式题库：

```text
_other/考试/检索重构真实场景考试包/试卷题库.json
```

已有定向结论和运行态统计表明：S06 30 题中 28 题会落入 `ENTITY_NOT_FOUND`；S07 30
题中 14 题会落入 `ENTITY_NOT_FOUND`、10 题会被严格营养误触发。请自行复核，不要直接
把这项描述当作结论。

## 交付格式

用以下结构输出：

1. 执行摘要
2. 当前真实路径图
3. 原始设计与实现偏差
4. 根因与风险分级
5. 候选架构与推荐方案
6. `IntentCandidate` schema 与本地编译边界
7. 意图/执行器/证据/失败状态映射表
8. 分阶段修复和测试计划
9. 开放问题与需用户决策项
10. 引用证据清单

请坚持调研立场：指出问题、证据和可选方案；除非得到明确实现授权，不修改代码、配置、
数据库、PDS、Milvus 或既有考试产物。
