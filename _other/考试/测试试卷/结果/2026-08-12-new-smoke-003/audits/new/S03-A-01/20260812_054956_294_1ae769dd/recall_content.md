# Recall Content

audit_id: 20260812_054956_294_1ae769dd
## Evidence / 已验证图事实
- {"edges": [{"from": "tipdoc_820d789ff48e", "relationship": "HAS_CHUNK", "to": "tipchunk_385f8ad4281b"}, {"from": "tipdoc_820d789ff48e", "relationship": "HAS_CHUNK", "to": "tipchunk_45dfd39d40d1"}, {"from": "tipdoc_820d789ff48e", "relationship": "HAS_CHUNK", "to": "tipchunk_0ab647800ff9"}, {"from": "tipdoc_820d789ff48e", "relationship": "HAS_CHUNK", "to": "tipchunk_5d9abc8cea8f"}, {"from": "tipdoc_820d789ff48e", "relationship": "HAS_CHUNK", "to": "tipchunk_9dfcc67f4c73"}], "node_ids": ["tipdoc_820d789ff48e", "tipchunk_385f8ad4281b", "tipchunk_45dfd39d40d1", "tipchunk_0ab647800ff9", "tipchunk_5d9abc8cea8f", "tipchunk_9dfcc67f4c73"], "properties": {"database_timestamp": "2026-08-12T05:49:56.299+00:00", "direction": "TechniqueDoc - HAS_CHUNK -> TechniqueChunk", "max_candidates": 5, "relationship_type": "HAS_CHUNK", "rows": [{"chunk_order": 0, "chunk_title": "如何决策吃什么", "technique_chunk_id": "tipchunk_385f8ad4281b", "technique_doc_id": "tipdoc_820d789ff48e"}, {"chunk_order": 1, "chunk_title": "如何决策吃什么", "technique_chunk_id": "tipchunk_45dfd39d40d1", "technique_doc_id": "tipdoc_820d789ff48e"}, {"chunk_order": 2, "chunk_title": "如何决策吃什么", "technique_chunk_id": "tipchunk_0ab647800ff9", "technique_doc_id": "tipdoc_820d789ff48e"}, {"chunk_order": 3, "chunk_title": "如何决策吃什么", "technique_chunk_id": "tipchunk_5d9abc8cea8f", "technique_doc_id": "tipdoc_820d789ff48e"}, {"chunk_order": 4, "chunk_title": "如何决策吃什么", "technique_chunk_id": "tipchunk_9dfcc67f4c73", "technique_doc_id": "tipdoc_820d789ff48e"}]}, "template_id": "technique_chunks_v1"}

## Evidence / 正文证据
### parent_id=tipdoc_820d789ff48e build_id=pds_2a8c0807733eb8022a623659

来源：parent_store；chunk_ids=tipdoc_820d789ff48e:chunk:0,tipdoc_820d789ff48e:chunk:1,tipdoc_820d789ff48e:chunk:2,tipdoc_820d789ff48e:chunk:3,tipdoc_820d789ff48e:chunk:4,tipdoc_820d789ff48e:chunk:5,tipdoc_820d789ff48e:chunk:6,tipdoc_820d789ff48e:chunk:7；anchor_ids=无

# 如何决策吃什么

分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量

## 摘要
如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。

## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

## 计算方法
## 计算方法

## 计算荤菜和素菜数量
### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。

## 形式语言描述
#### 形式语言描述

当 有人数 `N` 时，
设 `素菜数` 为 `a`, `荤菜数`为 `b`。
`N`, `a`, `b`均为整数。

此时有下列不等式组：

* a + b = N + 1
* a ≤ b ≤ a+1

解得

```javascript
const a = Math.floor((N+1)/2);
const b = Math.ceil((N+1)/2);
```

## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。

## Evidence / 推荐证据等级
- 未使用营养或饮食推荐策略。

## Evidence / 限制与不可证明项
- 无额外限制。

