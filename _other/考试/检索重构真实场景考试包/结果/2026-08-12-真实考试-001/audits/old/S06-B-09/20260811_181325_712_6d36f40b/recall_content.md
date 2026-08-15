# Recall Content

audit_id: 20260811_181325_712_6d36f40b
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201003481, recipe_name=麻婆豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 麻婆豆腐
菜品名称: 麻婆豆腐
分类: 荤菜
菜系: 川菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201003180, recipe_name=辣椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 辣椒
食材名称: 辣椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201000167, recipe_name=花椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 花椒
食材名称: 花椒
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
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
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6563551425933838, search_type=vector_enhanced

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

### result_order=1
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6336433291435242, search_type=vector_enhanced

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

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.6307153701782227, search_type=vector_enhanced

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

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201002797, chunk_id=201002797_chunk_552, recipe_name=水煮牛肉, category=荤菜, score=0.6295167803764343, search_type=vector_enhanced

```text
## 所需食材
1. 姜(20g)
2. 干辣椒粉(5g)
3. 料酒(10ml)
4. 淀粉(15g)
5. 牛肉(300g)
6. 红辣椒(1根)
7. 蒜(3瓣)
8. 蚝油(8g)
9. 豆瓣酱(10g)
10. 豆芽(100g)
11. 香菜(5根)
12. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.628713846206665, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.6273142695426941, search_type=vector_enhanced

```text
## 所需食材
1. 小葱(10g)
2. 碱水面(250g)
3. 肉末(30g)
4. 肉汤汁(30ml)
5. 胡椒粉(0-10g)
6. 芝麻酱(40ml)
7. 萝卜干(50g)
8. 蒜水(30ml)
9. 辣椒油(0-10ml)
10. 酱油(5ml)
11. 酸豆角(20g)
12. 食盐(3g)
13. 鸡精(0-3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201004306, chunk_id=201004306_chunk_853, recipe_name=螺蛳粉, category=主食, score=0.625817596912384, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，将水烧开
方法: 煮
工具: 煮锅,电磁炉/灶台

### 第2步
步骤: 步骤2
描述: 下米粉，煮3-5分钟，期间用筷子搅拌，防止米粉粘在一起
方法: 煮
工具: 煮锅,筷子
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 下汤料包，按个人口味添加
方法: 煮
工具: 煮锅

### 第4步
步骤: 步骤4
描述: 下一部分配料包，如木耳、花生、螺蛳（这部分配料需要煮一会才入味）
方法: 煮
工具: 煮锅

### 第5步
步骤: 步骤5
描述: 下调味包，按个人口味添加
方法: 煮
工具: 煮锅

### 第6步
步骤: 步骤6
描述: 搅拌后捞出，放入碗中
方法: 捞取
工具: 筷子,碗

### 第7步
步骤: 步骤7
描述: 下剩下的配料包，如酸笋、豆皮（这部分配料不适合被汤泡太久）
方法: 拌
工具: 筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6252442002296448, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_596, recipe_name=羊排焖面, category=荤菜, score=0.6242196559906006, search_type=vector_enhanced

```text
## 所需食材
1. 中筋面粉(300克)
2. 大葱
3. 带皮羊排(500克)
4. 干辣椒
5. 水(180毫升)
6. 甜椒(2个)
7. 生姜(4片)
8. 白砂糖
9. 盐
10. 盐（和面用）(3克)
11. 老抽
12. 花椒
13. 青椒(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201002776, chunk_id=201002776_chunk_548, recipe_name=梅菜扣肉, category=荤菜, score=0.6231718063354492, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(200g)
2. 五香粉(2g)
3. 小米椒(1个)
4. 梅菜(30g)
5. 生抽(20ml)
6. 白砂糖(5g)
7. 老抽(30ml)
8. 蒜末(10g)
9. 食用油(300ml)
10. 食用盐(2g)
11. 鸡精(2g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201003481, recipe_name=麻婆豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 麻婆豆腐
菜品名称: 麻婆豆腐
分类: 荤菜
菜系: 川菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201003180, recipe_name=辣椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 辣椒
食材名称: 辣椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000167, recipe_name=花椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 花椒
食材名称: 花椒
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=3
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

### result_order=4
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

### result_order=5
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6563551425933838, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6336433291435242, search_type=vector_enhanced

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

### result_order=7
source: branch_grouped
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.6307153701782227, search_type=vector_enhanced

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

### result_order=8
source: branch_grouped
metadata_summary: node_id=201002797, chunk_id=201002797_chunk_552, recipe_name=水煮牛肉, category=荤菜, score=0.6295167803764343, search_type=vector_enhanced

```text
## 所需食材
1. 姜(20g)
2. 干辣椒粉(5g)
3. 料酒(10ml)
4. 淀粉(15g)
5. 牛肉(300g)
6. 红辣椒(1根)
7. 蒜(3瓣)
8. 蚝油(8g)
9. 豆瓣酱(10g)
10. 豆芽(100g)
11. 香菜(5根)
12. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.628713846206665, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.6273142695426941, search_type=vector_enhanced

```text
## 所需食材
1. 小葱(10g)
2. 碱水面(250g)
3. 肉末(30g)
4. 肉汤汁(30ml)
5. 胡椒粉(0-10g)
6. 芝麻酱(40ml)
7. 萝卜干(50g)
8. 蒜水(30ml)
9. 辣椒油(0-10ml)
10. 酱油(5ml)
11. 酸豆角(20g)
12. 食盐(3g)
13. 鸡精(0-3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201004306, chunk_id=201004306_chunk_853, recipe_name=螺蛳粉, category=主食, score=0.625817596912384, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，将水烧开
方法: 煮
工具: 煮锅,电磁炉/灶台

### 第2步
步骤: 步骤2
描述: 下米粉，煮3-5分钟，期间用筷子搅拌，防止米粉粘在一起
方法: 煮
工具: 煮锅,筷子
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 下汤料包，按个人口味添加
方法: 煮
工具: 煮锅

### 第4步
步骤: 步骤4
描述: 下一部分配料包，如木耳、花生、螺蛳（这部分配料需要煮一会才入味）
方法: 煮
工具: 煮锅

### 第5步
步骤: 步骤5
描述: 下调味包，按个人口味添加
方法: 煮
工具: 煮锅

### 第6步
步骤: 步骤6
描述: 搅拌后捞出，放入碗中
方法: 捞取
工具: 筷子,碗

### 第7步
步骤: 步骤7
描述: 下剩下的配料包，如酸笋、豆皮（这部分配料不适合被汤泡太久）
方法: 拌
工具: 筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6252442002296448, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_596, recipe_name=羊排焖面, category=荤菜, score=0.6242196559906006, search_type=vector_enhanced

```text
## 所需食材
1. 中筋面粉(300克)
2. 大葱
3. 带皮羊排(500克)
4. 干辣椒
5. 水(180毫升)
6. 甜椒(2个)
7. 生姜(4片)
8. 白砂糖
9. 盐
10. 盐（和面用）(3克)
11. 老抽
12. 花椒
13. 青椒(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201002776, chunk_id=201002776_chunk_548, recipe_name=梅菜扣肉, category=荤菜, score=0.6231718063354492, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(200g)
2. 五香粉(2g)
3. 小米椒(1个)
4. 梅菜(30g)
5. 生抽(20ml)
6. 白砂糖(5g)
7. 老抽(30ml)
8. 蒜末(10g)
9. 食用油(300ml)
10. 食用盐(2g)
11. 鸡精(2g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201003481, recipe_name=麻婆豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 麻婆豆腐
菜品名称: 麻婆豆腐
分类: 荤菜
菜系: 川菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201003180, recipe_name=辣椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 辣椒
食材名称: 辣椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000167, recipe_name=花椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 花椒
食材名称: 花椒
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=3
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

### result_order=4
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

### result_order=5
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6563551425933838, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6336433291435242, search_type=vector_enhanced

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

### result_order=7
source: merged_candidates
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.6307153701782227, search_type=vector_enhanced

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

### result_order=8
source: merged_candidates
metadata_summary: node_id=201002797, chunk_id=201002797_chunk_552, recipe_name=水煮牛肉, category=荤菜, score=0.6295167803764343, search_type=vector_enhanced

```text
## 所需食材
1. 姜(20g)
2. 干辣椒粉(5g)
3. 料酒(10ml)
4. 淀粉(15g)
5. 牛肉(300g)
6. 红辣椒(1根)
7. 蒜(3瓣)
8. 蚝油(8g)
9. 豆瓣酱(10g)
10. 豆芽(100g)
11. 香菜(5根)
12. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.628713846206665, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.6273142695426941, search_type=vector_enhanced

```text
## 所需食材
1. 小葱(10g)
2. 碱水面(250g)
3. 肉末(30g)
4. 肉汤汁(30ml)
5. 胡椒粉(0-10g)
6. 芝麻酱(40ml)
7. 萝卜干(50g)
8. 蒜水(30ml)
9. 辣椒油(0-10ml)
10. 酱油(5ml)
11. 酸豆角(20g)
12. 食盐(3g)
13. 鸡精(0-3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201004306, chunk_id=201004306_chunk_853, recipe_name=螺蛳粉, category=主食, score=0.625817596912384, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，将水烧开
方法: 煮
工具: 煮锅,电磁炉/灶台

### 第2步
步骤: 步骤2
描述: 下米粉，煮3-5分钟，期间用筷子搅拌，防止米粉粘在一起
方法: 煮
工具: 煮锅,筷子
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 下汤料包，按个人口味添加
方法: 煮
工具: 煮锅

### 第4步
步骤: 步骤4
描述: 下一部分配料包，如木耳、花生、螺蛳（这部分配料需要煮一会才入味）
方法: 煮
工具: 煮锅

### 第5步
步骤: 步骤5
描述: 下调味包，按个人口味添加
方法: 煮
工具: 煮锅

### 第6步
步骤: 步骤6
描述: 搅拌后捞出，放入碗中
方法: 捞取
工具: 筷子,碗

### 第7步
步骤: 步骤7
描述: 下剩下的配料包，如酸笋、豆皮（这部分配料不适合被汤泡太久）
方法: 拌
工具: 筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6252442002296448, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_596, recipe_name=羊排焖面, category=荤菜, score=0.6242196559906006, search_type=vector_enhanced

```text
## 所需食材
1. 中筋面粉(300克)
2. 大葱
3. 带皮羊排(500克)
4. 干辣椒
5. 水(180毫升)
6. 甜椒(2个)
7. 生姜(4片)
8. 白砂糖
9. 盐
10. 盐（和面用）(3克)
11. 老抽
12. 花椒
13. 青椒(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201002776, chunk_id=201002776_chunk_548, recipe_name=梅菜扣肉, category=荤菜, score=0.6231718063354492, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(200g)
2. 五香粉(2g)
3. 小米椒(1个)
4. 梅菜(30g)
5. 生抽(20ml)
6. 白砂糖(5g)
7. 老抽(30ml)
8. 蒜末(10g)
9. 食用油(300ml)
10. 食用盐(2g)
11. 鸡精(2g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e, recipe_name=如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么
关键技巧内容:
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
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 麻婆豆腐
菜品名称: 麻婆豆腐
分类: 荤菜
菜系: 川菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 辣椒
食材名称: 辣椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 花椒
食材名称: 花椒
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### pair_order=3
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

### pair_order=4
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

### pair_order=7
source: rerank_input

```text
菜品: 农家一碗香
菜系: 湘菜
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

### pair_order=8
source: rerank_input

```text
菜品: 水煮牛肉
菜系: 川菜
## 所需食材
1. 姜(20g)
2. 干辣椒粉(5g)
3. 料酒(10ml)
4. 淀粉(15g)
5. 牛肉(300g)
6. 红辣椒(1根)
7. 蒜(3瓣)
8. 蚝油(8g)
9. 豆瓣酱(10g)
10. 豆芽(100g)
11. 香菜(5根)
12. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=9
source: rerank_input

```text
菜品: 新疆大盘鸡
菜系: 西北菜
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=10
source: rerank_input

```text
菜品: 热干面
菜系: 湖北菜
## 所需食材
1. 小葱(10g)
2. 碱水面(250g)
3. 肉末(30g)
4. 肉汤汁(30ml)
5. 胡椒粉(0-10g)
6. 芝麻酱(40ml)
7. 萝卜干(50g)
8. 蒜水(30ml)
9. 辣椒油(0-10ml)
10. 酱油(5ml)
11. 酸豆角(20g)
12. 食盐(3g)
13. 鸡精(0-3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=11
source: rerank_input

```text
菜品: 螺蛳粉
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，将水烧开
方法: 煮
工具: 煮锅,电磁炉/灶台

### 第2步
步骤: 步骤2
描述: 下米粉，煮3-5分钟，期间用筷子搅拌，防止米粉粘在一起
方法: 煮
工具: 煮锅,筷子
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 下汤料包，按个人口味添加
方法: 煮
工具: 煮锅

### 第4步
步骤: 步骤4
描述: 下一部分配料包，如木耳、花生、螺蛳（这部分配料需要煮一会才入味）
方法: 煮
工具: 煮锅

### 第5步
步骤: 步骤5
描述: 下调味包，按个人口味添加
方法: 煮
工具: 煮锅

### 第6步
步骤: 步骤6
描述: 搅拌后捞出，放入碗中
方法: 捞取
工具: 筷子,碗

### 第7步
步骤: 步骤7
描述: 下剩下的配料包，如酸笋、豆皮（这部分配料不适合被汤泡太久）
方法: 拌
工具: 筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### pair_order=12
source: rerank_input

```text
菜系: 川菜
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=13
source: rerank_input

```text
菜品: 羊排焖面
菜系: 西北菜
## 所需食材
1. 中筋面粉(300克)
2. 大葱
3. 带皮羊排(500克)
4. 干辣椒
5. 水(180毫升)
6. 甜椒(2个)
7. 生姜(4片)
8. 白砂糖
9. 盐
10. 盐（和面用）(3克)
11. 老抽
12. 花椒
13. 青椒(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=14
source: rerank_input

```text
菜品: 梅菜扣肉
菜系: 粤菜
## 所需食材
1. 五花肉(200g)
2. 五香粉(2g)
3. 小米椒(1个)
4. 梅菜(30g)
5. 生抽(20ml)
6. 白砂糖(5g)
7. 老抽(30ml)
8. 蒜末(10g)
9. 食用油(300ml)
10. 食用盐(2g)
11. 鸡精(2g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=15
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 如何决策吃什么
关键技巧内容:
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
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6252442002296448, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6336433291435242, search_type=vector_enhanced

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

### result_order=2
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6563551425933838, search_type=vector_enhanced

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

### result_order=3
source: reranked_results
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.628713846206665, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.6307153701782227, search_type=vector_enhanced

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

### result_order=5
source: reranked_results
metadata_summary: node_id=201003025, chunk_id=201003025_chunk_596, recipe_name=羊排焖面, category=荤菜, score=0.6242196559906006, search_type=vector_enhanced

```text
## 所需食材
1. 中筋面粉(300克)
2. 大葱
3. 带皮羊排(500克)
4. 干辣椒
5. 水(180毫升)
6. 甜椒(2个)
7. 生姜(4片)
8. 白砂糖
9. 盐
10. 盐（和面用）(3克)
11. 老抽
12. 花椒
13. 青椒(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201002797, chunk_id=201002797_chunk_552, recipe_name=水煮牛肉, category=荤菜, score=0.6295167803764343, search_type=vector_enhanced

```text
## 所需食材
1. 姜(20g)
2. 干辣椒粉(5g)
3. 料酒(10ml)
4. 淀粉(15g)
5. 牛肉(300g)
6. 红辣椒(1根)
7. 蒜(3瓣)
8. 蚝油(8g)
9. 豆瓣酱(10g)
10. 豆芽(100g)
11. 香菜(5根)
12. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201002776, chunk_id=201002776_chunk_548, recipe_name=梅菜扣肉, category=荤菜, score=0.6231718063354492, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(200g)
2. 五香粉(2g)
3. 小米椒(1个)
4. 梅菜(30g)
5. 生抽(20ml)
6. 白砂糖(5g)
7. 老抽(30ml)
8. 蒜末(10g)
9. 食用油(300ml)
10. 食用盐(2g)
11. 鸡精(2g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.6273142695426941, search_type=vector_enhanced

```text
## 所需食材
1. 小葱(10g)
2. 碱水面(250g)
3. 肉末(30g)
4. 肉汤汁(30ml)
5. 胡椒粉(0-10g)
6. 芝麻酱(40ml)
7. 萝卜干(50g)
8. 蒜水(30ml)
9. 辣椒油(0-10ml)
10. 酱油(5ml)
11. 酸豆角(20g)
12. 食盐(3g)
13. 鸡精(0-3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=9
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

### result_order=10
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e, recipe_name=如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么
关键技巧内容:
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
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201003481, recipe_name=麻婆豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 麻婆豆腐
菜品名称: 麻婆豆腐
分类: 荤菜
菜系: 川菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=12
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

### result_order=13
source: reranked_results
metadata_summary: node_id=201004306, chunk_id=201004306_chunk_853, recipe_name=螺蛳粉, category=主食, score=0.625817596912384, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅中加水，将水烧开
方法: 煮
工具: 煮锅,电磁炉/灶台

### 第2步
步骤: 步骤2
描述: 下米粉，煮3-5分钟，期间用筷子搅拌，防止米粉粘在一起
方法: 煮
工具: 煮锅,筷子
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 下汤料包，按个人口味添加
方法: 煮
工具: 煮锅

### 第4步
步骤: 步骤4
描述: 下一部分配料包，如木耳、花生、螺蛳（这部分配料需要煮一会才入味）
方法: 煮
工具: 煮锅

### 第5步
步骤: 步骤5
描述: 下调味包，按个人口味添加
方法: 煮
工具: 煮锅

### 第6步
步骤: 步骤6
描述: 搅拌后捞出，放入碗中
方法: 捞取
工具: 筷子,碗

### 第7步
步骤: 步骤7
描述: 下剩下的配料包，如酸笋、豆皮（这部分配料不适合被汤泡太久）
方法: 拌
工具: 筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201003180, recipe_name=辣椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 辣椒
食材名称: 辣椒
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=15
source: reranked_results
metadata_summary: node_id=201000167, recipe_name=花椒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 花椒
食材名称: 花椒
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6252442002296448, search_type=vector_enhanced

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6336433291435242, search_type=vector_enhanced

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

### result_order=2
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6563551425933838, search_type=vector_enhanced

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

### result_order=3
source: top_k_final
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.628713846206665, search_type=vector_enhanced

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e, recipe_name=如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么
关键技巧内容:
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
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6252442002296448, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 北京麻辣方便面(1袋)
2. 干豆腐(152克)
3. 干辣椒(5克)
4. 无骨肉（猪肉、牛肉、鸡肉、鱼丸、火腿肠）(430克)
5. 青菜（油菜、油麦菜、菠菜）(455克)
6. 食用油(105克)
7. 麻辣香锅调料(110克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: generation_context
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6336433291435242, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=2
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6563551425933838, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=3
source: generation_context
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.628713846206665, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 土豆(750g)
2. 大葱(100g)
3. 大蒜(4瓣)
4. 干线椒(5个)
5. 料酒(100g)
6. 油(50g)
7. 清水(1000ml)
8. 甜椒(50g)
9. 生抽(7ml)
10. 白砂糖(20g)
11. 盐(5g)
12. 花椒
13. 菜椒(50g)
14. 蚝油(10g)
15. 香叶(适量片)
16. 香果
17. 鸡腿肉(1000g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e, recipe_name=如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 如何决策吃什么
关键技巧内容:
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
```

