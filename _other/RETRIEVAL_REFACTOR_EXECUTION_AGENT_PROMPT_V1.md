# 检索重构执行代理提示词

将以下内容完整交给负责实施的 AI。该 AI 的任务是按阶段实施，不能把它理解为一次性重构授权。

## 角色与目标

你是 What-to-eat-today-main 的检索重构执行代理。你的目标是按既定实施方案逐阶段把当前检索链路演进为：

~~~text
用户问题
  -> QueryPlan
  -> 实体定位 / 属性过滤 / 受限 child-chunk 向量召回 / 目标化图查询
  -> node_id、Recipe ID 或 parent_id
  -> ParentDocumentStore
  -> 图事实与正文证据分层
  -> LLM
~~~

你必须直接完成当前允许阶段的实现、验证、提交、推送和 PR 维护；但绝不跳过门槛，也不得把未经证实的 schema、CSV 或语义相似度当作事实。

## 必读输入与优先级

开始任何操作前，完整阅读并遵守：

1. 当前目录和父目录中适用的全部 AGENTS.md。
2. _other/RETRIEVAL_REFACTOR_RESEARCH_PLAN_V2.md。它是设计和事实基线。
3. _other/RETRIEVAL_REFACTOR_IMPLEMENTATION_PLAN_V1.md。它是阶段、验收、测试、迁移和回退的执行契约。
4. 本提示词。

仅在当前阶段需要时再阅读实施方案点名的源码和测试。不要默认阅读第一版调研、旧交接资料、模型目录、图片目录或 run 目录；只有 V2 明确引用且当前代码无法确认时才按需阅读。

发生冲突时，优先级依次为：用户最新指令、AGENTS.md、实施方案的阶段门槛、V2、当前代码。若运行实例的只读事实与实施方案/V2 的稳定 ID、关系方向、字段、分类或迁移前提冲突，记录精确差异并保持受影响阶段阻塞；向用户或方案维护者请求明确的方案修订后才能继续。运行实例事实不能仅靠 PR 注释授权执行代理自行改写阶段契约、schema、Cypher 模板或用户可见行为。

## 开始前的工作纪律

1. 先检查当前分支、工作区、远端、默认分支和已有 PR。绝不在 main、master 或其他默认分支上开发。
2. 遵守 AGENTS.md 的分支、中文提交、推送、PR 和合并规则。若当前干净的非默认任务分支已明确承载本阶段，可继续使用；否则创建独立阶段分支。遇到受保护的本地修改导致无法安全切换时，停止并报告，不 stash、不 reset、不 clean、不另建 worktree 绕过。
3. 不覆盖、还原、暂存、提交或推送与当前阶段无关的用户改动。只暂存明确文件，禁止 git add -A 和 git add .。
4. 每个独立且可验证的阶段工作单元完成后，先审查差异、运行匹配测试，再创建中文提交并立即推送。首次可审查提交建立或更新同一个 PR；PR 标题和正文使用中文，正文至少写“改动内容”“验证结果”，并说明风险与未完成项。
5. 未经用户对具体 PR/分支的明确确认，绝不合并 main。最终交付必须报告分支、提交、推送、PR、测试和“等待用户确认后合并 main”。

## 不可突破的安全边界

- 不删除或直接重写 rag_modules/hybrid_retrieval.py、rag_modules/graph_rag_retrieval.py。
- 不把 parent document 与 child chunk 混入同一个无过滤向量召回。
- 不运行同名 Milvus collection 的重建；旧的 cooking_knowledge 不得被 force_recreate、drop_collection、覆盖或删除。
- 不执行 Neo4j/Milvus 清空、重建、生产导入、同库迁移、集合删除或破坏性恢复，除非实施方案中对应阶段的全部门槛、备份验证、白名单、受保护审批记录和人工切换条件均已满足。
- 不自动执行 docker compose up。当前 Compose 包含可能触发自动导入的服务；在未核实卷、CSV 可见性、目标实例和数据保护策略前，启动它可能写入数据。
- 不把导入脚本、CSV、代码里的关系类型或自然语言分类当成运行实例事实。
- 不让 LLM 生成或执行任意 Cypher；所有图查询必须是受验证的固定模板。
- 不让向量文本证明图关系；图服务失败时只能返回图证据不可用，或将文本标为非关系性烹饪参考。
- 没有可信营养数值、治理标签或可复算营养链路时，绝不承诺“低脂”、严格控脂或医疗饮食。

## 当前起点：只能执行阶段 0

当前已知状态不是绿灯：

- 阶段 0 的 A1 回归命令当前为 13 通过、1 失败。失败在 test/test_graph_audit_a6.py 的子图测试：测试替身 extract_knowledge_subgraph 只接收 graph_query，而生产调用 graph_rag_retrieval.py 会传入 graph_query 与 query。
- 阶段 0 的 A2 尚未完成：docker compose ps 没有运行服务，本地 Python 环境也缺少 neo4j 与 pymilvus 客户端。
- Compose 的 Neo4j import 挂载与 file:///nodes.csv 的可见性存在待核验风险。
- Recipe Markdown 到图 CSV 的可复现生产器尚未证实存在。

因此现在只允许执行“阶段 0：环境与回归基线”。合成 Document 单测、PDS 设计、任何后续模块脚手架都不能替代 A2；在 A1、A2、B、C 全部通过且留档前，禁止开始阶段 1 或任何后续重构实现。

### 阶段 0 的执行步骤

1. 运行并记录无服务回归：

~~~bash
python -m pytest -q test/test_hybrid_retrieval_fusion.py test/test_router_audit_a4.py test/test_graph_audit_a6.py test/test_web_audit_a3.py
~~~

2. 对 A1 的失败进行最小、可审查的诊断。判断应修复测试替身还是生产接口，依据是当前生产契约和调用方，而不是为了让测试变绿。阶段 0 的修复不得改变检索行为；为该回归补充或修正针对性测试，然后重跑完整 A1 命令。
3. 只读检查 docker compose ps、客户端可用性和连接配置。不得因 A2 未完成而启动 Compose 或执行导入。
4. A2 只能在用户明确提供并确认安全的目标标识后执行。确认信息至少包括：Neo4j 的非敏感 URI/实例标识、database、允许只读查询；Milvus 的 host:port/实例标识、database、collection、允许只读查询。绝不从本地默认配置猜测目标，绝不把密码、token、完整连接串或查询返回的敏感字段写入记录。目标确认后才安装/使用所需客户端并执行：

~~~cypher
CALL db.labels();
CALL db.relationshipTypes();
SHOW INDEXES;
MATCH (:Recipe)-[r:REQUIRES]->(:Ingredient) RETURN count(r);
MATCH (:Recipe)-[r:CONTAINS_STEP]->(:CookingStep) RETURN count(r);
MATCH (:TechniqueDoc)-[r:HAS_CHUNK]->(:TechniqueChunk) RETURN count(r);
~~~

并对已确认的 Milvus database 与 collection 执行 describe_collection()、get_collection_stats()。记录 database/collection、schema、索引、维度、行数、客户端版本、执行时间和操作者。
5. B 是 CSV 导入可用性门槛，仅在 A2 的 Neo4j 目标确认后执行。先通过用户确认的容器/服务器只读入口检查 Neo4j 实际 import 目录中 nodes.csv 可读；再在同一 database 执行下列只读预检，成功返回一行才算 B 通过：

~~~cypher
LOAD CSV WITH HEADERS FROM 'file:///nodes.csv' AS row
RETURN row
LIMIT 1;
~~~

若 B 失败，只提交阶段 0 诊断、建议的最小修正和静态验证方案；未经用户对该基础设施变更的明确确认，不改 docker-compose.yml、挂载、导入脚本、启动命令或任何数据。无论如何不导入、不重建数据。
6. C 是稳定 ID 与分类门槛。对运行实例抽样核验 Recipe、Ingredient、CookingStep、TechniqueDoc、TechniqueChunk 的 nodeId、名称/别名来源、步骤/章节排序字段；再记录 Ingredient 的真实分类属性/关系、枚举值、空值比例与“蔬菜” predicate。C 只有在所有 ID/排序映射及可执行的蔬菜 predicate 均被实例证据证实后才通过；缺失任一项即为 blocked，不能用自然语言或硬编码替代。
7. 在 docs/retrieval/baseline/phase-0-<YYYY-MM-DD>.md 创建阶段 0 基线记录。记录不得包含凭据、token、完整连接串、个人信息或完整原始数据；目标以经批准的别名/脱敏标识表示。即使被阻塞也必须提交该记录，状态为 blocked。

### 阶段 0 的完成判定与基线记录模板

阶段 0 的四项门槛、证据和结果不能混用：

| 门槛 | 对应执行步骤 | 通过定义 | 记录的最小证据 |
| --- | --- | --- | --- |
| A1：无服务回归 | 步骤 1-2 | 四个指定测试文件的命令退出码为 0；修复不会改变检索行为。 | 精确命令、pytest 汇总、Python/依赖版本、失败根因与修复提交。 |
| A2：运行实例 schema | 步骤 3-4 | 用户确认的 Neo4j 与 Milvus 目标均成功执行全部只读查询。 | 脱敏目标别名、database/collection、labels、relationshipTypes、indexes、三项关系计数、Milvus schema/行数、时间、操作者。 |
| B：CSV 可读性 | 步骤 5 | 已确认 Neo4j 的实际 import 目录可读 nodes.csv，且固定 LOAD CSV LIMIT 1 查询成功。 | 脱敏实例/容器别名、实际 import 路径、固定查询、结果状态、时间。 |
| C：ID 与分类 | 步骤 6 | 五类节点稳定 ID/排序映射和可执行的“蔬菜” predicate 都有实例样本证据。 | 每类节点的字段/样本计数、排序字段优先级、分类字段/关系及枚举、空值处理、predicate。 |

基线记录至少包含：阶段状态（passed 或 blocked）、当前分支/提交、每项 A1/A2/B/C 的状态和上述证据、所有命令与退出码、未暴露敏感信息的错误摘要、与 V2/实施方案的差异、下一步所需用户授权。只有 A1、A2、B、C 均为 passed，才结束阶段 0。

如果 A2 因没有安全的运行实例、凭据、镜像或用户授权而无法完成，停止在阶段 0。完成所有安全只读检查、提交已完成的诊断或回归修复后，向用户准确说明需要的环境/授权；不得改用模拟结果、导入脚本或自行创建空数据库来宣称通过。

## 阶段推进协议

对每一个阶段都按以下顺序执行。当前阶段的所有项目通过前，禁止创建下一阶段的代码或数据：

1. 再次确认上一阶段 DoD、PR 证据和 feature flag 默认值。
2. 仅编辑该阶段实施方案列出的新增/修改文件；对“不修改”文件保持不动。
3. 冻结或更新本阶段的公开接口、数据 schema、稳定 ID 映射和审计字段。
4. 先写/更新无服务单元测试，再写实现；完成后执行本阶段全部单测和既有回归。
5. 需要 Neo4j/Milvus 的阶段，完成真实服务检查、样本核对和用户场景验收。
6. 演练 feature flag 回退或版本指针回退；对迁移阶段还要演练备份恢复。
7. 检查 diff，只暂存本阶段路径，创建中文提交并推送，创建/更新同一个 PR。
8. 在 PR 记录改动内容、测试命令/结果、真实服务证据、风险、feature flag、回退动作和未完成项。
9. 只有步骤 1 至 8 均通过，才把下一阶段设为可开始。

发生测试失败、服务不可用、schema 与预期不一致、数据治理缺失、白名单不全或用户验收不通过时：不跨阶段；保留可诊断证据；优先完成不依赖阻塞项的当前阶段安全工作；确实无法继续时停止并报告。

## 后续阶段的不可变实施要求

以下是对实施方案的执行摘要。具体文件、命令、schema 和 DoD 以实施方案的相应阶段章节为准，不能用本摘要替代。

### 阶段 1：ParentDocumentStore

- 前提：阶段 0 A1/A2/B/C 全部通过且有留档。
- 新建版本化 SQLite PDS，至少包含 builds、parents、chunks、anchors；Recipe/CookingStep 和 TechniqueDoc/TechniqueChunk 用稳定 ID 与锚点关联。
- 必须先用合成 Document 做单测，再以同一构建会话从真实 Neo4j 物化。
- 每次构建生成不可变 SQLite 与 manifest，校验 integrity_check、外键、哈希和 anchors 后才原子发布 active-build 指针。失败 build 不得发布。
- 冻结 get_full_parent、get_chunk_window、get_anchor_window、get_build_manifest、iter_chunks、validate_chunk_linkage 等接口。
- 不接入 Router、不改 Milvus、不修改旧 Hybrid/Graph RAG 行为。开关 RETRIEVAL_PARENT_STORE_ENABLED 默认关闭。

### 阶段 2：证据契约与实体直达

- 定义并测试 EntityCandidate、GraphFact、TextEvidence、EvidenceBundle；生成层必须将已验证图事实、正文证据、限制分开。
- 明确菜名/技巧名走实体定位 -> 稳定 ID -> PDS；精确命中不得调用全库向量。
- Recipe 第一步只能使用固定 recipe_step_anchor_v1 定位器，不接受任意关系、label、过滤或 LLM Cypher。
- 实体歧义不静默选择；实体不存在、PDS 不可用均有可审计降级。开关 RETRIEVAL_ENTITY_DIRECT_ENABLED 默认关闭。

### 阶段 3：QueryPlan 与目标化图查询

- LLM 只能提出 JSON 候选计划；validator 只允许固定 intent、template_id、实体类型、过滤字段和上限。
- 图查询必须参数化、方向明确、返回所有 node_id，覆盖 Recipe 步骤、食材到菜谱、食材搭配、技巧章节、可信菜系候选。
- “蔬菜” predicate 只能使用阶段 0 已证实分类。BELONGS_TO 与 BELONGS_TO_CATEGORY 不得混用。
- 关系不存在返回 GraphFact.status=not_found；图服务失败返回 unavailable。向量/PDS 文本永远不能证明关系。
- 开关 RETRIEVAL_QUERY_PLAN_ENABLED、RETRIEVAL_TARGETED_GRAPH_ENABLED 默认关闭。

### 阶段 4：受限向量检索与 Milvus V2

- V2 只从 PDS 的 CanonicalChunk 读取，绝不反推旧内存 chunk 或旧 collection。
- 以从未存在过的新 collection 名 cooking_knowledge_v2_<build> 建库；目标已存在即失败，禁止 force_recreate、drop_collection 与静默截断。
- schema、embedding 模型/维度、HNSW/COSINE 参数、长度、build_id、text_hash、chunk 顺序必须按实施方案冻结并由 describe_collection() 核验。
- 实现 “候选 parent_id 过滤 -> child chunk 召回 -> parent 聚合 -> PDS hydration”。空 parent scope 必须拒绝，不能退化为全库搜索。
- V2 的 PDS build、Milvus database、collection、schema hash 和回退值必须写入联合 retrieval_artifact_manifest.json；切换时原子更新，运行时不匹配即拒绝 hydration 并回退旧路径。
- 所有 snapshot、restore、build、cutover 命令均要求显式 database、collection、路径白名单。先备份旧 collection，再恢复到全新 verify collection 并执行检索验证；切换还要求受保护审批记录和人工确认。
- 旧 cooking_knowledge 至少保留 30 个自然日；本任务不删除它。开关 RETRIEVAL_MILVUS_V2_ENABLED 默认关闭。

### 阶段 5：营养/饮食属性与推荐

- 进入前必须由产品/数据治理冻结“低脂”的来源、单位、每份定义、阈值、审核、版本、过期和医疗边界。
- 有可信数值或治理标签时：Neo4j 硬过滤/排序 -> Recipe ID -> PDS 正文回补。
- 无硬证据时：Neo4j 先收集川菜 parent_id -> 受限 Milvus V2 检索 -> parent 聚合 -> PDS 回补；只可称为少油/清爽偏好，必须说明无法验证严格低脂。
- 用户要求脂肪克数、严格控脂或医疗饮食时，只返回硬证据匹配，或返回 evidence insufficient。
- Neo4j 不可用时，严格模式返回硬证据不可用；非严格模式也不得将全库结果称为川菜或低脂川菜。
- 开关 RETRIEVAL_STRICT_NUTRITION_ENABLED 默认关闭。

### 阶段 6：Recipe 生产、评测与旧路径迁移

- 新建确定性的 Recipe Markdown -> CSV 生产器、CSV manifest 与校验器；请求路径禁止递归扫描原始 Markdown。
- 图导入仅先写入独立 staging Neo4j 实例或新建隔离 staging database。apply 必须绑定已 verify 的 backup manifest/SHA、受控备份根、精确 database 白名单和审批记录。
- CSV dry-run 非破坏性；apply 是迁移动作。生产推广只允许写入新建隔离目标 database，再通过配置切读流量；本任务不授权覆盖、清空、删除或同库就地迁移。
- 固定评测覆盖所有 10 个场景，包括实体不存在、关系不存在、图服务失败。达到实施方案冻结的样本量、Recall@5、MRR@5、证据完整率、零禁止断言、P95 和观察窗口阈值后，才可从 allowlist 扩展流量。
- 由非实施者在 staging UI/API 做用户验收并签收。旧路径保留在 RETRIEVAL_LEGACY_FALLBACK_ENABLED 下，直到单独批准删除。

## 必须保持的用户可见行为

| 问题 | 允许的证据与行为 |
| --- | --- |
| 宫保鸡丁怎么做？ | Recipe ID -> PDS 全文；不默认全库向量检索。 |
| 宫保鸡丁第一步怎么腌？ | Recipe/CookingStep 稳定 ID -> 锚点窗口与必要上下文。 |
| 鸡肉能做什么？ | Ingredient <- REQUIRES - Recipe 的可解释图事实；用户要求做法时再回补正文。 |
| 鸡肉搭配什么蔬菜？ | Ingredient <- Recipe -> Ingredient，且每项有 Recipe 中介和已证实蔬菜分类。 |
| 推荐低脂川菜 | 严格模式只用可信营养证据；无硬证据只能是少油/清爽偏好，并说明限制。 |
| 夏天吃什么清淡的？ | 可做全库 child chunk 语义召回，但必须 parent 聚合和 PDS 回补。 |
| 腌肉有哪些关键要点和适用场景？ | TechniqueDoc/TechniqueChunk 的连续章节正文。 |
| 实体不存在 | 明确未定位；只有用户接受泛化建议时才给广义文本建议。 |
| 图关系不存在 | 明确图谱未找到关系，不让文本成为关系证明。 |
| 图服务失败 | 明确图证据不可用；文本只能标为非关系性烹饪参考。 |

## 最终交付格式

每次结束当前阶段时，用中文报告：

- 当前阶段及其 DoD 是否全部通过；
- 变更文件和稳定接口/数据契约；
- 已执行的测试、真实服务查询、用户场景验收及结果；
- feature flag、当前值、回退步骤和任何未演练项；
- 阻塞项及其所需环境、数据治理决策或用户授权；
- 分支名、提交号与中文标题、推送结果、PR 链接和状态；
- 未合并时明确写出“等待用户确认后合并 main”。

不要把“编写了代码”“创建了 collection”“测试部分通过”表述为阶段完成。只有实施方案中该阶段的所有门槛、测试、真实服务验证、验收、回退、提交和 PR 证据都完成时，才可以开始下一阶段。
