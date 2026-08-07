# 检索重构分阶段实施方案

## 目标与非目标

### 目标

在不一次性替换现有检索链路的前提下，把当前“实体、主题、向量并行召回 + 通用一跳扩展”演进为下列可审计链路：

~~~text
用户问题
  -> QueryPlan（受 schema 约束并校验）
  -> 实体定位 / 属性过滤 / 受限 child-chunk 向量召回 / 目标化图查询
  -> node_id、Recipe ID 或 parent_id
  -> ParentDocumentStore
  -> 图事实与正文证据分层
  -> LLM
~~~

职责边界固定如下：

| 组件 | 负责 | 明确不负责 |
| --- | --- | --- |
| Neo4j | 稳定 ID、关系、可信结构化属性、固定模板的图查询 | 全文读取、任意 LLM 生成的 Cypher |
| Milvus | child chunk 的语义召回，以及按 parent_id 的受限检索 | 全文读取、关系证明、营养事实判断 |
| ParentDocumentStore | 按稳定 ID 精确返回全文、章节、锚点和相邻 chunk | 无过滤语义召回、图关系推理 |
| QueryPlan / EvidenceBuilder | 验证意图、选择白名单操作、保留证据来源与缺失状态 | 补造实体、关系或营养事实 |
| LLM | 在已验证的图事实和正文证据上组织回答 | 臆测图关系、把相似文本说成营养事实 |

### 非目标

- 不在任一阶段删除或直接重写旧的 hybrid_retrieval.py、graph_rag_retrieval.py。
- 不把 parent document 与 child chunk 放入同一个无过滤的向量召回集合。
- 不把导入脚本、CSV 或代码中的预期 schema 当作运行中 Neo4j/Milvus 的事实。
- 不在没有可信营养字段、治理标签或可复算链路时承诺“低脂”。
- 不在本方案实施期间执行 Neo4j/Milvus 重建、清空或同名集合覆盖；数据操作只在相应阶段的审批、备份和白名单通过后执行。

### 持续执行授权与终止条件

本方案授权执行代理从阶段 0 持续推进至阶段 6，而不是在提交计划、单个模块、单次测试或单个 PR 更新后等待用户确认。下列常规工作均已授权：阅读当前阶段所需代码、创建本阶段模块/测试/脚本/文档、修复当前阶段的回归、建立隔离测试夹具、运行测试和只读诊断、构建非破坏性 staging 产物、提交、推送、创建或更新同一 PR、执行实施方案规定的 staging 验收与回退演练。

代理应在当前阶段 DoD 通过后立即开始下一阶段，不询问命名、模块拆分、测试组织、feature flag 默认值、提交时机或 PR 更新等常规实现选择；应采用本方案和现有代码中最保守且可回退的做法。最终成功条件是阶段 6 DoD 通过，十个固定场景、三类失败降级、离线评测、staging 用户场景验收、回退演练和 PR 证据全部完成。

自主执行不放宽任何阶段门槛，也不授权伪造实例事实、跳过测试、覆盖用户改动、合并 main、删除旧数据或绕开受保护审批。遇到测试失败、依赖缺失或当前阶段实现缺陷时，代理必须自行诊断、最小修复、补充测试并重跑，而不能将它们作为向用户询问或提前停止的理由。只有下列不可由本地代码解决的外部条件才构成阻塞：没有已授权的真实服务/数据目标、运行实例事实与冻结契约实质冲突、受保护切换审批记录缺失、或数据治理决策尚未存在。此时代理仍须完成所有安全的本地与 staging 工作、提交诊断和证据，并在可用的监控/重试机制中继续检查外部状态；不得以模拟数据或未批准的破坏性操作假装推进。

每个阶段的“审核通过”采用可自主执行的独立审查签收：执行代理在推送该阶段提交后，启动一个不继承实现上下文、不会修改工作区的独立审查代理，向其提供该阶段 diff、测试/服务证据、实施方案章节和 PR 链接。审查代理必须在 docs/retrieval/reviews/phase-<n>-<commit>.md 记录审查身份、输入 commit、通过/不通过结论、发现项与时间；不通过即由执行代理修复并重审。该签收满足阶段间的 PR 审核门槛，但不替代 main 合并审批，也不替代受保护环境切换审批。

## 已确认事实与待核验门槛

### 事实状态

| 状态 | 事实与依据 | 对实施的约束 |
| --- | --- | --- |
| 已证实 | 菜谱全文由 GraphDataPreparationModule 从 Recipe、REQUIRES、CONTAINS_STEP 临时组装，最后只放在 self.documents 中。见 rag_modules/graph_data_preparation.py:225、243-271、328-358。 | 必须先物化 ParentDocumentStore，不能把 Milvus 命中直接当全文。 |
| 已证实 | chunk 具备 chunk_id、parent_id、chunk_index、total_chunks；按章节切分时才有 section_title。见 graph_data_preparation.py:443-538。 | PDS 必须保存上述定位字段，并额外保存图锚点映射。 |
| 已证实 | 当前 Milvus schema 只有 id、vector、text、节点与常用元数据、chunk_id、parent_id，缺少 chunk_index、total_chunks、section_title、build_id。见 rag_modules/milvus_index_construction.py:91-120。 | 受限检索的顺序与版本一致性只能放在 Milvus V2。 |
| 已证实 | build_vector_index 对同名 collection 调用 force_recreate=True；create_collection 会 drop_collection。见 milvus_index_construction.py:122-160、199-217。 | V2 只能使用新 collection 名；不得复用 cooking_knowledge。 |
| 已证实 | 当前混合检索并行执行实体、主题、向量三路，并按 node_id 优先去重；向量结果会做通用一跳邻居扩展。见 hybrid_retrieval.py:576-633、996-1120、1122-1321。 | QueryPlan 不能直接接入旧默认链路；必须以独立开关灰度。 |
| 已证实 | Graph RAG 多跳匹配使用无方向的可变长度路径，relation_types 仅参与相关性评分；路径和子图 Document 没有 node_id 或 parent_id。见 graph_rag_retrieval.py:287-365、924-945、996-1020。 | 关系题必须改用固定、方向明确的模板，且所有结果保留稳定 ID。 |
| 已证实 | Router 仅在 hybrid_traditional 与 graph_rag 间选择，异常时回落传统混合检索；生成层将所有 Document 文本平铺成一个上下文。见 intelligent_query_router.py:28-70、331-403；generation_integration.py:142-184。 | 需新增 QueryPlan 路径和 EvidenceBundle，而不是修改旧路由语义。 |
| 已证实 | 导入脚本为五类节点声明 nodeId 唯一约束，预期关系方向是 Recipe-REQUIRES->Ingredient、Recipe-CONTAINS_STEP->CookingStep、TechniqueDoc-HAS_CHUNK->TechniqueChunk。见 data/cypher/neo4j_import.cypher:16-20、163-193、270-284。 | 这些仅是目标模板的代码依据，仍须由运行实例确认。 |
| 已证实（本方案验证） | 执行阶段 0 的四个既有测试文件，结果为 13 通过、1 失败。失败项是 test/test_graph_audit_a6.py:99-128 的子图测试；测试替身的 extract_knowledge_subgraph 只接收 graph_query，而生产代码在 graph_rag_retrieval.py:642 传入 graph_query 与 query。 | A1 当前未通过；阶段 0 必须以单独、可审查的回归修复恢复全绿，且不得借此开始后续重构。 |
| 待环境核验 | 本次只读检查显示 docker compose ps 没有运行服务，且 Python 无 neo4j、pymilvus 包；因此尚不能执行实例 schema 查询。 | 阶段 0 的 A2 未完成，阶段 1 及以后不得开始实现。 |
| 待环境核验 | Neo4j 服务把具名卷挂到服务器 import 目录，却把仓库 data/cypher 挂到容器 /import；脚本用 file:///nodes.csv。见 docker-compose.yml:20-24、97-119；data/cypher/neo4j_import.cypher:42。 | 导入、迁移、重建前必须验证 CSV 对 Neo4j 实际可见；不匹配先修正挂载或复制步骤。 |
| 待证实 | Recipe Markdown 到 nodes.csv / relationships.csv 的可复现生产器未被证明存在；V2 仅确认技巧文档有对应生产链。 | 允许阶段 1 从现有 Neo4j 物化，但禁止据此宣称可全量重建或增量同步。 |
| 需要产品/数据治理决策 | “低脂”是每份脂肪阈值、热量阈值、人工标签，还是由食材与用量计算；来源、审核、更新周期与医疗场景边界尚未冻结。 | 阶段 5 前只能做少油/清爽偏好，不得提供严格低脂结论。 |

### 阶段 0 的强制门槛

阶段 0 必须同时通过 A1 与 A2。合成 Document 单元测试是阶段 1 的第一步，不能替代 A2，也不能据此提前开始阶段 1。

| 门槛 | 只读核验与留档 | 通过标准 |
| --- | --- | --- |
| A1：无服务回归 | python -m pytest -q test/test_hybrid_retrieval_fusion.py test/test_router_audit_a4.py test/test_graph_audit_a6.py test/test_web_audit_a3.py | 命令退出码为 0，失败项、Python 版本、依赖锁定状态进入基线记录。 |
| A2：Neo4j 运行实例 | 连接目标数据库执行 CALL db.labels();、CALL db.relationshipTypes();、SHOW INDEXES;，以及下方三个计数查询。 | 有成功连接记录；标签、边类型、索引、计数、数据库名、执行时间和操作者被存档。 |
| A2：Milvus 运行实例 | 使用已安装的 pymilvus 对当前配置 collection 执行 describe_collection() 与 get_collection_stats()。 | collection 名、schema、向量维度、主键、索引、行数、load 状态和客户端版本被存档。 |
| B：CSV 导入可用性 | 在 Neo4j 容器内先读目录再执行非破坏性 LOAD CSV 预检；例如确认 /var/lib/neo4j/import/nodes.csv 存在，且 LIMIT 1 可读。 | 证明 file:///nodes.csv 可读取；否则先以单独基础设施提交修正挂载或复制流程。 |
| C：ID 与分类 | 在 A2 实例上抽样核验 Recipe、Ingredient、CookingStep、TechniqueDoc、TechniqueChunk 的 nodeId、名称/别名来源、步骤顺序、技巧章节顺序，以及“蔬菜”的真实分类字段或关系。 | 形成映射表和空值处理规则；没有经验证分类不得运行“鸡肉搭配什么蔬菜”的硬过滤。 |

阶段 0 必须记录的 Neo4j 计数查询如下；不得以导入脚本替代结果：

~~~cypher
MATCH (:Recipe)-[r:REQUIRES]->(:Ingredient) RETURN count(r);
MATCH (:Recipe)-[r:CONTAINS_STEP]->(:CookingStep) RETURN count(r);
MATCH (:TechniqueDoc)-[r:HAS_CHUNK]->(:TechniqueChunk) RETURN count(r);
~~~

## 总体架构与数据契约

### 稳定 ID 与消歧

| 概念 | 目标 ID | 定位、排序与回补规则 |
| --- | --- | --- |
| Recipe | Recipe.nodeId | 精确名称，再别名/同义词，再全文候选；同分候选返回候选或请求澄清，绝不静默任选。 |
| Ingredient | Ingredient.nodeId | 与 Recipe 相同的消歧流程，且结果 label 必须是 Ingredient。 |
| CookingStep | CookingStep.nodeId + Recipe.nodeId | 先按 CONTAINS_STEP.stepOrder，再按 CookingStep.stepNumber；标题文本不作为稳定 ID。 |
| TechniqueDoc | TechniqueDoc.nodeId | 精确名称、标题、标签、全文候选归一。 |
| TechniqueChunk | TechniqueChunk.nodeId + TechniqueDoc.nodeId | 先按 HAS_CHUNK.chunkOrder，再按 TechniqueChunk.chunkIndex。 |
| child chunk | chunk_id + parent_id + build_id | chunk_id 由物化器确定，Milvus V2 与 PDS 必须逐条一致。 |
| 前端 recipe_序号 | 不纳入本契约 | 除非另行建立并验证映射表。 |

### ParentDocumentStore 数据模型

SQLite 的核心表必须至少包含下列字段；所有主键、外键和唯一性在迁移脚本与单元测试中验证。

| 表 | 主键/约束 | 关键字段 | 用途 |
| --- | --- | --- | --- |
| builds | build_id 主键 | source_fingerprint、builder_version、chunk_config、created_at、status | 记录可复现构建，不把不同构建的内容混读。 |
| parents | parent_id、build_id 联合唯一 | node_type、title、full_content、content_hash、metadata_json | Recipe、TechniqueDoc 的全文。 |
| chunks | chunk_id、build_id 联合唯一 | parent_id、chunk_index、total_chunks、section_title、text、text_hash | 章节与相邻 chunk 回补。 |
| anchors | anchor_type、anchor_id、parent_id、build_id 联合唯一 | chunk_id、ordinal、source_relation | 把 CookingStep.nodeId 或 TechniqueChunk.nodeId 映射到 PDS chunk；显示标题不是锚点。 |

公开读取接口在阶段 1 冻结为：

~~~text
ParentDocumentStore.open(active_build_id=None)
get_full_parent(parent_id, expected_node_type=None) -> ParentDocument | None
get_chunk_window(parent_id, anchor_chunk_id, before, after) -> list[TextEvidenceSource]
get_anchor_window(parent_id, anchor_type, anchor_id, before, after) -> list[TextEvidenceSource]
get_build_manifest(build_id) -> BuildManifest
iter_chunks(build_id) -> iterator[CanonicalChunk]
validate_chunk_linkage(rows_from_milvus) -> LinkageReport
~~~

写入接口只由物化器使用：先生成不可变的 parent_store.<build_id>.sqlite 与 manifest，再原子更新 active-build 指针。CanonicalChunk 是 V2 唯一允许的建库输入，至少含 chunk_id、parent_id、chunk_index、total_chunks、section_title、text、text_hash、build_id；V2 不得从旧的内存 chunks 或当前 Milvus 反推它。读取器绝不在请求期间从 Markdown 目录扫描全文。

### 检索与证据对象

阶段 2 起统一用下列对象交接，旧的 LangChain Document 仅在兼容适配层出现：

| 对象 | 必填字段 | 约束 |
| --- | --- | --- |
| EntityCandidate | node_id、node_type、display_name、match_kind、score、ambiguity | 只表示已定位的候选；ambiguity 为真时不得自动选一个。 |
| QueryPlan | intent、entities、filters、graph_template、vector_scope、response_policy、plan_version | 只能来自枚举与白名单校验；LLM 输出只是候选。 |
| GraphFact | fact_id、template_id、node_ids、edges、properties、status | status 只能是 verified、not_found、unavailable；文本不得填充 verified。 |
| TextEvidence | parent_id、build_id、chunk_ids、anchor_ids、text、origin | origin 为 parent_store 或 milvus_child；后者必须经过 PDS 回补。 |
| EvidenceBundle | query_plan、entity_candidates、graph_facts、text_evidence、limitations | 图事实与正文证据物理分栏；缺失状态显式保留。 |

生成层的提示模板必须分为“已验证图事实”“正文证据”“限制与不可证明项”三个区块。它只能从 GraphFact.status=verified 输出关系断言；只能在 nutrition 证据等级满足要求时输出严格营养结论。

### QueryPlan 白名单

允许的 intent 和固定模板在阶段 3 固化为：RECIPE_FULL、RECIPE_STEP、INGREDIENT_RECIPES、INGREDIENT_PAIR_VEGETABLE、TECHNIQUE_SECTION、PREFERENCE_RECOMMEND、ENTITY_NOT_FOUND。模板必须参数化，标签、关系类型、方向和返回字段写死在代码中；拒绝原样执行 LLM 生成的 Cypher。

典型模板的方向如下：

~~~cypher
// 食材能做什么
MATCH (i:Ingredient {nodeId: $ingredient_id})<-[:REQUIRES]-(r:Recipe)
RETURN r.nodeId, r.name, r.cuisineType

// 鸡肉搭配什么蔬菜；vegetable predicate 必须来自阶段 0 的已确认映射
MATCH (i:Ingredient {nodeId: $ingredient_id})<-[:REQUIRES]-(r:Recipe)-[:REQUIRES]->(v:Ingredient)
WHERE v.nodeId <> i.nodeId AND <verified_vegetable_predicate>
RETURN r.nodeId, r.name, v.nodeId, v.name

// 菜谱中的目标步骤
MATCH (r:Recipe {nodeId: $recipe_id})-[c:CONTAINS_STEP]->(s:CookingStep {nodeId: $step_id})
RETURN s.nodeId, c.stepOrder, s.stepNumber
~~~

## 阶段 0：环境与回归基线

### 目标与不做什么

完成 A1、A2、B、C 的只读核验，建立当前行为和评测样本基线；不改变任何检索逻辑、不重建数据库、不创建 Milvus collection。

### 进入条件

- 工作分支干净或仅含本任务的已审查改动。
- 可取得目标 Neo4j/Milvus 的只读连接信息，或明确记录其不可用原因。
- 阶段 0 尚未批准任何数据导入、迁移或删除动作。

### 文件范围、接口与数据动作

| 类别 | 文件 |
| --- | --- |
| 新增 | docs/retrieval/baseline/phase-0-<日期>.md，保存命令、版本、输出摘要、实例 schema、样本 ID 和分类映射。 |
| 条件修改 | docker-compose.yml 仅当 B 失败时，单独修正 Neo4j import 目录与 CSV 可见性；同时新增对应预检脚本或文档。 |
| 不修改 | rag_modules/ 下所有运行检索模块、main.py、config.py、Milvus 数据、Neo4j 数据。 |

此阶段不引入新公开运行接口。只读 PDS/Milvus/Neo4j 诊断命令必须显式目标化当前配置的 database 与 collection。

### 测试、真实服务检查与验收

先执行无服务回归：

~~~bash
python -m pytest -q test/test_hybrid_retrieval_fusion.py test/test_router_audit_a4.py test/test_graph_audit_a6.py test/test_web_audit_a3.py
~~~

再在真实服务可用且凭据已提供后执行 A2 的 Cypher、Milvus describe_collection()、get_collection_stats()，并做 B 的非破坏性 CSV 可读预检。必须在基线记录中保存实际的 labels、relationshipTypes、indexes、集合 schema、行数与失败信息。当前 docker compose ps 为空且 neo4j/pymilvus 未安装，这一现状只能标为阻塞，不能用模拟结果替代。

用户场景验收是为下阶段固定判定样本和期望：宫保鸡丁全文、首步腌制、鸡肉菜谱、鸡肉蔬菜搭配、低脂川菜、夏天清淡、腌肉技巧，以及实体不存在、关系不存在、图失败。此阶段只记录当前表现，不要求改善。

### 回退、完成定义与提交检查点

- 开关：无运行开关；若 B 的修正上线，使用 compose 变更的独立提交回退，不触碰卷或数据库。
- 回退：撤销未部署的基础设施配置提交；已经记录的基线文件不删除，仅标记被替代。
- DoD：A1、A2、B、C 全部留档并通过；测试命令退出码为 0；独立审查签收通过；不含任何运行检索改动或数据写操作。
- 提交/PR：提交“文档（检索基线）：记录运行 schema 与回归门槛”；推送后创建或更新草稿 PR，正文写明 A1/A2/B/C 结果。任一项失败时只提交如实的诊断文档，PR 保持草稿，禁止开始阶段 1。

## 阶段 1：ParentDocumentStore

### 目标与不做什么

在阶段 0 完成后，新增版本化 SQLite ParentDocumentStore，物化 Recipe 与 TechniqueDoc 的全文、chunk、图锚点和相邻窗口读取。此阶段不接管 Router、不改变 Milvus collection、不让请求路径依赖新 store。

### 进入条件

- 阶段 0 DoD 已被 PR 记录，且存在本方案定义的独立审查通过记录。
- C 中 Recipe、CookingStep、TechniqueDoc、TechniqueChunk 的 ID、顺序字段和别名来源已冻结。
- 若从现有 Neo4j 物化，已验证只读连接；若计划重建源数据，C 的 Recipe 生产器门槛也必须先通过。

### 文件范围、接口、schema 与 ID 映射

| 类别 | 文件 |
| --- | --- |
| 新增 | rag_modules/parent_document_store.py、rag_modules/parent_document_materializer.py、scripts/build_parent_document_store.py、test/test_parent_document_store.py、test/test_parent_document_materializer.py。 |
| 修改 | config.py 增加 PDS 路径、active build 指针及 RETRIEVAL_PARENT_STORE_ENABLED；main.py 只实例化和健康检查，不把它接到 Router。 |
| 不修改 | hybrid_retrieval.py、graph_rag_retrieval.py、milvus_index_construction.py、generation_integration.py 的既有调用契约。 |

物化器以同一构建会话读取 Neo4j：Recipe 取 Recipe、REQUIRES、CONTAINS_STEP；TechniqueDoc 取 TechniqueDoc、HAS_CHUNK。Recipe 步骤排序沿用已验证的 COALESCE(stepOrder, stepNumber) 规则，现有组装依据见 graph_data_preparation.py:243-346；技巧章节排序依据见同文件:368-434。它必须为每个 Recipe 的 CookingStep.nodeId、每个 TechniqueDoc 的 TechniqueChunk.nodeId 写入 anchors。

build_id 由物化器版本、规范化 chunk 配置、按 parent_id 排序的全文哈希组成。source_fingerprint 存放每个 parent 内容哈希的有序摘要。chunk_id 必须稳定、可重现且由 parent_id 与 chunk_index 推导，不能依赖当前全局递增计数；这消除现有 graph_data_preparation.py:459-534 中全局 chunk_id 对重排敏感的问题。

### 数据构建、测试与验收

数据动作是新增不可变 SQLite 文件和 manifest，非破坏性。构建过程写入同目录临时文件，完成 integrity_check、外键检查、content/chunk 哈希检查后原子发布 active-build 指针；保留至少上一个成功 build。阶段 4 启用 V2 后，PDS 构建可以继续生成和验证，但不得单独改 active-build 指针；必须经阶段 4 的联合 artifact manifest 与 collection 一起切换。

先从合成 Document 做无服务测试，再接入真实 Neo4j 物化。这两个步骤不得调换：

~~~bash
python -m pytest -q test/test_parent_document_store.py test/test_parent_document_materializer.py
python scripts/build_parent_document_store.py --dry-run --source neo4j --output <staging-path>
python scripts/build_parent_document_store.py --source neo4j --output <versioned-path> --build-id <build> --publish --active-pointer <pointer-path>
python scripts/build_parent_document_store.py --check-active --active-pointer <pointer-path> --expected-build <build>
~~~

实际发布命令仅当 staging 的 SQLite integrity_check、外键、所有 anchors、manifest 哈希和源内容样本校验都通过时才允许更新指针；任一失败必须保留 staging 文件、退出非零且不改变 active 指针。真实服务检查至少抽样一个 Recipe、一个 CookingStep、一个 TechniqueDoc、一个 TechniqueChunk，核对 node_id、parent_id、顺序、全文哈希和 anchors；并执行 PDS 的 SQLite integrity_check。Milvus 尚未接入，因此此阶段不得宣称 PDS 与现有 child chunk 一致；阶段 4 会以该 PDS 的 CanonicalChunk 直接构建 V2 并完成首个 linkage 检查。

用户场景验收：可用 Recipe ID 返回完整“宫保鸡丁”正文；可用 CookingStep ID 返回“第一步”对应正文窗口；可用 TechniqueChunk ID 返回“腌肉”命中章节和相邻章节。所有返回都包含 build_id、parent_id 与锚点 ID。

### 回退、完成定义与提交检查点

- 开关：RETRIEVAL_PARENT_STORE_ENABLED，默认关闭。
- 回退：关闭开关；或把 active-build 指针切回上一个已验证的 PDS SQLite 文件。绝不删除新旧 build。
- DoD：核心四表和公开接口已测试；合成与真实 Neo4j 两类检查通过；失败构建不发布；没有 Router/Milvus 行为变化。
- 提交/PR：提交“功能（父文档库）：物化版本化全文与锚点”；只暂存本阶段路径，运行上述测试后推送并更新草稿 PR 的 build_id、样本核对和回退指针。

## 阶段 2：证据契约与实体直达

### 目标与不做什么

定义 EntityCandidate、GraphFact、TextEvidence、EvidenceBundle，并让明确菜名或技巧名走“实体定位 -> 稳定 ID -> PDS”直达路径。此阶段不替换关系题图查询、不启用 Milvus V2、不更改旧 hybrid/Graph RAG 的默认路由。

### 进入条件

- 阶段 1 的 PDS build 已发布、抽样 ID/anchor 校验通过。
- PDS 与其 build manifest 可被只读健康检查打开。
- 实体别名、全文索引的实例可用性及同分消歧策略已在阶段 0 记录。

### 文件范围、接口与数据

| 类别 | 文件 |
| --- | --- |
| 新增 | rag_modules/retrieval_contracts.py、rag_modules/entity_resolver.py、rag_modules/entity_direct_retrieval.py、rag_modules/evidence_builder.py、test/test_entity_resolver.py、test/test_entity_direct_retrieval.py、test/test_evidence_bundle.py、test/test_generation_evidence_context.py。 |
| 修改 | generation_integration.py 增加 EvidenceBundle 输入适配和三分层 prompt；config.py 增加 RETRIEVAL_ENTITY_DIRECT_ENABLED；main.py 组装新组件；必要时 rag_modules/web_service_handler.py 增加审计字段。 |
| 不修改 | hybrid_retrieval.py、graph_rag_retrieval.py 的既有实现和 milvus_index_construction.py。 |

实体解析接口为 resolve(query_text, expected_types) -> list[EntityCandidate]。解析优先级固定为精确名称、经治理的别名/同义词、已验证的全文候选；候选并列时 EvidenceBundle 标记 ambiguity，不调用全局向量检索来打破平局。

实体直达接口为 retrieve(entity, request_scope) -> EvidenceBundle。Recipe_FULL 调 get_full_parent；Recipe_STEP 只允许使用最小的固定定位器 recipe_step_anchor_v1：输入 recipe_id 与经过校验的序号/step_id，固定匹配 Recipe-[:CONTAINS_STEP]->CookingStep，返回 step_id、stepOrder、stepNumber，限制为一个结果，再以 get_anchor_window 回补。该定位器不是通用图查询：不接受 LLM Cypher、关系类型、label 或任意过滤表达式；请求、参数、返回 ID、空结果和图不可用状态进入审计。TechniqueDoc/TechniqueChunk 同理。TextEvidence 必须标明 parent_store、build_id、chunk_ids；GraphFact 仅包含本阶段已经执行并验证的实体/步骤定位事实。

### 测试、场景验收与降级

~~~bash
python -m pytest -q test/test_entity_resolver.py test/test_entity_direct_retrieval.py test/test_evidence_bundle.py test/test_generation_evidence_context.py
python -m pytest -q test/test_hybrid_retrieval_fusion.py test/test_router_audit_a4.py test/test_graph_audit_a6.py test/test_web_audit_a3.py
~~~

集成测试使用测试 Neo4j + 阶段 1 PDS，断言“宫保鸡丁怎么做？”精确命中时 Milvus fake client 的调用数为 0，且返回完整食材和有序步骤；“宫保鸡丁第一步怎么腌？”只允许 recipe_step_anchor_v1 返回目标步骤、相邻步骤和必要食材。测试还必须断言定位器拒绝任意关系/label/Cypher 入参，并记录 template_id、参数上限和 unavailable/not_found。生成测试断言图事实、正文、限制三个区块不混排。

实体不存在时：返回显式 ENTITY_NOT_FOUND；只可在用户接受泛化建议时进入旧的广义文本推荐，并标明“未定位到同名实体”。PDS 读取失败时关闭本路径并回落旧路由，同时记录 parent-store-unavailable；不伪造正文。

### 回退、完成定义与提交检查点

- 开关：RETRIEVAL_ENTITY_DIRECT_ENABLED 依赖 RETRIEVAL_PARENT_STORE_ENABLED；两个默认关闭。
- 回退：关闭实体直达开关，回到当前 Router/Hybrid；PDS build 保留以便诊断。
- DoD：四种证据对象 schema 通过序列化和拒绝非法状态测试；两个明确菜名场景不触发全库向量；歧义和 PDS 故障可审计地降级；旧回归仍通过。
- 提交/PR：提交“功能（证据链）：增加实体直达与分层上下文”；推送并更新 PR，附上 0 次向量调用、歧义、PDS 故障三个审计样本。

## 阶段 3：QueryPlan 与目标化图查询

### 目标与不做什么

用经过 schema 校验的 QueryPlan 和固定白名单 Cypher 处理步骤、食材到菜谱、食材搭配、技巧章节等请求，替代新路径中的默认三路并行和通用一跳扩展。此阶段不删除旧 Graph RAG，不启用受限向量召回来证明关系。

### 进入条件

- 阶段 2 DoD 完成，EvidenceBundle 与实体解析可用。
- 阶段 0 已确认运行实例的标签、关系类型、索引与蔬菜分类 predicate。
- 所有模板都有上限、参数化字段和明确返回 node_id 的设计评审记录。

### 文件范围、接口、模板与数据

| 类别 | 文件 |
| --- | --- |
| 新增 | rag_modules/query_plan.py、rag_modules/targeted_graph_retrieval.py、rag_modules/query_plan_validator.py、test/test_query_plan_validator.py、test/test_targeted_graph_retrieval.py、test/test_relation_failure_policy.py。 |
| 修改 | config.py 增加 RETRIEVAL_QUERY_PLAN_ENABLED 与 RETRIEVAL_TARGETED_GRAPH_ENABLED；main.py 在新开关下优先执行 QueryPlan；evidence_builder.py 接收 GraphFact。 |
| 不修改 | graph_rag_retrieval.py、hybrid_retrieval.py、milvus_index_construction.py 的旧入口和既有测试语义。 |

LLM 若参与规划，只能输出候选 JSON。validator 必须验证 intent 枚举、实体类型、过滤字段、最大候选数、固定 template_id；非法 JSON、未知关系、未知标签、任意 Cypher 字符串一律拒绝并转保守规则计划。TargetedGraphRetriever 只接受 template_id 与绑定参数，结果必须含模板 ID、方向、关系类型、全部 node_id、数据库时间戳。

模板至少覆盖：Recipe 步骤定位、Ingredient <- REQUIRES - Recipe、Ingredient <- REQUIRES - Recipe - REQUIRES -> Ingredient、TechniqueDoc - HAS_CHUNK -> TechniqueChunk、可信菜系候选 ID 过滤。BELONGS_TO 和 BELONGS_TO_CATEGORY 的选择必须按阶段 0 实例结果决定，不能混用导入脚本中的两个概念。

### 测试、场景验收与关系故障策略

~~~bash
python -m pytest -q test/test_query_plan_validator.py test/test_targeted_graph_retrieval.py test/test_relation_failure_policy.py
python -m pytest -q test/test_entity_resolver.py test/test_entity_direct_retrieval.py test/test_evidence_bundle.py test/test_generation_evidence_context.py
python -m pytest -q test/test_hybrid_retrieval_fusion.py test/test_router_audit_a4.py test/test_graph_audit_a6.py test/test_web_audit_a3.py
~~~

真实 Neo4j 集成检查对每个 template 执行 EXPLAIN/PROFILE 审查和带 LIMIT 的实际查询，确认返回 ID、方向与关系类型。用户验收如下：

| 场景 | 必须结果 |
| --- | --- |
| 鸡肉能做什么？ | 只由 Ingredient <- REQUIRES - Recipe 图事实给出可解释菜谱列表；需要做法时再回补相应 PDS。 |
| 鸡肉搭配什么蔬菜？ | 每一个推荐蔬菜都附有 Recipe 中介和经确认的蔬菜分类事实。 |
| 宫保鸡丁第一步怎么腌？ | Recipe 与 CookingStep 的关系事实和 PDS 锚点正文一致。 |
| 腌肉有哪些关键要点和适用场景？ | TechniqueDoc/HAS_CHUNK 的定位事实与连续正文分层返回。 |

图关系不存在时：返回 GraphFact.status=not_found，明确“当前图谱未找到该关系”；可另给非关系性烹饪参考，但不得把它写成关系证明。图服务失败时：GraphFact.status=unavailable，保留错误审计；可返回已知 PDS 正文或向量文本，且必须标注为“非关系性烹饪参考”，不能回答关系已成立。

### 回退、完成定义与提交检查点

- 开关：RETRIEVAL_QUERY_PLAN_ENABLED、RETRIEVAL_TARGETED_GRAPH_ENABLED；前者开启时后者仍可单独关闭，使关系计划显式返回 unavailable。
- 回退：关闭两个开关回旧 Router。关系题的响应策略仍不得用旧向量文本伪造 verified GraphFact。
- DoD：validator 拒绝越权计划；所有白名单模板有单测和真实服务记录；四类图场景、关系不存在、图失败都通过；没有自由 Cypher 执行通道。
- 提交/PR：提交“功能（查询计划）：增加白名单图查询与关系证据”；推送并更新 PR，列出每个 template 的 EXPLAIN/PROFILE 摘要、关系故障样本和未确认 schema 项。

## 阶段 4：受限向量检索与 Milvus V2

### 目标与不做什么

实现“候选 parent_id 过滤 -> child chunk 语义召回 -> parent 聚合 -> PDS hydration”，建立含顺序、章节和 build_id 的版本化 Milvus V2。此阶段不在同名集合上重建，不删除旧 collection，也不把向量文本作为关系或严格营养证据。

### 进入条件

- 阶段 3 DoD 通过，QueryPlan 能给出已验证的 candidate parent_id 集合或明确为全库偏好检索。
- 阶段 1 的 PDS CanonicalChunk 已通过自校验；V2 构建器只读取同一 build 的 iter_chunks 输出，并在写入前后执行 linkage 验证。此处不要求也不得假设它与旧 collection 一致。
- Milvus A2 描述、当前 collection 名、可用磁盘/备份位置、维护窗口和人工切换负责人已记录。
- 新 collection 名、备份目标、恢复目标均通过 collection 白名单校验；白名单绝不包含当前旧集合的删除或重建操作。

### 文件范围、V2 schema 与构建

| 类别 | 文件 |
| --- | --- |
| 新增 | rag_modules/restricted_vector_retrieval.py、rag_modules/milvus_v2_index.py、scripts/validate_pds_milvus_linkage.py、scripts/milvus_snapshot.py、scripts/build_milvus_v2.py、scripts/retrieval_cutover.py、test/test_restricted_vector_retrieval.py、test/test_parent_aggregation.py、test/test_milvus_v2_schema.py、test/test_retrieval_artifact_manifest.py。 |
| 修改 | config.py 增加 RETRIEVAL_MILVUS_V2_ENABLED、RETRIEVAL_MILVUS_COLLECTION、目标 collection 白名单；main.py 在 QueryPlan 的 PREFERENCE_RECOMMEND 分支组装 V2 检索；parent_document_store.py 在 V2 开启时只读取联合 artifact manifest；必要时 evidence_builder.py 接收 PDS hydration。 |
| 不修改 | milvus_index_construction.py 的 build_vector_index 行为、旧 cooking_knowledge collection、hybrid_retrieval.py、graph_rag_retrieval.py。 |

V2 collection 名规则为 cooking_knowledge_v2_<build_id_short>，且每次构建都在显式的 milvus database 中完成。所有 V2 工具均把 --database 与 --allowed-database 设为必填，拒绝 SDK 默认 database、别名推断或与批准记录不相符的 database。创建前必须确认目标 collection 不存在；若已存在则直接失败，禁止 force_recreate、drop_collection 或复用名称。V2 schema 作为 milvus_v2_schema_v1 冻结：id 为 VARCHAR(150) 主键且等于 chunk_id；vector 为 FLOAT_VECTOR，维度等于已冻结的 embedding_model 与 GraphRAGConfig.milvus_dimension（当前代码默认 512，见 config.py:33-38）；text 为 VARCHAR(15000)；parent_id、node_id 为 VARCHAR(100)；node_type、category 为 VARCHAR(100)；cuisine_type 为 VARCHAR(200)；doc_type 为 VARCHAR(50)；chunk_index、total_chunks 为 INT64；section_title 为 VARCHAR(500)；build_id 为 VARCHAR(64)；text_hash 为 VARCHAR(64)。索引固定为 vector 上的 COSINE/HNSW，M=16、efConstruction=200，查询 ef=64；这些参数、embedding model、维度和 schema hash 必须写入 collection manifest 并由 describe_collection() 验证。任何超长字段必须在构建前以失败报告处理，不能静默截断。

id 等于 chunk_id；parent_id 必须等于 PDS parent_id；build_id、text_hash、chunk_index、section_title 必须与同一 build 的 CanonicalChunk 一致。构建器先运行 validate_pds_milvus_linkage.py 的 preinsert 模式确认 CanonicalChunk 的唯一性、顺序和哈希，再写入新 collection，随后用 postinsert 模式抽样及全量计数核对。过滤表达式只由受控字段和值构建，parent_id 列表为空时禁止退化为全库搜索。

阶段 4 新增 retrieval_artifact_manifest.json，内容至少包括 pds_build_id、pds_manifest_sha256、milvus_database、milvus_collection、milvus_schema_hash、milvus_build_id、created_at、rollback_database、rollback_collection、rollback_pds_build。切换只允许 retrieval_cutover.py 在验证所有字段后原子替换该联合 manifest。运行时若 collection 返回的 build_id、PDS build 或 manifest hash 任一不一致，拒绝 hydration、记录 artifact-mismatch 并回退旧路径；V2 开启时不得仅靠 PDS active-build 指针或环境变量分别切换两端。

parent 聚合规则固定：同 parent_id 的命中按最佳 child 相似度、不同章节覆盖数、去重后的 chunk_index 窗口综合评分；仅聚合后 Top-N parent 调 PDS 取全文或相邻窗口。Milvus 文本只作命中理由，不作为全文来源。

### 迁移、备份、切换与恢复

所有命令在实现后由运维脚本提供，脚本必须先打印目标并要求显式确认；以下是验收时必须执行的命令形态，尖括号为人工填写的不可复用值：

~~~bash
python scripts/milvus_snapshot.py create --database <milvus-db> --collection cooking_knowledge --output <immutable-backup-dir> --allowed-database <milvus-db> --allowed-collection cooking_knowledge
python scripts/milvus_snapshot.py verify --manifest <immutable-backup-dir>/manifest.json --database <milvus-db> --collection cooking_knowledge --allowed-database <milvus-db> --allowed-collection cooking_knowledge
python scripts/milvus_snapshot.py restore --manifest <immutable-backup-dir>/manifest.json --target-database <milvus-db> --target-collection cooking_knowledge_restore_verify_<date> --allowed-database <milvus-db> --allowed-collection cooking_knowledge_restore_verify_<date>
python scripts/milvus_snapshot.py verify --manifest <immutable-backup-dir>/manifest.json --database <milvus-db> --collection cooking_knowledge_restore_verify_<date> --check-search
python scripts/validate_pds_milvus_linkage.py --parent-store <store-path> --build <build> --mode preinsert
python scripts/build_milvus_v2.py --database <milvus-db> --allowed-database <milvus-db> --collection cooking_knowledge_v2_<build> --parent-store-build <build> --allowed-collection cooking_knowledge_v2_<build> --verify-only
python scripts/build_milvus_v2.py --database <milvus-db> --allowed-database <milvus-db> --collection cooking_knowledge_v2_<build> --parent-store-build <build> --allowed-collection cooking_knowledge_v2_<build>
python scripts/validate_pds_milvus_linkage.py --parent-store <store-path> --build <build> --collection cooking_knowledge_v2_<build> --mode postinsert
python scripts/retrieval_cutover.py --database <milvus-db> --allowed-database <milvus-db> --from cooking_knowledge --to cooking_knowledge_v2_<build> --parent-store-build <build> --artifact-manifest <manifest-path> --approval-record <protected-approval-json> --expected-backup-sha256 <sha256>
~~~

snapshot verify 必须逐项校验 manifest 的数据库/collection、schema、总行数、抽样 chunk_id、text_hash 与可恢复性，而非仅检查备份目录存在。可恢复性必须包含上方“恢复到全新 verify collection 后再执行检索”的演练；恢复验证 collection 只可由白名单脚本在验证后按显式保留/清理策略处理，不能触及旧 collection。build 验证必须比较 V2 行数、PDS CanonicalChunk 数、build_id、随机样本向量可检索性和过滤后不越界性。

切换前必须由指定人工确认测试环境/生产环境、目标 collection、PDS build、备份 manifest 和回退值；自动任务无权切换。protected-approval-json 由受保护发布环境写入，至少包含审批人、双人审批记录、环境、from/to collection、PDS build、backup SHA256、过期时间和变更单号。retrieval_cutover.py 必须校验这些值与参数及当前 manifest 完全相等、审批未过期、运行环境为受保护发布环境；任一项不符即拒绝。--allowed-collection 之外还必须校验数据库别名、备份输出根目录、manifest 路径和恢复目标，拒绝相对路径、通配符和未登记目标。

旧 cooking_knowledge 在整个观察期保留为只读回退源。最快恢复命令是配置回退，而非导入备份：

~~~bash
RETRIEVAL_MILVUS_V2_ENABLED=false RETRIEVAL_MILVUS_COLLECTION=cooking_knowledge <按现有部署方式重启服务>
~~~

若旧集合意外不可用，恢复只能写入新的恢复集合，绝不覆盖同名对象：

~~~bash
python scripts/milvus_snapshot.py restore --manifest <immutable-backup-dir>/manifest.json --target-database <milvus-db> --target-collection cooking_knowledge_restore_<date> --allowed-database <milvus-db> --allowed-collection cooking_knowledge_restore_<date>
python scripts/milvus_snapshot.py verify --database <milvus-db> --collection cooking_knowledge_restore_<date> --manifest <immutable-backup-dir>/manifest.json --check-search
~~~

### 测试、场景验收与回退

~~~bash
python -m pytest -q test/test_milvus_v2_schema.py test/test_restricted_vector_retrieval.py test/test_parent_aggregation.py test/test_retrieval_artifact_manifest.py
python -m pytest -q test/test_query_plan_validator.py test/test_targeted_graph_retrieval.py test/test_relation_failure_policy.py
python scripts/validate_pds_milvus_linkage.py --parent-store <store-path> --build <build> --mode preinsert
python scripts/build_milvus_v2.py --database <milvus-db> --allowed-database <milvus-db> --collection cooking_knowledge_v2_<build> --parent-store-build <build> --verify-only
~~~

真实 Milvus 集成测试必须使用新测试 collection，验证目标已存在拒绝、从不调用 drop_collection、list 过滤、转义、空候选拒绝、跨 parent 去重、PDS hydration、source build 不一致及联合 manifest 不一致拒绝。旧集合不得参与写入测试。

用户验收：

- “夏天吃什么清淡的？”没有硬候选时允许全库 child chunk 语义召回，但必须 parent 聚合后再回补正文。
- 本阶段仅用内部“川菜 + 清淡偏好”样本验证候选 parent_id 过滤、聚合和回补；不向用户提供“推荐低脂川菜”的严格或软偏好话术，该用户可见策略在阶段 5 才启用。
- 图服务失败的关系问题仍遵守阶段 3：向量文本仅是非关系性参考。

### 完成定义与提交检查点

- 开关：RETRIEVAL_MILVUS_V2_ENABLED 与显式 RETRIEVAL_MILVUS_COLLECTION；默认保留旧值。
- 回退：先关闭 V2 并切回 cooking_knowledge；必要时切到已验证 restore collection。不得 drop V2 或旧集合来“回退”。
- DoD：备份创建、恢复至全新验证集合并检索、verify 均通过；新 collection 在白名单内且确认从不存在目标创建；PDS/Milvus linkage、联合 artifact manifest、过滤边界、parent 聚合、人工切换、artifact-mismatch 拒绝、配置回退均演练成功；旧 collection 仍存在。旧 collection 的最低保留期为 V2 正式切换后 30 个自然日，由检索值班负责人负责；期满后也不在本任务中删除，任何删除另需单独批准与恢复演练。
- 提交/PR：先提交“功能（向量检索）：增加受限 child chunk 聚合”，再提交“维护（Milvus）：增加 V2 构建与可恢复切换”；每个独立验证后立即推送并更新同一 PR。PR 记录 backup manifest、目标 collection、人工确认、旧集合保留期限与恢复演练结果。

## 阶段 5：营养/饮食属性与推荐

### 目标与不做什么

把“硬营养/饮食约束”和“少油、清爽等文本偏好”分成不同证据等级和回答策略。此阶段只在已做出数据治理决策后实现严格低脂；不以正文、嵌入相似度或模型推断替代营养数据。

### 进入条件

- 阶段 4 DoD 完成；受限向量和 PDS hydration 已可审计。
- 产品/数据治理以可审计记录选择且只选择一种出口：严格营养出口，确认严格低脂的来源、阈值、单位、每份定义、适用人群、来源版本、审核人和更新规则；或软偏好出口，明确当前无可用可信营养来源、严格模式必须保持关闭、可用文案与医疗/阈值请求的证据不足响应。
- 选择严格营养出口时，至少一种可信数据已落地：Recipe 级每份脂肪/热量数值、治理的饮食标签、或可重复执行的“食材用量 + 营养库”计算。选择软偏好出口时，不得伪造数据以满足本条件。

### 文件范围、属性契约与数据动作

| 类别 | 文件 |
| --- | --- |
| 新增 | rag_modules/nutrition_policy.py、rag_modules/recommendation_evidence.py、scripts/validate_nutrition_dataset.py、test/test_nutrition_policy.py、test/test_low_fat_recommendation.py。 |
| 条件修改 | data/cypher/neo4j_import.cypher 及相应 CSV/生产器，只在数据治理决定新增可信字段时修改；targeted_graph_retrieval.py 增加固定营养过滤模板；generation_integration.py 增加证据等级措辞；config.py 增加 RETRIEVAL_STRICT_NUTRITION_ENABLED。 |
| 不修改 | 旧 Milvus collection、旧混合检索的语义，不以 rerank 分数写回营养字段。 |

严格模式的最低字段契约为 Recipe.nodeId、fat_g_per_serving、energy_kcal_per_serving（如适用）、nutrition_source、nutrition_version、reviewed_at，或 governance_tag、tag_policy_version、reviewed_at。每项必须有单位、空值、过期和冲突处理规则。若采用计算方式，输入食材 nodeId、数量、单位、营养库版本和计算版本必须可复现并落档。

### 双路径、测试与验收

“推荐低脂川菜”固定分为两条路径：

1. 有可信营养字段或治理标签：Neo4j 按四川菜和阈值/标签硬过滤或排序 -> 返回 Recipe ID -> PDS 正文回补。回答可给出数值、阈值或治理标签依据。
2. 无可信营养字段：Neo4j 先收集川菜 parent_id -> Milvus V2 在 parent_id 范围内检索 child chunk -> parent 聚合 -> PDS 正文回补。只能表述为“可能更符合少油/清爽偏好”，且必须说明当前资料不能验证严格低脂。

原问题出现“低脂”但没有硬证据时，非严格模式可以给出第二条路径的候选和上述限制。用户要求脂肪克数、严格控脂或医疗饮食时，只有第一条路径能返回结果；否则响应“证据不足”，不展示软偏好候选为满足条件的推荐。

Neo4j 不可用时，严格模式一律返回“营养/菜系硬证据不可用”，不得调用 Milvus 代替硬过滤；非严格模式也不得把全库结果称为“川菜”或“低脂川菜”。若 PDS 与 Milvus 均可用，可以单独给出明确标注的非分类烹饪参考；若用户请求仍要求川菜、低脂、阈值或医疗约束，则返回 evidence unavailable/insufficient，不给出冒充约束匹配的候选。

~~~bash
python -m pytest -q test/test_nutrition_policy.py test/test_low_fat_recommendation.py
python -m pytest -q test/test_restricted_vector_retrieval.py test/test_parent_aggregation.py
~~~

测试必须注入 Neo4j unavailable，并断言严格路径不调用全库 Milvus、非严格路径不输出“川菜”或“低脂”约束已满足。严格营养出口额外执行下列数据集校验和真实 Neo4j 硬过滤抽样；软偏好出口不得伪造 governed source，而必须测试 RETRIEVAL_STRICT_NUTRITION_ENABLED 无法开启、低脂/医疗/阈值请求返回证据不足、以及川菜 scope 内的少油/清爽文案。两种出口的审计均须包含 evidence_level、选择的 policy 版本与缺失原因。用户验收包括：有证据时“推荐低脂川菜”只出现硬匹配；无证据时明确不能验证严格低脂；图不可用时明确硬证据不可用；“夏天吃什么清淡的？”仍是偏好题，不自动升级为营养承诺。

~~~bash
python scripts/validate_nutrition_dataset.py --source <governed-source> --policy <policy-version> --strict
~~~

### 回退、完成定义与提交检查点

- 开关：RETRIEVAL_STRICT_NUTRITION_ENABLED 默认关闭，且与数据集 policy_version 绑定。
- 回退：关闭严格模式，保留已治理数据；回复降为少油/清爽偏好或证据不足，绝不保留旧的严格话术。
- DoD：严格营养出口必须关联数据治理决策、验证报告和硬/软两条路径、医疗/阈值拒绝、缺失/过期/冲突数据测试；软偏好出口必须关联“不具备严格营养证据”的治理决定、严格开关强制关闭、少油/清爽 scope 测试、医疗/阈值证据不足测试。两种出口均要求回答审计可追溯至具体字段/标签或明确的缺失决定，并完成独立审查签收。
- 提交/PR：提交“功能（营养推荐）：区分严格筛选与清爽偏好”；数据 schema、生成器和应用逻辑拆分为独立可验证提交。PR 必须写明阈值定义、数据覆盖率、已知缺口和用户可见限制。

## 阶段 6：数据生产、评测与旧路径迁移

### 目标与不做什么

补齐 Recipe Markdown 到图 CSV 的可复现生产闭环，建立离线评测和渐进式默认路由迁移。此阶段仍不直接删除旧模块、不进行无备份重建，也不在任何场景一次性替换全部流量。

### 进入条件

- 阶段 5 DoD 已通过：严格营养出口或软偏好出口二者之一已按阶段 5 的完整 DoD 关闭，不存在“未完成阶段 5 直接进入阶段 6”的例外。
- Recipe 输入来源、授权、规范、ID 生成、变更检测、CSV 输出和导入预检设计已评审。
- 阶段 0 的 B 已通过；任何目标环境导入另有备份、白名单和人工批准。
- eval/retrieval_release_thresholds.yaml 已提交并冻结：至少 50 条评测（10 个必测场景各至少 1 条、其余为固定释义或故障注入）；10 个必测场景的必需事实与证据等级通过率为 100%；禁止断言、关系伪证和严格营养误报为 0；Recall@5、MRR@5 均不得低于旧路径超过 0.02；PDS/Milvus evidence linkage 为 100%；P95 延迟不高于旧路径基线的 1.20 倍；连续 7 个自然日且至少 100 次新路径请求满足同样的零禁止断言与错误率不高于旧路径加 1 个百分点。任何调整必须以新的阈值文件提交和产品/检索负责人批准完成，不能在评测后口头修改。 |
- 持久化 rollout 监控已配置：受保护 CI/CD 身份每 15 分钟从已授权指标源采集时间戳、流量、错误率、P95、禁止断言计数、营养误报计数和 variant，保存为不可变 job artifact；启动监控、可读取指标源和首个成功采样均已验证。没有指标源、调度器或运行身份时，阶段 6 只能保持 blocked，不能把离线评测替代连续 7 天观察。 |

### 文件范围、生产闭环与评测

| 类别 | 文件 |
| --- | --- |
| 新增 | scripts/build_recipe_graph_csv.py、data/manifests/recipe-build.schema.json、scripts/validate_recipe_graph_csv.py、scripts/neo4j_snapshot.py、scripts/neo4j_graph_import.py、scripts/monitor_retrieval_rollout.py、.github/workflows/retrieval-rollout-monitor.yml、eval/retrieval_refactor_cases.yaml、eval/retrieval_release_thresholds.yaml、scripts/run_retrieval_eval.py、test/test_recipe_graph_producer.py、test/test_retrieval_refactor_eval.py、test/test_neo4j_import_guard.py、test/test_retrieval_rollout_monitor.py。 |
| 修改 | data/cypher/neo4j_import.cypher 仅在生产器 schema 已验证后调整；docker-compose.yml 仅维持阶段 0 验证的 import 路径；main.py/config.py 以分流比例或 allowlist 控制新路径默认启用。 |
| 不修改 | 已验证的旧 Hybrid/Graph RAG 实现不删除；旧 Milvus collection 继续保留到批准的保留期结束。 |

生产器输入必须是显式目录或 manifest，禁止请求期递归扫描。它以确定性顺序生成 nodes.csv、relationships.csv、manifest（源文件哈希、producer 版本、schema 版本、节点/边数量、稳定 ID 摘要）。validate_recipe_graph_csv.py 检查唯一 nodeId、外键、关系方向、步骤顺序、CSV 转义和与 PDS/Milvus build 的映射可行性。

任何图导入先在独立 staging Neo4j 实例或新建、隔离的 staging database 运行，脚本必须要求精确 database 名、CSV 目录、受控备份根目录和白名单；不允许默认 database、通配符、相对路径、既有生产数据库或生产/开发混用。neo4j_snapshot.py 依据阶段 0 已记录的运行方式执行原生 dump 或可恢复导出，写入带 schema、节点/边计数、样本 nodeId 哈希的 manifest。neo4j_graph_import.py 的 apply 模式必须接收 --backup-manifest、--expected-backup-sha256 和 --backup-root，验证其对应同一个 database、CSV manifest、备份根目录和已通过的 verify 记录后才能继续；还必须在前后运行 schema、唯一性、关系计数、样本 ID、CSV manifest 哈希核对。批次大小固定且可记录，失败时停止后续批次，不自动继续。

CSV 生成和 dry-run 是非破坏性的；任何 apply 会写入图数据库，属于受控迁移动作而非普通构建。只有 staging 完整导入、快照恢复、阶段 6 评测和用户验收均通过后，才可用同一 immutable CSV manifest 对经过明确批准的新建隔离目标 database 重复“快照 -> verify -> dry-run -> batch apply -> postcheck”流程，再通过配置切换读流量。回退优先将流量/配置留在旧 PDS 与旧 collection；数据恢复只还原到新的 restore database 供比较。对原目标 database 的覆盖、清空、删除或同库就地迁移不在本计划授权范围内，须另行批准。

monitor_retrieval_rollout.py 必须有 --once 和 --evaluate 两种模式：--once 只能读已授权指标源，生成带 UTC 时间、variant 和配置 hash 的不可变 artifact；--evaluate 合并连续 artifact，计算 7 个自然日、至少 100 次请求和所有冻结阈值，输出 rollout-window.json。CI 工作流以受保护身份每 15 分钟执行 --once，并在窗口满足时执行 --evaluate；执行身份、指标源别名、artifact 保留期和下一次计划运行时间写入 PR。连续监控到第 8 个自然日仍未收集够 100 次、指标源持续不可用或任一禁止断言非零时，自动创建 blocked 报告并保持旧流量/开关，不扩大流量；只要调度器仍可用就继续采样，不把超时报告当作通过。

评测集每条样本记录 intent、gold entity ID、gold relation/path（若有）、可接受 parent_id、必需证据等级、禁止断言和故障注入期望。至少覆盖以下问题：

| 场景 | 离线断言 |
| --- | --- |
| 宫保鸡丁怎么做？ | Recipe ID 直达、全文、食材和有序步骤；不调用全库向量。 |
| 宫保鸡丁第一步怎么腌？ | Recipe/CookingStep 稳定 ID、锚点窗口、必要上下文。 |
| 鸡肉能做什么？ | Ingredient <- REQUIRES - Recipe 的图事实与可解释 Recipe 列表。 |
| 鸡肉搭配什么蔬菜？ | 每个蔬菜有 Recipe 中介、方向正确、分类 predicate 已证实。 |
| 推荐低脂川菜 | 有硬证据走硬过滤；无硬证据走受限 parent 检索且限制措辞正确。 |
| 夏天吃什么清淡的？ | 全库 child chunk 允许，但必须 parent 聚合与正文回补。 |
| 腌肉有哪些关键要点和适用场景？ | TechniqueDoc/TechniqueChunk 连续章节正文。 |
| 实体不存在 | 不静默臆测实体，输出候选或明确未找到。 |
| 图关系不存在 | GraphFact 为 not_found，不让文本成为关系证明。 |
| 图服务失败 | GraphFact 为 unavailable；文本仅标为非关系性参考。 |

### 测试、发布、回退与完成定义

~~~bash
python -m pytest -q test/test_recipe_graph_producer.py test/test_retrieval_refactor_eval.py test/test_neo4j_import_guard.py
python scripts/build_recipe_graph_csv.py --input-manifest <source-manifest> --output <staging-csv-dir> --dry-run
python scripts/validate_recipe_graph_csv.py --input <staging-csv-dir> --strict
python scripts/neo4j_snapshot.py create --database <staging-db> --output <immutable-backup-dir> --allowed-database <staging-db>
python scripts/neo4j_snapshot.py verify --database <staging-db> --manifest <immutable-backup-dir>/manifest.json --allowed-database <staging-db>
python scripts/neo4j_graph_import.py --database <staging-db> --csv-dir <staging-csv-dir> --allowed-database <staging-db> --dry-run
python scripts/neo4j_graph_import.py --database <staging-db> --csv-dir <staging-csv-dir> --allowed-database <staging-db> --backup-root <immutable-backup-dir> --backup-manifest <immutable-backup-dir>/manifest.json --expected-backup-sha256 <sha256> --batch-size <approved-size> --approval-record <protected-approval-json> --apply
python scripts/neo4j_snapshot.py restore --manifest <immutable-backup-dir>/manifest.json --target-database <staging-restore-db> --allowed-database <staging-restore-db>
python scripts/neo4j_snapshot.py verify --database <staging-restore-db> --manifest <immutable-backup-dir>/manifest.json --allowed-database <staging-restore-db>
python scripts/run_retrieval_eval.py --cases eval/retrieval_refactor_cases.yaml --variant <old-or-new> --report <report-path>
python -m pytest -q test/test_retrieval_rollout_monitor.py
python scripts/monitor_retrieval_rollout.py --once --metrics-source <approved-alias> --variant <variant> --artifact-dir <artifact-dir>
python scripts/monitor_retrieval_rollout.py --evaluate --artifact-dir <artifact-dir> --thresholds eval/retrieval_release_thresholds.yaml --window-days 7 --min-requests 100
~~~

导入守卫单测必须验证错误 database、既有非隔离目标、旧 collection/实例、缺失批准、缺失/未验证/不匹配的 backup manifest 或 SHA256、相对路径及无白名单都会拒绝；恢复演练在全新的 staging-restore-db 完成后才算备份可用。对旧、新变体分别报告 Recall@K、MRR、关系路径正确率、证据完整率、答案忠实率、严格营养错误率、P95 延迟和故障降级正确率，并逐项与已冻结的 release thresholds 比较。未达到进入时冻结的阈值或任一禁止断言出现时，不扩大流量。

干净测试进程只能提供自动化辅助证据，不能签收最终用户场景验收。最终验收必须由可识别的独立审查代理或非实施者在 staging UI/API 逐条提交 10 个必测问题与三类故障注入，按评测文件中的“必需事实、可见限制、禁止断言”签收。签收记录必须保存审查身份、输入 commit、实际 QueryPlan、GraphFact 状态、TextEvidence build_id/parent_id、最终可见回复和结果；实体不存在、关系不存在、图服务失败三项分别确认没有静默臆测、没有关系伪证、没有将文本伪装为图事实。

发布以 allowlist -> 小比例 -> 明确默认新路径三步进行，每一步必须由 rollout-window.json 证明满足已冻结观察窗口和错误审计阈值。执行代理在前一步窗口达标后立即推进下一步，而不是等待常规确认；受保护环境切换仍以已存在且可验证的审批记录为前提。旧路径保留在 RETRIEVAL_LEGACY_FALLBACK_ENABLED 下，直至评测、线上错误率和用户反馈达标并获得单独删除批准。回退是把 allowlist/比例归零或关闭新开关，不删除任何 collection、PDS build 或模块。

- DoD：Recipe 生产器可重放并通过 CSV 校验；评测覆盖表中全部场景和故障注入；监控器单测、首个采样、连续 7 天/100 请求 rollout-window 和阈值计算通过；独立审查代理或非实施者完成最终 staging 签收；新路径分阶段发布与回退演练成功；旧模块仍可通过兼容开关运行。
- 提交/PR：依次提交“构建（菜谱数据）：增加可复现 CSV 生产器”、“测试（检索评测）：覆盖证据与降级场景”、“维护（检索迁移）：增加渐进切换”。每次推送更新同一 PR 的指标表、流量阶段、风险和回退状态；没有用户明确确认不得合并 main。

## 测试矩阵

| 测试层 | 阶段 | 重点 | 无服务命令或真实服务证据 |
| --- | --- | --- | --- |
| 既有回归 | 0 及每阶段 | 融合、路由审计、图审计、Web 审计不回归 | python -m pytest -q test/test_hybrid_retrieval_fusion.py test/test_router_audit_a4.py test/test_graph_audit_a6.py test/test_web_audit_a3.py |
| PDS 单元 | 1 | schema、原子发布、hash、anchor、窗口、失败 build 不发布 | test_parent_document_store.py、test_parent_document_materializer.py |
| PDS 集成 | 1 | Neo4j 到 SQLite 的 Recipe/TechniqueDoc 物化 | A2 连接、SQLite integrity_check、抽样 stable ID 核对 |
| 实体与证据 | 2 | 消歧、零向量直达、分层 prompt、PDS 故障 | test_entity_resolver.py、test_entity_direct_retrieval.py、test_evidence_bundle.py |
| QueryPlan/图 | 3 | 枚举校验、模板方向、白名单、not_found/unavailable | test_query_plan_validator.py、test_targeted_graph_retrieval.py、EXPLAIN/PROFILE |
| Milvus V2 | 4 | V2 schema、目标已存在拒绝、过滤、空 scope 拒绝、parent 聚合、PDS/联合 manifest build 一致性、备份恢复检索演练 | test_milvus_v2_schema.py、test_restricted_vector_retrieval.py、test_retrieval_artifact_manifest.py、新测试 collection |
| 营养 | 5 | 硬证据、软偏好、严格医疗/阈值拒绝、过期数据 | test_nutrition_policy.py、test_low_fat_recommendation.py、治理数据验证报告 |
| 端到端评测/导入 | 6 | CSV 生产、导入白名单/快照恢复、十个固定场景、关系和营养禁止断言、P95、7 天 rollout 监控、独立签收 | test_neo4j_import_guard.py、test_retrieval_rollout_monitor.py、run_retrieval_eval.py 的 old/new 报告、rollout-window 与 staging 签收记录 |

每个阶段必须先执行其新增单测，再执行既有回归；涉及 Neo4j/Milvus 的阶段还必须完成真实服务检查。实现、测试、验收任一项未通过时，禁止开始下一阶段；不得以“后续补测试”“先重构再调试”或全量切换规避。

## 迁移、回退与发布策略

### 门槛总表

| 阶段 | 必须满足的前置门槛 | feature flag/切换点 | 回退动作 |
| --- | --- | --- | --- |
| 0：基线 | A1、A2、B、C 全部留档；无服务回归和实例 schema 均通过 | 无运行开关 | 仅回退未部署的 compose 修正；不动数据。 |
| 1：ParentDocumentStore | 阶段 0 DoD、稳定 ID/顺序已确认 | RETRIEVAL_PARENT_STORE_ENABLED | 关闭开关或 active-build 指针回到上一个 PDS build。 |
| 2：实体直达 | PDS 真实物化、anchor 样本核对、PDS 健康检查 | RETRIEVAL_ENTITY_DIRECT_ENABLED | 关闭实体直达，回旧 Router/Hybrid。 |
| 3：QueryPlan/目标化图 | 实例 labels/关系/分类 predicate 已确认；阶段 2 EvidenceBundle 通过 | RETRIEVAL_QUERY_PLAN_ENABLED、RETRIEVAL_TARGETED_GRAPH_ENABLED | 关闭新计划路径；关系题返回 unavailable/not_found，不伪造图事实。 |
| 4：Milvus V2 | PDS CanonicalChunk -> V2 linkage、备份恢复检索 verify、database/collection/路径白名单、受保护人工切换确认 | RETRIEVAL_MILVUS_V2_ENABLED、RETRIEVAL_MILVUS_COLLECTION、联合 artifact manifest | 配置切回 cooking_knowledge；必要时切换已验证 restore collection；旧集合保留。 |
| 5：营养/偏好 | 阶段 4 DoD；治理记录已选择严格营养出口或软偏好出口，并完成相应 DoD | RETRIEVAL_STRICT_NUTRITION_ENABLED | 关闭严格模式，仅软偏好或证据不足；不保留严格话术。 |
| 6：生产/迁移 | Recipe 生产器、CSV 校验、staging 快照恢复、已冻结指标、离线评测和用户签收达标 | 新路径 allowlist/流量比例、RETRIEVAL_LEGACY_FALLBACK_ENABLED | allowlist/比例归零，保留旧模块、旧 collection 与 PDS builds；图恢复只写入新 restore database。 |

### 发布纪律

1. 每阶段是一道硬门：实现、单元测试、集成/真实服务核验、用户场景验收、回退演练、独立提交和 PR 更新必须全部完成。
2. 所有 Neo4j/Milvus 写操作先通过环境、数据库、collection、文件路径白名单；未知目标、同名目标或通配目标立即失败。
3. 任何迁移先备份并验证恢复，不以“已存在原始 CSV”作为备份；旧 Milvus collection 与 PDS build 在观察期保留。
4. 功能默认关闭，通过显式配置、allowlist 和可审计的人工确认开启；不以代码合并本身视为切换授权。
5. 遇到图服务失败时，正文回补和向量命中可以作为烹饪参考，但不得变成关系证明；遇到营养证据缺失时，偏好文本不得变成严格低脂承诺。
6. 阶段通过后，执行代理立即推进下一阶段和对应 PR 更新；不为普通实现取舍、单测修复、依赖安装、staging 验收或回退演练向用户请求许可。
7. “用户场景验收”可由独立的干净测试进程、独立审查代理或非实施者在 staging UI/API 复现并签收；执行代理必须主动触发和记录该验收。只有 main 合并和受保护环境数据切换仍以既有的明确审批记录为准。

## 实施顺序与提交检查点

| 顺序 | 独立提交目标 | 合并前必须附在 PR 的证据 |
| --- | --- | --- |
| 0 | 文档（检索基线）：记录运行 schema 与回归门槛 | A1/A2/B/C 的原始摘要和阻塞说明。 |
| 1 | 功能（父文档库）：物化版本化全文与锚点 | PDS schema、真实样本、integrity_check、回退 build。 |
| 2 | 功能（证据链）：增加实体直达与分层上下文 | 直达不调用全库向量、歧义/PDS 故障审计。 |
| 3 | 功能（查询计划）：增加白名单图查询与关系证据 | 模板清单、EXPLAIN/PROFILE、not_found/unavailable 样本。 |
| 4a | 功能（向量检索）：增加受限 child chunk 聚合 | scope 边界、parent 聚合、PDS hydration 测试。 |
| 4b | 维护（Milvus）：增加 V2 构建与可恢复切换 | backup manifest verify、白名单、人工切换确认、回退演练。 |
| 5 | 功能（营养推荐）：区分严格筛选与清爽偏好 | 数据治理版本、覆盖率、阈值与医疗限制测试。 |
| 6a | 构建（菜谱数据）：增加可复现 CSV 生产器 | manifest、确定性重跑、CSV 校验。 |
| 6b | 测试（检索评测）：覆盖证据与降级场景 | old/new 指标、十个场景和禁止断言。 |
| 6c | 维护（检索迁移）：增加渐进切换 | allowlist/比例记录、线上观察和回退结果。 |

每个提交前只暂存本阶段的明确文件，先检查差异并运行对应命令；提交后立即推送当前任务分支并更新同一个 PR。PR 保持草稿直到该阶段所有验收完成；最终进入 main 前仍需用户对该 PR 或分支作出明确合并确认。
