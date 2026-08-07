# GraphRAG 评测方案与执行指南

适用项目：

- `/home/kdm/MyWorkSpace/AgentLearnSpace/AllProjects/What-to-eat-today-main/What-to-eat-today-main`

目标：

- 给当前项目设计两套可落地的评测方案
- 重点评估 `RAG 召回效果` 和 `切片策略`
- 帮助回答面试中关于“为什么这么切”“召回率怎么测”“有没有测试过”的问题

---

## 1. 先背的切片依据回答

可以直接背这一段：

> 当前切片采用“结构优先、长度兜底”的策略。先把菜谱、食材和步骤组织成结构化菜谱文档；对于短文档直接整篇保留，对于长文档优先按 `##` 章节标题切分，尽量保持描述、食材、步骤等业务语义单元完整；如果文档没有明显章节边界，再退化为固定长度加 overlap 的滑窗切片。`chunk_size=500`、`chunk_overlap=50` 主要是工程折中，目标是在检索粒度和语义完整性之间取得平衡。根据项目 `data` 目录下 Markdown 文档统计，约 80% 文档超过 500 字符，中位数约 710 字符，因此 500 这个阈值在当前数据分布下是有效的。当前方案优点是简单稳定、贴合菜谱结构，缺点是章节内部尤其步骤部分切得还不够细，后续可以继续做步骤级切分、语义切分或 small-to-big 检索优化。

补充统计：

- Markdown 文档数：341
- 超过 500 字符：274 篇，约 80.4%
- 中位数：710 字符
- 75 分位：901 字符
- 90 分位：1180 字符
- 最长：4797 字符

注意：

- 当前代码里的 `chunk_size=500` 指的是 **字符数**，不是 token 数。
- 如果要更严谨，后续可以补一轮 tokenizer 维度的 token 分布统计。

---

## 2. 项目现状判断

当前项目适合分两层评测：

### 第一层：检索与切片离线评测

目的：

- 不依赖 LLM 主观打分
- 先回答“切片策略是否合理”“召回是否命中证据”
- 成本低、最适合先做

### 第二层：端到端 RAG 输出质量评测

目的：

- 测最终问答质量
- 看 GraphRAG、混合检索、路由系统对最终回答有没有帮助
- 这层可以考虑引入 `Ragas`，也可以结合 `LangSmith` 做链路跟踪

---

## 3. 两套评测方案

## 方案 A：不依赖评审模型的检索/切片评测

### 适用场景

- 你想先验证：
  - `chunk_size=500 / overlap=50` 是否合理
  - 按章节切 vs 固定长度切哪个更好
  - 图RAG / 混合检索 / 向量检索谁更容易召回关键证据

### 核心思路

人工构造一批问答测试集，每条 query 手动标注：

- 正确答案应依赖的 `recipe_name`
- 或者关键 `node_id / parent_id / chunk_id`
- 或者关键证据关键词

然后对比不同检索配置下的：

- Top-1 命中率
- Top-3 命中率
- Top-5 命中率
- MRR
- 命中证据的平均排名

### 你要评什么

#### 1. 切片策略对比

至少对比这 3 组：

- 基线 1：当前策略
  - 短文档不切
  - 长文档优先按 `##` 章节切
  - 无章节时按 `500/50` 滑窗切

- 基线 2：纯长度切片
  - 不按章节
  - 统一 `500/50`

- 基线 3：更细粒度切片
  - 比如 `300/30`
  - 或按 `##` 切后，制作步骤再按 `### 第i步` 细分

#### 2. 召回链路对比

至少对比这 4 组：

- 仅向量检索
- 传统混合检索（`HybridRetrievalModule.hybrid_search`）
- 仅图RAG检索
- 智能路由完整链路

### 推荐 query 类型

最好覆盖 5 类：

1. 实体查找：
   - `宫保鸡丁怎么做`
   - `糖醋排骨需要什么食材`

2. 主题问答：
   - `推荐几个下饭菜`
   - `有哪些适合早餐的简单做法`

3. 关系问答：
   - `鸡肉适合搭配什么蔬菜`
   - `哪些菜属于川菜`

4. 流程问答：
   - `蒸水蛋的步骤是什么`
   - `炸鲜奶怎么做`

5. 多跳/复杂问答：
   - `为什么这道菜适合新手`
   - `和宫保鸡丁类似的菜有哪些`

### 推荐评测指标

- `Recall@1`
- `Recall@3`
- `Recall@5`
- `MRR`
- `Hit Position Avg`
- `Chunk Count Avg`

### 这套方案的好处

- 不依赖额外大模型判分
- 指标最清楚
- 最适合回答“有没有做召回测试”
- 最适合验证切片策略

### 这套方案的不足

- 只能说明“证据召回得对不对”
- 不能直接说明“最终回答是否好”

---

## 方案 B：端到端 RAG 输出质量评测

### 适用场景

- 你已经先做完方案 A
- 想进一步回答：
  - 最终答案有没有提升
  - 图RAG和路由是否改善了最终问答效果
  - 有没有减轻答非所问和幻觉

### 核心思路

对同一批 query，跑不同方案的最终答案，然后对答案做质量评估。

你可以选两种方式：

#### 方式 1：人工评测

人工打标签：

- 是否答对
- 是否答全
- 是否包含明显幻觉
- 是否引用到了正确证据
- 是否可解释

优点：

- 最稳
- 不依赖额外工具

缺点：

- 成本高

#### 方式 2：Ragas + 可选 LangSmith

适合中后期。

Ragas 可用来评估：

- answer relevancy
- faithfulness
- context recall
- context precision

LangSmith 更适合做：

- 链路追踪
- prompt / retriever 版本对比
- 运行样本管理

### 当前项目要不要直接上 Ragas / LangSmith

建议：

- **先做方案 A**
- 再上 **Ragas**
- `LangSmith` 是加分项，不是必须项

原因：

- 你现在最缺的是“切片与召回的硬证据”
- 不是一上来就做 LLM Judge
- 检索没测清楚，直接做端到端评测很容易定位不清问题来源

### 推荐端到端对比组

- 仅向量检索 + 生成
- 传统混合检索 + 生成
- 图RAG检索 + 生成
- 智能路由完整链路 + 生成

### 推荐评测维度

- `Answer Correctness`
- `Answer Completeness`
- `Faithfulness`
- `Context Relevance`
- `Hallucination Rate`
- `Latency`

### 这套方案的好处

- 能衡量最终用户感知效果
- 适合做汇报、论文式总结、面试结果展示

### 这套方案的不足

- 成本更高
- 更依赖模型
- 不如方案 A 那么容易定位问题

---

## 4. 推荐执行顺序

建议按这个顺序做：

1. 先整理测试 query 集
2. 先做方案 A：召回/切片离线评测
3. 先选出表现更好的切片方案
4. 再做方案 B：最终答案质量评测
5. 如果时间足够，再接入 `Ragas`
6. 如果后续做大量实验，再接 `LangSmith`

一句话：

> `先测检索，再测答案；先做硬指标，再做 LLM Judge。`

---

## 5. 前置条件

在开始评测前，至少满足以下条件：

### 环境前置

- 已能正常启动项目
- Neo4j 正常运行
- Milvus 正常运行
- embedding 模型可用
- LLM API 可用

### 数据前置

- Neo4j 中已导入图数据
- Milvus 中已完成向量索引构建
- 当前 `build_recipe_documents()` 和 `chunk_documents()` 可以顺利执行

### 代码前置

你至少要能调用这几条主链路：

- `GraphDataPreparationModule.build_recipe_documents()`
- `GraphDataPreparationModule.chunk_documents()`
- `HybridRetrievalModule.hybrid_search()`
- `GraphRAGRetrieval.graph_rag_search()`
- `IntelligentQueryRouter.route_query()`

---

## 6. 建议的 test 目录结构

建议在 `/test` 下这样组织：

```text
test/
├── README_evaluation_plan.md
├── datasets/
│   ├── retrieval_eval_queries.csv
│   ├── retrieval_eval_queries.md
│   └── generation_eval_queries.csv
├── configs/
│   ├── chunk_strategy_baseline.json
│   ├── chunk_strategy_small.json
│   └── chunk_strategy_stepwise.json
├── results/
│   ├── retrieval/
│   ├── generation/
│   └── comparison/
└── notebooks/
    └── eval_analysis.ipynb
```

如果你现在只想先落一个最小版本，可以先建：

```text
test/
├── README_evaluation_plan.md
├── datasets/
│   └── retrieval_eval_queries.csv
└── results/
```

---

## 7. retrieval 评测数据模板

建议先人工写一个 CSV，字段至少包含：

```csv
query,query_type,gold_recipe_name,gold_parent_id,gold_keywords,notes
宫保鸡丁怎么做,entity,宫保鸡丁,,鸡肉|花生|步骤,实体型问题
鸡肉适合搭配什么蔬菜,relation,,,鸡肉|蔬菜|搭配,关系型问题
推荐几个早餐做法,theme,,,早餐|简单|推荐,主题型问题
蒸水蛋的步骤是什么,process,蒸水蛋,,蒸水蛋|步骤|蒸,流程型问题
和宫保鸡丁类似的菜有哪些,multihop,宫保鸡丁,,类似|川菜|鸡丁,复杂型问题
```

说明：

- `gold_recipe_name`：适合实体明确的问题
- `gold_parent_id`：适合你后续程序化命中判断
- `gold_keywords`：适合复杂问题做辅助判断

建议第一版先做 30 到 50 条 query，按 5 类问题平均分配。

---

## 8. 切片策略对比建议

至少准备这 3 组：

### 方案 S1：当前默认方案

- `chunk_size = 500`
- `chunk_overlap = 50`
- 优先按 `##` 标题切

### 方案 S2：更小粒度方案

- `chunk_size = 300`
- `chunk_overlap = 30`
- 仍保留标题切分

目的：

- 看更细粒度是否提高精确召回
- 代价是可能造成上下文太碎

### 方案 S3：步骤增强方案

- 标题切分后
- `## 制作步骤` 章节再按 `### 第i步` 细分

目的：

- 看流程问题是否更容易命中步骤证据

---

## 9. 推荐的测试场景

### 场景 A：实体精确问题

例子：

- `糖醋排骨怎么做`
- `蒸水蛋需要什么材料`

关注：

- 实体 chunk 是否能排进 Top-3

### 场景 B：主题问题

例子：

- `推荐几个适合早餐的做法`
- `有哪些家常下饭菜`

关注：

- 主题级检索和向量检索谁贡献更大

### 场景 C：流程问题

例子：

- `炸鲜奶的步骤是什么`
- `提拉米苏怎么分步骤做`

关注：

- 当前“按 `##` 切”是否足够
- 是否需要对 `制作步骤` 再细分

### 场景 D：关系问题

例子：

- `鸡肉适合搭配什么蔬菜`
- `哪些菜属于川菜`

关注：

- 图RAG是否比纯向量更容易命中证据

### 场景 E：多跳复杂问题

例子：

- `和宫保鸡丁类似的菜有哪些`
- `为什么这道菜适合新手`

关注：

- 智能路由和图RAG是否优于传统混合检索

---

## 10. 推荐的结果记录方式

建议每次实验保存一份 CSV：

```csv
query,method,chunk_strategy,top_k,hit_at_1,hit_at_3,hit_at_5,mrr,first_hit_rank,retrieved_recipe_names,notes
宫保鸡丁怎么做,hybrid,baseline,5,1,1,1,1.0,1,宫保鸡丁|辣子鸡|鱼香肉丝,命中很好
鸡肉适合搭配什么蔬菜,graph_rag,baseline,5,0,1,1,0.5,2,宫保鸡丁|青椒鸡丁|黄焖鸡,需要看图路径质量
```

这样后面可以很方便比较：

- 不同方法
- 不同切片
- 不同 query 类型

---

## 11. 什么时候用 Ragas

### 建议使用时机

当你已经完成以下事情后，再上 Ragas：

- query 数据集已整理好
- 检索层的召回评测已跑完
- 你已经知道哪种切片更合理

### 为什么不建议一上来就用

因为你现在最核心的问题不是“最终回答文本优不优雅”，而是：

- 检索证据有没有召回来
- 切片是不是合理
- 哪条链路更适合哪种 query

这些问题先用 Ragas 解决不够直接。

---

## 12. 什么时候用 LangSmith

LangSmith 更适合：

- 做链路 trace
- 记录每次实验配置
- 看每次 query 走了哪条链
- 对比 prompt / retriever 版本

如果你后续想做很多实验、反复对比版本，LangSmith 会很有帮助。

但如果你当前只是做第一轮评测：

- 它不是必须项
- 先用本地 CSV + Markdown + notebook 就够了

---

## 13. 当前项目最适合的建议

最推荐的落地路径：

### 第一步

先做一份 `retrieval_eval_queries.csv`

### 第二步

先只比较：

- 当前切片方案
- 更小粒度切片方案
- 步骤细分方案

在下面 4 条检索链路上的差异：

- vector only
- hybrid
- graph_rag
- routed

### 第三步

拿到硬指标后，再做端到端答案评测。

### 第四步

如果时间还够，再加：

- `Ragas`
- `LangSmith`

---

## 14. 面试时可以怎么说

你可以这么回答：

> 我给这个项目设计了两层评测。第一层是离线检索评测，重点验证切片策略和召回效果，通过人工标注 query 的 gold recipe 或 gold evidence，比较不同切片方案和检索链路的 Recall@K、MRR 等指标；第二层是端到端 RAG 输出质量评测，评估最终答案的正确性、完整性和幻觉情况。我的执行顺序是先测检索再测答案，先做不依赖评审模型的硬指标，再视需要接入 Ragas 做自动评估，LangSmith 更多用于后续链路追踪和实验管理。

---

## 15. 当前缺口与后续建议

当前项目还缺：

- 专门的评测数据集
- 自动化评测脚本
- 检索层结果落盘与统计脚本
- 端到端答案评分脚本

建议下一步优先补：

1. `test/datasets/retrieval_eval_queries.csv`
2. 一版最小可用 retrieval 评测脚本
3. 一版切片策略对比脚本

如果你愿意，我下一步最值得做的不是继续写说明，而是直接补下面两个文件：

- `test/datasets/retrieval_eval_queries.csv` 模板
- `test/eval_retrieval_plan.md` 或一版最小评测脚本

这样你就可以真正开始跑实验，而不是停留在方案层。
