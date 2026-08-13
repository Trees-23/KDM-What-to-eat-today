# 新路径统一意图规划改造实施方案

## 1. 目的与结论

本方案将 `new` 检索路径改造成“先理解需求，再执行受控检索”的统一流程。

现有问题不是关键词数量不够，而是入口以一组字面规则抢占请求：营养规则、关系
规则、少量偏好词、实体直达依次执行。没有命中这些规则的泛化推荐会被当成“查某个
菜名”，继而错误返回 `ENTITY_NOT_FOUND`。例如“下班很晚，想找准备步骤少的家常菜”
本质是推荐需求，不是实体不存在。

目标架构是：每个进入 `new` 路径的可信用户问题都先经过 LLM 语义理解。LLM 只能产出
低权限的“意图候选单”，本地程序负责把它编译成唯一允许执行的查询计划；实际查询仍
只能使用固定图模板、受限向量检索和 PDS 正文库。

```text
用户真实问题
  -> 输入边界处理
  -> LLM 意图理解（候选单）
  -> 本地校验与计划编译
  -> 实体解析 / 图关系查询 / 受限向量查询 / 营养硬筛选
  -> PDS 正文回补
  -> 证据校验与生成
  -> SSE 非空校验
```

本方案不把“川味”“少油感觉”等个别说法做成专用分支。它们只是 LLM 能理解的一类
自然表达；同一套流程要覆盖场景、时间、工具、食材、菜系、口味、人数、难度、做法
和步骤等自然表达；实际执行仅限已声明支持的槽位组合。

## 2. 当前可复用能力与改造边界

### 2.1 现有三类数据职责

| 数据层 | 它负责什么 | 它不负责什么 |
| --- | --- | --- |
| 图数据库 | 证明结构化关系：菜谱使用哪些食材、菜谱包含哪些步骤、菜系归属、技巧章节归属 | 语义相似推荐、完整正文展示、严格营养推断 |
| 向量数据库（Milvus V2） | 在允许范围内寻找和用户场景、口味、偏好接近的菜谱片段 | 证明图关系、证明严格营养事实、返回最终完整正文 |
| PDS 正文库（ParentDocumentStore） | 根据稳定菜谱 ID 或锚点返回完整菜谱、技巧正文、步骤上下文，作为展示依据 | 猜测用户说的是哪个实体、全库语义搜索、证明图关系 |

“PDS 正文回补”就是：向量检索或图查询先得到某个菜谱 ID、步骤 ID 或片段 ID 后，
再从完整菜谱正文库取回可复核的原文。向量命中的一小段文本不能独自充当最终依据。

### 2.2 已有安全基础

- `QueryPlanValidator` 已限制可用意图、模板、参数和上限，且拒绝 `cypher`、`query`、
  `where`、`filter` 等越权字段。
- `TargetedGraphRetriever` 已使用固定、参数化的图模板。
- `RestrictedVectorRetriever` 已绑定 PDS/Milvus 构建版本，向量命中会验证关联并回补 PDS。
- `EntityResolver` 已能按精确名称、别名和全文索引定位稳定实体 ID。
- 生成层已能区分已验证图事实、正文证据和限制。

现有 `QueryPlanValidator` 接受 `source="llm_candidate"`，但它不是可直接给 LLM 使用的
执行接口。LLM 不能输出 `QueryPlan`，因为执行计划里有实体 ID、检索范围等只能由本地
可信数据生成的信息。

### 2.3 不做的事

- 不开启旧 Router 作为 new 路径的正常流程。
- 不允许 LLM 生成或执行 Cypher、SQL、Milvus filter、collection 名、nodeId、parent_id、
  图标签、关系类型或排序表达式。
- 不退回旧的未受限向量检索。
- 不用“为每道题增加关键词或题号白名单”的办法伪造泛化能力。
- 没有受治理营养数据时，不声称低脂、低热量、低盐、适合特定疾病或医疗饮食。

## 3. 目标流程与职责分工

### 3.1 输入边界

调用入口必须把以下内容分开传递和审计：

```text
user_message              用户真实提问；唯一进入意图理解和营养判断的文本
system_instructions       系统行为规则；不作为用户需求解析
evaluation_constraints    考试或评测的回答限制；不作为用户需求解析
conversation_context      经授权且结构化的会话偏好；不可伪装为用户本轮要求
```

例如以下内容必须拆分：

```text
user_message: 想喝一碗清淡些的川味汤。
evaluation_constraints: 没有受治理营养来源时不要断言低脂。
```

意图理解应得到“川味汤、清淡偏好”，而不是把“不要断言低脂”误当作用户在要求低脂。
安全约束只在最终回答策略中生效。

### 3.2 LLM 的职责

LLM 只负责把自然语言归类为有限意图，并抽取用户表达的实体提及和偏好槽位。它不决定
数据库访问方式，更没有任何数据访问权限。

可将它理解为填写一张需求单：

```text
用户：下班很晚，想找准备步骤少的家常菜。

需求单：
- 主要意图：按条件推荐
- 场景：晚餐
- 偏好：家常、准备少、步骤少
- 明确实体：无
- 是否要求严格营养：否
```

### 3.3 本地程序的职责

本地程序必须完成以下四件事：

1. 检查 LLM 候选单是否为合法、有限、低权限的数据结构。
2. 判断哪些实体必须解析，并通过本地 `EntityResolver` 获得真实 ID。
3. 根据固定映射选择图查询、向量检索、PDS 正文读取或严格营养拒答。
4. 将实际使用的证据、检索范围、限制和失败状态写入审计。

LLM 负责“听懂人话”，本地程序负责“决定允许做什么查询”。两者之间必须保持两份
不同的 JSON：LLM 只填写不带执行权的**需求单**，本地编译器才生成可交给检索器的
**执行单（`QueryPlan`）**。任何 LLM 输出均不得直接作为检索器输入。

## 4. 意图候选单契约

### 4.1 内部 JSON 形状

内部字段使用稳定代码，避免 LLM 输出任意中文同义词导致无法一一对应。面向用户展示时
可在程序中将代码翻译成中文。

```json
{
  "intent": "RECIPE_STEP",
  "confidence": 0.99,
  "entity_mentions": [
    {
      "text": "宫保鸡丁"
    }
  ],
  "slots": {
    "step_number": 1,
    "cuisines": [],
    "ingredients": [],
    "preferences": [],
    "meal_context": [],
    "tools": [],
    "methods": [],
    "servings": null,
    "time_budget_minutes": null,
    "nutrition_constraint": null
  }
}
```

这份 JSON 是“用户要什么”的需求单，不是“数据库怎么查”的执行单。`entity_mentions`
只能提供用户原话；本地程序根据 `intent` 的固定映射决定允许解析的实体类型。例如
`RECIPE_STEP` 才允许解析 `Recipe`，不能由 LLM 指定 `expected_type`。

第一版仅允许如下 `intent`：

| 内部意图代码 | 用户实际在问什么 |
| --- | --- |
| `ENTITY_LOOKUP` | 某道菜、食材或技巧是否存在，或需要列出候选 |
| `RECIPE_DETAIL` | 某道菜怎么做、食材和完整做法 |
| `RECIPE_STEP` | 某道菜指定第几步怎么做 |
| `TECHNIQUE_SECTION` | 某项烹饪技巧的章节、要点或适用场景 |
| `INGREDIENT_RECIPES` | 某食材能做哪些菜 |
| `INGREDIENT_VEGETABLE_PAIRS` | 某食材适合搭配哪些蔬菜 |
| `PREFERENCE_RECOMMEND` | 按场景、口味、工具、时间、食材、菜系等推荐 |
| `STRICT_NUTRITION` | 明确脂肪/热量/营养阈值或医疗饮食请求 |
| `CLARIFY_OR_OUT_OF_SCOPE` | 信息不足、歧义过大或超出知识库可支持范围 |

### 4.2 槽位允许范围

槽位值必须使用受控枚举，而不是让 LLM 发明检索词。第一版可按实际数据能力逐步扩展：

| 槽位 | 例子 | 用途 |
| --- | --- | --- |
| `cuisines` | `SICHUAN_STYLE` | 表示用户偏好川味；由本地映射到已验证菜系范围 |
| `ingredients` | 仅保留用户原文提及 | 交由实体解析获得真实食材 ID |
| `preferences` | `LIGHT_FEEL`、`LOW_OIL_FEEL`、`FEW_STEPS`、`HOMESTYLE`、`MILD_FLAVOR` | 用于受控向量检索和回答措辞，不是严格事实 |
| `meal_context` | `BREAKFAST`、`LUNCH`、`DINNER` | 推荐排序语义 |
| `tools` | `MICROWAVE`、`RICE_COOKER` | 推荐排序语义；不得假定菜谱一定支持，必须由正文核验 |
| `methods` | `STEAM`、`BOIL`、`FRY`、`STEW` | 可作为偏好或已验证过滤条件 |
| `step_number` | 1 至 1000 的整数 | 仅用于 `RECIPE_STEP` |
| `time_budget_minutes` | 合理正整数 | 推荐偏好；必须由正文时间字段核验后才能作为依据 |
| `nutrition_constraint` | 结构化阈值或医疗类别 | 仅在 `STRICT_NUTRITION` 使用 |

`LOW_OIL_FEEL` 表示“少油感觉/不油腻偏好”，绝不等于“低脂”。`SICHUAN_STYLE` 表示
用户说“川味/川菜风格”，本地程序才可将其映射到经过数据核验的“川菜”范围。

第一版还必须冻结以下输入上限，超出即拒绝候选单并返回 `CLARIFY_OR_OUT_OF_SCOPE`：

```text
entity_mentions 最多 8 项；每项 text 最长 80 个字符
每个列表槽位最多 5 项；重复值由本地去重
confidence 必须为 0 至 1 的有限数值
未知枚举、空字符串、未声明的槽位组合一律不原样透传给检索器
```

产品能力以“已声明支持的组合”为准，不承诺任意槽位的任意组合都能执行。无法映射为
硬范围的槽位最多保留为软偏好；无法作为软偏好解释的槽位必须澄清，不能临时拼成检索词。

### 4.3 LLM 明确禁止输出的字段

以下字段一律不出现在候选单中：

```text
nodeId、recipe_id、ingredient_id、step_id、parent_id、chunk_id、build_id
Cypher、SQL、Milvus filter、collection、数据库名、图标签、关系类型
template_id、vector_scope、排序字段、相似度阈值、营养结论、证据等级
```

理由是这些字段要么是执行权，要么是运行态真实数据，要么会导致模型伪造关系或越过
检索范围。它们只能由本地编译器、实体解析器、固定模板和治理数据产生。

### 4.4 候选单失败处理

| 情况 | 本地行为 | 禁止行为 |
| --- | --- | --- |
| 非法 JSON、未知字段、未知意图 | 记录 `PLANNER_INVALID_OUTPUT`，请求澄清或返回保守不可理解回应 | 当作有效计划执行 |
| 超时、空响应、服务错误 | 有限次数重试后 `PLANNER_UNAVAILABLE` | 回退未受限旧向量检索 |
| 置信度过低或槽位冲突 | `CLARIFY_OR_OUT_OF_SCOPE`，提出具体澄清问题 | 写成 `ENTITY_NOT_FOUND` |
| 有效意图但实体解析失败 | 仅实体必须存在的计划才走实体未找到或候选确认 | 让泛化推荐变成实体不存在 |

### 4.5 硬条件、软偏好与展示要求

编译器必须把候选单拆为三类，三类不能互相升级：

| 类型 | 例子 | 可做什么 | 不可做什么 |
| --- | --- | --- | --- |
| `hard_constraints` | 属于川菜、包含鸡肉、指定第 1 步 | 仅在本地取得图事实或正文证据后过滤/断言 | 无证据时放宽范围或写成事实 |
| `soft_preferences` | 清淡、少油感觉、家常、步骤少 | 用于受限向量排序和“贴近偏好”的措辞 | 说成低脂、低热量、一定省时 |
| `display_requests` | 想看步骤、食材、时间 | 仅展示 PDS 中实际存在的字段 | 从菜名、相似度或常识补写字段 |

工具、做法和时间默认都是软偏好；只有正文存在可解析、可回补的对应字段时，才可在答案中
作为事实陈述。每一个硬条件必须记录其证据来源；缺少来源时终止该条件路径，不得降级为全库。

## 5. 检索路径与选择规则

系统不是“图检索和向量检索二选一”。一个问题可由实体解析、图缩范围、向量排序和 PDS
正文回补组合完成。

### 路径 A：实体直接查正文

适用于用户明确问某道菜或某篇技巧的详情。

```text
LLM：RECIPE_DETAIL 或 TECHNIQUE_SECTION
  -> 实体解析：名称/别名/受控近似匹配，得到真实实体 ID
  -> PDS：按真实 ID 取完整菜谱或技巧正文
  -> 基于正文回答
```

例子：“宫保鸡丁怎么做？”

不使用向量检索，因为用户已经给出明确对象，按稳定 ID 读取更准确、更可审计。

### 路径 B：图关系查询

适用于用户问明确的实体关系。

```text
LLM：INGREDIENT_RECIPES / INGREDIENT_VEGETABLE_PAIRS / RECIPE_STEP
  -> 实体解析：获得真实食材或菜谱 ID
  -> 固定图模板：验证食材、菜谱、蔬菜、步骤之间的关系
  -> PDS：取关联菜谱正文或步骤上下文
  -> 基于“已验证图事实 + 正文证据”回答
```

例子：“猪肉适合搭配什么蔬菜？”

图数据库负责证明“猪肉、某菜谱、某蔬菜确实存在可追溯关系”；PDS 负责展示菜谱做法。
只有 `GraphFact.status=verified` 的关系才能在回答中当作事实。

### 路径 C：纯条件推荐

适用于没有明确菜名、食材或可验证范围的泛化需求。

```text
LLM：PREFERENCE_RECOMMEND
  -> 本地编译：受控全库菜谱 child chunk 范围 all_child_chunks
  -> Milvus V2：按场景与偏好寻找候选片段
  -> PDS：按命中 parent_id 回补完整菜谱
  -> 本地提取时间、步骤、工具、食材等可展示依据
  -> 推荐候选并说明“贴近偏好”的原因
```

例子：“下班很晚，想找准备步骤少的家常菜。”

这里的 `all_child_chunks` 是受 `QueryPlan`、构建版本和 PDS 链接校验约束的新版范围，
不是旧路径中没有正文回补和范围治理的向量检索。

`all_child_chunks` 只表示当前 active build 内、类型为 Recipe 的 child chunk，不包含技巧
文档、历史 build、未链接 parent 或任意其他 collection。`top_k`、向量相似度阈值、候选
扩展倍数和排序算法均为本地固定配置，LLM 不可见也不可控。

若没有匹配结果，状态应为 `NO_PREFERENCE_RESULTS`，而不是 `ENTITY_NOT_FOUND`。

### 路径 D：图缩小范围后再条件推荐

适用于用户既给出了可验证的硬范围，又给出了场景或口味等软偏好。这是与路径 C 并列的
主要组合路径，不是路径 C 的特殊补丁。

```text
LLM：PREFERENCE_RECOMMEND
  -> 必要时实体解析：如“鸡肉”“豆腐”得到真实食材 ID
  -> 固定图模板：取得可验证菜谱范围
       菜系范围：已验证属于川菜的 Recipe ID
       食材范围：确实包含鸡肉的 Recipe ID
       多食材范围：按明确规则求交集或并集
  -> Milvus V2：只在该 Recipe ID 范围内做偏好检索
  -> PDS：回补完整菜谱正文
  -> 回答“硬范围事实”和“偏好匹配”时分别表述
```

例子一：“想找少油感觉的川味晚餐。”

```text
硬范围：本地将 SICHUAN_STYLE 映射为受验证的川菜范围
软偏好：晚餐、少油感觉
结果：只在已验证川菜中找更贴近少油感觉的候选
```

例子二：“想吃鸡肉做的清淡晚餐。”

```text
实体解析：鸡肉 -> 真实食材 ID
图缩范围：得到含鸡肉的 Recipe ID
向量排序：只在这些鸡肉菜中找贴近清淡晚餐的候选
```

“少油感觉”“清淡”“不厚重”只能称为偏好匹配；“属于川菜”“包含鸡肉”必须由图事实
验证。

范围不能静默截断。若图查询得到的可验证 Recipe 范围超过当前检索器可表达的上限，实施时
必须采用可验证的分页/服务端范围过滤；在此能力上线前返回 `SCOPE_TOO_LARGE`，不能只取
前 N 条后仍声称覆盖全部范围。硬范围为空、图服务不可用或 PDS/Milvus build 不一致时，也
不得扩大成无范围全库检索。

### 路径 E：严格营养和医疗饮食

适用于用户明确提出可计算/可核验的营养阈值或医疗条件。

```text
用户：每份脂肪不超过 5 克的晚餐
  -> 输入边界后的本地硬安全预检：发现明确脂肪阈值
  -> LLM：STRICT_NUTRITION，并提取条件
  -> 本地检查是否存在受治理营养数据
       有：营养硬筛选 -> Recipe ID -> PDS 正文
       无：NUTRITION_EVIDENCE_INSUFFICIENT
```

营养数据是未来新增的、独立于图/PDS/向量库的治理数据源。要支持严格结论，它至少必须
保存：菜谱稳定 ID、每份定义、脂肪/热量等数值和单位、来源、审核状态、数据版本、过期
时间、计算方法或引用依据、医疗适用边界。

当前仓库没有这类受治理数据。因此当前阶段必须：

- 对“每份脂肪不超过 5 克”“热量低于 500 千卡”“糖尿病患者吃什么”等请求明确返回
  `NUTRITION_EVIDENCE_INSUFFICIENT`。
- 不用“少油”“清淡”“蒸煮”或向量相似度代替严格营养/医疗结论。
- 对“少油感觉”“不想太腻”“清爽一点”继续按路径 C 或 D 做软偏好推荐，并明确不得把
  其表述升级为低脂或医疗建议。

严格营养门只识别用户的**正向要求**，并且只读取 `user_message`。例如“不要说低脂”、
“我不要求低脂”以及评测规则中的“不要断言低脂”都不是严格营养请求；它们分别是回答
限制或否定信息。若本地硬门与 LLM 候选冲突，本地硬门优先，严格请求不得被降级为软偏好。

### 路径 F：澄清、近似名称和不存在实体

实体解析顺序应固定为：

```text
精确标准名
  -> 治理别名
  -> 受控近似匹配
  -> 并列候选确认
  -> 明确未找到
```

| 情况 | 例子 | 结果 |
| --- | --- | --- |
| 唯一高置信近似名称 | “宫爆鸡丁怎么做” | 提示按“宫保鸡丁”查询后继续执行 |
| 多个并列候选 | 同名菜谱或多个接近技巧 | 返回候选，请用户确认；不静默任选 |
| 明确实体确实不存在 | “知识库有蓝莓红烧肉吗” | `ENTITY_NOT_FOUND`，可给出安全的替代澄清问题 |
| 泛化推荐没有匹配 | “只用微波炉做什么方便” | `NO_PREFERENCE_RESULTS`，绝不使用实体不存在 |
| 意图不够明确 | “给我推荐最健康的” | 请求补充标准；医疗/严格营养风险时提示证据边界 |

近似匹配只能用于提出候选或在唯一高置信时规范化名称，不能直接伪造稳定 ID。
唯一高置信的定义必须在配置中冻结：最低分、第一名与第二名的最小分差、最大候选数均由
本地决定并纳入审计；任一条件不满足即为 `ENTITY_AMBIGUOUS`，不能静默选择第一名。

## 6. 意图到执行器、证据和失败状态映射

| 意图 | 本地编译动作 | 检索路径 | 回答所需证据 | 主要失败状态 |
| --- | --- | --- | --- | --- |
| `ENTITY_LOOKUP` | 确定预期实体类型，执行实体解析 | 实体解析 | 匹配候选、匹配方式 | `ENTITY_NOT_FOUND`、`ENTITY_AMBIGUOUS` |
| `RECIPE_DETAIL` | Recipe mention -> 真实 Recipe ID | 路径 A | PDS 完整菜谱正文 | `ENTITY_NOT_FOUND`、`PARENT_DOCUMENT_NOT_FOUND` |
| `RECIPE_STEP` | Recipe ID + 合法步骤序号 | 路径 B | verified 步骤图事实 + PDS 步骤窗口 | `GRAPH_RELATION_NOT_FOUND`、`PDS_ANCHOR_NOT_FOUND` |
| `TECHNIQUE_SECTION` | TechniqueDoc ID + 章节需求 | 路径 A/B | verified 技巧章节关系（若需要）+ PDS 正文 | `ENTITY_NOT_FOUND`、`GRAPH_RELATION_NOT_FOUND` |
| `INGREDIENT_RECIPES` | Ingredient mention -> 真实 Ingredient ID | 路径 B | verified `REQUIRES` 图事实 + PDS 菜谱正文 | `ENTITY_NOT_FOUND`、`GRAPH_RELATION_NOT_FOUND` |
| `INGREDIENT_VEGETABLE_PAIRS` | Ingredient ID + 已核验蔬菜分类 | 路径 B | verified 图事实 + PDS 菜谱正文 | `ENTITY_NOT_FOUND`、`GRAPH_RELATION_NOT_FOUND` |
| `PREFERENCE_RECOMMEND`，无硬范围 | 受控槽位 -> 全库 child chunk 范围 | 路径 C | PDS 回补正文；偏好仅作匹配理由 | `NO_PREFERENCE_RESULTS`、`VECTOR_UNAVAILABLE` |
| `PREFERENCE_RECOMMEND`，有菜系/食材范围 | 实体/菜系规范化 -> 图取得 Recipe ID 范围 | 路径 D | verified 范围事实 + PDS 回补正文 | `ENTITY_NOT_FOUND`、`CUISINE_SCOPE_NOT_FOUND`、`NO_PREFERENCE_RESULTS` |
| `STRICT_NUTRITION` | 解析阈值/医疗条件，检查治理数据 | 路径 E | 受治理营养来源 + PDS 正文 | `NUTRITION_EVIDENCE_INSUFFICIENT` |
| `CLARIFY_OR_OUT_OF_SCOPE` | 不编译 QueryPlan | 路径 F | 无 | `INTENT_UNRESOLVED`、`OUT_OF_SCOPE` |

`ENTITY_NOT_FOUND` 的唯一正确语义是：用户的计划确实需要一个可识别的实体，且在正确
类型范围中没有可靠候选。它不是“所有检索没有结果”的总称。

## 7. 本地计划编译规则

### 7.1 编译器输入和输出

```text
输入：已通过 schema 校验的 IntentCandidate
      + 可信用户问题
      + 本地会话偏好（如有）
      + 实体解析结果
      + PDS/图数据库可验证的运行态范围

输出：`CompileResult`，以下之一
      1. `EXECUTE`：已通过 QueryPlanValidator 的 QueryPlan 和声明策略
      2. `CLARIFY`：请求用户澄清的结构化状态
      3. `TERMINAL`：明确证据不足、实体不存在或超出范围的结构化状态
      4. `UNAVAILABLE`：依赖服务或工件不可用的结构化状态
```

编译器包含一张写死在代码中的意图映射表。它不接受 LLM 指定模板、ID 或检索范围。
例如 `RECIPE_STEP` 永远只能编译到固定的步骤模板；`PREFERENCE_RECOMMEND` 永远只能
编译到受限 V2 范围，不可转到旧的无约束检索。

只有 `EXECUTE` 可以调用图、Milvus、PDS 和生成模型。`CLARIFY`、`TERMINAL`、`UNAVAILABLE`
使用本地固定回复模板，不调用生成模型，不写语义缓存和会话上下文。`EXECUTE` 的输出还必须
携带本地构造的 `claim_policy`：可断言的硬事实、可说的软偏好、禁止声明和必要提示分别列出；
生成层只能在该范围内组织语言。

### 7.2 多实体推荐范围规则

当 `PREFERENCE_RECOMMEND` 包含食材时，必须在产品层冻结选择规则：

| 用户表达 | 范围规则 |
| --- | --- |
| “鸡肉做的清淡晚餐” | 图取包含鸡肉的菜谱范围，再向量排序 |
| “鸡肉和豆腐能做什么” | 默认取同时包含两者的交集；交集为空时可询问是否允许分别推荐 |
| “鸡肉或豆腐都可以” | 取并集，并在回答中说明候选来自哪类食材 |
| 仅“适合晚餐、步骤少” | 不要求实体，直接使用受控全库 child chunk 范围 |

菜系、食材、做法等只有在本地已存在可验证映射时才可作为硬范围。没有映射时，槽位
可保留为语义偏好，但不得伪装成图事实。

第一版一轮只允许一个主任务。若请求包含互不从属的多个任务，例如“推荐鸡肉菜并讲其中
一道的第一步”，编译器返回 `CLARIFY`，要求用户先选择任务；不得由 LLM 自行拆成多次
查询或自行选定“其中一道”。后续若产品需要多任务能力，应单独定义 `primary_intent`、
follow-up 范围、最大子计划数和原子失败策略。

### 7.3 规则保留位置

| 类别 | 保留为本地规则 | 不再作为顶层意图抢占规则 |
| --- | --- | --- |
| 高风险安全门 | 空输入、请求长度、注入/越权字段、明确医疗词、明确营养数值阈值 | 无 |
| 结构合法性 | JSON schema、枚举、置信度、槽位组合、数值范围 | 无 |
| 执行边界 | 固定模板、最大候选数、PDS/Milvus 构建一致性、实体类型、证据要求 | 无 |
| 普通语义 | 川味、少油感觉、清爽、快手、步骤少、家常、口味温和、地方特色 | 是；由 LLM 槽位理解，必要时做后校验 |

### 7.4 回退矩阵

| 情况 | planner 路径行为 | 是否允许旧 Router |
| --- | --- | --- |
| planner 开关关闭 | 保持当前路径，供灰度对照 | 允许 |
| planner JSON 非法、超时、低置信度或编译失败 | `CLARIFY` 或 `UNAVAILABLE`，fail-closed | 不允许 |
| 严格营养/医疗证据不足 | `TERMINAL`，固定说明证据边界 | 不允许 |
| 图、Milvus、PDS 不可用或 build 不一致 | `UNAVAILABLE`，不得扩大查询范围 | 不允许 |
| 已验证范围为空或超过实现上限 | `TERMINAL`（如 `NO_PREFERENCE_RESULTS`、`SCOPE_TOO_LARGE`） | 不允许 |

旧 Router 只能在 planner 根本未启用时使用，不能作为 planner 已启用后的“猜测补救”。
实现必须移除新 planner 调用链对 `validate_or_conservative()`、关键词 `_try_*` 抢占和
隐式 legacy fallback 的依赖；这些兼容逻辑不得绕过 `CompileResult`。

### 7.5 不可违反的不变量

```text
1. LLM 只生成需求单，永远不能直接生成或执行 QueryPlan。
2. LLM 永远不能产生 ID、模板、范围、过滤器、排序、候选数或证据等级。
3. 只有 EXECUTE 可以访问检索器和生成模型。
4. 只有 verified 图事实才能支持结构化关系断言，只有 PDS 回补正文才能进入最终回答。
5. 严格营养和医疗请求不得降级为软偏好；软偏好不得升级为营养或医疗结论。
6. 任一失败、范围为空或依赖不可用时，均不得扩大检索范围。
7. 未声明支持的槽位组合和多任务请求必须澄清或终止。
8. 范围截断必须显式返回状态，禁止静默截断后宣称完整覆盖。
9. CLARIFY、TERMINAL、UNAVAILABLE 不得生成、缓存或写入会话。
10. 所有上述决定必须进入审计，且可由测试观测。
```

## 8. 分阶段实施计划

### 实施代理的自主恢复纪律

本方案的实施代理对“完成实施并通过第 9.5 节最终闸门”负责，而不是只对代码修改负责。
服务未启动、依赖缺失、构建工件过期、测试失败、端口冲突、配置不一致或本次改动引入的
运行错误，都属于代理应先自行处理的常规实施工作，不是向用户报告“实施失败”的理由。

每次验证前后，代理必须按以下闭环执行，直至本阶段和最终闸门通过：

```text
检查状态 -> 定位根因 -> 启动/修复本地依赖或本次代码 -> 重建可再生工件
-> 重跑受影响测试和健康检查 -> 修复新增失败 -> 记录证据 -> 推进下一阶段
```

允许自主处理的范围：

- 启动、停止、重启仓库声明的本地开发服务；优先只启动本阶段需要的 Neo4j、Milvus、
  etcd、MinIO 或 backend，并通过健康检查、日志和只读查询确认就绪。
- 安装项目声明的开发依赖、修复本次改动的代码/测试/配置、释放本次进程占用的端口、重建
  本任务产生且可由脚本确定性再生的 PDS、V2 向量索引或测试工件。
- 遇到服务或测试失败时读取日志、检查环境变量和 artifact manifest，做最小修复并重复验证；
  不得用跳过测试、降低断言、伪造审计、硬编码通过结果或关闭安全检查来“修复”。

以下情况仍是不可自行突破的边界：不得猜测或索取之外的凭据；不得清空、删除、覆盖既有
Neo4j/Milvus 数据、Docker volume、旧 collection 或用户文件；不得启动会自动导入或写入
既有数据的服务组合，除非先确认目标是隔离的本地开发实例或已有明确的受保护授权；不得
绕过生产/staging 审批、外部账号权限、真实数据治理决策或本方案的 fail-closed 规则。

若遇到此类外部边界，代理仍须完成所有可安全执行的本地诊断、修复、测试和证据记录；只有
在连续排除可自行修复的原因后，才可报告精确的外部阻塞项。单纯“服务没启动”不构成阻塞。

### 阶段 0：冻结契约和输入边界

目标：在不接入生产路径前冻结“用户说什么”和“系统限制什么”的边界。

- 新增 `IntentCandidate` 数据模型和 JSON schema，不修改现有执行 `QueryPlan` 契约。
- 新增明确的 API 请求边界：`user_message` 与 `evaluation_constraints` 分离；旧单字段兼容
  期间不得把内部约束拼接进用户语义输入。
- 定义所有意图、槽位枚举、置信度阈值、字段/列表长度上限、硬软条件分类、澄清状态和审计字段。
- 冻结多食材交集/并集策略、菜系规范化映射和无法验证时的表达规则。
- 冻结 `CompileResult` 的 `EXECUTE`、`CLARIFY`、`TERMINAL`、`UNAVAILABLE` 状态及其是否
  允许检索、生成、缓存的矩阵。

验收：S07-C 中“不要断言低脂”等文字不进入 planner 与营养识别；planner-only 测试能
确认输入边界。

### 阶段 1：LLM 意图理解器

目标：为每个 new-path 请求生成有限、可校验的候选单。

- 新增独立 planner 模块，使用低温度、短输出、严格 JSON 约束和明确超时。
- prompt 只列出允许意图、允许槽位、反例和禁止字段；不暴露数据库结构、真实 ID 或查询语句。
- 使用 JSON schema/Pydantic 校验模型响应，拒绝多余字段。
- 校验需求单只能包含用户需求字段；拒绝 ID、模板、范围、过滤器、排序和证据字段。
- 记录 planner 模型版本、延迟、响应哈希、解析状态、规范化候选和拒绝原因；不把原始敏感
  内容写入非受控日志。

验收：非法 JSON、空响应、未知意图、低置信度、超时全部 fail-closed；任何失败不会调用
旧未受限向量检索。

### 阶段 2：本地编译器与统一路由

目标：由一个入口替代当前按关键词抢占的 `_try_*` 顺序。

- 新增 `IntentPlanCompiler`，输入为候选单与本地解析结果，输出 `QueryPlan` 或结构化终止状态。
- 编译结果必须显式标记 `EXECUTE`、`CLARIFY`、`TERMINAL` 或 `UNAVAILABLE`；只有 `EXECUTE`
  可以继续访问检索器和生成模型。
- 先处理明确的高风险营养/医疗门，再执行 planner；普通“少油、清爽”等不抢占流程。
- 将现有实体直达、目标图、受限向量执行器接到编译结果，不重写其白名单边界。
- 修改 `retrieve_for_generation()`：new 路径选择后先进入 planner/compile，而不是先分别运行
  营养、目标图、偏好词表和实体直达。
- planner 已启用后的非法输出、编译失败、证据不足、范围为空或依赖不可用均 fail-closed，
  不允许旧 Router 回退；旧 Router 只在 planner 开关关闭时保留作灰度对照。

验收：S06-A-02 编译为路径 C；S07-A-02 编译为路径 D；两者不进入 `ENTITY_NOT_FOUND`。

### 阶段 3：实体体验和范围组合

目标：完成实体别名、近似候选、澄清，以及食材/菜系范围加偏好排序。

- 为实体解析结果增加“唯一高置信近似”“并列候选”“无候选”三种稳定结果。
- 将实体解析用于需要实体的计划，而不再对所有问题盲目尝试菜谱/技巧名匹配。
- 实现“图缩范围 -> 范围内 V2 向量 -> PDS 回补”的组合编译。
- 明确当硬范围不存在、图服务不可用、范围为空时的状态；禁止扩大为未验证全库范围并声称硬事实。
- 增加范围超过上限时的 `SCOPE_TOO_LARGE` 状态；在分页/完整过滤实现前不得静默截断。

验收：川味/川菜、鸡肉+清淡、多食材交集/并集、近似菜名、同名歧义都有单元和集成测试。

### 阶段 4：营养与医疗边界

目标：将严格营养能力与软偏好能力彻底分开。

- 当前没有治理营养源时，继续保持严格请求的证据不足出口。
- 将“少油感觉、清爽、不厚重”编译为软偏好，允许路径 C/D，不允许生成严格营养声明。
- 若未来产品批准营养数据源，单独引入版本化营养存储和审核契约，再开启营养硬筛选；不得从
  菜谱正文或向量相似度推导医学/营养结论。

验收：所有脂肪克数、热量阈值和医疗饮食测试均无误报；软偏好推荐均含“偏好匹配而非严格
营养验证”的生成约束。

### 阶段 5：SSE 空回答独立修复

目标：修复检索已成功但流式生成零输出仍被记成功的问题，且不与 planner 代码混在同一提交。

- 流式生成耗尽后，若 `chunk_count == 0` 或 `answer_chars == 0`，记为 `GENERATION_EMPTY_STREAM`。
- 将空流视为一次失败，受控重试或执行一次非流式回退；回退答案仍为空则请求失败。
- Web 层只对非空成功回答写入语义缓存和会话上下文。
- 审计中 `Generation Stream`、`Final Output`、`Request Complete` 三处成功状态必须一致。

验收：空迭代器、仅无内容分片、空非流式回退、正常流、流中断等注入测试全部覆盖。

### 阶段 6：灰度、审计与回退

目标：在现有 new-path 开关体系中逐步启用，保持可观测和可回退。

- 增加独立 planner 开关和版本号；默认关闭。
- 审计记录候选意图、编译路径、实体解析结果数量、范围来源、图事实状态、PDS 回补数量、
  向量范围、最终限制与生成非空状态。
- 用固定 300 题、释义改写集和失败注入集在灰度前后对比。
- planner 服务不可用时保持 fail-closed，不把新路径扩大到不受控检索；planner 已启用时
  禁止旧 Router 回退，只有关闭 planner 的对照流量才可使用旧 Router。

## 9. 测试与验收计划

### 9.1 Planner-only 测试

不连接数据库，只验证“人话 -> 候选单”。

- 正式 300 题人工冻结期望意图和关键槽位。
- S06/S07 扩展释义矩阵：快手/省事/步骤少/准备少、川菜/川味、少油感觉/不油腻/轻口味/
  不厚重、清蒸/蒸制/煮制等。
- 注入未知意图、非法 JSON、多余字段、伪造 ID、Cypher 字段、超时、空响应、低置信度。
- 注入超长 mention、过多实体/槽位、未知枚举、否定营养表达、多个独立任务和不支持的槽位组合。
- 验收指标：候选单合法率、意图准确率、关键槽位准确率、无效候选执行率为零。

### 9.2 检索层测试

使用 Fake Neo4j、Fake Milvus、临时 PDS 验证本地编译和执行边界。

- 每个意图只产生对应白名单 `QueryPlan`。
- 任何 LLM 输出不得影响模板 ID、图关系类型、数据库名、collection、nodeId 或 `parent_id`。
- 需求单不能直接交给执行器；`CompileResult` 非 `EXECUTE` 时检索调用次数必须为零。
- 关系题必须有 verified 图事实；向量命中必须 PDS 回补。
- 纯偏好题无候选返回 `NO_PREFERENCE_RESULTS`；没有明确实体的题永不返回 `ENTITY_NOT_FOUND`。
- 菜系/食材范围加偏好的组合路径只在已验证范围中搜索。
- 范围超过上限返回 `SCOPE_TOO_LARGE`，不得静默取前 N 条。

### 9.3 生成与 API 层测试

- 模拟正常流、空流、仅空内容分片、流异常、非流式回退成功和回退为空。
- 验证 `[DONE]` 不能是唯一输出且仍被记录成功。
- 验证空答案不会进入缓存和会话上下文。
- 验证严格营养不足时不会调用生成模型来编造推荐；软偏好回答不会声称低脂、低热量或医疗适用。
- 验证 `evaluation_constraints` 不进入 planner 输入。
- 验证 `CLARIFY`、`TERMINAL`、`UNAVAILABLE` 不调用生成、不写缓存、不写会话上下文。
- 验证多任务请求不会被自动拆解为多个查询计划。

### 9.4 端到端验收阈值

| 指标 | 验收要求 |
| --- | --- |
| S06/S07 泛化推荐误报 `ENTITY_NOT_FOUND` | 0 |
| 严格营养/医疗误报 | 0 |
| planner 非法输出实际执行次数 | 0 |
| 非 `EXECUTE` 状态调用检索/生成次数 | 0 |
| 图关系无 verified 证据仍被断言次数 | 0 |
| 向量候选缺 PDS 回补仍进入回答次数 | 0 |
| `chunk_count=0` 或 `answer_chars=0` 被标成功次数 | 0 |
| 300 题结果覆盖 | 100%，无重复或未知题 |

### 9.5 最终实施完成与上线闸门

以下表格是本方案的最终验收边界，不是建议项。每一行都必须有可自动运行的测试，并在
验收报告中保存测试名称、输入、断言结果和对应审计记录。任一行缺少测试、测试失败、
审计不可观测或阈值未达标，均视为**未完成实施**：`RETRIEVAL_INTENT_PLANNER_ENABLED`
必须保持 `false`，不得进入灰度或替代当前路径。

| 验收边界 | 必须验证的事实 | 通过条件 | 失败后的结论 |
| --- | --- | --- | --- |
| 需求单与执行单隔离 | 注入 ID、模板、过滤器、范围、排序、候选数、证据等级 | schema 拒绝；执行器调用次数为 0 | 不得启用 planner |
| 编译状态闸门 | 对 `CLARIFY`、`TERMINAL`、`UNAVAILABLE` 分别注入 | 图、Milvus、PDS、生成、缓存、会话写入次数均为 0 | 不得启用 planner |
| 输入可信边界 | `evaluation_constraints`、系统规则、否定营养表达、历史偏好同时出现 | planner 与营养门只依据 `user_message`；结构化授权偏好不得覆盖本轮需求 | 不得启用 planner |
| 执行权限与回退 | planner 非法、超时、低置信度、编译失败、依赖不可用 | 不调用 `validate_or_conservative()`、关键词抢占或旧 Router；返回对应结构化状态 | 不得启用 planner |
| 证据和声明边界 | 图关系、向量命中、软偏好、缺失时间/工具字段 | 关系断言均有 verified 图事实；回答正文均有 PDS 回补；软偏好不升级为硬/营养事实 | 不得启用 planner |
| 硬范围边界 | 菜系、食材、多食材交并集、范围为空、范围超上限 | 只在已验证范围内检索；空范围不扩展；超限返回 `SCOPE_TOO_LARGE`，无静默截断 | 不得启用 planner |
| 实体解析边界 | 精确名、别名、近似名、并列候选、无候选 | 仅本地决定实体类型；近似名满足阈值才规范化；歧义不静默选择 | 不得启用 planner |
| 营养与医疗边界 | 脂肪/热量阈值、疾病饮食、少油感觉、否定低脂说法 | 严格请求只走治理证据；当前均返回证据不足；软偏好不产生医疗/营养结论 | 不得启用 planner |
| 多任务与未知组合 | 两个独立任务、未知枚举、超长或过多槽位 | 返回 `CLARIFY_OR_OUT_OF_SCOPE`；不拆计划、不透传陌生检索词 | 不得启用 planner |
| 输出与缓存边界 | 正常流、空流、仅空分片、失败回退 | 空输出不记成功、不缓存、不写会话；成功审计三处一致 | 不得启用 planner |
| 自主恢复与真实运行 | 服务未启动、依赖缺失、端口冲突、artifact 不一致、一次失败后修复 | 代理自行恢复安全本地依赖并重跑验证；报告含健康检查、修复和重跑证据 | 不得宣称实施完成 |
| 回归与审计完整性 | 冻结 300 题、释义集、失败注入集 | 第 9.4 全部阈值达标，审计包含第 12 节全部必填字段 | 不得进入灰度 |

完成实施的唯一判定是：上述全部自动化测试通过、第 9.4 所有阈值达标、依赖服务已由代理
实际验证可用且验收报告可复核，并由负责人显式将 planner 开关从关闭状态纳入灰度。只完成
代码、只完成局部测试、只通过 300 题或只报告“服务未启动”都不构成“实施完成”。

## 10. 关键场景模拟

### 场景一：下班晚、步骤少的家常菜

```text
用户：下班很晚，想找准备步骤少的家常菜。

LLM 候选：PREFERENCE_RECOMMEND
槽位：晚餐、家常、准备少、步骤少

编译：不要求实体；全库受控 child chunk 范围
执行：Milvus V2 -> 候选菜谱 ID -> PDS 全文
回答：引用正文中的时间、步骤、工具等作为“贴近需求”的依据
无结果：NO_PREFERENCE_RESULTS
```

### 场景二：少油感觉的川味晚餐

```text
用户：想找少油感觉的川味晚餐。

LLM 候选：PREFERENCE_RECOMMEND
槽位：SICHUAN_STYLE、晚餐、LOW_OIL_FEEL

编译：本地将川味映射到可验证川菜范围
执行：图验证川菜 Recipe ID -> 范围内 Milvus V2 -> PDS
回答：川菜归属是图事实；少油感觉是偏好匹配
禁止说法：这是低脂川菜
```

### 场景三：宫保鸡丁第一步

```text
用户：宫保鸡丁第一步怎么做？

LLM 候选：RECIPE_STEP
实体提及：宫保鸡丁（Recipe）
槽位：step_number=1

编译：实体解析 -> 真实 Recipe ID；步骤号校验
执行：固定 Recipe -> CookingStep 图模板 -> PDS 步骤窗口
回答：图证明该步骤属于该菜谱且顺序为 1；PDS 提供完整步骤正文
```

### 场景四：鸡肉做的清淡晚餐

```text
用户：想吃鸡肉做的清淡晚餐。

LLM 候选：PREFERENCE_RECOMMEND
实体提及：鸡肉；本地按该意图仅解析 Ingredient
槽位：晚餐、清淡

编译：实体解析鸡肉 -> 图找包含鸡肉的 Recipe ID
执行：范围内 Milvus V2 -> PDS
回答：包含鸡肉是图事实；清淡是偏好匹配
```

### 场景五：宫爆鸡丁近似名称

```text
用户：宫爆鸡丁怎么做？

LLM 候选：RECIPE_DETAIL
实体解析：唯一高置信别名/近似候选“宫保鸡丁”
执行：提示规范化名称 -> PDS 完整菜谱
```

若有多个并列候选，则不执行详情检索，先让用户确认。

### 场景六：每份脂肪不超过 5 克

```text
用户：推荐每份脂肪不超过 5 克的晚餐。

本地硬门：明确营养阈值
LLM 候选：STRICT_NUTRITION
当前数据能力：没有受治理营养数据
结果：NUTRITION_EVIDENCE_INSUFFICIENT
禁止：以“看起来清淡”的菜替代答案
```

### 场景七：评测安全约束

```text
用户真实问题：想喝一碗清淡些的川味汤。
评测限制：没有治理数据时不要断言低脂。

LLM 仅解析用户真实问题：PREFERENCE_RECOMMEND
执行：川菜范围 -> 向量推荐 -> PDS
生成：遵守评测限制，但不把用户问题误判为严格低脂请求
```

## 11. 预计文件影响范围

下列为实施时的预期文件范围，具体命名以现有模块风格为准：

| 范围 | 预期改动 |
| --- | --- |
| `rag_modules/intent_planner.py` | 新增 LLM 候选单调用、超时、JSON 解析、审计适配 |
| `rag_modules/intent_candidate.py` 或现有契约模块 | 新增候选单 schema、枚举和本地校验 |
| `rag_modules/intent_plan_compiler.py` | 新增候选单到 QueryPlan/终止状态的本地编译 |
| `main.py` | 用统一 planner/compile 入口替换 new 路径关键词抢占顺序 |
| `rag_modules/entity_resolver.py` | 补充近似候选/澄清所需的稳定结果，不放开伪 ID |
| `rag_modules/nutrition_policy.py` | 将严格门与软偏好语义边界改为结构化输入后处理 |
| `rag_modules/web_service_handler.py` | 分离可信用户消息与系统/评测约束；修复空 SSE 成功与空缓存 |
| `rag_modules/generation_integration.py` | 修复空流检测、回退和一致审计 |
| `test/` | planner-only、编译器、组合检索、营养边界、空流、API 输入边界、300 题回归 |

现有 `query_plan.py`、`query_plan_validator.py`、`targeted_graph_retrieval.py`、
`restricted_vector_retrieval.py` 应优先复用。除非测试证明已有白名单不足，否则不放宽
这些模块的执行权限。

## 12. 审计、灰度和回退

每次请求至少记录：

```text
planner_input_hash
planner_model / planner_version / latency
planner_parse_status / candidate_intent / confidence / normalized_slots
compiler_status / compile_action / selected_path / query_plan_hash
entity_resolution_status / candidate_count / chosen_ids（仅审计允许时）
graph_template_id / graph_fact_status
hard_constraints / soft_preferences / claim_policy
vector_scope / scope_size / scope_truncated / parent_count / PDS_text_evidence_count
nutrition_policy_status
generation_chunk_count / answer_chars / generation_called / cache_write_status / context_write_status
```

开关应独立于已有 new-path 灰度开关，例如：

```text
RETRIEVAL_INTENT_PLANNER_ENABLED=false
RETRIEVAL_INTENT_PLANNER_VERSION=v1
```

回退原则：

- planner 关闭时，保持当前行为，便于对照和回滚。
- planner 开启但失败时，不扩大检索权限；返回澄清/不可用/证据不足状态，不走旧 Router。
- 只有 planner 关闭的对照流量才允许旧 Router，并必须审计 `legacy_fallback_reason`。
- PDS/Milvus 构建不一致、图服务不可用、营养治理数据缺失时，不伪造成功。
- 流式输出为空时不缓存、不记成功。

## 13. 实施前需冻结的决策

1. planner 使用的模型、P95 延迟预算、单请求成本预算和可用性目标。
2. 用户问题、系统规则、评测约束、会话偏好的 API 数据结构与可信来源。
3. 候选单枚举和槽位词典的版本管理方式。
4. 多食材“交集/并集”的默认产品语义。
5. 当没有匹配候选时，产品是请求补充条件还是直接说明资料不足。
6. 未来严格营养数据的来源、审核、每份定义、版本与医疗边界；在此之前严格模式保持关闭。
7. 仅在 planner 关闭的对照流量中使用旧 Router 的开关与审计标记；planner 启用后的故障
   始终 fail-closed，不允许以用户授权绕过该边界。

## 14. 现有实现与审计依据

- 当前 new 路径的关键词抢占顺序和实体直达提前返回：`main.py` 中
  `AdvancedGraphRAGSystem.retrieve_for_generation()`、`_preference_plan()`、
  `_try_nutrition_recommendation()`、`_try_entity_direct()`。
- 当前固定 QueryPlan/模板白名单和 `llm_candidate` 来源支持：
  `rag_modules/query_plan.py`、`rag_modules/query_plan_validator.py`。
- 当前固定图模板和 verified 图事实边界：`rag_modules/targeted_graph_retrieval.py`。
- 当前 V2 受限向量、PDS 链接和空范围拒绝：`rag_modules/restricted_vector_retrieval.py`。
- 当前实体定位优先级：`rag_modules/entity_resolver.py`。
- 当前严格营养与软偏好边界：`rag_modules/nutrition_policy.py`。
- 当前空流仍会记成功的生成/HTTP 链路：`rag_modules/generation_integration.py`、
  `rag_modules/web_service_handler.py`。
- S05 空 SSE 证据：
  `_other/考试/测试试卷2/结果/2026-08-12-new-smoke-004/audits/new/S05-A-02/20260812_061725_654_af9dbc9c/rag_process.md`。
- S06 无候选且未发生向量检索证据：
  `_other/考试/测试试卷2/结果/2026-08-12-new-smoke-004/audits/new/S06-A-02/20260812_062254_062_b99fa6f5/rag_process.md`。
- S07-C 约束污染实际审计：
  `_other/考试/结果/2026-08-12-真实考试-001/audits/new/S07-C-01/20260811_195057_578_a1248a3e/rag_process.md`。

本文件是实施方向和验收契约，不授权直接修改运行逻辑、图数据、Milvus、PDS 或考试产物。
