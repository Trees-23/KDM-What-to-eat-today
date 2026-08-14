# 推荐约束与重排执行提示词 V1

将以下内容完整交给负责实现的 AI。它应直接在当前仓库内完成实现、测试、提交、推送和 PR 维护；不得只给方案或停在分析。

---

你是本仓库的实现负责人。请实现 `_other/RECOMMENDATION_CONSTRAINTS_RERANK_IMPLEMENTATION_PLAN_V1.md` 中的“推荐约束需求单、硬过滤与重排”方案，并严格遵守本仓库及用户提供的 `AGENTS.md` 规则。

## 交付目标

修复 `PREFERENCE_RECOMMEND` 路径中“意图/槽位识别正确，但模糊推荐候选不满足显式做法或工具条件”的问题。目标流程必须是：

```text
IntentCandidate
  -> 本地 ConstraintSpec
  -> 硬过滤 parent_id 范围
  -> 受限向量召回 candidate_k
  -> 本地确定性重排
  -> answer_k PDS 证据
  -> 生成回答
```

禁止让 LLM 输出或执行 Cypher、Milvus filter、实体 ID、`parent_id`、权重、排序表达式或 `QueryPlan`。

## 开始前必须做

1. 读取所有适用的 `AGENTS.md`。
2. 检查分支、工作区、远端和默认分支；保护已有用户改动。
3. 不在 `main`/`master` 上开发；创建独立 ASCII 任务分支。
4. 先通读以下文件及现有测试：
   - `_other/RECOMMENDATION_CONSTRAINTS_RERANK_IMPLEMENTATION_PLAN_V1.md`
   - `rag_modules/intent_candidate.py`
   - `rag_modules/intent_plan_compiler.py`
   - `rag_modules/query_plan.py`
   - `rag_modules/query_plan_validator.py`
   - `rag_modules/parent_document_materializer.py`
   - `rag_modules/parent_document_store.py`
   - `rag_modules/restricted_vector_retrieval.py`
   - `main.py`
   - `rag_modules/planner_acceptance_runtime.py`
   - `test/test_intent_plan_compiler.py`
   - `test/test_restricted_vector_retrieval.py`
   - `test/test_intent_planner_acceptance_runner.py`

## 必须实现

### 1. 约束需求单

- 新增低权限、严格校验的 `ConstraintSpec` 数据模型及本地分类器。
- 不改变 LLM 的职责：LLM 继续只输出 `IntentCandidate` 的 intent/槽位。
- 本地代码依据用户真实文本中的强度词（例如“只、仅、必须、不能、完全不要”）和受控槽位，决定每项进入硬过滤、软偏好或澄清/终止。模型原始食材词只有经 `EntityResolver` 唯一解析后才能变为本地 `verified_ingredient_ids`。
- V1 至少覆盖：菜系、方法、工具、总时长、份量、餐次、`LIGHT_FEEL`、`FEW_STEPS`、歧义和严格营养边界。
- 对不存在或不可信的结构化属性必须保守处理，不能伪造值。

### 2. PDS 属性物化

- 在 Recipe 父文档 metadata 中加入受控、可追溯的聚合字段：`recipe_methods`、`recipe_tools`、`recipe_cooking_appliances`、`step_count`、`prep_minutes`、`cook_minutes`、`total_minutes`、`servings_count` 及属性来源。`step_count` 必须来自可追溯的 Recipe 步骤聚合；未知时为 `null`，不能以正文行数或字符数猜测。
- 复用 Neo4j Recipe/Step 的现有 `methods`、`tools`、时间、份量数据；不要在请求路径扫描 Markdown。
- 明确 `recipe_cooking_appliances` 只表示直接烹饪设备。V1 中“只有微波炉”的判定必须是“包含 `MICROWAVE` 且不依赖其他烹饪设备”；刀、碗、筷子等准备工具不算冲突。
- 保持 PDS build 的不可变、版本化和 Milvus linkage 约束。任何 metadata 改动都必须通过重建/校验流程验证。

### 3. 硬过滤

- 在推荐意图中，先构造候选 `parent_id` 范围：现有菜系/经本地解析的具名食材范围与新增正向方法、工具、烹饪设备、可解析时长范围取交集；`不能用微波炉`、`完全不要油炸`等排除条件必须以前置集合差实现。
- “只有微波炉”“必须蒸制”等明确约束必须在向量检索前过滤。
- 空交集必须返回可解释的 `NO_PREFERENCE_RESULTS`，不得扩大到全库或悄悄放宽条件。
- 保持 `QueryPlanValidator` 和 `RestrictedVectorRetriever` 的白名单、`parent_ids`、PDS 回补与审计链路；不得新增任意查询接口。

### 4. 两段式召回与重排

- 推荐路径区分 `candidate_k`（默认 30）和 `answer_k`（默认 5）。
- 完整可信用户问题仍作为向量查询，使软偏好参与候选召回。
- 新增确定性本地 `PreferenceReranker`，在向量候选返回后、生成前执行。
- V1 使用可解释规则，不调用第二个 LLM：
  - 按方案中的 `recommendation_rerank_v1` 固定评分表实现，不能凭经验另设分值。
  - `LIGHT_FEEL` 对蒸/煮加分，对炸制扣分；不能据此作营养断言。
  - `FEW_STEPS`、可解析总时长短加分；未知字段不加分、不扣分。
  - 份量仅作为软分；V1 不对餐次打结构化分，除非先新增有来源的餐次字段。
  - 已作为硬过滤的工具/方法不应被不符合者以高向量分绕过。
- 排序必须稳定，并记录 `vector_score`、每项 bonus/penalty、`final_score`、属性来源和未知字段。

### 5. 审计、回退与测试

- 在 RAG audit 中记录 `ConstraintSpec`、各硬范围大小和交集、候选 TopN、重排后的 TopK、每条分数解释和空集原因；不保存敏感原始内容。
- 新能力必须受 feature flag 控制，默认关闭；关闭时不改变现有行为。
- 保持严格营养、图关系、实体不存在、图服务故障等现有安全行为。
- 新增单元测试、集成测试和推荐回归题，至少覆盖：
  - 只有微波炉（最终候选必须含 `MICROWAVE`，且不依赖其他烹饪设备）。
  - 必须蒸制。
  - 川菜且蒸制。
  - 清爽川味蒸菜不再把麻辣香锅、火锅底料列为最终 TopK。
  - 少工具早餐。
  - 硬范围空集。
  - metadata 未知字段。
  - feature flag 关闭的兼容行为。
- 重跑与改动范围匹配的既有测试；若运行真实 300 题验收，必须是单次全量运行，不能以聚合台账代替。

## 不得做

- 不为固定题目、菜名或题号写特例。
- 不直接在向量 Top5 后过滤来伪装硬约束。
- 不放宽 `QueryPlanValidator` 的执行权限。
- 不把“清爽/少油”说成低脂、低热量、医疗适用。
- 不提交既有用户的无关考试产物、密钥或大临时文件。
- 不使用 `git add -A` 或 `git add .`；只暂存本次任务的明确路径。

## 交付方式

1. 分阶段实施，每个独立可验证阶段创建中文提交并立即推送。
2. 第一个可审查提交推送后创建同一条草稿 PR；完成验证后更新为可审查状态。PR 标题、正文、提交信息均使用中文。
3. PR 正文至少包含“改动内容”“验证结果”“风险与注意事项”。
4. 完成后用中文报告：分支、提交、推送、PR 链接与状态、验证结果；明确等待用户确认后才可合并 `main`。

开始实现。遇到不确定的内部 API 时，先读取现有代码、测试和相邻实现；在不扩大权限和不破坏证据链的前提下作保守选择。
