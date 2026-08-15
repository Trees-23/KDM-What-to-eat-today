# 真实服务考试预检

- 运行编号：`2026-08-11-真实考试-003`
- 预检关闭时间：`2026-08-11T22:25:23+08:00`
- 实现提交：`bdecb3e69c62cb478a5dcbcdd393c1551db75730`
- 当前分支：`codex/independent-exam`
- 目标基线：`origin/main` 的 `a22897275c26f89398b766af754c44452f2b35f6`
- 题库 SHA-256：`688edfea11db27a5cf5796ffa886e785f73c1f2ceb6a714f879830b3d06df88d`
- `题库校验报告.md` 声明的 SHA-256：`688edfea11db27a5cf5796ffa886e785f73c1f2ceb6a714f879830b3d06df88d`
- 静态题库重生成校验：`python _other/考试/工具/生成试卷.py` 已成功生成 300 题，SHA 与预检一致；检查后无题库或校验报告差异。

## 只读服务状态

- `GET /health`：`{"service":"RAG System","status":"healthy","timestamp":"2026-08-11 14:25:23.642155"}`
- Neo4j：节点 `3802`，关系 `16350`；仅执行了只读 MATCH 查询。
- PDS：`run/retrieval/parent_store.pds_2a8c0807733eb8022a623659.sqlite` 可读，parents=`341`，chunks=`1333`。
- Milvus V2 artifact 可读，内容保存在 `components/预检只读查询结果.json`；未执行导入、迁移、删除或任何写查询。
- Compose 容器状态：
```text
what-to-eat-backend|running|Up 33 minutes (healthy)
what-to-eat-frontend|exited|Exited (255) 7 hours ago
what-to-eat-milvus-etcd|running|Up 59 minutes (healthy)
what-to-eat-milvus-minio|running|Up 59 minutes (healthy)
what-to-eat-milvus-standalone|running|Up 59 minutes (healthy)
what-to-eat-neo4j|running|Up 59 minutes (healthy)
what-to-eat-neo4j-init|exited|Exited (0) 3 hours ago
what-to-eat-nginx|exited|Exited (255) 7 hours ago
```

## 实体与图路径复核

- S01/S02 的名称、类型与 sourcePath 精确解析：`60/60`。
- S03 的名称、类型与 sourcePath 精确解析：`10/30`；失败 `20` 题。
- S04 实际 Recipe-REQUIRES 路径非零：`30/30`。
- S05 A/B 实际目标多跳路径非零：`20/20`。
- S05 C 实际目标多跳路径为零：`10/10`；这是预期反例而非阻断原因。
- S08 虚构菜名命中：`0/30`；S09 虚构食材命中：`0/30`。

### S03 阻断明细

S03 有 20/30 题无法以题库声明的 TechniqueDoc 名称和 sourcePath 唯一解析：对应 sourcePath 存在 TechniqueDoc，但当前节点标题与题库 entity_name 不一致。因此无法在任何 API 请求前按题库契约冻结完整 gold_manifest。

- `S03-A-01`：题库名称 `如何选择现在吃什么`，sourcePath `data/tips/如何选择现在吃什么.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_820d789ff48e:如何决策吃什么`。
- `S03-A-02`：题库名称 `高级专业术语`，sourcePath `data/tips/advanced/高级专业术语.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_fdb80333cd59:做菜专业术语`。
- `S03-A-04`：题库名称 `油温判断技巧`，sourcePath `data/tips/advanced/油温判断技巧.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_b43f2b437984:油温判断技巧及常见温度和单位换算表`。
- `S03-A-07`：题库名称 `高压力锅`，sourcePath `data/tips/learn/高压力锅.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_4ba80da791e4:蒸（米）/炖（使用电饭煲/高压锅/电压力锅）`。
- `S03-A-08`：题库名称 `学习炒与煎`，sourcePath `data/tips/learn/学习炒与煎.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_29af79a321e3:炒/煎`。
- `S03-A-09`：题库名称 `微波炉`，sourcePath `data/tips/learn/微波炉.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_5e4d6d67fc39:使用微波炉`。
- `S03-A-10`：题库名称 `学习蒸`，sourcePath `data/tips/learn/学习蒸.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_9e62e8f43239:蒸`。
- `S03-B-01`：题库名称 `学习凉拌`，sourcePath `data/tips/learn/学习凉拌.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_fd7f557c37a7:凉拌`。
- `S03-B-02`：题库名称 `学习焯水`，sourcePath `data/tips/learn/学习焯水.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_897acc483178:焯水`。
- `S03-B-04`：题库名称 `空气炸锅`，sourcePath `data/tips/learn/空气炸锅.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_0899584efc31:使用空气炸锅`。
- `S03-B-05`：题库名称 `学习煮`，sourcePath `data/tips/learn/学习煮.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_beafa0e516d2:煮`。
- `S03-B-06`：题库名称 `学习腌`，sourcePath `data/tips/learn/学习腌.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_e5959b9d0464:腌（肉）`。
- `S03-B-08`：题库名称 `食材相克与禁忌`，sourcePath `data/tips/食材相克与禁忌.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_7e937e95d07f:揭秘食材搭配的智慧：这些食物不宜同食`。
- `S03-B-09`：题库名称 `油温判断技巧`，sourcePath `data/tips/advanced/油温判断技巧.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_b43f2b437984:油温判断技巧及常见温度和单位换算表`。
- `S03-C-02`：题库名称 `学习腌`，sourcePath `data/tips/learn/学习腌.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_e5959b9d0464:腌（肉）`。
- `S03-C-03`：题库名称 `学习焯水`，sourcePath `data/tips/learn/学习焯水.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_897acc483178:焯水`。
- `S03-C-04`：题库名称 `学习蒸`，sourcePath `data/tips/learn/学习蒸.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_9e62e8f43239:蒸`。
- `S03-C-05`：题库名称 `学习炒与煎`，sourcePath `data/tips/learn/学习炒与煎.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_29af79a321e3:炒/煎`。
- `S03-C-06`：题库名称 `空气炸锅`，sourcePath `data/tips/learn/空气炸锅.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_0899584efc31:使用空气炸锅`。
- `S03-C-07`：题库名称 `高压力锅`，sourcePath `data/tips/learn/高压力锅.md`，精确匹配 `0`；该 sourcePath 的当前 TechniqueDoc 为 `tipdoc_4ba80da791e4:蒸（米）/炖（使用电饭煲/高压锅/电压力锅）`。

## 预检结论

**失败，停止考试。** S03 有 20/30 题无法以题库声明的 TechniqueDoc 名称和 sourcePath 唯一解析：对应 sourcePath 存在 TechniqueDoc，但当前节点标题与题库 entity_name 不一致。因此无法在任何 API 请求前按题库契约冻结完整 gold_manifest。
未启动 old/new Compose 覆盖，未发送 `/api/chat/stream` 请求，未生成 SSE/HTTP 响应或运行时审计，未运行 S09/S10 隔离组件。
为满足逐题可复核性，old/new 各写 300 条 `blocked` 结果；这些行不是新旧路径的成功计分，也不构成安全通过。
