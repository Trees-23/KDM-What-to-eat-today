# Recall Content

audit_id: 20260811_165908_806_22aa07b3
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=tipdoc_820d789ff48e, recipe_name=如何决策吃什么, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧文档: 如何决策吃什么
分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
来源: tips/如何选择现在吃什么.md

补充信息: 技巧章节: 如何决策吃什么
章节: 正文
分类: 通用知识
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
内容: # 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=tipchunk_0ab647800ff9, recipe_name=如何决策吃什么 / 计算荤菜和素菜数量, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算荤菜和素菜数量
章节: 计算荤菜和素菜数量
分类: 通用知识
摘要: 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
内容: ### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=tipchunk_45dfd39d40d1, recipe_name=如何决策吃什么 / 计算方法, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算方法
章节: 计算方法
分类: 通用知识
摘要: 计算方法
内容: ## 计算方法
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=3
source: entity_level
metadata_summary: node_id=tipchunk_5d9abc8cea8f, recipe_name=如何决策吃什么 / 形式语言描述, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 形式语言描述
章节: 形式语言描述
分类: 通用知识
摘要: 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得
内容: #### 形式语言描述

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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=4
source: entity_level
metadata_summary: node_id=tipchunk_9dfcc67f4c73, recipe_name=如何决策吃什么 / 菜的选择, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 菜的选择
章节: 菜的选择
分类: 通用知识
摘要: 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
内容: ### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
_no content_

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.815475344657898, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1235, recipe_name=如何决策吃什么, category=通用知识, score=0.7345408201217651, search_type=vector_enhanced

```text
## 摘要
如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1234, recipe_name=如何决策吃什么, category=通用知识, score=0.7218552231788635, search_type=vector_enhanced

```text
# 如何决策吃什么

分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6307581067085266, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6242837309837341, search_type=vector_enhanced

```text
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.6150272488594055, search_type=vector_enhanced

```text
## 食用（此流程必选）
### 食用（此流程必选）

* 将搅拌后的食材直接食用
* 将未搅拌的主食材蘸取蘸料后食用
* 将食材与蘸料加入主食中食用
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1149, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6079573631286621, search_type=vector_enhanced

```text
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1150, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6079573631286621, search_type=vector_enhanced

```text
## 烹饪建议

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.5924526453018188, search_type=vector_enhanced

```text
## 所需食材
1. 味素(5克)
2. 姜(5克)
3. 盐(15克)
4. 葱(5克)
5. 蒜(5克)
6. 西红柿(1个)
7. 食用油(15毫升)
8. 香油(2滴)
9. 鸡蛋(1-2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.5892803072929382, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, recipe_name=如何决策吃什么, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧文档: 如何决策吃什么
分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
来源: tips/如何选择现在吃什么.md

补充信息: 技巧章节: 如何决策吃什么
章节: 正文
分类: 通用知识
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
内容: # 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=tipchunk_0ab647800ff9, recipe_name=如何决策吃什么 / 计算荤菜和素菜数量, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算荤菜和素菜数量
章节: 计算荤菜和素菜数量
分类: 通用知识
摘要: 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
内容: ### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=tipchunk_45dfd39d40d1, recipe_name=如何决策吃什么 / 计算方法, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算方法
章节: 计算方法
分类: 通用知识
摘要: 计算方法
内容: ## 计算方法
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=tipchunk_5d9abc8cea8f, recipe_name=如何决策吃什么 / 形式语言描述, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 形式语言描述
章节: 形式语言描述
分类: 通用知识
摘要: 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得
内容: #### 形式语言描述

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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=tipchunk_9dfcc67f4c73, recipe_name=如何决策吃什么 / 菜的选择, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 菜的选择
章节: 菜的选择
分类: 通用知识
摘要: 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
内容: ### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.815475344657898, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1235, recipe_name=如何决策吃什么, category=通用知识, score=0.7345408201217651, search_type=vector_enhanced

```text
## 摘要
如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1234, recipe_name=如何决策吃什么, category=通用知识, score=0.7218552231788635, search_type=vector_enhanced

```text
# 如何决策吃什么

分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6307581067085266, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6242837309837341, search_type=vector_enhanced

```text
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.6150272488594055, search_type=vector_enhanced

```text
## 食用（此流程必选）
### 食用（此流程必选）

* 将搅拌后的食材直接食用
* 将未搅拌的主食材蘸取蘸料后食用
* 将食材与蘸料加入主食中食用
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1149, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6079573631286621, search_type=vector_enhanced

```text
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1150, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6079573631286621, search_type=vector_enhanced

```text
## 烹饪建议

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.5924526453018188, search_type=vector_enhanced

```text
## 所需食材
1. 味素(5克)
2. 姜(5克)
3. 盐(15克)
4. 葱(5克)
5. 蒜(5克)
6. 西红柿(1个)
7. 食用油(15毫升)
8. 香油(2滴)
9. 鸡蛋(1-2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.5892803072929382, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=tipdoc_820d789ff48e, recipe_name=如何决策吃什么, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧文档: 如何决策吃什么
分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
来源: tips/如何选择现在吃什么.md

补充信息: 技巧章节: 如何决策吃什么
章节: 正文
分类: 通用知识
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
内容: # 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=tipchunk_0ab647800ff9, recipe_name=如何决策吃什么 / 计算荤菜和素菜数量, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算荤菜和素菜数量
章节: 计算荤菜和素菜数量
分类: 通用知识
摘要: 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
内容: ### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=tipchunk_45dfd39d40d1, recipe_name=如何决策吃什么 / 计算方法, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算方法
章节: 计算方法
分类: 通用知识
摘要: 计算方法
内容: ## 计算方法
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=tipchunk_5d9abc8cea8f, recipe_name=如何决策吃什么 / 形式语言描述, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 形式语言描述
章节: 形式语言描述
分类: 通用知识
摘要: 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得
内容: #### 形式语言描述

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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=tipchunk_9dfcc67f4c73, recipe_name=如何决策吃什么 / 菜的选择, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 菜的选择
章节: 菜的选择
分类: 通用知识
摘要: 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
内容: ### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6242837309837341, search_type=vector_enhanced

```text
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.6150272488594055, search_type=vector_enhanced

```text
## 食用（此流程必选）
### 食用（此流程必选）

* 将搅拌后的食材直接食用
* 将未搅拌的主食材蘸取蘸料后食用
* 将食材与蘸料加入主食中食用
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1150, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6079573631286621, search_type=vector_enhanced

```text
## 烹饪建议

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.5924526453018188, search_type=vector_enhanced

```text
## 所需食材
1. 味素(5克)
2. 姜(5克)
3. 盐(15克)
4. 葱(5克)
5. 蒜(5克)
6. 西红柿(1个)
7. 食用油(15毫升)
8. 香油(2滴)
9. 鸡蛋(1-2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipchunk_0ab647800ff9,tipchunk_45dfd39d40d1,tipchunk_5d9abc8cea8f,tipchunk_9dfcc67f4c73, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 使用空气炸锅
关键技巧内容:
## 正文
# 使用空气炸锅
## 什么是空气炸锅
## 什么是空气炸锅

空气炸锅为一种电子炊具，用空气替代原本热油加热，让食物变熟，令食材无需遇油也能达到近似油炸的效果。
## 工作方式
### 工作方式

空气炸锅借由上方的加热器产生高温热风，让热空气在食物周遭循环对流，快速加热食物自身的油脂，带走食物的水分，产生油炸的效果，并创造类似油炸食物的酥脆感。
## 优点
### 优点

* 由于无需添加食用油，因此可以**大幅减少**摄入含有高量脂肪和热量的食用油。
* 高速循环的热空气使食物脱水，表面变得金黄酥脆，让食物变得外焦里嫩。
* 操作简单，对新人友好。
## 流程
## 流程

* 将空气炸锅放在稳固、平整且水平的隔热表面上。
* 取出煎锅，将食材放入炸篮，将煎锅滑入产品中。
* 修改预设温度，旋转旋钮调整烹饪时间。
* 调整好烹饪时间后，产品将开始烹饪，等待定时器响铃时烹饪完成。
* 将炸篮中的食物全部倒入碗或碟中。务必从所用煎锅中取出装有原料的炸篮，因为煎锅底部**可能残留有热油或油脂**。
## 注意事项
## 注意事项

* 使用空气炸锅应注意设置温度不宜过高（尽量在 120℃内，最好不超过 168℃），制作时间不宜太长（约 10 分钟左右），避免生成过多有害成分[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)。
* 减少用空气炸锅烹饪淀粉类食物，如土豆、面包、油条等，可相应减少[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)摄入。相对而言，空气炸锅适合烹调脂肪或水分含量更高的食物，如肉类、蔬菜。
* 使用过程中，不能遮挡顶部的进风口和背面的出风口。用手遮挡的话，可能会被**热空气烫伤**。
* 不同品牌炸锅温差可达±10℃，首次尝试建议减少 10%时间后逐步调整
## 烹饪建议
## 烹饪建议
## 常用食物
### 常用食物

| 食物名称 | 温度(℃) | 时间（分钟） | 方法步骤 |
|---------|---------|--------|--------------------------------------------------------------------|
| **薯条** | 200 | 15-20 | 1. 冷冻薯条无需解冻，表面喷少量油；- 2. 平铺炸篮（不重叠），每5分钟摇晃一次；- 3. 最后2分钟可调至210℃上色。 |
| **鸡翅** | 180 | 18-22 | 1. 鸡翅划刀，用生抽、料酒、蚝油、蒜末腌制1小时；- 2. 平铺炸篮，表面刷蜂蜜水；- 3. 烤10分钟后翻面继续烤。 |
| **鱼类** | 180-190 | 12-15 | 1. 鱼身两面划刀，用姜片、葱段、盐、料酒腌制20分钟；- 2. 鱼表面刷油，垫锡纸防粘；- 3. 中途翻面一次。 |
| **牛排** | 200 | 8-12 | 1. 牛排室温回温，双面撒盐、黑胡椒和橄榄油；- 2. 空气炸锅预热5分钟，牛排放入后根据厚度烤制（每面4-6分钟）。 |
| **牛肉块** | 180 | 15-18 | 1. 牛肉切2cm立方块，用生抽、淀粉、黑胡椒腌制30分钟；- 2. 平铺炸篮，烤10分钟后翻动一次；- 3. 可加洋葱、彩椒同烤。 |
| **猪肉排** | 175-185 | 16-20 | 1. 猪排用刀背拍松，生抽、蒜粉、五香粉腌制40分钟；- 2. 表面喷油，垫烘焙纸；- 3. 中途翻面并刷腌料汁。 |
| **蛋挞** | 170-180 | 12-15 | 1. 蛋挞皮解冻后倒入自制蛋液（牛奶+淡奶油+糖+蛋黄）；- 2. 炸锅无需预热，烤至挞皮金黄、中心微焦即可。 |
| **蛋糕** | 160 | 25-30 | 1. 6寸模具垫油纸，倒入蛋糕糊（7分满）；- 2. 低温慢烤，插入牙签无粘连即熟；- 3. 倒扣冷却防塌陷。 |
| **披萨** | 180-190 | 8-12 | 1. 冷冻披萨无需解冻，可撒额外芝士；-
## 操作要点
### 操作要点

1. **预处理关键**
 - 肉类需充分解冻并擦干表面水分（牛排/猪排建议室温回温）
 - 冷冻食品（薯条/披萨）可直接烹饪，但需加大摇晃/翻面频率

2. **防粘技巧**
 - 鱼类/蛋糕等易粘食物建议垫烘焙纸或锡纸
 - 炸篮底部可铺洋葱片/柠檬片提升风味并隔离汁水

3. **上色控制**
 - 最后 2-3 分钟调高 10-20℃可使表面更酥脆（适用于薯条/鸡翅）
 - 蛋挞/蛋糕表面加盖锡纸可防止过度焦化

4. **熟度检测**
 - 肉类：用筷子按压，硬挺为全熟，柔软带弹性为半熟
 - 蛋糕：牙签插入中心无面糊粘连即熟
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 如何决策吃什么
技巧文档: 如何决策吃什么
分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
来源: tips/如何选择现在吃什么.md

补充信息: 技巧章节: 如何决策吃什么
章节: 正文
分类: 通用知识
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
内容: # 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算荤菜和素菜数量
章节: 计算荤菜和素菜数量
分类: 通用知识
摘要: 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
内容: ### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算方法
章节: 计算方法
分类: 通用知识
摘要: 计算方法
内容: ## 计算方法
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 形式语言描述
章节: 形式语言描述
分类: 通用知识
摘要: 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得
内容: #### 形式语言描述

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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 菜的选择
章节: 菜的选择
分类: 通用知识
摘要: 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
内容: ### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### pair_order=5
source: rerank_input

```text
菜品: 汤面
菜系: 未知
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=6
source: rerank_input

```text
菜系: 技巧知识
## 食用（此流程必选）
### 食用（此流程必选）

* 将搅拌后的食材直接食用
* 将未搅拌的主食材蘸取蘸料后食用
* 将食材与蘸料加入主食中食用
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=7
source: rerank_input

```text
菜系: 技巧知识
## 烹饪建议

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=8
source: rerank_input

```text
菜品: 西红柿鸡蛋汤
菜系: 未知
## 所需食材
1. 味素(5克)
2. 姜(5克)
3. 盐(15克)
4. 葱(5克)
5. 蒜(5克)
6. 西红柿(1个)
7. 食用油(15毫升)
8. 香油(2滴)
9. 鸡蛋(1-2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=9
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 使用空气炸锅
关键技巧内容:
## 正文
# 使用空气炸锅
## 什么是空气炸锅
## 什么是空气炸锅

空气炸锅为一种电子炊具，用空气替代原本热油加热，让食物变熟，令食材无需遇油也能达到近似油炸的效果。
## 工作方式
### 工作方式

空气炸锅借由上方的加热器产生高温热风，让热空气在食物周遭循环对流，快速加热食物自身的油脂，带走食物的水分，产生油炸的效果，并创造类似油炸食物的酥脆感。
## 优点
### 优点

* 由于无需添加食用油，因此可以**大幅减少**摄入含有高量脂肪和热量的食用油。
* 高速循环的热空气使食物脱水，表面变得金黄酥脆，让食物变得外焦里嫩。
* 操作简单，对新人友好。
## 流程
## 流程

* 将空气炸锅放在稳固、平整且水平的隔热表面上。
* 取出煎锅，将食材放入炸篮，将煎锅滑入产品中。
* 修改预设温度，旋转旋钮调整烹饪时间。
* 调整好烹饪时间后，产品将开始烹饪，等待定时器响铃时烹饪完成。
* 将炸篮中的食物全部倒入碗或碟中。务必从所用煎锅中取出装有原料的炸篮，因为煎锅底部**可能残留有热油或油脂**。
## 注意事项
## 注意事项

* 使用空气炸锅应注意设置温度不宜过高（尽量在 120℃内，最好不超过 168℃），制作时间不宜太长（约 10 分钟左右），避免生成过多有害成分[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)。
* 减少用空气炸锅烹饪淀粉类食物，如土豆、面包、油条等，可相应减少[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)摄入。相对而言，空气炸锅适合烹调脂肪或水分含量更高的食物，如肉类、蔬菜。
* 使用过程中，不能遮挡顶部的进风口和背面的出风口。用手遮挡的话，可能会被**热空气烫伤**。
* 不同品牌炸锅温差可达±10℃，首次尝试建议减少 10%时间后逐步调整
## 烹饪建议
#
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, recipe_name=如何决策吃什么, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧文档: 如何决策吃什么
分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
来源: tips/如何选择现在吃什么.md

补充信息: 技巧章节: 如何决策吃什么
章节: 正文
分类: 通用知识
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
内容: # 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=tipchunk_9dfcc67f4c73, recipe_name=如何决策吃什么 / 菜的选择, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 菜的选择
章节: 菜的选择
分类: 通用知识
摘要: 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
内容: ### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=tipchunk_5d9abc8cea8f, recipe_name=如何决策吃什么 / 形式语言描述, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 形式语言描述
章节: 形式语言描述
分类: 通用知识
摘要: 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得
内容: #### 形式语言描述

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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=tipchunk_0ab647800ff9, recipe_name=如何决策吃什么 / 计算荤菜和素菜数量, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算荤菜和素菜数量
章节: 计算荤菜和素菜数量
分类: 通用知识
摘要: 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
内容: ### 计算荤菜和素菜数量

* 菜的数量 = 人数 + 1。
* 荤菜比素菜多一个，或一样多即可。

由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=tipchunk_45dfd39d40d1, recipe_name=如何决策吃什么 / 计算方法, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 计算方法
章节: 计算方法
分类: 通用知识
摘要: 计算方法
内容: ## 计算方法
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.6150272488594055, search_type=vector_enhanced

```text
## 食用（此流程必选）
### 食用（此流程必选）

* 将搅拌后的食材直接食用
* 将未搅拌的主食材蘸取蘸料后食用
* 将食材与蘸料加入主食中食用
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=6
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipchunk_0ab647800ff9,tipchunk_45dfd39d40d1,tipchunk_5d9abc8cea8f,tipchunk_9dfcc67f4c73, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 使用空气炸锅
关键技巧内容:
## 正文
# 使用空气炸锅
## 什么是空气炸锅
## 什么是空气炸锅

空气炸锅为一种电子炊具，用空气替代原本热油加热，让食物变熟，令食材无需遇油也能达到近似油炸的效果。
## 工作方式
### 工作方式

空气炸锅借由上方的加热器产生高温热风，让热空气在食物周遭循环对流，快速加热食物自身的油脂，带走食物的水分，产生油炸的效果，并创造类似油炸食物的酥脆感。
## 优点
### 优点

* 由于无需添加食用油，因此可以**大幅减少**摄入含有高量脂肪和热量的食用油。
* 高速循环的热空气使食物脱水，表面变得金黄酥脆，让食物变得外焦里嫩。
* 操作简单，对新人友好。
## 流程
## 流程

* 将空气炸锅放在稳固、平整且水平的隔热表面上。
* 取出煎锅，将食材放入炸篮，将煎锅滑入产品中。
* 修改预设温度，旋转旋钮调整烹饪时间。
* 调整好烹饪时间后，产品将开始烹饪，等待定时器响铃时烹饪完成。
* 将炸篮中的食物全部倒入碗或碟中。务必从所用煎锅中取出装有原料的炸篮，因为煎锅底部**可能残留有热油或油脂**。
## 注意事项
## 注意事项

* 使用空气炸锅应注意设置温度不宜过高（尽量在 120℃内，最好不超过 168℃），制作时间不宜太长（约 10 分钟左右），避免生成过多有害成分[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)。
* 减少用空气炸锅烹饪淀粉类食物，如土豆、面包、油条等，可相应减少[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)摄入。相对而言，空气炸锅适合烹调脂肪或水分含量更高的食物，如肉类、蔬菜。
* 使用过程中，不能遮挡顶部的进风口和背面的出风口。用手遮挡的话，可能会被**热空气烫伤**。
* 不同品牌炸锅温差可达±10℃，首次尝试建议减少 10%时间后逐步调整
## 烹饪建议
## 烹饪建议
## 常用食物
### 常用食物

| 食物名称 | 温度(℃) | 时间（分钟） | 方法步骤 |
|---------|---------|--------|--------------------------------------------------------------------|
| **薯条** | 200 | 15-20 | 1. 冷冻薯条无需解冻，表面喷少量油；- 2. 平铺炸篮（不重叠），每5分钟摇晃一次；- 3. 最后2分钟可调至210℃上色。 |
| **鸡翅** | 180 | 18-22 | 1. 鸡翅划刀，用生抽、料酒、蚝油、蒜末腌制1小时；- 2. 平铺炸篮，表面刷蜂蜜水；- 3. 烤10分钟后翻面继续烤。 |
| **鱼类** | 180-190 | 12-15 | 1. 鱼身两面划刀，用姜片、葱段、盐、料酒腌制20分钟；- 2. 鱼表面刷油，垫锡纸防粘；- 3. 中途翻面一次。 |
| **牛排** | 200 | 8-12 | 1. 牛排室温回温，双面撒盐、黑胡椒和橄榄油；- 2. 空气炸锅预热5分钟，牛排放入后根据厚度烤制（每面4-6分钟）。 |
| **牛肉块** | 180 | 15-18 | 1. 牛肉切2cm立方块，用生抽、淀粉、黑胡椒腌制30分钟；- 2. 平铺炸篮，烤10分钟后翻动一次；- 3. 可加洋葱、彩椒同烤。 |
| **猪肉排** | 175-185 | 16-20 | 1. 猪排用刀背拍松，生抽、蒜粉、五香粉腌制40分钟；- 2. 表面喷油，垫烘焙纸；- 3. 中途翻面并刷腌料汁。 |
| **蛋挞** | 170-180 | 12-15 | 1. 蛋挞皮解冻后倒入自制蛋液（牛奶+淡奶油+糖+蛋黄）；- 2. 炸锅无需预热，烤至挞皮金黄、中心微焦即可。 |
| **蛋糕** | 160 | 25-30 | 1. 6寸模具垫油纸，倒入蛋糕糊（7分满）；- 2. 低温慢烤，插入牙签无粘连即熟；- 3. 倒扣冷却防塌陷。 |
| **披萨** | 180-190 | 8-12 | 1. 冷冻披萨无需解冻，可撒额外芝士；-
## 操作要点
### 操作要点

1. **预处理关键**
 - 肉类需充分解冻并擦干表面水分（牛排/猪排建议室温回温）
 - 冷冻食品（薯条/披萨）可直接烹饪，但需加大摇晃/翻面频率

2. **防粘技巧**
 - 鱼类/蛋糕等易粘食物建议垫烘焙纸或锡纸
 - 炸篮底部可铺洋葱片/柠檬片提升风味并隔离汁水

3. **上色控制**
 - 最后 2-3 分钟调高 10-20℃可使表面更酥脆（适用于薯条/鸡翅）
 - 蛋挞/蛋糕表面加盖锡纸可防止过度焦化

4. **熟度检测**
 - 肉类：用筷子按压，硬挺为全熟，柔软带弹性为半熟
 - 蛋糕：牙签插入中心无面糊粘连即熟
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6242837309837341, search_type=vector_enhanced

```text
## 所需食材
1. 其他蔬菜（青椒番茄胡萝卜等）(适量g)
2. 冷水(200-400ml)
3. 盐(适量g)
4. 肉类（牛羊鱼虾等）(适量g)
5. 胡椒粉(适量g)
6. 蛋类（鸡蛋鸭蛋等）(适量个)
7. 豆制品（豆腐皮等）(适量g)
8. 青菜（生菜菠菜等）(适量g)
9. 面食(70-230g)
10. 香油(适量ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1150, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6079573631286621, search_type=vector_enhanced

```text
## 烹饪建议

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.5924526453018188, search_type=vector_enhanced

```text
## 所需食材
1. 味素(5克)
2. 姜(5克)
3. 盐(15克)
4. 葱(5克)
5. 蒜(5克)
6. 西红柿(1个)
7. 食用油(15毫升)
8. 香油(2滴)
9. 鸡蛋(1-2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=tipdoc_820d789ff48e, recipe_name=如何决策吃什么, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧文档: 如何决策吃什么
分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
来源: tips/如何选择现在吃什么.md

补充信息: 技巧章节: 如何决策吃什么
章节: 正文
分类: 通用知识
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
内容: # 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=tipchunk_9dfcc67f4c73, recipe_name=如何决策吃什么 / 菜的选择, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 菜的选择
章节: 菜的选择
分类: 通用知识
摘要: 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
内容: ### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=tipchunk_5d9abc8cea8f, recipe_name=如何决策吃什么 / 形式语言描述, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 形式语言描述
章节: 形式语言描述
分类: 通用知识
摘要: 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得
内容: #### 形式语言描述

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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.6150272488594055, search_type=vector_enhanced

```text
## 食用（此流程必选）
### 食用（此流程必选）

* 将搅拌后的食材直接食用
* 将未搅拌的主食材蘸取蘸料后食用
* 将食材与蘸料加入主食中食用
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipchunk_0ab647800ff9,tipchunk_45dfd39d40d1,tipchunk_5d9abc8cea8f,tipchunk_9dfcc67f4c73, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 使用空气炸锅
关键技巧内容:
## 正文
# 使用空气炸锅
## 什么是空气炸锅
## 什么是空气炸锅

空气炸锅为一种电子炊具，用空气替代原本热油加热，让食物变熟，令食材无需遇油也能达到近似油炸的效果。
## 工作方式
### 工作方式

空气炸锅借由上方的加热器产生高温热风，让热空气在食物周遭循环对流，快速加热食物自身的油脂，带走食物的水分，产生油炸的效果，并创造类似油炸食物的酥脆感。
## 优点
### 优点

* 由于无需添加食用油，因此可以**大幅减少**摄入含有高量脂肪和热量的食用油。
* 高速循环的热空气使食物脱水，表面变得金黄酥脆，让食物变得外焦里嫩。
* 操作简单，对新人友好。
## 流程
## 流程

* 将空气炸锅放在稳固、平整且水平的隔热表面上。
* 取出煎锅，将食材放入炸篮，将煎锅滑入产品中。
* 修改预设温度，旋转旋钮调整烹饪时间。
* 调整好烹饪时间后，产品将开始烹饪，等待定时器响铃时烹饪完成。
* 将炸篮中的食物全部倒入碗或碟中。务必从所用煎锅中取出装有原料的炸篮，因为煎锅底部**可能残留有热油或油脂**。
## 注意事项
## 注意事项

* 使用空气炸锅应注意设置温度不宜过高（尽量在 120℃内，最好不超过 168℃），制作时间不宜太长（约 10 分钟左右），避免生成过多有害成分[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)。
* 减少用空气炸锅烹饪淀粉类食物，如土豆、面包、油条等，可相应减少[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)摄入。相对而言，空气炸锅适合烹调脂肪或水分含量更高的食物，如肉类、蔬菜。
* 使用过程中，不能遮挡顶部的进风口和背面的出风口。用手遮挡的话，可能会被**热空气烫伤**。
* 不同品牌炸锅温差可达±10℃，首次尝试建议减少 10%时间后逐步调整
## 烹饪建议
## 烹饪建议
## 常用食物
### 常用食物

| 食物名称 | 温度(℃) | 时间（分钟） | 方法步骤 |
|---------|---------|--------|--------------------------------------------------------------------|
| **薯条** | 200 | 15-20 | 1. 冷冻薯条无需解冻，表面喷少量油；- 2. 平铺炸篮（不重叠），每5分钟摇晃一次；- 3. 最后2分钟可调至210℃上色。 |
| **鸡翅** | 180 | 18-22 | 1. 鸡翅划刀，用生抽、料酒、蚝油、蒜末腌制1小时；- 2. 平铺炸篮，表面刷蜂蜜水；- 3. 烤10分钟后翻面继续烤。 |
| **鱼类** | 180-190 | 12-15 | 1. 鱼身两面划刀，用姜片、葱段、盐、料酒腌制20分钟；- 2. 鱼表面刷油，垫锡纸防粘；- 3. 中途翻面一次。 |
| **牛排** | 200 | 8-12 | 1. 牛排室温回温，双面撒盐、黑胡椒和橄榄油；- 2. 空气炸锅预热5分钟，牛排放入后根据厚度烤制（每面4-6分钟）。 |
| **牛肉块** | 180 | 15-18 | 1. 牛肉切2cm立方块，用生抽、淀粉、黑胡椒腌制30分钟；- 2. 平铺炸篮，烤10分钟后翻动一次；- 3. 可加洋葱、彩椒同烤。 |
| **猪肉排** | 175-185 | 16-20 | 1. 猪排用刀背拍松，生抽、蒜粉、五香粉腌制40分钟；- 2. 表面喷油，垫烘焙纸；- 3. 中途翻面并刷腌料汁。 |
| **蛋挞** | 170-180 | 12-15 | 1. 蛋挞皮解冻后倒入自制蛋液（牛奶+淡奶油+糖+蛋黄）；- 2. 炸锅无需预热，烤至挞皮金黄、中心微焦即可。 |
| **蛋糕** | 160 | 25-30 | 1. 6寸模具垫油纸，倒入蛋糕糊（7分满）；- 2. 低温慢烤，插入牙签无粘连即熟；- 3. 倒扣冷却防塌陷。 |
| **披萨** | 180-190 | 8-12 | 1. 冷冻披萨无需解冻，可撒额外芝士；-
## 操作要点
### 操作要点

1. **预处理关键**
 - 肉类需充分解冻并擦干表面水分（牛排/猪排建议室温回温）
 - 冷冻食品（薯条/披萨）可直接烹饪，但需加大摇晃/翻面频率

2. **防粘技巧**
 - 鱼类/蛋糕等易粘食物建议垫烘焙纸或锡纸
 - 炸篮底部可铺洋葱片/柠檬片提升风味并隔离汁水

3. **上色控制**
 - 最后 2-3 分钟调高 10-20℃可使表面更酥脆（适用于薯条/鸡翅）
 - 蛋挞/蛋糕表面加盖锡纸可防止过度焦化

4. **熟度检测**
 - 肉类：用筷子按压，硬挺为全熟，柔软带弹性为半熟
 - 蛋糕：牙签插入中心无面糊粘连即熟
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=tipdoc_820d789ff48e, recipe_name=如何决策吃什么, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 如何决策吃什么
技巧文档: 如何决策吃什么
分类: 通用知识
标签: 如何决策吃什么,如何选择现在吃什么,形式语言描述,正文,菜的选择,计算方法,计算荤菜和素菜数量
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。 计算方法 计算荤菜和素菜数量 菜的数量 = 人数 + 1。 荤菜比素菜多一个，或一样多即可。 由此得到荤菜数量和素菜数量，再在上一步的菜谱中选择即可。 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
来源: tips/如何选择现在吃什么.md

补充信息: 技巧章节: 如何决策吃什么
章节: 正文
分类: 通用知识
摘要: 如何决策吃什么 如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
内容: # 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=1
source: generation_context
metadata_summary: node_id=tipchunk_9dfcc67f4c73, recipe_name=如何决策吃什么 / 菜的选择, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 菜的选择
章节: 菜的选择
分类: 通用知识
摘要: 菜的选择 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。 如果有小孩，考虑增加有甜味的菜。 考虑增加特色菜、拿手菜。 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为： 猪肉 、 鸡肉 、 牛肉 、 羊肉 、 鸭肉 、 鱼肉 。 不要选择奇奇怪怪的动物做荤菜。
内容: ### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=2
source: generation_context
metadata_summary: node_id=tipchunk_5d9abc8cea8f, recipe_name=如何决策吃什么 / 形式语言描述, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 如何决策吃什么
技巧章节: 如何决策吃什么 / 形式语言描述
章节: 形式语言描述
分类: 通用知识
摘要: 形式语言描述 当 有人数 N 时， 设 素菜数 为 a , 荤菜数 为 b 。 N , a , b 均为整数。 此时有下列不等式组： a + b = N + 1 a ≤ b ≤ a+1 解得
内容: #### 形式语言描述

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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
```

### result_order=3
source: generation_context
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.6150272488594055, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 食用（此流程必选）
### 食用（此流程必选）

* 将搅拌后的食材直接食用
* 将未搅拌的主食材蘸取蘸料后食用
* 将食材与蘸料加入主食中食用
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipchunk_0ab647800ff9,tipchunk_45dfd39d40d1,tipchunk_5d9abc8cea8f,tipchunk_9dfcc67f4c73, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 使用空气炸锅
关键技巧内容:
## 正文
# 使用空气炸锅
## 什么是空气炸锅
## 什么是空气炸锅

空气炸锅为一种电子炊具，用空气替代原本热油加热，让食物变熟，令食材无需遇油也能达到近似油炸的效果。
## 工作方式
### 工作方式

空气炸锅借由上方的加热器产生高温热风，让热空气在食物周遭循环对流，快速加热食物自身的油脂，带走食物的水分，产生油炸的效果，并创造类似油炸食物的酥脆感。
## 优点
### 优点

* 由于无需添加食用油，因此可以**大幅减少**摄入含有高量脂肪和热量的食用油。
* 高速循环的热空气使食物脱水，表面变得金黄酥脆，让食物变得外焦里嫩。
* 操作简单，对新人友好。
## 流程
## 流程

* 将空气炸锅放在稳固、平整且水平的隔热表面上。
* 取出煎锅，将食材放入炸篮，将煎锅滑入产品中。
* 修改预设温度，旋转旋钮调整烹饪时间。
* 调整好烹饪时间后，产品将开始烹饪，等待定时器响铃时烹饪完成。
* 将炸篮中的食物全部倒入碗或碟中。务必从所用煎锅中取出装有原料的炸篮，因为煎锅底部**可能残留有热油或油脂**。
## 注意事项
## 注意事项

* 使用空气炸锅应注意设置温度不宜过高（尽量在 120℃内，最好不超过 168℃），制作时间不宜太长（约 10 分钟左右），避免生成过多有害成分[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)。
* 减少用空气炸锅烹饪淀粉类食物，如土豆、面包、油条等，可相应减少[丙烯酰胺](https://zh.wikipedia.org/wiki/%E4%B8%99%E7%83%AF%E9%85%B0%E8%83%BA)摄入。相对而言，空气炸锅适合烹调脂肪或水分含量更高的食物，如肉类、蔬菜。
* 使用过程中，不能遮挡顶部的进风口和背面的出风口。用手遮挡的话，可能会被**热空气烫伤**。
* 不同品牌炸锅温差可达±10℃，首次尝试建议减少 10%时间后逐步调整
## 烹饪建议
## 烹饪建议
## 常用食物
### 常用食物

| 食物名称 | 温度(℃) | 时间（分钟） | 方法步骤 |
|---------|---------|--------|--------------------------------------------------------------------|
| **薯条** | 200 | 15-20 | 1. 冷冻薯条无需解冻，表面喷少量油；- 2. 平铺炸篮（不重叠），每5分钟摇晃一次；- 3. 最后2分钟可调至210℃上色。 |
| **鸡翅** | 180 | 18-22 | 1. 鸡翅划刀，用生抽、料酒、蚝油、蒜末腌制1小时；- 2. 平铺炸篮，表面刷蜂蜜水；- 3. 烤10分钟后翻面继续烤。 |
| **鱼类** | 180-190 | 12-15 | 1. 鱼身两面划刀，用姜片、葱段、盐、料酒腌制20分钟；- 2. 鱼表面刷油，垫锡纸防粘；- 3. 中途翻面一次。 |
| **牛排** | 200 | 8-12 | 1. 牛排室温回温，双面撒盐、黑胡椒和橄榄油；- 2. 空气炸锅预热5分钟，牛排放入后根据厚度烤制（每面4-6分钟）。 |
| **牛肉块** | 180 | 15-18 | 1. 牛肉切2cm立方块，用生抽、淀粉、黑胡椒腌制30分钟；- 2. 平铺炸篮，烤10分钟后翻动一次；- 3. 可加洋葱、彩椒同烤。 |
| **猪肉排** | 175-185 | 16-20 | 1. 猪排用刀背拍松，生抽、蒜粉、五香粉腌制40分钟；- 2. 表面喷油，垫烘焙纸；- 3. 中途翻面并刷腌料汁。 |
| **蛋挞** | 170-180 | 12-15 | 1. 蛋挞皮解冻后倒入自制蛋液（牛奶+淡奶油+糖+蛋黄）；- 2. 炸锅无需预热，烤至挞皮金黄、中心微焦即可。 |
| **蛋糕** | 160 | 25-30 | 1. 6寸模具垫油纸，倒入蛋糕糊（7分满）；- 2. 低温慢烤，插入牙签无粘连即熟；- 3. 倒扣冷却防塌陷。 |
| **披萨** | 180-190 | 8-12 | 1. 冷冻披萨无需解冻，可撒额外芝士；-
## 操作要点
### 操作要点

1. **预处理关键**
 - 肉类需充分解冻并擦干表面水分（牛排/猪排建议室温回温）
 - 冷冻食品（薯条/披萨）可直接烹饪，但需加大摇晃/翻面频率

2. **防粘技巧**
 - 鱼类/蛋糕等易粘食物建议垫烘焙纸或锡纸
 - 炸篮底部可铺洋葱片/柠檬片提升风味并隔离汁水

3. **上色控制**
 - 最后 2-3 分钟调高 10-20℃可使表面更酥脆（适用于薯条/鸡翅）
 - 蛋挞/蛋糕表面加盖锡纸可防止过度焦化

4. **熟度检测**
 - 肉类：用筷子按压，硬挺为全熟，柔软带弹性为半熟
 - 蛋糕：牙签插入中心无面糊粘连即熟
```

