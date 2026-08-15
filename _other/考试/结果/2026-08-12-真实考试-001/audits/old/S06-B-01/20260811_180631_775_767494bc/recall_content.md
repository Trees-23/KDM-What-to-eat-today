# Recall Content

audit_id: 20260811_180631_775_767494bc
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201001539, recipe_name=鸡汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡汤
食材名称: 鸡汤
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
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
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 暖胃
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

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6349042654037476, search_type=vector_enhanced

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

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6143561601638794, search_type=vector_enhanced

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
metadata_summary: node_id=201000571, chunk_id=201000571_chunk_105, recipe_name=手抓饼, category=早餐, score=0.6104562282562256, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(50毫升)
2. 开水(100毫升)
3. 普通面粉(200克)
4. 火腿(30克)
5. 生菜(30克)
6. 盐(3克)
7. 芝士片(1片)
8. 食用油(15毫升)
9. 鸡蛋(1个)

关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004588, chunk_id=201004588_chunk_913, recipe_name=火腿饭团, category=主食, score=0.6031479835510254, search_type=vector_enhanced

```text
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201001136, chunk_id=201001136_chunk_246, recipe_name=龟苓膏, category=甜品, score=0.6027151346206665, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(120毫升)
2. 开水(500毫升)
3. 白砂糖(100克)
4. 龟苓膏粉(25克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201001398, chunk_id=201001398_chunk_308, recipe_name=金汤力, category=饮料, score=0.6024594306945801, search_type=vector_enhanced

```text
## 所需食材
1. 冰块(100克)
2. 新鲜绿叶(1片)
3. 柠檬(1个)
4. 汤力水气泡水(1罐)
5. 金酒(30~40毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201003989, chunk_id=201003989_chunk_785, recipe_name=银耳莲子粥, category=汤类, score=0.5982207655906677, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10-20g)
2. 去心莲子(20g)
3. 枸杞(5-6g)
4. 红枣(6g)
5. 银耳(60g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5917647480964661, search_type=vector_enhanced

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
metadata_summary: node_id=201003873, chunk_id=201003873_chunk_759, recipe_name=陈皮排骨汤, category=汤类, score=0.5892394781112671, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤容器
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤勺

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201004002, chunk_id=201004002_chunk_790, recipe_name=陈皮排骨汤, category=汤类, score=0.5889403820037842, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤盅
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤匙
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201001539, recipe_name=鸡汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡汤
食材名称: 鸡汤
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=1
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

### result_order=2
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

### result_order=3
source: branch_grouped
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 暖胃
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

### result_order=4
source: branch_grouped
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6349042654037476, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6143561601638794, search_type=vector_enhanced

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
metadata_summary: node_id=201000571, chunk_id=201000571_chunk_105, recipe_name=手抓饼, category=早餐, score=0.6104562282562256, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(50毫升)
2. 开水(100毫升)
3. 普通面粉(200克)
4. 火腿(30克)
5. 生菜(30克)
6. 盐(3克)
7. 芝士片(1片)
8. 食用油(15毫升)
9. 鸡蛋(1个)

关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201004588, chunk_id=201004588_chunk_913, recipe_name=火腿饭团, category=主食, score=0.6031479835510254, search_type=vector_enhanced

```text
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201001136, chunk_id=201001136_chunk_246, recipe_name=龟苓膏, category=甜品, score=0.6027151346206665, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(120毫升)
2. 开水(500毫升)
3. 白砂糖(100克)
4. 龟苓膏粉(25克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201001398, chunk_id=201001398_chunk_308, recipe_name=金汤力, category=饮料, score=0.6024594306945801, search_type=vector_enhanced

```text
## 所需食材
1. 冰块(100克)
2. 新鲜绿叶(1片)
3. 柠檬(1个)
4. 汤力水气泡水(1罐)
5. 金酒(30~40毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201003989, chunk_id=201003989_chunk_785, recipe_name=银耳莲子粥, category=汤类, score=0.5982207655906677, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10-20g)
2. 去心莲子(20g)
3. 枸杞(5-6g)
4. 红枣(6g)
5. 银耳(60g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5917647480964661, search_type=vector_enhanced

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
metadata_summary: node_id=201003873, chunk_id=201003873_chunk_759, recipe_name=陈皮排骨汤, category=汤类, score=0.5892394781112671, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤容器
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤勺

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201004002, chunk_id=201004002_chunk_790, recipe_name=陈皮排骨汤, category=汤类, score=0.5889403820037842, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤盅
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤匙
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201001539, recipe_name=鸡汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡汤
食材名称: 鸡汤
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=1
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

### result_order=2
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

### result_order=3
source: merged_candidates
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 暖胃
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

### result_order=4
source: merged_candidates
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6349042654037476, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6143561601638794, search_type=vector_enhanced

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
metadata_summary: node_id=201000571, chunk_id=201000571_chunk_105, recipe_name=手抓饼, category=早餐, score=0.6104562282562256, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(50毫升)
2. 开水(100毫升)
3. 普通面粉(200克)
4. 火腿(30克)
5. 生菜(30克)
6. 盐(3克)
7. 芝士片(1片)
8. 食用油(15毫升)
9. 鸡蛋(1个)

关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004588, chunk_id=201004588_chunk_913, recipe_name=火腿饭团, category=主食, score=0.6031479835510254, search_type=vector_enhanced

```text
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201001136, chunk_id=201001136_chunk_246, recipe_name=龟苓膏, category=甜品, score=0.6027151346206665, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(120毫升)
2. 开水(500毫升)
3. 白砂糖(100克)
4. 龟苓膏粉(25克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201001398, chunk_id=201001398_chunk_308, recipe_name=金汤力, category=饮料, score=0.6024594306945801, search_type=vector_enhanced

```text
## 所需食材
1. 冰块(100克)
2. 新鲜绿叶(1片)
3. 柠檬(1个)
4. 汤力水气泡水(1罐)
5. 金酒(30~40毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201003989, chunk_id=201003989_chunk_785, recipe_name=银耳莲子粥, category=汤类, score=0.5982207655906677, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10-20g)
2. 去心莲子(20g)
3. 枸杞(5-6g)
4. 红枣(6g)
5. 银耳(60g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5917647480964661, search_type=vector_enhanced

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
metadata_summary: node_id=201003873, chunk_id=201003873_chunk_759, recipe_name=陈皮排骨汤, category=汤类, score=0.5892394781112671, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤容器
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤勺

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201004002, chunk_id=201004002_chunk_790, recipe_name=陈皮排骨汤, category=汤类, score=0.5889403820037842, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤盅
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤匙
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 鸡汤
食材名称: 鸡汤
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### pair_order=1
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

### pair_order=2
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

### pair_order=3
source: rerank_input

```text
命中关键词: 暖胃
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

### pair_order=4
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
菜品: 手抓饼
分类: 早餐
菜系: 未知
## 所需食材
1. 冷水(50毫升)
2. 开水(100毫升)
3. 普通面粉(200克)
4. 火腿(30克)
5. 生菜(30克)
6. 盐(3克)
7. 芝士片(1片)
8. 食用油(15毫升)
9. 鸡蛋(1个)

关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### pair_order=7
source: rerank_input

```text
菜品: 火腿饭团
菜系: 未知
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=8
source: rerank_input

```text
菜系: 未知
## 所需食材
1. 冷水(120毫升)
2. 开水(500毫升)
3. 白砂糖(100克)
4. 龟苓膏粉(25克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### pair_order=9
source: rerank_input

```text
菜品: 金汤力
菜系: 未知
## 所需食材
1. 冰块(100克)
2. 新鲜绿叶(1片)
3. 柠檬(1个)
4. 汤力水气泡水(1罐)
5. 金酒(30~40毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=10
source: rerank_input

```text
菜品: 银耳莲子粥
菜系: 未知
## 所需食材
1. 冰糖(10-20g)
2. 去心莲子(20g)
3. 枸杞(5-6g)
4. 红枣(6g)
5. 银耳(60g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
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
菜品: 陈皮排骨汤
菜系: 粤菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤容器
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤勺

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=13
source: rerank_input

```text
菜品: 陈皮排骨汤
菜系: 粤菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤盅
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤匙
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6143561601638794, search_type=vector_enhanced

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
metadata_summary: node_id=201003989, chunk_id=201003989_chunk_785, recipe_name=银耳莲子粥, category=汤类, score=0.5982207655906677, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10-20g)
2. 去心莲子(20g)
3. 枸杞(5-6g)
4. 红枣(6g)
5. 银耳(60g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 暖胃
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

### result_order=3
source: reranked_results
metadata_summary: node_id=201001398, chunk_id=201001398_chunk_308, recipe_name=金汤力, category=饮料, score=0.6024594306945801, search_type=vector_enhanced

```text
## 所需食材
1. 冰块(100克)
2. 新鲜绿叶(1片)
3. 柠檬(1个)
4. 汤力水气泡水(1罐)
5. 金酒(30~40毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201004002, chunk_id=201004002_chunk_790, recipe_name=陈皮排骨汤, category=汤类, score=0.5889403820037842, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤盅
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤匙
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201003873, chunk_id=201003873_chunk_759, recipe_name=陈皮排骨汤, category=汤类, score=0.5892394781112671, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤容器
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤勺

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201001136, chunk_id=201001136_chunk_246, recipe_name=龟苓膏, category=甜品, score=0.6027151346206665, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(120毫升)
2. 开水(500毫升)
3. 白砂糖(100克)
4. 龟苓膏粉(25克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 甜品 (Category)
- OUT BELONGS_TO 甜品 (RecipeCategory)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201001539, recipe_name=鸡汤, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡汤
食材名称: 鸡汤
类别: 其他
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 其他 (Category)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_848, recipe_name=蛋炒饭, category=主食, score=0.6349042654037476, search_type=vector_enhanced

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

### result_order=9
source: reranked_results
metadata_summary: node_id=201000571, chunk_id=201000571_chunk_105, recipe_name=手抓饼, category=早餐, score=0.6104562282562256, search_type=vector_enhanced

```text
## 所需食材
1. 冷水(50毫升)
2. 开水(100毫升)
3. 普通面粉(200克)
4. 火腿(30克)
5. 生菜(30克)
6. 盐(3克)
7. 芝士片(1片)
8. 食用油(15毫升)
9. 鸡蛋(1个)

关联图谱:
- OUT REQUIRES 芝士片 (Ingredient): category: 蛋白质
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_844, recipe_name=蛋包饭, category=主食, score=0.5917647480964661, search_type=vector_enhanced

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

### result_order=12
source: reranked_results
metadata_summary: node_id=201004588, chunk_id=201004588_chunk_913, recipe_name=火腿饭团, category=主食, score=0.6031479835510254, search_type=vector_enhanced

```text
## 所需食材
1. 冷冻玉米粒(30g)
2. 冷冻青豆(30g)
3. 水(90ml)
4. 沙拉酱(20g)
5. 海苔碎(10g)
6. 火腿(100g)
7. 米饭(125g)
8. 食用油(10-15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=13
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
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6143561601638794, search_type=vector_enhanced

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
metadata_summary: node_id=201003989, chunk_id=201003989_chunk_785, recipe_name=银耳莲子粥, category=汤类, score=0.5982207655906677, search_type=vector_enhanced

```text
## 所需食材
1. 冰糖(10-20g)
2. 去心莲子(20g)
3. 枸杞(5-6g)
4. 红枣(6g)
5. 银耳(60g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 暖胃
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

### result_order=3
source: top_k_final
metadata_summary: node_id=201001398, chunk_id=201001398_chunk_308, recipe_name=金汤力, category=饮料, score=0.6024594306945801, search_type=vector_enhanced

```text
## 所需食材
1. 冰块(100克)
2. 新鲜绿叶(1片)
3. 柠檬(1个)
4. 汤力水气泡水(1罐)
5. 金酒(30~40毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201004002, chunk_id=201004002_chunk_790, recipe_name=陈皮排骨汤, category=汤类, score=0.5889403820037842, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤盅
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤匙
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6143561601638794, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
metadata_summary: node_id=201003989, chunk_id=201003989_chunk_785, recipe_name=银耳莲子粥, category=汤类, score=0.5982207655906677, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 冰糖(10-20g)
2. 去心莲子(20g)
3. 枸杞(5-6g)
4. 红枣(6g)
5. 银耳(60g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201002697, recipe_name=枝竹羊腩煲, category=荤菜, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 暖胃
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

### result_order=3
source: generation_context
metadata_summary: node_id=201001398, chunk_id=201001398_chunk_308, recipe_name=金汤力, category=饮料, score=0.6024594306945801, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 冰块(100克)
2. 新鲜绿叶(1片)
3. 柠檬(1个)
4. 汤力水气泡水(1罐)
5. 金酒(30~40毫升)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 饮料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: generation_context
metadata_summary: node_id=201004002, chunk_id=201004002_chunk_790, recipe_name=陈皮排骨汤, category=汤类, score=0.5889403820037842, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 排骨用热水过一遍，去血水
方法: 焯水
工具: 锅
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 陈皮、麦冬、玉竹、石斛和西洋参冲洗干净
方法: 冲洗
工具: 盆
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 煲汤盅洗干净
方法: 清洗
工具: 煲汤盅
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 打开煲汤盅，先放入排骨在底部，然后依次放入陈皮、麦冬、玉竹、石斛和西洋参
方法: 摆放
工具: 煲汤盅
时间: 约2分钟

### 第5步
步骤: 步骤5
描述: 加入热水进煲汤盅，水不宜太满
方法: 加水
工具: 煲汤盅
时间: 约1分钟

### 第6步
步骤: 步骤6
描述: 煲汤容器加入水，炖煮1.5小时
方法: 炖
工具: 煲汤盅
时间: 1.5小时

### 第7步
步骤: 步骤7
描述: 加入食盐，趁热饮用
方法: 调味
工具: 汤匙
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

