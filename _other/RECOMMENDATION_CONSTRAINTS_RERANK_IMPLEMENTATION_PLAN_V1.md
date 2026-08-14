# 推荐约束与重排实施方案 V1

## 1. 目的

本方案解决当前 `PREFERENCE_RECOMMEND` 路径的一个具体问题：系统能识别菜系、做法、工具、人数、时长和口味等槽位，但只有菜系和具名食材会稳定缩小候选范围；其余条件主要依赖向量相似度，导致“清爽川味蒸菜”召回麻辣香锅、火锅底料等不合适菜谱。

目标不是让 LLM 直接写检索规则，而是在现有意图识别之后，用本地代码把槽位转换为一张可审计的约束需求单，再执行“硬过滤 -> 向量召回 TopN -> 软偏好重排 -> TopK -> PDS 正文回答”。

## 2. 已确认的现状

当前路径位于 `main.py`：

```text
intent_planner.plan(user_message)
  -> _planner_preference_scope(candidate)
  -> IntentPlanCompiler.compile(...)
  -> _try_restricted_vector(query, top_k, plan)
  -> generation
```

- `IntentCandidate` 已有 `cuisines`、`ingredients`、`methods`、`tools`、`preferences`、`meal_context`、`servings`、`time_budget_minutes` 等槽位。
- `_planner_preference_scope()` 会对川菜和具名食材生成已验证的菜谱 ID 范围并取交集。
- `PREFERENCE_RECOMMEND` 当前将范围以 `parent_ids` 传给 `RestrictedVectorRetriever`，再直接取配置的 `top_k`，没有独立重排。
- PDS 物化器已持有菜系、准备时间、烹饪时间、份量、每步的 `methods` 和 `tools` 原始数据；当前父文档 metadata 未聚合全部方法/工具字段。
- 300 题审计显示：工具约束“微波炉”大多能被文本召回命中；“清爽、轻口味、少工具、蒸制”等组合偏好不稳定。尤其“清爽川味蒸菜”的五个候选中包含麻辣香锅、尖叫牛蛙、牛油火锅底料和水煮鱼。

## 3. 原则与边界

1. LLM 只识别意图和填写槽位，不能输出 Cypher、Milvus filter、实体 ID、`parent_id`、权重、查询模板或执行计划。
2. 本地代码决定槽位的执行方式：硬过滤、软重排或澄清/安全终止。
3. 明确的“只、仅、必须、不能、完全不要”等表达可升级为硬约束，但仅限 V1 已声明支持的字段：菜系、具名食材、方法、烹饪设备和可解析总时长。普通“想要、偏好、尽量、清爽一点”等默认是软偏好。
4. 没有可验证字段时，不能把主观推断当作事实。`清爽` 可以用于排序，不能据此宣称低脂、低热量或医疗适用。
5. 硬过滤必须在向量召回之前进行；不能只在既有 Top5 之后删结果。
6. 软偏好保留在原始向量查询中以提高候选召回率，同时必须用于后续重排。
7. 无完全匹配时不能偷偷放宽硬约束。必须返回可解释的无结果/放宽建议，或仅在用户明确允许的回退策略下放宽。

## 4. 目标架构

```text
用户真实问题
  -> IntentPlanner: IntentCandidate（意图 + 原始槽位）
  -> RecommendationConstraintCompiler: ConstraintSpec（约束需求单）
  -> 硬过滤：从活动 PDS build 得到合格 parent_id 集合
  -> RestrictedVectorRetriever：在合格集合中召回 TopN
  -> PreferenceReranker：按软偏好重排并取 TopK
  -> PDS 证据（最终 TopK）
  -> Generation（仅基于最终证据）
```

`ConstraintSpec` 是新增的内部数据模型；它不是 LLM 输出，也不是 `QueryPlan` 的替代品。

- `IntentCandidate`：模型说用户表达了什么。
- `ConstraintSpec`：本地策略说每个条件如何执行。
- `QueryPlan`：本地程序生成的受限检索计划。

## 5. 需求单数据模型

建议新增 `rag_modules/recommendation_constraints.py`，使用冻结 dataclass 或 Pydantic 模型，并提供严格校验与 `to_dict()` 审计输出。

```python
@dataclass(frozen=True)
class HardRecipeFilters:
    cuisines: tuple[str, ...] = ()
    verified_ingredient_ids: tuple[str, ...] = ()
    methods: tuple[str, ...] = ()
    excluded_methods: tuple[str, ...] = ()
    tools: tuple[str, ...] = ()
    excluded_tools: tuple[str, ...] = ()
    required_cooking_appliances: tuple[str, ...] = ()
    excluded_cooking_appliances: tuple[str, ...] = ()
    max_total_minutes: int | None = None

@dataclass(frozen=True)
class SoftRecipePreferences:
    preferences: tuple[str, ...] = ()
    meal_context: tuple[str, ...] = ()
    prefer_shorter_time: bool = False
    target_servings: int | None = None

@dataclass(frozen=True)
class ClarificationDecision:
    required: bool = False
    reason: str | None = None

@dataclass(frozen=True)
class ConstraintSpec:
    intent: str
    hard_filters: HardRecipeFilters
    soft_preferences: SoftRecipePreferences
    clarification: ClarificationDecision
    policy_version: str = "recommendation_constraints_v1"
```

V1 只支持已存在或可确定抽取的字段：菜系、做法、工具、总耗时、份量、餐次和偏好。`油重感`、`温和`、`清爽` 不应在 V1 作为硬字段。

### 5.1 分类规则

| 用户表达 | V1 分类 | 说明 |
| --- | --- | --- |
| “川菜”“川味” | 硬过滤 | 现有图/PDS 已支持。 |
| “只有微波炉”“只用微波炉” | 硬过滤 | 必须使用微波炉，且不得依赖其他烹饪设备；刀、碗、筷子等准备工具不视为冲突。 |
| “必须蒸制”“只想蒸” | 硬过滤 | 不满足做法即不合格。 |
| “不能用微波炉”“完全不要油炸” | 硬过滤 | 写入排除工具/排除方法，候选含冲突项即不合格。 |
| “30 分钟内” | 硬过滤 | 仅对可解析总耗时的菜谱执行。 |
| “两人份”“两个人吃” | 软偏好 | V1 始终只排序优先，不把份量升级为硬过滤，也不制造精确份量承诺。 |
| “清爽一点”“别太腻”“简单些” | 软偏好 | 使用可解释信号重排。 |
| 同名实体、多任务冲突、必要对象不明确 | 澄清 | 不发起不等价检索。 |
| 严格营养/医疗要求 | 安全终止 | 复用现有营养证据不足路径。 |

分类必须由本地 `RecommendationConstraintCompiler` 完成。它接收 `user_message`、已校验 `IntentCandidate` 和本地解析出的具名食材 ID，依据受控词表、否定词和显式强度词判断；不信任 LLM 自行声明“这是硬约束”。具名食材只有通过 `EntityResolver` 唯一解析后才可写入 `verified_ingredient_ids`；模型的原始食材词继续留在 `IntentCandidate`，不能直接作为执行 ID。

## 6. 数据与候选池改造

### 6.1 物化属性

修改 `rag_modules/parent_document_materializer.py`，在 Recipe 父文档 metadata 中写入：

```json
{
  "cuisine_type": "川菜",
  "recipe_methods": ["STEAM", "BOIL"],
  "recipe_tools": ["MICROWAVE"],
  "recipe_cooking_appliances": ["MICROWAVE"],
  "step_count": 4,
  "prep_minutes": 6,
  "cook_minutes": 15,
  "total_minutes": 21,
  "servings_text": "1人份",
  "servings_count": 1,
  "attribute_provenance": {
    "recipe_methods": "graph_step.methods",
    "recipe_tools": "graph_step.tools",
    "step_count": "graph_step.count",
    "total_minutes": "recipe.prepTime+recipe.cookTime"
  }
}
```

要求：

- 方法和工具必须使用与 `IntentSlots` 一致的受控枚举；无法映射时保留原始文本，不伪造枚举。
- `recipe_cooking_appliances` 只包括会直接烹饪的设备，如 `MICROWAVE`、`RICE_COOKER`、`WOK`、`STEAMER`、`OVEN`；刀、碗、筷子、案板等准备工具不在其中。V1 的“只有微波炉”判定为：候选包含 `MICROWAVE`，且 `recipe_cooking_appliances` 是 `{MICROWAVE}` 的子集。
- `step_count` 为有来源的 Recipe 步骤总数；缺失或无法可靠聚合时为 `null`，不以正文行数或字符数替代。
- `total_minutes` 仅在准备/烹饪时间可可靠解析时写入；无法解析则为 `null`，不是 `0`。
- 份量解析失败不阻塞 build，但不得伪造 `servings_count`。
- 新字段会改变 PDS build，必须重建 Milvus V2、联合 manifest，并运行既有 PDS/Milvus linkage 校验。

### 6.2 候选范围解析

扩展 `main.py::_planner_preference_scope()`，或抽出 `RecommendationCandidateScopeResolver`：

1. 复用现有菜系和具名食材的已验证范围。
2. 根据活动 PDS build 的 `recipe_methods`、`recipe_tools`、`recipe_cooking_appliances`、`total_minutes` 增加 parent ID 集合；正向硬条件取包含关系，排除条件取不包含关系。
3. 对所有硬集合取交集；无交集返回 `NO_PREFERENCE_RESULTS`，并在 limitation/audit 中记录哪个硬条件造成空集。
4. 对缺失 metadata 的菜谱：硬过滤时视为“不满足”；软重排时保留但不加分，并记录属性未知。
5. 保留 `QueryPlan` 的现有 `parent_ids` 白名单接口；不允许 LLM 创建任意 Milvus filter。

## 7. 召回与重排

### 7.1 两段式候选

对 `PREFERENCE_RECOMMEND`：

1. 在硬范围内召回 `candidate_k=30`；若硬范围小于 30，则取全部范围。
2. 使用完整的可信 `user_message` 作为向量查询，保留软偏好语义。
3. 对最多 30 个 `ParentAggregate` 执行本地重排。
4. 只将重排后的 `answer_k`（默认 5）回补为最终证据并交给生成层。

不要把 `candidate_k` 与回答用的 `top_k` 混为一谈。前者为重排留足候选，后者控制最终上下文长度。

### 7.2 V1 规则重排器

新增 `rag_modules/preference_reranker.py`，输入为 `ConstraintSpec`、向量候选及父文档 metadata，输出稳定排序和逐项解释。

V1 不调用第二个 LLM。每个候选的分数由以下组成：

```text
final_score = vector_score
            + soft_match_bonus
            + structured_fit_bonus
            - conflict_penalty
```

评分表必须版本化为 `recommendation_rerank_v1`，按如下确定性规则实施：

| 项目 | 规则 | 分值 |
| --- | --- | --- |
| 基础向量分 | 将本批候选的 `ParentAggregate.score` min-max 归一化到 `[0, 1]`；若全部相等则为 `0.5`。 | `70 * normalized_score` |
| `LIGHT_FEEL` 正向 | `recipe_methods` 含 `STEAM` 或 `BOIL`，且不含 `FRY`。 | `+10` |
| `LIGHT_FEEL` 冲突 | `recipe_methods` 含 `FRY`。 | `-20` |
| `FEW_STEPS` | `step_count <= 6`。 | `+6` |
| `FEW_STEPS` 时长 | `total_minutes <= 25`。 | `+6` |
| `FEW_STEPS` 反向 | `total_minutes > 60`。 | `-6` |
| 目标份量 | `servings_count == target_servings`。 | `+4` |
| 邻近份量 | `abs(servings_count - target_servings) == 1`。 | `+1` |

未知字段不加分、不扣分。若同一候选同时命中正向和冲突规则，冲突规则优先，例如含 `FRY` 的菜不得取得 `LIGHT_FEEL` 正向加分。V1 不对 `DINNER` / `BREAKFAST` 打结构化分，除非先建立了有来源的餐次字段。显式工具/做法已经作为硬过滤时，不再靠分数弥补不符合者。仅表达“做法/口感偏好”，绝不输出低脂断言。

排序必须稳定：相同分数以原向量分、parent ID 作为固定 tie-breaker。每条候选保存 `vector_score`、各项 bonus/penalty、`final_score`、属性来源和未知字段。

### 7.3 无完全匹配和降级

- 硬范围为空：不扩大到全库；回复“没有同时满足 X、Y 的已验证菜谱”，并给出一次可选放宽方向。
- 软偏好无可靠信号：仍可使用向量结果，但回答应说明“按正文的做法/标签贴近偏好推荐”，不将其表述为严格事实。
- 向量不可用、工件不一致、PDS 不可用：复用当前 fail-closed 终止路径。

## 8. 代码改动清单

| 模块 | 改动 |
| --- | --- |
| `rag_modules/recommendation_constraints.py` | 新增需求单模型、本地分类器和序列化。 |
| `rag_modules/intent_candidate.py` | 仅在必要时扩展受控枚举；不赋予 LLM 执行字段。 |
| `rag_modules/intent_plan_compiler.py` | 对推荐意图接收/携带 `ConstraintSpec`；继续只生成白名单 `QueryPlan`。 |
| `rag_modules/parent_document_materializer.py` | 聚合方法、工具、步骤数、时间、份量 metadata 并写入来源。 |
| `rag_modules/parent_document_store.py` | 增加按 build 枚举/筛选 Recipe metadata 的只读辅助方法，避免请求路径扫描 Markdown。 |
| `main.py` | 在 planner 后创建 `ConstraintSpec`；扩展硬范围；将 `candidate_k` 传给向量检索；在生成前调用重排。 |
| `rag_modules/restricted_vector_retrieval.py` | 如有需要，区分候选数量与最终数量；保持 parent ID 白名单和 PDS linkage。 |
| `rag_modules/preference_reranker.py` | 新增确定性重排、解释和稳定 tie-break。 |
| `rag_modules/rag_audit.py` / 审计调用点 | 记录需求单、硬范围计数、重排前后候选、分数构成、空集原因。 |
| 测试与考试工件 | 新增单元、集成、回归题和人工候选相关性检查。 |

## 9. 分阶段实施

### 阶段 A：契约与测试先行

- 为 `ConstraintSpec` 和 `PreferenceReranker` 写单元测试。
- 固定 V1 分类矩阵：`只有微波炉`、`必须蒸制`、`清爽一点`、`30 分钟内`、`两人份`、冲突/歧义输入。
- 不改线上检索行为；通过 feature flag 保持关闭。

### 阶段 B：物化属性与工件重建

- 在 PDS metadata 写入聚合属性及来源。
- 重新构建 PDS/Milvus/manifest，验证 chunk 数和 linkage。
- 输出属性覆盖率报告：方法、工具、步骤数、时间、份量各自的已知/未知数量。

### 阶段 C：硬过滤

- 实现方法、工具、时长的 parent ID 范围相交。
- 对空范围实现可解释终止，不进行全库回退。
- 仅开启在测试/allowlist。

### 阶段 D：候选重排

- 将推荐路径改为 `candidate_k=30`、`answer_k=5`。
- 实现 V1 规则重排与审计。
- 保证非推荐意图的结果、排序和延迟行为不变。

### 阶段 E：验收与逐步放量

- 重跑完整 300 题和新的偏好回归集。
- 先对 allowlist 请求观察审计，再按既有 rollout 开关小比例放量。
- 任何硬约束违规、证据链缺失、空答案、工件不一致均自动停用新路径。

## 10. 验收标准

### 10.1 必须通过

- LLM 不能构造检索执行字段，`QueryPlanValidator` 白名单不放宽。
- “只有微波炉”最终候选 100% 含 `MICROWAVE`，且 `recipe_cooking_appliances` 不含其他设备。
- “必须蒸制”最终候选 100% 含 `STEAM`。
- “川菜且蒸制”最终候选 100% 同时满足两项；为空时明确无结果，不混入其他菜系/做法。
- PDS/Milvus build 和 text linkage 全部一致。
- 安全题不产生关系伪造、实体猜测、严格营养或医疗断言。
- 非推荐路径回归不退化。

### 10.2 推荐质量门槛

建立独立的 `S11` 偏好重排题集，至少覆盖：

- 工具：微波炉、电饭煲、蒸锅。
- 做法：蒸、煮、炒、炸的显式限定。
- 多条件：川菜 + 蒸制、晚餐 + 一人份、30 分钟内 + 少步骤。
- 软偏好：清爽、少油感觉、简单、温和口味。
- 空交集和放宽建议。

每题保留 Top30 和最终 Top5 的候选标题、metadata、分数构成。对最终 Top5 做人工相关性标注，单独统计：

```text
硬约束满足率
Top5 严格相关率
Top5 部分相关率
Top5 明显冲突率
无结果解释正确率
P95 总耗时
```

对于“清爽川味蒸菜”，当前召回的麻辣香锅、火锅底料等必须不再出现在最终 Top5；若合格集合无菜，系统应明确返回无完全匹配项。

## 11. 风险、回滚与非目标

- 属性抽取不完整会使硬过滤过度收缩。V1 只对来源可靠的属性执行硬过滤，并报告覆盖率。
- 主观标签误伤风险高。`清爽/少油` 仅用于排序，不作为营养/医疗结论。
- `candidate_k=30` 可能增加向量/PDS 开销；需要记录 P50/P95，并优先只回补重排前所需的最小证据。
- 使用 feature flag 包裹新需求单、硬过滤和重排；默认关闭。关闭后保持现有 planner 路径，不修改旧 Router。
- 本方案不处理个性化画像、医疗营养推荐、跨会话偏好持久化或让 LLM 自行生成检索 DSL。

## 12. 实施顺序

1. 先提交阶段 A 的纯模型、规则和测试。
2. 再提交阶段 B 的 metadata 物化与工件验证。
3. 再提交阶段 C 的硬过滤与空集处理。
4. 最后提交阶段 D 的重排、审计和 S11 题集。
5. 每个独立可验证阶段单独提交、推送并更新同一 PR；完成后执行一次新的单次全量验收，不能以聚合台账替代最终验收。
