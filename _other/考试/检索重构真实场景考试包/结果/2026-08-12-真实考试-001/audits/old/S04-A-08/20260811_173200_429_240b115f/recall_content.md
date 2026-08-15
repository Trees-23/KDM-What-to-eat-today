# Recall Content

audit_id: 20260811_173200_429_240b115f
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
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

### result_order=4
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

### result_order=5
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
metadata_summary: node_id=201005528, chunk_id=201005528_chunk_1096, recipe_name=糖拌西红柿, category=素菜, score=0.6169561147689819, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀将西红柿皮米字型划开
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 用筷子插入西红柿的菊花，在燃气上转动烤 10 秒（或用开水冲 30 秒），直到西红柿皮卷边
方法: 烤,烫
工具: 筷子,燃气,开水
时间: 10-30秒

### 第3步
步骤: 步骤3
描述: 把西红柿的衣服脱光
方法: 去皮
工具: 手

### 第4步
步骤: 步骤4
描述: 再西红柿大卸八块（沿纹路切可以更多的留汁水），去掉头部根蒂部，备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 全部切好后，将西红柿在盘子中均匀码一层
方法: 摆盘
工具: 盘子

### 第6步
步骤: 步骤6
描述: 撒上白糖，重复上面一步直到全部西红柿放完
方法: 撒
工具: 盘子

### 第7步
步骤: 步骤7
描述: 放入冰箱冷藏 10 分钟
方法: 冷藏
工具: 冰箱
时间: 10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1123, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.6097688674926758, search_type=vector_enhanced

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

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5857701897621155, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.5840438604354858, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.5804290771484375, search_type=vector_enhanced

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

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201003793, chunk_id=201003793_chunk_745, recipe_name=罗宋汤, category=汤类, score=0.5707922577857971, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201005528, chunk_id=201005528_chunk_1095, recipe_name=糖拌西红柿, category=素菜, score=0.5517750382423401, search_type=vector_enhanced

```text
## 所需食材
1. 白砂糖(20克)
2. 西红柿(200克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.5501641631126404, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.5493188500404358, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_628, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.546129047870636, search_type=vector_enhanced

```text
## 所需食材
1. 八角(0.5个)
2. 土豆(3个)
3. 姜(4片)
4. 料酒(35毫升)
5. 油(15毫升)
6. 洋葱(1个)
7. 牛肉(600克)
8. 白糖
9. 老抽
10. 花椒(3克)
11. 葱(1根)
12. 西红柿(3个)
13. 酱油(15毫升)
14. 香叶(2片)
15. 黑胡椒粉(2克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
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

### result_order=1
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

### result_order=2
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

### result_order=7
source: branch_grouped
metadata_summary: node_id=201005528, chunk_id=201005528_chunk_1096, recipe_name=糖拌西红柿, category=素菜, score=0.6169561147689819, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀将西红柿皮米字型划开
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 用筷子插入西红柿的菊花，在燃气上转动烤 10 秒（或用开水冲 30 秒），直到西红柿皮卷边
方法: 烤,烫
工具: 筷子,燃气,开水
时间: 10-30秒

### 第3步
步骤: 步骤3
描述: 把西红柿的衣服脱光
方法: 去皮
工具: 手

### 第4步
步骤: 步骤4
描述: 再西红柿大卸八块（沿纹路切可以更多的留汁水），去掉头部根蒂部，备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 全部切好后，将西红柿在盘子中均匀码一层
方法: 摆盘
工具: 盘子

### 第6步
步骤: 步骤6
描述: 撒上白糖，重复上面一步直到全部西红柿放完
方法: 撒
工具: 盘子

### 第7步
步骤: 步骤7
描述: 放入冰箱冷藏 10 分钟
方法: 冷藏
工具: 冰箱
时间: 10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1123, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.6097688674926758, search_type=vector_enhanced

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

### result_order=9
source: branch_grouped
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5857701897621155, search_type=vector_enhanced

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
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.5840438604354858, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.5804290771484375, search_type=vector_enhanced

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

### result_order=12
source: branch_grouped
metadata_summary: node_id=201003793, chunk_id=201003793_chunk_745, recipe_name=罗宋汤, category=汤类, score=0.5707922577857971, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201005528, chunk_id=201005528_chunk_1095, recipe_name=糖拌西红柿, category=素菜, score=0.5517750382423401, search_type=vector_enhanced

```text
## 所需食材
1. 白砂糖(20克)
2. 西红柿(200克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.5501641631126404, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1029, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.5493188500404358, search_type=vector_enhanced

```text
## 标签
快速做法：鸡蛋与西红柿同炒,可用生抽替代部分盐,可选加番茄酱增汤汁,可选加熟肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=16
source: branch_grouped
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_628, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.546129047870636, search_type=vector_enhanced

```text
## 所需食材
1. 八角(0.5个)
2. 土豆(3个)
3. 姜(4片)
4. 料酒(35毫升)
5. 油(15毫升)
6. 洋葱(1个)
7. 牛肉(600克)
8. 白糖
9. 老抽
10. 花椒(3克)
11. 葱(1根)
12. 西红柿(3个)
13. 酱油(15毫升)
14. 香叶(2片)
15. 黑胡椒粉(2克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
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

### result_order=1
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

### result_order=2
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

### result_order=7
source: merged_candidates
metadata_summary: node_id=201005528, chunk_id=201005528_chunk_1096, recipe_name=糖拌西红柿, category=素菜, score=0.6169561147689819, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀将西红柿皮米字型划开
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 用筷子插入西红柿的菊花，在燃气上转动烤 10 秒（或用开水冲 30 秒），直到西红柿皮卷边
方法: 烤,烫
工具: 筷子,燃气,开水
时间: 10-30秒

### 第3步
步骤: 步骤3
描述: 把西红柿的衣服脱光
方法: 去皮
工具: 手

### 第4步
步骤: 步骤4
描述: 再西红柿大卸八块（沿纹路切可以更多的留汁水），去掉头部根蒂部，备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 全部切好后，将西红柿在盘子中均匀码一层
方法: 摆盘
工具: 盘子

### 第6步
步骤: 步骤6
描述: 撒上白糖，重复上面一步直到全部西红柿放完
方法: 撒
工具: 盘子

### 第7步
步骤: 步骤7
描述: 放入冰箱冷藏 10 分钟
方法: 冷藏
工具: 冰箱
时间: 10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.5840438604354858, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5857701897621155, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.5804290771484375, search_type=vector_enhanced

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

### result_order=11
source: merged_candidates
metadata_summary: node_id=201003793, chunk_id=201003793_chunk_745, recipe_name=罗宋汤, category=汤类, score=0.5707922577857971, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.5501641631126404, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_628, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.546129047870636, search_type=vector_enhanced

```text
## 所需食材
1. 八角(0.5个)
2. 土豆(3个)
3. 姜(4片)
4. 料酒(35毫升)
5. 油(15毫升)
6. 洋葱(1个)
7. 牛肉(600克)
8. 白糖
9. 老抽
10. 花椒(3克)
11. 葱(1根)
12. 西红柿(3个)
13. 酱油(15毫升)
14. 香叶(2片)
15. 黑胡椒粉(2克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=1
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

### pair_order=2
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

### pair_order=7
source: rerank_input

```text
菜品: 糖拌西红柿
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀将西红柿皮米字型划开
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 用筷子插入西红柿的菊花，在燃气上转动烤 10 秒（或用开水冲 30 秒），直到西红柿皮卷边
方法: 烤,烫
工具: 筷子,燃气,开水
时间: 10-30秒

### 第3步
步骤: 步骤3
描述: 把西红柿的衣服脱光
方法: 去皮
工具: 手

### 第4步
步骤: 步骤4
描述: 再西红柿大卸八块（沿纹路切可以更多的留汁水），去掉头部根蒂部，备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 全部切好后，将西红柿在盘子中均匀码一层
方法: 摆盘
工具: 盘子

### 第6步
步骤: 步骤6
描述: 撒上白糖，重复上面一步直到全部西红柿放完
方法: 撒
工具: 盘子

### 第7步
步骤: 步骤7
描述: 放入冰箱冷藏 10 分钟
方法: 冷藏
工具: 冰箱
时间: 10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=8
source: rerank_input

```text
菜品: 西葫芦炒鸡蛋
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=9
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

### pair_order=10
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

### pair_order=11
source: rerank_input

```text
菜品: 罗宋汤
菜系: 未知
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=12
source: rerank_input

```text
菜品: 番茄牛肉蛋花汤
菜系: 未知
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### pair_order=13
source: rerank_input

```text
菜品: 西红柿土豆炖牛肉
菜系: 未知
## 所需食材
1. 八角(0.5个)
2. 土豆(3个)
3. 姜(4片)
4. 料酒(35毫升)
5. 油(15毫升)
6. 洋葱(1个)
7. 牛肉(600克)
8. 白糖
9. 老抽
10. 花椒(3克)
11. 葱(1根)
12. 西红柿(3个)
13. 酱油(15毫升)
14. 香叶(2片)
15. 黑胡椒粉(2克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.5804290771484375, search_type=vector_enhanced

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

### result_order=1
source: reranked_results
metadata_summary: node_id=201005528, chunk_id=201005528_chunk_1096, recipe_name=糖拌西红柿, category=素菜, score=0.6169561147689819, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀将西红柿皮米字型划开
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 用筷子插入西红柿的菊花，在燃气上转动烤 10 秒（或用开水冲 30 秒），直到西红柿皮卷边
方法: 烤,烫
工具: 筷子,燃气,开水
时间: 10-30秒

### 第3步
步骤: 步骤3
描述: 把西红柿的衣服脱光
方法: 去皮
工具: 手

### 第4步
步骤: 步骤4
描述: 再西红柿大卸八块（沿纹路切可以更多的留汁水），去掉头部根蒂部，备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 全部切好后，将西红柿在盘子中均匀码一层
方法: 摆盘
工具: 盘子

### 第6步
步骤: 步骤6
描述: 撒上白糖，重复上面一步直到全部西红柿放完
方法: 撒
工具: 盘子

### 第7步
步骤: 步骤7
描述: 放入冰箱冷藏 10 分钟
方法: 冷藏
工具: 冰箱
时间: 10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201005669, chunk_id=201005669_chunk_1124, recipe_name=西葫芦炒鸡蛋, category=素菜, score=0.5840438604354858, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 西红柿洗净，切成小块，备用
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 西葫芦洗净，切成边长约为4cm的菱形，备用
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 打三个鸡蛋到碗里，打散搅匀，备用
方法: 打散
工具: 碗,筷子

### 第4步
步骤: 步骤4
描述: 热锅，锅内放入5-10ml食用油
方法: 热锅
工具: 炒锅

### 第5步
步骤: 步骤5
描述: 倒入鸡蛋，保持翻炒至鸡蛋成固体，用锅铲分成小块后盛到碗里，备用
方法: 炒
工具: 炒锅,锅铲,碗

### 第6步
步骤: 步骤6
描述: 锅内放入5-10ml食用油，倒入西红柿，炒至变软
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 倒入西葫芦一起翻炒均匀，放入6g食用盐，将火调小然后等待4-5分钟
方法: 炒,焖
工具: 炒锅,锅铲
时间: 4-5分钟

### 第8步
步骤: 步骤8
描述: 倒入备用的鸡蛋，中火翻炒15秒
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

### 第9步
步骤: 步骤9
描述: 关火，盛盘
方法: 盛盘
工具: 锅铲
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_628, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.546129047870636, search_type=vector_enhanced

```text
## 所需食材
1. 八角(0.5个)
2. 土豆(3个)
3. 姜(4片)
4. 料酒(35毫升)
5. 油(15毫升)
6. 洋葱(1个)
7. 牛肉(600克)
8. 白糖
9. 老抽
10. 花椒(3克)
11. 葱(1根)
12. 西红柿(3个)
13. 酱油(15毫升)
14. 香叶(2片)
15. 黑胡椒粉(2克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=4
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

### result_order=5
source: reranked_results
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.5501641631126404, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201003793, chunk_id=201003793_chunk_745, recipe_name=罗宋汤, category=汤类, score=0.5707922577857971, search_type=vector_enhanced

```text
## 所需食材
1. 包菜(200g)
2. 植物油(5mL)
3. 橄榄油(5mL)
4. 欧芹(100g)
5. 洋葱(100g)
6. 牛肉(250g)
7. 牛肉高汤(500mL)
8. 番茄罐头(2罐)
9. 番茄膏(5g)
10. 盐(18g)
11. 红肠(150g)
12. 胡萝卜(100g)
13. 马铃薯(400g)
14. 黑胡椒(3g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201004040, chunk_id=201004040_chunk_797, recipe_name=汤面, category=主食, score=0.5857701897621155, search_type=vector_enhanced

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

### result_order=9
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

### result_order=10
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

### result_order=11
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

### result_order=12
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
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.5804290771484375, search_type=vector_enhanced

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

### result_order=1
source: top_k_final
metadata_summary: node_id=201005528, chunk_id=201005528_chunk_1096, recipe_name=糖拌西红柿, category=素菜, score=0.6169561147689819, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀将西红柿皮米字型划开
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 用筷子插入西红柿的菊花，在燃气上转动烤 10 秒（或用开水冲 30 秒），直到西红柿皮卷边
方法: 烤,烫
工具: 筷子,燃气,开水
时间: 10-30秒

### 第3步
步骤: 步骤3
描述: 把西红柿的衣服脱光
方法: 去皮
工具: 手

### 第4步
步骤: 步骤4
描述: 再西红柿大卸八块（沿纹路切可以更多的留汁水），去掉头部根蒂部，备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 全部切好后，将西红柿在盘子中均匀码一层
方法: 摆盘
工具: 盘子

### 第6步
步骤: 步骤6
描述: 撒上白糖，重复上面一步直到全部西红柿放完
方法: 撒
工具: 盘子

### 第7步
步骤: 步骤7
描述: 放入冰箱冷藏 10 分钟
方法: 冷藏
工具: 冰箱
时间: 10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_628, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.546129047870636, search_type=vector_enhanced

```text
## 所需食材
1. 八角(0.5个)
2. 土豆(3个)
3. 姜(4片)
4. 料酒(35毫升)
5. 油(15毫升)
6. 洋葱(1个)
7. 牛肉(600克)
8. 白糖
9. 老抽
10. 花椒(3克)
11. 葱(1根)
12. 西红柿(3个)
13. 酱油(15毫升)
14. 香叶(2片)
15. 黑胡椒粉(2克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.5501641631126404, search_type=vector_enhanced

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201005181, chunk_id=201005181_chunk_1028, recipe_name=西红柿炒鸡蛋, category=素菜, score=0.5804290771484375, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=1
source: generation_context
metadata_summary: node_id=201005528, chunk_id=201005528_chunk_1096, recipe_name=糖拌西红柿, category=素菜, score=0.6169561147689819, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀将西红柿皮米字型划开
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 用筷子插入西红柿的菊花，在燃气上转动烤 10 秒（或用开水冲 30 秒），直到西红柿皮卷边
方法: 烤,烫
工具: 筷子,燃气,开水
时间: 10-30秒

### 第3步
步骤: 步骤3
描述: 把西红柿的衣服脱光
方法: 去皮
工具: 手

### 第4步
步骤: 步骤4
描述: 再西红柿大卸八块（沿纹路切可以更多的留汁水），去掉头部根蒂部，备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 全部切好后，将西红柿在盘子中均匀码一层
方法: 摆盘
工具: 盘子

### 第6步
步骤: 步骤6
描述: 撒上白糖，重复上面一步直到全部西红柿放完
方法: 撒
工具: 盘子

### 第7步
步骤: 步骤7
描述: 放入冰箱冷藏 10 分钟
方法: 冷藏
工具: 冰箱
时间: 10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201003196, chunk_id=201003196_chunk_628, recipe_name=西红柿土豆炖牛肉, category=荤菜, score=0.546129047870636, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 八角(0.5个)
2. 土豆(3个)
3. 姜(4片)
4. 料酒(35毫升)
5. 油(15毫升)
6. 洋葱(1个)
7. 牛肉(600克)
8. 白糖
9. 老抽
10. 花椒(3克)
11. 葱(1根)
12. 西红柿(3个)
13. 酱油(15毫升)
14. 香叶(2片)
15. 黑胡椒粉(2克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201003210, recipe_name=西红柿, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 西红柿
食材名称: 西红柿
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=4
source: generation_context
metadata_summary: node_id=201003726, chunk_id=201003726_chunk_729, recipe_name=番茄牛肉蛋花汤, category=汤类, score=0.5501641631126404, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 所需食材
1. 姜(适量片)
2. 牛肉(150g)
3. 番茄(1个)
4. 盐(2g)
5. 胡椒粉(0.5g)
6. 葱(适量根)
7. 蒜(适量瓣)
8. 鸡蛋(1个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

