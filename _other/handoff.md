# 检索重构调研交接

## 当前状态

本仓库尚未实施新的检索架构。本次交接只新增三份设计/调研文档，没有改动运行代码、Neo4j 数据或 Milvus 数据。

当前分支上的目标是：先验证数据契约和存储选型，再以小步方式把当前“并行三路召回 + 泛化一跳扩展”迁移为“计划驱动 + 父子文档补全 + 目标化图查询”。

配套文档：

- `_other/RETRIEVAL_REFACTOR_RESEARCH_PLAN_V1.md`：第一版方向、调研路线、待决策项。
- `_other/RETRIEVAL_REFACTOR_RESEARCH_PROMPT.md`：给下一位 AI 的接手提示词与只读调研任务。
- `../RETRIEVAL_REFACTOR_HANDOFF.md`：更完整的现状分析与目标架构说明（如存在）。

## 已观察到的代码事实

### 数据准备与向量索引

`rag_modules/graph_data_preparation.py`：

- 从 Neo4j 读取 Recipe、食材和步骤；
- 通过关系组装完整 Recipe `full_content`；
- 再将完整文档切为 child chunk；
- Recipe chunk 的 `parent_id` 当前取 `doc.metadata["node_id"]`。

`rag_modules/milvus_index_construction.py`：

- Milvus child collection 包含 `id`、`vector`、`text`、`node_id`、`recipe_name`、`node_type`、分类/菜系/难度、`chunk_id`、`parent_id`；
- chunk 的正文保存于 `text`；
- 当前 schema 中未见 `chunk_index`、`total_chunks`、`section_title`；
- 因此即使按 `parent_id` 找到所有 child chunk，也尚未具备可靠的章节读取与相邻窗口回补契约。

结论：当前 `parent_id` 是关联键，不是可直接读取的父文档存储。

### 当前检索链路

`main.py` 初始化：

- `HybridRetrievalModule`；
- `GraphRAGRetrieval`；
- `IntelligentQueryRouter`。

`intelligent_query_router.py` 当前主要在 `hybrid_traditional` 与 `graph_rag` 之间选择。

`hybrid_retrieval.py` 当前存在：

- 实体关键词提取和实体索引；
- 关系主题关键词与关系索引；
- Milvus 向量检索；
- 对多个结果的通用一跳邻居补充、合并、去重、可选 rerank。

虽然该模块会初始化 `BM25Retriever`，但不能据此假设 BM25 已成为稳定主检索链；需要继续核对实际 `hybrid_search()` 调用路径。

`graph_rag_retrieval.py` 当前支持多跳/子图类检索，但通用路径输出更适合关系事实，不能保证普通 Recipe 的完整正文。

## 已形成的架构方向

```text
用户问题
→ QueryPlan
→ 实体解析 / 属性过滤 / 向量检索 / 目标化图查询
→ node_id、Recipe ID 或 parent_id
→ ParentDocumentStore
→ 图事实 + 正文证据
→ LLM
```

### 分工

| 组件 | 应负责的事情 |
| --- | --- |
| Neo4j | 图节点、关系、属性过滤、关联/路径查询 |
| Milvus | child chunk 的语义召回 |
| ParentDocumentStore | 根据 parent ID 精确读取完整菜谱、章节或 chunk 窗口 |
| EntityResolver | 名称/别名/全文候选归一为稳定 ID |
| GraphRelationRetriever | 仅运行白名单、方向和跳数受控的图查询 |

### 典型流程

```text
宫保鸡丁怎么做？
→ Recipe ID
→ ParentDocumentStore
→ 完整菜谱
```

```text
鸡肉能做什么？
→ Ingredient ID
→ Ingredient ←[:REQUIRES]- Recipe
→ Recipe ID
→ 菜谱摘要或正文
```

```text
鸡肉搭配什么蔬菜？
→ Ingredient ID
→ Ingredient ←[:REQUIRES]- Recipe -[:REQUIRES]→ Ingredient
→ 图关系证据
```

## 待确认，不能当作事实

1. ParentDocumentStore 最终是否使用 SQLite、Neo4j 即时组装，或独立 Milvus parent collection。
2. Neo4j 实例中全部关系名称、方向、属性是否与 CSV 导入脚本完全一致。
3. 生产环境是否存在可用的 Neo4j 全文索引，以及是否需要额外引入 BM25/稀疏向量。
4. `parent_id` 是否对所有文档类型都等于稳定 `node_id`。
5. 低脂、清淡、适合夏天等业务概念是否有可信结构化字段，还是只可语义近似。
6. 增量构建、删除、重建时，Neo4j、Milvus、ParentDocumentStore 如何保持一致。

## 建议下一步

严格按 `_other/RETRIEVAL_REFACTOR_RESEARCH_PLAN_V1.md` 的阶段 A 做窄范围只读确认。优先确认：

1. 父文档能否重建/读取；
2. parent-child 元数据缺哪些字段；
3. 图关系的真实方向；
4. 现有入口和测试覆盖；
5. 再输出 ParentDocumentStore 的选型 ADR 和最小实施切片。

不要先删除旧的 `hybrid_retrieval.py` 或 `graph_rag_retrieval.py`，也不要直接重建数据。新链路应先以独立模块和测试入口验证，再替换主入口。
