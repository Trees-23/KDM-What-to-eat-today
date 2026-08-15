# Recall Content

audit_id: 20260811_173002_465_93305a07
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
metadata_summary: node_id=201004841, recipe_name=凉拌豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 凉拌豆腐
菜品名称: 凉拌豆腐
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
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
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.6226478815078735, search_type=vector_enhanced

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

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201005112, chunk_id=201005112_chunk_1013, recipe_name=葱煎豆腐, category=素菜, score=0.5987547039985657, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐洗净，切成约5 mm厚片，置于碟中备用。
方法: 切
工具: 刀,碟子
时间: 2-3分钟

### 第2步
步骤: 步骤2
描述: 葱洗净，去根后切成葱花备用。
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 青辣椒洗净，切开去籽后切成1 cm×1 cm小块备用。
方法: 切
工具: 刀,案板
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 平底锅加热，倒入9 ml食用油，使油均匀铺满锅底。
方法: 加热
工具: 平底锅
时间: 30秒

### 第5步
步骤: 步骤5
描述: 均匀放入豆腐片，小火煎至一面金黄后翻面继续煎至两面金黄。
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将煎好的豆腐盛出备用。
方法: 盛出
工具: 锅铲,碟子
时间: 10秒

### 第7步
步骤: 步骤7
描述: 补油至覆盖锅底，倒入辣椒块，大火翻炒并用锅铲碾压3分钟。
方法: 炒,碾压
工具: 锅铲,平底锅
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 倒入煎好的豆腐，加入盐与鸡精，中火翻炒1分钟后加入10 ml水，大火收汁。
方法: 炒,收汁
工具: 锅铲,平底锅
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 出锅前撒上葱花，起锅盛盘即可。
方法: 撒,盛盘
工具: 锅铲,盘子
时间: 20秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201005212, chunk_id=201005212_chunk_1034, recipe_name=金针菇日本豆腐煲, category=素菜, score=0.5964180827140808, search_type=vector_enhanced

```text
# 金针菇日本豆腐煲
难度: 2.0星

时间信息: 准备时间: 5-10分钟, 烹饪时间: 10-15分钟
份量: 1人份

## 所需食材
1. 小米椒(3-5根)
2. 日本豆腐(2袋)
3. 水(100毫升)
4. 生抽(15毫升)
5. 糖(3克)
6. 老抽(3毫升)
7. 蒜(2-3瓣)
8. 蚝油(5毫升)
9. 金针菇(1-2把)
10. 食用油(10-15毫升)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐切片，小火煎到两面金黄出锅备用。
方法: 切,煎
工具: 刀,平底锅,锅铲
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 切蒜成蒜末；将生抽、蚝油、老抽、糖、100ml水调汁备用。
方法: 切,调汁
工具: 刀,案板,小碗
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 热锅放油，油热放小米椒、蒜末爆香，先放金针菇，炒软，把煎好的豆腐平铺在金针菇上，倒入步骤2配好的料汁，焖5分钟，大火收汁。
方法: 炒,焖,收汁
工具: 炒锅,锅铲
时间: 8-10分钟

## 标签
金针菇一定要先炒软,豆腐尽量不要翻炒，容易碎
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_959, recipe_name=凉拌豆腐, category=素菜, score=0.5945385694503784, search_type=vector_enhanced

```text
## 标签
选用北豆腐或老豆腐口感更佳,可省略醋和辣椒油以清淡口味,酱汁比例可调
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201005074, chunk_id=201005074_chunk_1006, recipe_name=脆皮豆腐, category=素菜, score=0.5843358635902405, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡蛋搅拌形成蛋液放置备用
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 配置酱料：20 g 生抽+10 g 蚝油+5 g 老抽+10 g 白糖+10 g 玉米淀粉+200 ml 清水，搅拌均匀
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 老豆腐切片，每块豆腐切5片，厚度约1.2 cm
方法: 切
工具: 刀,案板
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 玉米淀粉倒入盘中，将老豆腐片先粘上淀粉，再粘上蛋液，放置一旁备用
方法: 裹粉
工具: 盘,筷子
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 热锅，倒入18 ml食用油，等待10秒让油温升高
方法: 热锅
工具: 平底锅
时间: 10秒

### 第6步
步骤: 步骤6
描述: 将裹好蛋液的老豆腐片均匀放入锅中，小火煎至一面金黄后翻面
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 待两面均煎至金黄后，倒入调好的酱料，让每块豆腐都裹满酱汁，大火煮3分钟至酱汁浓稠
方法: 煮,收汁
工具: 平底锅,锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 关火，出锅装盘
方法: 关火
工具: 锅铲
时间: 10秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5835245847702026, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.5833241939544678, search_type=vector_enhanced

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

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201005112, chunk_id=201005112_chunk_1012, recipe_name=葱煎豆腐, category=素菜, score=0.5784730911254883, search_type=vector_enhanced

```text
## 所需食材
1. 水(10毫升)
2. 白豆腐(0.8块)
3. 盐(3克)
4. 葱(0.67根)
5. 青辣椒(0.5只)
6. 食用油(9毫升)
7. 鸡精(1.5克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_684, recipe_name=麻婆豆腐, category=荤菜, score=0.5732986330986023, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大蒜和生姜切碎，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 小米辣切成辣椒圈，备用
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 五花肉切成肉糜（本来就是买的肉糜的跳过）
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 肉糜中加入一半的食盐和味极鲜酱油，搅拌均匀，备用
方法: 腌制,搅拌
工具: 盆,筷子

### 第5步
步骤: 步骤5
描述: 鸭蛋用菜刀竖着对半切开（注意安全），去除蛋黄（一定要去除，不然会腥），剩下的蛋白捣碎成大约 2 mm * 2 mm 大小，不用太碎，备用
方法: 切,捣碎
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 打开豆腐包装，用水果刀将在盒子中的豆腐划成大约 2.5 cm * 3 cm 大小，备用
方法: 切
工具: 水果刀

### 第7步
步骤: 步骤7
描述: 热锅，锅内放入 10ml - 15ml 食用油。等待 10 秒让油温升高
方法: 加热
工具: 炒锅
时间: 10秒

### 第8步
步骤: 步骤8
描述: 调成小火，放入大蒜、生姜、辣椒圈、花椒、咸鸭蛋、蒜蓉辣酱翻炒 20 秒，炒出香味
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第9步
步骤: 步骤9
描述: 调成中火，放入肉糜，翻炒大约 1 分钟，肉炒变色
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 调成小火，放入豆腐，将剩下的食盐、味极鲜酱油酱油均匀的洒在豆腐上
方法: 调味
工具: 锅铲

### 第11步
步骤: 步骤11
描述: 从锅边倒入开水（不然豆腐容易破），没过豆腐即可
方法: 煮
工具: 锅铲

### 第12步
步骤: 步骤12
描述: 开大火，水沸腾后立马转入中火，等待大约 10 分钟
方法: 煮,炖
工具: 炒锅
时间: 10分钟

### 第13步
步骤: 步骤13
描述: 等到水只剩 1/5 并且豆腐表面已经入色，关火，盛盘
方法: 收汁,装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201002224, chunk_id=201002224_chunk_460, recipe_name=卤菜, category=荤菜, score=0.5677323341369629, search_type=vector_enhanced

```text
## 所需食材
1. 南腐乳(15ml)
2. 卤料包(1包)
3. 啤酒(330ml)
4. 大蒜(40g)
5. 干辣椒(10g)
6. 洋葱(100g)
7. 清水(足量ml)
8. 牛腱子(500g)
9. 生姜(30g)
10. 生抽(120ml)
11. 白糖(30g)
12. 盐(10-15g)
13. 老抽(60ml)
14. 蚝油(15ml)
15. 豆瓣酱(15ml)
16. 黄豆酱(15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
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
metadata_summary: node_id=201004841, recipe_name=凉拌豆腐, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 凉拌豆腐
菜品名称: 凉拌豆腐
分类: 素菜
难度: 2.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
```

### result_order=3
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

### result_order=4
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

### result_order=5
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

### result_order=6
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

### result_order=7
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

### result_order=8
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

### result_order=9
source: branch_grouped
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.6226478815078735, search_type=vector_enhanced

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

### result_order=10
source: branch_grouped
metadata_summary: node_id=201005112, chunk_id=201005112_chunk_1013, recipe_name=葱煎豆腐, category=素菜, score=0.5987547039985657, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐洗净，切成约5 mm厚片，置于碟中备用。
方法: 切
工具: 刀,碟子
时间: 2-3分钟

### 第2步
步骤: 步骤2
描述: 葱洗净，去根后切成葱花备用。
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 青辣椒洗净，切开去籽后切成1 cm×1 cm小块备用。
方法: 切
工具: 刀,案板
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 平底锅加热，倒入9 ml食用油，使油均匀铺满锅底。
方法: 加热
工具: 平底锅
时间: 30秒

### 第5步
步骤: 步骤5
描述: 均匀放入豆腐片，小火煎至一面金黄后翻面继续煎至两面金黄。
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将煎好的豆腐盛出备用。
方法: 盛出
工具: 锅铲,碟子
时间: 10秒

### 第7步
步骤: 步骤7
描述: 补油至覆盖锅底，倒入辣椒块，大火翻炒并用锅铲碾压3分钟。
方法: 炒,碾压
工具: 锅铲,平底锅
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 倒入煎好的豆腐，加入盐与鸡精，中火翻炒1分钟后加入10 ml水，大火收汁。
方法: 炒,收汁
工具: 锅铲,平底锅
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 出锅前撒上葱花，起锅盛盘即可。
方法: 撒,盛盘
工具: 锅铲,盘子
时间: 20秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201005212, chunk_id=201005212_chunk_1034, recipe_name=金针菇日本豆腐煲, category=素菜, score=0.5964180827140808, search_type=vector_enhanced

```text
# 金针菇日本豆腐煲
难度: 2.0星

时间信息: 准备时间: 5-10分钟, 烹饪时间: 10-15分钟
份量: 1人份

## 所需食材
1. 小米椒(3-5根)
2. 日本豆腐(2袋)
3. 水(100毫升)
4. 生抽(15毫升)
5. 糖(3克)
6. 老抽(3毫升)
7. 蒜(2-3瓣)
8. 蚝油(5毫升)
9. 金针菇(1-2把)
10. 食用油(10-15毫升)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐切片，小火煎到两面金黄出锅备用。
方法: 切,煎
工具: 刀,平底锅,锅铲
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 切蒜成蒜末；将生抽、蚝油、老抽、糖、100ml水调汁备用。
方法: 切,调汁
工具: 刀,案板,小碗
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 热锅放油，油热放小米椒、蒜末爆香，先放金针菇，炒软，把煎好的豆腐平铺在金针菇上，倒入步骤2配好的料汁，焖5分钟，大火收汁。
方法: 炒,焖,收汁
工具: 炒锅,锅铲
时间: 8-10分钟

## 标签
金针菇一定要先炒软,豆腐尽量不要翻炒，容易碎
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_959, recipe_name=凉拌豆腐, category=素菜, score=0.5945385694503784, search_type=vector_enhanced

```text
## 标签
选用北豆腐或老豆腐口感更佳,可省略醋和辣椒油以清淡口味,酱汁比例可调
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=13
source: branch_grouped
metadata_summary: node_id=201005074, chunk_id=201005074_chunk_1006, recipe_name=脆皮豆腐, category=素菜, score=0.5843358635902405, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡蛋搅拌形成蛋液放置备用
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 配置酱料：20 g 生抽+10 g 蚝油+5 g 老抽+10 g 白糖+10 g 玉米淀粉+200 ml 清水，搅拌均匀
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 老豆腐切片，每块豆腐切5片，厚度约1.2 cm
方法: 切
工具: 刀,案板
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 玉米淀粉倒入盘中，将老豆腐片先粘上淀粉，再粘上蛋液，放置一旁备用
方法: 裹粉
工具: 盘,筷子
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 热锅，倒入18 ml食用油，等待10秒让油温升高
方法: 热锅
工具: 平底锅
时间: 10秒

### 第6步
步骤: 步骤6
描述: 将裹好蛋液的老豆腐片均匀放入锅中，小火煎至一面金黄后翻面
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 待两面均煎至金黄后，倒入调好的酱料，让每块豆腐都裹满酱汁，大火煮3分钟至酱汁浓稠
方法: 煮,收汁
工具: 平底锅,锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 关火，出锅装盘
方法: 关火
工具: 锅铲
时间: 10秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5835245847702026, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_683, recipe_name=麻婆豆腐, category=荤菜, score=0.5833241939544678, search_type=vector_enhanced

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

### result_order=16
source: branch_grouped
metadata_summary: node_id=201005112, chunk_id=201005112_chunk_1012, recipe_name=葱煎豆腐, category=素菜, score=0.5784730911254883, search_type=vector_enhanced

```text
## 所需食材
1. 水(10毫升)
2. 白豆腐(0.8块)
3. 盐(3克)
4. 葱(0.67根)
5. 青辣椒(0.5只)
6. 食用油(9毫升)
7. 鸡精(1.5克)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=17
source: branch_grouped
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_684, recipe_name=麻婆豆腐, category=荤菜, score=0.5732986330986023, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大蒜和生姜切碎，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 小米辣切成辣椒圈，备用
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 五花肉切成肉糜（本来就是买的肉糜的跳过）
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 肉糜中加入一半的食盐和味极鲜酱油，搅拌均匀，备用
方法: 腌制,搅拌
工具: 盆,筷子

### 第5步
步骤: 步骤5
描述: 鸭蛋用菜刀竖着对半切开（注意安全），去除蛋黄（一定要去除，不然会腥），剩下的蛋白捣碎成大约 2 mm * 2 mm 大小，不用太碎，备用
方法: 切,捣碎
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 打开豆腐包装，用水果刀将在盒子中的豆腐划成大约 2.5 cm * 3 cm 大小，备用
方法: 切
工具: 水果刀

### 第7步
步骤: 步骤7
描述: 热锅，锅内放入 10ml - 15ml 食用油。等待 10 秒让油温升高
方法: 加热
工具: 炒锅
时间: 10秒

### 第8步
步骤: 步骤8
描述: 调成小火，放入大蒜、生姜、辣椒圈、花椒、咸鸭蛋、蒜蓉辣酱翻炒 20 秒，炒出香味
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第9步
步骤: 步骤9
描述: 调成中火，放入肉糜，翻炒大约 1 分钟，肉炒变色
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 调成小火，放入豆腐，将剩下的食盐、味极鲜酱油酱油均匀的洒在豆腐上
方法: 调味
工具: 锅铲

### 第11步
步骤: 步骤11
描述: 从锅边倒入开水（不然豆腐容易破），没过豆腐即可
方法: 煮
工具: 锅铲

### 第12步
步骤: 步骤12
描述: 开大火，水沸腾后立马转入中火，等待大约 10 分钟
方法: 煮,炖
工具: 炒锅
时间: 10分钟

### 第13步
步骤: 步骤13
描述: 等到水只剩 1/5 并且豆腐表面已经入色，关火，盛盘
方法: 收汁,装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=18
source: branch_grouped
metadata_summary: node_id=201002224, chunk_id=201002224_chunk_460, recipe_name=卤菜, category=荤菜, score=0.5677323341369629, search_type=vector_enhanced

```text
## 所需食材
1. 南腐乳(15ml)
2. 卤料包(1包)
3. 啤酒(330ml)
4. 大蒜(40g)
5. 干辣椒(10g)
6. 洋葱(100g)
7. 清水(足量ml)
8. 牛腱子(500g)
9. 生姜(30g)
10. 生抽(120ml)
11. 白糖(30g)
12. 盐(10-15g)
13. 老抽(60ml)
14. 蚝油(15ml)
15. 豆瓣酱(15ml)
16. 黄豆酱(15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
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
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_684, recipe_name=麻婆豆腐, category=荤菜, score=0.5732986330986023, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大蒜和生姜切碎，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 小米辣切成辣椒圈，备用
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 五花肉切成肉糜（本来就是买的肉糜的跳过）
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 肉糜中加入一半的食盐和味极鲜酱油，搅拌均匀，备用
方法: 腌制,搅拌
工具: 盆,筷子

### 第5步
步骤: 步骤5
描述: 鸭蛋用菜刀竖着对半切开（注意安全），去除蛋黄（一定要去除，不然会腥），剩下的蛋白捣碎成大约 2 mm * 2 mm 大小，不用太碎，备用
方法: 切,捣碎
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 打开豆腐包装，用水果刀将在盒子中的豆腐划成大约 2.5 cm * 3 cm 大小，备用
方法: 切
工具: 水果刀

### 第7步
步骤: 步骤7
描述: 热锅，锅内放入 10ml - 15ml 食用油。等待 10 秒让油温升高
方法: 加热
工具: 炒锅
时间: 10秒

### 第8步
步骤: 步骤8
描述: 调成小火，放入大蒜、生姜、辣椒圈、花椒、咸鸭蛋、蒜蓉辣酱翻炒 20 秒，炒出香味
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第9步
步骤: 步骤9
描述: 调成中火，放入肉糜，翻炒大约 1 分钟，肉炒变色
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 调成小火，放入豆腐，将剩下的食盐、味极鲜酱油酱油均匀的洒在豆腐上
方法: 调味
工具: 锅铲

### 第11步
步骤: 步骤11
描述: 从锅边倒入开水（不然豆腐容易破），没过豆腐即可
方法: 煮
工具: 锅铲

### 第12步
步骤: 步骤12
描述: 开大火，水沸腾后立马转入中火，等待大约 10 分钟
方法: 煮,炖
工具: 炒锅
时间: 10分钟

### 第13步
步骤: 步骤13
描述: 等到水只剩 1/5 并且豆腐表面已经入色，关火，盛盘
方法: 收汁,装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.6226478815078735, search_type=vector_enhanced

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

### result_order=3
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

### result_order=4
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

### result_order=5
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

### result_order=6
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

### result_order=7
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

### result_order=8
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

### result_order=9
source: merged_candidates
metadata_summary: node_id=201005112, chunk_id=201005112_chunk_1013, recipe_name=葱煎豆腐, category=素菜, score=0.5987547039985657, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐洗净，切成约5 mm厚片，置于碟中备用。
方法: 切
工具: 刀,碟子
时间: 2-3分钟

### 第2步
步骤: 步骤2
描述: 葱洗净，去根后切成葱花备用。
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 青辣椒洗净，切开去籽后切成1 cm×1 cm小块备用。
方法: 切
工具: 刀,案板
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 平底锅加热，倒入9 ml食用油，使油均匀铺满锅底。
方法: 加热
工具: 平底锅
时间: 30秒

### 第5步
步骤: 步骤5
描述: 均匀放入豆腐片，小火煎至一面金黄后翻面继续煎至两面金黄。
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将煎好的豆腐盛出备用。
方法: 盛出
工具: 锅铲,碟子
时间: 10秒

### 第7步
步骤: 步骤7
描述: 补油至覆盖锅底，倒入辣椒块，大火翻炒并用锅铲碾压3分钟。
方法: 炒,碾压
工具: 锅铲,平底锅
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 倒入煎好的豆腐，加入盐与鸡精，中火翻炒1分钟后加入10 ml水，大火收汁。
方法: 炒,收汁
工具: 锅铲,平底锅
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 出锅前撒上葱花，起锅盛盘即可。
方法: 撒,盛盘
工具: 锅铲,盘子
时间: 20秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201005212, chunk_id=201005212_chunk_1034, recipe_name=金针菇日本豆腐煲, category=素菜, score=0.5964180827140808, search_type=vector_enhanced

```text
# 金针菇日本豆腐煲
难度: 2.0星

时间信息: 准备时间: 5-10分钟, 烹饪时间: 10-15分钟
份量: 1人份

## 所需食材
1. 小米椒(3-5根)
2. 日本豆腐(2袋)
3. 水(100毫升)
4. 生抽(15毫升)
5. 糖(3克)
6. 老抽(3毫升)
7. 蒜(2-3瓣)
8. 蚝油(5毫升)
9. 金针菇(1-2把)
10. 食用油(10-15毫升)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐切片，小火煎到两面金黄出锅备用。
方法: 切,煎
工具: 刀,平底锅,锅铲
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 切蒜成蒜末；将生抽、蚝油、老抽、糖、100ml水调汁备用。
方法: 切,调汁
工具: 刀,案板,小碗
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 热锅放油，油热放小米椒、蒜末爆香，先放金针菇，炒软，把煎好的豆腐平铺在金针菇上，倒入步骤2配好的料汁，焖5分钟，大火收汁。
方法: 炒,焖,收汁
工具: 炒锅,锅铲
时间: 8-10分钟

## 标签
金针菇一定要先炒软,豆腐尽量不要翻炒，容易碎
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201005074, chunk_id=201005074_chunk_1006, recipe_name=脆皮豆腐, category=素菜, score=0.5843358635902405, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡蛋搅拌形成蛋液放置备用
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 配置酱料：20 g 生抽+10 g 蚝油+5 g 老抽+10 g 白糖+10 g 玉米淀粉+200 ml 清水，搅拌均匀
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 老豆腐切片，每块豆腐切5片，厚度约1.2 cm
方法: 切
工具: 刀,案板
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 玉米淀粉倒入盘中，将老豆腐片先粘上淀粉，再粘上蛋液，放置一旁备用
方法: 裹粉
工具: 盘,筷子
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 热锅，倒入18 ml食用油，等待10秒让油温升高
方法: 热锅
工具: 平底锅
时间: 10秒

### 第6步
步骤: 步骤6
描述: 将裹好蛋液的老豆腐片均匀放入锅中，小火煎至一面金黄后翻面
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 待两面均煎至金黄后，倒入调好的酱料，让每块豆腐都裹满酱汁，大火煮3分钟至酱汁浓稠
方法: 煮,收汁
工具: 平底锅,锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 关火，出锅装盘
方法: 关火
工具: 锅铲
时间: 10秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5835245847702026, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=13
source: merged_candidates
metadata_summary: node_id=201002224, chunk_id=201002224_chunk_460, recipe_name=卤菜, category=荤菜, score=0.5677323341369629, search_type=vector_enhanced

```text
## 所需食材
1. 南腐乳(15ml)
2. 卤料包(1包)
3. 啤酒(330ml)
4. 大蒜(40g)
5. 干辣椒(10g)
6. 洋葱(100g)
7. 清水(足量ml)
8. 牛腱子(500g)
9. 生姜(30g)
10. 生抽(120ml)
11. 白糖(30g)
12. 盐(10-15g)
13. 老抽(60ml)
14. 蚝油(15ml)
15. 豆瓣酱(15ml)
16. 黄豆酱(15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
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
菜品: 麻婆豆腐
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大蒜和生姜切碎，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 小米辣切成辣椒圈，备用
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 五花肉切成肉糜（本来就是买的肉糜的跳过）
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 肉糜中加入一半的食盐和味极鲜酱油，搅拌均匀，备用
方法: 腌制,搅拌
工具: 盆,筷子

### 第5步
步骤: 步骤5
描述: 鸭蛋用菜刀竖着对半切开（注意安全），去除蛋黄（一定要去除，不然会腥），剩下的蛋白捣碎成大约 2 mm * 2 mm 大小，不用太碎，备用
方法: 切,捣碎
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 打开豆腐包装，用水果刀将在盒子中的豆腐划成大约 2.5 cm * 3 cm 大小，备用
方法: 切
工具: 水果刀

### 第7步
步骤: 步骤7
描述: 热锅，锅内放入 10ml - 15ml 食用油。等待 10 秒让油温升高
方法: 加热
工具: 炒锅
时间: 10秒

### 第8步
步骤: 步骤8
描述: 调成小火，放入大蒜、生姜、辣椒圈、花椒、咸鸭蛋、蒜蓉辣酱翻炒 20 秒，炒出香味
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第9步
步骤: 步骤9
描述: 调成中火，放入肉糜，翻炒大约 1 分钟，肉炒变色
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 调成小火，放入豆腐，将剩下的食盐、味极鲜酱油酱油均匀的洒在豆腐上
方法: 调味
工具: 锅铲

### 第11步
步骤: 步骤11
描述: 从锅边倒入开水（不然豆腐容易破），没过豆腐即可
方法: 煮
工具: 锅铲

### 第12步
步骤: 步骤12
描述: 开大火，水沸腾后立马转入中火，等待大约 10 分钟
方法: 煮,炖
工具: 炒锅
时间: 10分钟

### 第13步
步骤: 步骤13
描述: 等到水只剩 1/5 并且豆腐表面已经入
```

### pair_order=2
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

### pair_order=3
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

### pair_order=4
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

### pair_order=5
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

### pair_order=6
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

### pair_order=7
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

### pair_order=8
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

### pair_order=9
source: rerank_input

```text
菜品: 葱煎豆腐
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐洗净，切成约5 mm厚片，置于碟中备用。
方法: 切
工具: 刀,碟子
时间: 2-3分钟

### 第2步
步骤: 步骤2
描述: 葱洗净，去根后切成葱花备用。
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 青辣椒洗净，切开去籽后切成1 cm×1 cm小块备用。
方法: 切
工具: 刀,案板
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 平底锅加热，倒入9 ml食用油，使油均匀铺满锅底。
方法: 加热
工具: 平底锅
时间: 30秒

### 第5步
步骤: 步骤5
描述: 均匀放入豆腐片，小火煎至一面金黄后翻面继续煎至两面金黄。
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将煎好的豆腐盛出备用。
方法: 盛出
工具: 锅铲,碟子
时间: 10秒

### 第7步
步骤: 步骤7
描述: 补油至覆盖锅底，倒入辣椒块，大火翻炒并用锅铲碾压3分钟。
方法: 炒,碾压
工具: 锅铲,平底锅
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 倒入煎好的豆腐，加入盐与鸡精，中火翻炒1分钟后加入10 ml水，大火收汁。
方法: 炒,收汁
工具: 锅铲,平底锅
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 出锅前撒上葱花，起锅盛盘即可。
方法: 撒,盛盘
工具: 锅铲,盘子
时间: 20秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=10
source: rerank_input

```text
菜系: 未知
# 金针菇日本豆腐煲
难度: 2.0星

时间信息: 准备时间: 5-10分钟, 烹饪时间: 10-15分钟
份量: 1人份

## 所需食材
1. 小米椒(3-5根)
2. 日本豆腐(2袋)
3. 水(100毫升)
4. 生抽(15毫升)
5. 糖(3克)
6. 老抽(3毫升)
7. 蒜(2-3瓣)
8. 蚝油(5毫升)
9. 金针菇(1-2把)
10. 食用油(10-15毫升)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐切片，小火煎到两面金黄出锅备用。
方法: 切,煎
工具: 刀,平底锅,锅铲
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 切蒜成蒜末；将生抽、蚝油、老抽、糖、100ml水调汁备用。
方法: 切,调汁
工具: 刀,案板,小碗
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 热锅放油，油热放小米椒、蒜末爆香，先放金针菇，炒软，把煎好的豆腐平铺在金针菇上，倒入步骤2配好的料汁，焖5分钟，大火收汁。
方法: 炒,焖,收汁
工具: 炒锅,锅铲
时间: 8-10分钟

## 标签
金针菇一定要先炒软,豆腐尽量不要翻炒，容易碎
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=11
source: rerank_input

```text
菜品: 脆皮豆腐
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡蛋搅拌形成蛋液放置备用
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 配置酱料：20 g 生抽+10 g 蚝油+5 g 老抽+10 g 白糖+10 g 玉米淀粉+200 ml 清水，搅拌均匀
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 老豆腐切片，每块豆腐切5片，厚度约1.2 cm
方法: 切
工具: 刀,案板
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 玉米淀粉倒入盘中，将老豆腐片先粘上淀粉，再粘上蛋液，放置一旁备用
方法: 裹粉
工具: 盘,筷子
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 热锅，倒入18 ml食用油，等待10秒让油温升高
方法: 热锅
工具: 平底锅
时间: 10秒

### 第6步
步骤: 步骤6
描述: 将裹好蛋液的老豆腐片均匀放入锅中，小火煎至一面金黄后翻面
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 待两面均煎至金黄后，倒入调好的酱料，让每块豆腐都裹满酱汁，大火煮3分钟至酱汁浓稠
方法: 煮,收汁
工具: 平底锅,锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 关火，出锅装盘
方法: 关火
工具: 锅铲
时间: 10秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=12
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

### pair_order=13
source: rerank_input

```text
菜品: 卤菜
菜系: 未知
## 所需食材
1. 南腐乳(15ml)
2. 卤料包(1包)
3. 啤酒(330ml)
4. 大蒜(40g)
5. 干辣椒(10g)
6. 洋葱(100g)
7. 清水(足量ml)
8. 牛腱子(500g)
9. 生姜(30g)
10. 生抽(120ml)
11. 白糖(30g)
12. 盐(10-15g)
13. 老抽(60ml)
14. 蚝油(15ml)
15. 豆瓣酱(15ml)
16. 黄豆酱(15ml)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_684, recipe_name=麻婆豆腐, category=荤菜, score=0.5732986330986023, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大蒜和生姜切碎，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 小米辣切成辣椒圈，备用
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 五花肉切成肉糜（本来就是买的肉糜的跳过）
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 肉糜中加入一半的食盐和味极鲜酱油，搅拌均匀，备用
方法: 腌制,搅拌
工具: 盆,筷子

### 第5步
步骤: 步骤5
描述: 鸭蛋用菜刀竖着对半切开（注意安全），去除蛋黄（一定要去除，不然会腥），剩下的蛋白捣碎成大约 2 mm * 2 mm 大小，不用太碎，备用
方法: 切,捣碎
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 打开豆腐包装，用水果刀将在盒子中的豆腐划成大约 2.5 cm * 3 cm 大小，备用
方法: 切
工具: 水果刀

### 第7步
步骤: 步骤7
描述: 热锅，锅内放入 10ml - 15ml 食用油。等待 10 秒让油温升高
方法: 加热
工具: 炒锅
时间: 10秒

### 第8步
步骤: 步骤8
描述: 调成小火，放入大蒜、生姜、辣椒圈、花椒、咸鸭蛋、蒜蓉辣酱翻炒 20 秒，炒出香味
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第9步
步骤: 步骤9
描述: 调成中火，放入肉糜，翻炒大约 1 分钟，肉炒变色
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 调成小火，放入豆腐，将剩下的食盐、味极鲜酱油酱油均匀的洒在豆腐上
方法: 调味
工具: 锅铲

### 第11步
步骤: 步骤11
描述: 从锅边倒入开水（不然豆腐容易破），没过豆腐即可
方法: 煮
工具: 锅铲

### 第12步
步骤: 步骤12
描述: 开大火，水沸腾后立马转入中火，等待大约 10 分钟
方法: 煮,炖
工具: 炒锅
时间: 10分钟

### 第13步
步骤: 步骤13
描述: 等到水只剩 1/5 并且豆腐表面已经入色，关火，盛盘
方法: 收汁,装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.6226478815078735, search_type=vector_enhanced

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

### result_order=2
source: reranked_results
metadata_summary: node_id=201005112, chunk_id=201005112_chunk_1013, recipe_name=葱煎豆腐, category=素菜, score=0.5987547039985657, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐洗净，切成约5 mm厚片，置于碟中备用。
方法: 切
工具: 刀,碟子
时间: 2-3分钟

### 第2步
步骤: 步骤2
描述: 葱洗净，去根后切成葱花备用。
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 青辣椒洗净，切开去籽后切成1 cm×1 cm小块备用。
方法: 切
工具: 刀,案板
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 平底锅加热，倒入9 ml食用油，使油均匀铺满锅底。
方法: 加热
工具: 平底锅
时间: 30秒

### 第5步
步骤: 步骤5
描述: 均匀放入豆腐片，小火煎至一面金黄后翻面继续煎至两面金黄。
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将煎好的豆腐盛出备用。
方法: 盛出
工具: 锅铲,碟子
时间: 10秒

### 第7步
步骤: 步骤7
描述: 补油至覆盖锅底，倒入辣椒块，大火翻炒并用锅铲碾压3分钟。
方法: 炒,碾压
工具: 锅铲,平底锅
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 倒入煎好的豆腐，加入盐与鸡精，中火翻炒1分钟后加入10 ml水，大火收汁。
方法: 炒,收汁
工具: 锅铲,平底锅
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 出锅前撒上葱花，起锅盛盘即可。
方法: 撒,盛盘
工具: 锅铲,盘子
时间: 20秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201005212, chunk_id=201005212_chunk_1034, recipe_name=金针菇日本豆腐煲, category=素菜, score=0.5964180827140808, search_type=vector_enhanced

```text
# 金针菇日本豆腐煲
难度: 2.0星

时间信息: 准备时间: 5-10分钟, 烹饪时间: 10-15分钟
份量: 1人份

## 所需食材
1. 小米椒(3-5根)
2. 日本豆腐(2袋)
3. 水(100毫升)
4. 生抽(15毫升)
5. 糖(3克)
6. 老抽(3毫升)
7. 蒜(2-3瓣)
8. 蚝油(5毫升)
9. 金针菇(1-2把)
10. 食用油(10-15毫升)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐切片，小火煎到两面金黄出锅备用。
方法: 切,煎
工具: 刀,平底锅,锅铲
时间: 3-5分钟

### 第2步
步骤: 步骤2
描述: 切蒜成蒜末；将生抽、蚝油、老抽、糖、100ml水调汁备用。
方法: 切,调汁
工具: 刀,案板,小碗
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 热锅放油，油热放小米椒、蒜末爆香，先放金针菇，炒软，把煎好的豆腐平铺在金针菇上，倒入步骤2配好的料汁，焖5分钟，大火收汁。
方法: 炒,焖,收汁
工具: 炒锅,锅铲
时间: 8-10分钟

## 标签
金针菇一定要先炒软,豆腐尽量不要翻炒，容易碎
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201005074, chunk_id=201005074_chunk_1006, recipe_name=脆皮豆腐, category=素菜, score=0.5843358635902405, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡蛋搅拌形成蛋液放置备用
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第2步
步骤: 步骤2
描述: 配置酱料：20 g 生抽+10 g 蚝油+5 g 老抽+10 g 白糖+10 g 玉米淀粉+200 ml 清水，搅拌均匀
方法: 搅拌
工具: 碗,筷子
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 老豆腐切片，每块豆腐切5片，厚度约1.2 cm
方法: 切
工具: 刀,案板
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 玉米淀粉倒入盘中，将老豆腐片先粘上淀粉，再粘上蛋液，放置一旁备用
方法: 裹粉
工具: 盘,筷子
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 热锅，倒入18 ml食用油，等待10秒让油温升高
方法: 热锅
工具: 平底锅
时间: 10秒

### 第6步
步骤: 步骤6
描述: 将裹好蛋液的老豆腐片均匀放入锅中，小火煎至一面金黄后翻面
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 待两面均煎至金黄后，倒入调好的酱料，让每块豆腐都裹满酱汁，大火煮3分钟至酱汁浓稠
方法: 煮,收汁
工具: 平底锅,锅铲
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 关火，出锅装盘
方法: 关火
工具: 锅铲
时间: 10秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5835245847702026, search_type=vector_enhanced

```text
## 标签
可根据个人口味添加豆腐干等配料,注意煎制时火候，避免外焦内生
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
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

### result_order=7
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

### result_order=8
source: reranked_results
metadata_summary: node_id=201002224, chunk_id=201002224_chunk_460, recipe_name=卤菜, category=荤菜, score=0.5677323341369629, search_type=vector_enhanced

```text
## 所需食材
1. 南腐乳(15ml)
2. 卤料包(1包)
3. 啤酒(330ml)
4. 大蒜(40g)
5. 干辣椒(10g)
6. 洋葱(100g)
7. 清水(足量ml)
8. 牛腱子(500g)
9. 生姜(30g)
10. 生抽(120ml)
11. 白糖(30g)
12. 盐(10-15g)
13. 老抽(60ml)
14. 蚝油(15ml)
15. 豆瓣酱(15ml)
16. 黄豆酱(15ml)

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

### result_order=12
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
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_684, recipe_name=麻婆豆腐, category=荤菜, score=0.5732986330986023, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大蒜和生姜切碎，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 小米辣切成辣椒圈，备用
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 五花肉切成肉糜（本来就是买的肉糜的跳过）
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 肉糜中加入一半的食盐和味极鲜酱油，搅拌均匀，备用
方法: 腌制,搅拌
工具: 盆,筷子

### 第5步
步骤: 步骤5
描述: 鸭蛋用菜刀竖着对半切开（注意安全），去除蛋黄（一定要去除，不然会腥），剩下的蛋白捣碎成大约 2 mm * 2 mm 大小，不用太碎，备用
方法: 切,捣碎
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 打开豆腐包装，用水果刀将在盒子中的豆腐划成大约 2.5 cm * 3 cm 大小，备用
方法: 切
工具: 水果刀

### 第7步
步骤: 步骤7
描述: 热锅，锅内放入 10ml - 15ml 食用油。等待 10 秒让油温升高
方法: 加热
工具: 炒锅
时间: 10秒

### 第8步
步骤: 步骤8
描述: 调成小火，放入大蒜、生姜、辣椒圈、花椒、咸鸭蛋、蒜蓉辣酱翻炒 20 秒，炒出香味
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第9步
步骤: 步骤9
描述: 调成中火，放入肉糜，翻炒大约 1 分钟，肉炒变色
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 调成小火，放入豆腐，将剩下的食盐、味极鲜酱油酱油均匀的洒在豆腐上
方法: 调味
工具: 锅铲

### 第11步
步骤: 步骤11
描述: 从锅边倒入开水（不然豆腐容易破），没过豆腐即可
方法: 煮
工具: 锅铲

### 第12步
步骤: 步骤12
描述: 开大火，水沸腾后立马转入中火，等待大约 10 分钟
方法: 煮,炖
工具: 炒锅
时间: 10分钟

### 第13步
步骤: 步骤13
描述: 等到水只剩 1/5 并且豆腐表面已经入色，关火，盛盘
方法: 收汁,装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.6226478815078735, search_type=vector_enhanced

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

### result_order=2
source: top_k_final
metadata_summary: node_id=201005112, chunk_id=201005112_chunk_1013, recipe_name=葱煎豆腐, category=素菜, score=0.5987547039985657, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐洗净，切成约5 mm厚片，置于碟中备用。
方法: 切
工具: 刀,碟子
时间: 2-3分钟

### 第2步
步骤: 步骤2
描述: 葱洗净，去根后切成葱花备用。
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 青辣椒洗净，切开去籽后切成1 cm×1 cm小块备用。
方法: 切
工具: 刀,案板
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 平底锅加热，倒入9 ml食用油，使油均匀铺满锅底。
方法: 加热
工具: 平底锅
时间: 30秒

### 第5步
步骤: 步骤5
描述: 均匀放入豆腐片，小火煎至一面金黄后翻面继续煎至两面金黄。
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将煎好的豆腐盛出备用。
方法: 盛出
工具: 锅铲,碟子
时间: 10秒

### 第7步
步骤: 步骤7
描述: 补油至覆盖锅底，倒入辣椒块，大火翻炒并用锅铲碾压3分钟。
方法: 炒,碾压
工具: 锅铲,平底锅
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 倒入煎好的豆腐，加入盐与鸡精，中火翻炒1分钟后加入10 ml水，大火收汁。
方法: 炒,收汁
工具: 锅铲,平底锅
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 出锅前撒上葱花，起锅盛盘即可。
方法: 撒,盛盘
工具: 锅铲,盘子
时间: 20秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5835245847702026, search_type=vector_enhanced

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

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201003481, chunk_id=201003481_chunk_684, recipe_name=麻婆豆腐, category=荤菜, score=0.5732986330986023, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大蒜和生姜切碎，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 小米辣切成辣椒圈，备用
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 五花肉切成肉糜（本来就是买的肉糜的跳过）
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 肉糜中加入一半的食盐和味极鲜酱油，搅拌均匀，备用
方法: 腌制,搅拌
工具: 盆,筷子

### 第5步
步骤: 步骤5
描述: 鸭蛋用菜刀竖着对半切开（注意安全），去除蛋黄（一定要去除，不然会腥），剩下的蛋白捣碎成大约 2 mm * 2 mm 大小，不用太碎，备用
方法: 切,捣碎
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 打开豆腐包装，用水果刀将在盒子中的豆腐划成大约 2.5 cm * 3 cm 大小，备用
方法: 切
工具: 水果刀

### 第7步
步骤: 步骤7
描述: 热锅，锅内放入 10ml - 15ml 食用油。等待 10 秒让油温升高
方法: 加热
工具: 炒锅
时间: 10秒

### 第8步
步骤: 步骤8
描述: 调成小火，放入大蒜、生姜、辣椒圈、花椒、咸鸭蛋、蒜蓉辣酱翻炒 20 秒，炒出香味
方法: 炒
工具: 炒锅,锅铲
时间: 20秒

### 第9步
步骤: 步骤9
描述: 调成中火，放入肉糜，翻炒大约 1 分钟，肉炒变色
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 调成小火，放入豆腐，将剩下的食盐、味极鲜酱油酱油均匀的洒在豆腐上
方法: 调味
工具: 锅铲

### 第11步
步骤: 步骤11
描述: 从锅边倒入开水（不然豆腐容易破），没过豆腐即可
方法: 煮
工具: 锅铲

### 第12步
步骤: 步骤12
描述: 开大火，水沸腾后立马转入中火，等待大约 10 分钟
方法: 煮,炖
工具: 炒锅
时间: 10分钟

### 第13步
步骤: 步骤13
描述: 等到水只剩 1/5 并且豆腐表面已经入色，关火，盛盘
方法: 收汁,装盘
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201004841, chunk_id=201004841_chunk_958, recipe_name=凉拌豆腐, category=素菜, score=0.6226478815078735, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=2
source: generation_context
metadata_summary: node_id=201005112, chunk_id=201005112_chunk_1013, recipe_name=葱煎豆腐, category=素菜, score=0.5987547039985657, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 豆腐洗净，切成约5 mm厚片，置于碟中备用。
方法: 切
工具: 刀,碟子
时间: 2-3分钟

### 第2步
步骤: 步骤2
描述: 葱洗净，去根后切成葱花备用。
方法: 切
工具: 刀,案板
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 青辣椒洗净，切开去籽后切成1 cm×1 cm小块备用。
方法: 切
工具: 刀,案板
时间: 1-2分钟

### 第4步
步骤: 步骤4
描述: 平底锅加热，倒入9 ml食用油，使油均匀铺满锅底。
方法: 加热
工具: 平底锅
时间: 30秒

### 第5步
步骤: 步骤5
描述: 均匀放入豆腐片，小火煎至一面金黄后翻面继续煎至两面金黄。
方法: 煎
工具: 平底锅,锅铲
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 将煎好的豆腐盛出备用。
方法: 盛出
工具: 锅铲,碟子
时间: 10秒

### 第7步
步骤: 步骤7
描述: 补油至覆盖锅底，倒入辣椒块，大火翻炒并用锅铲碾压3分钟。
方法: 炒,碾压
工具: 锅铲,平底锅
时间: 3分钟

### 第8步
步骤: 步骤8
描述: 倒入煎好的豆腐，加入盐与鸡精，中火翻炒1分钟后加入10 ml水，大火收汁。
方法: 炒,收汁
工具: 锅铲,平底锅
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 出锅前撒上葱花，起锅盛盘即可。
方法: 撒,盛盘
工具: 锅铲,盘子
时间: 20秒
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201004341, chunk_id=201004341_chunk_863, recipe_name=韭菜盒子, category=主食, score=0.5835245847702026, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

