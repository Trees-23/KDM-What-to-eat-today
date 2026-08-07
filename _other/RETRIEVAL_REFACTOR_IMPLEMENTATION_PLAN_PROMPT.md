# 给实施方案代理的提示词

你正在为 `What-to-eat-today-main` 编写检索重构的**实施方案**。你的任务是产出可执行、可验收、分阶段推进的计划文档，不是立刻修改运行代码、重建数据库或删除旧模块。

## 必读材料

按顺序完整阅读：

1. `_other/RETRIEVAL_REFACTOR_RESEARCH_PLAN_V2.md`
2. `_other/RETRIEVAL_REFACTOR_RESEARCH_PLAN_V1.md`
3. `_other/handoff.md`
4. `../RETRIEVAL_REFACTOR_HANDOFF.md`（如存在）

然后只在必要范围内阅读这些实现与测试：

- `rag_modules/graph_data_preparation.py`
- `rag_modules/milvus_index_construction.py`
- `rag_modules/hybrid_retrieval.py`
- `rag_modules/graph_rag_retrieval.py`
- `rag_modules/intelligent_query_router.py`
- `rag_modules/generation_integration.py`
- `main.py`
- `config.py`
- `data/cypher/neo4j_import.cypher`
- `docker-compose.yml`
- `test/test_hybrid_retrieval_fusion.py`
- `test/test_router_audit_a4.py`
- `test/test_graph_audit_a6.py`
- `test/test_web_audit_a3.py`

## 总目标

将现有“实体、主题、向量并行召回 + 通用一跳扩展”逐步演进为：

```text
用户问题
-> QueryPlan
-> 实体定位 / 属性过滤 / 受限向量召回 / 目标化图查询
-> node_id、Recipe ID 或 parent_id
-> ParentDocumentStore
-> 图事实与正文证据分层
-> LLM
```

职责边界固定如下：

- Neo4j：关系、稳定 ID、可信结构化属性和受限图查询。
- Milvus：child chunk 的语义召回；不承担全文读取。
- ParentDocumentStore：按 ID 精确返回全文、章节和相邻 chunk。
- LLM：提出受 schema 约束的计划候选、组织已验证的证据；不负责臆测图关系或营养事实。

## 前置门槛

实施方案必须把以下事项列为明确的阶段门槛，而不是写成“后续再看”：

1. 运行中的 Neo4j/Milvus schema 只读核验尚未完成；导入脚本不能替代实例事实。
2. `docker-compose.yml` 中 Neo4j CSV import 目录可能不匹配；在导入、重建或迁移数据前必须验证并修正。
3. Recipe Markdown 到图 CSV 的可复现生产器尚未证实存在；任何全量重建或增量同步前必须补齐。
4. “低脂”严格筛选需要可信营养字段、治理标签或可重复计算；没有这些数据时只能做少油/清爽偏好推荐，不能输出营养学保证。
5. 现有 Milvus 同名重建会删除集合；schema 升级必须使用版本化新集合和显式切换，不能覆盖旧集合。
6. 阶段 0 必须完成无服务依赖测试和运行实例 schema 核验；在阶段 0 未通过前，不得开始后续重构实现。合成 Document 单元测试属于阶段 1 的第一步，不构成跳过阶段 0 的理由。

## 分阶段约束

实施方案必须至少拆为以下顺序，允许细分但不得合并跳过：

1. 环境与回归基线。
2. ParentDocumentStore 的 schema、物化与读取接口。
3. 证据契约、实体直达与生成层分层上下文。
4. QueryPlan 和白名单目标化图查询。
5. 受限向量检索、parent 聚合和 Milvus V2 迁移。
6. 营养/饮食属性与推荐可信度。
7. Recipe 数据生产闭环、离线评测、旧路径逐步下线。

对每个阶段都必须写清：

- 目标与不做什么；
- 进入条件；
- 需要新增、修改或不修改的文件；
- 公开接口、数据 schema 和 ID 映射；
- 数据构建、迁移或重建动作，以及它们是否破坏性；
- 单元测试、集成测试、真实服务检查和明确的测试命令；
- 用户场景验收标准；
- 回退方式和 feature flag；
- 完成定义（Definition of Done）；
- 独立提交与 PR 更新检查点。

实施方案还必须包含一张明确的门槛表：

| 阶段 | 必须满足的前置门槛 | feature flag/切换点 | 回退动作 |
| --- | --- | --- | --- |

其中至少覆盖 ParentDocumentStore、实体直达、QueryPlan/目标化图、Milvus V2 和严格营养模式。Milvus 迁移须写明备份验证、目标 collection 白名单、人工切换确认、旧集合保留和恢复命令。

规则：**一个阶段的实现、测试和验收未全部通过，禁止开始下一阶段。** 禁止用“后续补测试”“先重构再调试”“一次性替换旧链路”规避该规则。

## 必须覆盖的场景

- `宫保鸡丁怎么做？`
- `宫保鸡丁第一步怎么腌？`
- `鸡肉能做什么？`
- `鸡肉搭配什么蔬菜？`
- `推荐低脂川菜`
- `夏天吃什么清淡的？`
- `腌肉有哪些关键要点和适用场景？`
- 实体不存在、图关系不存在、图服务失败时的降级行为。

对“推荐低脂川菜”必须明确两条路径：

```text
有可信营养字段/标签：Neo4j 硬过滤或排序 -> 正文回补。
无可信营养字段：川菜候选 parent_id 过滤 -> Milvus child chunk 语义检索
-> parent 聚合 -> 正文回补；只能称为少油/清爽偏好，不能承诺低脂。
```

对于原问题使用“低脂”而没有硬证据的情况，方案必须规定：可以给出“可能更符合少油清爽偏好”的候选，但必须说明无法验证严格低脂；若用户要求具体营养阈值、严格控脂或医疗饮食，只能返回硬证据匹配项或证据不足。

对于关系问题，方案必须规定：图服务失败时不得使用向量文本当作关系证明；可以明确返回图证据不可用，或把文本结果标注为非关系性烹饪参考。

## 输出要求

创建 `_other/RETRIEVAL_REFACTOR_IMPLEMENTATION_PLAN_V1.md`，使用中文，结构至少为：

```markdown
# 检索重构分阶段实施方案

## 目标与非目标
## 已确认事实与待核验门槛
## 总体架构与数据契约
## 阶段 0：环境与回归基线
## 阶段 1：ParentDocumentStore
## 阶段 2：证据契约与实体直达
## 阶段 3：QueryPlan 与目标化图查询
## 阶段 4：受限向量检索与 Milvus V2
## 阶段 5：营养/饮食属性与推荐
## 阶段 6：数据生产、评测与旧路径迁移
## 测试矩阵
## 迁移、回退与发布策略
## 实施顺序与提交检查点
```

每项关键事实需写出代码文件和行号或具体查询依据。明确区分“已证实”“待环境核验”“需要产品或数据治理决策”。

## 安全边界

- 不递归扫描项目、模型、图片或 `run/` 目录。
- 不重建或删除 Neo4j/Milvus 数据，不创建/执行破坏性迁移。
- 不改动运行代码；本次交付物仅是实施方案 Markdown。
- 不直接删除旧 `hybrid_retrieval.py` 或 `graph_rag_retrieval.py`。
- 不把 parent document 与 child chunk 混入同一无过滤向量召回。

在完成文档后，自检每个阶段是否都有独立的测试、验收和回退边界；若没有，继续细化，不要交付笼统的路线图。
