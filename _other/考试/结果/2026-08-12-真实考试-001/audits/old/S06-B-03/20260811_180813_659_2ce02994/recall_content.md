# Recall Content

audit_id: 20260811_180813_659_2ce02994
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201005725, recipe_name=鸡蛋羹, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201004841, recipe_name=凉拌豆腐, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 清淡
菜品: 凉拌豆腐
分类: 素菜
难度: 2.0
主要食材: 白糖, 生抽, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201004215, recipe_name=葱油拌面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 晚餐
菜品: 葱油拌面
分类: 主食
菜系: 沪菜
难度: 2.0
主要食材: 白糖, 小葱, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
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

### result_order=3
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
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6668335199356079, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6661337614059448, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6542143821716309, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.6391054391860962, search_type=vector_enhanced

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

### result_order=4
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6339592933654785, search_type=vector_enhanced

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

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201002797, chunk_id=201002797_chunk_552, recipe_name=水煮牛肉, category=荤菜, score=0.6267493367195129, search_type=vector_enhanced

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

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6257911324501038, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6251769661903381, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_608, recipe_name=芥末罗氏虾, category=荤菜, score=0.622139573097229, search_type=vector_enhanced

```text
## 所需食材
1. 小米辣(2个)
2. 生抽(30g)
3. 生粉(10g)
4. 白糖(3g)
5. 盐(3g)
6. 罗氏虾(250g)
7. 胡椒粉(5g)
8. 蒜(2个)
9. 蚝油(15g)
10. 青芥末(20g)
11. 食用油(80ml)
12. 黄油(20g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201001698, chunk_id=201001698_chunk_367, recipe_name=杀猪菜, category=荤菜, score=0.6213563084602356, search_type=vector_enhanced

```text
## 所需食材
1. 八角(1个)
2. 姜粉(5克)
3. 干辣椒(5个)
4. 排骨(400克)
5. 料酒(10克)
6. 枸杞
7. 生抽(10克)
8. 盐(5克)
9. 菜籽油(10克)
10. 葱结(1个)
11. 蒜瓣(5个)
12. 蒜蓉(5克)
13. 血肠(200克)
14. 辣椒油(5克)
15. 酸菜(500克)
16. 香叶(2片)
17. 香油(10克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201005725, recipe_name=鸡蛋羹, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201004841, recipe_name=凉拌豆腐, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 清淡
菜品: 凉拌豆腐
分类: 素菜
难度: 2.0
主要食材: 白糖, 生抽, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201004215, recipe_name=葱油拌面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 晚餐
菜品: 葱油拌面
分类: 主食
菜系: 沪菜
难度: 2.0
主要食材: 白糖, 小葱, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
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
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6668335199356079, search_type=vector_enhanced

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

### result_order=6
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6661337614059448, search_type=vector_enhanced

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

### result_order=7
source: branch_grouped
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6542143821716309, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.6391054391860962, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6339592933654785, search_type=vector_enhanced

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

### result_order=10
source: branch_grouped
metadata_summary: node_id=201002797, chunk_id=201002797_chunk_552, recipe_name=水煮牛肉, category=荤菜, score=0.6267493367195129, search_type=vector_enhanced

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

### result_order=11
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6257911324501038, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6251769661903381, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_608, recipe_name=芥末罗氏虾, category=荤菜, score=0.622139573097229, search_type=vector_enhanced

```text
## 所需食材
1. 小米辣(2个)
2. 生抽(30g)
3. 生粉(10g)
4. 白糖(3g)
5. 盐(3g)
6. 罗氏虾(250g)
7. 胡椒粉(5g)
8. 蒜(2个)
9. 蚝油(15g)
10. 青芥末(20g)
11. 食用油(80ml)
12. 黄油(20g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201001698, chunk_id=201001698_chunk_367, recipe_name=杀猪菜, category=荤菜, score=0.6213563084602356, search_type=vector_enhanced

```text
## 所需食材
1. 八角(1个)
2. 姜粉(5克)
3. 干辣椒(5个)
4. 排骨(400克)
5. 料酒(10克)
6. 枸杞
7. 生抽(10克)
8. 盐(5克)
9. 菜籽油(10克)
10. 葱结(1个)
11. 蒜瓣(5个)
12. 蒜蓉(5克)
13. 血肠(200克)
14. 辣椒油(5克)
15. 酸菜(500克)
16. 香叶(2片)
17. 香油(10克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201005725, recipe_name=鸡蛋羹, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201004841, recipe_name=凉拌豆腐, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 清淡
菜品: 凉拌豆腐
分类: 素菜
难度: 2.0
主要食材: 白糖, 生抽, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201004215, recipe_name=葱油拌面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 晚餐
菜品: 葱油拌面
分类: 主食
菜系: 沪菜
难度: 2.0
主要食材: 白糖, 小葱, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
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
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6668335199356079, search_type=vector_enhanced

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

### result_order=6
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6661337614059448, search_type=vector_enhanced

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

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6542143821716309, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.6391054391860962, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6339592933654785, search_type=vector_enhanced

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

### result_order=10
source: merged_candidates
metadata_summary: node_id=201002797, chunk_id=201002797_chunk_552, recipe_name=水煮牛肉, category=荤菜, score=0.6267493367195129, search_type=vector_enhanced

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

### result_order=11
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6257911324501038, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6251769661903381, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_608, recipe_name=芥末罗氏虾, category=荤菜, score=0.622139573097229, search_type=vector_enhanced

```text
## 所需食材
1. 小米辣(2个)
2. 生抽(30g)
3. 生粉(10g)
4. 白糖(3g)
5. 盐(3g)
6. 罗氏虾(250g)
7. 胡椒粉(5g)
8. 蒜(2个)
9. 蚝油(15g)
10. 青芥末(20g)
11. 食用油(80ml)
12. 黄油(20g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201001698, chunk_id=201001698_chunk_367, recipe_name=杀猪菜, category=荤菜, score=0.6213563084602356, search_type=vector_enhanced

```text
## 所需食材
1. 八角(1个)
2. 姜粉(5克)
3. 干辣椒(5个)
4. 排骨(400克)
5. 料酒(10克)
6. 枸杞
7. 生抽(10克)
8. 盐(5克)
9. 菜籽油(10克)
10. 葱结(1个)
11. 蒜瓣(5个)
12. 蒜蓉(5克)
13. 血肠(200克)
14. 辣椒油(5克)
15. 酸菜(500克)
16. 香叶(2片)
17. 香油(10克)

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
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 清淡
菜品: 凉拌豆腐
分类: 素菜
难度: 2.0
主要食材: 白糖, 生抽, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 晚餐
菜品: 葱油拌面
分类: 主食
菜系: 沪菜
难度: 2.0
主要食材: 白糖, 小葱, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
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

### pair_order=6
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

### pair_order=7
source: rerank_input

```text
菜品: 韭菜盒子
菜系: 未知
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=8
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

### pair_order=9
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

### pair_order=10
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

### pair_order=11
source: rerank_input

```text
菜品: 蛋包饭
菜系: 日式
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=12
source: rerank_input

```text
菜品: 蛋炒饭
菜系: 未知
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=13
source: rerank_input

```text
菜品: 芥末罗氏虾
菜系: 未知
## 所需食材
1. 小米辣(2个)
2. 生抽(30g)
3. 生粉(10g)
4. 白糖(3g)
5. 盐(3g)
6. 罗氏虾(250g)
7. 胡椒粉(5g)
8. 蒜(2个)
9. 蚝油(15g)
10. 青芥末(20g)
11. 食用油(80ml)
12. 黄油(20g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=14
source: rerank_input

```text
菜品: 杀猪菜
菜系: 东北菜
## 所需食材
1. 八角(1个)
2. 姜粉(5克)
3. 干辣椒(5个)
4. 排骨(400克)
5. 料酒(10克)
6. 枸杞
7. 生抽(10克)
8. 盐(5克)
9. 菜籽油(10克)
10. 葱结(1个)
11. 蒜瓣(5个)
12. 蒜蓉(5克)
13. 血肠(200克)
14. 辣椒油(5克)
15. 酸菜(500克)
16. 香叶(2片)
17. 香油(10克)

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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6339592933654785, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201004215, recipe_name=葱油拌面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 晚餐
菜品: 葱油拌面
分类: 主食
菜系: 沪菜
难度: 2.0
主要食材: 白糖, 小葱, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6668335199356079, search_type=vector_enhanced

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

### result_order=3
source: reranked_results
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6251769661903381, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
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

### result_order=5
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6661337614059448, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_608, recipe_name=芥末罗氏虾, category=荤菜, score=0.622139573097229, search_type=vector_enhanced

```text
## 所需食材
1. 小米辣(2个)
2. 生抽(30g)
3. 生粉(10g)
4. 白糖(3g)
5. 盐(3g)
6. 罗氏虾(250g)
7. 胡椒粉(5g)
8. 蒜(2个)
9. 蚝油(15g)
10. 青芥末(20g)
11. 食用油(80ml)
12. 黄油(20g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201001698, chunk_id=201001698_chunk_367, recipe_name=杀猪菜, category=荤菜, score=0.6213563084602356, search_type=vector_enhanced

```text
## 所需食材
1. 八角(1个)
2. 姜粉(5克)
3. 干辣椒(5个)
4. 排骨(400克)
5. 料酒(10克)
6. 枸杞
7. 生抽(10克)
8. 盐(5克)
9. 菜籽油(10克)
10. 葱结(1个)
11. 蒜瓣(5个)
12. 蒜蓉(5克)
13. 血肠(200克)
14. 辣椒油(5克)
15. 酸菜(500克)
16. 香叶(2片)
17. 香油(10克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201004841, recipe_name=凉拌豆腐, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 清淡
菜品: 凉拌豆腐
分类: 素菜
难度: 2.0
主要食材: 白糖, 生抽, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201002797, chunk_id=201002797_chunk_552, recipe_name=水煮牛肉, category=荤菜, score=0.6267493367195129, search_type=vector_enhanced

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

### result_order=10
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6257911324501038, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(30g)
2. 火腿肠(50g)
3. 牛奶(10ml)
4. 玉米粒(30g)
5. 番茄酱(20ml)
6. 米饭(200g)
7. 胡萝卜(30g)
8. 青豆(30g)
9. 食用油(15ml)
10. 鸡胸肉(50g)
11. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.6391054391860962, search_type=vector_enhanced

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

### result_order=12
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

### result_order=13
source: reranked_results
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6542143821716309, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201005725, recipe_name=鸡蛋羹, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋羹
菜品名称: 鸡蛋羹
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=15
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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6339592933654785, search_type=vector_enhanced

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
source: top_k_final
metadata_summary: node_id=201004215, recipe_name=葱油拌面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 晚餐
菜品: 葱油拌面
分类: 主食
菜系: 沪菜
难度: 2.0
主要食材: 白糖, 小葱, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6668335199356079, search_type=vector_enhanced

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

### result_order=3
source: top_k_final
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6251769661903381, search_type=vector_enhanced

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6339592933654785, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
source: generation_context
metadata_summary: node_id=201004215, recipe_name=葱油拌面, category=主食, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 晚餐
菜品: 葱油拌面
分类: 主食
菜系: 沪菜
难度: 2.0
主要食材: 白糖, 小葱, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201002103, chunk_id=201002103_chunk_436, recipe_name=麻辣香锅, category=荤菜, score=0.6668335199356079, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=3
source: generation_context
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6251769661903381, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 冷饭(500ml)
2. 油(12ml)
3. 火腿(2个)
4. 灯影牛肉丝/午餐肉/腊肠/卤肉
5. 生抽(10ml)
6. 盐(4g)
7. 胡椒粉(8g)
8. 胡萝卜(30g)
9. 香葱(1颗)
10. 鸡蛋(1.5个)
11. 黄瓜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
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

