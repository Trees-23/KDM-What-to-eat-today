# Recall Content

audit_id: 20260811_180547_386_17af1734
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

### result_order=1
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

### result_order=2
source: entity_level
metadata_summary: node_id=201002073, recipe_name=鱼香肉丝, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鱼香肉丝
菜品名称: 鱼香肉丝
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=3
source: entity_level
metadata_summary: node_id=201002454, recipe_name=宫保鸡丁, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 宫保鸡丁
菜品名称: 宫保鸡丁
分类: 荤菜
菜系: 川菜
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

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6798698902130127, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 米饭提前用铲子铲成小块
方法: 切
工具: 铲子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 火腿肠、胡萝卜、黄瓜等根据需求切片或者块状
方法: 切
工具: 刀,案板
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 如果家里有熟肉，准备好味道更佳
方法: 准备
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 将蛋白、蛋黄分开，分别打入一个大碗里，各自搅匀。注意，不要在这一步加盐
方法: 分离,搅拌
工具: 碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 大火热锅，待锅里冒烟放入食用油，放入蛋白，待主体凝固后盛出备用
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 如果油够，则直接放入蛋黄；如果油不够则放入食用油并等其升温到大火热锅
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 待蛋黄主体凝固后，将火调至中小火，倒入火腿肠、熟肉、胡萝卜、黄瓜等备料，翻炒10秒钟到爆香
方法: 炒
工具: 炒锅,锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 重新倒入蛋白，翻炒5秒，迅速倒入米饭大火翻炒，使每一粒饭都裹上鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 翻炒过程中将米饭的块状捣碎，待米饭全部捣碎并翻炒均匀
方法: 炒,捣碎
工具: 锅铲
时间: 3分钟

### 第10步
步骤: 步骤10
描述: 调至小火，加盐、胡椒粉、生抽，进一步翻炒均匀，能看到一些米饭在锅里有“跳起来”的时候即可
方法: 炒
工具: 锅铲
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 最后倒入香葱再翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第12步
步骤: 步骤12
描述: 关火，盛入碗中
方法: 盛盘
工具: 碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6794626116752625, search_type=vector_enhanced

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
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6760270595550537, search_type=vector_enhanced

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

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.6741757988929749, search_type=vector_enhanced

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

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.6686538457870483, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201003745, chunk_id=201003745_chunk_733, recipe_name=皮蛋瘦肉粥, category=主食, score=0.6681790351867676, search_type=vector_enhanced

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

### result_order=6
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.663419783115387, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_440, recipe_name=黄焖鸡, category=荤菜, score=0.6572251915931702, search_type=vector_enhanced

```text
## 所需食材
1. 味精
2. 土豆(1个)
3. 干辣椒(5.5个)
4. 料酒(10ml)
5. 生姜片(2片)
6. 白糖(5g)
7. 白胡椒粉(5g)
8. 盐(10g)
9. 酱油(5ml)
10. 青椒(2个)
11. 香菇(5朵)
12. 鸡腿(2只)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201004801, chunk_id=201004801_chunk_952, recipe_name=韩式拌饭, category=主食, score=0.655390739440918, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 蔬菜清洗、切丝，放锅中翻炒至食材变软后盛出备用。
方法: 清洗,切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅中加水，水沸腾后焯牛肉卷，煮熟约3分钟捞出。
方法: 煮
工具: 锅,筷子
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 煎溏心蛋备用。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 将米饭放在碗中，倒扣在大碗中央。
方法: 摆盘
工具: 碗
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 将炒好的蔬菜和牛肉卷依次绕圈摆放在米饭上，把煎蛋放在中央。
方法: 摆盘
工具: 碗,筷子
时间: 2分钟

### 第6步
步骤: 步骤6
描述: 调制酱汁：10ml韩式辣酱 + 5ml生抽 + 20ml雪碧 + 10g芝麻 + 5ml芝麻油，搅拌均匀，可按口味再加生抽和盐。
方法: 搅拌
工具: 小碗,勺子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将调好的酱汁均匀淋在摆好盘的食材上即可。
方法: 淋
工具: 勺子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.6538468599319458, search_type=vector_enhanced

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

### result_order=2
source: branch_grouped
metadata_summary: node_id=201002073, recipe_name=鱼香肉丝, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鱼香肉丝
菜品名称: 鱼香肉丝
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201002454, recipe_name=宫保鸡丁, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 宫保鸡丁
菜品名称: 宫保鸡丁
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=4
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

### result_order=5
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

### result_order=6
source: branch_grouped
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6798698902130127, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 米饭提前用铲子铲成小块
方法: 切
工具: 铲子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 火腿肠、胡萝卜、黄瓜等根据需求切片或者块状
方法: 切
工具: 刀,案板
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 如果家里有熟肉，准备好味道更佳
方法: 准备
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 将蛋白、蛋黄分开，分别打入一个大碗里，各自搅匀。注意，不要在这一步加盐
方法: 分离,搅拌
工具: 碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 大火热锅，待锅里冒烟放入食用油，放入蛋白，待主体凝固后盛出备用
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 如果油够，则直接放入蛋黄；如果油不够则放入食用油并等其升温到大火热锅
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 待蛋黄主体凝固后，将火调至中小火，倒入火腿肠、熟肉、胡萝卜、黄瓜等备料，翻炒10秒钟到爆香
方法: 炒
工具: 炒锅,锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 重新倒入蛋白，翻炒5秒，迅速倒入米饭大火翻炒，使每一粒饭都裹上鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 翻炒过程中将米饭的块状捣碎，待米饭全部捣碎并翻炒均匀
方法: 炒,捣碎
工具: 锅铲
时间: 3分钟

### 第10步
步骤: 步骤10
描述: 调至小火，加盐、胡椒粉、生抽，进一步翻炒均匀，能看到一些米饭在锅里有“跳起来”的时候即可
方法: 炒
工具: 锅铲
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 最后倒入香葱再翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第12步
步骤: 步骤12
描述: 关火，盛入碗中
方法: 盛盘
工具: 碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6794626116752625, search_type=vector_enhanced

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
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6760270595550537, search_type=vector_enhanced

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
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.6741757988929749, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.6686538457870483, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=201003745, chunk_id=201003745_chunk_733, recipe_name=皮蛋瘦肉粥, category=主食, score=0.6681790351867676, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.663419783115387, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_440, recipe_name=黄焖鸡, category=荤菜, score=0.6572251915931702, search_type=vector_enhanced

```text
## 所需食材
1. 味精
2. 土豆(1个)
3. 干辣椒(5.5个)
4. 料酒(10ml)
5. 生姜片(2片)
6. 白糖(5g)
7. 白胡椒粉(5g)
8. 盐(10g)
9. 酱油(5ml)
10. 青椒(2个)
11. 香菇(5朵)
12. 鸡腿(2只)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201004801, chunk_id=201004801_chunk_952, recipe_name=韩式拌饭, category=主食, score=0.655390739440918, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 蔬菜清洗、切丝，放锅中翻炒至食材变软后盛出备用。
方法: 清洗,切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅中加水，水沸腾后焯牛肉卷，煮熟约3分钟捞出。
方法: 煮
工具: 锅,筷子
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 煎溏心蛋备用。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 将米饭放在碗中，倒扣在大碗中央。
方法: 摆盘
工具: 碗
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 将炒好的蔬菜和牛肉卷依次绕圈摆放在米饭上，把煎蛋放在中央。
方法: 摆盘
工具: 碗,筷子
时间: 2分钟

### 第6步
步骤: 步骤6
描述: 调制酱汁：10ml韩式辣酱 + 5ml生抽 + 20ml雪碧 + 10g芝麻 + 5ml芝麻油，搅拌均匀，可按口味再加生抽和盐。
方法: 搅拌
工具: 小碗,勺子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将调好的酱汁均匀淋在摆好盘的食材上即可。
方法: 淋
工具: 勺子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.6538468599319458, search_type=vector_enhanced

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

### result_order=2
source: merged_candidates
metadata_summary: node_id=201002073, recipe_name=鱼香肉丝, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鱼香肉丝
菜品名称: 鱼香肉丝
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201002454, recipe_name=宫保鸡丁, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 宫保鸡丁
菜品名称: 宫保鸡丁
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=4
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

### result_order=5
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

### result_order=6
source: merged_candidates
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6798698902130127, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 米饭提前用铲子铲成小块
方法: 切
工具: 铲子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 火腿肠、胡萝卜、黄瓜等根据需求切片或者块状
方法: 切
工具: 刀,案板
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 如果家里有熟肉，准备好味道更佳
方法: 准备
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 将蛋白、蛋黄分开，分别打入一个大碗里，各自搅匀。注意，不要在这一步加盐
方法: 分离,搅拌
工具: 碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 大火热锅，待锅里冒烟放入食用油，放入蛋白，待主体凝固后盛出备用
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 如果油够，则直接放入蛋黄；如果油不够则放入食用油并等其升温到大火热锅
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 待蛋黄主体凝固后，将火调至中小火，倒入火腿肠、熟肉、胡萝卜、黄瓜等备料，翻炒10秒钟到爆香
方法: 炒
工具: 炒锅,锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 重新倒入蛋白，翻炒5秒，迅速倒入米饭大火翻炒，使每一粒饭都裹上鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 翻炒过程中将米饭的块状捣碎，待米饭全部捣碎并翻炒均匀
方法: 炒,捣碎
工具: 锅铲
时间: 3分钟

### 第10步
步骤: 步骤10
描述: 调至小火，加盐、胡椒粉、生抽，进一步翻炒均匀，能看到一些米饭在锅里有“跳起来”的时候即可
方法: 炒
工具: 锅铲
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 最后倒入香葱再翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第12步
步骤: 步骤12
描述: 关火，盛入碗中
方法: 盛盘
工具: 碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6794626116752625, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6760270595550537, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.6741757988929749, search_type=vector_enhanced

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
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.6686538457870483, search_type=vector_enhanced

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
metadata_summary: node_id=201003745, chunk_id=201003745_chunk_733, recipe_name=皮蛋瘦肉粥, category=主食, score=0.6681790351867676, search_type=vector_enhanced

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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.663419783115387, search_type=vector_enhanced

```text
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_440, recipe_name=黄焖鸡, category=荤菜, score=0.6572251915931702, search_type=vector_enhanced

```text
## 所需食材
1. 味精
2. 土豆(1个)
3. 干辣椒(5.5个)
4. 料酒(10ml)
5. 生姜片(2片)
6. 白糖(5g)
7. 白胡椒粉(5g)
8. 盐(10g)
9. 酱油(5ml)
10. 青椒(2个)
11. 香菇(5朵)
12. 鸡腿(2只)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: merged_candidates
metadata_summary: node_id=201004801, chunk_id=201004801_chunk_952, recipe_name=韩式拌饭, category=主食, score=0.655390739440918, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 蔬菜清洗、切丝，放锅中翻炒至食材变软后盛出备用。
方法: 清洗,切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅中加水，水沸腾后焯牛肉卷，煮熟约3分钟捞出。
方法: 煮
工具: 锅,筷子
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 煎溏心蛋备用。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 将米饭放在碗中，倒扣在大碗中央。
方法: 摆盘
工具: 碗
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 将炒好的蔬菜和牛肉卷依次绕圈摆放在米饭上，把煎蛋放在中央。
方法: 摆盘
工具: 碗,筷子
时间: 2分钟

### 第6步
步骤: 步骤6
描述: 调制酱汁：10ml韩式辣酱 + 5ml生抽 + 20ml雪碧 + 10g芝麻 + 5ml芝麻油，搅拌均匀，可按口味再加生抽和盐。
方法: 搅拌
工具: 小碗,勺子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将调好的酱汁均匀淋在摆好盘的食材上即可。
方法: 淋
工具: 勺子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=15
source: merged_candidates
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.6538468599319458, search_type=vector_enhanced

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
命中关键词: 麻婆豆腐
菜品名称: 麻婆豆腐
分类: 荤菜
菜系: 川菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 鱼香肉丝
菜品名称: 鱼香肉丝
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 宫保鸡丁
菜品名称: 宫保鸡丁
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### pair_order=4
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

### pair_order=5
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

### pair_order=6
source: rerank_input

```text
菜品: 蛋炒饭
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 米饭提前用铲子铲成小块
方法: 切
工具: 铲子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 火腿肠、胡萝卜、黄瓜等根据需求切片或者块状
方法: 切
工具: 刀,案板
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 如果家里有熟肉，准备好味道更佳
方法: 准备
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 将蛋白、蛋黄分开，分别打入一个大碗里，各自搅匀。注意，不要在这一步加盐
方法: 分离,搅拌
工具: 碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 大火热锅，待锅里冒烟放入食用油，放入蛋白，待主体凝固后盛出备用
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 如果油够，则直接放入蛋黄；如果油不够则放入食用油并等其升温到大火热锅
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 待蛋黄主体凝固后，将火调至中小火，倒入火腿肠、熟肉、胡萝卜、黄瓜等备料，翻炒10秒钟到爆香
方法: 炒
工具: 炒锅,锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 重新倒入蛋白，翻炒5秒，迅速倒入米饭大火翻炒，使每一粒饭都裹上鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 翻炒过程中将米饭的块状捣碎，待米饭全部捣碎并翻炒均匀
方法: 炒,捣碎
工具: 锅铲
时间: 3分钟

### 第10步
步骤: 步骤10
描述: 调至小火，加盐、胡椒粉、生抽，进一步翻炒均匀，能看到一些米饭在锅里有“跳起来”的时候即可
方法: 炒
工具: 锅铲
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 最后倒入香葱再翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第12步
步骤: 步骤12
描述: 关火，盛入碗中
方法: 盛盘
工具: 碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT
```

### pair_order=7
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

### pair_order=8
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
## 正文
# 如何决策吃什么

如何决策吃什么也是我做菜之前一大难题。所以只能用数学描述一下了。

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### pair_order=13
source: rerank_input

```text
菜品: 黄焖鸡
菜系: 未知
## 所需食材
1. 味精
2. 土豆(1个)
3. 干辣椒(5.5个)
4. 料酒(10ml)
5. 生姜片(2片)
6. 白糖(5g)
7. 白胡椒粉(5g)
8. 盐(10g)
9. 酱油(5ml)
10. 青椒(2个)
11. 香菇(5朵)
12. 鸡腿(2只)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=14
source: rerank_input

```text
菜品: 韩式拌饭
菜系: 韩餐
## 制作步骤

### 第1步
步骤: 步骤1
描述: 蔬菜清洗、切丝，放锅中翻炒至食材变软后盛出备用。
方法: 清洗,切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅中加水，水沸腾后焯牛肉卷，煮熟约3分钟捞出。
方法: 煮
工具: 锅,筷子
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 煎溏心蛋备用。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 将米饭放在碗中，倒扣在大碗中央。
方法: 摆盘
工具: 碗
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 将炒好的蔬菜和牛肉卷依次绕圈摆放在米饭上，把煎蛋放在中央。
方法: 摆盘
工具: 碗,筷子
时间: 2分钟

### 第6步
步骤: 步骤6
描述: 调制酱汁：10ml韩式辣酱 + 5ml生抽 + 20ml雪碧 + 10g芝麻 + 5ml芝麻油，搅拌均匀，可按口味再加生抽和盐。
方法: 搅拌
工具: 小碗,勺子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将调好的酱汁均匀淋在摆好盘的食材上即可。
方法: 淋
工具: 勺子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=15
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

### pair_order=16
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
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6798698902130127, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 米饭提前用铲子铲成小块
方法: 切
工具: 铲子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 火腿肠、胡萝卜、黄瓜等根据需求切片或者块状
方法: 切
工具: 刀,案板
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 如果家里有熟肉，准备好味道更佳
方法: 准备
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 将蛋白、蛋黄分开，分别打入一个大碗里，各自搅匀。注意，不要在这一步加盐
方法: 分离,搅拌
工具: 碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 大火热锅，待锅里冒烟放入食用油，放入蛋白，待主体凝固后盛出备用
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 如果油够，则直接放入蛋黄；如果油不够则放入食用油并等其升温到大火热锅
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 待蛋黄主体凝固后，将火调至中小火，倒入火腿肠、熟肉、胡萝卜、黄瓜等备料，翻炒10秒钟到爆香
方法: 炒
工具: 炒锅,锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 重新倒入蛋白，翻炒5秒，迅速倒入米饭大火翻炒，使每一粒饭都裹上鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 翻炒过程中将米饭的块状捣碎，待米饭全部捣碎并翻炒均匀
方法: 炒,捣碎
工具: 锅铲
时间: 3分钟

### 第10步
步骤: 步骤10
描述: 调至小火，加盐、胡椒粉、生抽，进一步翻炒均匀，能看到一些米饭在锅里有“跳起来”的时候即可
方法: 炒
工具: 锅铲
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 最后倒入香葱再翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第12步
步骤: 步骤12
描述: 关火，盛入碗中
方法: 盛盘
工具: 碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6794626116752625, search_type=vector_enhanced

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
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6760270595550537, search_type=vector_enhanced

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

### result_order=3
source: reranked_results
metadata_summary: node_id=201003745, chunk_id=201003745_chunk_733, recipe_name=皮蛋瘦肉粥, category=主食, score=0.6681790351867676, search_type=vector_enhanced

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

### result_order=4
source: reranked_results
metadata_summary: node_id=201004801, chunk_id=201004801_chunk_952, recipe_name=韩式拌饭, category=主食, score=0.655390739440918, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 蔬菜清洗、切丝，放锅中翻炒至食材变软后盛出备用。
方法: 清洗,切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 锅中加水，水沸腾后焯牛肉卷，煮熟约3分钟捞出。
方法: 煮
工具: 锅,筷子
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 煎溏心蛋备用。
方法: 煎
工具: 平底锅,锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 将米饭放在碗中，倒扣在大碗中央。
方法: 摆盘
工具: 碗
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 将炒好的蔬菜和牛肉卷依次绕圈摆放在米饭上，把煎蛋放在中央。
方法: 摆盘
工具: 碗,筷子
时间: 2分钟

### 第6步
步骤: 步骤6
描述: 调制酱汁：10ml韩式辣酱 + 5ml生抽 + 20ml雪碧 + 10g芝麻 + 5ml芝麻油，搅拌均匀，可按口味再加生抽和盐。
方法: 搅拌
工具: 小碗,勺子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将调好的酱汁均匀淋在摆好盘的食材上即可。
方法: 淋
工具: 勺子
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
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

### result_order=6
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

### result_order=7
source: reranked_results
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_440, recipe_name=黄焖鸡, category=荤菜, score=0.6572251915931702, search_type=vector_enhanced

```text
## 所需食材
1. 味精
2. 土豆(1个)
3. 干辣椒(5.5个)
4. 料酒(10ml)
5. 生姜片(2片)
6. 白糖(5g)
7. 白胡椒粉(5g)
8. 盐(10g)
9. 酱油(5ml)
10. 青椒(2个)
11. 香菇(5朵)
12. 鸡腿(2只)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
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
metadata_summary: node_id=201002162, chunk_id=201002162_chunk_448, recipe_name=农家一碗香, category=荤菜, score=0.6686538457870483, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_532, recipe_name=新疆大盘鸡, category=荤菜, score=0.6538468599319458, search_type=vector_enhanced

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

### result_order=12
source: reranked_results
metadata_summary: node_id=201002511, chunk_id=201002511_chunk_508, recipe_name=小炒黄牛肉, category=荤菜, score=0.6741757988929749, search_type=vector_enhanced

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

### result_order=14
source: reranked_results
metadata_summary: node_id=201002073, recipe_name=鱼香肉丝, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鱼香肉丝
菜品名称: 鱼香肉丝
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=15
source: reranked_results
metadata_summary: node_id=201002454, recipe_name=宫保鸡丁, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 宫保鸡丁
菜品名称: 宫保鸡丁
分类: 荤菜
菜系: 川菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=16
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1236, recipe_name=如何决策吃什么, category=通用知识, score=0.663419783115387, search_type=vector_enhanced

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
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6798698902130127, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 米饭提前用铲子铲成小块
方法: 切
工具: 铲子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 火腿肠、胡萝卜、黄瓜等根据需求切片或者块状
方法: 切
工具: 刀,案板
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 如果家里有熟肉，准备好味道更佳
方法: 准备
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 将蛋白、蛋黄分开，分别打入一个大碗里，各自搅匀。注意，不要在这一步加盐
方法: 分离,搅拌
工具: 碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 大火热锅，待锅里冒烟放入食用油，放入蛋白，待主体凝固后盛出备用
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 如果油够，则直接放入蛋黄；如果油不够则放入食用油并等其升温到大火热锅
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 待蛋黄主体凝固后，将火调至中小火，倒入火腿肠、熟肉、胡萝卜、黄瓜等备料，翻炒10秒钟到爆香
方法: 炒
工具: 炒锅,锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 重新倒入蛋白，翻炒5秒，迅速倒入米饭大火翻炒，使每一粒饭都裹上鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 翻炒过程中将米饭的块状捣碎，待米饭全部捣碎并翻炒均匀
方法: 炒,捣碎
工具: 锅铲
时间: 3分钟

### 第10步
步骤: 步骤10
描述: 调至小火，加盐、胡椒粉、生抽，进一步翻炒均匀，能看到一些米饭在锅里有“跳起来”的时候即可
方法: 炒
工具: 锅铲
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 最后倒入香葱再翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第12步
步骤: 步骤12
描述: 关火，盛入碗中
方法: 盛盘
工具: 碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6794626116752625, search_type=vector_enhanced

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
metadata_summary: node_id=201002295, recipe_name=米饭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 米饭
食材名称: 米饭
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=3
source: top_k_final
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
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6798698902130127, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 米饭提前用铲子铲成小块
方法: 切
工具: 铲子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 火腿肠、胡萝卜、黄瓜等根据需求切片或者块状
方法: 切
工具: 刀,案板
时间: 3分钟

### 第3步
步骤: 步骤3
描述: 如果家里有熟肉，准备好味道更佳
方法: 准备
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 将蛋白、蛋黄分开，分别打入一个大碗里，各自搅匀。注意，不要在这一步加盐
方法: 分离,搅拌
工具: 碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 大火热锅，待锅里冒烟放入食用油，放入蛋白，待主体凝固后盛出备用
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 如果油够，则直接放入蛋黄；如果油不够则放入食用油并等其升温到大火热锅
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 待蛋黄主体凝固后，将火调至中小火，倒入火腿肠、熟肉、胡萝卜、黄瓜等备料，翻炒10秒钟到爆香
方法: 炒
工具: 炒锅,锅铲
时间: 10秒

### 第8步
步骤: 步骤8
描述: 重新倒入蛋白，翻炒5秒，迅速倒入米饭大火翻炒，使每一粒饭都裹上鸡蛋
方法: 炒
工具: 炒锅,锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 翻炒过程中将米饭的块状捣碎，待米饭全部捣碎并翻炒均匀
方法: 炒,捣碎
工具: 锅铲
时间: 3分钟

### 第10步
步骤: 步骤10
描述: 调至小火，加盐、胡椒粉、生抽，进一步翻炒均匀，能看到一些米饭在锅里有“跳起来”的时候即可
方法: 炒
工具: 锅铲
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 最后倒入香葱再翻炒10秒
方法: 炒
工具: 锅铲
时间: 10秒

### 第12步
步骤: 步骤12
描述: 关火，盛入碗中
方法: 盛盘
工具: 碗
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.6794626116752625, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
metadata_summary: node_id=201002295, recipe_name=米饭, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 米饭
食材名称: 米饭
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201003481, recipe_name=麻婆豆腐, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

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

