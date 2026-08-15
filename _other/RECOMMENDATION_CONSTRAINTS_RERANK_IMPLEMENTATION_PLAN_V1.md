# 推荐约束与重排实施方案 V1

## 1. 目的

解决 `PREFERENCE_RECOMMEND` 路径中“模型识别出了工具、做法、时长等条件，但候选仍不满足用户明确限制”的问题。

目标流程：

```text
用户问题
  -> IntentPlanner: IntentCandidate（意图 + 槽位）
  -> RecommendationConstraintCompiler: ConstraintSpec（本地决定条件强弱）
  -> ResolvedCandidateScope（活动 PDS build 内的硬过滤 parent_id）
  -> 受限向量召回 Top30 候选元数据
  -> 本地确定性重排
  -> 回补最终 Top5 PDS 正文
  -> 生成回答
```

LLM 只识别“用户提到了什么”；本地代码只根据真实用户原话决定“这是参考条件还是必须遵守的限制”。LLM 不得输出 Cypher、Milvus filter、实体 ID、`parent_id`、权重、排序表达式或 `QueryPlan`。

## 2. 当前问题与范围

现有路径能稳定用菜系和具名食材缩小候选范围，但工具、做法、人数、时长和口味主要依赖向量相似度。因此“只有微波炉”“必须蒸制”可能仍得到依赖其他设备或炸制的菜谱。

V1 覆盖：菜系、唯一解析的具名食材、工具、烹饪设备、做法、总时长、份量、餐次、`LIGHT_FEEL`、`FEW_STEPS`。

V1 不做：营养、医疗、个性化画像、跨会话偏好、LLM 检索 DSL。`清爽`、`少油感觉`、`温和`不能被表述为低脂、低热量、医疗适用。

## 3. 条件分类规则

### 3.1 职责边界

- `IntentCandidate` 只提供受控槽位，例如 `MICROWAVE`、`STEAM`、`STIR_FRY`。
- `RecommendationConstraintCompiler` 同时读取可信用户原话和已校验槽位；槽位本身不带“必须/不要”的执行权限。
- 工具和做法默认是软偏好。只有本地文本规则识别到明确限制，才成为硬过滤。
- 菜系与唯一解析的具名食材继续复用当前已验证范围；`30 分钟内`等可解析上限属于硬过滤；份量、餐次和主观口感在 V1 一律是软偏好。

### 3.2 明确限制词

本地规则至少覆盖下列形式，并记录命中的原始词、字段和判定结果：

| 用户表达 | 工具/做法执行方式 |
| --- | --- |
| `只`、`仅`、`只能`、`只有`、`只用`、`必须` | 正向硬约束 |
| `不要`、`不能`、`不得`、`完全不要`、`不使用` | 排除硬约束 |
| `优先`、`尽量`、`也行`、`最好`、`想试试` | 软偏好 |
| 无上述明确限制词 | 软偏好 |

“家里只有微波炉”属于排他性硬约束，即使没有“必须”二字。否定、排他和对象无法可靠配对时返回澄清，绝不猜测。

### 3.3 做法语义

V1 受控做法为 `STEAM`、`BOIL`、`FRY`、`STEW`、`STIR_FRY`。需要同步扩展 `IntentSlots`、planner 提示词、图步骤归一化和 PDS 物化；`炒`、`煸炒`、`爆炒`等本地映射到 `STIR_FRY`。

| 用户表达 | 硬规则 |
| --- | --- |
| `必须蒸` | 包含 `STEAM` |
| `只蒸` | 包含 `STEAM`，并排除所有明确冲突做法（V1 至少 `FRY`、`STIR_FRY`） |
| `不要炸` | 排除 `FRY` |
| `必须炒` | 包含 `STIR_FRY` |

“蒸菜也行”“优先蒸”等仍是软偏好。多条条件互相矛盾时返回澄清。

## 4. 本地数据模型

新增 `rag_modules/recommendation_constraints.py`：

```python
@dataclass(frozen=True)
class HardRecipeFilters:
    cuisines: tuple[str, ...] = ()
    verified_ingredient_ids: tuple[str, ...] = ()
    methods: tuple[str, ...] = ()
    excluded_methods: tuple[str, ...] = ()
    required_cooking_appliances: tuple[str, ...] = ()
    excluded_cooking_appliances: tuple[str, ...] = ()
    max_total_minutes: int | None = None

@dataclass(frozen=True)
class SoftRecipePreferences:
    methods: tuple[str, ...] = ()
    tools: tuple[str, ...] = ()
    preferences: tuple[str, ...] = ()
    meal_context: tuple[str, ...] = ()
    prefer_shorter_time: bool = False
    target_servings: int | None = None

@dataclass(frozen=True)
class ConstraintSpec:
    intent: str
    hard_filters: HardRecipeFilters
    soft_preferences: SoftRecipePreferences
    clarification_reason: str | None = None
    policy_version: str = "recommendation_constraints_v1"

@dataclass(frozen=True)
class ResolvedCandidateScope:
    build_id: str
    parent_ids: tuple[str, ...]
    hard_filter_counts: Mapping[str, int]
```

`ResolvedCandidateScope` 是纯本地对象，不能由 LLM 创建或修改。具名食材仅在 `EntityResolver` 唯一解析后才写入 `verified_ingredient_ids`。

## 5. PDS 属性物化

修改 `parent_document_materializer.py`，为 Recipe 父文档写入受控、可追溯 metadata：

```json
{
  "recipe_methods": ["STEAM", "STIR_FRY"],
  "recipe_tools": ["微波炉", "碗"],
  "recipe_cooking_appliances": ["MICROWAVE"],
  "recipe_optional_cooking_appliances": [],
  "unknown_cooking_appliance": false,
  "step_count": 4,
  "prep_minutes": 6,
  "cook_minutes": 15,
  "total_minutes": 21,
  "servings_count": 1,
  "attribute_provenance": {
    "recipe_methods": "graph_step.methods",
    "recipe_cooking_appliances": "graph_step.tools"
  }
}
```

规则：

- `recipe_tools` 保留原始可追溯工具；`recipe_cooking_appliances` 仅包含直接烹饪设备，刀、碗、筷子、案板不在其中。
- 必须区分必需设备、可选/替代设备和未知设备。数据无法判断时标记未知，不伪造结论。
- “只能用微波炉”通过条件：包含 `MICROWAVE`、已知必需烹饪设备集合是 `{MICROWAVE}` 的子集、且没有未知必需设备。可选替代设备不构成冲突。
- 方法和设备必须使用与 `IntentSlots` 对应的受控枚举；无法映射的原始文本保留在 provenance，不进入受控字段。
- `step_count` 来自 Recipe 步骤聚合；`total_minutes`、`servings_count` 解析失败时为 `null`，绝不以正文或 `0` 猜测。

metadata 变动必须重建 PDS、Milvus V2 和联合 manifest，并运行 PDS/Milvus linkage 校验与属性覆盖率报告。

## 6. 硬范围与数量边界

`ParentDocumentStore` 新增活动 build 的只读 Recipe metadata 枚举/筛选接口；请求路径不得扫描 Markdown 或提前读取全文。

1. 菜系、已验证食材、正向方法/设备、排除方法/设备、时长在活动 PDS build 内取集合交集/差集。
2. 缺少硬属性的菜谱视为不满足该硬条件；软偏好中属性未知则保留但不加分。
3. 空交集返回 `NO_PREFERENCE_RESULTS`，说明哪些限制没有同时满足，并给出一次放宽方向；不得退回全库。
4. `max_hard_scope` 默认 200，做成配置项。`<= 30` 的范围全部进入重排；`31..200` 在完整范围内向量选 Top30；`> 200` 返回“条件仍过宽，请增加一个条件”。
5. 旧 `QueryPlanValidator.MAX_CANDIDATES=50` 不能再阻止 51..200 的本地硬范围。实现时只提高推荐白名单的受控容量，不新增模板、字段、LLM 输入或任意查询能力。
6. 检索分批时必须合并所有批次的候选，再统一选全局 Top30，禁止按批次先截断造成排序偏差。

## 7. 两段式召回与重排

```text
candidate_k = 30
answer_k = 5
```

- 使用完整可信用户问题进行向量查询。
- 第一段只返回 `parent_id`、标题、检索分数和 Recipe metadata；不回补 30 篇完整正文。
- `PreferenceReranker` 对 Top30 确定性排序；第二段只为最终 Top5 回补 PDS 全文作为生成证据。
- 范围小于 30 时，全部范围进入重排；最终答案最多返回 5 项。

新增 `rag_modules/preference_reranker.py`。评分表版本固定为 `recommendation_rerank_v1`：

| 项目 | 规则 | 分值 |
| --- | --- | --- |
| 基础检索分 | 本批 `retrieval_score` min-max 到 `[0, 1]`；相同为 `0.5` | `70 * normalized_score` |
| `LIGHT_FEEL` 正向 | 含 `STEAM` 或 `BOIL`，且不含 `FRY` | `+10` |
| `LIGHT_FEEL` 冲突 | 含 `FRY` | `-20` |
| `FEW_STEPS` | `step_count <= 6` | `+6` |
| `FEW_STEPS` 时长 | `total_minutes <= 25` | `+6` |
| `FEW_STEPS` 反向 | `total_minutes > 60` | `-6` |
| 目标份量 | 精确匹配 | `+4` |
| 邻近份量 | 相差 1 | `+1` |

审计必须分开保存 `best_chunk_score`、`coverage_bonus`、`retrieval_score`、重排 bonus/penalty、`final_score`、属性来源与未知字段。排序相同依次使用 `retrieval_score`、`parent_id` 作为稳定 tie-break。

## 8. 故障与回退

不实现“单次异常自动关闭全局功能”。功能开关继续由部署配置控制。

- 硬范围为空：仅本次回复无完全匹配和一次放宽建议。
- metadata、PDS、Milvus 或工件不一致：仅本次请求不声称满足硬条件，返回受控不可用说明并记录告警。
- 重排器失败但硬过滤和受限检索成功：可按原始受限向量顺序返回，明确记录 `rerank_unavailable`；不得放宽硬条件。
- 所有异常保留审计，后续请求仍可尝试新路径。

## 9. 实施阶段

### 阶段 A：契约、文本分类与单元测试

- 增加 `STIR_FRY` 及本地强度/否定/排他解析。
- 测试工具、做法从软偏好升级为硬约束的完整矩阵。
- 新 feature flag 默认关闭。

### 阶段 B：属性物化与工件校验

- 物化方法、原始工具、必需/可选设备、未知状态、步骤数、时间、份量与来源。
- 重建 PDS/Milvus/manifest，验证 linkage 和字段覆盖率。

### 阶段 C：硬范围和两段式检索

- 实现 `ResolvedCandidateScope`、`max_hard_scope=200`、全局 Top30 合并。
- 第一段仅取 metadata，第二段只回补 Top5 正文。

### 阶段 D：重排、审计与验收卷

- 实现确定性重排和降级。
- 完成 `_other/考试/推荐约束与重排验收-V1/` 的 18 题独立验收卷。
- 不要求运行旧 300 题全量考试。

## 10. 验收

最终验收只运行本方案专用的 18 题试卷、相关单元测试和集成测试。硬约束、安全边界与软偏好分开判定；具体门槛见专用试卷的 `评分与验收标准.md`。

必须满足：LLM 没有执行权、硬约束不被向量高分绕过、PDS/Milvus linkage 一致、非推荐路径不回归、严格营养/医疗结论不被伪造。
