# RAG 模块优化实施计划

## 目标

本计划用于优化 `rag_modules/graph_rag_retrieval.py` 中的知识子图召回逻辑，并补齐 `TechniqueDoc` / `TechniqueChunk` 在项目全流程中的适配。

核心目标：

1. 知识子图召回能正确识别技巧类知识节点。
2. 命中 `TechniqueDoc` / `TechniqueChunk` 后能补齐同一技巧文档下的相关兄弟 chunk。
3. 最终召回上下文不只包含节点名和关系名，还要包含 `summary` / `content` 等正文证据。
4. `TechniqueDoc` / `TechniqueChunk` 能融入数据导入、图检索、混合检索、向量索引、生成、审计、评估全流程。
5. 每个子任务严格执行闭环：完成任务 -> 测试验证 -> 测试通过 -> 状态修改为成功。

## 执行规则

所有任务必须遵守以下流程：

```text
任务状态: pending
    ↓
开始实现，状态改为 in_progress
    ↓
完成代码或数据修改
    ↓
执行该任务指定测试
    ↓
测试通过
    ↓
状态改为 success
```

如果测试失败：

```text
测试失败
    ↓
记录失败原因
    ↓
整改
    ↓
重新测试
    ↓
测试通过后才允许进入下一子阶段
```

禁止事项：

1. 禁止跳过测试进入下一子阶段。
2. 禁止只做代码修改但不验证。
3. 禁止测试失败后把任务标记为成功。
4. 禁止只看最终 RAGAS 分数，不检查召回文本内容。
5. 禁止在未确认影响范围前重构无关模块。

任务状态只允许使用：

```text
pending
in_progress
blocked
failed
success
```

## 阶段 0：基线确认

### 0.1 记录当前 q087 基线结果

状态：success

任务：

1. 读取 `eval/result/ragas_scores.jsonl`。
2. 记录 q087 当前指标：
   - `faithfulness`
   - `answer_relevancy`
   - `context_recall`
   - `context_precision`
3. 读取 `eval/ragas_data_output/eval_results.jsonl`。
4. 记录 q087 当前 `retrieved_contexts` 是否包含：
   - `腌渍`
   - `腌渍基本概念`
   - `腌渍容器及时间`
   - `常用的腌渍用料`
   - `几种较为通用的腌渍公式`

测试命令：

```bash
python - <<'PY'
import json
from pathlib import Path

for path in [
    Path("eval/result/ragas_scores.jsonl"),
    Path("eval/ragas_data_output/eval_results.jsonl"),
]:
    print("FILE:", path)
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    print("rows:", len(rows))
    for row in rows:
        if row.get("id") == "q087":
            print(json.dumps(row.get("scores", {}), ensure_ascii=False, indent=2))
            contexts = row.get("retrieved_contexts", [])
            if contexts:
                text = "\n".join(contexts)
                for key in ["腌渍", "腌渍基本概念", "腌渍容器及时间", "常用的腌渍用料", "几种较为通用的腌渍公式"]:
                    print(key, key in text)
PY
```

通过标准：

1. 能成功读取两个结果文件。
2. 能明确记录当前召回缺口。

失败处理：

1. 如果文件不存在，先重新跑 quick test。
2. 如果 JSONL 解析失败，先修复结果文件或重新生成。

执行记录：

1. 已读取 `eval/result/ragas_scores.jsonl` 和 `eval/ragas_data_output/eval_results.jsonl`。
2. q087 当前基线：`faithfulness=0.6624`，`answer_relevancy=0.9251`，`context_recall=0.1429`，`context_precision=1.0000`。
3. 当前召回已包含 `腌渍`、`常用的腌渍用料`、`几种较为通用的腌渍公式`。
4. 当前召回未包含 `腌渍基本概念`、`腌渍容器及时间`。

## 阶段 1：子图意图推断适配 Technique 节点

### 1.1 扩展目标标签映射

状态：success

修改文件：

```text
rag_modules/graph_rag_retrieval.py
```

修改函数：

```python
_normalize_target_labels()
```

任务：

1. 将 `TechniqueDoc`、`TechniqueChunk` 加入 `valid_labels`。
2. 增加技巧类自然语言映射：
   - `技巧`
   - `知识`
   - `知识点`
   - `烹饪技巧`
   - `要点`
   - `注意事项`
   - `适用场景`
   - `场景`
   - `腌肉`
   - `腌制`
   - `腌渍`
3. 上述词应映射到 `TechniqueDoc` / `TechniqueChunk`。

测试命令：

```bash
python -m py_compile rag_modules/graph_rag_retrieval.py
```

补充测试：

```bash
python - <<'PY'
from rag_modules.graph_rag_retrieval import GraphRAGRetrieval

g = GraphRAGRetrieval.__new__(GraphRAGRetrieval)
print(g._normalize_target_labels(["烹饪技巧", "腌肉", "注意事项"]))
PY
```

通过标准：

1. Python 编译通过。
2. 输出中包含 `TechniqueDoc` 或 `TechniqueChunk`。

失败处理：

1. 如果编译失败，先修复语法。
2. 如果没有返回 Technique 标签，修正映射规则后重新测试。

执行记录：

1. 已将 `TechniqueDoc`、`TechniqueChunk` 加入目标标签映射。
2. 已执行 `python -m py_compile rag_modules/graph_rag_retrieval.py`，测试通过。
3. 已执行函数级测试，`烹饪技巧`、`腌肉`、`注意事项` 可映射到 Technique 标签。

### 1.2 扩展关系类型映射

状态：success

修改函数：

```python
_normalize_relation_types()
```

任务：

1. 将 `HAS_CHUNK` 加入 `valid_types`。
2. 增加技巧文档关系映射：
   - `章节`
   - `内容`
   - `知识点`
   - `技巧`
   - `要点`
   - `包含章节`
   - `文档分块`
3. 上述词应映射到 `HAS_CHUNK`。

测试命令：

```bash
python - <<'PY'
from rag_modules.graph_rag_retrieval import GraphRAGRetrieval

g = GraphRAGRetrieval.__new__(GraphRAGRetrieval)
print(g._normalize_relation_types(["包含章节", "知识点", "HAS_CHUNK"]))
PY
```

通过标准：

1. 输出中包含 `HAS_CHUNK`。
2. 原有关系映射不被破坏，例如 `步骤 -> CONTAINS_STEP` 仍可用。

执行记录：

1. 已将 `HAS_CHUNK` 加入关系类型映射。
2. 已执行函数级测试，`包含章节`、`知识点` 可映射到 `HAS_CHUNK`，`步骤` 仍可映射到 `CONTAINS_STEP`。

### 1.3 子图推断使用原始 query

状态：success

修改函数：

```python
extract_knowledge_subgraph()
_infer_subgraph_target_labels()
_infer_subgraph_relation_types()
graph_rag_search()
```

任务：

1. 将 `_infer_subgraph_target_labels(graph_query)` 改为 `_infer_subgraph_target_labels(graph_query, query)`。
2. 将 `_infer_subgraph_relation_types(graph_query)` 改为 `_infer_subgraph_relation_types(graph_query, query)`。
3. `hint_text` 必须包含：
   - 原始 query
   - `graph_query.source_entities`
   - `graph_query.target_entities`
   - `graph_query.relation_types`
4. 更新 audit 中记录的 `target_labels` 和 `relation_types`，确保传入 query 后输出一致。

测试命令：

```bash
python -m py_compile rag_modules/graph_rag_retrieval.py
```

补充测试：

```bash
python - <<'PY'
from rag_modules.graph_rag_retrieval import GraphRAGRetrieval, GraphQuery, QueryType

g = GraphRAGRetrieval.__new__(GraphRAGRetrieval)
q = GraphQuery(query_type=QueryType.SUBGRAPH, source_entities=["腌（肉）"], target_entities=[], relation_types=[])
print(g._infer_subgraph_target_labels(q, "请讲讲腌（肉）的关键要点，适合用在哪些烹饪场景？"))
print(g._infer_subgraph_relation_types(q, "请讲讲腌（肉）的关键要点，适合用在哪些烹饪场景？"))
PY
```

通过标准：

1. 输出能体现 `TechniqueDoc` / `TechniqueChunk`。
2. 输出能体现 `HAS_CHUNK`。

执行记录：

1. 已将 `_infer_subgraph_target_labels()` 和 `_infer_subgraph_relation_types()` 改为接收原始 query。
2. 已更新 `extract_knowledge_subgraph()` 和审计记录调用。
3. 已执行函数级测试，q087 查询可推断出 `TechniqueDoc`、`TechniqueChunk`、`HAS_CHUNK`。

## 阶段 2：命中技巧节点后补齐兄弟 chunk

### 2.1 新增技巧节点识别工具函数

状态：success

新增函数：

```python
_is_technique_node(node: Dict[str, Any]) -> bool
_collect_technique_node_ids(subgraph: KnowledgeSubgraph) -> List[str]
```

任务：

1. 判断节点 labels 是否包含 `TechniqueDoc` 或 `TechniqueChunk`。
2. 从 `central_nodes` 和 `connected_nodes` 中提取所有技巧节点 ID。
3. 去重并保持顺序。

测试命令：

```bash
python -m py_compile rag_modules/graph_rag_retrieval.py
```

通过标准：

1. 编译通过。
2. 函数可正确识别 `TechniqueDoc` / `TechniqueChunk`。

执行记录：

1. 已新增 `_is_technique_node()` 和 `_collect_technique_node_ids()`。
2. 已执行 `python -m py_compile rag_modules/graph_rag_retrieval.py`，测试通过。
3. 已执行函数级测试，`TechniqueDoc` / `TechniqueChunk` 可正确识别，普通 `Recipe` 不会误判。

### 2.2 新增兄弟 chunk 查询函数

状态：success

新增函数：

```python
_fetch_technique_sibling_chunks(node_ids: List[str], limit: int = 8) -> Dict[str, Any]
```

任务：

1. 如果命中 `TechniqueDoc`，查询其 `HAS_CHUNK` 下的 `TechniqueChunk`。
2. 如果命中 `TechniqueChunk`，先找到所属 `TechniqueDoc`，再查询同文档下的所有兄弟 chunk。
3. 按 `chunkOrder` 或 `chunkIndex` 排序。
4. 返回结构中必须包含：
   - doc 节点
   - chunk 节点列表
   - `HAS_CHUNK` 关系列表

建议 Cypher：

```cypher
UNWIND $node_ids AS node_id
MATCH (n {nodeId: node_id})
OPTIONAL MATCH (doc_from_chunk:TechniqueDoc)-[:HAS_CHUNK]->(n)
WITH collect(DISTINCT CASE WHEN n:TechniqueDoc THEN n ELSE doc_from_chunk END) AS docs
UNWIND docs AS doc
WITH DISTINCT doc
WHERE doc IS NOT NULL
MATCH (doc)-[r:HAS_CHUNK]->(chunk:TechniqueChunk)
RETURN doc, r, chunk
ORDER BY doc.nodeId, COALESCE(r.chunkOrder, chunk.chunkIndex, 999)
LIMIT $limit
```

测试命令：

```bash
docker exec what-to-eat-neo4j cypher-shell -u neo4j -p all-in-rag "
MATCH (doc:TechniqueDoc)-[r:HAS_CHUNK]->(chunk:TechniqueChunk)
WHERE doc.name CONTAINS '腌'
RETURN doc.name, chunk.name, chunk.sectionTitle
ORDER BY COALESCE(r.chunkOrder, chunk.chunkIndex, 999)
LIMIT 10
"
```

通过标准：

1. 能查询出 `腌（肉）` 的多个 chunk。
2. 至少包含 `腌渍`、`腌渍基本概念`、`常用的腌渍用料` 等章节。

执行记录：

1. 已新增 `_fetch_technique_sibling_chunks()`。
2. 已验证 Neo4j 中存在 `18` 个技巧文档、`120` 个技巧 chunk、`120` 条 `HAS_CHUNK` 关系。
3. 已验证 `腌（肉）` 可查询出 `9` 个同文档 chunk，包含 `腌渍`、`腌渍基本概念`、`腌渍容器及时间`、`常用的腌渍用料`、`几种较为通用的腌渍公式`。

### 2.3 将兄弟 chunk 合并进子图

状态：success

新增函数：

```python
_expand_technique_subgraph(subgraph: KnowledgeSubgraph, limit: int = 8) -> KnowledgeSubgraph
```

任务：

1. 从子图中识别技巧节点。
2. 查询同文档兄弟 chunk。
3. 将查询结果合并到 `connected_nodes` 和 `relationships`。
4. 使用 `_node_key()` 和 `_relationship_key()` 去重。
5. 更新 `graph_metrics` 中的节点数和关系数。

接入位置：

```python
subgraph = self.extract_knowledge_subgraph(graph_query)
subgraph = self._expand_technique_subgraph(subgraph)
```

测试命令：

```bash
python -m py_compile rag_modules/graph_rag_retrieval.py
```

通过标准：

1. 编译通过。
2. 后续 quick test 的召回文本中出现同文档多个技巧 chunk。

执行记录：

1. 已新增 `_expand_technique_subgraph()`。
2. 已将扩展逻辑接入 `extract_knowledge_subgraph()` 的返回路径。
3. 已执行 `python -m py_compile rag_modules/graph_rag_retrieval.py`，测试通过。

## 阶段 3：子图 Document 输出正文内容

### 3.1 新增节点详情格式化

状态：success

新增函数：

```python
_format_node_detail(node: Dict[str, Any], max_chars: int = 900) -> str
```

任务：

1. 对 `TechniqueChunk` 优先输出：
   - `sectionTitle`
   - `summary`
   - `content`
2. 对 `TechniqueDoc` 优先输出：
   - `title`
   - `summary`
   - `content`
3. 对 `CookingStep` 输出：
   - `description`
   - `technique`
   - `time`
4. 对 `Recipe` 输出：
   - `name`
   - `description`
   - `category`
   - `cuisineType`
5. 单个节点详情必须限制长度，避免 prompt 过长。

测试命令：

```bash
python -m py_compile rag_modules/graph_rag_retrieval.py
```

通过标准：

1. 编译通过。
2. 对技巧节点能输出 `content` 或 `summary`。

执行记录：

1. 已新增 `_format_node_detail()`。
2. 已执行 `python -m py_compile rag_modules/graph_rag_retrieval.py`，测试通过。
3. 已执行函数级测试，`TechniqueChunk.content` 可输出为正文片段。

### 3.2 子图描述增加技巧正文区

状态：success

修改函数：

```python
_build_subgraph_description()
```

任务：

1. 保留原有：
   - 知识子图主题
   - 子图规模
   - 关键节点
   - 关键关系
   - 图推理链
2. 新增 `关键技巧内容` 区域。
3. 如果子图中存在 `TechniqueChunk`，必须输出其正文。
4. 输出顺序优先按 `chunkIndex` 或 `chunkOrder`。

目标输出示例：

```text
关键技巧内容：
## 腌渍
在烹饪前腌制肉类是让肉类预先入味的常用方法...

## 腌渍基本概念
此处介绍的是正常口味的腌渍过程...

## 常用的腌渍用料
生抽：调酱香且带有咸味的底味...
```

测试命令：

```bash
python -m py_compile rag_modules/graph_rag_retrieval.py
```

通过标准：

1. 编译通过。
2. quick test 的 `eval/ragas_data_output/eval_results.jsonl` 中，`retrieved_contexts` 能看到技巧正文，而不是只有节点名。

执行记录：

1. 已新增 `_build_technique_content_sections()`。
2. 已修改 `_build_subgraph_description()`，新增 `关键技巧内容` 区域。
3. 已执行函数级测试，子图描述可输出技巧正文。
4. 端到端 quick test 将在阶段 5 统一验证。

## 阶段 4：TechniqueDoc / TechniqueChunk 全流程适配专项排查

阶段 4 是强制专项排查阶段。排查过程中如果发现任何模块尚未适配 `TechniqueDoc` / `TechniqueChunk`，或存在适配不完整、字段丢失、召回链路断裂、审计不可见等问题，必须在本阶段下新增独立子任务。

新增子任务必须遵守：

1. 明确遗漏模块和问题现象。
2. 明确修改文件和修改范围。
3. 明确测试命令和通过标准。
4. 完成修改后必须测试验证。
5. 测试失败必须整改并重新测试。
6. 测试通过后才能将该子任务状态改为 `success`。
7. 所有新增子任务均为 `success` 后，才允许进入阶段 5。

### 4.1 数据导入适配排查

状态：success

排查文件：

```text
data/cypher/generate_tips_csv.py
data/cypher/import_tips.cypher
data/cypher/neo4j_import.cypher
data/cypher/tips_nodes.csv
data/cypher/tips_relationships.csv
```

任务：

1. 确认 tips markdown 能生成 `TechniqueDoc` / `TechniqueChunk`。
2. 确认 `summary` / `content` / `sectionTitle` / `chunkIndex` 字段完整。
3. 确认 `HAS_CHUNK` 关系存在并带顺序字段。
4. 确认 Neo4j 中存在相关约束和索引。

测试命令：

```bash
docker exec what-to-eat-neo4j cypher-shell -u neo4j -p all-in-rag "
MATCH (d:TechniqueDoc)-[r:HAS_CHUNK]->(c:TechniqueChunk)
RETURN count(DISTINCT d) AS docs, count(c) AS chunks, count(r) AS rels
"
```

通过标准：

1. `docs > 0`
2. `chunks > 0`
3. `rels > 0`

执行记录：

1. 已执行 Neo4j 查询，结果为 `docs=18`、`chunks=120`、`rels=120`。
2. 数据导入链路已确认存在 `TechniqueDoc` / `TechniqueChunk` / `HAS_CHUNK`。

### 4.2 图数据准备适配排查

状态：success

排查文件：

```text
rag_modules/graph_data_preparation.py
```

任务：

1. 确认 `load_graph_data()` 加载 `TechniqueDoc` / `TechniqueChunk`。
2. 确认 `build_technique_documents()` 能构造 Document。
3. 确认 `chunk_documents()` 不破坏技巧文档元数据。

测试命令：

```bash
docker exec what-to-eat-backend python - <<'PY'
from config import DEFAULT_CONFIG
from rag_modules.graph_data_preparation import GraphDataPreparationModule

d = GraphDataPreparationModule(
    DEFAULT_CONFIG.neo4j_uri,
    DEFAULT_CONFIG.neo4j_user,
    DEFAULT_CONFIG.neo4j_password,
)
print(d.load_graph_data())
d.build_recipe_documents()
d.build_technique_documents()
chunks = d.chunk_documents()
print("documents", len(d.documents), "chunks", len(chunks))
print("technique docs", len(d.technique_docs), "technique chunks", len(d.technique_chunks))
d.close()
PY
```

通过标准：

1. `technique_docs > 0`
2. `technique_chunks > 0`
3. `documents` 和 `chunks` 包含技巧文档。

执行记录：

1. 已在后端容器执行图数据准备测试。
2. 结果为 `technique_docs=18`、`technique_chunks=120`、`documents=341`、`chunks=1333`。
3. 技巧文档已进入 Document/chunk 构建流程。

### 4.3 图索引适配排查

状态：success

排查文件：

```text
rag_modules/graph_indexing.py
```

任务：

1. 确认 `TechniqueDoc` 被加入实体 KV。
2. 确认 `TechniqueChunk` 被加入实体 KV。
3. 确认技巧类 tags、title、sectionTitle、summary、content 可参与索引。
4. 确认 `HAS_CHUNK` 关系可进入关系 KV。

测试命令：

```bash
python -m py_compile rag_modules/graph_indexing.py
```

通过标准：

1. 编译通过。
2. 代码中明确处理 `TechniqueDoc` / `TechniqueChunk` / `HAS_CHUNK`。

执行记录：

1. 已执行 `python -m py_compile rag_modules/graph_indexing.py`，测试通过。
2. 已确认 `graph_indexing.py` 中明确处理 `TechniqueDoc`、`TechniqueChunk` 和 `HAS_CHUNK`。

### 4.4 混合检索适配排查

状态：success

排查文件：

```text
rag_modules/hybrid_retrieval.py
rag_modules/intelligent_query_router.py
```

任务：

1. 确认 hybrid 检索不会过滤掉 `TechniqueDoc` / `TechniqueChunk`。
2. 确认实体级、主题级、向量级检索能返回技巧文档。
3. 确认路由器不会把技巧类问题错误路由到不支持技巧数据的路径。
4. 如果命中技巧 chunk，也应考虑补同文档兄弟 chunk。

测试命令：

```bash
python -m py_compile rag_modules/hybrid_retrieval.py rag_modules/intelligent_query_router.py
```

通过标准：

1. 编译通过。
2. quick test 中能看到技巧类上下文。

执行记录：

1. 已执行 `python -m py_compile rag_modules/hybrid_retrieval.py rag_modules/intelligent_query_router.py`，测试通过。
2. 已确认 `hybrid_retrieval.py` 关系抽取包含 `TechniqueDoc` / `TechniqueChunk`。
3. 阶段 5 quick test 发现 q087 实际策略为 `hybrid_traditional`，召回仍未包含 `腌渍基本概念` 和 `腌渍容器及时间`。
4. 结论：混合检索链路虽然能召回技巧文档，但没有补齐同文档兄弟 chunk，必须新增修复子任务。
5. 已通过 4.7 新增兄弟 chunk 扩展和最终上下文保底机制完成整改。
6. 复测 q087 的最终 `retrieved_contexts` 已包含技巧类正文、`腌渍基本概念` 和 `腌渍容器及时间`，混合检索适配通过。

### 4.7 混合检索命中技巧节点后补齐兄弟 chunk

状态：success

新增原因：

1. q087 当前实际走 `hybrid_traditional`。
2. `graph_rag_retrieval.py` 的子图增强不会影响该路径。
3. `hybrid_retrieval.py` 当前只返回命中的技巧 chunk 或技巧文档片段，未补同文档兄弟 chunk。

修改文件：

```text
rag_modules/hybrid_retrieval.py
```

任务：

1. 在混合检索合并后、rerank 前识别 `TechniqueDoc` / `TechniqueChunk`。
2. 命中 `TechniqueDoc` 时查询其 `HAS_CHUNK` 下的多个 chunk。
3. 命中 `TechniqueChunk` 时先找到所属 `TechniqueDoc`，再查询兄弟 chunk。
4. 生成一个高信息密度的补充 `Document`，包含 `sectionTitle` 和 `content`。
5. 将补充 Document 加入 rerank 候选池。
6. 确保不会影响普通菜谱召回。

测试命令：

```bash
python -m py_compile rag_modules/hybrid_retrieval.py
python eval/run_eval.py --input eval/user_input/quick_test_1.jsonl --max-workers 1 --allow-missing-metrics
```

通过标准：

1. 编译通过。
2. q087 的 `retrieved_contexts` 中包含 `腌渍基本概念`。
3. q087 的 `retrieved_contexts` 中包含 `腌渍容器及时间`。
4. q087 的 `context_recall` 高于当前基线 `0.1429`。

执行记录：

1. 已新增 `_collect_technique_node_ids_from_docs()`、`_fetch_technique_sibling_chunks()`、`_expand_technique_contexts()`，混合检索命中 `TechniqueDoc` / `TechniqueChunk` 后可补齐同文档兄弟 chunk。
2. 首轮 quick test 发现扩展文档进入 rerank 候选池，但被 reranker 排出最终 top-k，测试失败，未标记成功。
3. 已新增 `_ensure_technique_expansion_in_final()` 和 `_find_low_priority_replacement_index()`，在命中技巧节点且扩展文档未进入最终结果时执行最终上下文保底。
4. 已执行 `python -m py_compile rag_modules/hybrid_retrieval.py`，测试通过。
5. 已执行函数级测试，确认 `technique_expansion` 文档可替换低优先级普通结果并进入最终结果。
6. 已重启后端并执行 quick test：q087 `retrieved_contexts` 包含 `技巧文档扩展上下文`、`关键技巧内容`、`腌渍基本概念`、`腌渍容器及时间`、`常用的腌渍用料`、`几种较为通用的腌渍公式`。
7. q087 `context_recall` 从基线 `0.1429` 提升到 `0.8571`，召回闭环通过。

### 4.5 向量库适配排查

状态：success

排查文件：

```text
main.py
rag_modules/milvus_index_construction.py
```

任务：

1. 确认后端重建知识库时会调用 `build_technique_documents()`。
2. 确认 Milvus 中包含技巧文档 chunk。
3. 确认技巧文档 metadata 保留 `node_type` / `doc_type` / `parent_id`。

测试命令：

```bash
docker exec what-to-eat-backend python - <<'PY'
from config import DEFAULT_CONFIG
from rag_modules.milvus_index_construction import MilvusIndexConstructionModule

m = MilvusIndexConstructionModule(
    host=DEFAULT_CONFIG.milvus_host,
    port=DEFAULT_CONFIG.milvus_port,
    collection_name=DEFAULT_CONFIG.milvus_collection_name,
    dimension=DEFAULT_CONFIG.milvus_dimension,
    model_name=DEFAULT_CONFIG.embedding_model,
)
print("has collection:", m.has_collection())
print(m.similarity_search("腌肉的关键要点", k=5))
PY
```

通过标准：

1. 搜索结果中至少有一条来自技巧文档。
2. 如果没有，需要重建 Milvus collection。

执行记录：

1. 已在后端容器执行 Milvus 查询。
2. 首次测试发现需要先调用 `load_collection()`，补充后测试通过。
3. 查询 `腌肉的关键要点` 返回 5 条结果，均来自 `TechniqueDoc 腌（肉）`。

### 4.6 生成与审计适配排查

状态：success

排查文件：

```text
rag_modules/generation_integration.py
rag_modules/rag_audit.py
rag_modules/web_service_handler.py
```

任务：

1. 确认生成模块只依赖 `Document.page_content` 时，技巧正文已经进入上下文。
2. 确认审计文件能记录技巧类召回内容。
3. 确认 `recall_content.md` 中能看到 `TechniqueDoc` / `TechniqueChunk` 正文。

测试命令：

```bash
python eval/run_eval.py --input eval/user_input/quick_test_1.jsonl --max-workers 1
```

通过标准：

1. `run/<audit_id>/recall_content.md` 中包含技巧正文。
2. `eval/ragas_data_output/eval_results.jsonl` 中 `retrieved_contexts` 包含技巧正文。

执行记录：

1. 已检查 `run/20260509_152630_137_3af32998/recall_content.md`。
2. 审计文件中 `Hybrid Retrieval / Technique Expanded Context` 包含 `技巧文档扩展上下文`、`腌渍基本概念`、`腌渍容器及时间` 等正文。
3. 审计文件中 `Hybrid Retrieval / Top-K Final Retrieval Context` 已包含技巧扩展正文。
4. 已检查 `eval/ragas_data_output/eval_results.jsonl`，q087 的 `retrieved_contexts` 包含技巧正文。

## 阶段 5：端到端验证

### 5.1 快速单条验证

状态：failed

测试命令：

```bash
python eval/run_eval.py \
  --input eval/user_input/quick_test_1.jsonl \
  --max-workers 1
```

通过标准：

1. 脚本无异常退出。
2. 不出现非预期 `NaN`。
3. `context_recall` 高于当前基线。
4. `retrieved_contexts` 包含技巧正文。
5. 回答内容能覆盖：
   - 腌肉定义
   - 目的
   - 操作手法
   - 常用腌料
   - 时间控制
   - 适用场景

失败处理：

1. 如果 `context_recall` 仍低，检查兄弟 chunk 是否进入上下文。
2. 如果上下文有正文但回答没用，检查生成 prompt。
3. 如果检索不到技巧正文，回到阶段 1 到阶段 3 排查。

执行记录：

1. 已使用 `--allow-missing-metrics` 执行 q087 quick test。
2. 召回侧通过：`context_recall=0.8571`，高于基线 `0.1429`；`retrieved_contexts` 已包含技巧正文、`腌渍基本概念`、`腌渍容器及时间`。
3. 指标侧未完全通过：本轮结果中 `faithfulness=NaN`、`answer_correctness=NaN`，不满足“无非预期 NaN”的端到端通过标准。
4. 当前失败点不在召回链路，而在 RAGAS 指标计算稳定性或评估服务超时，需要单独整改后重新执行不带 `--allow-missing-metrics` 的 5.1 验证。

### 5.1A 图查询规划改为 LLM schema-first

状态：success

新增原因：

1. 当前 `_infer_subgraph_target_labels()` / `_infer_subgraph_relation_types()` 依赖 query 关键词硬匹配，和前置 `understand_graph_query()` 的 LLM 意图识别存在职责重复。
2. 更合理的方向是让 LLM 在查询规划阶段直接输出真实图谱 label 和 relationship type。
3. 硬匹配只保留为 fallback，避免 LLM 缺字段或输出自然语言时检索失效。

修改文件：

```text
rag_modules/graph_rag_retrieval.py
```

任务：

1. 扩展 `GraphQuery`，新增：
   - `target_labels`
   - `normalized_relation_types`
2. 修改 `understand_graph_query()` prompt，显式提供真实图谱 schema：
   - 节点标签：`Recipe`、`Ingredient`、`CookingStep`、`Category`、`DifficultyLevel`、`TechniqueDoc`、`TechniqueChunk`、`ConceptType`
   - 关系类型：`REQUIRES`、`CONTAINS_STEP`、`NEXT_STEP`、`BELONGS_TO_CATEGORY`、`BELONGS_TO`、`HAS_DIFFICULTY_LEVEL`、`DIFFICULTY_LEVEL`、`HAS_CONCEPT_TYPE`、`HAS_CHUNK` 等
3. 要求 LLM 输出 `target_labels` 和 `normalized_relation_types`。
4. 子图检索、多跳检索、实体关系检索优先使用 LLM 输出的规范字段。
5. 当规范字段缺失时，再退回 `_normalize_target_labels()` / `_normalize_relation_types()` 和 query 关键词兜底。

测试命令：

```bash
python -m py_compile rag_modules/graph_rag_retrieval.py
python - <<'PY'
from rag_modules.graph_rag_retrieval import GraphRAGRetrieval, GraphQuery, QueryType

g = GraphRAGRetrieval.__new__(GraphRAGRetrieval)

q = GraphQuery(
    query_type=QueryType.SUBGRAPH,
    source_entities=["腌（肉）"],
    target_entities=["技巧章节"],
    relation_types=["章节"],
    target_labels=["TechniqueDoc", "TechniqueChunk"],
    normalized_relation_types=["HAS_CHUNK"],
)
print(g._infer_subgraph_target_labels(q, "请讲讲腌肉要点"))
print(g._infer_subgraph_relation_types(q, "请讲讲腌肉要点"))

fallback = GraphQuery(
    query_type=QueryType.SUBGRAPH,
    source_entities=["腌肉"],
    target_entities=[],
    relation_types=[],
)
print(g._infer_subgraph_target_labels(fallback, "请讲讲腌肉要点"))
print(g._infer_subgraph_relation_types(fallback, "请讲讲腌肉要点"))
PY
```

通过标准：

1. 编译通过。
2. 规范字段测试优先返回 `TechniqueDoc`、`TechniqueChunk`、`HAS_CHUNK`。
3. fallback 测试在没有规范字段时仍能通过 query 推断出 `TechniqueDoc`、`TechniqueChunk`、`HAS_CHUNK`。

执行记录：

1. 已扩展 `GraphQuery`，新增 `target_labels` 和 `normalized_relation_types`。
2. 已修改 `understand_graph_query()` prompt，明确列出真实 Neo4j 节点标签和关系类型，并要求 LLM 返回规范字段。
3. 已新增 `_get_query_target_labels()` 和 `_get_query_relation_types()`，查询执行优先使用 LLM 输出的规范字段。
4. 已将多跳、子图、实体关系检索中的标签/关系获取改为 schema-first，硬匹配仅作为 fallback。
5. 已执行 `python -m py_compile rag_modules/graph_rag_retrieval.py`，测试通过。
6. 已执行函数级测试：规范字段优先返回 `TechniqueDoc`、`TechniqueChunk`、`HAS_CHUNK`；缺失规范字段时 fallback 仍能从 query 推断出同样结果。

### 5.2 低分集回归验证

状态：pending

测试命令：

```bash
python eval/run_eval.py \
  --input eval/user_input/low_score_43.jsonl \
  --max-workers 1
```

通过标准：

1. 技巧类问题的 `context_recall` 平均值提升。
2. 不因技巧类扩展导致菜谱类问题明显退化。
3. `context_precision` 不应明显下降。

### 5.3 标准 100 条验证

状态：pending

测试命令：

```bash
python eval/run_eval.py \
  --input eval/user_input/standard_100.jsonl \
  --max-workers 1
```

通过标准：

1. 整体 `context_recall` 比当前基线提升。
2. 整体 `context_precision` 保持稳定。
3. 技巧类问题召回内容不再只有节点名和关系名。

## 第一轮建议实施范围

第一轮只做低风险高收益修改：

1. 阶段 1：子图意图推断适配 Technique 节点。
2. 阶段 2：命中技巧节点后补齐兄弟 chunk。
3. 阶段 3：子图 Document 输出正文内容。
4. 阶段 4：TechniqueDoc / TechniqueChunk 全流程适配排查。

第一轮暂不做复杂语义 rerank，也暂不引入新的模型依赖。

## 成功判定

本轮优化完成的最低成功标准：

1. `graph_rag_retrieval.py` 编译通过。
2. 后端重启后无启动错误。
3. q087 quick test 成功跑完。
4. `retrieved_contexts` 中出现 `腌（肉）` 相关多个正文 chunk。
5. `context_recall` 相比当前基线提升。
6. TechniqueDoc / TechniqueChunk 已完成全流程排查，无明显遗漏适配点。
