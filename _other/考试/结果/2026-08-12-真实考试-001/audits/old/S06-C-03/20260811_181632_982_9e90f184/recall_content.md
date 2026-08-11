# Recall Content

audit_id: 20260811_181632_982_9e90f184
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201003918, recipe_name=豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆腐
食材名称: 豆腐
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201002255, recipe_name=口水鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 口水鸡
分类: 荤菜
菜系: 川菜
难度: 3.0
主要食材: 蒜, 香菜, 生抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201002511, recipe_name=小炒黄牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 小炒黄牛肉
分类: 荤菜
菜系: 湘菜
难度: 4.0
主要食材: 食用油, 酱油, 牛里脊
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: topic_level
metadata_summary: node_id=201000160, recipe_name=小龙虾, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 小龙虾
分类: 水产
菜系: 川菜
难度: 4.0
主要食材: 桂皮, 郫县豆瓣, 姜
关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=3
source: topic_level
metadata_summary: node_id=201003435, recipe_name=香辣鸡爪煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 香辣鸡爪煲
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 生抽, 鸡爪, 葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_959, recipe_name=凉拌豆腐, category=素菜, score=0.6868160367012024, search_type=vector_enhanced

```text
## 标签
选用北豆腐或老豆腐口感更佳,可省略醋和辣椒油以清淡口味,酱汁比例可调
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6788711547851562, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.677251935005188, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.665088951587677, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=tipdoc_605102de4ff3, chunk_id=tipdoc_605102de4ff3_chunk_1206, recipe_name=去腥, category=烹饪技巧, score=0.6524637937545776, search_type=vector_enhanced

```text
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 去腥 / 添加调料 (TechniqueChunk): category: 烹饪技巧
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6404751539230347, search_type=vector_enhanced

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

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201001965, chunk_id=201001965_chunk_415, recipe_name=蒜苔炒肉末, category=荤菜, score=0.6377876996994019, search_type=vector_enhanced

```text
## 标签
加入食盐前可尝一下咸淡，自行增减盐量,选用五花肉薄片无需腌制即可入味
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.6247969269752502, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1323, recipe_name=凉拌, category=烹饪技巧, score=0.6224728226661682, search_type=vector_enhanced

```text
## 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）
### 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）

用例：面条、米饭、果类、嫩树叶等

* 确认食材安全
* 将食材处理成可食用状态
* 将食材处理成可搅拌状态

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.619762659072876, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆腐切成2 cm见方的小块，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 锅中加入500 ml饮用水，大火烧开。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入豆腐块，煮1-2分钟，以去除豆腥味并使豆腐口感更紧实。
方法: 煮
工具: 锅
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 将煮好的豆腐块捞出，沥干水分，放入碗中，备用。
方法: 捞,沥
工具: 漏勺,碗

### 第5步
步骤: 步骤5
描述: 将小葱洗净，切成葱花，备用。
方法: 洗,切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 将大蒜去皮，切成蒜末，备用。
方法: 去皮,切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 在一个干净的小碗中，加入15 ml生抽，5 ml香油，5 ml醋（可选），2 g白糖（可选）。
方法: 混合
工具: 小碗

### 第8步
步骤: 步骤8
描述: 加入切好的大蒜末。
方法: 混合
工具: 小碗

### 第9步
步骤: 步骤9
描述: 搅拌均匀，使白糖充分溶解，酱汁混合均匀。
方法: 搅拌
工具: 筷子,小碗

### 第10步
步骤: 步骤10
描述: 将制作好的酱汁均匀淋在豆腐块上。
方法: 淋
工具: 碗

### 第11步
步骤: 步骤11
描述: 撒上切好的小葱花。
方法: 撒
工具: 碗

### 第12步
步骤: 步骤12
描述: 根据个人喜好，淋上5 ml辣椒油（可选）。
方法: 淋
工具: 碗

### 第13步
步骤: 步骤13
描述: 用筷子或勺子轻轻拌匀，即可食用。
方法: 拌
工具: 筷子,勺子,碗

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201003918, recipe_name=豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆腐
食材名称: 豆腐
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201002255, recipe_name=口水鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 口水鸡
分类: 荤菜
菜系: 川菜
难度: 3.0
主要食材: 蒜, 香菜, 生抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201002511, recipe_name=小炒黄牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 小炒黄牛肉
分类: 荤菜
菜系: 湘菜
难度: 4.0
主要食材: 食用油, 酱油, 牛里脊
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201000160, recipe_name=小龙虾, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 小龙虾
分类: 水产
菜系: 川菜
难度: 4.0
主要食材: 桂皮, 郫县豆瓣, 姜
关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201003435, recipe_name=香辣鸡爪煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 香辣鸡爪煲
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 生抽, 鸡爪, 葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_959, recipe_name=凉拌豆腐, category=素菜, score=0.6868160367012024, search_type=vector_enhanced

```text
## 标签
选用北豆腐或老豆腐口感更佳,可省略醋和辣椒油以清淡口味,酱汁比例可调
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6788711547851562, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.677251935005188, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.665088951587677, search_type=vector_enhanced

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

### result_order=9
source: branch_grouped
metadata_summary: node_id=tipdoc_605102de4ff3, chunk_id=tipdoc_605102de4ff3_chunk_1206, recipe_name=去腥, category=烹饪技巧, score=0.6524637937545776, search_type=vector_enhanced

```text
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 去腥 / 添加调料 (TechniqueChunk): category: 烹饪技巧
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6404751539230347, search_type=vector_enhanced

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

### result_order=11
source: branch_grouped
metadata_summary: node_id=201001965, chunk_id=201001965_chunk_415, recipe_name=蒜苔炒肉末, category=荤菜, score=0.6377876996994019, search_type=vector_enhanced

```text
## 标签
加入食盐前可尝一下咸淡，自行增减盐量,选用五花肉薄片无需腌制即可入味
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.6247969269752502, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1323, recipe_name=凉拌, category=烹饪技巧, score=0.6224728226661682, search_type=vector_enhanced

```text
## 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）
### 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）

用例：面条、米饭、果类、嫩树叶等

* 确认食材安全
* 将食材处理成可食用状态
* 将食材处理成可搅拌状态

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.619762659072876, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆腐切成2 cm见方的小块，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 锅中加入500 ml饮用水，大火烧开。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入豆腐块，煮1-2分钟，以去除豆腥味并使豆腐口感更紧实。
方法: 煮
工具: 锅
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 将煮好的豆腐块捞出，沥干水分，放入碗中，备用。
方法: 捞,沥
工具: 漏勺,碗

### 第5步
步骤: 步骤5
描述: 将小葱洗净，切成葱花，备用。
方法: 洗,切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 将大蒜去皮，切成蒜末，备用。
方法: 去皮,切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 在一个干净的小碗中，加入15 ml生抽，5 ml香油，5 ml醋（可选），2 g白糖（可选）。
方法: 混合
工具: 小碗

### 第8步
步骤: 步骤8
描述: 加入切好的大蒜末。
方法: 混合
工具: 小碗

### 第9步
步骤: 步骤9
描述: 搅拌均匀，使白糖充分溶解，酱汁混合均匀。
方法: 搅拌
工具: 筷子,小碗

### 第10步
步骤: 步骤10
描述: 将制作好的酱汁均匀淋在豆腐块上。
方法: 淋
工具: 碗

### 第11步
步骤: 步骤11
描述: 撒上切好的小葱花。
方法: 撒
工具: 碗

### 第12步
步骤: 步骤12
描述: 根据个人喜好，淋上5 ml辣椒油（可选）。
方法: 淋
工具: 碗

### 第13步
步骤: 步骤13
描述: 用筷子或勺子轻轻拌匀，即可食用。
方法: 拌
工具: 筷子,勺子,碗

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201003918, recipe_name=豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆腐
食材名称: 豆腐
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201002255, recipe_name=口水鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 口水鸡
分类: 荤菜
菜系: 川菜
难度: 3.0
主要食材: 蒜, 香菜, 生抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201002511, recipe_name=小炒黄牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 小炒黄牛肉
分类: 荤菜
菜系: 湘菜
难度: 4.0
主要食材: 食用油, 酱油, 牛里脊
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201000160, recipe_name=小龙虾, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 小龙虾
分类: 水产
菜系: 川菜
难度: 4.0
主要食材: 桂皮, 郫县豆瓣, 姜
关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201003435, recipe_name=香辣鸡爪煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 香辣鸡爪煲
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 生抽, 鸡爪, 葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.619762659072876, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆腐切成2 cm见方的小块，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 锅中加入500 ml饮用水，大火烧开。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入豆腐块，煮1-2分钟，以去除豆腥味并使豆腐口感更紧实。
方法: 煮
工具: 锅
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 将煮好的豆腐块捞出，沥干水分，放入碗中，备用。
方法: 捞,沥
工具: 漏勺,碗

### 第5步
步骤: 步骤5
描述: 将小葱洗净，切成葱花，备用。
方法: 洗,切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 将大蒜去皮，切成蒜末，备用。
方法: 去皮,切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 在一个干净的小碗中，加入15 ml生抽，5 ml香油，5 ml醋（可选），2 g白糖（可选）。
方法: 混合
工具: 小碗

### 第8步
步骤: 步骤8
描述: 加入切好的大蒜末。
方法: 混合
工具: 小碗

### 第9步
步骤: 步骤9
描述: 搅拌均匀，使白糖充分溶解，酱汁混合均匀。
方法: 搅拌
工具: 筷子,小碗

### 第10步
步骤: 步骤10
描述: 将制作好的酱汁均匀淋在豆腐块上。
方法: 淋
工具: 碗

### 第11步
步骤: 步骤11
描述: 撒上切好的小葱花。
方法: 撒
工具: 碗

### 第12步
步骤: 步骤12
描述: 根据个人喜好，淋上5 ml辣椒油（可选）。
方法: 淋
工具: 碗

### 第13步
步骤: 步骤13
描述: 用筷子或勺子轻轻拌匀，即可食用。
方法: 拌
工具: 筷子,勺子,碗

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6788711547851562, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6404751539230347, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.665088951587677, search_type=vector_enhanced

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

### result_order=9
source: merged_candidates
metadata_summary: node_id=tipdoc_605102de4ff3, chunk_id=tipdoc_605102de4ff3_chunk_1206, recipe_name=去腥, category=烹饪技巧, score=0.6524637937545776, search_type=vector_enhanced

```text
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 去腥 / 添加调料 (TechniqueChunk): category: 烹饪技巧
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201001965, chunk_id=201001965_chunk_415, recipe_name=蒜苔炒肉末, category=荤菜, score=0.6377876996994019, search_type=vector_enhanced

```text
## 标签
加入食盐前可尝一下咸淡，自行增减盐量,选用五花肉薄片无需腌制即可入味
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.6247969269752502, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1323, recipe_name=凉拌, category=烹饪技巧, score=0.6224728226661682, search_type=vector_enhanced

```text
## 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）
### 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）

用例：面条、米饭、果类、嫩树叶等

* 确认食材安全
* 将食材处理成可食用状态
* 将食材处理成可搅拌状态

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_605102de4ff3,tipdoc_fd7f557c37a7, recipe_name=去腥、如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 去腥、如何决策吃什么
关键技巧内容:
## 正文
# 去腥

去腥是做菜过程中的一道工序。

去腥指通过包括但不限于添加调料、焯水等手段去除肉类、水产等食物中腥膻味。

**腥膻味是某些食物的风味来源，过度去腥可能导致食物丧失风味。**

去腥的手段多种多样，在烹饪工程中要灵活选择。
## 手段
## 手段
## 添加调料
### 添加调料

在食材中添加调料是最简单的去腥手段。比如对于大部分使用鸡蛋液的菜肴（[鸡蛋羹](../../dishes/vegetable_dish/鸡蛋羹/鸡蛋羹.md)，[西红柿炒鸡蛋](../../dishes/vegetable_dish/西红柿炒鸡蛋.md)），可以在制作蛋液的过程中加入盐、料酒、食醋等调料来去腥。

烹饪某些肉类时，可以在汤底中加入花椒、八角、香叶、桂皮、小茴香、辣椒等香料来去腥。

成品麻辣火锅底料具有极其浓郁的香味，可以在烹饪时适量添加，足以覆盖绝大多数肉类的腥味。
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。
## 炝锅
### 炝锅

炒菜过程中，可以在过程中使用葱、姜、蒜、干辣椒等香料炝锅。香料中的香味物质在高温的作用下挥发出来，一定程度上能覆盖腥味并且增加成菜的风味。
## 冷水锅焯水
### 冷水锅焯水

某些动物性原料中残留有血液，如：鸡肉、猪蹄、排骨等。残留的血液如果不去除会导致成菜有一定的腥味。

冷水下锅时，残留的血液会分散到水中；随着温度升高，血液中的蛋白质凝固，原本分散在水中的血液形成浮沫飘在水面上。这时只需用勺撇去浮沫即可完成去腥，剩下的清汤可以用作炖煮菜的汤底继续烹饪。
## 注意事项
### 注意事项

- 焯水时往往在锅中加入一些调料如：花椒、八角、料酒、大葱等，进一步强化去腥的力度
- 八角香味浓郁，应适量添加
- 花椒和麻椒体积小而添加量大，添加后可能会残留在锅中甚至残留至成菜，可以使用纱布包裹一个调料包或者使用食品级不锈钢调料盒，方便在成菜前挑出
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 豆腐
食材名称: 豆腐
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 香辣
菜品: 口水鸡
分类: 荤菜
菜系: 川菜
难度: 3.0
主要食材: 蒜, 香菜, 生抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 香辣
菜品: 小炒黄牛肉
分类: 荤菜
菜系: 湘菜
难度: 4.0
主要食材: 食用油, 酱油, 牛里脊
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 香辣
菜品: 小龙虾
分类: 水产
菜系: 川菜
难度: 4.0
主要食材: 桂皮, 郫县豆瓣, 姜
关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### pair_order=4
source: rerank_input

```text
命中关键词: 香辣
菜品: 香辣鸡爪煲
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 生抽, 鸡爪, 葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=5
source: rerank_input

```text
菜品: 凉拌豆腐
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆腐切成2 cm见方的小块，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 锅中加入500 ml饮用水，大火烧开。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入豆腐块，煮1-2分钟，以去除豆腥味并使豆腐口感更紧实。
方法: 煮
工具: 锅
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 将煮好的豆腐块捞出，沥干水分，放入碗中，备用。
方法: 捞,沥
工具: 漏勺,碗

### 第5步
步骤: 步骤5
描述: 将小葱洗净，切成葱花，备用。
方法: 洗,切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 将大蒜去皮，切成蒜末，备用。
方法: 去皮,切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 在一个干净的小碗中，加入15 ml生抽，5 ml香油，5 ml醋（可选），2 g白糖（可选）。
方法: 混合
工具: 小碗

### 第8步
步骤: 步骤8
描述: 加入切好的大蒜末。
方法: 混合
工具: 小碗

### 第9步
步骤: 步骤9
描述: 搅拌均匀，使白糖充分溶解，酱汁混合均匀。
方法: 搅拌
工具: 筷子,小碗

### 第10步
步骤: 步骤10
描述: 将制作好的酱汁均匀淋在豆腐块上。
方法: 淋
工具: 碗

### 第11步
步骤: 步骤11
描述: 撒上切好的小葱花。
方法: 撒
工具: 碗

### 第12步
步骤: 步骤12
描述: 根据个人喜好，淋上5 ml辣椒油（可选）。
方法: 淋
工具: 碗

### 第13步
步骤: 步骤13
描述: 用筷子或勺子轻轻拌匀，即可食用。
方法: 拌
工具: 筷子,勺子,碗

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (Difficult
```

### pair_order=6
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

### pair_order=7
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

### pair_order=8
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

### pair_order=9
source: rerank_input

```text
菜系: 技巧知识
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 去腥 / 添加调料 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=10
source: rerank_input

```text
菜品: 蒜苔炒肉末
菜系: 东北菜
## 标签
加入食盐前可尝一下咸淡，自行增减盐量,选用五花肉薄片无需腌制即可入味
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=11
source: rerank_input

```text
菜品: 麻婆豆腐
菜系: 川菜
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=12
source: rerank_input

```text
菜系: 技巧知识
## 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）
### 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）

用例：面条、米饭、果类、嫩树叶等

* 确认食材安全
* 将食材处理成可食用状态
* 将食材处理成可搅拌状态

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=13
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 去腥、如何决策吃什么
关键技巧内容:
## 正文
# 去腥

去腥是做菜过程中的一道工序。

去腥指通过包括但不限于添加调料、焯水等手段去除肉类、水产等食物中腥膻味。

**腥膻味是某些食物的风味来源，过度去腥可能导致食物丧失风味。**

去腥的手段多种多样，在烹饪工程中要灵活选择。
## 手段
## 手段
## 添加调料
### 添加调料

在食材中添加调料是最简单的去腥手段。比如对于大部分使用鸡蛋液的菜肴（[鸡蛋羹](../../dishes/vegetable_dish/鸡蛋羹/鸡蛋羹.md)，[西红柿炒鸡蛋](../../dishes/vegetable_dish/西红柿炒鸡蛋.md)），可以在制作蛋液的过程中加入盐、料酒、食醋等调料来去腥。

烹饪某些肉类时，可以在汤底中加入花椒、八角、香叶、桂皮、小茴香、辣椒等香料来去腥。

成品麻辣火锅底料具有极其浓郁的香味，可以在烹饪时适量添加，足以覆盖绝大多数肉类的腥味。
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。
## 炝锅
### 炝锅

炒菜过程中，可以在过程中使用葱、姜、蒜、干辣椒等香料炝锅。香料中的香味物质在高温的作用下挥发出来，一定程度上能覆盖腥味并且增加成菜的风味。
## 冷水锅焯水
### 冷水锅焯水

某些动物性原料中残留有血液，如：鸡肉、猪蹄、排骨等。残留的血液如果不去除会导致成菜有一定的腥味。

冷水下锅时，残留的血液会分散到水中；随着温度升高，血液中的蛋白质凝固，原本分散在水中的血液形成浮沫飘在水面上。这时只需用勺撇去浮沫即可完成去腥，剩下的清汤可以用作炖煮菜的汤底继续烹饪。
## 注意事项
### 注意事项

- 焯水时往往在锅中加入一些调料如：花椒、八角、料酒、大葱等，进一步强化去腥的力度
- 八角香味浓郁，应适量添加
- 花椒和麻椒体积小而添加量大，添加后可能会残
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.6247969269752502, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6404751539230347, search_type=vector_enhanced

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
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.665088951587677, search_type=vector_enhanced

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
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6788711547851562, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.619762659072876, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将豆腐切成2 cm见方的小块，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 锅中加入500 ml饮用水，大火烧开。
方法: 煮
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入豆腐块，煮1-2分钟，以去除豆腥味并使豆腐口感更紧实。
方法: 煮
工具: 锅
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 将煮好的豆腐块捞出，沥干水分，放入碗中，备用。
方法: 捞,沥
工具: 漏勺,碗

### 第5步
步骤: 步骤5
描述: 将小葱洗净，切成葱花，备用。
方法: 洗,切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 将大蒜去皮，切成蒜末，备用。
方法: 去皮,切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 在一个干净的小碗中，加入15 ml生抽，5 ml香油，5 ml醋（可选），2 g白糖（可选）。
方法: 混合
工具: 小碗

### 第8步
步骤: 步骤8
描述: 加入切好的大蒜末。
方法: 混合
工具: 小碗

### 第9步
步骤: 步骤9
描述: 搅拌均匀，使白糖充分溶解，酱汁混合均匀。
方法: 搅拌
工具: 筷子,小碗

### 第10步
步骤: 步骤10
描述: 将制作好的酱汁均匀淋在豆腐块上。
方法: 淋
工具: 碗

### 第11步
步骤: 步骤11
描述: 撒上切好的小葱花。
方法: 撒
工具: 碗

### 第12步
步骤: 步骤12
描述: 根据个人喜好，淋上5 ml辣椒油（可选）。
方法: 淋
工具: 碗

### 第13步
步骤: 步骤13
描述: 用筷子或勺子轻轻拌匀，即可食用。
方法: 拌
工具: 筷子,勺子,碗

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_605102de4ff3,tipdoc_fd7f557c37a7, recipe_name=去腥、如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 去腥、如何决策吃什么
关键技巧内容:
## 正文
# 去腥

去腥是做菜过程中的一道工序。

去腥指通过包括但不限于添加调料、焯水等手段去除肉类、水产等食物中腥膻味。

**腥膻味是某些食物的风味来源，过度去腥可能导致食物丧失风味。**

去腥的手段多种多样，在烹饪工程中要灵活选择。
## 手段
## 手段
## 添加调料
### 添加调料

在食材中添加调料是最简单的去腥手段。比如对于大部分使用鸡蛋液的菜肴（[鸡蛋羹](../../dishes/vegetable_dish/鸡蛋羹/鸡蛋羹.md)，[西红柿炒鸡蛋](../../dishes/vegetable_dish/西红柿炒鸡蛋.md)），可以在制作蛋液的过程中加入盐、料酒、食醋等调料来去腥。

烹饪某些肉类时，可以在汤底中加入花椒、八角、香叶、桂皮、小茴香、辣椒等香料来去腥。

成品麻辣火锅底料具有极其浓郁的香味，可以在烹饪时适量添加，足以覆盖绝大多数肉类的腥味。
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。
## 炝锅
### 炝锅

炒菜过程中，可以在过程中使用葱、姜、蒜、干辣椒等香料炝锅。香料中的香味物质在高温的作用下挥发出来，一定程度上能覆盖腥味并且增加成菜的风味。
## 冷水锅焯水
### 冷水锅焯水

某些动物性原料中残留有血液，如：鸡肉、猪蹄、排骨等。残留的血液如果不去除会导致成菜有一定的腥味。

冷水下锅时，残留的血液会分散到水中；随着温度升高，血液中的蛋白质凝固，原本分散在水中的血液形成浮沫飘在水面上。这时只需用勺撇去浮沫即可完成去腥，剩下的清汤可以用作炖煮菜的汤底继续烹饪。
## 注意事项
### 注意事项

- 焯水时往往在锅中加入一些调料如：花椒、八角、料酒、大葱等，进一步强化去腥的力度
- 八角香味浓郁，应适量添加
- 花椒和麻椒体积小而添加量大，添加后可能会残留在锅中甚至残留至成菜，可以使用纱布包裹一个调料包或者使用食品级不锈钢调料盒，方便在成菜前挑出
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201003918, recipe_name=豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豆腐
食材名称: 豆腐
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201002255, recipe_name=口水鸡, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 口水鸡
分类: 荤菜
菜系: 川菜
难度: 3.0
主要食材: 蒜, 香菜, 生抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201001965, chunk_id=201001965_chunk_415, recipe_name=蒜苔炒肉末, category=荤菜, score=0.6377876996994019, search_type=vector_enhanced

```text
## 标签
加入食盐前可尝一下咸淡，自行增减盐量,选用五花肉薄片无需腌制即可入味
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1323, recipe_name=凉拌, category=烹饪技巧, score=0.6224728226661682, search_type=vector_enhanced

```text
## 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）
### 俺寻思这个也成类食材加工（此流程尽可能不选）（选项必选）

用例：面条、米饭、果类、嫩树叶等

* 确认食材安全
* 将食材处理成可食用状态
* 将食材处理成可搅拌状态

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201002511, recipe_name=小炒黄牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 小炒黄牛肉
分类: 荤菜
菜系: 湘菜
难度: 4.0
主要食材: 食用油, 酱油, 牛里脊
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201000160, recipe_name=小龙虾, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 小龙虾
分类: 水产
菜系: 川菜
难度: 4.0
主要食材: 桂皮, 郫县豆瓣, 姜
关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201003435, recipe_name=香辣鸡爪煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 香辣
菜品: 香辣鸡爪煲
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 生抽, 鸡爪, 葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=13
source: reranked_results
metadata_summary: node_id=tipdoc_605102de4ff3, chunk_id=tipdoc_605102de4ff3_chunk_1206, recipe_name=去腥, category=烹饪技巧, score=0.6524637937545776, search_type=vector_enhanced

```text
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 去腥 / 添加调料 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.6247969269752502, search_type=vector_enhanced

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6404751539230347, search_type=vector_enhanced

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
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.665088951587677, search_type=vector_enhanced

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
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6788711547851562, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_605102de4ff3,tipdoc_fd7f557c37a7, recipe_name=去腥、如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 去腥、如何决策吃什么
关键技巧内容:
## 正文
# 去腥

去腥是做菜过程中的一道工序。

去腥指通过包括但不限于添加调料、焯水等手段去除肉类、水产等食物中腥膻味。

**腥膻味是某些食物的风味来源，过度去腥可能导致食物丧失风味。**

去腥的手段多种多样，在烹饪工程中要灵活选择。
## 手段
## 手段
## 添加调料
### 添加调料

在食材中添加调料是最简单的去腥手段。比如对于大部分使用鸡蛋液的菜肴（[鸡蛋羹](../../dishes/vegetable_dish/鸡蛋羹/鸡蛋羹.md)，[西红柿炒鸡蛋](../../dishes/vegetable_dish/西红柿炒鸡蛋.md)），可以在制作蛋液的过程中加入盐、料酒、食醋等调料来去腥。

烹饪某些肉类时，可以在汤底中加入花椒、八角、香叶、桂皮、小茴香、辣椒等香料来去腥。

成品麻辣火锅底料具有极其浓郁的香味，可以在烹饪时适量添加，足以覆盖绝大多数肉类的腥味。
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。
## 炝锅
### 炝锅

炒菜过程中，可以在过程中使用葱、姜、蒜、干辣椒等香料炝锅。香料中的香味物质在高温的作用下挥发出来，一定程度上能覆盖腥味并且增加成菜的风味。
## 冷水锅焯水
### 冷水锅焯水

某些动物性原料中残留有血液，如：鸡肉、猪蹄、排骨等。残留的血液如果不去除会导致成菜有一定的腥味。

冷水下锅时，残留的血液会分散到水中；随着温度升高，血液中的蛋白质凝固，原本分散在水中的血液形成浮沫飘在水面上。这时只需用勺撇去浮沫即可完成去腥，剩下的清汤可以用作炖煮菜的汤底继续烹饪。
## 注意事项
### 注意事项

- 焯水时往往在锅中加入一些调料如：花椒、八角、料酒、大葱等，进一步强化去腥的力度
- 八角香味浓郁，应适量添加
- 花椒和麻椒体积小而添加量大，添加后可能会残留在锅中甚至残留至成菜，可以使用纱布包裹一个调料包或者使用食品级不锈钢调料盒，方便在成菜前挑出
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.6247969269752502, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 五花肉(20g)
2. 内脂豆腐(1盒)
3. 咸鸭蛋(1枚)
4. 大蒜(2瓣)
5. 小米椒(5根)
6. 开水(适量ml)
7. 生姜(2片)
8. 花椒(20颗)
9. 酱油(10g)
10. 食用油(10ml)
11. 食盐(3g)
12. 香辣酱(5g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: generation_context
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.6404751539230347, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.665088951587677, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.6788711547851562, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_820d789ff48e,tipdoc_605102de4ff3,tipdoc_fd7f557c37a7, recipe_name=去腥、如何决策吃什么, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 去腥、如何决策吃什么
关键技巧内容:
## 正文
# 去腥

去腥是做菜过程中的一道工序。

去腥指通过包括但不限于添加调料、焯水等手段去除肉类、水产等食物中腥膻味。

**腥膻味是某些食物的风味来源，过度去腥可能导致食物丧失风味。**

去腥的手段多种多样，在烹饪工程中要灵活选择。
## 手段
## 手段
## 添加调料
### 添加调料

在食材中添加调料是最简单的去腥手段。比如对于大部分使用鸡蛋液的菜肴（[鸡蛋羹](../../dishes/vegetable_dish/鸡蛋羹/鸡蛋羹.md)，[西红柿炒鸡蛋](../../dishes/vegetable_dish/西红柿炒鸡蛋.md)），可以在制作蛋液的过程中加入盐、料酒、食醋等调料来去腥。

烹饪某些肉类时，可以在汤底中加入花椒、八角、香叶、桂皮、小茴香、辣椒等香料来去腥。

成品麻辣火锅底料具有极其浓郁的香味，可以在烹饪时适量添加，足以覆盖绝大多数肉类的腥味。
## 蘸料
### 蘸料

某些食物在烹饪之后仍然腥味严重。可以调配蘸料来在食用时掩盖腥味。

常见的蘸料原料有：食醋、酱油、香油、豆瓣酱、甜面酱、芝麻酱、花生酱、豆腐乳、食盐、大蒜、生姜等。

各种蘸料搭配见仁见智，这里不做举例。
## 炝锅
### 炝锅

炒菜过程中，可以在过程中使用葱、姜、蒜、干辣椒等香料炝锅。香料中的香味物质在高温的作用下挥发出来，一定程度上能覆盖腥味并且增加成菜的风味。
## 冷水锅焯水
### 冷水锅焯水

某些动物性原料中残留有血液，如：鸡肉、猪蹄、排骨等。残留的血液如果不去除会导致成菜有一定的腥味。

冷水下锅时，残留的血液会分散到水中；随着温度升高，血液中的蛋白质凝固，原本分散在水中的血液形成浮沫飘在水面上。这时只需用勺撇去浮沫即可完成去腥，剩下的清汤可以用作炖煮菜的汤底继续烹饪。
## 注意事项
### 注意事项

- 焯水时往往在锅中加入一些调料如：花椒、八角、料酒、大葱等，进一步强化去腥的力度
- 八角香味浓郁，应适量添加
- 花椒和麻椒体积小而添加量大，添加后可能会残留在锅中甚至残留至成菜，可以使用纱布包裹一个调料包或者使用食品级不锈钢调料盒，方便在成菜前挑出
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。
## 计算方法
## 计算方法
```

