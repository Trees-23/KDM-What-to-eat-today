# 检索重构第二版调研与推进计划

## 1. 文档目的与结论

本文件基于第一版调研和第二轮源码、测试、部署调研，定义从当前检索实现推进到目标体验的建设路线。它不是直接实施说明；实施前应先按本文的前置门槛确认环境和数据事实，再以阶段化方案推进。

核心结论：当前问题不在于缺少更多召回器，而在于命中的图节点、Milvus child chunk 和用户真正需要的完整正文之间没有稳定的回补链路。重构应建立以下职责边界：

```text
Neo4j                 节点、关系、可信结构化属性、关系/路径事实
Milvus                child chunk 的受限语义召回
ParentDocumentStore   按稳定 ID 精确读取全文、章节和相邻 chunk
QueryPlan             按问题意图选择检索步骤
EvidenceBuilder       分开组织图事实与正文证据
LLM                   只基于已组织的证据生成回答
```

目标不是让所有问题走图谱，也不是把全文和 child chunk 无差别混入向量召回。

## 2. 目标用户场景

### 2.1 明确菜名

问题：`宫保鸡丁怎么做？`

```text
Recipe 名称/别名解析
-> Recipe nodeId
-> ParentDocumentStore.get_full_parent(recipe_id)
-> 食材、用量、完整有序步骤
```

不默认执行全库向量检索、主题索引或多跳图遍历。

### 2.2 具体步骤

问题：`宫保鸡丁第一步怎么腌？`

```text
Recipe ID
-> 目标步骤或章节定位
-> 当前步骤/章节 + 相邻步骤 + 必要食材
-> 正文证据
```

### 2.3 食材到菜谱

问题：`鸡肉能做什么？`

```text
Ingredient ID
-> Ingredient <-[:REQUIRES]- Recipe
-> Recipe ID 列表
-> 菜谱摘要；用户要求做法时再读取完整正文
```

### 2.4 食材搭配

问题：`鸡肉搭配什么蔬菜？`

```text
Ingredient ID
-> Ingredient <-[:REQUIRES]- Recipe -[:REQUIRES]-> Ingredient
-> 目标食材及其 Recipe 中介
-> 图事实证据
```

用户语义“搭配”映射为受限路径，而不是假设图中存在名为“搭配”的边。目标食材是否为蔬菜必须依据经确认的结构化分类。

### 2.5 推荐低脂川菜

```text
可信菜系字段过滤：Recipe.cuisineType = 川菜
-> 得到候选 Recipe ID
-> 对这些 parent_id 对应的 child chunk 做受限语义搜索
-> 按 parent_id 聚合和排序
-> 只读取 Top-N Recipe 的正文
-> 按营养/标签/正文证据等级生成推荐
```

“川菜”通常是硬过滤条件；“低脂”取决于数据质量：

| 低脂证据 | 系统行为 | 对用户的表达 |
| --- | --- | --- |
| 每份脂肪、热量等可信数值 | 严格筛选或排序 | 可以说明具体数值或满足的阈值 |
| 人工维护的低脂/少油标签 | 强证据排序 | 可以说明菜谱带有相应标签 |
| 正文中有少油、蒸煮、蔬菜为主等描述 | 只作语义偏好排序 | 只能说明做法偏清爽，不能宣称营养学低脂 |
| 无任何证据 | 不作低脂推荐 | 明确说明资料不足 |

这里的“证据来源”是内部数据契约，不要求向用户生硬地输出“来源是标签/文本”；它的作用是阻止 LLM 把语义相似误说成营养事实。

### 2.6 模糊偏好与技巧知识

`夏天吃什么清淡的？`：无明确实体时，先做全库 child chunk 语义召回，再按 parent_id 聚合并回补。

`腌肉有哪些关键要点和适用场景？`：定位 TechniqueDoc/TechniqueChunk，读取命中章节及相邻章节，保证技巧上下文连续。

## 3. 已确认的代码与数据契约

### 3.1 父子文档

- `GraphDataPreparationModule.build_recipe_documents()` 从 Recipe、`REQUIRES`、`CONTAINS_STEP` 组装 `full_content`；依据：`rag_modules/graph_data_preparation.py:243-356`。
- 该全文只在 `self.documents` 中存在，未见独立持久化；即使 Milvus 集合已存在，`main.py` 仍会在启动时重新组装和切块；依据：`graph_data_preparation.py:49`、`main.py:152-171`。
- 内存 chunk 具有 `chunk_id`、`parent_id`、`chunk_index`、`total_chunks`；`section_title` 只出现在按二级标题切分的分支；依据：`graph_data_preparation.py:466-534`。
- Recipe 和 TechniqueDoc 的 Milvus child chunk 使用各自文档 `node_id` 作为 `parent_id`。TechniqueChunk 是图中的章节节点，先被装配进 TechniqueDoc，再产生新的向量 chunk；它的 `nodeId` 不等于 Milvus `chunk_id`。Ingredient/CookingStep 不存在可直接读取的父文档，必须反查 Recipe；依据：`graph_data_preparation.py:360-440`、`443-534`。

### 3.2 Milvus

- 当前集合 schema 和写入字段为 `id/vector/text/node_id/recipe_name/node_type/category/cuisine_type/difficulty/doc_type/chunk_id/parent_id`；没有 `chunk_index`、`total_chunks`、`section_title` 或 `build_id`；依据：`rag_modules/milvus_index_construction.py:99-112`、`227-240`。
- 当前 `build_vector_index()` 会对同名集合 `force_recreate=True`，因此不能用它直接执行无回退的 schema 迁移；依据：`milvus_index_construction.py:215-217`。
- 当前混合检索以 `node_id` 去重，会合并同一 Recipe 的不同 child chunk，而不是按 parent 聚合；依据：`rag_modules/hybrid_retrieval.py:576-633`。

### 3.3 Neo4j

- 导入脚本定义稳定 ID 属性 `nodeId`，并为 Recipe、Ingredient、CookingStep、TechniqueDoc、TechniqueChunk 建唯一约束；依据：`data/cypher/neo4j_import.cypher:16-20`。
- 预期核心方向为 `Recipe -[:REQUIRES]-> Ingredient`、`Recipe -[:CONTAINS_STEP]-> CookingStep`、`TechniqueDoc -[:HAS_CHUNK]-> TechniqueChunk`；依据：`neo4j_import.cypher:162-193`、`268-284`。
- `BELONGS_TO` 是 CSV 通用关系映射；`BELONGS_TO_CATEGORY` 是由 `category` 属性额外生成的实体到 Category 关系，二者不能混用；依据：`neo4j_import.cypher:195-222`、`286-297`。
- 导入脚本声明全文索引，但当前实例是否存在且可用尚未证实；依据：`neo4j_import.cypher:33-38`。

### 3.4 当前运行链路

- `main.py` 初始化 Hybrid、Graph RAG 和 Router；Router 仅选择 `hybrid_traditional` 或 `graph_rag`；依据：`main.py:102-125`、`intelligent_query_router.py:331-403`。
- BM25 会初始化，但 `hybrid_search()` 实际并行跑实体、主题、向量三路，未使用 BM25；依据：`hybrid_retrieval.py:89-94`、`1122-1265`。
- 多路检索会执行通用一跳邻居扩展；依据：`hybrid_retrieval.py:1090-1120`。
- Graph RAG 的多跳分支使用无方向遍历，关系类型在该分支只是评分信号而非严格白名单；依据：`graph_rag_retrieval.py:313-346`。
- Graph RAG 输出的 Document 缺少稳定 `node_id/parent_id` 元数据，当前无法交给正文回补；依据：`graph_rag_retrieval.py:924-945`、`996-1019`。
- 生成模块只拼接 Document 文本，不能区分图事实和正文证据；依据：`generation_integration.py:162-184`。

### 3.5 后续必须冻结的 ID 与消歧契约

以下规则是目标契约，不是当前已完成实现；阶段 0 必须以真实实例 schema 和样本数据确认具体字段、枚举和别名来源：

| 概念 | 目标稳定标识 | 解析与消歧规则 |
| --- | --- | --- |
| Recipe | `Recipe.nodeId` | 精确名称 -> 别名/同义词 -> Neo4j 全文候选；同分候选不得静默任选，应保留候选或请求澄清 |
| Ingredient | `Ingredient.nodeId` | 与 Recipe 同样的候选解析流程，并限定标签为 Ingredient |
| CookingStep | `CookingStep.nodeId`，并携带所属 Recipe ID | Recipe 内顺序以 `CONTAINS_STEP.stepOrder` 为准，缺失时才使用 `CookingStep.stepNumber`；Markdown 标题不是图中的稳定 ID |
| TechniqueDoc | `TechniqueDoc.nodeId` | 精确名称、标题、标签和全文候选归一 |
| TechniqueChunk | `TechniqueChunk.nodeId`，并携带所属 TechniqueDoc ID | 顺序以 `HAS_CHUNK.chunkOrder` 为准，缺失时使用 `TechniqueChunk.chunkIndex` |
| “蔬菜” | Ingredient 的经确认分类规则 | 阶段 0 必须记录真实 `category` 枚举或分类关系；不得把自然语言“蔬菜”直接硬编码为未验证属性值 |

前端 `recipe_序号` 不属于上述 RAG ID 契约，除非后续单独建立映射表。

## 4. 前置门槛：未完成前不得推进对应重构阶段

### 门槛 A：运行环境与实例 schema

开始任何依赖真实图/向量结果的阶段前，必须完成下列只读检查并记录结果：

```cypher
CALL db.labels();
CALL db.relationshipTypes();
SHOW INDEXES;
MATCH (:Recipe)-[r:REQUIRES]->(:Ingredient) RETURN count(r);
MATCH (:Recipe)-[r:CONTAINS_STEP]->(:CookingStep) RETURN count(r);
MATCH (:TechniqueDoc)-[r:HAS_CHUNK]->(:TechniqueChunk) RETURN count(r);
```

还必须执行 Milvus `describe_collection()` 和 `get_collection_stats()`，确认当前 schema 与数据量。

当前宿主环境缺少 `neo4j`、`pymilvus` Python 包，且本次 `docker compose ps` 无运行服务，所以这项尚未完成。不能把导入脚本当作运行中数据库的事实。

门槛 A 分为两类：

- **A1，本地测试门槛：** 当前无服务依赖的单元测试必须通过。
- **A2，真实服务门槛：** 上述 Neo4j/Milvus 查询必须完成并留档。

阶段 0 的完成定义要求 A1 与 A2 均通过。阶段 1 及之后的重构实现不得在阶段 0 完成前开始；A1/A2 的拆分只用于定位阻塞来源，不代表可以跳过 A2。

### 门槛 B：Neo4j CSV 导入可用性

Compose 中 Neo4j 将具名卷挂至服务器 import 目录，但 CSV 目录挂载到 `/import`；导入脚本使用 `file:///nodes.csv`。在重建或迁移图数据前，必须验证 Neo4j 服务实际能读取 CSV；若不能，先修正卷挂载或复制步骤。依据：`docker-compose.yml:20-24`、`97-119`。

### 门槛 C：Recipe 数据生产闭环

技巧文档已有 Markdown 到 CSV 的可复现生成器，但 Recipe 的原始 Markdown 到 `nodes.csv/relationships.csv` 生成规则没有对应脚本。只要 ParentDocumentStore 以当前 Neo4j 为来源，第一阶段可以推进；但任何“从头重建全部数据”或增量同步方案必须先补齐 Recipe 数据生产器。

### 门槛 D：低脂业务定义

严格低脂推荐必须先决定并落地以下至少一种可信来源：

- Recipe 级每份脂肪/热量等营养字段及阈值；
- 经过治理的人工饮食标签；
- 可重复的“食材用量 + 营养库”计算流程。

如果只有正文描述，功能名称和回答措辞必须限定为“少油/清爽偏好推荐”，不能做严格低脂承诺。

用户可见行为固定为：原问题使用“低脂”但无硬证据时，可以提供“可能更符合少油清爽偏好”的候选，同时明确“现有资料无法验证严格低脂”；若用户要求严格控脂、具体脂肪克数或医疗饮食约束，则只返回有硬证据的菜谱，或明确证据不足。

## 5. 建议的阶段顺序

每个阶段都必须单独完成代码、测试、验证、提交和 PR 更新，再进入下一阶段。不得跨阶段将未验证的数据迁移、路由替换和旧模块删除合并在同一个变更中。

### 阶段 0：环境与回归基线

目标：完成 A1、A2 与门槛 B 的核验，记录真实 schema，冻结 ID/分类映射，固定当前回归测试和评测样本。

通过条件：服务可连接；schema、ID/别名来源、蔬菜分类规则记录入文档；当前单元测试通过；不改检索行为。

### 阶段 1：ParentDocumentStore

目标：新增 SQLite 父子文档物化和读取接口，不接入 Router。阶段 0 完成后，先以合成 Document 建立单元测试，再接入真实 Neo4j 文档物化。

最小 schema：

```text
builds(build_id, source_fingerprint, chunk_config, created_at)
parents(parent_id, node_type, title, full_content, build_id)
chunks(chunk_id, parent_id, chunk_index, total_chunks, section_title, text, build_id)
```

通过条件：Recipe、TechniqueDoc 的全文和窗口读取可由单元测试验证；每个 chunk 能反查父文档；采用临时文件校验后原子发布；不清空 Milvus。

权威来源与版本策略：Recipe 父文档由同一构建会话中的 Neo4j Recipe、Ingredient、CookingStep 物化；TechniqueDoc 由其节点和 HAS_CHUNK 物化。`build_id` 必须由构建器版本、chunk 配置、按稳定 parent_id 排序的全文哈希生成；`source_fingerprint` 记录各 parent 内容哈希。ParentDocumentStore 与当前 Milvus 的 chunk ID/文本一致性没有被验证前，禁止将它接入向量命中后的 hydration。

### 阶段 2：证据契约与实体直达

目标：定义 `EntityCandidate`、`GraphFact`、`TextEvidence`、`EvidenceBundle`；实现菜名/技巧名的精确 ID 直达父文档。

通过条件：明确菜名不调用全局向量搜索；生成层能接收分层证据；找不到实体时保守降级。

### 阶段 3：QueryPlan 与目标化图查询

目标：引入受校验的 QueryPlan，替换默认三路并行和泛化一跳扩展。

通过条件：食材到菜谱、食材搭配、菜谱步骤、技巧章节均使用固定的白名单 Cypher；每个结果保留 node_id、关系路径和来源。Recipe/技巧正文问题的图失败可降级到全文或向量；需要关系证明的问题不得用向量结果证明关系，只能明确返回图证据不可用，或把向量结果标为非关系性参考资料。

### 阶段 4：受限向量检索与 Milvus V2

目标：实现“候选 parent_id 过滤 -> child chunk 召回 -> parent 聚合 -> hydration”；为新集合补齐顺序、章节和 build_id。

通过条件：建立版本化新集合，旧集合保持可用；验证通过后才切换配置；`推荐低脂川菜` 等语义推荐不会检索到不属于已过滤候选的菜谱。

### 阶段 5：营养/饮食属性与推荐可信度

目标：按门槛 D 补齐低脂数据模型、计算或治理流程；将“硬筛选”和“软语义偏好”明确分开。

通过条件：有营养字段时能严格验证阈值；无硬证据时不会输出营养学保证；回答携带可审计证据等级。

### 阶段 6：数据生产、评测与旧路径下线

目标：补齐 Recipe 可复现数据生产，扩展离线评测集，逐步收缩旧 Hybrid/Graph RAG 默认路径。

通过条件：固定场景覆盖 Recipe、步骤、关系、推荐、技巧和失败降级；记录 Recall@K、MRR、证据完整性、答案忠实性和延迟；旧路径只在兼容开关下保留。

## 6. 实施与迁移约束

- 初期不删除 `hybrid_retrieval.py`、`graph_rag_retrieval.py`，新链路应通过独立模块和 feature flag 验证。
- Milvus schema 变更不得覆盖当前集合；使用新 collection 名称和 `build_id`，验证通过后切换。
- ParentDocumentStore 采用版本化构建和原子发布，读取失败应回退旧路径。
- 不使用 `RecipeRecommendationManager` 的按请求 `os.walk` 作为 RAG 回补实现；该接口 ID 与图 ID 不一致，且递归扫描不符合运行约束。依据：`rag_modules/recipe_recommendation.py:200-289`。
- 不将 parent document 与 child chunk 混入同一无过滤向量检索结果集。
- 所有用户可见的“低脂”“营养”等结论必须有结构化数值或治理标签支撑；正文语义只可作为偏好证据。

### 6.1 Feature flag 与回退约定

实施方案应采用明确开关，并在每阶段保留旧路径：

| 阶段 | 建议开关或切换点 | 回退动作 |
| --- | --- | --- |
| ParentDocumentStore | `RETRIEVAL_PARENT_STORE_ENABLED` | 关闭后不读取 SQLite，继续当前检索文本 |
| Entity/证据直达 | `RETRIEVAL_ENTITY_DIRECT_ENABLED` | 回到当前 Router/Hybrid，不删除旧模块 |
| QueryPlan/目标化图 | `RETRIEVAL_QUERY_PLAN_ENABLED`、`RETRIEVAL_TARGETED_GRAPH_ENABLED` | 关闭后使用旧路由；关系问题不得伪造图事实 |
| Milvus V2 | 新 collection 名和显式配置切换 | 将 collection 配置切回旧集合；不删除旧集合 |
| 营养严格模式 | `RETRIEVAL_STRICT_NUTRITION_ENABLED` | 关闭严格声明，只允许偏好推荐或证据不足响应 |

真实数据迁移前必须明确：备份验证方法、允许操作的 collection/database 白名单、构建结果校验、人工切换确认、旧数据保留周期和恢复命令。未经明确确认不得执行清空、覆盖或删除。

## 7. 验收基线

每阶段至少维持并逐步扩展以下场景：

| 场景 | 必需证据 | 预期行为 |
| --- | --- | --- |
| 宫保鸡丁怎么做 | Recipe ID + 父文档 | 完整食材和有序步骤 |
| 宫保鸡丁第一步怎么腌 | Recipe ID + 步骤窗口 | 局部步骤和必要上下文 |
| 鸡肉能做什么 | Ingredient <- REQUIRES - Recipe | 可解释菜谱列表 |
| 鸡肉搭配什么蔬菜 | Ingredient <- Recipe -> Ingredient | 有 Recipe 中介的关系事实 |
| 推荐低脂川菜 | 菜系过滤 + 低脂证据等级 | 不把语义相似伪装为营养事实 |
| 腌肉关键要点 | TechniqueDoc/Chunk 父子关系 | 连续章节正文 |
| 实体/关系不存在 | 降级策略 | 不静默返回空结果 |

现有测试中，混合融合、路由、Web 审计和评测运行器可作为回归基线；本轮已运行 `test_hybrid_retrieval_fusion.py`、`test_router_audit_a4.py`、`test_web_audit_a3.py`、`test_run_eval_queries.py`，共 14 项通过。

## 8. 下一步

下一位 AI 应以本文和第一版交接资料为输入，先写分阶段实施方案，不直接重构代码。实施方案必须将每个阶段的前置条件、变更文件、数据迁移、测试命令、验收条件、回退方式和提交/PR 检查点写清楚；只有当前阶段验收完成，才允许进入下一阶段。
