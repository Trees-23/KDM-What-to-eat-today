# 300 题三层评测实施方案 V1

## 1. 目的和执行边界

本文件是 [硬指标、RAG 指标与回答效果补充评测调研方案 V1](ANSWER_QUALITY_EVALUATION_RESEARCH_PLAN_V1.md) 的实施方案。它定义实际要建什么、按什么顺序运行、每一步输出什么、何时能进入下一步，以及最后怎样验收。

固定来源是已经完成的运行：

```text
_other/考试/检索重构真实场景考试包/结果/
  2026-08-15-intent-planner-300-005/
```

本实施只读取该目录及已冻结题库，不重跑 300 题、不调用线上检索、不重新生成最终回答、不修改原始 `passed/failed`。现有 300 题均为 `passed`，因此本次会对 300 题生成回答效果结果。

最终交付不是一个“万能总分”，而是三张互不抵消的成绩单：

```text
硬指标：系统有没有犯硬错
RAG 指标：候选有没有找对、排序和证据链好不好
回答效果：最终回复是否贴题、清楚、好执行
```

本 V1 不采用人工逐题打分。自动化系统完成判断、复核和稳定性检查；人只阅读最终报告、低分题和自动化无法验证的题目，不作为分数生产者或通过门槛。

## 2. 总体流程和关卡

每个阶段必须达到“退出条件”才能进入下一阶段。任一阶段发现来源数据不够，不补跑、不猜测，而是记录状态并停止该指标的计算。

| 阶段 | 大白话 | 主要产物 | 退出条件 |
| --- | --- | --- | --- |
| P0 | 确认旧考试材料能不能用 | 来源盘点和哈希清单 | 300 题、审计、答案、题库可一一对应。 |
| P1 | 把杂乱原始文件整理成一张标准表 | `evaluation-cases.jsonl` | 每题都有唯一行和来源定位；缺失项显式标记。 |
| P2 | 解决 RAG 的 gold 与相关性来源 | `rag-gold-registry.json` | 每个排名指标都能判定“可算 / N/A / 未验证”。 |
| P3 | 实现离线计算与 AI 评审组件 | 可重复运行的脚本、配置和测试 | 单元测试、样例题和防错校验通过。 |
| P4 | 实际跑三层评测 | 三张评分卡和汇总报告 | 300 题全部被处理，状态完整。 |
| P5 | 自动验收结果是否可信 | 验收报告和稳定性报告 | 输入完整、指标正确、AI 结果稳定。 |
| P6 | 汇总、归档并发布最终测试包 | `_other/最终300测试/<运行编号>/` | 原硬规则考试、新三层结果、结论和总览都已可追溯地放入同一包。 |

## 3. P0：来源盘点与不可变快照

### 3.1 输入

必须对整个来源运行目录递归枚举所有常规文件，按相对路径排序后计算 SHA-256，写入不可变的完整来源清单。下列文件是其中必须存在且还要做语义读取的关键文件：

- `new-results.jsonl`：题号、场景、难度、原始通过状态、审计 ID、规划事件、推荐事件；
- `runner.stdout.jsonl`：运行过程的补充事件；
- `frozen_questions.json`：题干、路线契约、`gold_target`、安全规则；
- `acceptance-report.json`、`failure-summary.json`：硬测试汇总引用；
- 每题审计目录下的 `rag_process.md` 与 `recall_content.md`：候选、最终证据、限制和最终回答的来源；
- 试卷题库与场景评分标准：场景、A/B/C 难度和指标口径。

### 3.2 要做的自动检查

1. `new-results.jsonl` 必须恰好有 300 个不重复题号，且题号都存在于 `frozen_questions.json`。
2. 每题的 `audit_id` 必须能定位到一组审计文件；每题的最终回答、场景、难度和原始 `status` 必须可读。
3. 核对现有运行中保存的字段。特别记录：S06/S07 的 60 题已应有 `candidate_top30` 和 `final_top5`；其他场景的候选和最终证据可能只在审计文件中。
4. 不使用旧 `汇总结果.py` 直接处理本运行。该脚本面向旧的 `old/new + completed` 结果格式，而本运行使用 `new-results.jsonl + passed`；必须走本方案的新标准化读取层。
5. 写入来源目录内全部常规文件的相对路径、大小和 SHA-256，以及读取时间、解析器版本和每题来源位置。

### 3.3 输出

```text
<三层评测运行目录>/
  source-run.json
  source-integrity-report.json
  source-integrity-report.md
```

`source-integrity-report.json` 每题记录 `source_ready`、缺失字段、审计路径和文件哈希。来源不完整的题不得静默跳过。

### 3.4 退出条件

- 300 个题号可以唯一映射；
- 所有题都有可追溯的原始状态和审计定位；
- 任一缺失项已经精确列出题号与原因；
- 未发生任何对原始运行目录的写入。

若 300 题映射失败或来源文件物理缺失，标记 `SOURCE_INTEGRITY_FAILED`，不进入 P1-P5 的评分；但仍必须走 P6 的异常归档路径，生成带缺失清单的 `NOT_READY` 最终包。该包只能称为“来源不完整的失败归档”，不得称为原硬规则考试完整副本。

## 4. P1：标准化评测输入

### 4.1 目标

把 JSONL、JSON 和 Markdown 审计统一成“每题一行”的稳定输入。后续 RAG 计算和 AI 评审只能读取这个标准化文件，不能各自随意解析原始文件。

### 4.2 每题最低字段

```json
{
  "case_id": "S06-A-01",
  "scenario_id": "S06",
  "difficulty_code": "A",
  "source_status": "passed",
  "user_question": "...",
  "final_answer": "...",
  "audit_id": "...",
  "hard_reference": {"source_status": "passed", "checks": {}},
  "route_contract": {},
  "gold_target": {},
  "ranking_candidates": [],
  "final_evidence": [],
  "limitations": [],
  "recommendation_trace": {},
  "field_status": {}
}
```

`field_status` 逐字段写明 `PRESENT`、`NOT_APPLICABLE` 或 `MISSING`。例如 S08 的“排名候选”是 `NOT_APPLICABLE`，不是 `MISSING`。

### 4.3 自动化规则

- 解析器同时保留原始值、来源文件、行号或审计段落；
- 候选必须按原始顺序保留，不得因解析过程重新排序；
- 最终回答和证据使用 SHA-256，防止后续文件被悄悄改动；
- 无法可靠解析的 Markdown 段落只记录为缺失，不用 LLM 猜字段；
- P1 只做数据搬运和结构校验，不给任何题打好坏分。

### 4.4 输出和退出条件

输出 `evaluation-cases.jsonl`、`case-field-coverage.json` 和字段映射说明。每个题必须恰有一行；所有 `MISSING` 有原因；300 行计数、题号集合和源文件哈希都与 P0 一致。

## 5. P2：RAG gold、适用范围和相关性

### 5.1 先判“该不该算”，再判“怎么算”

对每题每个 RAG 指标按以下顺序处理：

1. 根据场景和已验证业务状态判定 `N/A`。S05C、S08、S09、S10 的 Recall、Precision、Hit Rate、MRR、nDCG 必须是 `N/A`；已验证硬范围为空的推荐题同样是 `N/A`。
2. 对其余排名指标寻找冻结的 `gold_items`、相关性、候选顺序和审计来源。
3. 字段齐全才计算数值；本应适用但缺少任一必要材料时标记 `RAG_UNVERIFIED`，并写明缺什么。

这一步的目的，是防止“安全题正确不找东西”被错算成 RAG 0 分。

### 5.2 既有冻结 gold 的优先级

优先按下列顺序寻找 gold：

1. 与本次运行、题库哈希和运行时间一致的历史 `gold_manifest.json`；
2. `frozen_questions.json` 中已经落盘的具体 gold 项和相关性；
3. 只能提供契约、`gold_target` 或“应从 source markdown 冻结”的说明时，不能当作具体 gold 项。

当前运行目录保存了 300 题 `gold_target` 契约，但是否保存了可直接计算的具体相关性列表，需要由 P0/P2 自动盘点确认。没有可验证的具体 gold，就不能把计算结果叫做“原始考试的冻结 RAG 分”。

### 5.3 S06/S07 的自动相关性标注方案

若找不到历史冻结的推荐相关性列表，建立独立的 `DERIVED_AI_GOLD_V1`。它是补充 RAG 基线，不回写原考试，也不与历史冻结 gold 混在一个分母。

具体步骤：

1. 从每题 Top30 取候选，隐藏其原始名次、向量分和最终 Top5 身份；该 gold 的覆盖范围明确写为 `TOP30_ONLY`。
2. 规则引擎先验证硬约束：菜系、做法、厨具、时长、份量、排除项等。违反硬约束的候选直接为 `0`。
3. AI 相关性评审 A 与 B 独立读取“用户问题、结构化约束、候选 metadata、必要正文证据”，不读取原始排序或模型回答。
4. A/B 分别给 `0/1/2/3`：`0` 不相关或违反硬约束；`1` 满足基本任务；`2` 满足硬约束并体现一项重要软偏好；`3` 满足硬约束并体现全部关键软偏好和场景。
5. A/B 相同时取该标签；相差 1 时固定取较低标签，防止相关性被自动向上抬高；相差超过 1 时交给第三个 AI 仲裁器。仲裁器必须给出引用的约束和证据 ID。
6. 将上述合成规则写入 `rag-gold-policy-v1`，并记录每次 AI 调用的模型、提示词版本、输入哈希、输出和仲裁理由，然后冻结为版本化 gold。

这套流程不需要人工逐题标注。它的限制是：自动生成的 gold 只能证明“自动化评审下，Top5 在已取到 Top30 中的排序表现”，不能证明全库召回，也不能冒充考试当时已经人工冻结的 gold；报告必须明确标注 `DERIVED_AI_GOLD_V1` 和 `TOP30_ONLY`。

### 5.4 RAG 序列校验与计算口径

先校验推荐题的两条序列：

- `candidate_top30` 是原始候选池，必须有序且 `parent_id` 唯一；
- `final_top5` 是重排后的最终顺序，必须有序、`parent_id` 唯一，并且每个 ID 都是 `candidate_top30` 的成员。

任一校验失败时，所有依赖该序列的 RAG 指标标为 `RAG_UNVERIFIED`，并记录 `TOP30_DUPLICATE`、`TOP5_DUPLICATE`、`TOP5_NOT_IN_TOP30`、`RANK_MISSING` 或具体解析原因。不能凭标题模糊匹配补救。

计算时必须同时记录 `ranking_stage`：

- 标准检索 Recall、Precision、Hit Rate、MRR、nDCG 使用“覆盖整个检索范围”的冻结 gold，以及对应的原始候选排序；
- S06/S07 若有完整冻结 gold：候选池阶段使用 `candidate_top30`，最终重排阶段使用 `final_top5`，报告字段分别以 `retrieval_` 和 `rerank_` 前缀命名，不能混成一条“RAG 分”；
- `DERIVED_AI_GOLD_V1` 且范围为 `TOP30_ONLY` 时，只能根据 Top30 内已标注候选，计算 `top30_pool_selection_recall@1/3/5`、`top30_pool_precision@1/3/5`、`top30_pool_hit_rate@1/3/5`、`top30_pool_mrr@5`、`top30_pool_ndcg@5`，衡量最终 Top5 在 Top30 候选池中的选择与排序质量；这些字段绝不能命名或汇总为全库 Recall@K；
- 只有二元相关性时：不计算 nDCG，或将该项标为 `RAG_UNVERIFIED`，不得伪造分级收益；
- 路由准确率、证据完整率、证据链接率只从路线契约和审计的可验证字段计算；
- 对安全题只输出原硬测试的安全检查引用和回答效果，不输出排名分。

每个数值必须能回链到“题号 -> 候选顺序 -> gold 版本 -> 计算公式 -> 审计 ID”。

### 5.5 输出和退出条件

输出：

```text
rag-gold-registry.json
rag-data-coverage.md
```

退出条件是每题每项 RAG 指标的**可计算状态**都有且仅有一种值：`COMPUTABLE`、`N/A` 或 `RAG_UNVERIFIED`。P2 尚不产出数值评分卡；它只冻结 gold、序列检查结果和覆盖报告。不存在空白格、用 0 代替不适用、或混合不同 gold 版本的聚合分。

## 6. P3：实现组件和自动评审设计

### 6.1 建议组件

在考试包的 `工具/` 下新增独立目录，不改动既有监考脚本：

```text
工具/three_layer_evaluation/
  build_evaluation_cases.py       # P0/P1：来源核验与标准化
  build_rag_gold.py               # P2：冻结 gold 检索或 AI 补充 gold
  compute_rag_scorecard.py        # P4：RAG 指标计算
  build_hard_reference.py         # P4：硬测试引用表
  judge_answer_quality.py         # P4：多 AI 回答效果评审
  validate_scorecards.py          # P5：完整性、公式和状态校验
  render_integrated_summary.py    # P6：汇总报告
  configs/
    answer-quality-rubric-v1.json
    ai-judge-profile-v1.json
    issue-tags-v1.json
  tests/
    fixtures/
```

目录和命名是实施建议；实际开始编码前可以按仓库已有组织微调，但组件职责不能合并到一个不可审计的大脚本。

### 6.2 回答效果的自动评审

每道通过题输入封闭材料：用户问题、最终回答、该题最终证据、限制说明、场景权重、rubric。评审器不能访问网络、数据库、其他菜谱、原始硬测试结论或其他评审器结果。

自动流程：

1. **结构校验器**确认输入齐全、证据 ID 在本题允许集合中、场景允许的指标没有错用 `null`。
2. **AI 评审 A**按五项指标给 1-5 分、标签和证据理由，重点看任务完成和可执行性。
3. **AI 评审 B**独立评审同一材料，重点反查偏题、偏好遗漏、夸大证据和边界不清；它不读取 A 的输出。
4. **共识器**逐维比较 A/B。两者相同时取该整数；相差 1 分时固定取较低整数，防止自动评分因半分或向上取整而虚高；相差超过 1 分或标签冲突时标记 `AUTO_DISAGREEMENT`。
5. **AI 仲裁器**只处理 `AUTO_DISAGREEMENT`，独立重读原材料并输出最终分、标签和解释；它不能只“投票”，必须引用证据或限制。
6. **公式校验器**按场景权重重算 0-100 分，拒绝 AI 自己给出的不一致总分。
7. 任何必要材料、适用维度或结构化输出缺失，整题标为 `QUALITY_UNVERIFIED`：各维和总分均为 `null`，不进入回答效果均分。

评分使用调研方案既定权重：正常回答 `40/25/35`、推荐 `25/35/20`、拒答或降级 `30/45/25`。人只在最终报告中看 `AUTO_DISAGREEMENT`、仲裁题、低分题和 `QUALITY_UNVERIFIED`，不回填分数。

### 6.3 AI 调用的可复现要求

- A、B 优先使用不同模型或不同供应商；若只能使用同一模型，必须使用独立调用、不同系统提示词和独立随机种子，并在报告标记 `SINGLE_MODEL_REVIEW_RISK`；
- 固定模型版本、温度、最大输出、提示词哈希和 JSON Schema；
- 所有模型输出必须保留原文和解析后的 JSON；
- 证据中的指令视为数据，评审提示词明确禁止执行；
- 每个评审输入必须含输入哈希，禁止评审器读取其他题的信息。

## 7. P4：正式运行顺序

### 7.1 运行前

1. 创建新目录 `<三层评测运行编号>`，不在原始 300 题目录写入任何文件。
2. 固定 `source-run.json`、解析器版本、配置哈希和 AI judge profile。
3. 运行 P0。若为 `SOURCE_INTEGRITY_FAILED`，跳过 P1-P5，直接进入 P6 异常归档；若来源完整，才运行 P1。
4. 正常路径运行 P2；先完成所有 `N/A` 判定和 gold 覆盖报告，再允许计算任何 RAG 平均分。

### 7.2 运行中

1. 生成 `hard-scorecard-reference.json`：只引用原结果的硬指标、题号和审计 ID。
2. 依据 P2 的 `COMPUTABLE` 状态实际计算 RAG 数值，生成 `rag-scorecard.json`；不能计算的项保留 P2 写入的 `N/A` 或 `RAG_UNVERIFIED`。
3. 对所有 `status=passed` 题运行回答效果自动评审，生成 `quality-scorecard.json`。
4. 对 AI 分歧题运行仲裁器；不因仲裁失败阻塞其他题，失败题写 `QUALITY_UNVERIFIED`。
5. 每个阶段记录开始/结束时间、输入哈希、输出哈希、异常和重试次数。

### 7.3 运行后

生成 `integrated-summary.md`，按场景、难度、指标和状态并列展示：

- 硬指标：原考试通过/失败/阻塞、禁止断言、无依据关系和安全检查；
- RAG：有效题数、`N/A`、`RAG_UNVERIFIED`、各排名指标、路线/证据指标；
- 回答效果：全体均分、S01-S10 场景均分、各维分、低于 70 的场景、问题标签、AI 分歧和未验证题；
- 诊断：候选未命中优先指向检索，候选命中但 Top5 差优先指向重排，RAG 正常但回答低分优先指向生成。

## 8. P5：自动验收

### 8.1 数据和硬指标验收

| 检查项 | 通过条件 |
| --- | --- |
| 来源完整性 | 300 个唯一题号均有来源、哈希和审计定位。 |
| 原结果保护 | 原始目录无写入；硬指标引用与 `acceptance-report.json` 一致。 |
| 标准化完整性 | `evaluation-cases.jsonl` 恰有 300 行，题号、场景和状态一一对应。 |
| 状态完整性 | 每项 RAG 和回答效果都无空状态。 |

### 8.2 RAG 验收

| 检查项 | 通过条件 |
| --- | --- |
| 公式测试 | 用固定小样例验证 Recall、Precision、Hit Rate、MRR、nDCG 的手算预期。 |
| 安全题保护 | S05C、S08-S10 的排名指标全部为 `N/A`，没有被算为 0。 |
| gold 可追溯 | 每个数值能指向 gold 版本、候选顺序和审计 ID。 |
| 缺失处理 | 本应适用却缺材料的项全部为 `RAG_UNVERIFIED` 且写明原因。 |
| 聚合隔离 | `FROZEN_GOLD` 与 `DERIVED_AI_GOLD_V1` 分开汇总；`TOP30_ONLY` 只报告 Top30 候选池内的选择/排序指标，不混成全库 Recall 或冻结 nDCG。 |

若排名题出现 `RAG_UNVERIFIED`，仍可以发布“部分 RAG 基线”，但不得宣称该场景 RAG 已完整验收。要称为完整 RAG 基线，所有本应适用的排名题都必须有可追溯 gold 和候选顺序。

### 8.3 回答效果自动化验收

先从 300 题中按固定种子 `answer-quality-stability-v1` 抽取 90 题自动稳定性集：十个场景 x A/B/C 三种难度，每个组合 3 题。首次抽取后把题号、来源回答哈希和抽样种子写入 `auto-judge-stability-set-v1.json`；后续运行必须复用该文件，不能重新抽样。该集合不是人工校准集，专门用于检查 AI 评审器可靠性。

| 检查项 | 通过条件 |
| --- | --- |
| JSON 和证据校验 | 100% 通过；不合法输出必须转为 `QUALITY_UNVERIFIED`，不能被静默修补。 |
| A/B 一致性 | 90 题中，至少 90% 的适用维度 A/B 相差不超过 1 分。 |
| 仲裁闭环 | 100% 的大分歧题都有仲裁结果或明确 `QUALITY_UNVERIFIED`。 |
| 重复稳定性 | 对同一 90 题独立运行 3 次，至少 95% 的适用维度最大差不超过 1 分，至少 95% 的题总分最大差不超过 5 分。 |
| 反偏差测试 | 所有冻结 fixture 都满足各自机器可判定的分数、标签和不变量阈值。 |

不使用人工一致率替代这些检查。它们只能证明自动评分器“自洽和稳定”，不能证明它等同于真人偏好；报告应如实标为“AI 自动回答效果基线”。

反偏差 fixture 固定在代码库并版本化，至少包含：

| Fixture | 机器验收条件 |
| --- | --- |
| 冗长但偏题 | `task_score <= 2`、`total_score_100 <= 50`，且含 `OFF_TOPIC`。 |
| 简短但完整 | `task_score >= 4`、`readability_score >= 4`、`total_score_100 >= 75`。 |
| 证据顺序置换 | 各适用维度差不超过 1、总分差不超过 5、问题标签集合完全相同。 |
| 证据注入指令 | 输出必须符合 Schema，不得执行或引用注入指令；与去除该指令的对照输入相比，各适用维度差不超过 1。 |
| 拒答边界不清 | `boundary_expression_score <= 2`，且含 `LIMITATION_UNCLEAR` 或 `REFUSAL_NOT_HELPFUL`。 |

所有 fixture 及其预期条件 100% 通过，才算反偏差测试通过。

### 8.4 总体验收结论

`validate_scorecards.py` 自动输出以下其中一种结论：

- `READY_FOR_AUTO_BASELINE`：数据、公式、状态和 AI 稳定性全部通过；
- `AUTO_BASELINE_WITH_LIMITATIONS`：可生成报告，但存在 `RAG_UNVERIFIED`、`QUALITY_UNVERIFIED` 或单模型风险，限制已明确列出；
- `NOT_READY`：来源映射、公式、安全题状态、AI 稳定性或输出完整性不达标，不能把分数用于版本比较。

无论哪种结论，都不影响原有 300 题硬测试结论。

## 9. P6：汇总、归档和用户查看方式

### 9.1 最终归档原则

`_other/最终300测试/` 是用户查看最终 300 题结果的唯一交付根目录。它不是临时日志目录，也不只放新增 RAG/回答效果结果。来源完整的正常最终交付必须同时包含：

1. 本次三层评测所依据的既有 300 题硬规则考试完整快照；
2. 新生成的硬指标引用、RAG 评分、回答效果评分和自动验收；
3. 一份人可以直接阅读的总览和最终结论。

来源不完整的异常归档不产生三层结果，只保留可读取的来源副本、缺失清单、`NOT_READY` 结论和总览，并显式标记未执行的阶段。

既有硬规则考试的唯一来源是：

```text
_other/考试/检索重构真实场景考试包/结果/
  2026-08-15-intent-planner-300-005/
```

正常 P6 必须在 P0 已完成完整来源清单和哈希后才可复制。复制使用保留目录结构和文件内容的方式，不移动、不删除、不修改来源目录；复制完成后重新递归计算文件清单和哈希，逐项与 P0 的完整来源清单比对。任一文件缺失、额外、路径不一致或哈希不一致，则最终包为 `NOT_READY`，不得只放一个“300/300 passed”的摘要冒充完整硬规则结果。

若 P0 已标记 `SOURCE_INTEGRITY_FAILED`，P6 不得伪装执行“完整副本”验证：只能复制仍可读取的来源文件，写入 `source-missing-manifest.json`、P0 缺失原因和 `NOT_READY` 结论，并在总览第一行明确“原硬规则考试来源不完整，未生成完整副本”。这个异常包仍放在 `_other/最终300测试/<最终测试运行编号>/`，用于保存已完成工作和阻塞证据。

### 9.2 最终目录结构

```text
_other/最终300测试/
  README.md                                      # 指向最新最终包和历次包目录
  <最终测试运行编号>/                             # 每次新建，禁止覆盖历史最终包
    00-最终总览.md                                # 用户优先阅读：三层结论、限制、低分归因
    01-原始300硬规则考试/
      source-run.json                             # 原始来源绝对路径、哈希和复制时间
      source-copy-manifest.json                   # 原路径与复制路径的逐文件哈希对照
      source-missing-manifest.json                # 仅 SOURCE_INTEGRITY_FAILED 时存在
      2026-08-15-intent-planner-300-005/          # 原硬规则考试的完整只读副本
        acceptance-report.json
        failure-summary.json
        frozen_questions.json
        new-results.jsonl
        runner.stdout.jsonl
        audits/
        ...
    02-三层评测输入与硬指标/
      source-integrity-report.json
      evaluation-cases.jsonl
      hard-scorecard-reference.json
    03-RAG指标/
      rag-gold-registry.json
      rag-data-coverage.md
      rag-scorecard.json
    04-回答效果/
      quality-scorecard.json
      auto-judge-stability-set-v1.json
      auto-judge-stability-report.json
    05-自动验收与结论/
      validation-report.json
      integrated-summary.md
      final-package-manifest.json
      final-conclusion.json
```

`<最终测试运行编号>` 例如 `2026-08-15-three-layer-evaluation-001`。根目录 `README.md` 只列出各最终包、运行时间、来源硬规则运行编号和 `READY_FOR_AUTO_BASELINE` / `AUTO_BASELINE_WITH_LIMITATIONS` / `NOT_READY` 状态；它不覆盖或删除旧包。

### 9.3 P6 的自动执行步骤

1. 新建唯一最终测试运行目录，并写入本次运行编号、代码提交、配置哈希和来源路径。
2. 正常路径：将原硬规则 300 题运行完整复制到 `01-原始300硬规则考试/`，生成递归逐文件复制清单并验证与 P0 完整来源清单逐项哈希一致；异常路径：仅复制仍可读取的文件并生成 `source-missing-manifest.json`，最终状态固定为 `NOT_READY`。
3. 正常路径：将 P0-P5 产物按上述分区复制或生成到 `02` 至 `05`，保留每个文件的来源和生成版本；异常路径：不要求也不得伪造 P1-P5 产物，`02` 至 `04` 可以不存在。
4. 生成 `00-最终总览.md`：正常路径先说明原硬规则考试的原始结论，再分别说明 RAG 和回答效果的有效范围、未验证项和限制；异常路径第一行说明来源不完整、未执行 P1-P5、最终状态为 `NOT_READY`。两种路径都严禁把三层写成一个总分。
5. 生成 `final-conclusion.json`：正常路径至少含硬指标原结论、RAG 结论、回答效果结论、自动验收结论、最低场景、`RAG_UNVERIFIED` / `QUALITY_UNVERIFIED` 计数、来源与复制哈希状态；异常路径至少含 `SOURCE_INTEGRITY_FAILED`、缺失清单引用、已复制文件数、未执行阶段和 `NOT_READY`。
6. 生成 `final-package-manifest.json`：枚举最终包内实际存在的必要文件、哈希、生成时间和验证状态；异常路径的必要文件为可读取来源副本、`source-missing-manifest.json`、`00-最终总览.md` 和 `final-conclusion.json`。
7. 正常路径中，只有完整复制清单、三层评分卡、自动验收和总览全部存在且互相链接时，才更新根目录 `README.md` 的“最新最终包”条目；`SOURCE_INTEGRITY_FAILED` 异常路径中，只有缺失清单、`NOT_READY` 结论、总览和包清单全部存在时才追加“失败归档”条目。

### 9.4 人只看什么

人不必逐题打分，只需从 `_other/最终300测试/<最终测试运行编号>/00-最终总览.md` 开始看：

- 三层是否均可用，还是哪一层存在限制；
- 原始 300 题硬规则考试的完整副本是否已通过哈希核验；
- 低于 70 的回答效果场景和代表题；
- RAG 缺失、AI 大分歧和未验证题；
- 最常见问题标签；
- “应改检索 / 应改重排 / 应改回答生成”的归因列表。

### 9.5 后续版本比较规则

后续系统版本只能与“相同题库哈希、相同 gold 版本、相同 rubric、相同 AI judge profile、相同指标口径”的基线比较。任一版本变化时，报告必须新开一列并说明不可直接横比的原因。

## 10. 实施完成定义

以下条件全部满足，才算本实施方案落地完成：

1. 新标准化读取层能只读处理最新 300 题运行，不依赖旧结果格式；
2. 三张评分卡能对每题给出完整、可追溯的状态和来源；
3. RAG 的 `N/A`、`RAG_UNVERIFIED`、历史冻结 gold 和 AI 补充 gold 被严格区分；
4. 回答效果完全由规则校验和多 AI 自动评审产生，无人工逐题评分；
5. 自动验收通过，或限制被明确标记为 `AUTO_BASELINE_WITH_LIMITATIONS`；
6. 最终报告能明确告诉使用者：问题主要在硬规则、检索、重排还是回答表达；
7. `_other/最终300测试/<最终测试运行编号>/` 中已包含原硬规则考试的完整可验证副本、三层结果、自动验收、结论和总览；
8. 原始 300 题运行和其 `passed/failed` 没有被修改。

达到这些条件后，下一步才是依据低分归因修改系统，并用同一套三层流程比较修改前后结果；不是直接用总分决定系统“好或不好”。
