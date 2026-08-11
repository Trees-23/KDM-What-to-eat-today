# Recall Content

audit_id: 20260811_194328_532_5e5f67dd
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201003844, recipe_name=西红柿鸡蛋汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿鸡蛋汤
菜品名称: 西红柿鸡蛋汤
分类: 汤类
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

## Hybrid Retrieval / Topic Branch Raw Results
_no content_

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6888076066970825, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_752, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6835126876831055, search_type=vector_enhanced

```text
# 西红柿鸡蛋汤
难度: 2.0星

时间信息: 准备时间: 约5分钟, 烹饪时间: 约5分钟
份量: 1人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1123, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.6585375070571899, search_type=vector_enhanced

```text
## 所需食材
1. 西红柿(100g)
2. 西葫芦(500g)
3. 食用油(10-20ml)
4. 食用盐(6g)
5. 鸡蛋(3个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6490994095802307, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6471187472343445, search_type=vector_enhanced

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
metadata_summary: node_id=201005653, chunk_id=201005653_chunk_1120, recipe_name=西红柿豆腐汤羹, category=素菜, score=0.6446433067321777, search_type=vector_enhanced

```text
## 所需食材
1. 姜(1片)
2. 开水(350ml)
3. 淀粉(5g)
4. 盐(2g)
5. 西红柿(1个)
6. 豆腐(100g)
7. 食用油(5ml)
8. 香葱(0.5根)
9. 鸡精(2g)
10. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_728, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.6352615356445312, search_type=vector_enhanced

```text
# 番茄牛肉蛋花汤
难度: 3.0星

时间信息: 准备时间: 20-25分钟（含腌制15-20分钟）, 烹饪时间: 约10分钟
份量: 按人数计算

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6339448094367981, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6331303119659424, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6251152753829956, search_type=vector_enhanced

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
metadata_summary: node_id=201003844, recipe_name=西红柿鸡蛋汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿鸡蛋汤
菜品名称: 西红柿鸡蛋汤
分类: 汤类
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6888076066970825, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_752, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6835126876831055, search_type=vector_enhanced

```text
# 西红柿鸡蛋汤
难度: 2.0星

时间信息: 准备时间: 约5分钟, 烹饪时间: 约5分钟
份量: 1人份

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1123, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.6585375070571899, search_type=vector_enhanced

```text
## 所需食材
1. 西红柿(100g)
2. 西葫芦(500g)
3. 食用油(10-20ml)
4. 食用盐(6g)
5. 鸡蛋(3个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6490994095802307, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6471187472343445, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=201005653, chunk_id=201005653_chunk_1120, recipe_name=西红柿豆腐汤羹, category=素菜, score=0.6446433067321777, search_type=vector_enhanced

```text
## 所需食材
1. 姜(1片)
2. 开水(350ml)
3. 淀粉(5g)
4. 盐(2g)
5. 西红柿(1个)
6. 豆腐(100g)
7. 食用油(5ml)
8. 香葱(0.5根)
9. 鸡精(2g)
10. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_728, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.6352615356445312, search_type=vector_enhanced

```text
# 番茄牛肉蛋花汤
难度: 3.0星

时间信息: 准备时间: 20-25分钟（含腌制15-20分钟）, 烹饪时间: 约10分钟
份量: 按人数计算

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6339448094367981, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6331303119659424, search_type=vector_enhanced

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

### result_order=12
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6251152753829956, search_type=vector_enhanced

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
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6331303119659424, search_type=vector_enhanced

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

### result_order=1
source: merged_candidates
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6490994095802307, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1123, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.6585375070571899, search_type=vector_enhanced

```text
## 所需食材
1. 西红柿(100g)
2. 西葫芦(500g)
3. 食用油(10-20ml)
4. 食用盐(6g)
5. 鸡蛋(3个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6471187472343445, search_type=vector_enhanced

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
metadata_summary: node_id=201005653, chunk_id=201005653_chunk_1120, recipe_name=西红柿豆腐汤羹, category=素菜, score=0.6446433067321777, search_type=vector_enhanced

```text
## 所需食材
1. 姜(1片)
2. 开水(350ml)
3. 淀粉(5g)
4. 盐(2g)
5. 西红柿(1个)
6. 豆腐(100g)
7. 食用油(5ml)
8. 香葱(0.5根)
9. 鸡精(2g)
10. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_728, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.6352615356445312, search_type=vector_enhanced

```text
# 番茄牛肉蛋花汤
难度: 3.0星

时间信息: 准备时间: 20-25分钟（含腌制15-20分钟）, 烹饪时间: 约10分钟
份量: 按人数计算

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6339448094367981, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6251152753829956, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
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

### pair_order=1
source: rerank_input

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### pair_order=3
source: rerank_input

```text
菜品: 西红柿炒鸡蛋
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=4
source: rerank_input

```text
菜品: 西葫芦炒鸡蛋
菜系: 未知
## 所需食材
1. 西红柿(100g)
2. 西葫芦(500g)
3. 食用油(10-20ml)
4. 食用盐(6g)
5. 鸡蛋(3个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
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
菜品: 西红柿豆腐汤羹
菜系: 未知
## 所需食材
1. 姜(1片)
2. 开水(350ml)
3. 淀粉(5g)
4. 盐(2g)
5. 西红柿(1个)
6. 豆腐(100g)
7. 食用油(5ml)
8. 香葱(0.5根)
9. 鸡精(2g)
10. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=7
source: rerank_input

```text
菜系: 未知
# 番茄牛肉蛋花汤
难度: 3.0星

时间信息: 准备时间: 20-25分钟（含腌制15-20分钟）, 烹饪时间: 约10分钟
份量: 按人数计算

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### pair_order=8
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

### pair_order=9
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

### pair_order=10
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
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6331303119659424, search_type=vector_enhanced

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

### result_order=1
source: reranked_results
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6490994095802307, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6471187472343445, search_type=vector_enhanced

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
metadata_summary: node_id=201005653, chunk_id=201005653_chunk_1120, recipe_name=西红柿豆腐汤羹, category=素菜, score=0.6446433067321777, search_type=vector_enhanced

```text
## 所需食材
1. 姜(1片)
2. 开水(350ml)
3. 淀粉(5g)
4. 盐(2g)
5. 西红柿(1个)
6. 豆腐(100g)
7. 食用油(5ml)
8. 香葱(0.5根)
9. 鸡精(2g)
10. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_728, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.6352615356445312, search_type=vector_enhanced

```text
# 番茄牛肉蛋花汤
难度: 3.0星

时间信息: 准备时间: 20-25分钟（含腌制15-20分钟）, 烹饪时间: 约10分钟
份量: 按人数计算

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1123, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.6585375070571899, search_type=vector_enhanced

```text
## 所需食材
1. 西红柿(100g)
2. 西葫芦(500g)
3. 食用油(10-20ml)
4. 食用盐(6g)
5. 鸡蛋(3个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6251152753829956, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
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

### result_order=8
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.6339448094367981, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201000006, recipe_name=鸡蛋, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6331303119659424, search_type=vector_enhanced

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

### result_order=1
source: top_k_final
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6490994095802307, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6471187472343445, search_type=vector_enhanced

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
metadata_summary: node_id=201005653, chunk_id=201005653_chunk_1120, recipe_name=西红柿豆腐汤羹, category=素菜, score=0.6446433067321777, search_type=vector_enhanced

```text
## 所需食材
1. 姜(1片)
2. 开水(350ml)
3. 淀粉(5g)
4. 盐(2g)
5. 西红柿(1个)
6. 豆腐(100g)
7. 食用油(5ml)
8. 香葱(0.5根)
9. 鸡精(2g)
10. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
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
metadata_summary: node_id=201003844, chunk_id=201003844_chunk_753, recipe_name=西红柿鸡蛋汤, category=汤类, score=0.6331303119659424, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=1
source: generation_context
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6490994095802307, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，可选：用开水烫表皮后放入冷水剥去外皮，去蒂后切成边长不超过4cm的小块
方法: 切,烫,剥
工具: 刀,案板,锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 将鸡蛋打入碗中，加入1g盐搅匀，可选加1ml醋去腥增蓬松，制成鸡蛋液
方法: 搅拌
工具: 碗,筷子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 热锅，倒入食用油，油热后倒入鸡蛋液，翻炒至鸡蛋结为固体且微微发黄，制成半熟鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 关火，将半熟鸡蛋盛盘，重新开火（不洗锅）
方法: 盛盘
工具: 锅铲,盘子
时间: 10秒

### 第5步
步骤: 步骤5
描述: 加入西红柿块，锅铲拍打并翻炒20秒或至西红柿软烂
方法: 炒
工具: 锅铲
时间: 20秒

### 第6步
步骤: 步骤6
描述: 加入半熟鸡蛋，翻炒均匀；可选加入10ml番茄酱和50ml清水增加汤汁，也可加入其他熟肉
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入剩余盐、可选的糖和葱花，翻炒均匀后关火盛盘
方法: 炒,盛盘
工具: 锅铲,盘子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6471187472343445, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
metadata_summary: node_id=201005653, chunk_id=201005653_chunk_1120, recipe_name=西红柿豆腐汤羹, category=素菜, score=0.6446433067321777, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 姜(1片)
2. 开水(350ml)
3. 淀粉(5g)
4. 盐(2g)
5. 西红柿(1个)
6. 豆腐(100g)
7. 食用油(5ml)
8. 香葱(0.5根)
9. 鸡精(2g)
10. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
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

