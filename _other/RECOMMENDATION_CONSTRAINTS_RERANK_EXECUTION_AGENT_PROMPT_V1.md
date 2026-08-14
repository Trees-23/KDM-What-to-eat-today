# 推荐约束与重排执行提示词 V1

将以下内容完整交给负责实现的 AI。它应在当前仓库中完成实现、测试、提交、推送和 PR 维护；不得只给方案或停在分析。

---

你是本仓库的实现负责人。请实现 `_other/RECOMMENDATION_CONSTRAINTS_RERANK_IMPLEMENTATION_PLAN_V1.md`，并以 `_other/考试/推荐约束与重排验收-V1/` 作为本次唯一的最终验收试卷。严格遵守仓库和用户提供的 `AGENTS.md`。

## 交付目标

实现以下路径：

```text
IntentCandidate
  -> 本地 ConstraintSpec
  -> 本地 ResolvedCandidateScope
  -> Top30 候选 metadata
  -> 确定性重排
  -> Top5 PDS 正文证据
  -> 生成回答
```

LLM 只能输出 `IntentCandidate` 的意图和受控槽位，不能输出或执行 Cypher、Milvus filter、实体 ID、`parent_id`、权重、排序表达式或 `QueryPlan`。

## 开始前

1. 读取所有适用的 `AGENTS.md`，检查分支、工作区、远端和默认分支，保护用户已有改动。
2. 不在 `main`/`master` 开发；创建或继续独立 ASCII 任务分支。
3. 通读实施方案、专用验收卷、现有 intent/PDS/retrieval 代码和相邻测试。
4. 不提交无关考试结果、密钥、大型临时文件；脏工作区不得使用 `git add -A` 或 `git add .`。

## 必须实现

### 1. 条件强弱由本地原话规则决定

- 新增严格校验、低权限的 `ConstraintSpec` 与 `RecommendationConstraintCompiler`。
- `IntentCandidate` 只表明“提到了哪个工具/做法”；本地代码读取真实用户问题中的强度、否定和排他表达，决定软偏好、正向硬约束或排除硬约束。
- `只`、`仅`、`只能`、`只有`、`只用`、`必须`升级为正向硬约束；`不要`、`不能`、`不得`、`完全不要`、`不使用`升级为排除硬约束；`优先`、`尽量`、`也行`、`最好`和无明确限制词保持软偏好。
- “家里只有微波炉”必须按排他性硬约束处理。否定对象、冲突或歧义无法可靠识别时澄清。
- 具名食材只有经 `EntityResolver` 唯一解析后才能成为执行 ID。

### 2. 做法、设备与 PDS 属性

- 增加 `STIR_FRY`；将“炒、煸炒、爆炒”等本地归一化为该枚举，并同步更新 `IntentSlots`、planner 提示和测试。
- 物化 `recipe_methods`、`recipe_tools`、`recipe_cooking_appliances`、`recipe_optional_cooking_appliances`、未知设备状态、步骤数、时间、份量及属性来源。
- “只能用微波炉”只能命中：包含 `MICROWAVE`、没有其他已知必需烹饪设备、没有未知必需设备的菜谱。刀、碗、筷子不算烹饪设备；可选替代设备不算冲突。
- 不在请求路径扫描 Markdown；新增活动 PDS build 的只读 Recipe metadata 查询接口。
- 属性变动后重建 PDS、Milvus V2、联合 manifest，并运行 linkage 和覆盖率校验。

### 3. 硬范围与 Top30

- 在向量查询前计算 `ResolvedCandidateScope`：已验证菜系/食材和正向条件取交集，排除条件取差集。
- 空范围返回可解释的 `NO_PREFERENCE_RESULTS`，不得回退全库。
- `max_hard_scope` 默认 200 且可配置；`candidate_k=30`，`answer_k=5`。
- 51..200 个本地 verified `parent_id` 仍必须可以受限查询。容量调整不得新增 QueryPlan 模板、字段、LLM 可控输入或任意查询能力。
- 分批 Milvus 查询必须全局合并后选 Top30，不能按批次截断。

### 4. 两段式重排

- 第一段取 Top30 的 ID、标题、检索分和 metadata，不读取完整父文档。
- 新增确定性 `PreferenceReranker`，严格使用实施方案中的 `recommendation_rerank_v1` 评分表。
- 第二段只为最终 Top5 回补 PDS 正文，再交给生成层。
- 审计分开记录原始 chunk 分、coverage bonus、聚合检索分和重排分，且排序稳定。

### 5. 单次故障处理与验收

- 不因单次错误自动关闭全局新路径。每次故障只影响当前请求并写审计/告警。
- 硬过滤成功但重排失败时，可返回原始受限向量排序；不得放宽硬约束。
- PDS/Milvus/工件不一致时，当前请求必须明确不可验证，不能伪造硬约束满足。
- 新增单元和集成测试，执行专用 18 题验收卷；不要求也不得以旧 300 题作为本次完成条件。

## 不得做

- 不为固定题目、菜名或题号写特例。
- 不在旧 Top5 后过滤来伪装硬约束。
- 不把清爽、少油感觉说成低脂、低热量或医疗适用。
- 不把候选 Top30 的完整正文交给生成层。
- 不覆盖、暂存或提交用户已有的无关考试产物。

## 交付方式

每个独立可验证阶段创建中文提交并立即推送；第一个可审查提交后维护同一条草稿 PR。完成后更新 PR 的“改动内容”“验证结果”“风险与注意事项”，并用中文报告分支、提交、推送、PR、验收结果。等待用户明确确认后才可合并 `main`。
