# 给下一位 AI 的提示词：继续检索重构调研

你正在接手 `What-to-eat-today-main` 的检索重构调研。当前只有第一版架构方向，不代表所有细节已经确认。你的第一职责是**验证关键事实、收敛选型和提出可执行的小步计划**，不是立即大范围重写代码。

## 阅读顺序

1. `_other/handoff.md`
2. `_other/RETRIEVAL_REFACTOR_RESEARCH_PLAN_V1.md`
3. `../RETRIEVAL_REFACTOR_HANDOFF.md`（如该文件存在）
4. 下列指定代码文件：
   - `rag_modules/graph_data_preparation.py`
   - `rag_modules/milvus_index_construction.py`
   - `rag_modules/graph_indexing.py`
   - `rag_modules/hybrid_retrieval.py`
   - `rag_modules/graph_rag_retrieval.py`
   - `rag_modules/intelligent_query_router.py`
   - `main.py`
   - `data/cypher/neo4j_import.cypher`

## 已形成的方向

目标不是“让所有问题都走图谱”，而是分工：

```text
Neo4j：节点、关系、结构化属性、关系/路径查询
Milvus：child chunk 的语义检索
ParentDocumentStore：按 parent_id 精确读取完整正文或章节
```

预期主链：

```text
用户问题
→ QueryPlan
→ 实体定位 / 属性过滤 / 向量召回 / 目标化图查询
→ node_id、Recipe ID 或 parent_id
→ 父子文档补全
→ 图事实与正文证据分层
→ LLM
```

关键原则：

- 明确菜名：定位 Recipe ID 后直接取父文档，不默认向量检索或多跳图检索。
- 明确食材且问关联：先定位 Ingredient ID，再走精确关系查询。
- 模糊推荐：可靠属性过滤 + 向量语义召回，不依赖手工关系主题 Key。
- Graph RAG 只服务关系、多跳、路径问题；图查询的 Recipe ID 可再用于取正文。
- `parent_id` 是指针，不等于父文档内容。
- 父文档不能与 child chunk 无过滤地混进同一个向量召回结果集。

## 你的第一轮任务：只读调研与报告

请按下面顺序推进，不做实现修改：

1. **验证父子数据契约。**
   - `full_content` 在哪里生成？是否被持久化？
   - Milvus 实际 schema 有哪些字段？是否保存 `chunk_index`、`total_chunks`、`section_title`？
   - `node_id`、`parent_id`、`chunk_id` 的映射对 Recipe、TechniqueDoc、TechniqueChunk 是否一致？

2. **验证 Neo4j 图 schema。**
   - `REQUIRES`、`CONTAINS_STEP`、`BELONGS_TO`、`HAS_CHUNK` 的真实名称、方向、属性。
   - `Recipe`、`Ingredient`、`CookingStep` 的稳定 ID 字段和是否已有全文索引。
   - 能否用受控 Cypher 实现“鸡肉能做什么”“鸡肉搭配什么蔬菜”。

3. **验证当前运行链路。**
   - `main.py` 如何初始化和调用 router、hybrid、graph RAG。
   - 当前 `BM25Retriever` 是否真的参与主路径。
   - 当前实体/主题/向量如何合并，通用一跳查询在哪里发生。

4. **比较 ParentDocumentStore 方案。**
   - Neo4j 即时组装；
   - SQLite 父文档表；
   - 单独 Milvus 父文档集合。
   - 从读取方式、部署复杂度、重建、章节读取、并发与数据一致性比较。

5. **给出下一步最小实现切片。**
   - 只提出可独立验证的一小步，优先 ParentDocumentStore 的 schema、构建流程和读取接口。
   - 明确需要改的文件、新增的测试、重建或迁移动作。

## 输出格式

先输出一份中文调研报告，按以下结构：

```markdown
# 检索重构事实确认报告

## 已验证事实
## 与第一版假设不一致的地方
## 未确认项与最小验证方法
## ParentDocumentStore 选型比较
## 建议的下一步最小实现
## 风险与回退
```

每条事实必须注明代码文件和行号或具体 schema/查询依据。明确区分：

- 已在代码或数据库中证实；
- 合理但尚未证实；
- 需要用户作出产品/部署选择。

## 安全与范围约束

- 用户的 WSL 曾在递归扫描大型目录时崩溃。禁止对整个项目做递归 `find`、`du`、全量哈希、扫描模型/图片/`run/` 目录。
- 只读取上述指定的小型文本文件、Git 元数据，或用户明确许可的最小数据库查询。
- 先做只读调研；除非用户明确要求实施，否则不要修改代码、重建 Milvus、清空集合、导入/删除 Neo4j 数据。
- 不要假设现有 `parent_id` 已经可以回补正文；必须先验证。
- 不要把自然语言“搭配”误当作 Neo4j 中存在的同名边；需要把它映射为真实、受限的关系路径。

## 与用户沟通

用中文、先给结论后给证据。不要只说“可以做”；要明确说明当前代码是否已经支持、缺什么、下一步最小改动是什么。
