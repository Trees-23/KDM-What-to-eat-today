# Recall Content

audit_id: 20260811_194215_326_cad7fac4
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201000560, recipe_name=牛奶, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛奶
食材名称: 牛奶
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201000646, recipe_name=燕麦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 燕麦
食材名称: 燕麦
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201000644, recipe_name=牛奶燕麦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛奶燕麦
菜品名称: 牛奶燕麦
分类: 早餐
难度: 1.0
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201004040, recipe_name=汤面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 汤面
分类: 主食
难度: 2.0
主要食材: 盐, 香油, 其他蔬菜（青椒番茄胡萝卜等）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201005164, recipe_name=蚝油生菜, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 蚝油生菜
分类: 素菜
菜系: 粤菜
难度: 2.0
主要食材: 大蒜, 清水, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: topic_level
metadata_summary: node_id=201005181, recipe_name=西红柿炒鸡蛋, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 西红柿炒鸡蛋
分类: 素菜
难度: 2.0
主要食材: 西红柿, 食用油, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=3
source: topic_level
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: topic_level
metadata_summary: node_id=201002350, recipe_name=回锅肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 回锅肉
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 小葱, 料酒, 蒜苗
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: topic_level
metadata_summary: node_id=201002555, recipe_name=巴基斯坦牛肉咖喱, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 巴基斯坦牛肉咖喱
分类: 荤菜
菜系: 巴基斯坦菜
难度: 5.0
主要食材: 姜粉, 螺丝椒, 原味酸奶
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=6
source: topic_level
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 枝竹羊腩煲
分类: 荤菜
菜系: 粤菜
难度: 5.0
主要食材: 清水, 砂糖, 香菇
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=7
source: topic_level
metadata_summary: node_id=201001746, recipe_name=水煮肉片, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 水煮肉片
分类: 荤菜
菜系: 川菜
难度: 5.0
主要食材: 芹菜, 生姜, 小米辣干辣椒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.6754708290100098, search_type=vector_enhanced

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

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_124, recipe_name=牛奶燕麦, category=早餐, score=0.6290738582611084, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶倒入早餐杯（冷的即可）
方法: 倒
工具: 早餐杯
时间: 10秒

### 第2步
步骤: 步骤2
描述: 准备好200ml水，如果是直饮水直接加入燕麦，否则请烧开后加入燕麦
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 水沸后2分钟，燕麦煮好
方法: 煮
工具: 锅
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 煮好的燕麦捞出倒入牛奶中（尽量不要将煮燕麦的水也倒入牛奶，影响口感）
方法: 捞
工具: 漏勺,早餐杯
时间: 10秒

### 第5步
步骤: 步骤5
描述: 热锅，锅内放一层底油，油热后煎鸡蛋，每面煎20秒，考虑调底味（3g椒盐，可选）
方法: 煎
工具: 平底锅,锅铲
时间: 40秒

### 第6步
步骤: 步骤6
描述: 关火，装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_123, recipe_name=牛奶燕麦, category=早餐, score=0.6235311031341553, search_type=vector_enhanced

```text
## 所需食材
1. 椒盐(3g)
2. 燕麦(40g)
3. 牛奶(280ml)
4. 鸡蛋(1个)

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201000979, chunk_id=201000979_chunk_206, recipe_name=炸鲜奶, category=甜品, score=0.610257625579834, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(250g)
2. 玉米淀粉(30g)
3. 白糖(30g)
4. 面包糠(100g)
5. 食用油
6. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_122, recipe_name=牛奶燕麦, category=早餐, score=0.5981590747833252, search_type=vector_enhanced

```text
# 牛奶燕麦
难度: 1.0星

时间信息: 准备时间: 1分钟, 烹饪时间: 3分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.5901514887809753, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5852644443511963, search_type=vector_enhanced

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
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_120, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.572340726852417, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶与干燕麦混合搅拌均匀至黏稠状。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋搅拌均匀至颜色单一程度。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 30秒

### 第3步
步骤: 步骤3
描述: 将鸡蛋液倒入燕麦牛奶中继续搅拌至黏稠、均匀。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 30秒

### 第4步
步骤: 步骤4
描述: 平底锅中加入一层黄油并覆盖均匀。
方法: 加热,抹油
工具: 平底锅,锅铲或刷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 下入搅拌好的食材，并摊开至饼状。
方法: 摊平
工具: 平底锅,锅铲
时间: 30秒

### 第6步
步骤: 步骤6
描述: 小火加热两到三分钟。如想要加入蔬菜，可以在加热过程中加入碎菜叶。
方法: 煎
工具: 平底锅,锅铲
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 翻面继续加热两分钟。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 出锅，搭配剩下的牛奶作为早餐。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201000953, chunk_id=201000953_chunk_202, recipe_name=无厨师机蜂蜜面包, category=甜品, score=0.5638816952705383, search_type=vector_enhanced

```text
## 所需食材
1. 水(20g)
2. 牛奶(200g)
3. 白砂糖(70g)
4. 盐(2g)
5. 芝麻
6. 花生油
7. 蛋液
8. 蜂蜜(20g)
9. 酵母(4g)
10. 高筋面粉(400g)
11. 鸡蛋(1个)
12. 黄油(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201003683, chunk_id=201003683_chunk_720, recipe_name=奶油蘑菇汤, category=汤类, score=0.5605655908584595, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(50克)
2. 淡奶油(30毫升)
3. 清水(100毫升)
4. 牛奶(200毫升)
5. 白蘑菇(200克)
6. 盐(2克)
7. 面粉(10克)
8. 黄油(15克)
9. 黑胡椒碎(1克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201000560, recipe_name=牛奶, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛奶
食材名称: 牛奶
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201000646, recipe_name=燕麦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 燕麦
食材名称: 燕麦
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000644, recipe_name=牛奶燕麦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛奶燕麦
菜品名称: 牛奶燕麦
分类: 早餐
难度: 1.0
关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201004040, recipe_name=汤面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 汤面
分类: 主食
难度: 2.0
主要食材: 盐, 香油, 其他蔬菜（青椒番茄胡萝卜等）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201005164, recipe_name=蚝油生菜, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 蚝油生菜
分类: 素菜
菜系: 粤菜
难度: 2.0
主要食材: 大蒜, 清水, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201005181, recipe_name=西红柿炒鸡蛋, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 西红柿炒鸡蛋
分类: 素菜
难度: 2.0
主要食材: 西红柿, 食用油, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201002350, recipe_name=回锅肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 回锅肉
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 小葱, 料酒, 蒜苗
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201002555, recipe_name=巴基斯坦牛肉咖喱, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 巴基斯坦牛肉咖喱
分类: 荤菜
菜系: 巴基斯坦菜
难度: 5.0
主要食材: 姜粉, 螺丝椒, 原味酸奶
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 枝竹羊腩煲
分类: 荤菜
菜系: 粤菜
难度: 5.0
主要食材: 清水, 砂糖, 香菇
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201001746, recipe_name=水煮肉片, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 水煮肉片
分类: 荤菜
菜系: 川菜
难度: 5.0
主要食材: 芹菜, 生姜, 小米辣干辣椒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.6754708290100098, search_type=vector_enhanced

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

### result_order=12
source: branch_grouped
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_124, recipe_name=牛奶燕麦, category=早餐, score=0.6290738582611084, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶倒入早餐杯（冷的即可）
方法: 倒
工具: 早餐杯
时间: 10秒

### 第2步
步骤: 步骤2
描述: 准备好200ml水，如果是直饮水直接加入燕麦，否则请烧开后加入燕麦
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 水沸后2分钟，燕麦煮好
方法: 煮
工具: 锅
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 煮好的燕麦捞出倒入牛奶中（尽量不要将煮燕麦的水也倒入牛奶，影响口感）
方法: 捞
工具: 漏勺,早餐杯
时间: 10秒

### 第5步
步骤: 步骤5
描述: 热锅，锅内放一层底油，油热后煎鸡蛋，每面煎20秒，考虑调底味（3g椒盐，可选）
方法: 煎
工具: 平底锅,锅铲
时间: 40秒

### 第6步
步骤: 步骤6
描述: 关火，装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_123, recipe_name=牛奶燕麦, category=早餐, score=0.6235311031341553, search_type=vector_enhanced

```text
## 所需食材
1. 椒盐(3g)
2. 燕麦(40g)
3. 牛奶(280ml)
4. 鸡蛋(1个)

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201000979, chunk_id=201000979_chunk_206, recipe_name=炸鲜奶, category=甜品, score=0.610257625579834, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(250g)
2. 玉米淀粉(30g)
3. 白糖(30g)
4. 面包糠(100g)
5. 食用油
6. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_122, recipe_name=牛奶燕麦, category=早餐, score=0.5981590747833252, search_type=vector_enhanced

```text
# 牛奶燕麦
难度: 1.0星

时间信息: 准备时间: 1分钟, 烹饪时间: 3分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=16
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.5901514887809753, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=17
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5852644443511963, search_type=vector_enhanced

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

### result_order=18
source: branch_grouped
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_120, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.572340726852417, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶与干燕麦混合搅拌均匀至黏稠状。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋搅拌均匀至颜色单一程度。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 30秒

### 第3步
步骤: 步骤3
描述: 将鸡蛋液倒入燕麦牛奶中继续搅拌至黏稠、均匀。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 30秒

### 第4步
步骤: 步骤4
描述: 平底锅中加入一层黄油并覆盖均匀。
方法: 加热,抹油
工具: 平底锅,锅铲或刷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 下入搅拌好的食材，并摊开至饼状。
方法: 摊平
工具: 平底锅,锅铲
时间: 30秒

### 第6步
步骤: 步骤6
描述: 小火加热两到三分钟。如想要加入蔬菜，可以在加热过程中加入碎菜叶。
方法: 煎
工具: 平底锅,锅铲
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 翻面继续加热两分钟。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 出锅，搭配剩下的牛奶作为早餐。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=19
source: branch_grouped
metadata_summary: node_id=201000953, chunk_id=201000953_chunk_202, recipe_name=无厨师机蜂蜜面包, category=甜品, score=0.5638816952705383, search_type=vector_enhanced

```text
## 所需食材
1. 水(20g)
2. 牛奶(200g)
3. 白砂糖(70g)
4. 盐(2g)
5. 芝麻
6. 花生油
7. 蛋液
8. 蜂蜜(20g)
9. 酵母(4g)
10. 高筋面粉(400g)
11. 鸡蛋(1个)
12. 黄油(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=20
source: branch_grouped
metadata_summary: node_id=201003683, chunk_id=201003683_chunk_720, recipe_name=奶油蘑菇汤, category=汤类, score=0.5605655908584595, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(50克)
2. 淡奶油(30毫升)
3. 清水(100毫升)
4. 牛奶(200毫升)
5. 白蘑菇(200克)
6. 盐(2克)
7. 面粉(10克)
8. 黄油(15克)
9. 黑胡椒碎(1克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201000560, recipe_name=牛奶, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛奶
食材名称: 牛奶
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201000646, recipe_name=燕麦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 燕麦
食材名称: 燕麦
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_124, recipe_name=牛奶燕麦, category=早餐, score=0.6290738582611084, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶倒入早餐杯（冷的即可）
方法: 倒
工具: 早餐杯
时间: 10秒

### 第2步
步骤: 步骤2
描述: 准备好200ml水，如果是直饮水直接加入燕麦，否则请烧开后加入燕麦
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 水沸后2分钟，燕麦煮好
方法: 煮
工具: 锅
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 煮好的燕麦捞出倒入牛奶中（尽量不要将煮燕麦的水也倒入牛奶，影响口感）
方法: 捞
工具: 漏勺,早餐杯
时间: 10秒

### 第5步
步骤: 步骤5
描述: 热锅，锅内放一层底油，油热后煎鸡蛋，每面煎20秒，考虑调底味（3g椒盐，可选）
方法: 煎
工具: 平底锅,锅铲
时间: 40秒

### 第6步
步骤: 步骤6
描述: 关火，装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201004040, recipe_name=汤面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 汤面
分类: 主食
难度: 2.0
主要食材: 盐, 香油, 其他蔬菜（青椒番茄胡萝卜等）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201005164, recipe_name=蚝油生菜, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 蚝油生菜
分类: 素菜
菜系: 粤菜
难度: 2.0
主要食材: 大蒜, 清水, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201005181, recipe_name=西红柿炒鸡蛋, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 西红柿炒鸡蛋
分类: 素菜
难度: 2.0
主要食材: 西红柿, 食用油, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201002350, recipe_name=回锅肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 回锅肉
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 小葱, 料酒, 蒜苗
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201002555, recipe_name=巴基斯坦牛肉咖喱, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 巴基斯坦牛肉咖喱
分类: 荤菜
菜系: 巴基斯坦菜
难度: 5.0
主要食材: 姜粉, 螺丝椒, 原味酸奶
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 枝竹羊腩煲
分类: 荤菜
菜系: 粤菜
难度: 5.0
主要食材: 清水, 砂糖, 香菇
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201001746, recipe_name=水煮肉片, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 水煮肉片
分类: 荤菜
菜系: 川菜
难度: 5.0
主要食材: 芹菜, 生姜, 小米辣干辣椒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_120, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.572340726852417, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶与干燕麦混合搅拌均匀至黏稠状。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋搅拌均匀至颜色单一程度。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 30秒

### 第3步
步骤: 步骤3
描述: 将鸡蛋液倒入燕麦牛奶中继续搅拌至黏稠、均匀。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 30秒

### 第4步
步骤: 步骤4
描述: 平底锅中加入一层黄油并覆盖均匀。
方法: 加热,抹油
工具: 平底锅,锅铲或刷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 下入搅拌好的食材，并摊开至饼状。
方法: 摊平
工具: 平底锅,锅铲
时间: 30秒

### 第6步
步骤: 步骤6
描述: 小火加热两到三分钟。如想要加入蔬菜，可以在加热过程中加入碎菜叶。
方法: 煎
工具: 平底锅,锅铲
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 翻面继续加热两分钟。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 出锅，搭配剩下的牛奶作为早餐。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201000979, chunk_id=201000979_chunk_206, recipe_name=炸鲜奶, category=甜品, score=0.610257625579834, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(250g)
2. 玉米淀粉(30g)
3. 白糖(30g)
4. 面包糠(100g)
5. 食用油
6. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.5901514887809753, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5852644443511963, search_type=vector_enhanced

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

### result_order=15
source: merged_candidates
metadata_summary: node_id=201000953, chunk_id=201000953_chunk_202, recipe_name=无厨师机蜂蜜面包, category=甜品, score=0.5638816952705383, search_type=vector_enhanced

```text
## 所需食材
1. 水(20g)
2. 牛奶(200g)
3. 白砂糖(70g)
4. 盐(2g)
5. 芝麻
6. 花生油
7. 蛋液
8. 蜂蜜(20g)
9. 酵母(4g)
10. 高筋面粉(400g)
11. 鸡蛋(1个)
12. 黄油(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=16
source: merged_candidates
metadata_summary: node_id=201003683, chunk_id=201003683_chunk_720, recipe_name=奶油蘑菇汤, category=汤类, score=0.5605655908584595, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(50克)
2. 淡奶油(30毫升)
3. 清水(100毫升)
4. 牛奶(200毫升)
5. 白蘑菇(200克)
6. 盐(2克)
7. 面粉(10克)
8. 黄油(15克)
9. 黑胡椒碎(1克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7, recipe_name=凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 凉拌
关键技巧内容:
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 牛奶
食材名称: 牛奶
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 燕麦
食材名称: 燕麦
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### pair_order=2
source: rerank_input

```text
菜品: 牛奶燕麦
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶倒入早餐杯（冷的即可）
方法: 倒
工具: 早餐杯
时间: 10秒

### 第2步
步骤: 步骤2
描述: 准备好200ml水，如果是直饮水直接加入燕麦，否则请烧开后加入燕麦
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 水沸后2分钟，燕麦煮好
方法: 煮
工具: 锅
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 煮好的燕麦捞出倒入牛奶中（尽量不要将煮燕麦的水也倒入牛奶，影响口感）
方法: 捞
工具: 漏勺,早餐杯
时间: 10秒

### 第5步
步骤: 步骤5
描述: 热锅，锅内放一层底油，油热后煎鸡蛋，每面煎20秒，考虑调底味（3g椒盐，可选）
方法: 煎
工具: 平底锅,锅铲
时间: 40秒

### 第6步
步骤: 步骤6
描述: 关火，装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### pair_order=3
source: rerank_input

```text
命中关键词: 做法
菜品: 汤面
分类: 主食
难度: 2.0
主要食材: 盐, 香油, 其他蔬菜（青椒番茄胡萝卜等）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 做法
菜品: 蚝油生菜
分类: 素菜
菜系: 粤菜
难度: 2.0
主要食材: 大蒜, 清水, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=5
source: rerank_input

```text
命中关键词: 做法
菜品: 西红柿炒鸡蛋
分类: 素菜
难度: 2.0
主要食材: 西红柿, 食用油, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=6
source: rerank_input

```text
命中关键词: 做法
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=7
source: rerank_input

```text
命中关键词: 做法
菜品: 回锅肉
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 小葱, 料酒, 蒜苗
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=8
source: rerank_input

```text
命中关键词: 做法
菜品: 巴基斯坦牛肉咖喱
分类: 荤菜
菜系: 巴基斯坦菜
难度: 5.0
主要食材: 姜粉, 螺丝椒, 原味酸奶
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### pair_order=9
source: rerank_input

```text
命中关键词: 做法
菜品: 枝竹羊腩煲
分类: 荤菜
菜系: 粤菜
难度: 5.0
主要食材: 清水, 砂糖, 香菇
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### pair_order=10
source: rerank_input

```text
命中关键词: 做法
菜品: 水煮肉片
分类: 荤菜
菜系: 川菜
难度: 5.0
主要食材: 芹菜, 生姜, 小米辣干辣椒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=11
source: rerank_input

```text
菜品: 燕麦鸡蛋饼
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶与干燕麦混合搅拌均匀至黏稠状。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋搅拌均匀至颜色单一程度。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 30秒

### 第3步
步骤: 步骤3
描述: 将鸡蛋液倒入燕麦牛奶中继续搅拌至黏稠、均匀。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 30秒

### 第4步
步骤: 步骤4
描述: 平底锅中加入一层黄油并覆盖均匀。
方法: 加热,抹油
工具: 平底锅,锅铲或刷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 下入搅拌好的食材，并摊开至饼状。
方法: 摊平
工具: 平底锅,锅铲
时间: 30秒

### 第6步
步骤: 步骤6
描述: 小火加热两到三分钟。如想要加入蔬菜，可以在加热过程中加入碎菜叶。
方法: 煎
工具: 平底锅,锅铲
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 翻面继续加热两分钟。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 出锅，搭配剩下的牛奶作为早餐。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### pair_order=12
source: rerank_input

```text
菜品: 炸鲜奶
菜系: 未知
## 所需食材
1. 牛奶(250g)
2. 玉米淀粉(30g)
3. 白糖(30g)
4. 面包糠(100g)
5. 食用油
6. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### pair_order=13
source: rerank_input

```text
菜系: 技巧知识
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=14
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

### pair_order=15
source: rerank_input

```text
菜品: 无厨师机蜂蜜面包
菜系: 未知
## 所需食材
1. 水(20g)
2. 牛奶(200g)
3. 白砂糖(70g)
4. 盐(2g)
5. 芝麻
6. 花生油
7. 蛋液
8. 蜂蜜(20g)
9. 酵母(4g)
10. 高筋面粉(400g)
11. 鸡蛋(1个)
12. 黄油(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### pair_order=16
source: rerank_input

```text
菜品: 奶油蘑菇汤
菜系: 未知
## 所需食材
1. 洋葱(50克)
2. 淡奶油(30毫升)
3. 清水(100毫升)
4. 牛奶(200毫升)
5. 白蘑菇(200克)
6. 盐(2克)
7. 面粉(10克)
8. 黄油(15克)
9. 黑胡椒碎(1克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### pair_order=17
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 凉拌
关键技巧内容:
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_124, recipe_name=牛奶燕麦, category=早餐, score=0.6290738582611084, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶倒入早餐杯（冷的即可）
方法: 倒
工具: 早餐杯
时间: 10秒

### 第2步
步骤: 步骤2
描述: 准备好200ml水，如果是直饮水直接加入燕麦，否则请烧开后加入燕麦
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 水沸后2分钟，燕麦煮好
方法: 煮
工具: 锅
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 煮好的燕麦捞出倒入牛奶中（尽量不要将煮燕麦的水也倒入牛奶，影响口感）
方法: 捞
工具: 漏勺,早餐杯
时间: 10秒

### 第5步
步骤: 步骤5
描述: 热锅，锅内放一层底油，油热后煎鸡蛋，每面煎20秒，考虑调底味（3g椒盐，可选）
方法: 煎
工具: 平底锅,锅铲
时间: 40秒

### 第6步
步骤: 步骤6
描述: 关火，装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_120, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.572340726852417, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶与干燕麦混合搅拌均匀至黏稠状。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋搅拌均匀至颜色单一程度。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 30秒

### 第3步
步骤: 步骤3
描述: 将鸡蛋液倒入燕麦牛奶中继续搅拌至黏稠、均匀。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 30秒

### 第4步
步骤: 步骤4
描述: 平底锅中加入一层黄油并覆盖均匀。
方法: 加热,抹油
工具: 平底锅,锅铲或刷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 下入搅拌好的食材，并摊开至饼状。
方法: 摊平
工具: 平底锅,锅铲
时间: 30秒

### 第6步
步骤: 步骤6
描述: 小火加热两到三分钟。如想要加入蔬菜，可以在加热过程中加入碎菜叶。
方法: 煎
工具: 平底锅,锅铲
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 翻面继续加热两分钟。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 出锅，搭配剩下的牛奶作为早餐。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=2
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.5901514887809753, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201004040, recipe_name=汤面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 汤面
分类: 主食
难度: 2.0
主要食材: 盐, 香油, 其他蔬菜（青椒番茄胡萝卜等）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7, recipe_name=凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 凉拌
关键技巧内容:
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201000646, recipe_name=燕麦, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 燕麦
食材名称: 燕麦
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5852644443511963, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201000979, chunk_id=201000979_chunk_206, recipe_name=炸鲜奶, category=甜品, score=0.610257625579834, search_type=vector_enhanced

```text
## 所需食材
1. 牛奶(250g)
2. 玉米淀粉(30g)
3. 白糖(30g)
4. 面包糠(100g)
5. 食用油
6. 鸡蛋(2个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201000953, chunk_id=201000953_chunk_202, recipe_name=无厨师机蜂蜜面包, category=甜品, score=0.5638816952705383, search_type=vector_enhanced

```text
## 所需食材
1. 水(20g)
2. 牛奶(200g)
3. 白砂糖(70g)
4. 盐(2g)
5. 芝麻
6. 花生油
7. 蛋液
8. 蜂蜜(20g)
9. 酵母(4g)
10. 高筋面粉(400g)
11. 鸡蛋(1个)
12. 黄油(30g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201000560, recipe_name=牛奶, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 牛奶
食材名称: 牛奶
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201003683, chunk_id=201003683_chunk_720, recipe_name=奶油蘑菇汤, category=汤类, score=0.5605655908584595, search_type=vector_enhanced

```text
## 所需食材
1. 洋葱(50克)
2. 淡奶油(30毫升)
3. 清水(100毫升)
4. 牛奶(200毫升)
5. 白蘑菇(200克)
6. 盐(2克)
7. 面粉(10克)
8. 黄油(15克)
9. 黑胡椒碎(1克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201005164, recipe_name=蚝油生菜, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 蚝油生菜
分类: 素菜
菜系: 粤菜
难度: 2.0
主要食材: 大蒜, 清水, 食用油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201001746, recipe_name=水煮肉片, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 水煮肉片
分类: 荤菜
菜系: 川菜
难度: 5.0
主要食材: 芹菜, 生姜, 小米辣干辣椒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=13
source: reranked_results
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201005181, recipe_name=西红柿炒鸡蛋, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 西红柿炒鸡蛋
分类: 素菜
难度: 2.0
主要食材: 西红柿, 食用油, 糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=15
source: reranked_results
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 枝竹羊腩煲
分类: 荤菜
菜系: 粤菜
难度: 5.0
主要食材: 清水, 砂糖, 香菇
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=16
source: reranked_results
metadata_summary: node_id=201002350, recipe_name=回锅肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 回锅肉
分类: 荤菜
菜系: 川菜
难度: 4.0
主要食材: 小葱, 料酒, 蒜苗
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=17
source: reranked_results
metadata_summary: node_id=201002555, recipe_name=巴基斯坦牛肉咖喱, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 巴基斯坦牛肉咖喱
分类: 荤菜
菜系: 巴基斯坦菜
难度: 5.0
主要食材: 姜粉, 螺丝椒, 原味酸奶
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_124, recipe_name=牛奶燕麦, category=早餐, score=0.6290738582611084, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶倒入早餐杯（冷的即可）
方法: 倒
工具: 早餐杯
时间: 10秒

### 第2步
步骤: 步骤2
描述: 准备好200ml水，如果是直饮水直接加入燕麦，否则请烧开后加入燕麦
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 水沸后2分钟，燕麦煮好
方法: 煮
工具: 锅
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 煮好的燕麦捞出倒入牛奶中（尽量不要将煮燕麦的水也倒入牛奶，影响口感）
方法: 捞
工具: 漏勺,早餐杯
时间: 10秒

### 第5步
步骤: 步骤5
描述: 热锅，锅内放一层底油，油热后煎鸡蛋，每面煎20秒，考虑调底味（3g椒盐，可选）
方法: 煎
工具: 平底锅,锅铲
时间: 40秒

### 第6步
步骤: 步骤6
描述: 关火，装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_120, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.572340726852417, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶与干燕麦混合搅拌均匀至黏稠状。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋搅拌均匀至颜色单一程度。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 30秒

### 第3步
步骤: 步骤3
描述: 将鸡蛋液倒入燕麦牛奶中继续搅拌至黏稠、均匀。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 30秒

### 第4步
步骤: 步骤4
描述: 平底锅中加入一层黄油并覆盖均匀。
方法: 加热,抹油
工具: 平底锅,锅铲或刷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 下入搅拌好的食材，并摊开至饼状。
方法: 摊平
工具: 平底锅,锅铲
时间: 30秒

### 第6步
步骤: 步骤6
描述: 小火加热两到三分钟。如想要加入蔬菜，可以在加热过程中加入碎菜叶。
方法: 煎
工具: 平底锅,锅铲
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 翻面继续加热两分钟。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 出锅，搭配剩下的牛奶作为早餐。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=2
source: top_k_final
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.5901514887809753, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201004040, recipe_name=汤面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 做法
菜品: 汤面
分类: 主食
难度: 2.0
主要食材: 盐, 香油, 其他蔬菜（青椒番茄胡萝卜等）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7, recipe_name=凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 凉拌
关键技巧内容:
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201000644, chunk_id=201000644_chunk_124, recipe_name=牛奶燕麦, category=早餐, score=0.6290738582611084, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶倒入早餐杯（冷的即可）
方法: 倒
工具: 早餐杯
时间: 10秒

### 第2步
步骤: 步骤2
描述: 准备好200ml水，如果是直饮水直接加入燕麦，否则请烧开后加入燕麦
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 水沸后2分钟，燕麦煮好
方法: 煮
工具: 锅
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 煮好的燕麦捞出倒入牛奶中（尽量不要将煮燕麦的水也倒入牛奶，影响口感）
方法: 捞
工具: 漏勺,早餐杯
时间: 10秒

### 第5步
步骤: 步骤5
描述: 热锅，锅内放一层底油，油热后煎鸡蛋，每面煎20秒，考虑调底味（3g椒盐，可选）
方法: 煎
工具: 平底锅,锅铲
时间: 40秒

### 第6步
步骤: 步骤6
描述: 关火，装盘
方法: 装盘
工具: 盘子
时间: 5秒

关联图谱:
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 燕麦 (Ingredient): category: 淀粉类
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
```

### result_order=1
source: generation_context
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_120, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.572340726852417, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将牛奶与干燕麦混合搅拌均匀至黏稠状。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋搅拌均匀至颜色单一程度。
方法: 搅拌
工具: 碗,筷子或打蛋器
时间: 30秒

### 第3步
步骤: 步骤3
描述: 将鸡蛋液倒入燕麦牛奶中继续搅拌至黏稠、均匀。
方法: 搅拌
工具: 碗,筷子或勺子
时间: 30秒

### 第4步
步骤: 步骤4
描述: 平底锅中加入一层黄油并覆盖均匀。
方法: 加热,抹油
工具: 平底锅,锅铲或刷子
时间: 30秒

### 第5步
步骤: 步骤5
描述: 下入搅拌好的食材，并摊开至饼状。
方法: 摊平
工具: 平底锅,锅铲
时间: 30秒

### 第6步
步骤: 步骤6
描述: 小火加热两到三分钟。如想要加入蔬菜，可以在加热过程中加入碎菜叶。
方法: 煎
工具: 平底锅,锅铲
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 翻面继续加热两分钟。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 出锅，搭配剩下的牛奶作为早餐。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=2
source: generation_context
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.5901514887809753, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: generation_context
metadata_summary: node_id=201004040, recipe_name=汤面, category=主食, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 做法
菜品: 汤面
分类: 主食
难度: 2.0
主要食材: 盐, 香油, 其他蔬菜（青椒番茄胡萝卜等）
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7, recipe_name=凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 凉拌
关键技巧内容:
## 正文
# 凉拌
## 凉拌是什么
## 凉拌是什么

凉拌是一种将主食材与辅料通过搅拌混合以成菜的方式
## 凉拌的形态
### 凉拌的形态

凉拌可做成食材与辅料在空间上交混的形态
凉拌可做成食材与辅料在空间上分立的形态，此时辅料被称为蘸料
## 为什么凉拌
### 为什么凉拌

* 部分凉拌成菜时不需要热源
* 部分凉拌能减少洗锅的流程（不洗或仅过水即可）
* 凉拌能保留食材状态，此点特别展现在蔬菜、生肉上
## 凉拌的目的
### 凉拌的目的

* 凉拌的目的在于对无味或味淡食材添加味道，例如鸡肋
## 凉拌能放什么
### 凉拌能放什么

包括但不限于：

* 主食材
* 辅料
* 腌制酱料
* 调味料
## 注意事项
### 注意事项

* 凉拌时应该注意食材安全，在不确认食材是否安全时，请勿凉拌对应食材，在确认食材不安全时不应凉拌对应食材
* 凉拌应尽可能加大主食菜的接触面积，故凉拌时推荐刀花、切片、拍碎甚至搅碎
* 凉拌菜对肠胃提出了基本要求，请在确认不会喷射或存有喷射时间时采用凉拌
* 文件撰写时处于新冠疫情状态下，建议将所有食材均在 100 摄氏度以上的环境中加热 15 秒以上以图心理安慰，若想求得安全请尽量避免凉拌
## 器具
## 器具

可以使用任何容器，从瓷缸到食品级塑料袋均可
## 注意事项
### 注意事项

* 为方便搅拌时食材不溅出，使用容积在所有食材两倍以上的硬质容器较为合适
* 为保证食品安全，在塑料袋或塑料碗中腌制后请尽快将食材移至瓷容器或金属质容器中
* 为保证食品安全，请在洁净的砧板上处理生食食材与辅料
```

