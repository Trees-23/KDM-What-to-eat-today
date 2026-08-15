# Recall Content

audit_id: 20260811_182129_493_e28a0f66
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201002295, recipe_name=米饭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 米饭
食材名称: 米饭
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201000127, recipe_name=红烧鲤鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=2
source: topic_level
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: topic_level
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=tipdoc_4ba80da791e4, chunk_id=tipdoc_4ba80da791e4_chunk_1180, recipe_name=蒸（米）/炖（使用电饭煲/高压锅/电压力锅）, category=烹饪技巧, score=0.6775987148284912, search_type=vector_enhanced

```text
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

分类: 烹饪技巧
标签: 什么是压力锅,优点,工作方式,时间,正文,注意事项,流程,煮,蒸,蒸米炖使用电饭煲高压锅电压力锅,蒸（米）/炖（使用电饭煲/高压锅/电压力锅）,高压力锅,高压锅

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=tipdoc_4ba80da791e4, chunk_id=tipdoc_4ba80da791e4_chunk_1182, recipe_name=蒸（米）/炖（使用电饭煲/高压锅/电压力锅）, category=烹饪技巧, score=0.671463131904602, search_type=vector_enhanced

```text
## 正文
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.665152370929718, search_type=vector_enhanced

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
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6648102402687073, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 煮好米饭，通常使用买米赠送的量杯，一杯米240g
方法: 煮
工具: 电饭煲

### 第2步
步骤: 步骤2
描述: 锅中放油30ml
方法: 倒油
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入肉馅，调中火煎至两面微焦
方法: 煎
工具: 锅

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入锅中，不要打散，盖上锅盖
方法: 煎
工具: 锅,锅盖

### 第5步
步骤: 步骤5
描述: 调一个碗汁，碗中放入计算中的对应数量的老抽、生抽、醋、糖、红葱油，搅拌均匀
方法: 搅拌
工具: 碗,筷子

### 第6步
步骤: 步骤6
描述: 打开锅盖，将碗汁倒入锅中，等待三分钟
方法: 焖
工具: 锅
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 关火，将肉蛋盖到米饭上
方法: 装盘
工具: 锅铲

### 第8步
步骤: 步骤8
描述: 安全检查，开始食用盖饭

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.663206934928894, search_type=vector_enhanced

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
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.6607380509376526, search_type=vector_enhanced

```text
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.660103440284729, search_type=vector_enhanced

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

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201003745, chunk_id=201003745_chunk_733, recipe_name=皮蛋瘦肉粥, category=主食, score=0.6595910787582397, search_type=vector_enhanced

```text
## 所需食材
1. 大米(150毫升)
2. 小葱(1棵)
3. 生姜(1拇指块)
4. 生菜(4叶)
5. 瘦肉(100克)
6. 皮蛋(2颗)
7. 盐(2克)
8. 胡椒粉(1克)
9. 蚝油(5毫升)
10. 酱油(5毫升)
11. 食用油(10毫升)
12. 饮用水(1升)
13. 香菜(1棵)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO_CATEGORY 早餐 (Category)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1323, recipe_name=凉拌, category=烹饪技巧, score=0.6587013602256775, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1149, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6474469900131226, search_type=vector_enhanced

```text
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201002295, recipe_name=米饭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 米饭
食材名称: 米饭
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000127, recipe_name=红烧鲤鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=tipdoc_4ba80da791e4, chunk_id=tipdoc_4ba80da791e4_chunk_1180, recipe_name=蒸（米）/炖（使用电饭煲/高压锅/电压力锅）, category=烹饪技巧, score=0.6775987148284912, search_type=vector_enhanced

```text
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

分类: 烹饪技巧
标签: 什么是压力锅,优点,工作方式,时间,正文,注意事项,流程,煮,蒸,蒸米炖使用电饭煲高压锅电压力锅,蒸（米）/炖（使用电饭煲/高压锅/电压力锅）,高压力锅,高压锅

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=tipdoc_4ba80da791e4, chunk_id=tipdoc_4ba80da791e4_chunk_1182, recipe_name=蒸（米）/炖（使用电饭煲/高压锅/电压力锅）, category=烹饪技巧, score=0.671463131904602, search_type=vector_enhanced

```text
## 正文
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.665152370929718, search_type=vector_enhanced

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
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6648102402687073, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 煮好米饭，通常使用买米赠送的量杯，一杯米240g
方法: 煮
工具: 电饭煲

### 第2步
步骤: 步骤2
描述: 锅中放油30ml
方法: 倒油
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入肉馅，调中火煎至两面微焦
方法: 煎
工具: 锅

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入锅中，不要打散，盖上锅盖
方法: 煎
工具: 锅,锅盖

### 第5步
步骤: 步骤5
描述: 调一个碗汁，碗中放入计算中的对应数量的老抽、生抽、醋、糖、红葱油，搅拌均匀
方法: 搅拌
工具: 碗,筷子

### 第6步
步骤: 步骤6
描述: 打开锅盖，将碗汁倒入锅中，等待三分钟
方法: 焖
工具: 锅
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 关火，将肉蛋盖到米饭上
方法: 装盘
工具: 锅铲

### 第8步
步骤: 步骤8
描述: 安全检查，开始食用盖饭

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.663206934928894, search_type=vector_enhanced

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
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.6607380509376526, search_type=vector_enhanced

```text
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.660103440284729, search_type=vector_enhanced

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

### result_order=12
source: branch_grouped
metadata_summary: node_id=201003745, chunk_id=201003745_chunk_733, recipe_name=皮蛋瘦肉粥, category=主食, score=0.6595910787582397, search_type=vector_enhanced

```text
## 所需食材
1. 大米(150毫升)
2. 小葱(1棵)
3. 生姜(1拇指块)
4. 生菜(4叶)
5. 瘦肉(100克)
6. 皮蛋(2颗)
7. 盐(2克)
8. 胡椒粉(1克)
9. 蚝油(5毫升)
10. 酱油(5毫升)
11. 食用油(10毫升)
12. 饮用水(1升)
13. 香菜(1棵)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO_CATEGORY 早餐 (Category)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1323, recipe_name=凉拌, category=烹饪技巧, score=0.6587013602256775, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1149, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6474469900131226, search_type=vector_enhanced

```text
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201002295, recipe_name=米饭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 米饭
食材名称: 米饭
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000127, recipe_name=红烧鲤鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=tipdoc_4ba80da791e4, chunk_id=tipdoc_4ba80da791e4_chunk_1180, recipe_name=蒸（米）/炖（使用电饭煲/高压锅/电压力锅）, category=烹饪技巧, score=0.6775987148284912, search_type=vector_enhanced

```text
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

分类: 烹饪技巧
标签: 什么是压力锅,优点,工作方式,时间,正文,注意事项,流程,煮,蒸,蒸米炖使用电饭煲高压锅电压力锅,蒸（米）/炖（使用电饭煲/高压锅/电压力锅）,高压力锅,高压锅

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.665152370929718, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6648102402687073, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 煮好米饭，通常使用买米赠送的量杯，一杯米240g
方法: 煮
工具: 电饭煲

### 第2步
步骤: 步骤2
描述: 锅中放油30ml
方法: 倒油
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入肉馅，调中火煎至两面微焦
方法: 煎
工具: 锅

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入锅中，不要打散，盖上锅盖
方法: 煎
工具: 锅,锅盖

### 第5步
步骤: 步骤5
描述: 调一个碗汁，碗中放入计算中的对应数量的老抽、生抽、醋、糖、红葱油，搅拌均匀
方法: 搅拌
工具: 碗,筷子

### 第6步
步骤: 步骤6
描述: 打开锅盖，将碗汁倒入锅中，等待三分钟
方法: 焖
工具: 锅
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 关火，将肉蛋盖到米饭上
方法: 装盘
工具: 锅铲

### 第8步
步骤: 步骤8
描述: 安全检查，开始食用盖饭

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.663206934928894, search_type=vector_enhanced

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
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.6607380509376526, search_type=vector_enhanced

```text
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.660103440284729, search_type=vector_enhanced

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

### result_order=11
source: merged_candidates
metadata_summary: node_id=201003745, chunk_id=201003745_chunk_733, recipe_name=皮蛋瘦肉粥, category=主食, score=0.6595910787582397, search_type=vector_enhanced

```text
## 所需食材
1. 大米(150毫升)
2. 小葱(1棵)
3. 生姜(1拇指块)
4. 生菜(4叶)
5. 瘦肉(100克)
6. 皮蛋(2颗)
7. 盐(2克)
8. 胡椒粉(1克)
9. 蚝油(5毫升)
10. 酱油(5毫升)
11. 食用油(10毫升)
12. 饮用水(1升)
13. 香菜(1棵)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO_CATEGORY 早餐 (Category)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1323, recipe_name=凉拌, category=烹饪技巧, score=0.6587013602256775, search_type=vector_enhanced

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

### result_order=13
source: merged_candidates
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1149, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6474469900131226, search_type=vector_enhanced

```text
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_4ba80da791e4,tipdoc_820d789ff48e,tipdoc_fd7f557c37a7,tipdoc_0899584efc31, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

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
命中关键词: 米饭
食材名称: 米饭
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### pair_order=3
source: rerank_input

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### pair_order=5
source: rerank_input

```text
菜系: 技巧知识
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

分类: 烹饪技巧
标签: 什么是压力锅,优点,工作方式,时间,正文,注意事项,流程,煮,蒸,蒸米炖使用电饭煲高压锅电压力锅,蒸（米）/炖（使用电饭煲/高压锅/电压力锅）,高压力锅,高压锅

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=6
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

### pair_order=7
source: rerank_input

```text
菜品: 肉蛋盖饭
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 煮好米饭，通常使用买米赠送的量杯，一杯米240g
方法: 煮
工具: 电饭煲

### 第2步
步骤: 步骤2
描述: 锅中放油30ml
方法: 倒油
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入肉馅，调中火煎至两面微焦
方法: 煎
工具: 锅

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入锅中，不要打散，盖上锅盖
方法: 煎
工具: 锅,锅盖

### 第5步
步骤: 步骤5
描述: 调一个碗汁，碗中放入计算中的对应数量的老抽、生抽、醋、糖、红葱油，搅拌均匀
方法: 搅拌
工具: 碗,筷子

### 第6步
步骤: 步骤6
描述: 打开锅盖，将碗汁倒入锅中，等待三分钟
方法: 焖
工具: 锅
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 关火，将肉蛋盖到米饭上
方法: 装盘
工具: 锅铲

### 第8步
步骤: 步骤8
描述: 安全检查，开始食用盖饭

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
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
菜品: 小炒黄牛肉
菜系: 湘菜
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=10
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

### pair_order=11
source: rerank_input

```text
菜品: 皮蛋瘦肉粥
分类: 主食
菜系: 未知
## 所需食材
1. 大米(150毫升)
2. 小葱(1棵)
3. 生姜(1拇指块)
4. 生菜(4叶)
5. 瘦肉(100克)
6. 皮蛋(2颗)
7. 盐(2克)
8. 胡椒粉(1克)
9. 蚝油(5毫升)
10. 酱油(5毫升)
11. 食用油(10毫升)
12. 饮用水(1升)
13. 香菜(1棵)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO_CATEGORY 早餐 (Category)
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
菜系: 技巧知识
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=14
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
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6648102402687073, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 煮好米饭，通常使用买米赠送的量杯，一杯米240g
方法: 煮
工具: 电饭煲

### 第2步
步骤: 步骤2
描述: 锅中放油30ml
方法: 倒油
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入肉馅，调中火煎至两面微焦
方法: 煎
工具: 锅

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入锅中，不要打散，盖上锅盖
方法: 煎
工具: 锅,锅盖

### 第5步
步骤: 步骤5
描述: 调一个碗汁，碗中放入计算中的对应数量的老抽、生抽、醋、糖、红葱油，搅拌均匀
方法: 搅拌
工具: 碗,筷子

### 第6步
步骤: 步骤6
描述: 打开锅盖，将碗汁倒入锅中，等待三分钟
方法: 焖
工具: 锅
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 关火，将肉蛋盖到米饭上
方法: 装盘
工具: 锅铲

### 第8步
步骤: 步骤8
描述: 安全检查，开始食用盖饭

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201002937, recipe_name=糖醋排骨, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 糖醋排骨
分类: 荤菜
菜系: 苏菜
难度: 4.0
主要食材: 番茄酱, 排骨, 姜片
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201003745, chunk_id=201003745_chunk_733, recipe_name=皮蛋瘦肉粥, category=主食, score=0.6595910787582397, search_type=vector_enhanced

```text
## 所需食材
1. 大米(150毫升)
2. 小葱(1棵)
3. 生姜(1拇指块)
4. 生菜(4叶)
5. 瘦肉(100克)
6. 皮蛋(2颗)
7. 盐(2克)
8. 胡椒粉(1克)
9. 蚝油(5毫升)
10. 酱油(5毫升)
11. 食用油(10毫升)
12. 饮用水(1升)
13. 香菜(1棵)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO_CATEGORY 早餐 (Category)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.663206934928894, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_4ba80da791e4, chunk_id=tipdoc_4ba80da791e4_chunk_1180, recipe_name=蒸（米）/炖（使用电饭煲/高压锅/电压力锅）, category=烹饪技巧, score=0.6775987148284912, search_type=vector_enhanced

```text
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

分类: 烹饪技巧
标签: 什么是压力锅,优点,工作方式,时间,正文,注意事项,流程,煮,蒸,蒸米炖使用电饭煲高压锅电压力锅,蒸（米）/炖（使用电饭煲/高压锅/电压力锅）,高压力锅,高压锅

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.660103440284729, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1323, recipe_name=凉拌, category=烹饪技巧, score=0.6587013602256775, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201000127, recipe_name=红烧鲤鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
难度: 4.0
主要食材: 蒜瓣, 清水, 盐
关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201002295, recipe_name=米饭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 米饭
食材名称: 米饭
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.6607380509376526, search_type=vector_enhanced

```text
## 所需食材
1. 小米椒(30g)
2. 牛里脊(400g)
3. 芹菜(200g)
4. 酱油(6ml)
5. 野山椒(30g)
6. 食用油(15ml)
7. 香菜(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=12
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_4ba80da791e4,tipdoc_820d789ff48e,tipdoc_fd7f557c37a7,tipdoc_0899584efc31, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

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

### result_order=13
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.665152370929718, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=14
source: reranked_results
metadata_summary: node_id=tipdoc_0899584efc31, chunk_id=tipdoc_0899584efc31_chunk_1149, recipe_name=使用空气炸锅, category=烹饪技巧, score=0.6474469900131226, search_type=vector_enhanced

```text
## 烹饪建议
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 使用空气炸锅 / 什么是空气炸锅 (TechniqueChunk): category: 烹饪技巧
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6648102402687073, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 煮好米饭，通常使用买米赠送的量杯，一杯米240g
方法: 煮
工具: 电饭煲

### 第2步
步骤: 步骤2
描述: 锅中放油30ml
方法: 倒油
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入肉馅，调中火煎至两面微焦
方法: 煎
工具: 锅

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入锅中，不要打散，盖上锅盖
方法: 煎
工具: 锅,锅盖

### 第5步
步骤: 步骤5
描述: 调一个碗汁，碗中放入计算中的对应数量的老抽、生抽、醋、糖、红葱油，搅拌均匀
方法: 搅拌
工具: 碗,筷子

### 第6步
步骤: 步骤6
描述: 打开锅盖，将碗汁倒入锅中，等待三分钟
方法: 焖
工具: 锅
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 关火，将肉蛋盖到米饭上
方法: 装盘
工具: 锅铲

### 第8步
步骤: 步骤8
描述: 安全检查，开始食用盖饭

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_4ba80da791e4,tipdoc_820d789ff48e,tipdoc_fd7f557c37a7,tipdoc_0899584efc31, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

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

### result_order=4
source: top_k_final
metadata_summary: node_id=tipdoc_4ba80da791e4, chunk_id=tipdoc_4ba80da791e4_chunk_1180, recipe_name=蒸（米）/炖（使用电饭煲/高压锅/电压力锅）, category=烹饪技巧, score=0.6775987148284912, search_type=vector_enhanced

```text
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

分类: 烹饪技巧
标签: 什么是压力锅,优点,工作方式,时间,正文,注意事项,流程,煮,蒸,蒸米炖使用电饭煲高压锅电压力锅,蒸（米）/炖（使用电饭煲/高压锅/电压力锅）,高压力锅,高压锅

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201002282, recipe_name=台式卤肉饭, category=荤菜, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 炖煮
菜品: 台式卤肉饭
分类: 荤菜
菜系: 台湾菜
难度: 5.0
主要食材: 大蒜, 白胡椒粉, 五香粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6648102402687073, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 煮好米饭，通常使用买米赠送的量杯，一杯米240g
方法: 煮
工具: 电饭煲

### 第2步
步骤: 步骤2
描述: 锅中放油30ml
方法: 倒油
工具: 锅

### 第3步
步骤: 步骤3
描述: 放入肉馅，调中火煎至两面微焦
方法: 煎
工具: 锅

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入锅中，不要打散，盖上锅盖
方法: 煎
工具: 锅,锅盖

### 第5步
步骤: 步骤5
描述: 调一个碗汁，碗中放入计算中的对应数量的老抽、生抽、醋、糖、红葱油，搅拌均匀
方法: 搅拌
工具: 碗,筷子

### 第6步
步骤: 步骤6
描述: 打开锅盖，将碗汁倒入锅中，等待三分钟
方法: 焖
工具: 锅
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 关火，将肉蛋盖到米饭上
方法: 装盘
工具: 锅铲

### 第8步
步骤: 步骤8
描述: 安全检查，开始食用盖饭

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201003196, recipe_name=西红柿土豆炖牛肉, category=荤菜, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 炖煮
菜品: 西红柿土豆炖牛肉
分类: 荤菜
难度: 4.0
主要食材: 油, 黑胡椒粉, 牛肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_4ba80da791e4,tipdoc_820d789ff48e,tipdoc_fd7f557c37a7,tipdoc_0899584efc31, recipe_name=使用空气炸锅, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

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

### result_order=4
source: generation_context
metadata_summary: node_id=tipdoc_4ba80da791e4, chunk_id=tipdoc_4ba80da791e4_chunk_1180, recipe_name=蒸（米）/炖（使用电饭煲/高压锅/电压力锅）, category=烹饪技巧, score=0.6775987148284912, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
# 蒸（米）/炖（使用电饭煲/高压锅/电压力锅）

分类: 烹饪技巧
标签: 什么是压力锅,优点,工作方式,时间,正文,注意事项,流程,煮,蒸,蒸米炖使用电饭煲高压锅电压力锅,蒸（米）/炖（使用电饭煲/高压锅/电压力锅）,高压力锅,高压锅

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 蒸（米）/炖（使用电饭煲/高压锅/电压力锅） / 注意事项 (TechniqueChunk): category: 烹饪技巧
```

