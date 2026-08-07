# 检索重构第一版调研路线方案

## 1. 文档目的

本文件不是最终技术方案，也不授权直接重写检索代码。它记录当前已经形成共识的重构方向、还未证实的假设，以及后续 AI/开发者应按什么顺序补齐事实。

项目当前的检索把实体级、关系主题级、向量级同时执行，并对很多结果做通用一跳扩展。这让“谁负责定位、谁负责正文、谁负责关系”混在一起。第一版方向是把职责拆开。

## 2. 当前已确认的事实

1. Neo4j 是图数据库，包含 `Recipe`、`Ingredient`、`CookingStep`、`TechniqueDoc`、`TechniqueChunk` 等节点及关系。
2. `rag_modules/graph_data_preparation.py` 会从 Neo4j 把 Recipe、食材、步骤组装为完整菜谱 `full_content`，再切成 chunk。
3. `rag_modules/milvus_index_construction.py` 当前把 child chunk 写入 Milvus，字段包含 `text`、`node_id`、`chunk_id`、`parent_id` 等。
4. 当前 Milvus schema 没有独立的完整父文档记录，也没有保存 `chunk_index`、`total_chunks`、`section_title` 等用于稳定相邻 chunk 回补的字段。
5. 当前 Recipe chunk 构建时，`parent_id` 使用 Recipe 的 `node_id`。这个映射对后续要支持的文档类型仍需核实。
6. `hybrid_retrieval.py` 当前并行执行实体、主题、向量相关逻辑；`BM25Retriever` 会初始化，但当前主搜索不应被误解为已经稳定使用 BM25 主路径。
7. `graph_rag_retrieval.py` 有通用多跳/子图能力，但普通菜谱正文不应依赖它来完整还原。

## 3. 第一版目标架构

```text
用户问题
  → QueryPlan
  → 按意图选择：实体定位 / 属性过滤 / 向量召回 / 目标化图查询
  → 得到 node_id、Recipe ID 或 parent_id
  → ParentDocumentStore 补全文档
  → 图事实与正文证据分层
  → LLM
```

职责边界如下：

| 能力 | 职责 | 不负责什么 |
| --- | --- | --- |
| EntityResolver | 名称、别名、全文候选归一为稳定 ID | 给 LLM 输出大段摘要 |
| MetadataFilter | 菜系、分类、难度、时间、可信标签过滤 | 自然语言关系推理 |
| VectorRetriever | 从 child chunk 中做语义定位 | 决定完整上下文边界 |
| GraphRelationRetriever | 查询明确的图关系、方向和路径 | 代替菜谱正文存储 |
| ParentDocumentStore | 按 ID 读取完整正文、章节、相邻 chunk | 关系推理 |
| EvidenceBuilder | 分开组织结构化事实与正文证据 | 再做检索决策 |

### 3.1 问题类型与建议路径

| 问题 | 建议路径 |
| --- | --- |
| `宫保鸡丁怎么做？` | 实体解析 → Recipe ID → 完整父文档 |
| `宫保鸡丁第一步怎么腌？` | 实体解析 → Recipe/parent ID → 步骤章节、相邻上下文、必要食材 |
| `鸡肉能做什么？` | Ingredient ID → Neo4j 目标化关系查询 → Recipe ID → 菜谱摘要/正文 |
| `鸡肉搭配什么蔬菜？` | Ingredient ID → `Ingredient ← Recipe → Ingredient` 的受约束路径 → 图事实 |
| `推荐低脂川菜` | 可靠属性先过滤 → 向量语义召回 → 按父文档聚合 |
| `夏天适合吃什么清淡的菜？` | 向量召回 → `parent_id` 回补 |

### 3.2 需要降级的旧策略

- 不再默认并行执行“实体级 + 主题级 + 向量级”。
- 不再对每个候选无差别执行 `MATCH (n)-[r]-(neighbor)`。
- 不再让 `RelationKeyValue` 的手工主题关系词承担主要主题检索能力。
- 不再把任意 `[*1..3]` 多跳查询作为关系检索的默认实现。

实体词典可保留为精确/别名匹配缓存；手工关系主题索引可以保留为优化，但不作为主要架构能力。

## 4. 父文档存储：当前假设与待决策项

`parent_id` 只是定位键，不是完整父文档。当前系统能够在构建索引时生成 `full_content`，但没有确认它被独立持久化。

当前有三种可行方向，尚未最终定案：

| 方案 | 做法 | 优点 | 风险/代价 |
| --- | --- | --- | --- |
| A. Neo4j 即时组装 | 已知 Recipe ID 后读取 Recipe、食材、步骤并重新拼装 | 不新增存储，数据结构单一 | 每次读取正文都要查图和拼文本 |
| B. SQLite 父文档表 | `parent_id → full_content / sections / chunk 顺序` | 按 ID 精确读取，简单、易检查，不污染向量检索 | 新增一个本地持久化文件和构建步骤 |
| C. 单独 Milvus 父文档集合 | child collection 只做向量；parent collection 按 ID filter/read | 不增加新的服务类型 | Milvus 是向量库，精确正文读取不是其最自然职责 |

第一版偏向 **B：SQLite 父文档表**。理由是父文档主要按 ID 精确读取，SQLite 不需要额外服务，且能存完整正文、章节和 chunk 顺序。这个选择需要在确认部署方式、并发要求、数据规模后再锁定。

无论选哪一种，禁止把父文档和 child chunk 无过滤地放在同一条向量召回中。父文档的访问模式应是：

```text
child chunk 命中 / Recipe ID 命中
→ 得到 parent_id
→ 按 ID 精确读取父文档
```

而不是“再对父文档做一次随机向量召回”。

## 5. 调研路线

### 阶段 A：建立事实基线

目标：确认当前数据和调用边界，而不是先改代码。

需要确认：

1. `Recipe`、`Ingredient`、`CookingStep` 的真实标签、属性、关系名称和方向。
2. `node_id`、`parent_id`、Milvus 主键、chunk ID 的实际映射。
3. Milvus 是否支持并已保存按父文档回补所需字段；如没有，补字段是否需要全量重建索引。
4. 完整父文档是否只在索引构建进程内存在，还是已有可复用的持久化来源。
5. 当前 API/CLI 的真实入口、上下文组装位置、审计和评估用例。

交付物：一份“已验证的数据契约”，不修改运行逻辑。

### 阶段 B：做父文档方案决策

目标：选定 ParentDocumentStore 的实现，不凭印象决定。

比较维度：

- 按 Recipe ID 读取完整菜谱的延迟；
- 是否能按章节、步骤和 chunk 窗口读取；
- 索引重建和数据更新是否可重复；
- 是否增加部署复杂度；
- 多进程/多机器运行时是否可用；
- 与现有 Neo4j、Milvus 的数据一致性和故障恢复方式。

交付物：一页 ADR，明确选型、数据 schema、构建时机、重建命令和回退方式。

### 阶段 C：设计最小 QueryPlan 与实体解析

建议最小模型：

```python
QueryPlan(
    intent,            # recipe_content / relation / recommendation / technique / factual
    entity_mentions,
    filters,
    relation_request,
    content_need,
)
```

实体解析先采用：

```text
精确名称 → 别名 → Neo4j 全文或 BM25 兜底 → 候选 ID + 分数
```

BM25 在这里是“词面候选召回的可能实现”，不是必须新增的一条全局主检索链。先核实现有 Neo4j 全文索引、词典规模和错误案例，再决定是否增加应用侧 BM25 或 Milvus 稀疏向量。

交付物：实体解析输入/输出契约、候选阈值与歧义处理策略。

### 阶段 D：设计目标化图查询

目标：保留图谱真正有价值的场景，不再泛化扩展邻居。

最小查询模板：

| 意图 | 约束关系查询 |
| --- | --- |
| 某菜有哪些食材 | `Recipe -[:REQUIRES]-> Ingredient` |
| 某菜有哪些步骤 | `Recipe -[:CONTAINS_STEP]-> CookingStep`，按步骤序号 |
| 某食材能做什么 | `Ingredient <-[:REQUIRES]- Recipe` |
| 食材搭配 | `Ingredient <-[:REQUIRES]- Recipe -[:REQUIRES]-> Ingredient` |
| 技巧章节 | `TechniqueDoc -[:HAS_CHUNK]-> TechniqueChunk` |

真实关系名称、方向和属性必须按阶段 A 的导入数据/Neo4j 实例验证后确定。

交付物：白名单 Cypher 模板、参数 schema、最大跳数约束、失败兜底规则。

### 阶段 E：渐进迁移

不要直接删除旧模块。建议新增一套小模块，先在受控入口按 feature flag 或测试入口运行：

```text
rag_modules/retrieval/
  models.py
  query_planner.py
  entity_resolver.py
  parent_document_store.py
  vector_retriever.py
  graph_relation_retriever.py
  evidence_builder.py
  orchestrator.py
```

旧模块映射：

| 现有文件 | 迁移后的去向 |
| --- | --- |
| `intelligent_query_router.py` | 逐步收缩为 QueryPlan 入口/兼容适配器 |
| `hybrid_retrieval.py` | 拆出实体解析、向量检索、rerank；移除默认三路并行和通用一跳 |
| `graph_rag_retrieval.py` | 保留为复杂关系/路径能力，新增白名单目标化查询 |
| `graph_data_preparation.py` | 扩展为父文档与 child chunk 的可重复物化 |
| `milvus_index_construction.py` | child schema 补齐回补字段，支持按 parent 过滤 |
| `main.py` | 最终只初始化组件并调用 Orchestrator |

## 6. 先后顺序和验收问题

推荐实施顺序：

```text
事实基线
→ ParentDocumentStore
→ EntityResolver
→ QueryPlan + Orchestrator
→ 目标化图查询
→ 推荐/向量整合
→ 旧三路并行下线
```

每个阶段至少验证：

1. `宫保鸡丁怎么做？`：能通过 Recipe ID 取到完整食材和有序步骤。
2. `宫保鸡丁第一步怎么腌？`：能取到目标步骤及必要上下文。
3. `鸡肉能做什么？`：走一条明确的 Ingredient 到 Recipe 关系。
4. `鸡肉搭配什么蔬菜？`：只返回有 Recipe 中介的关系证据。
5. `推荐低脂川菜`：先应用可靠菜系过滤，再进行语义召回。
6. 找不到实体或图关系时：能降级到向量/全文或明确返回证据不足，不静默空结果。

## 7. 当前不应做的事情

- 未核实 schema 前，不要直接改写或删除 `hybrid_retrieval.py`、`graph_rag_retrieval.py`。
- 不要把“父文档存 Milvus”理解为必须让 parent 与 child 一起参与向量召回。
- 不要在没有关系白名单的前提下开放任意长度多跳 Cypher。
- 不要因为当前有 `parent_id` 就假设已经支持父文档 hydration。
- 不要把所有模糊表达都强行转换成图关系；低脂、清淡、夏天等通常优先走属性/语义能力。

## 8. 下一位 AI 的第一任务

先阅读 `handoff.md` 与本文件，再以只读、窄范围检查完成阶段 A，并写一份事实确认报告。报告必须把“代码中已证实的事实”“仍是设计假设”“需要用户决定的选项”分开写。
