# Recall Content

audit_id: 20260811_181440_983_2f3feed8
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201001916, recipe_name=糖醋里脊, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 糖醋里脊
菜品名称: 糖醋里脊
分类: 荤菜
菜系: 陕菜,豫菜,浙菜,鲁菜,川菜,淮扬菜,粤菜,闽菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 糖醋排骨
菜品名称: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
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

### result_order=2
source: topic_level
metadata_summary: node_id=201003138, recipe_name=荔枝肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 酸甜口
菜品: 荔枝肉
分类: 荤菜
菜系: 闽菜
难度: 4.0
主要食材: 瘦肉, 凤梨, 芝麻
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6956875920295715, search_type=vector_enhanced

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
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.645543098449707, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6420108675956726, search_type=vector_enhanced

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

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.634846031665802, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.6333889961242676, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6320887207984924, search_type=vector_enhanced

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

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201004446, chunk_id=201004446_chunk_885, recipe_name=微波炉腊肠煲仔饭, category=主食, score=0.6303669214248657, search_type=vector_enhanced

```text
## 所需食材
1. 油(15ml)
2. 生抽(10ml)
3. 盐(5g)
4. 米(200ml)
5. 红萝卜(1个)
6. 腊肠(1根)
7. 青菜
8. 香葱(1颗)
9. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201005511, chunk_id=201005511_chunk_1091, recipe_name=白灼菜心, category=素菜, score=0.6281375885009766, search_type=vector_enhanced

```text
## 所需食材
1. 大蒜(4瓣)
2. 小米辣(2根)
3. 新鲜菜心(250g)
4. 清水(500ml)
5. 生抽(5g)
6. 盐(5g)
7. 糖(5g)
8. 蚝油(5g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201005342, chunk_id=201005342_chunk_1059, recipe_name=包菜炒鸡蛋粉丝, category=素菜, score=0.626029372215271, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(0.5颗)
2. 干辣椒(5根)
3. 生抽(15ml)
4. 盐(2g)
5. 粉丝(1把)
6. 老抽(10ml)
7. 胡萝卜(0.5根)
8. 菜籽油(20ml)
9. 葱(0.5根)
10. 蒜瓣(2片)
11. 蚝油(10ml)
12. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201003818, chunk_id=201003818_chunk_749, recipe_name=腊八粥, category=汤类, score=0.6257506012916565, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10~25克)
2. 去壳核桃(25克)
3. 大米(50克)
4. 小米(50克)
5. 栗子(25克)
6. 桂圆(25克)
7. 糯米(50克)
8. 红枣(25克)
9. 红腰豆(25克)
10. 红豆(25克)
11. 绿豆(25克)
12. 花生(25克)
13. 莲子(25克)
14. 葡萄干(25克)
15. 薏米(50克)
16. 豌豆(25克)
17. 饮用水(1000毫升)
18. 黄豆(25克)
19. 黑米(50克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201001916, recipe_name=糖醋里脊, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 糖醋里脊
菜品名称: 糖醋里脊
分类: 荤菜
菜系: 陕菜,豫菜,浙菜,鲁菜,川菜,淮扬菜,粤菜,闽菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 糖醋排骨
菜品名称: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=2
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

### result_order=3
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

### result_order=4
source: branch_grouped
metadata_summary: node_id=201003138, recipe_name=荔枝肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 酸甜口
菜品: 荔枝肉
分类: 荤菜
菜系: 闽菜
难度: 4.0
主要食材: 瘦肉, 凤梨, 芝麻
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6956875920295715, search_type=vector_enhanced

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
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.645543098449707, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6420108675956726, search_type=vector_enhanced

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

### result_order=8
source: branch_grouped
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.634846031665802, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.6333889961242676, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6320887207984924, search_type=vector_enhanced

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

### result_order=11
source: branch_grouped
metadata_summary: node_id=201004446, chunk_id=201004446_chunk_885, recipe_name=微波炉腊肠煲仔饭, category=主食, score=0.6303669214248657, search_type=vector_enhanced

```text
## 所需食材
1. 油(15ml)
2. 生抽(10ml)
3. 盐(5g)
4. 米(200ml)
5. 红萝卜(1个)
6. 腊肠(1根)
7. 青菜
8. 香葱(1颗)
9. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201005511, chunk_id=201005511_chunk_1091, recipe_name=白灼菜心, category=素菜, score=0.6281375885009766, search_type=vector_enhanced

```text
## 所需食材
1. 大蒜(4瓣)
2. 小米辣(2根)
3. 新鲜菜心(250g)
4. 清水(500ml)
5. 生抽(5g)
6. 盐(5g)
7. 糖(5g)
8. 蚝油(5g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201005342, chunk_id=201005342_chunk_1059, recipe_name=包菜炒鸡蛋粉丝, category=素菜, score=0.626029372215271, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(0.5颗)
2. 干辣椒(5根)
3. 生抽(15ml)
4. 盐(2g)
5. 粉丝(1把)
6. 老抽(10ml)
7. 胡萝卜(0.5根)
8. 菜籽油(20ml)
9. 葱(0.5根)
10. 蒜瓣(2片)
11. 蚝油(10ml)
12. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201003818, chunk_id=201003818_chunk_749, recipe_name=腊八粥, category=汤类, score=0.6257506012916565, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10~25克)
2. 去壳核桃(25克)
3. 大米(50克)
4. 小米(50克)
5. 栗子(25克)
6. 桂圆(25克)
7. 糯米(50克)
8. 红枣(25克)
9. 红腰豆(25克)
10. 红豆(25克)
11. 绿豆(25克)
12. 花生(25克)
13. 莲子(25克)
14. 葡萄干(25克)
15. 薏米(50克)
16. 豌豆(25克)
17. 饮用水(1000毫升)
18. 黄豆(25克)
19. 黑米(50克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201001916, recipe_name=糖醋里脊, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 糖醋里脊
菜品名称: 糖醋里脊
分类: 荤菜
菜系: 陕菜,豫菜,浙菜,鲁菜,川菜,淮扬菜,粤菜,闽菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 糖醋排骨
菜品名称: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=2
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

### result_order=3
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

### result_order=4
source: merged_candidates
metadata_summary: node_id=201003138, recipe_name=荔枝肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 酸甜口
菜品: 荔枝肉
分类: 荤菜
菜系: 闽菜
难度: 4.0
主要食材: 瘦肉, 凤梨, 芝麻
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6956875920295715, search_type=vector_enhanced

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
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.645543098449707, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6420108675956726, search_type=vector_enhanced

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

### result_order=8
source: merged_candidates
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.634846031665802, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.6333889961242676, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6320887207984924, search_type=vector_enhanced

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

### result_order=11
source: merged_candidates
metadata_summary: node_id=201004446, chunk_id=201004446_chunk_885, recipe_name=微波炉腊肠煲仔饭, category=主食, score=0.6303669214248657, search_type=vector_enhanced

```text
## 所需食材
1. 油(15ml)
2. 生抽(10ml)
3. 盐(5g)
4. 米(200ml)
5. 红萝卜(1个)
6. 腊肠(1根)
7. 青菜
8. 香葱(1颗)
9. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201005511, chunk_id=201005511_chunk_1091, recipe_name=白灼菜心, category=素菜, score=0.6281375885009766, search_type=vector_enhanced

```text
## 所需食材
1. 大蒜(4瓣)
2. 小米辣(2根)
3. 新鲜菜心(250g)
4. 清水(500ml)
5. 生抽(5g)
6. 盐(5g)
7. 糖(5g)
8. 蚝油(5g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201005342, chunk_id=201005342_chunk_1059, recipe_name=包菜炒鸡蛋粉丝, category=素菜, score=0.626029372215271, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(0.5颗)
2. 干辣椒(5根)
3. 生抽(15ml)
4. 盐(2g)
5. 粉丝(1把)
6. 老抽(10ml)
7. 胡萝卜(0.5根)
8. 菜籽油(20ml)
9. 葱(0.5根)
10. 蒜瓣(2片)
11. 蚝油(10ml)
12. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201003818, chunk_id=201003818_chunk_749, recipe_name=腊八粥, category=汤类, score=0.6257506012916565, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10~25克)
2. 去壳核桃(25克)
3. 大米(50克)
4. 小米(50克)
5. 栗子(25克)
6. 桂圆(25克)
7. 糯米(50克)
8. 红枣(25克)
9. 红腰豆(25克)
10. 红豆(25克)
11. 绿豆(25克)
12. 花生(25克)
13. 莲子(25克)
14. 葡萄干(25克)
15. 薏米(50克)
16. 豌豆(25克)
17. 饮用水(1000毫升)
18. 黄豆(25克)
19. 黑米(50克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
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
命中关键词: 糖醋里脊
菜品名称: 糖醋里脊
分类: 荤菜
菜系: 陕菜,豫菜,浙菜,鲁菜,川菜,淮扬菜,粤菜,闽菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 糖醋排骨
菜品名称: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### pair_order=2
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

### pair_order=3
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

### pair_order=4
source: rerank_input

```text
命中关键词: 酸甜口
菜品: 荔枝肉
分类: 荤菜
菜系: 闽菜
难度: 4.0
主要食材: 瘦肉, 凤梨, 芝麻
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
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
菜品: 燕麦鸡蛋饼
分类: 早餐
菜系: 未知
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### pair_order=7
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
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### pair_order=10
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

### pair_order=11
source: rerank_input

```text
菜品: 微波炉腊肠煲仔饭
菜系: 未知
## 所需食材
1. 油(15ml)
2. 生抽(10ml)
3. 盐(5g)
4. 米(200ml)
5. 红萝卜(1个)
6. 腊肠(1根)
7. 青菜
8. 香葱(1颗)
9. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=12
source: rerank_input

```text
菜品: 白灼菜心
菜系: 粤菜
## 所需食材
1. 大蒜(4瓣)
2. 小米辣(2根)
3. 新鲜菜心(250g)
4. 清水(500ml)
5. 生抽(5g)
6. 盐(5g)
7. 糖(5g)
8. 蚝油(5g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=13
source: rerank_input

```text
菜品: 包菜炒鸡蛋粉丝
菜系: 未知
## 所需食材
1. 包菜(0.5颗)
2. 干辣椒(5根)
3. 生抽(15ml)
4. 盐(2g)
5. 粉丝(1把)
6. 老抽(10ml)
7. 胡萝卜(0.5根)
8. 菜籽油(20ml)
9. 葱(0.5根)
10. 蒜瓣(2片)
11. 蚝油(10ml)
12. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=14
source: rerank_input

```text
菜品: 腊八粥
菜系: 未知
## 所需食材
1. 冰糖(10~25克)
2. 去壳核桃(25克)
3. 大米(50克)
4. 小米(50克)
5. 栗子(25克)
6. 桂圆(25克)
7. 糯米(50克)
8. 红枣(25克)
9. 红腰豆(25克)
10. 红豆(25克)
11. 绿豆(25克)
12. 花生(25克)
13. 莲子(25克)
14. 葡萄干(25克)
15. 薏米(50克)
16. 豌豆(25克)
17. 饮用水(1000毫升)
18. 黄豆(25克)
19. 黑米(50克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
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
metadata_summary: node_id=201003138, recipe_name=荔枝肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 酸甜口
菜品: 荔枝肉
分类: 荤菜
菜系: 闽菜
难度: 4.0
主要食材: 瘦肉, 凤梨, 芝麻
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=1
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

### result_order=2
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

### result_order=3
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6956875920295715, search_type=vector_enhanced

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

### result_order=4
source: reranked_results
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6320887207984924, search_type=vector_enhanced

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

### result_order=5
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6420108675956726, search_type=vector_enhanced

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

### result_order=6
source: reranked_results
metadata_summary: node_id=201001916, recipe_name=糖醋里脊, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 糖醋里脊
菜品名称: 糖醋里脊
分类: 荤菜
菜系: 陕菜,豫菜,浙菜,鲁菜,川菜,淮扬菜,粤菜,闽菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201004152, chunk_id=201004152_chunk_821, recipe_name=热干面, category=主食, score=0.634846031665802, search_type=vector_enhanced

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

### result_order=8
source: reranked_results
metadata_summary: node_id=201003818, chunk_id=201003818_chunk_749, recipe_name=腊八粥, category=汤类, score=0.6257506012916565, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10~25克)
2. 去壳核桃(25克)
3. 大米(50克)
4. 小米(50克)
5. 栗子(25克)
6. 桂圆(25克)
7. 糯米(50克)
8. 红枣(25克)
9. 红腰豆(25克)
10. 红豆(25克)
11. 绿豆(25克)
12. 花生(25克)
13. 莲子(25克)
14. 葡萄干(25克)
15. 薏米(50克)
16. 豌豆(25克)
17. 饮用水(1000毫升)
18. 黄豆(25克)
19. 黑米(50克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.645543098449707, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(50毫升)
2. 盐(适量克)
3. 纯干燕麦片(50克)
4. 胡椒(适量克)
5. 蔬菜（菠菜等）(50克)
6. 鸡蛋(2个)
7. 黄油(适量克)

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201005342, chunk_id=201005342_chunk_1059, recipe_name=包菜炒鸡蛋粉丝, category=素菜, score=0.626029372215271, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(0.5颗)
2. 干辣椒(5根)
3. 生抽(15ml)
4. 盐(2g)
5. 粉丝(1把)
6. 老抽(10ml)
7. 胡萝卜(0.5根)
8. 菜籽油(20ml)
9. 葱(0.5根)
10. 蒜瓣(2片)
11. 蚝油(10ml)
12. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=11
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

### result_order=12
source: reranked_results
metadata_summary: node_id=201004446, chunk_id=201004446_chunk_885, recipe_name=微波炉腊肠煲仔饭, category=主食, score=0.6303669214248657, search_type=vector_enhanced

```text
## 所需食材
1. 油(15ml)
2. 生抽(10ml)
3. 盐(5g)
4. 米(200ml)
5. 红萝卜(1个)
6. 腊肠(1根)
7. 青菜
8. 香葱(1颗)
9. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=13
source: reranked_results
metadata_summary: node_id=201005511, chunk_id=201005511_chunk_1091, recipe_name=白灼菜心, category=素菜, score=0.6281375885009766, search_type=vector_enhanced

```text
## 所需食材
1. 大蒜(4瓣)
2. 小米辣(2根)
3. 新鲜菜心(250g)
4. 清水(500ml)
5. 生抽(5g)
6. 盐(5g)
7. 糖(5g)
8. 蚝油(5g)
9. 食用油(10g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 糖醋排骨
菜品名称: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=15
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.6333889961242676, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201003138, recipe_name=荔枝肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 酸甜口
菜品: 荔枝肉
分类: 荤菜
菜系: 闽菜
难度: 4.0
主要食材: 瘦肉, 凤梨, 芝麻
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=1
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

### result_order=2
source: top_k_final
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
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6956875920295715, search_type=vector_enhanced

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

### result_order=4
source: top_k_final
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6320887207984924, search_type=vector_enhanced

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

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201003138, recipe_name=荔枝肉, category=荤菜, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 酸甜口
菜品: 荔枝肉
分类: 荤菜
菜系: 闽菜
难度: 4.0
主要食材: 瘦肉, 凤梨, 芝麻
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=1
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

### result_order=2
source: generation_context
metadata_summary: node_id=201002391, recipe_name=奶酪培根通心粉, category=荤菜, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

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
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6956875920295715, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=4
source: generation_context
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6320887207984924, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

