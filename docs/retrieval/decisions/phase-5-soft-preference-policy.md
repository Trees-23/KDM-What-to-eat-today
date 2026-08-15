# 阶段 5 软偏好治理决定

## 决策

2026-08-09，本项目选择 `nutrition_soft_preference_v1` 软偏好出口。当前仓库及本机图谱/PDS/Milvus 工件没有可审计的 Recipe 级每份脂肪数值、营养来源版本、审核记录、治理饮食标签，或可复算的食材用量与营养库计算链路。

因此，`RETRIEVAL_STRICT_NUTRITION_ENABLED` 必须保持关闭。即使环境变量被设置为 `true`，配置也不会启用严格模式。现有 Markdown、CSV、PDS 正文、Milvus 相似度、rerank 分数及自然语言“低脂”描述都不是可信营养来源，不能用于补造数值、阈值或医疗结论。

## 用户可见策略

- “推荐低脂川菜”在非严格请求下，先以固定 `recipe_cuisine_filter_v1` 模板确认 PDS 提供的川菜候选，再在该 parent scope 内执行 V2 child-chunk 检索、parent 聚合和 PDS hydration。输出只能称为“可能更符合少油/清爽偏好”，并明确不能验证严格低脂。
- 任何脂肪克数、每份阈值、严格控脂、医疗/医嘱/疾病饮食请求都返回 `evidence insufficient`，不展示软偏好候选作为满足条件的推荐。
- Neo4j 或受控川菜范围不可用时，不调用未受限的 Milvus 检索，也不把全库结果称为川菜、低脂川菜或满足营养约束的结果。
- “夏天吃什么清淡的？”不是营养承诺，继续按普通偏好检索处理。

## 审计与升级条件

每个阶段 5 请求记录 `evidence_level`、`policy_version`、`source_status`、`missing_reason` 与 `claim_scope`。严格营养出口只有在单独记录来源、单位、每份定义、阈值、适用人群、审核人、更新规则、过期与冲突处理，并通过 `scripts/validate_nutrition_dataset.py` 和真实 Neo4j 硬过滤验证后才能启用。
