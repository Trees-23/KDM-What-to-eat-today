# 新路径统一意图规划调研方案

## 背景与结论

现有 `new` 检索入口并非“先理解意图，再选择受控检索计划”，而是若干
规则分支按固定顺序抢占请求：营养规则、目标图规则、通用偏好短词表、实体
直达，最后才可能回退旧 Router。该入口位于 `main.py` 的
`AdvancedGraphRAGSystem.retrieve_for_generation()`。

这会把没有明确菜名的语义推荐请求送入实体解析。例如“下班很晚，想找准备
步骤少的家常菜”不匹配当前偏好词表，实体解析又找不到同名菜谱，最终错误返回
`ENTITY_NOT_FOUND`。运行态 60 题普查表明：

| 场景 | 有正文证据的受限向量 | `ENTITY_NOT_FOUND` | 其他 |
| --- | ---: | ---: | ---: |
| S06（通用推荐） | 2 / 30 | 28 / 30 | 0 |
| S07（川味软偏好） | 6 / 30 | 14 / 30 | 10 / 30 严格营养误触发 |

原检索重构方案的目标却是：

```text
用户问题
  -> QueryPlan（受 schema 约束并校验）
  -> 实体定位 / 属性过滤 / 受限 child-chunk 向量召回 / 目标化图查询
  -> PDS 正文与图事实
  -> LLM 基于证据生成回答
```

`QueryPlanValidator` 已接受 `source="llm_candidate"`，但当前没有新路径的
LLM 计划器实际生成候选计划。此次调研的目标是确定如何补齐这层，而不是直接
实现或用更多关键词掩盖问题。

## 调研目标

1. 设计并验证一个前置的、受约束的 LLM 意图规划层。
2. 保留现有安全边界：禁止任意 Cypher、禁止未受限向量检索、图关系必须来自
   已验证图事实、向量命中必须 PDS 回补。
3. 明确 `ENTITY_NOT_FOUND` 只能用于“明确实体查询且未定位”，不能用于泛化
   推荐、偏好或场景请求。
4. 将营养安全判断从“字符串抢占路由”改为“已识别意图后的硬约束校验”，避免
   测试/系统提示中的“不得断言低脂”污染用户意图。
5. 为后续修复形成可实现、可审计、可回归验证的技术规格和风险清单。

## 已证实的现状

### 入口与分流

- `retrieve_for_generation()` 先调用 `_try_nutrition_recommendation()`，再尝试
  `_try_targeted_graph()`、`_preference_plan()`、`_try_entity_direct()`。
- `_is_preference_query()` 只识别 `夏天吃`、`天气热`、`清淡`、`清爽`、`不腻`。
- `_try_entity_direct()` 对任何没有前序命中的请求尝试菜谱/技巧实体解析；无候选
  且 `allow_generalized_advice=false` 时直接返回 `ENTITY_NOT_FOUND`。
- 当前 `new` 入口没有调用 `IntelligentQueryRouter.analyze_query()`，因此没有 LLM
  意图理解。旧 Router 虽有 LLM 分析，但不应作为新路径的正常依赖。

### 已有可复用能力

- `QueryPlan` 和 `QueryPlanValidator` 已白名单化 intent、template、实体类型、
  参数及候选上限，并拒绝 `cypher`、`query`、`where` 等越权参数。
- Validator 已允许 `source` 为 `rule` 或 `llm_candidate`。
- `EntityResolver` 能按精确名称、治理别名、全文索引定位稳定 `nodeId`；其职责应
  是解析已确定需要实体的计划，而不是判断所有请求是否为实体问题。
- `TargetedGraphRetriever` 只执行固定模板；`RestrictedVectorRetriever` 绑定 PDS/
  Milvus 联合 artifact 并回补正文。
- `nutrition_policy.py` 已定义“严格营养数据缺失时不可声称低脂”等回答边界。

### 已发现的旁路风险

- `S05-A-02` 证明生成流可在无内容时仍被记录为成功并发送 `[DONE]`。这与意图
  规划是独立问题，但任何后续验证必须同时防止空回答被当作通过。
- 当前 S07-C 题干的安全说明含“低脂”等字样，会被营养规则误判为严格营养请求。
  正式产品输入应将用户消息与系统/评测约束分离；规划器只读取用户语义输入。

## 目标架构候选

建议优先评估以下两阶段模型，而不是让 LLM 直接决定检索器或生成查询语句：

```text
原始用户消息
  -> 输入边界处理
       分离系统/评测约束；保留原始消息与规范化消息
  -> 硬安全预检
       仅处理医疗、明确营养阈值、注入/越权输入等不可放开的场景
  -> LLM Intent Planner
       输出受 schema 约束的候选意图、槽位、置信度、是否必须实体定位
  -> Plan Compiler + QueryPlanValidator
       LLM 不能提供 nodeId、Cypher、标签、关系、过滤表达式
       稳定 ID 只能由 EntityResolver/PDS/固定图查询产生
  -> 执行器
       固定图模板 / 受限向量 / 实体全文 / 明确拒答
  -> 证据校验
       图事实、PDS 正文、营养限制分栏
  -> 生成与空流保护
```

### 初始意图枚举建议

调研时必须验证枚举是否足够，不能假定以下列表就是最终实现：

| 候选意图 | 示例 | 执行约束 |
| --- | --- | --- |
| `ENTITY_LOOKUP` | “有云岚02号幻味砂锅吗” | 解析明确实体；无候选才 `ENTITY_NOT_FOUND` |
| `RECIPE_DETAIL` | “宫保鸡丁怎么做” | 解析 Recipe 后 PDS 全文/步骤 |
| `RECIPE_STEP` | “宫保鸡丁第 2 步” | 固定步骤图模板 + PDS 锚点回补 |
| `TECHNIQUE_SECTION` | “焯水的关键要点” | 固定技巧模板 + PDS 章节 |
| `INGREDIENT_RECIPES` | “鸡肉能做什么” | 固定食材到菜谱图模板 + PDS |
| `INGREDIENT_VEGETABLE_PAIRS` | “猪肉搭配哪些蔬菜” | 固定多跳图模板 + PDS；无路径为 `graph_not_found` |
| `PREFERENCE_RECOMMEND` | “下班晚、步骤少”“少油感觉的川味晚餐” | 受限向量；可由已验证菜系范围缩小 scope |
| `NUTRITION_CONSTRAINED` | “每份脂肪不超过 5g 的川菜” | 无治理来源时终止为证据不足，不推荐伪低脂候选 |
| `OUT_OF_SCOPE_OR_UNCLEAR` | 不足以理解的输入 | 澄清或安全受限回应，不把它变成实体不存在 |

`ENTITY_NOT_FOUND` 应是 `ENTITY_LOOKUP` 或需实体的图/详情计划执行后的状态，不应是
顶层意图，更不能成为偏好推荐的默认出口。

## 必须回答的调研问题

### A. 意图规划输入和输出

1. LLM 应只输出什么最小 JSON？是否仅包含 `intent`、`slots`、`confidence`、
   `requires_entity_resolution`、`response_policy`？
2. 哪些字段绝不能由 LLM 输出？至少应包括 nodeId、parent_id、Cypher、标签、关系
   类型、任意过滤条件、向量 collection 和候选排序分数。
3. 低置信度、非法 JSON、未知 intent、冲突槽位时应如何 fail closed？应返回澄清、
   保守规则计划还是指定的不可证明回应？
4. 是否需要一份独立 JSON Schema/Pydantic 模型，而不是直接复用执行 `QueryPlan`？
   推荐答案是“需要”：LLM 输出 `IntentCandidate`，本地编译后才得到 `QueryPlan`。

### B. 规则与 LLM 的职责边界

1. 哪些规则可放在 LLM 前作为硬门：医疗/严格数值营养、越权指令、空输入、长度限制？
2. 哪些规则应移到 LLM 后：`少油`、`川味`、`快手`、`步骤少`、`不腻`、菜系同义词？
3. 现有关键词应如何保留为“偏好抽取/会话记忆”，而不是抢占顶层路由？
4. 测试契约或系统提示应如何从用户消息分离，避免“不要断言低脂”被误识别成用户要求低脂？

### C. 实体解析与计划编译

1. 每个意图需要哪些实体类型、是否必须解析、可否多实体并行、歧义如何呈现？
2. 对 `PREFERENCE_RECOMMEND`，如何从 LLM 槽位构造受限 scope？
   - 无经验证结构化范围：是否允许 `all_child_chunks`？
   - `川味` 是否规范化为 `川菜`，且通过 PDS metadata/固定图模板得到 parent_id？
3. 对有实体的计划，如果实体无法定位，何时是 `ENTITY_NOT_FOUND`，何时应澄清？
4. 如何保证 LLM 不可通过槽位让执行器越过 QueryPlan 白名单？

### D. 营养与回答安全

1. “少油感觉”“清爽”“不厚重”应归为软口味偏好；“低脂”“每份脂肪不超过 X”应归为
   严格营养约束。边界如何版本化？
2. 是否应先识别意图，再检查严格营养约束，而不是对全文做关键词抢占？
3. 对软偏好候选的生成提示如何强制“偏好匹配”措辞，避免生成严格低脂、低盐、低热量断言？

### E. 运行可靠性与审计

1. Planner 的原始 JSON、校验结果、规范化意图、实体解析、编译 QueryPlan、执行路径、
   PDS 回补、最终限制应分别写入哪些审计字段？
2. LLM planner 超时/空响应/非 JSON 时的重试上限、降级路径和可见回应是什么？
3. 生成流零 chunk 时，系统应如何记录失败并执行非流式 fallback 或返回显式错误？
4. 如何避免将 planner 调用和生成调用混为同一个审计阶段或相互污染会话缓存？

## 调研方法与交付物

### 1. 静态代码与提交追踪

- 追踪 `retrieve_for_generation`、`IntelligentQueryRouter`、`QueryPlanValidator`、
  `EntityResolver`、`nutrition_policy`、生成流处理器。
- 解释为何 `source="llm_candidate"` 已存在却未被入口使用。
- 对照 `_other/RETRIEVAL_REFACTOR_IMPLEMENTATION_PLAN_V1.md` 的目标链路与实际调用链。

### 2. 不改代码的原型验证

- 用冻结的 S01-S10 正式题库和其释义题进行 planner-only 实验：仅输出候选意图与槽位，
  不调用 Neo4j/Milvus 写操作、不调用生成回答。
- 为每题记录：原始题干、候选意图、置信度、抽取槽位、应执行模板、是否需实体、是否会触发
  营养硬门、是否会错误产出 `ENTITY_NOT_FOUND`。
- 至少对 S06/S07 做同义改写矩阵：快手/步骤少/省事、川菜/川味、少油感觉/不油腻/
  不厚重/轻口味、严格低脂/软偏好。

### 3. 对比评估

对每个输入比较当前规则路径与候选目标路径：

| 指标 | 目标 |
| --- | --- |
| 意图分类准确率 | 按冻结人工标签计算，按 S01-S10 分场景报告 |
| `ENTITY_NOT_FOUND` 误报 | 偏好/场景推荐题为 0 |
| 计划合法率 | LLM 输出经编译与 validator 后为 100%；非法输出不执行 |
| 图关系安全 | 关系题不执行任意 Cypher，且图事实必须 verified 才可断言 |
| PDS 证据链接 | 所有用于回答的向量候选均可回补 PDS |
| 营养误报 | 严格营养断言与医疗断言为 0 |
| 空流假成功 | `chunk_count=0` 或 `answer_chars=0` 不得被标记为成功 |
| 释义鲁棒性 | 同一意图改写不应仅因关键词替换而落入实体未找到 |

### 4. 最终调研交付

调研报告必须给出：

1. 建议的 `IntentCandidate` JSON Schema 与允许枚举。
2. Planner prompt 的核心约束与 JSON 示例。
3. 意图到“本地编译逻辑/白名单 QueryPlan/证据要求/错误状态”的映射表。
4. LLM 失败或低置信度的保守行为定义。
5. 分阶段实施清单、文件影响范围、回归测试清单、上线/回退开关建议。
6. 至少三个可选方案的取舍，包括“不使用 LLM、只扩词表”为何不足。
7. 未解决的产品/数据治理问题，尤其是营养字段与用户偏好持久化边界。

## 非目标与硬约束

- 本调研不修改应用代码、题库、`.env`、Compose 主配置、Neo4j、Milvus、PDS 或既有考试结果。
- 不启用旧路径作为新路径正常流程；旧 Router 只可作为明确配置的故障兼容回退。
- 不允许 LLM 输出或执行任意 Cypher、SQL、Milvus filter、collection 名、nodeId、parent_id。
- 不因 planner 失败而自动放开全库旧向量检索或伪造关系/营养事实。
- 不通过为每道题配置专用关键词或题干 allowlist 来伪造泛化能力。

## 建议的后续实施门槛

只有在调研报告明确了 schema、失败策略和评估集后，才开始编码。实施前至少应冻结：

1. 用户消息与测试/系统约束的输入边界。
2. `IntentCandidate` 枚举、JSON schema 与 validator 规则。
3. 每种意图的执行边界、证据要求与不可证明状态。
4. S05 空流的独立修复和测试用例。
5. S06/S07 的完整释义回归集，不允许只测试“少油川菜”“清爽川菜”等精确短语。
