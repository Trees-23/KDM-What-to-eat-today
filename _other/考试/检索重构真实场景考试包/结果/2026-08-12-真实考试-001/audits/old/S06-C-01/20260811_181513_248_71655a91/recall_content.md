# Recall Content

audit_id: 20260811_181513_248_71655a91
## Hybrid Retrieval / Entity Branch Raw Results
_no content_

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201004316, recipe_name=酸辣蕨根粉, category=主食,凉菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201002203, recipe_name=凉拌鸡丝, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: topic_level
metadata_summary: node_id=201002415, recipe_name=姜炒鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5970267653465271, search_type=vector_enhanced

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
metadata_summary: node_id=201001916, chunk_id=201001916_chunk_404, recipe_name=糖醋里脊, category=荤菜, score=0.5873424410820007, search_type=vector_enhanced

```text
## 所需食材
1. 料酒(20g)
2. 淀粉(50g)
3. 生抽(10ml)
4. 番茄酱(30ml)
5. 白糖(30g)
6. 白胡椒粉(5g)
7. 蚝油(10g)
8. 醋(10g)
9. 里脊肉(500g)
10. 食盐(10g)
11. 鸡蛋(50g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1152, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5832828283309937, search_type=vector_enhanced

```text
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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_796, recipe_name=汤面, category=主食, score=0.5832004547119141, search_type=vector_enhanced

```text
# 汤面
难度: 2.0星

时间信息: 准备时间: 5-10分钟（切菜、处理肉类）, 烹饪时间: 15-20分钟
份量: 1人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5803565382957458, search_type=vector_enhanced

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

### result_order=5
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.5800769329071045, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.5793645977973938, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1149, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5748326778411865, search_type=vector_enhanced

```text
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1150, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5748326778411865, search_type=vector_enhanced

```text
## 烹饪建议

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5742778778076172, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201004316, recipe_name=酸辣蕨根粉, category=主食,凉菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201002203, recipe_name=凉拌鸡丝, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201002415, recipe_name=姜炒鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5970267653465271, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=201001916, chunk_id=201001916_chunk_404, recipe_name=糖醋里脊, category=荤菜, score=0.5873424410820007, search_type=vector_enhanced

```text
## 所需食材
1. 料酒(20g)
2. 淀粉(50g)
3. 生抽(10ml)
4. 番茄酱(30ml)
5. 白糖(30g)
6. 白胡椒粉(5g)
7. 蚝油(10g)
8. 醋(10g)
9. 里脊肉(500g)
10. 食盐(10g)
11. 鸡蛋(50g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1152, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5832828283309937, search_type=vector_enhanced

```text
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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_796, recipe_name=汤面, category=主食, score=0.5832004547119141, search_type=vector_enhanced

```text
# 汤面
难度: 2.0星

时间信息: 准备时间: 5-10分钟（切菜、处理肉类）, 烹饪时间: 15-20分钟
份量: 1人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5803565382957458, search_type=vector_enhanced

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

### result_order=9
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.5800769329071045, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.5793645977973938, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1149, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5748326778411865, search_type=vector_enhanced

```text
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1150, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5748326778411865, search_type=vector_enhanced

```text
## 烹饪建议

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5742778778076172, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201004316, recipe_name=酸辣蕨根粉, category=主食,凉菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201002203, recipe_name=凉拌鸡丝, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201002415, recipe_name=姜炒鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5970267653465271, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=201001916, chunk_id=201001916_chunk_404, recipe_name=糖醋里脊, category=荤菜, score=0.5873424410820007, search_type=vector_enhanced

```text
## 所需食材
1. 料酒(20g)
2. 淀粉(50g)
3. 生抽(10ml)
4. 番茄酱(30ml)
5. 白糖(30g)
6. 白胡椒粉(5g)
7. 蚝油(10g)
8. 醋(10g)
9. 里脊肉(500g)
10. 食盐(10g)
11. 鸡蛋(50g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1152, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5832828283309937, search_type=vector_enhanced

```text
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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5803565382957458, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.5800769329071045, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.5793645977973938, search_type=vector_enhanced

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

### result_order=10
source: merged_candidates
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5742778778076172, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_0899584efc31,tipdoc_820d789ff48e,tipdoc_fd7f557c37a7, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

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
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

### pair_order=4
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

### pair_order=5
source: rerank_input

```text
菜品: 糖醋里脊
菜系: 陕菜,豫菜,浙菜,鲁菜,川菜,淮扬菜,粤菜,闽菜
## 所需食材
1. 料酒(20g)
2. 淀粉(50g)
3. 生抽(10ml)
4. 番茄酱(30ml)
5. 白糖(30g)
6. 白胡椒粉(5g)
7. 蚝油(10g)
8. 醋(10g)
9. 里脊肉(500g)
10. 食盐(10g)
11. 鸡蛋(50g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=6
source: rerank_input

```text
菜系: 技巧知识
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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
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
菜系: 技巧知识
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### pair_order=9
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

### pair_order=10
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

### pair_order=11
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
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5970267653465271, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5803565382957458, search_type=vector_enhanced

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

### result_order=2
source: reranked_results
metadata_summary: node_id=201001916, chunk_id=201001916_chunk_404, recipe_name=糖醋里脊, category=荤菜, score=0.5873424410820007, search_type=vector_enhanced

```text
## 所需食材
1. 料酒(20g)
2. 淀粉(50g)
3. 生抽(10ml)
4. 番茄酱(30ml)
5. 白糖(30g)
6. 白胡椒粉(5g)
7. 蚝油(10g)
8. 醋(10g)
9. 里脊肉(500g)
10. 食盐(10g)
11. 鸡蛋(50g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1152, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5832828283309937, search_type=vector_enhanced

```text
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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201002415, recipe_name=姜炒鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 姜炒鸡
分类: 荤菜
菜系: 湘菜
难度: 3.0
主要食材: 生姜, 美人辣, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201002203, recipe_name=凉拌鸡丝, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 凉拌鸡丝
分类: 荤菜
难度: 3.0
主要食材: 香醋, 盐, 鸡胸肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201004316, recipe_name=酸辣蕨根粉, category=主食,凉菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 酸辣蕨根粉
分类: 主食,凉菜
菜系: 川菜
难度: 2.0
主要食材: 油泼辣子, 盐, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 凉菜 (Category)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5742778778076172, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_0899584efc31,tipdoc_820d789ff48e,tipdoc_fd7f557c37a7, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

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

### result_order=9
source: reranked_results
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 快手菜
菜品: 咖喱炒蟹
分类: 水产
菜系: 泰国菜
难度: 4.0
主要食材: 青蟹, 咖喱块, 洋葱
关联图谱:
- OUT REQUIRES 青蟹 (Ingredient): category: 蛋白质
- OUT REQUIRES 咖喱块 (Ingredient): category: 调料
- OUT REQUIRES 洋葱 (Ingredient): category: 蔬菜
```

### result_order=10
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.5800769329071045, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=11
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1329, recipe_name=凉拌, category=烹饪技巧, score=0.5793645977973938, search_type=vector_enhanced

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

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5970267653465271, search_type=vector_enhanced

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
source: top_k_final
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5803565382957458, search_type=vector_enhanced

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

### result_order=2
source: top_k_final
metadata_summary: node_id=201001916, chunk_id=201001916_chunk_404, recipe_name=糖醋里脊, category=荤菜, score=0.5873424410820007, search_type=vector_enhanced

```text
## 所需食材
1. 料酒(20g)
2. 淀粉(50g)
3. 生抽(10ml)
4. 番茄酱(30ml)
5. 白糖(30g)
6. 白胡椒粉(5g)
7. 蚝油(10g)
8. 醋(10g)
9. 里脊肉(500g)
10. 食盐(10g)
11. 鸡蛋(50g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1152, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5832828283309937, search_type=vector_enhanced

```text
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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_0899584efc31,tipdoc_820d789ff48e,tipdoc_fd7f557c37a7, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

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
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5970267653465271, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
source: generation_context
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5803565382957458, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=2
source: generation_context
metadata_summary: node_id=201001916, chunk_id=201001916_chunk_404, recipe_name=糖醋里脊, category=荤菜, score=0.5873424410820007, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 料酒(20g)
2. 淀粉(50g)
3. 生抽(10ml)
4. 番茄酱(30ml)
5. 白糖(30g)
6. 白胡椒粉(5g)
7. 蚝油(10g)
8. 醋(10g)
9. 里脊肉(500g)
10. 食盐(10g)
11. 鸡蛋(50g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: generation_context
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1152, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.5832828283309937, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
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
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_0899584efc31,tipdoc_820d789ff48e,tipdoc_fd7f557c37a7, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

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

