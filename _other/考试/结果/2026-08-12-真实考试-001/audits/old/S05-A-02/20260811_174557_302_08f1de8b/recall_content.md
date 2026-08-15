# Recall Content

audit_id: 20260811_174557_302_08f1de8b
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201001782, recipe_name=猪肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 猪肉
食材名称: 猪肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201001901, recipe_name=土豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201000438, recipe_name=青椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 青椒
食材名称: 青椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=3
source: entity_level
metadata_summary: node_id=201001758, recipe_name=芹菜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芹菜
食材名称: 芹菜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=4
source: entity_level
metadata_summary: node_id=201005331, recipe_name=萝卜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 萝卜
食材名称: 萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=5
source: entity_level
metadata_summary: node_id=201004769, recipe_name=豆角, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=6
source: entity_level
metadata_summary: node_id=201005369, recipe_name=莲藕, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 莲藕
食材名称: 莲藕
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=7
source: entity_level
metadata_summary: node_id=201004806, recipe_name=蘑菇, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蘑菇
食材名称: 蘑菇
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=8
source: entity_level
metadata_summary: node_id=201005130, recipe_name=西兰花, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西兰花
食材名称: 西兰花
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201000411, recipe_name=蛏抱蛋, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6217882633209229, search_type=vector_enhanced

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

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201001780, chunk_id=201001780_chunk_381, recipe_name=洋葱炒猪肉, category=荤菜, score=0.6166141033172607, search_type=vector_enhanced

```text
## 标签
猪肉可选猪肩肉片或肉丝
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=tipdoc_7e937e95d07f, chunk_id=tipdoc_7e937e95d07f_chunk_1231, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食, category=通用知识, score=0.5906415581703186, search_type=vector_enhanced

```text
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的钙结合，形成草酸钙。
 * **可能影响**：影响钙的吸收，降低牛奶的补钙效果。
 * **健康建议**：建议分开食用，或间隔一段时间。

6. **豆浆 + 鸡蛋：蛋白质的“消化挑战”**
 * **相克原理**：未煮熟的豆浆中含有一种胰蛋白酶抑制剂，会影响人体对蛋白质的消化和吸收。
 * **可能影响**：降低鸡蛋蛋白质的利用率，可能引起消化不良。
 * **健康建议**：确保豆浆彻底煮沸、煮透后（假沸不算），再搭配鸡蛋食用，这样胰蛋白酶抑制剂会被破坏，不会产生不良影响。

7. **黄瓜 + 西红柿：维生素C的“默默流失”**
 * **相克原理**：与胡萝卜类似，黄瓜中也含有一种维生素 C 分解酶。
 * **可能影响**：破坏西红柿等食物中的维生素 C，降低其抗氧化和免疫增强作用。
 * **健康建议**：最好分开食用，如果要做沙拉，可以考虑先吃西红柿，再吃黄瓜，或将两者分别处理。

8. **羊肉 + 西瓜：寒热的“碰撞”**
 * **相克原理**：羊肉性温热，具有补虚祛寒的功效；西瓜性寒凉，有清热解暑作用。
 * **可能影响**：两者同食，寒热性质相悖，可能导致脾胃不适，引起腹泻、腹胀等消化问题，尤其对于脾胃虚弱者。
 * **健康建议**：避免在同一餐中大量食用。

9. **猪肉 + 茶：蛋白质吸收的“阻碍”**
 * **相克原理**：茶叶中含有鞣酸，与猪肉中的蛋白质结合，会形成不易消化的沉淀物。
 * **可能影响**：影响蛋白质的消化吸收，可能引起便秘或消化不良。
 * **健康建议**：饭后一小时再饮茶，或避免在吃肉类时大量饮用浓茶。

10. **蜂蜜 + 豆腐：消化“不协调”**
 * **相克原理**：蜂蜜中的有机酸与豆腐中的蛋白质结合，可能形成不易消化的物质。
 * **可能影响**：可能引起肠胃不适，如腹泻。
 * **健康建议**：尽量避免同食。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 揭秘食材搭配的智慧：这些食物不宜同食 / 科学看待“相克”，智慧搭配日常饮食 (TechniqueChunk): category: 通用知识
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.5891380310058594, search_type=vector_enhanced

```text
## 所需食材
1. 姜(2片)
2. 小米椒(1个)
3. 猪肉（五花肉）(250g)
4. 白糖(5mg)
5. 蒜片(2片)
6. 豆瓣酱(10g)
7. 酱油(15ml)
8. 青椒(3个)
9. 鸡蛋(适量个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_449, recipe_name=农家一碗香, category=荤菜, score=0.5861289501190186, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将猪肉切片，最好把肥瘦分开放；青椒和小米辣切成段；蒜片用刀背拍成末；姜切成丝；鸡蛋打到小碗中，用筷子打散。
方法: 切,拍,打散
工具: 刀,案板,碗,筷子

### 第2步
步骤: 步骤2
描述: 锅中倒油，开小火，油热后倒入蛋液，炒散至断生，盛出备用。
方法: 炒
工具: 炒锅,锅铲,碗

### 第3步
步骤: 步骤3
描述: 锅中再加少许油，小火将肥猪肉下锅逼出猪油。
方法: 煎,煸
工具: 炒锅,锅铲

### 第4步
步骤: 步骤4
描述: 肥肉呈金黄色时转中火，加入瘦肉翻炒至变色。
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 加入姜丝、蒜末和豆瓣酱，翻炒均匀给猪肉上色。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 放入青红椒和炒好的鸡蛋，加入酱油和白糖，翻炒至青椒微微断生，保持清脆口感。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 出锅装盘即可。
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5852751731872559, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=tipdoc_7e937e95d07f, chunk_id=tipdoc_7e937e95d07f_chunk_1228, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食, category=通用知识, score=0.5793795585632324, search_type=vector_enhanced

```text
## 摘要
揭秘食材搭配的智慧：这些食物不宜同食 在日常烹饪中，我们都希望做出美味又健康的家常菜。然而，有些食材看似普通，搭配在一起却可能暗藏“玄机”，不仅影响食物的色香味，更可能阻碍营养吸收，甚至对身体健康产生微妙的影响。了解这些“食材相克”与“食用禁忌”，是提升饮食智慧、守护家人健康的重要一步。 常见食材搭配误区与科学解读 以下是一些在我们的餐桌上，需要特别留意的食材组合： 1. 菠菜 + 豆腐：草酸与钙质的“交锋” 相克原理 ：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。 可能影响 ：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。 健康建议 ：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。 2. 胡萝卜 + 白萝卜：维生素C的“损耗者” 相克原理 ：胡萝卜中含有一种特殊的“抗坏血酸氧化酶” 即维生素 C 分解酶 ，它会破坏其他食物中的维生素 C。 可能影响 ：导致白萝卜 以及其他富含维生素 C 的食物，如柑橘类 中的维生素 C 大量流失，降低其营养价值。 健康建议 ：两者最好分开食用，或将胡

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 揭秘食材搭配的智慧：这些食物不宜同食 / 科学看待“相克”，智慧搭配日常饮食 (TechniqueChunk): category: 通用知识
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1322, recipe_name=凉拌, category=烹饪技巧, score=0.5791282653808594, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 猪肉与禽肉没有例外，必须十成熟，必须完全熟制，必须不见任何血水
* 部分牛肉、鱼肉、海鲜类在确认安全后可生食

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201002179, chunk_id=201002179_chunk_452, recipe_name=冬瓜酿肉, category=荤菜, score=0.5718494653701782, search_type=vector_enhanced

```text
## 所需食材
1. 冬瓜(200g)
2. 水(50ml)
3. 水淀粉(25g)
4. 淀粉(5g)
5. 猪肉末(300g)
6. 生抽(10ml)
7. 盐(20g)
8. 胡椒粉(5g)
9. 葱姜末(30g)
10. 葱花(20g)
11. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201003355, chunk_id=201003355_chunk_660, recipe_name=青椒土豆炒肉, category=荤菜, score=0.5688109993934631, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(300g)
2. 土豆淀粉(5g)
3. 姜(5g)
4. 水(15g)
5. 猪肉（五花肉）(200g)
6. 盐(7g)
7. 葱(10g)
8. 蒜(12g)
9. 酱油(6-10ml)
10. 青椒(200g)
11. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201001782, recipe_name=猪肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 猪肉
食材名称: 猪肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201001901, recipe_name=土豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000438, recipe_name=青椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 青椒
食材名称: 青椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201001758, recipe_name=芹菜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芹菜
食材名称: 芹菜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201005331, recipe_name=萝卜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 萝卜
食材名称: 萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201004769, recipe_name=豆角, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201005369, recipe_name=莲藕, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 莲藕
食材名称: 莲藕
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201004806, recipe_name=蘑菇, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蘑菇
食材名称: 蘑菇
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201005130, recipe_name=西兰花, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西兰花
食材名称: 西兰花
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201000411, recipe_name=蛏抱蛋, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6217882633209229, search_type=vector_enhanced

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

### result_order=12
source: branch_grouped
metadata_summary: node_id=201001780, chunk_id=201001780_chunk_381, recipe_name=洋葱炒猪肉, category=荤菜, score=0.6166141033172607, search_type=vector_enhanced

```text
## 标签
猪肉可选猪肩肉片或肉丝
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=tipdoc_7e937e95d07f, chunk_id=tipdoc_7e937e95d07f_chunk_1231, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食, category=通用知识, score=0.5906415581703186, search_type=vector_enhanced

```text
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的钙结合，形成草酸钙。
 * **可能影响**：影响钙的吸收，降低牛奶的补钙效果。
 * **健康建议**：建议分开食用，或间隔一段时间。

6. **豆浆 + 鸡蛋：蛋白质的“消化挑战”**
 * **相克原理**：未煮熟的豆浆中含有一种胰蛋白酶抑制剂，会影响人体对蛋白质的消化和吸收。
 * **可能影响**：降低鸡蛋蛋白质的利用率，可能引起消化不良。
 * **健康建议**：确保豆浆彻底煮沸、煮透后（假沸不算），再搭配鸡蛋食用，这样胰蛋白酶抑制剂会被破坏，不会产生不良影响。

7. **黄瓜 + 西红柿：维生素C的“默默流失”**
 * **相克原理**：与胡萝卜类似，黄瓜中也含有一种维生素 C 分解酶。
 * **可能影响**：破坏西红柿等食物中的维生素 C，降低其抗氧化和免疫增强作用。
 * **健康建议**：最好分开食用，如果要做沙拉，可以考虑先吃西红柿，再吃黄瓜，或将两者分别处理。

8. **羊肉 + 西瓜：寒热的“碰撞”**
 * **相克原理**：羊肉性温热，具有补虚祛寒的功效；西瓜性寒凉，有清热解暑作用。
 * **可能影响**：两者同食，寒热性质相悖，可能导致脾胃不适，引起腹泻、腹胀等消化问题，尤其对于脾胃虚弱者。
 * **健康建议**：避免在同一餐中大量食用。

9. **猪肉 + 茶：蛋白质吸收的“阻碍”**
 * **相克原理**：茶叶中含有鞣酸，与猪肉中的蛋白质结合，会形成不易消化的沉淀物。
 * **可能影响**：影响蛋白质的消化吸收，可能引起便秘或消化不良。
 * **健康建议**：饭后一小时再饮茶，或避免在吃肉类时大量饮用浓茶。

10. **蜂蜜 + 豆腐：消化“不协调”**
 * **相克原理**：蜂蜜中的有机酸与豆腐中的蛋白质结合，可能形成不易消化的物质。
 * **可能影响**：可能引起肠胃不适，如腹泻。
 * **健康建议**：尽量避免同食。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 揭秘食材搭配的智慧：这些食物不宜同食 / 科学看待“相克”，智慧搭配日常饮食 (TechniqueChunk): category: 通用知识
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.5891380310058594, search_type=vector_enhanced

```text
## 所需食材
1. 姜(2片)
2. 小米椒(1个)
3. 猪肉（五花肉）(250g)
4. 白糖(5mg)
5. 蒜片(2片)
6. 豆瓣酱(10g)
7. 酱油(15ml)
8. 青椒(3个)
9. 鸡蛋(适量个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_449, recipe_name=农家一碗香, category=荤菜, score=0.5861289501190186, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将猪肉切片，最好把肥瘦分开放；青椒和小米辣切成段；蒜片用刀背拍成末；姜切成丝；鸡蛋打到小碗中，用筷子打散。
方法: 切,拍,打散
工具: 刀,案板,碗,筷子

### 第2步
步骤: 步骤2
描述: 锅中倒油，开小火，油热后倒入蛋液，炒散至断生，盛出备用。
方法: 炒
工具: 炒锅,锅铲,碗

### 第3步
步骤: 步骤3
描述: 锅中再加少许油，小火将肥猪肉下锅逼出猪油。
方法: 煎,煸
工具: 炒锅,锅铲

### 第4步
步骤: 步骤4
描述: 肥肉呈金黄色时转中火，加入瘦肉翻炒至变色。
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 加入姜丝、蒜末和豆瓣酱，翻炒均匀给猪肉上色。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 放入青红椒和炒好的鸡蛋，加入酱油和白糖，翻炒至青椒微微断生，保持清脆口感。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 出锅装盘即可。
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=16
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5852751731872559, search_type=vector_enhanced

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

### result_order=17
source: branch_grouped
metadata_summary: node_id=tipdoc_7e937e95d07f, chunk_id=tipdoc_7e937e95d07f_chunk_1228, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食, category=通用知识, score=0.5793795585632324, search_type=vector_enhanced

```text
## 摘要
揭秘食材搭配的智慧：这些食物不宜同食 在日常烹饪中，我们都希望做出美味又健康的家常菜。然而，有些食材看似普通，搭配在一起却可能暗藏“玄机”，不仅影响食物的色香味，更可能阻碍营养吸收，甚至对身体健康产生微妙的影响。了解这些“食材相克”与“食用禁忌”，是提升饮食智慧、守护家人健康的重要一步。 常见食材搭配误区与科学解读 以下是一些在我们的餐桌上，需要特别留意的食材组合： 1. 菠菜 + 豆腐：草酸与钙质的“交锋” 相克原理 ：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。 可能影响 ：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。 健康建议 ：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。 2. 胡萝卜 + 白萝卜：维生素C的“损耗者” 相克原理 ：胡萝卜中含有一种特殊的“抗坏血酸氧化酶” 即维生素 C 分解酶 ，它会破坏其他食物中的维生素 C。 可能影响 ：导致白萝卜 以及其他富含维生素 C 的食物，如柑橘类 中的维生素 C 大量流失，降低其营养价值。 健康建议 ：两者最好分开食用，或将胡

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 揭秘食材搭配的智慧：这些食物不宜同食 / 科学看待“相克”，智慧搭配日常饮食 (TechniqueChunk): category: 通用知识
```

### result_order=18
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1322, recipe_name=凉拌, category=烹饪技巧, score=0.5791282653808594, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 猪肉与禽肉没有例外，必须十成熟，必须完全熟制，必须不见任何血水
* 部分牛肉、鱼肉、海鲜类在确认安全后可生食

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=19
source: branch_grouped
metadata_summary: node_id=201002179, chunk_id=201002179_chunk_452, recipe_name=冬瓜酿肉, category=荤菜, score=0.5718494653701782, search_type=vector_enhanced

```text
## 所需食材
1. 冬瓜(200g)
2. 水(50ml)
3. 水淀粉(25g)
4. 淀粉(5g)
5. 猪肉末(300g)
6. 生抽(10ml)
7. 盐(20g)
8. 胡椒粉(5g)
9. 葱姜末(30g)
10. 葱花(20g)
11. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=20
source: branch_grouped
metadata_summary: node_id=201003355, chunk_id=201003355_chunk_660, recipe_name=青椒土豆炒肉, category=荤菜, score=0.5688109993934631, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(300g)
2. 土豆淀粉(5g)
3. 姜(5g)
4. 水(15g)
5. 猪肉（五花肉）(200g)
6. 盐(7g)
7. 葱(10g)
8. 蒜(12g)
9. 酱油(6-10ml)
10. 青椒(200g)
11. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201001782, recipe_name=猪肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 猪肉
食材名称: 猪肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201001901, recipe_name=土豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000438, recipe_name=青椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 青椒
食材名称: 青椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201001758, recipe_name=芹菜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芹菜
食材名称: 芹菜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201005331, recipe_name=萝卜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 萝卜
食材名称: 萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201004769, recipe_name=豆角, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201005369, recipe_name=莲藕, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 莲藕
食材名称: 莲藕
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004806, recipe_name=蘑菇, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蘑菇
食材名称: 蘑菇
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201005130, recipe_name=西兰花, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西兰花
食材名称: 西兰花
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201000411, recipe_name=蛏抱蛋, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6217882633209229, search_type=vector_enhanced

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

### result_order=12
source: merged_candidates
metadata_summary: node_id=201001780, chunk_id=201001780_chunk_381, recipe_name=洋葱炒猪肉, category=荤菜, score=0.6166141033172607, search_type=vector_enhanced

```text
## 标签
猪肉可选猪肩肉片或肉丝
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=tipdoc_7e937e95d07f, chunk_id=tipdoc_7e937e95d07f_chunk_1231, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食, category=通用知识, score=0.5906415581703186, search_type=vector_enhanced

```text
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的钙结合，形成草酸钙。
 * **可能影响**：影响钙的吸收，降低牛奶的补钙效果。
 * **健康建议**：建议分开食用，或间隔一段时间。

6. **豆浆 + 鸡蛋：蛋白质的“消化挑战”**
 * **相克原理**：未煮熟的豆浆中含有一种胰蛋白酶抑制剂，会影响人体对蛋白质的消化和吸收。
 * **可能影响**：降低鸡蛋蛋白质的利用率，可能引起消化不良。
 * **健康建议**：确保豆浆彻底煮沸、煮透后（假沸不算），再搭配鸡蛋食用，这样胰蛋白酶抑制剂会被破坏，不会产生不良影响。

7. **黄瓜 + 西红柿：维生素C的“默默流失”**
 * **相克原理**：与胡萝卜类似，黄瓜中也含有一种维生素 C 分解酶。
 * **可能影响**：破坏西红柿等食物中的维生素 C，降低其抗氧化和免疫增强作用。
 * **健康建议**：最好分开食用，如果要做沙拉，可以考虑先吃西红柿，再吃黄瓜，或将两者分别处理。

8. **羊肉 + 西瓜：寒热的“碰撞”**
 * **相克原理**：羊肉性温热，具有补虚祛寒的功效；西瓜性寒凉，有清热解暑作用。
 * **可能影响**：两者同食，寒热性质相悖，可能导致脾胃不适，引起腹泻、腹胀等消化问题，尤其对于脾胃虚弱者。
 * **健康建议**：避免在同一餐中大量食用。

9. **猪肉 + 茶：蛋白质吸收的“阻碍”**
 * **相克原理**：茶叶中含有鞣酸，与猪肉中的蛋白质结合，会形成不易消化的沉淀物。
 * **可能影响**：影响蛋白质的消化吸收，可能引起便秘或消化不良。
 * **健康建议**：饭后一小时再饮茶，或避免在吃肉类时大量饮用浓茶。

10. **蜂蜜 + 豆腐：消化“不协调”**
 * **相克原理**：蜂蜜中的有机酸与豆腐中的蛋白质结合，可能形成不易消化的物质。
 * **可能影响**：可能引起肠胃不适，如腹泻。
 * **健康建议**：尽量避免同食。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 揭秘食材搭配的智慧：这些食物不宜同食 / 科学看待“相克”，智慧搭配日常饮食 (TechniqueChunk): category: 通用知识
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_449, recipe_name=农家一碗香, category=荤菜, score=0.5861289501190186, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将猪肉切片，最好把肥瘦分开放；青椒和小米辣切成段；蒜片用刀背拍成末；姜切成丝；鸡蛋打到小碗中，用筷子打散。
方法: 切,拍,打散
工具: 刀,案板,碗,筷子

### 第2步
步骤: 步骤2
描述: 锅中倒油，开小火，油热后倒入蛋液，炒散至断生，盛出备用。
方法: 炒
工具: 炒锅,锅铲,碗

### 第3步
步骤: 步骤3
描述: 锅中再加少许油，小火将肥猪肉下锅逼出猪油。
方法: 煎,煸
工具: 炒锅,锅铲

### 第4步
步骤: 步骤4
描述: 肥肉呈金黄色时转中火，加入瘦肉翻炒至变色。
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 加入姜丝、蒜末和豆瓣酱，翻炒均匀给猪肉上色。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 放入青红椒和炒好的鸡蛋，加入酱油和白糖，翻炒至青椒微微断生，保持清脆口感。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 出锅装盘即可。
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=15
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5852751731872559, search_type=vector_enhanced

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

### result_order=16
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1322, recipe_name=凉拌, category=烹饪技巧, score=0.5791282653808594, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 猪肉与禽肉没有例外，必须十成熟，必须完全熟制，必须不见任何血水
* 部分牛肉、鱼肉、海鲜类在确认安全后可生食

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=17
source: merged_candidates
metadata_summary: node_id=201002179, chunk_id=201002179_chunk_452, recipe_name=冬瓜酿肉, category=荤菜, score=0.5718494653701782, search_type=vector_enhanced

```text
## 所需食材
1. 冬瓜(200g)
2. 水(50ml)
3. 水淀粉(25g)
4. 淀粉(5g)
5. 猪肉末(300g)
6. 生抽(10ml)
7. 盐(20g)
8. 胡椒粉(5g)
9. 葱姜末(30g)
10. 葱花(20g)
11. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=18
source: merged_candidates
metadata_summary: node_id=201003355, chunk_id=201003355_chunk_660, recipe_name=青椒土豆炒肉, category=荤菜, score=0.5688109993934631, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(300g)
2. 土豆淀粉(5g)
3. 姜(5g)
4. 水(15g)
5. 猪肉（五花肉）(200g)
6. 盐(7g)
7. 葱(10g)
8. 蒜(12g)
9. 酱油(6-10ml)
10. 青椒(200g)
11. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_7e937e95d07f,tipdoc_fd7f557c37a7, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 揭秘食材搭配的智慧：这些食物不宜同食

在日常烹饪中，我们都希望做出美味又健康的家常菜。然而，有些食材看似普通，搭配在一起却可能暗藏“玄机”，不仅影响食物的色香味，更可能阻碍营养吸收，甚至对身体健康产生微妙的影响。了解这些“食材相克”与“食用禁忌”，是提升饮食智慧、守护家人健康的重要一步。
## 常见食材搭配误区与科学解读
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的
## 科学看待“相克”，智慧搭配日常饮食
## 科学看待“相克”，智慧搭配日常饮食

* **“相克”并非绝对禁忌**：大多数所谓的“食物相克”，在科学研究中并未发现能引起严重中毒或致命后果。很多是基于传统经验、少数案例或体外实验的推测。日常少量食用或偶尔搭配，通常不会对健康造成明显影响。
* **重在均衡多样**：健康的饮食原则是均衡和多样化。与其过分担心“相克”，不如关注整体膳食结构的合理性，避免偏食、挑食。
* **烹饪方式有影响**：某些“相克”问题可以通过恰当的烹饪方式（如焯水、高温加热）来避免或减轻。
* **个体差异大**：每个人的体质、消化能力和对食物的敏感度都不同。对某些人来说可能引起不适的组合，对另一些人可能毫无影响。
* **关注自身感受**：如果在食用某种搭配后感到不适，应予以留意并在下次避免。
* **特殊人群请咨询专业人士**：如果您有特殊的健康状况、慢性疾病（如糖尿病、肾病等）或对某些食物过敏史，务必咨询医生或注册营养师的专业意见，他们能提供更具针对性和个性化的饮食建议。

希望这份详尽的食材搭配指南，能帮助您在享受烹饪乐趣的同时，更好地为自己和家人构筑一道健康防线！让我们一起吃得美味，吃得安心，吃得健康！
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
## 正文
# 凉拌
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 猪肉
食材名称: 猪肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 青椒
食材名称: 青椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 芹菜
食材名称: 芹菜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 萝卜
食材名称: 萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=5
source: rerank_input

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=6
source: rerank_input

```text
命中关键词: 莲藕
食材名称: 莲藕
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=7
source: rerank_input

```text
命中关键词: 蘑菇
食材名称: 蘑菇
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=8
source: rerank_input

```text
命中关键词: 西兰花
食材名称: 西兰花
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=9
source: rerank_input

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=10
source: rerank_input

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

### pair_order=11
source: rerank_input

```text
菜系: 技巧知识
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

### pair_order=12
source: rerank_input

```text
菜品: 洋葱炒猪肉
菜系: 未知
## 标签
猪肉可选猪肩肉片或肉丝
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=13
source: rerank_input

```text
菜系: 技巧知识
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含
```

### pair_order=14
source: rerank_input

```text
菜品: 农家一碗香
菜系: 湘菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将猪肉切片，最好把肥瘦分开放；青椒和小米辣切成段；蒜片用刀背拍成末；姜切成丝；鸡蛋打到小碗中，用筷子打散。
方法: 切,拍,打散
工具: 刀,案板,碗,筷子

### 第2步
步骤: 步骤2
描述: 锅中倒油，开小火，油热后倒入蛋液，炒散至断生，盛出备用。
方法: 炒
工具: 炒锅,锅铲,碗

### 第3步
步骤: 步骤3
描述: 锅中再加少许油，小火将肥猪肉下锅逼出猪油。
方法: 煎,煸
工具: 炒锅,锅铲

### 第4步
步骤: 步骤4
描述: 肥肉呈金黄色时转中火，加入瘦肉翻炒至变色。
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 加入姜丝、蒜末和豆瓣酱，翻炒均匀给猪肉上色。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 放入青红椒和炒好的鸡蛋，加入酱油和白糖，翻炒至青椒微微断生，保持清脆口感。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 出锅装盘即可。
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=15
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

### pair_order=16
source: rerank_input

```text
菜系: 技巧知识
## 注意事项
#### 注意事项

* 猪肉与禽肉没有例外，必须十成熟，必须完全熟制，必须不见任何血水
* 部分牛肉、鱼肉、海鲜类在确认安全后可生食

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=17
source: rerank_input

```text
菜品: 冬瓜酿肉
菜系: 未知
## 所需食材
1. 冬瓜(200g)
2. 水(50ml)
3. 水淀粉(25g)
4. 淀粉(5g)
5. 猪肉末(300g)
6. 生抽(10ml)
7. 盐(20g)
8. 胡椒粉(5g)
9. 葱姜末(30g)
10. 葱花(20g)
11. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=18
source: rerank_input

```text
菜品: 青椒土豆炒肉
菜系: 未知
## 所需食材
1. 土豆(300g)
2. 土豆淀粉(5g)
3. 姜(5g)
4. 水(15g)
5. 猪肉（五花肉）(200g)
6. 盐(7g)
7. 葱(10g)
8. 蒜(12g)
9. 酱油(6-10ml)
10. 青椒(200g)
11. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=19
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 揭秘食材搭配的智慧：这些食物不宜同食

在日常烹饪中，我们都希望做出美味又健康的家常菜。然而，有些食材看似普通，搭配在一起却可能暗藏“玄机”，不仅影响食物的色香味，更可能阻碍营养吸收，甚至对身体健康产生微妙的影响。了解这些“食材相克”与“食用禁忌”，是提升饮食智慧、守护家人健康的重要一步。
## 常见食材搭配误区与科学解读
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201001780, chunk_id=201001780_chunk_381, recipe_name=洋葱炒猪肉, category=荤菜, score=0.6166141033172607, search_type=vector_enhanced

```text
## 标签
猪肉可选猪肩肉片或肉丝
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5852751731872559, search_type=vector_enhanced

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

### result_order=2
source: reranked_results
metadata_summary: node_id=201003355, chunk_id=201003355_chunk_660, recipe_name=青椒土豆炒肉, category=荤菜, score=0.5688109993934631, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(300g)
2. 土豆淀粉(5g)
3. 姜(5g)
4. 水(15g)
5. 猪肉（五花肉）(200g)
6. 盐(7g)
7. 葱(10g)
8. 蒜(12g)
9. 酱油(6-10ml)
10. 青椒(200g)
11. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201002179, chunk_id=201002179_chunk_452, recipe_name=冬瓜酿肉, category=荤菜, score=0.5718494653701782, search_type=vector_enhanced

```text
## 所需食材
1. 冬瓜(200g)
2. 水(50ml)
3. 水淀粉(25g)
4. 淀粉(5g)
5. 猪肉末(300g)
6. 生抽(10ml)
7. 盐(20g)
8. 胡椒粉(5g)
9. 葱姜末(30g)
10. 葱花(20g)
11. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_7e937e95d07f,tipdoc_fd7f557c37a7, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 揭秘食材搭配的智慧：这些食物不宜同食

在日常烹饪中，我们都希望做出美味又健康的家常菜。然而，有些食材看似普通，搭配在一起却可能暗藏“玄机”，不仅影响食物的色香味，更可能阻碍营养吸收，甚至对身体健康产生微妙的影响。了解这些“食材相克”与“食用禁忌”，是提升饮食智慧、守护家人健康的重要一步。
## 常见食材搭配误区与科学解读
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的
## 科学看待“相克”，智慧搭配日常饮食
## 科学看待“相克”，智慧搭配日常饮食

* **“相克”并非绝对禁忌**：大多数所谓的“食物相克”，在科学研究中并未发现能引起严重中毒或致命后果。很多是基于传统经验、少数案例或体外实验的推测。日常少量食用或偶尔搭配，通常不会对健康造成明显影响。
* **重在均衡多样**：健康的饮食原则是均衡和多样化。与其过分担心“相克”，不如关注整体膳食结构的合理性，避免偏食、挑食。
* **烹饪方式有影响**：某些“相克”问题可以通过恰当的烹饪方式（如焯水、高温加热）来避免或减轻。
* **个体差异大**：每个人的体质、消化能力和对食物的敏感度都不同。对某些人来说可能引起不适的组合，对另一些人可能毫无影响。
* **关注自身感受**：如果在食用某种搭配后感到不适，应予以留意并在下次避免。
* **特殊人群请咨询专业人士**：如果您有特殊的健康状况、慢性疾病（如糖尿病、肾病等）或对某些食物过敏史，务必咨询医生或注册营养师的专业意见，他们能提供更具针对性和个性化的饮食建议。

希望这份详尽的食材搭配指南，能帮助您在享受烹饪乐趣的同时，更好地为自己和家人构筑一道健康防线！让我们一起吃得美味，吃得安心，吃得健康！
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
## 正文
# 凉拌
```

### result_order=5
source: reranked_results
metadata_summary: node_id=tipdoc_7e937e95d07f, chunk_id=tipdoc_7e937e95d07f_chunk_1231, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食, category=通用知识, score=0.5906415581703186, search_type=vector_enhanced

```text
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的钙结合，形成草酸钙。
 * **可能影响**：影响钙的吸收，降低牛奶的补钙效果。
 * **健康建议**：建议分开食用，或间隔一段时间。

6. **豆浆 + 鸡蛋：蛋白质的“消化挑战”**
 * **相克原理**：未煮熟的豆浆中含有一种胰蛋白酶抑制剂，会影响人体对蛋白质的消化和吸收。
 * **可能影响**：降低鸡蛋蛋白质的利用率，可能引起消化不良。
 * **健康建议**：确保豆浆彻底煮沸、煮透后（假沸不算），再搭配鸡蛋食用，这样胰蛋白酶抑制剂会被破坏，不会产生不良影响。

7. **黄瓜 + 西红柿：维生素C的“默默流失”**
 * **相克原理**：与胡萝卜类似，黄瓜中也含有一种维生素 C 分解酶。
 * **可能影响**：破坏西红柿等食物中的维生素 C，降低其抗氧化和免疫增强作用。
 * **健康建议**：最好分开食用，如果要做沙拉，可以考虑先吃西红柿，再吃黄瓜，或将两者分别处理。

8. **羊肉 + 西瓜：寒热的“碰撞”**
 * **相克原理**：羊肉性温热，具有补虚祛寒的功效；西瓜性寒凉，有清热解暑作用。
 * **可能影响**：两者同食，寒热性质相悖，可能导致脾胃不适，引起腹泻、腹胀等消化问题，尤其对于脾胃虚弱者。
 * **健康建议**：避免在同一餐中大量食用。

9. **猪肉 + 茶：蛋白质吸收的“阻碍”**
 * **相克原理**：茶叶中含有鞣酸，与猪肉中的蛋白质结合，会形成不易消化的沉淀物。
 * **可能影响**：影响蛋白质的消化吸收，可能引起便秘或消化不良。
 * **健康建议**：饭后一小时再饮茶，或避免在吃肉类时大量饮用浓茶。

10. **蜂蜜 + 豆腐：消化“不协调”**
 * **相克原理**：蜂蜜中的有机酸与豆腐中的蛋白质结合，可能形成不易消化的物质。
 * **可能影响**：可能引起肠胃不适，如腹泻。
 * **健康建议**：尽量避免同食。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 揭秘食材搭配的智慧：这些食物不宜同食 / 科学看待“相克”，智慧搭配日常饮食 (TechniqueChunk): category: 通用知识
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_449, recipe_name=农家一碗香, category=荤菜, score=0.5861289501190186, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将猪肉切片，最好把肥瘦分开放；青椒和小米辣切成段；蒜片用刀背拍成末；姜切成丝；鸡蛋打到小碗中，用筷子打散。
方法: 切,拍,打散
工具: 刀,案板,碗,筷子

### 第2步
步骤: 步骤2
描述: 锅中倒油，开小火，油热后倒入蛋液，炒散至断生，盛出备用。
方法: 炒
工具: 炒锅,锅铲,碗

### 第3步
步骤: 步骤3
描述: 锅中再加少许油，小火将肥猪肉下锅逼出猪油。
方法: 煎,煸
工具: 炒锅,锅铲

### 第4步
步骤: 步骤4
描述: 肥肉呈金黄色时转中火，加入瘦肉翻炒至变色。
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 加入姜丝、蒜末和豆瓣酱，翻炒均匀给猪肉上色。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 放入青红椒和炒好的鸡蛋，加入酱油和白糖，翻炒至青椒微微断生，保持清脆口感。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 出锅装盘即可。
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6217882633209229, search_type=vector_enhanced

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

### result_order=8
source: reranked_results
metadata_summary: node_id=201005130, recipe_name=西兰花, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西兰花
食材名称: 西兰花
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=9
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1322, recipe_name=凉拌, category=烹饪技巧, score=0.5791282653808594, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 猪肉与禽肉没有例外，必须十成熟，必须完全熟制，必须不见任何血水
* 部分牛肉、鱼肉、海鲜类在确认安全后可生食

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 奶酪培根通心粉
分类: 荤菜
菜系: 美式
难度: 3.0
主要食材: 洋葱, 黄油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201000438, recipe_name=青椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 青椒
食材名称: 青椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201001901, recipe_name=土豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 土豆
食材名称: 土豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=13
source: reranked_results
metadata_summary: node_id=201001758, recipe_name=芹菜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 芹菜
食材名称: 芹菜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201004806, recipe_name=蘑菇, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蘑菇
食材名称: 蘑菇
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=15
source: reranked_results
metadata_summary: node_id=201005331, recipe_name=萝卜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 萝卜
食材名称: 萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=16
source: reranked_results
metadata_summary: node_id=201004769, recipe_name=豆角, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆角
食材名称: 豆角
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=17
source: reranked_results
metadata_summary: node_id=201005369, recipe_name=莲藕, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 莲藕
食材名称: 莲藕
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=18
source: reranked_results
metadata_summary: node_id=201001782, recipe_name=猪肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 猪肉
食材名称: 猪肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=19
source: reranked_results
metadata_summary: node_id=201000411, recipe_name=蛏抱蛋, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 家常菜
菜品: 蛏抱蛋
分类: 水产
菜系: 闽菜
难度: 3.0
主要食材: 鸡蛋, 食用油, 鸡精
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 鸡精 (Ingredient): category: 调料
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201001780, chunk_id=201001780_chunk_381, recipe_name=洋葱炒猪肉, category=荤菜, score=0.6166141033172607, search_type=vector_enhanced

```text
## 标签
猪肉可选猪肩肉片或肉丝
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5852751731872559, search_type=vector_enhanced

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

### result_order=2
source: top_k_final
metadata_summary: node_id=201003355, chunk_id=201003355_chunk_660, recipe_name=青椒土豆炒肉, category=荤菜, score=0.5688109993934631, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(300g)
2. 土豆淀粉(5g)
3. 姜(5g)
4. 水(15g)
5. 猪肉（五花肉）(200g)
6. 盐(7g)
7. 葱(10g)
8. 蒜(12g)
9. 酱油(6-10ml)
10. 青椒(200g)
11. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_7e937e95d07f,tipdoc_fd7f557c37a7, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 揭秘食材搭配的智慧：这些食物不宜同食

在日常烹饪中，我们都希望做出美味又健康的家常菜。然而，有些食材看似普通，搭配在一起却可能暗藏“玄机”，不仅影响食物的色香味，更可能阻碍营养吸收，甚至对身体健康产生微妙的影响。了解这些“食材相克”与“食用禁忌”，是提升饮食智慧、守护家人健康的重要一步。
## 常见食材搭配误区与科学解读
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的
## 科学看待“相克”，智慧搭配日常饮食
## 科学看待“相克”，智慧搭配日常饮食

* **“相克”并非绝对禁忌**：大多数所谓的“食物相克”，在科学研究中并未发现能引起严重中毒或致命后果。很多是基于传统经验、少数案例或体外实验的推测。日常少量食用或偶尔搭配，通常不会对健康造成明显影响。
* **重在均衡多样**：健康的饮食原则是均衡和多样化。与其过分担心“相克”，不如关注整体膳食结构的合理性，避免偏食、挑食。
* **烹饪方式有影响**：某些“相克”问题可以通过恰当的烹饪方式（如焯水、高温加热）来避免或减轻。
* **个体差异大**：每个人的体质、消化能力和对食物的敏感度都不同。对某些人来说可能引起不适的组合，对另一些人可能毫无影响。
* **关注自身感受**：如果在食用某种搭配后感到不适，应予以留意并在下次避免。
* **特殊人群请咨询专业人士**：如果您有特殊的健康状况、慢性疾病（如糖尿病、肾病等）或对某些食物过敏史，务必咨询医生或注册营养师的专业意见，他们能提供更具针对性和个性化的饮食建议。

希望这份详尽的食材搭配指南，能帮助您在享受烹饪乐趣的同时，更好地为自己和家人构筑一道健康防线！让我们一起吃得美味，吃得安心，吃得健康！
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
## 正文
# 凉拌
```

### result_order=4
source: top_k_final
metadata_summary: node_id=tipdoc_7e937e95d07f, chunk_id=tipdoc_7e937e95d07f_chunk_1231, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食, category=通用知识, score=0.5906415581703186, search_type=vector_enhanced

```text
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的钙结合，形成草酸钙。
 * **可能影响**：影响钙的吸收，降低牛奶的补钙效果。
 * **健康建议**：建议分开食用，或间隔一段时间。

6. **豆浆 + 鸡蛋：蛋白质的“消化挑战”**
 * **相克原理**：未煮熟的豆浆中含有一种胰蛋白酶抑制剂，会影响人体对蛋白质的消化和吸收。
 * **可能影响**：降低鸡蛋蛋白质的利用率，可能引起消化不良。
 * **健康建议**：确保豆浆彻底煮沸、煮透后（假沸不算），再搭配鸡蛋食用，这样胰蛋白酶抑制剂会被破坏，不会产生不良影响。

7. **黄瓜 + 西红柿：维生素C的“默默流失”**
 * **相克原理**：与胡萝卜类似，黄瓜中也含有一种维生素 C 分解酶。
 * **可能影响**：破坏西红柿等食物中的维生素 C，降低其抗氧化和免疫增强作用。
 * **健康建议**：最好分开食用，如果要做沙拉，可以考虑先吃西红柿，再吃黄瓜，或将两者分别处理。

8. **羊肉 + 西瓜：寒热的“碰撞”**
 * **相克原理**：羊肉性温热，具有补虚祛寒的功效；西瓜性寒凉，有清热解暑作用。
 * **可能影响**：两者同食，寒热性质相悖，可能导致脾胃不适，引起腹泻、腹胀等消化问题，尤其对于脾胃虚弱者。
 * **健康建议**：避免在同一餐中大量食用。

9. **猪肉 + 茶：蛋白质吸收的“阻碍”**
 * **相克原理**：茶叶中含有鞣酸，与猪肉中的蛋白质结合，会形成不易消化的沉淀物。
 * **可能影响**：影响蛋白质的消化吸收，可能引起便秘或消化不良。
 * **健康建议**：饭后一小时再饮茶，或避免在吃肉类时大量饮用浓茶。

10. **蜂蜜 + 豆腐：消化“不协调”**
 * **相克原理**：蜂蜜中的有机酸与豆腐中的蛋白质结合，可能形成不易消化的物质。
 * **可能影响**：可能引起肠胃不适，如腹泻。
 * **健康建议**：尽量避免同食。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 揭秘食材搭配的智慧：这些食物不宜同食 / 科学看待“相克”，智慧搭配日常饮食 (TechniqueChunk): category: 通用知识
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201001780, chunk_id=201001780_chunk_381, recipe_name=洋葱炒猪肉, category=荤菜, score=0.6166141033172607, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 标签
猪肉可选猪肩肉片或肉丝
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5852751731872559, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=2
source: generation_context
metadata_summary: node_id=201003355, chunk_id=201003355_chunk_660, recipe_name=青椒土豆炒肉, category=荤菜, score=0.5688109993934631, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 土豆(300g)
2. 土豆淀粉(5g)
3. 姜(5g)
4. 水(15g)
5. 猪肉（五花肉）(200g)
6. 盐(7g)
7. 葱(10g)
8. 蒜(12g)
9. 酱油(6-10ml)
10. 青椒(200g)
11. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_7e937e95d07f,tipdoc_fd7f557c37a7, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 揭秘食材搭配的智慧：这些食物不宜同食、如何决策吃什么、凉拌
关键技巧内容:
## 正文
# 揭秘食材搭配的智慧：这些食物不宜同食

在日常烹饪中，我们都希望做出美味又健康的家常菜。然而，有些食材看似普通，搭配在一起却可能暗藏“玄机”，不仅影响食物的色香味，更可能阻碍营养吸收，甚至对身体健康产生微妙的影响。了解这些“食材相克”与“食用禁忌”，是提升饮食智慧、守护家人健康的重要一步。
## 常见食材搭配误区与科学解读
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的
## 科学看待“相克”，智慧搭配日常饮食
## 科学看待“相克”，智慧搭配日常饮食

* **“相克”并非绝对禁忌**：大多数所谓的“食物相克”，在科学研究中并未发现能引起严重中毒或致命后果。很多是基于传统经验、少数案例或体外实验的推测。日常少量食用或偶尔搭配，通常不会对健康造成明显影响。
* **重在均衡多样**：健康的饮食原则是均衡和多样化。与其过分担心“相克”，不如关注整体膳食结构的合理性，避免偏食、挑食。
* **烹饪方式有影响**：某些“相克”问题可以通过恰当的烹饪方式（如焯水、高温加热）来避免或减轻。
* **个体差异大**：每个人的体质、消化能力和对食物的敏感度都不同。对某些人来说可能引起不适的组合，对另一些人可能毫无影响。
* **关注自身感受**：如果在食用某种搭配后感到不适，应予以留意并在下次避免。
* **特殊人群请咨询专业人士**：如果您有特殊的健康状况、慢性疾病（如糖尿病、肾病等）或对某些食物过敏史，务必咨询医生或注册营养师的专业意见，他们能提供更具针对性和个性化的饮食建议。

希望这份详尽的食材搭配指南，能帮助您在享受烹饪乐趣的同时，更好地为自己和家人构筑一道健康防线！让我们一起吃得美味，吃得安心，吃得健康！
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
## 正文
# 凉拌
```

### result_order=4
source: generation_context
metadata_summary: node_id=tipdoc_7e937e95d07f, chunk_id=tipdoc_7e937e95d07f_chunk_1231, recipe_name=揭秘食材搭配的智慧：这些食物不宜同食, category=通用知识, score=0.5906415581703186, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 常见食材搭配误区与科学解读

以下是一些在我们的餐桌上，需要特别留意的食材组合：

1. **菠菜 + 豆腐：草酸与钙质的“交锋”**
 * **相克原理**：菠菜富含草酸，而豆腐是钙质的优质来源。当两者同食时，草酸会与钙离子结合形成不溶于水的草酸钙。
 * **可能影响**：草酸钙不仅难以被人体吸收利用，长期大量摄入还可能增加结石的风险。
 * **健康建议**：在烹饪菠菜前，建议先用沸水焯烫一下，可以有效去除大部分草酸，从而减少其与钙的结合。

2. **胡萝卜 + 白萝卜：维生素C的“损耗者”**
 * **相克原理**：胡萝卜中含有一种特殊的“抗坏血酸氧化酶”（即维生素 C 分解酶），它会破坏其他食物中的维生素 C。
 * **可能影响**：导致白萝卜（以及其他富含维生素 C 的食物，如柑橘类）中的维生素 C 大量流失，降低其营养价值。
 * **健康建议**：两者最好分开食用，或将胡萝卜烹熟后再与富含维生素 C 的食物同食，因为高温会使酶失去活性。

3. **虾类 + 大量维生素C：潜在的风险，但无需过度恐慌**
 * **相克原理**：虾等甲壳类水产品体内含有一种“五价砷”化合物。在极高剂量维生素 C 的还原作用下，五价砷理论上可能被还原为剧毒的“三价砷”（俗称砒霜）。
 * **可能影响**：理论上中毒，但**请注意**：日常饮食中虾类和维生素 C 的摄入量，远不足以达到引发中毒的剂量。这是一个被夸大的“相克”，不必过度恐慌。
 * **健康建议**：正常饮食即可，无需刻意回避。避免一次性大量摄入。

4. **柿子 + 螃蟹：消化道的“双重考验”**
 * **相克原理**：柿子富含鞣酸（又称单宁酸），螃蟹则蛋白质含量高。鞣酸遇到蛋白质容易凝固成不易消化的块状物——鞣酸蛋白。
 * **可能影响**：可能导致肠胃不适，如腹胀、腹痛、恶心、呕吐，甚至加重便秘。
 * **健康建议**：尽量避免同食，或至少间隔数小时。脾胃虚寒者尤其要注意。

5. **牛奶 + 巧克力：钙质吸收的“隐形障碍”**
 * **相克原理**：巧克力中含有草酸，与牛奶中的钙结合，形成草酸钙。
 * **可能影响**：影响钙的吸收，降低牛奶的补钙效果。
 * **健康建议**：建议分开食用，或间隔一段时间。

6. **豆浆 + 鸡蛋：蛋白质的“消化挑战”**
 * **相克原理**：未煮熟的豆浆中含有一种胰蛋白酶抑制剂，会影响人体对蛋白质的消化和吸收。
 * **可能影响**：降低鸡蛋蛋白质的利用率，可能引起消化不良。
 * **健康建议**：确保豆浆彻底煮沸、煮透后（假沸不算），再搭配鸡蛋食用，这样胰蛋白酶抑制剂会被破坏，不会产生不良影响。

7. **黄瓜 + 西红柿：维生素C的“默默流失”**
 * **相克原理**：与胡萝卜类似，黄瓜中也含有一种维生素 C 分解酶。
 * **可能影响**：破坏西红柿等食物中的维生素 C，降低其抗氧化和免疫增强作用。
 * **健康建议**：最好分开食用，如果要做沙拉，可以考虑先吃西红柿，再吃黄瓜，或将两者分别处理。

8. **羊肉 + 西瓜：寒热的“碰撞”**
 * **相克原理**：羊肉性温热，具有补虚祛寒的功效；西瓜性寒凉，有清热解暑作用。
 * **可能影响**：两者同食，寒热性质相悖，可能导致脾胃不适，引起腹泻、腹胀等消化问题，尤其对于脾胃虚弱者。
 * **健康建议**：避免在同一餐中大量食用。

9. **猪肉 + 茶：蛋白质吸收的“阻碍”**
 * **相克原理**：茶叶中含有鞣酸，与猪肉中的蛋白质结合，会形成不易消化的沉淀物。
 * **可能影响**：影响蛋白质的消化吸收，可能引起便秘或消化不良。
 * **健康建议**：饭后一小时再饮茶，或避免在吃肉类时大量饮用浓茶。

10. **蜂蜜 + 豆腐：消化“不协调”**
 * **相克原理**：蜂蜜中的有机酸与豆腐中的蛋白质结合，可能形成不易消化的物质。
 * **可能影响**：可能引起肠胃不适，如腹泻。
 * **健康建议**：尽量避免同食。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 揭秘食材搭配的智慧：这些食物不宜同食 / 科学看待“相克”，智慧搭配日常饮食 (TechniqueChunk): category: 通用知识
```

