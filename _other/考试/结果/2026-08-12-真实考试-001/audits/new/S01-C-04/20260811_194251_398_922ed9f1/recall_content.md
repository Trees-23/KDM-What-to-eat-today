# Recall Content

audit_id: 20260811_194251_398_922ed9f1
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201000730, recipe_name=鸡蛋三明治, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋三明治
菜品名称: 鸡蛋三明治
分类: 早餐
难度: 2.0
关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
```

### result_order=1
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
metadata_summary: node_id=201000730, chunk_id=201000730_chunk_145, recipe_name=鸡蛋三明治, category=早餐, score=0.676352322101593, search_type=vector_enhanced

```text
# 鸡蛋三明治
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 5分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 培根 (Ingredient): category: 蛋白质
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6221157908439636, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1170, recipe_name=炒/煎, category=烹饪技巧, score=0.6197894811630249, search_type=vector_enhanced

```text
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201005709, chunk_id=201005709_chunk_1131, recipe_name=蒸箱鸡蛋羹, category=素菜, score=0.601850688457489, search_type=vector_enhanced

```text
## 所需食材
1. 生抽(6ml)
2. 纯净水(1.0-1.5倍鸡蛋体积ml)
3. 食用油(5ml)
4. 食用盐(1g)
5. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6004815697669983, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201005272, chunk_id=201005272_chunk_1045, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, score=0.5937576293945312, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.5936087369918823, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.589226484298706, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5826243758201599, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201004172, chunk_id=201004172_chunk_827, recipe_name=煮泡面加蛋, category=主食, score=0.5786027312278748, search_type=vector_enhanced

```text
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201000730, recipe_name=鸡蛋三明治, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡蛋三明治
菜品名称: 鸡蛋三明治
分类: 早餐
难度: 2.0
关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
```

### result_order=1
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

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000730, chunk_id=201000730_chunk_145, recipe_name=鸡蛋三明治, category=早餐, score=0.676352322101593, search_type=vector_enhanced

```text
# 鸡蛋三明治
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 5分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 培根 (Ingredient): category: 蛋白质
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6221157908439636, search_type=vector_enhanced

```text
## 注意事项
#### 注意事项

* 辅料的种类，加工，方法极为宽泛，请不要局限您的思维，但请小心求证，适度适量，谨记安全

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 凉拌 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1170, recipe_name=炒/煎, category=烹饪技巧, score=0.6197894811630249, search_type=vector_enhanced

```text
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201005709, chunk_id=201005709_chunk_1131, recipe_name=蒸箱鸡蛋羹, category=素菜, score=0.601850688457489, search_type=vector_enhanced

```text
## 所需食材
1. 生抽(6ml)
2. 纯净水(1.0-1.5倍鸡蛋体积ml)
3. 食用油(5ml)
4. 食用盐(1g)
5. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6004815697669983, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201005272, chunk_id=201005272_chunk_1045, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, score=0.5937576293945312, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.5936087369918823, search_type=vector_enhanced

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

### result_order=9
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.589226484298706, search_type=vector_enhanced

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
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5826243758201599, search_type=vector_enhanced

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
metadata_summary: node_id=201004172, chunk_id=201004172_chunk_827, recipe_name=煮泡面加蛋, category=主食, score=0.5786027312278748, search_type=vector_enhanced

```text
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201000730, chunk_id=201000730_chunk_145, recipe_name=鸡蛋三明治, category=早餐, score=0.676352322101593, search_type=vector_enhanced

```text
# 鸡蛋三明治
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 5分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 培根 (Ingredient): category: 蛋白质
```

### result_order=1
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

### result_order=2
source: merged_candidates
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6221157908439636, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1170, recipe_name=炒/煎, category=烹饪技巧, score=0.6197894811630249, search_type=vector_enhanced

```text
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201005709, chunk_id=201005709_chunk_1131, recipe_name=蒸箱鸡蛋羹, category=素菜, score=0.601850688457489, search_type=vector_enhanced

```text
## 所需食材
1. 生抽(6ml)
2. 纯净水(1.0-1.5倍鸡蛋体积ml)
3. 食用油(5ml)
4. 食用盐(1g)
5. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6004815697669983, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201005272, chunk_id=201005272_chunk_1045, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, score=0.5937576293945312, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.5936087369918823, search_type=vector_enhanced

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

### result_order=8
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.589226484298706, search_type=vector_enhanced

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
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5826243758201599, search_type=vector_enhanced

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

### result_order=10
source: merged_candidates
metadata_summary: node_id=201004172, chunk_id=201004172_chunk_827, recipe_name=煮泡面加蛋, category=主食, score=0.5786027312278748, search_type=vector_enhanced

```text
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7,tipdoc_29af79a321e3, recipe_name=炒/煎、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 炒/煎、凉拌
关键技巧内容:
## 正文
# 炒/煎
## 器具
## 器具

可使用普通金属制（铁/不锈钢/铝）炒/煎锅或不粘锅。

不建议使用铝制容器, 原因详见食品安全一节
## 注意事项
### 注意事项

* 使用普通锅炒菜不粘的方法：
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。
## 热锅凉油法
#### 热锅凉油法

* 记住一定要是热锅凉油，首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入凉油，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 把油倒出来，倒出来后不要刷锅
 * 可以重复上述步骤 2-3 遍以得到更好的不粘效果
 * 注意：如果是燃气，可能会喷火，注意安全
## 热锅双油法
#### 热锅双油法

* 首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入“少量凉油”，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 再继续放入凉油，开始炒菜
 * 注意：如果是燃气，可能会喷火，注意安全。

补充：

* 目的是使油挂满锅底，所有市面上的家用锅都适用，挂油后秒变不粘锅。
* 使用不粘锅煎炒食物不会粘锅。不粘锅的功能来源于其内壁上的涂层。**金属锅铲会划伤涂层。使用不粘锅时应使用木制或硅胶锅铲以避免损坏涂层。**
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料
## 注意事项
### 注意事项

* 判断锅/油是否烧热时，可将手平放于锅的上方感受热量；油热后方可放入食材。
* 倒油入锅前，务必确认锅的内部没有残余水份。**水会导致热油飞溅，造成危险。**
* 接上条，食材放入油锅前，应当沥干水份（蛋液没事）；同理，不可将未解冻的食材放入油锅，以免冰化后造成危险。
* **若油锅起火，切不可倒水灭火**。这样做会使火势扩大。火刚起时，可迅速关火，盖上锅盖。
## 正文
# 凉拌
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
分类: 早餐
菜系: 未知
# 鸡蛋三明治
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 5分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 培根 (Ingredient): category: 蛋白质
```

### pair_order=1
source: rerank_input

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### pair_order=2
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

### pair_order=3
source: rerank_input

```text
菜系: 技巧知识
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=4
source: rerank_input

```text
菜品: 蒸箱鸡蛋羹
菜系: 未知
## 所需食材
1. 生抽(6ml)
2. 纯净水(1.0-1.5倍鸡蛋体积ml)
3. 食用油(5ml)
4. 食用盐(1g)
5. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=5
source: rerank_input

```text
菜品: 西红柿炒鸡蛋
菜系: 未知
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=6
source: rerank_input

```text
菜品: 鸡蛋火腿炒黄瓜
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=7
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

### pair_order=10
source: rerank_input

```text
菜品: 煮泡面加蛋
菜系: 未知
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=11
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 炒/煎、凉拌
关键技巧内容:
## 正文
# 炒/煎
## 器具
## 器具

可使用普通金属制（铁/不锈钢/铝）炒/煎锅或不粘锅。

不建议使用铝制容器, 原因详见食品安全一节
## 注意事项
### 注意事项

* 使用普通锅炒菜不粘的方法：
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。
## 热锅凉油法
#### 热锅凉油法

* 记住一定要是热锅凉油，首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入凉油，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 把油倒出来，倒出来后不要刷锅
 * 可以重复上述步骤 2-3 遍以得到更好的不粘效果
 * 注意：如果是燃气，可能会喷火，注意安全
## 热锅双油法
#### 热锅双油法

* 首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入“少量凉油”，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 再继续放入凉油，开始炒菜
 * 注意：如果是燃气，可能会喷火，注意安全。

补充：

* 目的是使油挂满锅底，所有市面上的家用锅都适用，挂油后秒变不粘锅。
* 使用不粘锅煎炒食物不会粘锅。不粘锅的功能来源于其内壁上的涂层。**金属锅铲会划伤涂层。使用不粘锅时应使用木制或硅胶锅铲以避免损坏涂层。**
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料
## 注意事项
### 注意事项

* 判断锅/油是否烧热时，可将手平放于锅的上方感受热量；油热后方可放入食材。
* 倒油入锅前，务必确认锅的内部没有残余水份。**水会导致热油飞溅，造成危险。**
* 接上条，食材放入油锅前，应当沥干水份（蛋液没事）；同理，不可将未解冻的食材放入油锅，以免冰化后造成危险。
* **若油锅起火，切不可倒水灭
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201000730, chunk_id=201000730_chunk_145, recipe_name=鸡蛋三明治, category=早餐, score=0.676352322101593, search_type=vector_enhanced

```text
# 鸡蛋三明治
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 5分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 培根 (Ingredient): category: 蛋白质
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.589226484298706, search_type=vector_enhanced

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
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5826243758201599, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7,tipdoc_29af79a321e3, recipe_name=炒/煎、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 炒/煎、凉拌
关键技巧内容:
## 正文
# 炒/煎
## 器具
## 器具

可使用普通金属制（铁/不锈钢/铝）炒/煎锅或不粘锅。

不建议使用铝制容器, 原因详见食品安全一节
## 注意事项
### 注意事项

* 使用普通锅炒菜不粘的方法：
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。
## 热锅凉油法
#### 热锅凉油法

* 记住一定要是热锅凉油，首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入凉油，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 把油倒出来，倒出来后不要刷锅
 * 可以重复上述步骤 2-3 遍以得到更好的不粘效果
 * 注意：如果是燃气，可能会喷火，注意安全
## 热锅双油法
#### 热锅双油法

* 首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入“少量凉油”，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 再继续放入凉油，开始炒菜
 * 注意：如果是燃气，可能会喷火，注意安全。

补充：

* 目的是使油挂满锅底，所有市面上的家用锅都适用，挂油后秒变不粘锅。
* 使用不粘锅煎炒食物不会粘锅。不粘锅的功能来源于其内壁上的涂层。**金属锅铲会划伤涂层。使用不粘锅时应使用木制或硅胶锅铲以避免损坏涂层。**
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料
## 注意事项
### 注意事项

* 判断锅/油是否烧热时，可将手平放于锅的上方感受热量；油热后方可放入食材。
* 倒油入锅前，务必确认锅的内部没有残余水份。**水会导致热油飞溅，造成危险。**
* 接上条，食材放入油锅前，应当沥干水份（蛋液没事）；同理，不可将未解冻的食材放入油锅，以免冰化后造成危险。
* **若油锅起火，切不可倒水灭火**。这样做会使火势扩大。火刚起时，可迅速关火，盖上锅盖。
## 正文
# 凉拌
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.5936087369918823, search_type=vector_enhanced

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

### result_order=5
source: reranked_results
metadata_summary: node_id=tipdoc_fd7f557c37a7, chunk_id=tipdoc_fd7f557c37a7_chunk_1326, recipe_name=凉拌, category=烹饪技巧, score=0.6221157908439636, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201004172, chunk_id=201004172_chunk_827, recipe_name=煮泡面加蛋, category=主食, score=0.5786027312278748, search_type=vector_enhanced

```text
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201005709, chunk_id=201005709_chunk_1131, recipe_name=蒸箱鸡蛋羹, category=素菜, score=0.601850688457489, search_type=vector_enhanced

```text
## 所需食材
1. 生抽(6ml)
2. 纯净水(1.0-1.5倍鸡蛋体积ml)
3. 食用油(5ml)
4. 食用盐(1g)
5. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201005272, chunk_id=201005272_chunk_1045, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, score=0.5937576293945312, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 黄瓜洗净，切半圆形片，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 火腿切半圆形片，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 红尖椒（可选）切碎，备用
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 将鸡蛋打入碗中，搅匀，即为鸡蛋液
方法: 搅拌
工具: 碗,筷子

### 第5步
步骤: 步骤5
描述: 热锅里倒5ml食用油
方法: 加热
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 油热后转小火，倒入打散的鸡蛋液，用筷子划散，翻炒至鸡蛋结为固体且颜色微微发黄，即为半熟鸡蛋，盛出备用
方法: 炒
工具: 炒锅,筷子
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 不用洗锅，往锅内倒入5ml食用油，倒入黄瓜片大火翻炒1分钟
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 把半熟鸡蛋倒入锅中，调入2g盐、3ml生抽，立刻倒入火腿片和辣椒碎（可选）翻炒均匀
方法: 炒
工具: 炒锅,锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=9
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

### result_order=10
source: reranked_results
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1170, recipe_name=炒/煎, category=烹饪技巧, score=0.6197894811630249, search_type=vector_enhanced

```text
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.6004815697669983, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201000730, chunk_id=201000730_chunk_145, recipe_name=鸡蛋三明治, category=早餐, score=0.676352322101593, search_type=vector_enhanced

```text
# 鸡蛋三明治
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 5分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 培根 (Ingredient): category: 蛋白质
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.589226484298706, search_type=vector_enhanced

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
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5826243758201599, search_type=vector_enhanced

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
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7,tipdoc_29af79a321e3, recipe_name=炒/煎、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 炒/煎、凉拌
关键技巧内容:
## 正文
# 炒/煎
## 器具
## 器具

可使用普通金属制（铁/不锈钢/铝）炒/煎锅或不粘锅。

不建议使用铝制容器, 原因详见食品安全一节
## 注意事项
### 注意事项

* 使用普通锅炒菜不粘的方法：
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。
## 热锅凉油法
#### 热锅凉油法

* 记住一定要是热锅凉油，首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入凉油，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 把油倒出来，倒出来后不要刷锅
 * 可以重复上述步骤 2-3 遍以得到更好的不粘效果
 * 注意：如果是燃气，可能会喷火，注意安全
## 热锅双油法
#### 热锅双油法

* 首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入“少量凉油”，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 再继续放入凉油，开始炒菜
 * 注意：如果是燃气，可能会喷火，注意安全。

补充：

* 目的是使油挂满锅底，所有市面上的家用锅都适用，挂油后秒变不粘锅。
* 使用不粘锅煎炒食物不会粘锅。不粘锅的功能来源于其内壁上的涂层。**金属锅铲会划伤涂层。使用不粘锅时应使用木制或硅胶锅铲以避免损坏涂层。**
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料
## 注意事项
### 注意事项

* 判断锅/油是否烧热时，可将手平放于锅的上方感受热量；油热后方可放入食材。
* 倒油入锅前，务必确认锅的内部没有残余水份。**水会导致热油飞溅，造成危险。**
* 接上条，食材放入油锅前，应当沥干水份（蛋液没事）；同理，不可将未解冻的食材放入油锅，以免冰化后造成危险。
* **若油锅起火，切不可倒水灭火**。这样做会使火势扩大。火刚起时，可迅速关火，盖上锅盖。
## 正文
# 凉拌
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.5936087369918823, search_type=vector_enhanced

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

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201000730, chunk_id=201000730_chunk_145, recipe_name=鸡蛋三明治, category=早餐, score=0.676352322101593, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
# 鸡蛋三明治
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 5分钟
份量: 1人份

关联图谱:
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 吐司 (Ingredient): category: 淀粉类
- OUT REQUIRES 培根 (Ingredient): category: 蛋白质
```

### result_order=1
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.589226484298706, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5826243758201599, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_fd7f557c37a7,tipdoc_29af79a321e3, recipe_name=炒/煎、凉拌, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 炒/煎、凉拌
关键技巧内容:
## 正文
# 炒/煎
## 器具
## 器具

可使用普通金属制（铁/不锈钢/铝）炒/煎锅或不粘锅。

不建议使用铝制容器, 原因详见食品安全一节
## 注意事项
### 注意事项

* 使用普通锅炒菜不粘的方法：
## 先炒鸡蛋法
#### 先炒鸡蛋法

* 不管炒什么菜之前都炒个鸡蛋，炒完不刷锅，再炒下个菜时就不粘。
## 热锅凉油法
#### 热锅凉油法

* 记住一定要是热锅凉油，首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入凉油，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 把油倒出来，倒出来后不要刷锅
 * 可以重复上述步骤 2-3 遍以得到更好的不粘效果
 * 注意：如果是燃气，可能会喷火，注意安全
## 热锅双油法
#### 热锅双油法

* 首先热锅
 * 干净的锅什么都不放，干烧，使其受热均匀，烧热
 * 放入“少量凉油”，旋转锅子，使油沾满整个锅（可以来回旋转使其受热均匀）
 * 看到有气体从锅中发出时，就表示锅子的油已经烧热了
 * 再继续放入凉油，开始炒菜
 * 注意：如果是燃气，可能会喷火，注意安全。

补充：

* 目的是使油挂满锅底，所有市面上的家用锅都适用，挂油后秒变不粘锅。
* 使用不粘锅煎炒食物不会粘锅。不粘锅的功能来源于其内壁上的涂层。**金属锅铲会划伤涂层。使用不粘锅时应使用木制或硅胶锅铲以避免损坏涂层。**
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料
## 注意事项
### 注意事项

* 判断锅/油是否烧热时，可将手平放于锅的上方感受热量；油热后方可放入食材。
* 倒油入锅前，务必确认锅的内部没有残余水份。**水会导致热油飞溅，造成危险。**
* 接上条，食材放入油锅前，应当沥干水份（蛋液没事）；同理，不可将未解冻的食材放入油锅，以免冰化后造成危险。
* **若油锅起火，切不可倒水灭火**。这样做会使火势扩大。火刚起时，可迅速关火，盖上锅盖。
## 正文
# 凉拌
```

### result_order=4
source: generation_context
metadata_summary: node_id=201000628, chunk_id=201000628_chunk_119, recipe_name=燕麦鸡蛋饼, category=早餐, score=0.5936087369918823, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

