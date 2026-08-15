# Recall Content

audit_id: 20260811_161505_629_47002ecd
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201000257, recipe_name=清蒸鲈鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 清蒸鲈鱼
菜品名称: 清蒸鲈鱼
分类: 水产
菜系: 粤菜
难度: 3.0
关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
```

### result_order=1
source: entity_level
metadata_summary: node_id=201000258, recipe_name=鲈鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲈鱼
食材名称: 鲈鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201000027, recipe_name=姜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 姜
食材名称: 姜
类别: 蔬菜
关联图谱:
- IN REQUIRES 香煎五花肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 地三鲜 (Recipe): category: 素菜；cuisineType: 东北菜；difficulty: 3.0
```

### result_order=3
source: entity_level
metadata_summary: node_id=201000062, recipe_name=葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 葱
食材名称: 葱
类别: 蔬菜
关联图谱:
- IN REQUIRES 清蒸生蚝 (Recipe): category: 水产；difficulty: 3.0
- IN REQUIRES 素炒豆角 (Recipe): category: 素菜；difficulty: 2.0
```

### result_order=4
source: entity_level
metadata_summary: node_id=201000262, recipe_name=蒸鱼豉油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸鱼豉油
食材名称: 蒸鱼豉油
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=5
source: entity_level
metadata_summary: node_id=201000009, recipe_name=食用油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 食用油
食材名称: 食用油
类别: 调料
关联图谱:
- IN REQUIRES 鲤鱼炖白菜 (Recipe): category: 水产；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 青椒土豆炒肉 (Recipe): category: 荤菜；difficulty: 3.0
```

### result_order=6
source: entity_level
metadata_summary: node_id=tipdoc_9e62e8f43239, recipe_name=蒸, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧文档: 蒸
分类: 烹饪技巧
标签: 学习蒸,方式,正文,注意事项,蒸,蒸锅,铁锅
摘要: 蒸 方式 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热 铁锅 如果没有蒸锅，只有普通的铁锅 非平底锅 ，可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。 铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
来源: tips/learn/学习蒸.md

补充信息: 技巧章节: 蒸
章节: 正文
分类: 烹饪技巧
摘要: 蒸
内容: # 蒸
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=7
source: entity_level
metadata_summary: node_id=tipchunk_6ce348d11822, recipe_name=蒸 / 方式, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 方式
章节: 方式
分类: 烹饪技巧
摘要: 方式
内容: ## 方式
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=8
source: entity_level
metadata_summary: node_id=tipchunk_9f97843cc8b2, recipe_name=蒸 / 注意事项, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 注意事项
章节: 注意事项
分类: 烹饪技巧
摘要: 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
内容: ## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=9
source: entity_level
metadata_summary: node_id=tipchunk_a06f1b706233, recipe_name=蒸 / 蒸锅, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 蒸锅
章节: 蒸锅
分类: 烹饪技巧
摘要: 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
内容: ### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201000519, recipe_name=太阳蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=1
source: topic_level
metadata_summary: node_id=201004928, recipe_name=松仁玉米, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 松仁玉米
分类: 素菜
难度: 2.0
主要食材: 白砂糖, 淀粉, 熟松子仁
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
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
metadata_summary: node_id=201000257, recipe_name=清蒸鲈鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 清蒸鲈鱼
分类: 水产
菜系: 粤菜
难度: 3.0
主要食材: 香葱, 鲈鱼, 食用盐
关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=4
source: topic_level
metadata_summary: node_id=201004117, recipe_name=炒馍, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 炒馍
分类: 主食
菜系: 西北菜
难度: 3.0
主要食材: 辣椒粉, 五香粉, 孜然粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=5
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

### result_order=6
source: topic_level
metadata_summary: node_id=201004341, recipe_name=韭菜盒子, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: topic_level
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 海鲜
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

### result_order=8
source: topic_level
metadata_summary: node_id=201004506, recipe_name=披萨饼皮, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 披萨饼皮
分类: 主食
难度: 4.0
主要食材: 中筋面粉, 食用盐, 橄榄油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=9
source: topic_level
metadata_summary: node_id=201004544, recipe_name=日式肥牛丼饭, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 去腥
菜品: 日式肥牛丼饭
分类: 主食
菜系: 日式
难度: 4.0
主要食材: 味淋, 酱油, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.7811521887779236, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片切丝、香葱的葱白切段，葱绿切丝，切丝后放入冷水浸泡备用。
方法: 切
工具: 刀,案板,冷水碗
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鲈鱼处理好后洗净，用厨房纸擦干，两面分别划几刀，用盐洗掉鱼身的粘液，并用10g盐抹遍鱼身的内外，腌制10分钟以上。
方法: 洗,腌制,切
工具: 厨房纸,刀,案板,盆
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼肚内塞上姜和葱白，鱼身也撒上姜和葱白，量为备用的一半。蒸鱼的碟子用筷子将鱼跟碟子隔开蒸。
方法: 摆盘
工具: 碟子,筷子
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 水烧热感觉到水温后放进入鱼，大火清蒸10分钟。
方法: 蒸
工具: 蒸锅,大火
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 蒸好的鱼，用干净的盘子装起来并去除身上姜蒜。
方法: 装盘
工具: 干净盘子,筷子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 鱼身浇上15ml蒸鱼豉油。
方法: 浇汁
工具: 量勺
时间: 15秒

### 第7步
步骤: 步骤7
描述: 鱼身重新撒上姜和葱丝，锅内加上10ml食用油并烧热，将食用油淋至鱼身即可出菜。
方法: 淋油
工具: 锅,量勺,锅铲
时间: 30秒

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_44, recipe_name=清蒸鲈鱼, category=水产, score=0.7697495818138123, search_type=vector_enhanced

```text
# 清蒸鲈鱼

菜系: 粤菜
难度: 3.0星

时间信息: 准备时间: 10分钟（腌制）+ 5分钟（处理与改刀）, 烹饪时间: 10分钟（蒸）
份量: 1条鱼

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_45, recipe_name=清蒸鲈鱼, category=水产, score=0.719322144985199, search_type=vector_enhanced

```text
## 所需食材
1. 姜(1块)
2. 料酒(10-15毫升)
3. 蒸鱼豉油(10-15毫升)
4. 食用油(10-15毫升)
5. 食用盐(5-10克)
6. 香葱(3根)
7. 鲈鱼(1条)

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.7118656635284424, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼开背杀好（让卖鱼的杀好，千万不要剖腹杀鱼，切记是开背），清洗干净
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 鱼表面用盐涂抹均匀，倒入料酒约80ml、姜末20g，放入冰箱保鲜层进行腌制1-2天
方法: 腌制
工具: 盆,冰箱
时间: 1-2天

### 第3步
步骤: 步骤3
描述: 取出腌制好的鱼，用绳挂起晾晒至半干（约1-2天，具体时间需结合气温与阳光）
方法: 晾晒
工具: 绳
时间: 1-2天

### 第4步
步骤: 步骤4
描述: 食用前请将鱼用清水清洗，沥干水分（防止水遇油飞溅）
方法: 清洗
工具: 盆

### 第5步
步骤: 步骤5
描述: 开大火将锅烧热，迅速改小火，锅中放油，尽量保持整个锅表面有油，将鱼沿锅边划入锅内（先煎鱼背面）
方法: 煎
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 鱼入锅后（和翻面后），不要着急移动鱼的位置（此时容易破皮），煎约30秒后，尝试晃动锅
方法: 煎
工具: 炒锅
时间: 30秒

### 第7步
步骤: 步骤7
描述: 背面煎约1分钟后，翻面煎约1-2分钟，煎至两面金黄
方法: 煎
工具: 锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入豆瓣酱炒出香味，放入姜蒜
方法: 炒
工具: 锅铲

### 第9步
步骤: 步骤9
描述: 炒出佐料香味后，加入料酒、生抽、老抽，倒入热水，水量和鱼平齐或者少点
方法: 炒,煮
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 此时改中大火，煮5-10分钟，后放入青椒段、白糖、鸡精、十三香、陈醋
方法: 煮
工具: 锅铲
时间: 5-10分钟

### 第11步
步骤: 步骤11
描述: 改小火2-5分钟，放入葱、香菜，即可出锅
方法: 焖
工具: 锅铲
时间: 2-5分钟

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 姜沫 (Ingredient): category: 调料
- OUT REQUIRES 料酒 (Ingredient): category: 调料
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.7116531729698181, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鱼清洗干净，确保无鱼鳞等异物
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 将鱼头朝左，鱼肚朝下，右手持刀。刀竖直切下1cm，按紧鱼身往左片3-4cm，再将鱼片中间轻轻划一刀
方法: 切
工具: 菜刀,案板

### 第3步
步骤: 步骤3
描述: 将鱼放进盆里，然后将大姜切片，大葱切段，用吃奶的力气将大葱大姜里的汁水挤到盆中
方法: 切,挤汁
工具: 盆,菜刀

### 第4步
步骤: 步骤4
描述: 加入20g盐、25g料酒，给鲤鱼搓澡，涂抹均匀，腌制30分钟以上
方法: 腌制
工具: 盆
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 在干净盆中加入100g面粉、200g淀粉、180g水、5g盐，搅拌均匀后加入一个鸡蛋，再次搅匀成可拉丝面糊
方法: 搅拌
工具: 盆

### 第6步
步骤: 步骤6
描述: 等待30分钟
方法: 静置
时间: 30分钟

### 第7步
步骤: 步骤7
描述: 将鱼放在案板上，用干毛巾擦干鱼身水分，盆冲洗干净并擦干
方法: 擦干
工具: 干毛巾,盆

### 第8步
步骤: 步骤8
描述: 起锅烧油，加入约1L油，油温烧至7成热（200-240℃）
方法: 炸
工具: 锅,锅铲,笊篱

### 第9步
步骤: 步骤9
描述: 捏鱼尾，鱼头先入油锅，用勺子淋热油定型，面糊成型后整鱼入锅，用笊篱托鱼头防糊
方法: 炸
工具: 锅,锅铲,笊篱

### 第10步
步骤: 步骤10
描述: 用锅铲和笊篱配合给鱼翻身，再炸2分钟，出锅装盘
方法: 炸
工具: 锅铲,笊篱,盘子
时间: 2分钟

### 第11步
步骤: 步骤11
描述: 将锅中油倒出，锅刷干净
方法: 倒油,清洗
工具: 锅

### 第12步
步骤: 步骤12
描述: 小碗混合50g清水、40g番茄酱、20g白糖、10g白醋，搅拌均匀
方法: 搅拌
工具: 小碗

### 第13步
步骤: 步骤13
描述: 另取小碗，10g淀粉加10g水调成水淀粉
方法: 搅拌
工具: 小碗

### 第14步
步骤: 步骤14
描述: 大火烧热锅，倒入料汁，烧开后转小火，加入水淀粉边倒边搅，20秒后关火
方法: 煮,搅拌
工具: 锅,勺子
时间: 20秒

### 第15步
步骤: 步骤15
描述: 将糖醋汁均匀浇在鱼身上，撒香菜或葱花点缀即可
方法: 浇汁
工具: 勺子,盘子

关联图谱:
- OUT REQUIRES 香菜 (Ingredient): category: 蔬菜
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 番茄酱 (Ingredient): category: 调料
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6931073665618896, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜蒜切碎，干辣椒切碎，与姜蒜一起备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第2步
步骤: 步骤2
描述: 锅中加入30-50ml油，小火加热至锅热。
方法: 加热
工具: 炒锅
时间: 约30秒

### 第3步
步骤: 步骤3
描述: 将擦干水分的鱼放入锅中，小火煎至底部金黄，期间晃动锅防止粘锅。
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 翻面，重复煎另一面至金黄。
方法: 煎
工具: 锅铲
时间: 约2-3分钟

### 第5步
步骤: 步骤5
描述: 加入姜蒜辣椒碎，翻炒出香味。
方法: 炒
工具: 锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 倒入适量料酒，迅速产生大量油烟，注意安全。
方法: 炝锅
工具: 锅铲
时间: 约15秒

### 第7步
步骤: 步骤7
描述: 加入醋、白砂糖、酱油（老抽），翻炒均匀。
方法: 炒
工具: 锅铲
时间: 约15秒

### 第8步
步骤: 步骤8
描述: 加入冷水，刚好淹没鱼身，转中火，盖锅盖1分钟后翻面，再盖锅盖继续炖煮3-4分钟。
方法: 炖
工具: 炒锅,锅盖
时间: 约4-5分钟

### 第9步
步骤: 步骤9
描述: 加入盐、小米椒、蚝油、味精，盖锅盖继续炖煮并适时翻面。
方法: 炖
工具: 锅铲,锅盖
时间: 约2-3分钟

### 第10步
步骤: 步骤10
描述: 汤汁收至鱼鳍下方位置时转小火，加入香菜和葱花，盖锅盖20秒后关火。
方法: 焖
工具: 锅盖
时间: 20秒

### 第11步
步骤: 步骤11
描述: 起锅装盘。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (Ingredient): category: 调料
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201000040, chunk_id=201000040_chunk_11, recipe_name=水煮鱼, category=水产, score=0.6867295503616333, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 巴沙鱼若从冷冻柜取出，放室温自然解冻5小时，再切片处理。
方法: 解冻
时间: 5小时

### 第2步
步骤: 步骤2
描述: 将巴沙鱼撇成约5cm长、3cm宽的薄片。
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 将鱼片放入大不锈钢碗中，加入30g豆瓣酱、3g盐、10ml藤椒油、3g白胡椒粉，用手抓匀后加入5ml菜籽油封味，常温静置至少30分钟入味。
方法: 腌制
工具: 大不锈钢碗
时间: 30分钟

### 第4步
步骤: 步骤4
描述: 大蒜切成蒜末；以300g花菜、200g生菜为例，将蔬菜洗净。
方法: 切,洗
工具: 刀,盆

### 第5步
步骤: 步骤5
描述: 花菜开水锅焯水备用；生菜洗净晾干后炒熟备用（不用放油）。
方法: 焯水,炒
工具: 锅,漏勺

### 第6步
步骤: 步骤6
描述: 热锅冷油（菜籽油20ml），加入10g豆瓣酱、10g豆豉（可选）和蒜末，中火慢炒。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 加入150ml热水，水开后放入腌制好的鱼片，轻轻翻动使其散开，加入2g盐和2g糖调味，水再次沸腾即可盛盘。
方法: 煮
工具: 锅,漏勺

### 第8步
步骤: 步骤8
描述: 先将熟蔬菜盛至大碗中，再将热鱼片铺在蔬菜上，浇上锅中剩余热汤即可。
方法: 盛盘
工具: 大碗

关联图谱:
- OUT REQUIRES 巴沙鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 蔬菜（土豆片/豆芽/花菜/生菜等） (Ingredient): category: 蔬菜
- OUT REQUIRES 红油豆瓣酱 (Ingredient): category: 调料
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6865550875663757, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 草鱼从背部切开，两面沿背部划几刀，不要划破鱼肚；用热水或刷子洗净表面粘液。
方法: 切,清洗
工具: 刀,刷子
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 鱼放入容器，加料酒、白胡椒粉、食盐抹匀，腌制二十分钟入味。
方法: 腌制
工具: 容器
时间: 20分钟

### 第3步
步骤: 步骤3
描述: 大葱切块，大蒜粒对半切，与八角、香叶、桂皮放同一容器；干辣椒段、灯笼椒切段放另一容器；芹菜切段；豆芽、千张焯水，千张切丝；洋葱切丝。
方法: 切,焯水
工具: 刀,案板,锅,漏勺
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 烤箱版：烤盘刷底油，鱼皮朝下烤至两面金黄，撒孜然粉。无烤箱版：热锅热油，锅边撒少量盐防粘，下鱼煎至两面金黄，撒孜然粉后出锅装盘。
方法: 烤,煎
工具: 烤箱/平底锅,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 锅中倒20ml食用油，油热后下大葱、大蒜、八角、香叶炒香。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入半包火锅底料和豆瓣酱炒出红油，放白糖、食盐、生抽调味，倒入与食材齐平的清水煮开。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 依次下芹菜段、豆芽、千张丝稍烫后铺洋葱丝，放上烤鱼，再铺干辣椒、灯笼椒、青花椒。
方法: 煮,铺
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 另起锅烧热油，浇在辣椒上激香，最后撒熟花生米、葱花、白芝麻、香菜，再煮5-6分钟即可。
方法: 浇油,煮
工具: 小锅,锅铲
时间: 5-6分钟

关联图谱:
- OUT REQUIRES 火锅底料 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒段 (Ingredient): category: 调料
- OUT REQUIRES 大葱 (Ingredient): category: 蔬菜
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6811927556991577, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼处理好后洗净，特别注意肚内的血丝，不洗干净会有腥味。放入大碗中，倒入料酒、10g姜片、5g盐，腌制15分钟。
方法: 腌制
工具: 碗
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 豆腐切块，放入凉水浸泡5分钟，捞出备用。
方法: 切,浸泡
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 煎鱼前，先用生姜片擦一下锅防止粘锅，倒入油（油量为15ml×鱼的条数），烧热后放入鱼煎2-3分钟，期间需要晃动一下鱼防止粘底，且需要翻一次身。
方法: 煎
工具: 炒锅,锅铲
时间: 2-3分钟

### 第4步
步骤: 步骤4
描述: 待鱼全部煎好后，倒入开水、5ml料酒、姜片，小火转至大火，盖上锅盖大火煮10分钟（水要稍微多一些，后面会蒸发掉一些）。
方法: 煮
工具: 炒锅,锅盖
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 见汤变白后倒入准备好的豆腐，调中火再煮5分钟，加入10g盐、3g胡椒粉调味，最后撒上葱花出锅。
方法: 煮,调味
工具: 锅铲
时间: 5分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.6738912463188171, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳜鱼从腹部切开，去除鱼鳃和内脏，打去鱼鳞，用刀在表皮上刮去粘液（可让摊主代劳）
方法: 切,清理
工具: 刀

### 第2步
步骤: 步骤2
描述: 鳜鱼身上打上花刀，放姜片，可放少许猪油，装盘并在下面垫筷子以便受热均匀
方法: 切,摆盘
工具: 刀,筷子

### 第3步
步骤: 步骤3
描述: 大葱划开后去除中间的芯，只保留外面两层；小葱划开备用；红椒去籽去肉备用
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 将大葱、小葱、辣椒码在一起切成丝，泡在水里备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 锅中加大量水，水热后放入鳜鱼，盖上锅盖，大火蒸8-10分钟
方法: 蒸
工具: 蒸锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 蒸鱼期间另起一锅烧热油至冒烟
方法: 加热
工具: 锅

### 第7步
步骤: 步骤7
描述: 蒸好后倒掉蒸鱼的水，去除姜片，放上葱丝，浇上热油
方法: 倒,淋
工具: 锅,筷子

### 第8步
步骤: 步骤8
描述: 倒入生抽或蒸鱼豉油即可上桌
方法: 淋

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201000257, recipe_name=清蒸鲈鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 清蒸鲈鱼
菜品名称: 清蒸鲈鱼
分类: 水产
菜系: 粤菜
难度: 3.0
关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201000258, recipe_name=鲈鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲈鱼
食材名称: 鲈鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000027, recipe_name=姜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 姜
食材名称: 姜
类别: 蔬菜
关联图谱:
- IN REQUIRES 香煎五花肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 地三鲜 (Recipe): category: 素菜；cuisineType: 东北菜；difficulty: 3.0
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201000062, recipe_name=葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 葱
食材名称: 葱
类别: 蔬菜
关联图谱:
- IN REQUIRES 清蒸生蚝 (Recipe): category: 水产；difficulty: 3.0
- IN REQUIRES 素炒豆角 (Recipe): category: 素菜；difficulty: 2.0
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201000262, recipe_name=蒸鱼豉油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸鱼豉油
食材名称: 蒸鱼豉油
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201000009, recipe_name=食用油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 食用油
食材名称: 食用油
类别: 调料
关联图谱:
- IN REQUIRES 鲤鱼炖白菜 (Recipe): category: 水产；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 青椒土豆炒肉 (Recipe): category: 荤菜；difficulty: 3.0
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=tipdoc_9e62e8f43239, recipe_name=蒸, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧文档: 蒸
分类: 烹饪技巧
标签: 学习蒸,方式,正文,注意事项,蒸,蒸锅,铁锅
摘要: 蒸 方式 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热 铁锅 如果没有蒸锅，只有普通的铁锅 非平底锅 ，可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。 铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
来源: tips/learn/学习蒸.md

补充信息: 技巧章节: 蒸
章节: 正文
分类: 烹饪技巧
摘要: 蒸
内容: # 蒸
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=tipchunk_6ce348d11822, recipe_name=蒸 / 方式, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 方式
章节: 方式
分类: 烹饪技巧
摘要: 方式
内容: ## 方式
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=tipchunk_9f97843cc8b2, recipe_name=蒸 / 注意事项, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 注意事项
章节: 注意事项
分类: 烹饪技巧
摘要: 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
内容: ## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=tipchunk_a06f1b706233, recipe_name=蒸 / 蒸锅, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 蒸锅
章节: 蒸锅
分类: 烹饪技巧
摘要: 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
内容: ### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201000519, recipe_name=太阳蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201004928, recipe_name=松仁玉米, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 松仁玉米
分类: 素菜
难度: 2.0
主要食材: 白砂糖, 淀粉, 熟松子仁
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=12
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

### result_order=13
source: branch_grouped
metadata_summary: node_id=201000257, recipe_name=清蒸鲈鱼, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 清蒸鲈鱼
分类: 水产
菜系: 粤菜
难度: 3.0
主要食材: 香葱, 鲈鱼, 食用盐
关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=14
source: branch_grouped
metadata_summary: node_id=201004117, recipe_name=炒馍, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 炒馍
分类: 主食
菜系: 西北菜
难度: 3.0
主要食材: 辣椒粉, 五香粉, 孜然粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=15
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

### result_order=16
source: branch_grouped
metadata_summary: node_id=201004341, recipe_name=韭菜盒子, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=17
source: branch_grouped
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 海鲜
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

### result_order=18
source: branch_grouped
metadata_summary: node_id=201004506, recipe_name=披萨饼皮, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 披萨饼皮
分类: 主食
难度: 4.0
主要食材: 中筋面粉, 食用盐, 橄榄油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=19
source: branch_grouped
metadata_summary: node_id=201004544, recipe_name=日式肥牛丼饭, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 去腥
菜品: 日式肥牛丼饭
分类: 主食
菜系: 日式
难度: 4.0
主要食材: 味淋, 酱油, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=20
source: branch_grouped
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.7811521887779236, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片切丝、香葱的葱白切段，葱绿切丝，切丝后放入冷水浸泡备用。
方法: 切
工具: 刀,案板,冷水碗
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鲈鱼处理好后洗净，用厨房纸擦干，两面分别划几刀，用盐洗掉鱼身的粘液，并用10g盐抹遍鱼身的内外，腌制10分钟以上。
方法: 洗,腌制,切
工具: 厨房纸,刀,案板,盆
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼肚内塞上姜和葱白，鱼身也撒上姜和葱白，量为备用的一半。蒸鱼的碟子用筷子将鱼跟碟子隔开蒸。
方法: 摆盘
工具: 碟子,筷子
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 水烧热感觉到水温后放进入鱼，大火清蒸10分钟。
方法: 蒸
工具: 蒸锅,大火
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 蒸好的鱼，用干净的盘子装起来并去除身上姜蒜。
方法: 装盘
工具: 干净盘子,筷子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 鱼身浇上15ml蒸鱼豉油。
方法: 浇汁
工具: 量勺
时间: 15秒

### 第7步
步骤: 步骤7
描述: 鱼身重新撒上姜和葱丝，锅内加上10ml食用油并烧热，将食用油淋至鱼身即可出菜。
方法: 淋油
工具: 锅,量勺,锅铲
时间: 30秒

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=21
source: branch_grouped
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_44, recipe_name=清蒸鲈鱼, category=水产, score=0.7697495818138123, search_type=vector_enhanced

```text
# 清蒸鲈鱼

菜系: 粤菜
难度: 3.0星

时间信息: 准备时间: 10分钟（腌制）+ 5分钟（处理与改刀）, 烹饪时间: 10分钟（蒸）
份量: 1条鱼

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=22
source: branch_grouped
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_45, recipe_name=清蒸鲈鱼, category=水产, score=0.719322144985199, search_type=vector_enhanced

```text
## 所需食材
1. 姜(1块)
2. 料酒(10-15毫升)
3. 蒸鱼豉油(10-15毫升)
4. 食用油(10-15毫升)
5. 食用盐(5-10克)
6. 香葱(3根)
7. 鲈鱼(1条)

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=23
source: branch_grouped
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.7118656635284424, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼开背杀好（让卖鱼的杀好，千万不要剖腹杀鱼，切记是开背），清洗干净
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 鱼表面用盐涂抹均匀，倒入料酒约80ml、姜末20g，放入冰箱保鲜层进行腌制1-2天
方法: 腌制
工具: 盆,冰箱
时间: 1-2天

### 第3步
步骤: 步骤3
描述: 取出腌制好的鱼，用绳挂起晾晒至半干（约1-2天，具体时间需结合气温与阳光）
方法: 晾晒
工具: 绳
时间: 1-2天

### 第4步
步骤: 步骤4
描述: 食用前请将鱼用清水清洗，沥干水分（防止水遇油飞溅）
方法: 清洗
工具: 盆

### 第5步
步骤: 步骤5
描述: 开大火将锅烧热，迅速改小火，锅中放油，尽量保持整个锅表面有油，将鱼沿锅边划入锅内（先煎鱼背面）
方法: 煎
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 鱼入锅后（和翻面后），不要着急移动鱼的位置（此时容易破皮），煎约30秒后，尝试晃动锅
方法: 煎
工具: 炒锅
时间: 30秒

### 第7步
步骤: 步骤7
描述: 背面煎约1分钟后，翻面煎约1-2分钟，煎至两面金黄
方法: 煎
工具: 锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入豆瓣酱炒出香味，放入姜蒜
方法: 炒
工具: 锅铲

### 第9步
步骤: 步骤9
描述: 炒出佐料香味后，加入料酒、生抽、老抽，倒入热水，水量和鱼平齐或者少点
方法: 炒,煮
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 此时改中大火，煮5-10分钟，后放入青椒段、白糖、鸡精、十三香、陈醋
方法: 煮
工具: 锅铲
时间: 5-10分钟

### 第11步
步骤: 步骤11
描述: 改小火2-5分钟，放入葱、香菜，即可出锅
方法: 焖
工具: 锅铲
时间: 2-5分钟

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 姜沫 (Ingredient): category: 调料
- OUT REQUIRES 料酒 (Ingredient): category: 调料
```

### result_order=24
source: branch_grouped
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.7116531729698181, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鱼清洗干净，确保无鱼鳞等异物
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 将鱼头朝左，鱼肚朝下，右手持刀。刀竖直切下1cm，按紧鱼身往左片3-4cm，再将鱼片中间轻轻划一刀
方法: 切
工具: 菜刀,案板

### 第3步
步骤: 步骤3
描述: 将鱼放进盆里，然后将大姜切片，大葱切段，用吃奶的力气将大葱大姜里的汁水挤到盆中
方法: 切,挤汁
工具: 盆,菜刀

### 第4步
步骤: 步骤4
描述: 加入20g盐、25g料酒，给鲤鱼搓澡，涂抹均匀，腌制30分钟以上
方法: 腌制
工具: 盆
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 在干净盆中加入100g面粉、200g淀粉、180g水、5g盐，搅拌均匀后加入一个鸡蛋，再次搅匀成可拉丝面糊
方法: 搅拌
工具: 盆

### 第6步
步骤: 步骤6
描述: 等待30分钟
方法: 静置
时间: 30分钟

### 第7步
步骤: 步骤7
描述: 将鱼放在案板上，用干毛巾擦干鱼身水分，盆冲洗干净并擦干
方法: 擦干
工具: 干毛巾,盆

### 第8步
步骤: 步骤8
描述: 起锅烧油，加入约1L油，油温烧至7成热（200-240℃）
方法: 炸
工具: 锅,锅铲,笊篱

### 第9步
步骤: 步骤9
描述: 捏鱼尾，鱼头先入油锅，用勺子淋热油定型，面糊成型后整鱼入锅，用笊篱托鱼头防糊
方法: 炸
工具: 锅,锅铲,笊篱

### 第10步
步骤: 步骤10
描述: 用锅铲和笊篱配合给鱼翻身，再炸2分钟，出锅装盘
方法: 炸
工具: 锅铲,笊篱,盘子
时间: 2分钟

### 第11步
步骤: 步骤11
描述: 将锅中油倒出，锅刷干净
方法: 倒油,清洗
工具: 锅

### 第12步
步骤: 步骤12
描述: 小碗混合50g清水、40g番茄酱、20g白糖、10g白醋，搅拌均匀
方法: 搅拌
工具: 小碗

### 第13步
步骤: 步骤13
描述: 另取小碗，10g淀粉加10g水调成水淀粉
方法: 搅拌
工具: 小碗

### 第14步
步骤: 步骤14
描述: 大火烧热锅，倒入料汁，烧开后转小火，加入水淀粉边倒边搅，20秒后关火
方法: 煮,搅拌
工具: 锅,勺子
时间: 20秒

### 第15步
步骤: 步骤15
描述: 将糖醋汁均匀浇在鱼身上，撒香菜或葱花点缀即可
方法: 浇汁
工具: 勺子,盘子

关联图谱:
- OUT REQUIRES 香菜 (Ingredient): category: 蔬菜
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 番茄酱 (Ingredient): category: 调料
```

### result_order=25
source: branch_grouped
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6931073665618896, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜蒜切碎，干辣椒切碎，与姜蒜一起备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第2步
步骤: 步骤2
描述: 锅中加入30-50ml油，小火加热至锅热。
方法: 加热
工具: 炒锅
时间: 约30秒

### 第3步
步骤: 步骤3
描述: 将擦干水分的鱼放入锅中，小火煎至底部金黄，期间晃动锅防止粘锅。
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 翻面，重复煎另一面至金黄。
方法: 煎
工具: 锅铲
时间: 约2-3分钟

### 第5步
步骤: 步骤5
描述: 加入姜蒜辣椒碎，翻炒出香味。
方法: 炒
工具: 锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 倒入适量料酒，迅速产生大量油烟，注意安全。
方法: 炝锅
工具: 锅铲
时间: 约15秒

### 第7步
步骤: 步骤7
描述: 加入醋、白砂糖、酱油（老抽），翻炒均匀。
方法: 炒
工具: 锅铲
时间: 约15秒

### 第8步
步骤: 步骤8
描述: 加入冷水，刚好淹没鱼身，转中火，盖锅盖1分钟后翻面，再盖锅盖继续炖煮3-4分钟。
方法: 炖
工具: 炒锅,锅盖
时间: 约4-5分钟

### 第9步
步骤: 步骤9
描述: 加入盐、小米椒、蚝油、味精，盖锅盖继续炖煮并适时翻面。
方法: 炖
工具: 锅铲,锅盖
时间: 约2-3分钟

### 第10步
步骤: 步骤10
描述: 汤汁收至鱼鳍下方位置时转小火，加入香菜和葱花，盖锅盖20秒后关火。
方法: 焖
工具: 锅盖
时间: 20秒

### 第11步
步骤: 步骤11
描述: 起锅装盘。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (Ingredient): category: 调料
```

### result_order=26
source: branch_grouped
metadata_summary: node_id=201000040, chunk_id=201000040_chunk_11, recipe_name=水煮鱼, category=水产, score=0.6867295503616333, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 巴沙鱼若从冷冻柜取出，放室温自然解冻5小时，再切片处理。
方法: 解冻
时间: 5小时

### 第2步
步骤: 步骤2
描述: 将巴沙鱼撇成约5cm长、3cm宽的薄片。
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 将鱼片放入大不锈钢碗中，加入30g豆瓣酱、3g盐、10ml藤椒油、3g白胡椒粉，用手抓匀后加入5ml菜籽油封味，常温静置至少30分钟入味。
方法: 腌制
工具: 大不锈钢碗
时间: 30分钟

### 第4步
步骤: 步骤4
描述: 大蒜切成蒜末；以300g花菜、200g生菜为例，将蔬菜洗净。
方法: 切,洗
工具: 刀,盆

### 第5步
步骤: 步骤5
描述: 花菜开水锅焯水备用；生菜洗净晾干后炒熟备用（不用放油）。
方法: 焯水,炒
工具: 锅,漏勺

### 第6步
步骤: 步骤6
描述: 热锅冷油（菜籽油20ml），加入10g豆瓣酱、10g豆豉（可选）和蒜末，中火慢炒。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 加入150ml热水，水开后放入腌制好的鱼片，轻轻翻动使其散开，加入2g盐和2g糖调味，水再次沸腾即可盛盘。
方法: 煮
工具: 锅,漏勺

### 第8步
步骤: 步骤8
描述: 先将熟蔬菜盛至大碗中，再将热鱼片铺在蔬菜上，浇上锅中剩余热汤即可。
方法: 盛盘
工具: 大碗

关联图谱:
- OUT REQUIRES 巴沙鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 蔬菜（土豆片/豆芽/花菜/生菜等） (Ingredient): category: 蔬菜
- OUT REQUIRES 红油豆瓣酱 (Ingredient): category: 调料
```

### result_order=27
source: branch_grouped
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6865550875663757, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 草鱼从背部切开，两面沿背部划几刀，不要划破鱼肚；用热水或刷子洗净表面粘液。
方法: 切,清洗
工具: 刀,刷子
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 鱼放入容器，加料酒、白胡椒粉、食盐抹匀，腌制二十分钟入味。
方法: 腌制
工具: 容器
时间: 20分钟

### 第3步
步骤: 步骤3
描述: 大葱切块，大蒜粒对半切，与八角、香叶、桂皮放同一容器；干辣椒段、灯笼椒切段放另一容器；芹菜切段；豆芽、千张焯水，千张切丝；洋葱切丝。
方法: 切,焯水
工具: 刀,案板,锅,漏勺
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 烤箱版：烤盘刷底油，鱼皮朝下烤至两面金黄，撒孜然粉。无烤箱版：热锅热油，锅边撒少量盐防粘，下鱼煎至两面金黄，撒孜然粉后出锅装盘。
方法: 烤,煎
工具: 烤箱/平底锅,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 锅中倒20ml食用油，油热后下大葱、大蒜、八角、香叶炒香。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入半包火锅底料和豆瓣酱炒出红油，放白糖、食盐、生抽调味，倒入与食材齐平的清水煮开。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 依次下芹菜段、豆芽、千张丝稍烫后铺洋葱丝，放上烤鱼，再铺干辣椒、灯笼椒、青花椒。
方法: 煮,铺
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 另起锅烧热油，浇在辣椒上激香，最后撒熟花生米、葱花、白芝麻、香菜，再煮5-6分钟即可。
方法: 浇油,煮
工具: 小锅,锅铲
时间: 5-6分钟

关联图谱:
- OUT REQUIRES 火锅底料 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒段 (Ingredient): category: 调料
- OUT REQUIRES 大葱 (Ingredient): category: 蔬菜
```

### result_order=28
source: branch_grouped
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6811927556991577, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼处理好后洗净，特别注意肚内的血丝，不洗干净会有腥味。放入大碗中，倒入料酒、10g姜片、5g盐，腌制15分钟。
方法: 腌制
工具: 碗
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 豆腐切块，放入凉水浸泡5分钟，捞出备用。
方法: 切,浸泡
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 煎鱼前，先用生姜片擦一下锅防止粘锅，倒入油（油量为15ml×鱼的条数），烧热后放入鱼煎2-3分钟，期间需要晃动一下鱼防止粘底，且需要翻一次身。
方法: 煎
工具: 炒锅,锅铲
时间: 2-3分钟

### 第4步
步骤: 步骤4
描述: 待鱼全部煎好后，倒入开水、5ml料酒、姜片，小火转至大火，盖上锅盖大火煮10分钟（水要稍微多一些，后面会蒸发掉一些）。
方法: 煮
工具: 炒锅,锅盖
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 见汤变白后倒入准备好的豆腐，调中火再煮5分钟，加入10g盐、3g胡椒粉调味，最后撒上葱花出锅。
方法: 煮,调味
工具: 锅铲
时间: 5分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=29
source: branch_grouped
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.6738912463188171, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳜鱼从腹部切开，去除鱼鳃和内脏，打去鱼鳞，用刀在表皮上刮去粘液（可让摊主代劳）
方法: 切,清理
工具: 刀

### 第2步
步骤: 步骤2
描述: 鳜鱼身上打上花刀，放姜片，可放少许猪油，装盘并在下面垫筷子以便受热均匀
方法: 切,摆盘
工具: 刀,筷子

### 第3步
步骤: 步骤3
描述: 大葱划开后去除中间的芯，只保留外面两层；小葱划开备用；红椒去籽去肉备用
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 将大葱、小葱、辣椒码在一起切成丝，泡在水里备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 锅中加大量水，水热后放入鳜鱼，盖上锅盖，大火蒸8-10分钟
方法: 蒸
工具: 蒸锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 蒸鱼期间另起一锅烧热油至冒烟
方法: 加热
工具: 锅

### 第7步
步骤: 步骤7
描述: 蒸好后倒掉蒸鱼的水，去除姜片，放上葱丝，浇上热油
方法: 倒,淋
工具: 锅,筷子

### 第8步
步骤: 步骤8
描述: 倒入生抽或蒸鱼豉油即可上桌
方法: 淋

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.7811521887779236, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片切丝、香葱的葱白切段，葱绿切丝，切丝后放入冷水浸泡备用。
方法: 切
工具: 刀,案板,冷水碗
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鲈鱼处理好后洗净，用厨房纸擦干，两面分别划几刀，用盐洗掉鱼身的粘液，并用10g盐抹遍鱼身的内外，腌制10分钟以上。
方法: 洗,腌制,切
工具: 厨房纸,刀,案板,盆
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼肚内塞上姜和葱白，鱼身也撒上姜和葱白，量为备用的一半。蒸鱼的碟子用筷子将鱼跟碟子隔开蒸。
方法: 摆盘
工具: 碟子,筷子
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 水烧热感觉到水温后放进入鱼，大火清蒸10分钟。
方法: 蒸
工具: 蒸锅,大火
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 蒸好的鱼，用干净的盘子装起来并去除身上姜蒜。
方法: 装盘
工具: 干净盘子,筷子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 鱼身浇上15ml蒸鱼豉油。
方法: 浇汁
工具: 量勺
时间: 15秒

### 第7步
步骤: 步骤7
描述: 鱼身重新撒上姜和葱丝，锅内加上10ml食用油并烧热，将食用油淋至鱼身即可出菜。
方法: 淋油
工具: 锅,量勺,锅铲
时间: 30秒

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201000258, recipe_name=鲈鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲈鱼
食材名称: 鲈鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000027, recipe_name=姜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 姜
食材名称: 姜
类别: 蔬菜
关联图谱:
- IN REQUIRES 香煎五花肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 地三鲜 (Recipe): category: 素菜；cuisineType: 东北菜；difficulty: 3.0
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201000062, recipe_name=葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 葱
食材名称: 葱
类别: 蔬菜
关联图谱:
- IN REQUIRES 清蒸生蚝 (Recipe): category: 水产；difficulty: 3.0
- IN REQUIRES 素炒豆角 (Recipe): category: 素菜；difficulty: 2.0
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201000262, recipe_name=蒸鱼豉油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸鱼豉油
食材名称: 蒸鱼豉油
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201000009, recipe_name=食用油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 食用油
食材名称: 食用油
类别: 调料
关联图谱:
- IN REQUIRES 鲤鱼炖白菜 (Recipe): category: 水产；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 青椒土豆炒肉 (Recipe): category: 荤菜；difficulty: 3.0
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=tipdoc_9e62e8f43239, recipe_name=蒸, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧文档: 蒸
分类: 烹饪技巧
标签: 学习蒸,方式,正文,注意事项,蒸,蒸锅,铁锅
摘要: 蒸 方式 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热 铁锅 如果没有蒸锅，只有普通的铁锅 非平底锅 ，可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。 铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
来源: tips/learn/学习蒸.md

补充信息: 技巧章节: 蒸
章节: 正文
分类: 烹饪技巧
摘要: 蒸
内容: # 蒸
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=tipchunk_6ce348d11822, recipe_name=蒸 / 方式, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 方式
章节: 方式
分类: 烹饪技巧
摘要: 方式
内容: ## 方式
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=tipchunk_9f97843cc8b2, recipe_name=蒸 / 注意事项, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 注意事项
章节: 注意事项
分类: 烹饪技巧
摘要: 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
内容: ## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=tipchunk_a06f1b706233, recipe_name=蒸 / 蒸锅, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 蒸锅
章节: 蒸锅
分类: 烹饪技巧
摘要: 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
内容: ### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201000519, recipe_name=太阳蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201004928, recipe_name=松仁玉米, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 松仁玉米
分类: 素菜
难度: 2.0
主要食材: 白砂糖, 淀粉, 熟松子仁
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=12
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

### result_order=13
source: merged_candidates
metadata_summary: node_id=201004117, recipe_name=炒馍, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 炒馍
分类: 主食
菜系: 西北菜
难度: 3.0
主要食材: 辣椒粉, 五香粉, 孜然粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=14
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

### result_order=15
source: merged_candidates
metadata_summary: node_id=201004341, recipe_name=韭菜盒子, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=16
source: merged_candidates
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 海鲜
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

### result_order=17
source: merged_candidates
metadata_summary: node_id=201004506, recipe_name=披萨饼皮, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 披萨饼皮
分类: 主食
难度: 4.0
主要食材: 中筋面粉, 食用盐, 橄榄油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=18
source: merged_candidates
metadata_summary: node_id=201004544, recipe_name=日式肥牛丼饭, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 去腥
菜品: 日式肥牛丼饭
分类: 主食
菜系: 日式
难度: 4.0
主要食材: 味淋, 酱油, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=19
source: merged_candidates
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.7118656635284424, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼开背杀好（让卖鱼的杀好，千万不要剖腹杀鱼，切记是开背），清洗干净
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 鱼表面用盐涂抹均匀，倒入料酒约80ml、姜末20g，放入冰箱保鲜层进行腌制1-2天
方法: 腌制
工具: 盆,冰箱
时间: 1-2天

### 第3步
步骤: 步骤3
描述: 取出腌制好的鱼，用绳挂起晾晒至半干（约1-2天，具体时间需结合气温与阳光）
方法: 晾晒
工具: 绳
时间: 1-2天

### 第4步
步骤: 步骤4
描述: 食用前请将鱼用清水清洗，沥干水分（防止水遇油飞溅）
方法: 清洗
工具: 盆

### 第5步
步骤: 步骤5
描述: 开大火将锅烧热，迅速改小火，锅中放油，尽量保持整个锅表面有油，将鱼沿锅边划入锅内（先煎鱼背面）
方法: 煎
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 鱼入锅后（和翻面后），不要着急移动鱼的位置（此时容易破皮），煎约30秒后，尝试晃动锅
方法: 煎
工具: 炒锅
时间: 30秒

### 第7步
步骤: 步骤7
描述: 背面煎约1分钟后，翻面煎约1-2分钟，煎至两面金黄
方法: 煎
工具: 锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入豆瓣酱炒出香味，放入姜蒜
方法: 炒
工具: 锅铲

### 第9步
步骤: 步骤9
描述: 炒出佐料香味后，加入料酒、生抽、老抽，倒入热水，水量和鱼平齐或者少点
方法: 炒,煮
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 此时改中大火，煮5-10分钟，后放入青椒段、白糖、鸡精、十三香、陈醋
方法: 煮
工具: 锅铲
时间: 5-10分钟

### 第11步
步骤: 步骤11
描述: 改小火2-5分钟，放入葱、香菜，即可出锅
方法: 焖
工具: 锅铲
时间: 2-5分钟

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 姜沫 (Ingredient): category: 调料
- OUT REQUIRES 料酒 (Ingredient): category: 调料
```

### result_order=20
source: merged_candidates
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.7116531729698181, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鱼清洗干净，确保无鱼鳞等异物
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 将鱼头朝左，鱼肚朝下，右手持刀。刀竖直切下1cm，按紧鱼身往左片3-4cm，再将鱼片中间轻轻划一刀
方法: 切
工具: 菜刀,案板

### 第3步
步骤: 步骤3
描述: 将鱼放进盆里，然后将大姜切片，大葱切段，用吃奶的力气将大葱大姜里的汁水挤到盆中
方法: 切,挤汁
工具: 盆,菜刀

### 第4步
步骤: 步骤4
描述: 加入20g盐、25g料酒，给鲤鱼搓澡，涂抹均匀，腌制30分钟以上
方法: 腌制
工具: 盆
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 在干净盆中加入100g面粉、200g淀粉、180g水、5g盐，搅拌均匀后加入一个鸡蛋，再次搅匀成可拉丝面糊
方法: 搅拌
工具: 盆

### 第6步
步骤: 步骤6
描述: 等待30分钟
方法: 静置
时间: 30分钟

### 第7步
步骤: 步骤7
描述: 将鱼放在案板上，用干毛巾擦干鱼身水分，盆冲洗干净并擦干
方法: 擦干
工具: 干毛巾,盆

### 第8步
步骤: 步骤8
描述: 起锅烧油，加入约1L油，油温烧至7成热（200-240℃）
方法: 炸
工具: 锅,锅铲,笊篱

### 第9步
步骤: 步骤9
描述: 捏鱼尾，鱼头先入油锅，用勺子淋热油定型，面糊成型后整鱼入锅，用笊篱托鱼头防糊
方法: 炸
工具: 锅,锅铲,笊篱

### 第10步
步骤: 步骤10
描述: 用锅铲和笊篱配合给鱼翻身，再炸2分钟，出锅装盘
方法: 炸
工具: 锅铲,笊篱,盘子
时间: 2分钟

### 第11步
步骤: 步骤11
描述: 将锅中油倒出，锅刷干净
方法: 倒油,清洗
工具: 锅

### 第12步
步骤: 步骤12
描述: 小碗混合50g清水、40g番茄酱、20g白糖、10g白醋，搅拌均匀
方法: 搅拌
工具: 小碗

### 第13步
步骤: 步骤13
描述: 另取小碗，10g淀粉加10g水调成水淀粉
方法: 搅拌
工具: 小碗

### 第14步
步骤: 步骤14
描述: 大火烧热锅，倒入料汁，烧开后转小火，加入水淀粉边倒边搅，20秒后关火
方法: 煮,搅拌
工具: 锅,勺子
时间: 20秒

### 第15步
步骤: 步骤15
描述: 将糖醋汁均匀浇在鱼身上，撒香菜或葱花点缀即可
方法: 浇汁
工具: 勺子,盘子

关联图谱:
- OUT REQUIRES 香菜 (Ingredient): category: 蔬菜
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 番茄酱 (Ingredient): category: 调料
```

### result_order=21
source: merged_candidates
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6931073665618896, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜蒜切碎，干辣椒切碎，与姜蒜一起备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第2步
步骤: 步骤2
描述: 锅中加入30-50ml油，小火加热至锅热。
方法: 加热
工具: 炒锅
时间: 约30秒

### 第3步
步骤: 步骤3
描述: 将擦干水分的鱼放入锅中，小火煎至底部金黄，期间晃动锅防止粘锅。
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 翻面，重复煎另一面至金黄。
方法: 煎
工具: 锅铲
时间: 约2-3分钟

### 第5步
步骤: 步骤5
描述: 加入姜蒜辣椒碎，翻炒出香味。
方法: 炒
工具: 锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 倒入适量料酒，迅速产生大量油烟，注意安全。
方法: 炝锅
工具: 锅铲
时间: 约15秒

### 第7步
步骤: 步骤7
描述: 加入醋、白砂糖、酱油（老抽），翻炒均匀。
方法: 炒
工具: 锅铲
时间: 约15秒

### 第8步
步骤: 步骤8
描述: 加入冷水，刚好淹没鱼身，转中火，盖锅盖1分钟后翻面，再盖锅盖继续炖煮3-4分钟。
方法: 炖
工具: 炒锅,锅盖
时间: 约4-5分钟

### 第9步
步骤: 步骤9
描述: 加入盐、小米椒、蚝油、味精，盖锅盖继续炖煮并适时翻面。
方法: 炖
工具: 锅铲,锅盖
时间: 约2-3分钟

### 第10步
步骤: 步骤10
描述: 汤汁收至鱼鳍下方位置时转小火，加入香菜和葱花，盖锅盖20秒后关火。
方法: 焖
工具: 锅盖
时间: 20秒

### 第11步
步骤: 步骤11
描述: 起锅装盘。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (Ingredient): category: 调料
```

### result_order=22
source: merged_candidates
metadata_summary: node_id=201000040, chunk_id=201000040_chunk_11, recipe_name=水煮鱼, category=水产, score=0.6867295503616333, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 巴沙鱼若从冷冻柜取出，放室温自然解冻5小时，再切片处理。
方法: 解冻
时间: 5小时

### 第2步
步骤: 步骤2
描述: 将巴沙鱼撇成约5cm长、3cm宽的薄片。
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 将鱼片放入大不锈钢碗中，加入30g豆瓣酱、3g盐、10ml藤椒油、3g白胡椒粉，用手抓匀后加入5ml菜籽油封味，常温静置至少30分钟入味。
方法: 腌制
工具: 大不锈钢碗
时间: 30分钟

### 第4步
步骤: 步骤4
描述: 大蒜切成蒜末；以300g花菜、200g生菜为例，将蔬菜洗净。
方法: 切,洗
工具: 刀,盆

### 第5步
步骤: 步骤5
描述: 花菜开水锅焯水备用；生菜洗净晾干后炒熟备用（不用放油）。
方法: 焯水,炒
工具: 锅,漏勺

### 第6步
步骤: 步骤6
描述: 热锅冷油（菜籽油20ml），加入10g豆瓣酱、10g豆豉（可选）和蒜末，中火慢炒。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 加入150ml热水，水开后放入腌制好的鱼片，轻轻翻动使其散开，加入2g盐和2g糖调味，水再次沸腾即可盛盘。
方法: 煮
工具: 锅,漏勺

### 第8步
步骤: 步骤8
描述: 先将熟蔬菜盛至大碗中，再将热鱼片铺在蔬菜上，浇上锅中剩余热汤即可。
方法: 盛盘
工具: 大碗

关联图谱:
- OUT REQUIRES 巴沙鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 蔬菜（土豆片/豆芽/花菜/生菜等） (Ingredient): category: 蔬菜
- OUT REQUIRES 红油豆瓣酱 (Ingredient): category: 调料
```

### result_order=23
source: merged_candidates
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6865550875663757, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 草鱼从背部切开，两面沿背部划几刀，不要划破鱼肚；用热水或刷子洗净表面粘液。
方法: 切,清洗
工具: 刀,刷子
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 鱼放入容器，加料酒、白胡椒粉、食盐抹匀，腌制二十分钟入味。
方法: 腌制
工具: 容器
时间: 20分钟

### 第3步
步骤: 步骤3
描述: 大葱切块，大蒜粒对半切，与八角、香叶、桂皮放同一容器；干辣椒段、灯笼椒切段放另一容器；芹菜切段；豆芽、千张焯水，千张切丝；洋葱切丝。
方法: 切,焯水
工具: 刀,案板,锅,漏勺
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 烤箱版：烤盘刷底油，鱼皮朝下烤至两面金黄，撒孜然粉。无烤箱版：热锅热油，锅边撒少量盐防粘，下鱼煎至两面金黄，撒孜然粉后出锅装盘。
方法: 烤,煎
工具: 烤箱/平底锅,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 锅中倒20ml食用油，油热后下大葱、大蒜、八角、香叶炒香。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入半包火锅底料和豆瓣酱炒出红油，放白糖、食盐、生抽调味，倒入与食材齐平的清水煮开。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 依次下芹菜段、豆芽、千张丝稍烫后铺洋葱丝，放上烤鱼，再铺干辣椒、灯笼椒、青花椒。
方法: 煮,铺
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 另起锅烧热油，浇在辣椒上激香，最后撒熟花生米、葱花、白芝麻、香菜，再煮5-6分钟即可。
方法: 浇油,煮
工具: 小锅,锅铲
时间: 5-6分钟

关联图谱:
- OUT REQUIRES 火锅底料 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒段 (Ingredient): category: 调料
- OUT REQUIRES 大葱 (Ingredient): category: 蔬菜
```

### result_order=24
source: merged_candidates
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6811927556991577, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼处理好后洗净，特别注意肚内的血丝，不洗干净会有腥味。放入大碗中，倒入料酒、10g姜片、5g盐，腌制15分钟。
方法: 腌制
工具: 碗
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 豆腐切块，放入凉水浸泡5分钟，捞出备用。
方法: 切,浸泡
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 煎鱼前，先用生姜片擦一下锅防止粘锅，倒入油（油量为15ml×鱼的条数），烧热后放入鱼煎2-3分钟，期间需要晃动一下鱼防止粘底，且需要翻一次身。
方法: 煎
工具: 炒锅,锅铲
时间: 2-3分钟

### 第4步
步骤: 步骤4
描述: 待鱼全部煎好后，倒入开水、5ml料酒、姜片，小火转至大火，盖上锅盖大火煮10分钟（水要稍微多一些，后面会蒸发掉一些）。
方法: 煮
工具: 炒锅,锅盖
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 见汤变白后倒入准备好的豆腐，调中火再煮5分钟，加入10g盐、3g胡椒粉调味，最后撒上葱花出锅。
方法: 煮,调味
工具: 锅铲
时间: 5分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=25
source: merged_candidates
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.6738912463188171, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳜鱼从腹部切开，去除鱼鳃和内脏，打去鱼鳞，用刀在表皮上刮去粘液（可让摊主代劳）
方法: 切,清理
工具: 刀

### 第2步
步骤: 步骤2
描述: 鳜鱼身上打上花刀，放姜片，可放少许猪油，装盘并在下面垫筷子以便受热均匀
方法: 切,摆盘
工具: 刀,筷子

### 第3步
步骤: 步骤3
描述: 大葱划开后去除中间的芯，只保留外面两层；小葱划开备用；红椒去籽去肉备用
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 将大葱、小葱、辣椒码在一起切成丝，泡在水里备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 锅中加大量水，水热后放入鳜鱼，盖上锅盖，大火蒸8-10分钟
方法: 蒸
工具: 蒸锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 蒸鱼期间另起一锅烧热油至冒烟
方法: 加热
工具: 锅

### 第7步
步骤: 步骤7
描述: 蒸好后倒掉蒸鱼的水，去除姜片，放上葱丝，浇上热油
方法: 倒,淋
工具: 锅,筷子

### 第8步
步骤: 步骤8
描述: 倒入生抽或蒸鱼豉油即可上桌
方法: 淋

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_9e62e8f43239,tipchunk_6ce348d11822,tipchunk_9f97843cc8b2,tipchunk_a06f1b706233, recipe_name=蒸, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 蒸
关键技巧内容:
## 正文
# 蒸
## 方式
## 方式
## 蒸锅
### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
## 铁锅
### 铁锅

如果没有蒸锅，只有普通的铁锅（非平底锅），可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。

铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖
## 注意事项
## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
菜品: 清蒸鲈鱼
分类: 水产
菜系: 粤菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片切丝、香葱的葱白切段，葱绿切丝，切丝后放入冷水浸泡备用。
方法: 切
工具: 刀,案板,冷水碗
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鲈鱼处理好后洗净，用厨房纸擦干，两面分别划几刀，用盐洗掉鱼身的粘液，并用10g盐抹遍鱼身的内外，腌制10分钟以上。
方法: 洗,腌制,切
工具: 厨房纸,刀,案板,盆
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼肚内塞上姜和葱白，鱼身也撒上姜和葱白，量为备用的一半。蒸鱼的碟子用筷子将鱼跟碟子隔开蒸。
方法: 摆盘
工具: 碟子,筷子
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 水烧热感觉到水温后放进入鱼，大火清蒸10分钟。
方法: 蒸
工具: 蒸锅,大火
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 蒸好的鱼，用干净的盘子装起来并去除身上姜蒜。
方法: 装盘
工具: 干净盘子,筷子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 鱼身浇上15ml蒸鱼豉油。
方法: 浇汁
工具: 量勺
时间: 15秒

### 第7步
步骤: 步骤7
描述: 鱼身重新撒上姜和葱丝，锅内加上10ml食用油并烧热，将食用油淋至鱼身即可出菜。
方法: 淋油
工具: 锅,量勺,锅铲
时间: 30秒

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### pair_order=1
source: rerank_input

```text
命中关键词: 鲈鱼
食材名称: 鲈鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 姜
食材名称: 姜
类别: 蔬菜
关联图谱:
- IN REQUIRES 香煎五花肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 地三鲜 (Recipe): category: 素菜；cuisineType: 东北菜；difficulty: 3.0
```

### pair_order=3
source: rerank_input

```text
命中关键词: 葱
食材名称: 葱
类别: 蔬菜
关联图谱:
- IN REQUIRES 清蒸生蚝 (Recipe): category: 水产；difficulty: 3.0
- IN REQUIRES 素炒豆角 (Recipe): category: 素菜；difficulty: 2.0
```

### pair_order=4
source: rerank_input

```text
命中关键词: 蒸鱼豉油
食材名称: 蒸鱼豉油
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### pair_order=5
source: rerank_input

```text
命中关键词: 食用油
食材名称: 食用油
类别: 调料
关联图谱:
- IN REQUIRES 鲤鱼炖白菜 (Recipe): category: 水产；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 青椒土豆炒肉 (Recipe): category: 荤菜；difficulty: 3.0
```

### pair_order=6
source: rerank_input

```text
命中关键词: 蒸锅
技巧文档: 蒸
分类: 烹饪技巧
标签: 学习蒸,方式,正文,注意事项,蒸,蒸锅,铁锅
摘要: 蒸 方式 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热 铁锅 如果没有蒸锅，只有普通的铁锅 非平底锅 ，可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。 铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
来源: tips/learn/学习蒸.md

补充信息: 技巧章节: 蒸
章节: 正文
分类: 烹饪技巧
摘要: 蒸
内容: # 蒸
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### pair_order=7
source: rerank_input

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 方式
章节: 方式
分类: 烹饪技巧
摘要: 方式
内容: ## 方式
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### pair_order=8
source: rerank_input

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 注意事项
章节: 注意事项
分类: 烹饪技巧
摘要: 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
内容: ## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### pair_order=9
source: rerank_input

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 蒸锅
章节: 蒸锅
分类: 烹饪技巧
摘要: 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
内容: ### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### pair_order=10
source: rerank_input

```text
命中关键词: 火候
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### pair_order=11
source: rerank_input

```text
命中关键词: 火候
菜品: 松仁玉米
分类: 素菜
难度: 2.0
主要食材: 白砂糖, 淀粉, 熟松子仁
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=12
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

### pair_order=13
source: rerank_input

```text
命中关键词: 火候
菜品: 炒馍
分类: 主食
菜系: 西北菜
难度: 3.0
主要食材: 辣椒粉, 五香粉, 孜然粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=14
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

### pair_order=15
source: rerank_input

```text
命中关键词: 火候
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=16
source: rerank_input

```text
命中关键词: 海鲜
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

### pair_order=17
source: rerank_input

```text
命中关键词: 火候
菜品: 披萨饼皮
分类: 主食
难度: 4.0
主要食材: 中筋面粉, 食用盐, 橄榄油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=18
source: rerank_input

```text
命中关键词: 去腥
菜品: 日式肥牛丼饭
分类: 主食
菜系: 日式
难度: 4.0
主要食材: 味淋, 酱油, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=19
source: rerank_input

```text
菜品: 香煎翘嘴鱼
分类: 水产
菜系: 湘菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼开背杀好（让卖鱼的杀好，千万不要剖腹杀鱼，切记是开背），清洗干净
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 鱼表面用盐涂抹均匀，倒入料酒约80ml、姜末20g，放入冰箱保鲜层进行腌制1-2天
方法: 腌制
工具: 盆,冰箱
时间: 1-2天

### 第3步
步骤: 步骤3
描述: 取出腌制好的鱼，用绳挂起晾晒至半干（约1-2天，具体时间需结合气温与阳光）
方法: 晾晒
工具: 绳
时间: 1-2天

### 第4步
步骤: 步骤4
描述: 食用前请将鱼用清水清洗，沥干水分（防止水遇油飞溅）
方法: 清洗
工具: 盆

### 第5步
步骤: 步骤5
描述: 开大火将锅烧热，迅速改小火，锅中放油，尽量保持整个锅表面有油，将鱼沿锅边划入锅内（先煎鱼背面）
方法: 煎
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 鱼入锅后（和翻面后），不要着急移动鱼的位置（此时容易破皮），煎约30秒后，尝试晃动锅
方法: 煎
工具: 炒锅
时间: 30秒

### 第7步
步骤: 步骤7
描述: 背面煎约1分钟后，翻面煎约1-2分钟，煎至两面金黄
方法: 煎
工具: 锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入豆瓣酱炒出香味，放入姜蒜
方法: 炒
工具: 锅铲

### 第9步
步骤: 步骤9
描述: 炒出佐料香味后，加入料酒、生抽、老抽，倒入热水，水量和鱼平齐或者少点
方法: 炒,煮
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 此时改中大火，煮5-10分钟，后放入青椒段、白糖、鸡精、十三香、陈醋
方法: 煮
工具: 锅铲
时间: 5-10分钟

### 第11步
步骤: 步骤11
描述: 改小火2-5分钟，放入葱、香菜，即可出锅
方法: 焖
工具: 锅铲
时间: 2-5分钟

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): cat
```

### pair_order=20
source: rerank_input

```text
菜品: 糖醋鲤鱼
分类: 水产
菜系: 鲁菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鱼清洗干净，确保无鱼鳞等异物
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 将鱼头朝左，鱼肚朝下，右手持刀。刀竖直切下1cm，按紧鱼身往左片3-4cm，再将鱼片中间轻轻划一刀
方法: 切
工具: 菜刀,案板

### 第3步
步骤: 步骤3
描述: 将鱼放进盆里，然后将大姜切片，大葱切段，用吃奶的力气将大葱大姜里的汁水挤到盆中
方法: 切,挤汁
工具: 盆,菜刀

### 第4步
步骤: 步骤4
描述: 加入20g盐、25g料酒，给鲤鱼搓澡，涂抹均匀，腌制30分钟以上
方法: 腌制
工具: 盆
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 在干净盆中加入100g面粉、200g淀粉、180g水、5g盐，搅拌均匀后加入一个鸡蛋，再次搅匀成可拉丝面糊
方法: 搅拌
工具: 盆

### 第6步
步骤: 步骤6
描述: 等待30分钟
方法: 静置
时间: 30分钟

### 第7步
步骤: 步骤7
描述: 将鱼放在案板上，用干毛巾擦干鱼身水分，盆冲洗干净并擦干
方法: 擦干
工具: 干毛巾,盆

### 第8步
步骤: 步骤8
描述: 起锅烧油，加入约1L油，油温烧至7成热（200-240℃）
方法: 炸
工具: 锅,锅铲,笊篱

### 第9步
步骤: 步骤9
描述: 捏鱼尾，鱼头先入油锅，用勺子淋热油定型，面糊成型后整鱼入锅，用笊篱托鱼头防糊
方法: 炸
工具: 锅,锅铲,笊篱

### 第10步
步骤: 步骤10
描述: 用锅铲和笊篱配合给鱼翻身，再炸2分钟，出锅装盘
方法: 炸
工具: 锅铲,笊篱,盘子
时间: 2分钟

### 第11步
步骤: 步骤11
描述: 将锅中油倒出，锅刷干净
方法: 倒油,清洗
工具: 锅

### 第12步
步骤: 步骤12
描述: 小碗混合50g清水、40g番茄酱、20g白糖、10g白醋，搅拌均匀
方法: 搅拌
工具: 小碗

### 第13步
步骤: 步骤13
描述: 另取小碗，10g淀粉加10
```

### pair_order=21
source: rerank_input

```text
菜品: 红烧鱼
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜蒜切碎，干辣椒切碎，与姜蒜一起备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第2步
步骤: 步骤2
描述: 锅中加入30-50ml油，小火加热至锅热。
方法: 加热
工具: 炒锅
时间: 约30秒

### 第3步
步骤: 步骤3
描述: 将擦干水分的鱼放入锅中，小火煎至底部金黄，期间晃动锅防止粘锅。
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 翻面，重复煎另一面至金黄。
方法: 煎
工具: 锅铲
时间: 约2-3分钟

### 第5步
步骤: 步骤5
描述: 加入姜蒜辣椒碎，翻炒出香味。
方法: 炒
工具: 锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 倒入适量料酒，迅速产生大量油烟，注意安全。
方法: 炝锅
工具: 锅铲
时间: 约15秒

### 第7步
步骤: 步骤7
描述: 加入醋、白砂糖、酱油（老抽），翻炒均匀。
方法: 炒
工具: 锅铲
时间: 约15秒

### 第8步
步骤: 步骤8
描述: 加入冷水，刚好淹没鱼身，转中火，盖锅盖1分钟后翻面，再盖锅盖继续炖煮3-4分钟。
方法: 炖
工具: 炒锅,锅盖
时间: 约4-5分钟

### 第9步
步骤: 步骤9
描述: 加入盐、小米椒、蚝油、味精，盖锅盖继续炖煮并适时翻面。
方法: 炖
工具: 锅铲,锅盖
时间: 约2-3分钟

### 第10步
步骤: 步骤10
描述: 汤汁收至鱼鳍下方位置时转小火，加入香菜和葱花，盖锅盖20秒后关火。
方法: 焖
工具: 锅盖
时间: 20秒

### 第11步
步骤: 步骤11
描述: 起锅装盘。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (In
```

### pair_order=22
source: rerank_input

```text
菜品: 水煮鱼
分类: 水产
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 巴沙鱼若从冷冻柜取出，放室温自然解冻5小时，再切片处理。
方法: 解冻
时间: 5小时

### 第2步
步骤: 步骤2
描述: 将巴沙鱼撇成约5cm长、3cm宽的薄片。
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 将鱼片放入大不锈钢碗中，加入30g豆瓣酱、3g盐、10ml藤椒油、3g白胡椒粉，用手抓匀后加入5ml菜籽油封味，常温静置至少30分钟入味。
方法: 腌制
工具: 大不锈钢碗
时间: 30分钟

### 第4步
步骤: 步骤4
描述: 大蒜切成蒜末；以300g花菜、200g生菜为例，将蔬菜洗净。
方法: 切,洗
工具: 刀,盆

### 第5步
步骤: 步骤5
描述: 花菜开水锅焯水备用；生菜洗净晾干后炒熟备用（不用放油）。
方法: 焯水,炒
工具: 锅,漏勺

### 第6步
步骤: 步骤6
描述: 热锅冷油（菜籽油20ml），加入10g豆瓣酱、10g豆豉（可选）和蒜末，中火慢炒。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 加入150ml热水，水开后放入腌制好的鱼片，轻轻翻动使其散开，加入2g盐和2g糖调味，水再次沸腾即可盛盘。
方法: 煮
工具: 锅,漏勺

### 第8步
步骤: 步骤8
描述: 先将熟蔬菜盛至大碗中，再将热鱼片铺在蔬菜上，浇上锅中剩余热汤即可。
方法: 盛盘
工具: 大碗

关联图谱:
- OUT REQUIRES 巴沙鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 蔬菜（土豆片/豆芽/花菜/生菜等） (Ingredient): category: 蔬菜
- OUT REQUIRES 红油豆瓣酱 (Ingredient): category: 调料
```

### pair_order=23
source: rerank_input

```text
分类: 水产
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 草鱼从背部切开，两面沿背部划几刀，不要划破鱼肚；用热水或刷子洗净表面粘液。
方法: 切,清洗
工具: 刀,刷子
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 鱼放入容器，加料酒、白胡椒粉、食盐抹匀，腌制二十分钟入味。
方法: 腌制
工具: 容器
时间: 20分钟

### 第3步
步骤: 步骤3
描述: 大葱切块，大蒜粒对半切，与八角、香叶、桂皮放同一容器；干辣椒段、灯笼椒切段放另一容器；芹菜切段；豆芽、千张焯水，千张切丝；洋葱切丝。
方法: 切,焯水
工具: 刀,案板,锅,漏勺
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 烤箱版：烤盘刷底油，鱼皮朝下烤至两面金黄，撒孜然粉。无烤箱版：热锅热油，锅边撒少量盐防粘，下鱼煎至两面金黄，撒孜然粉后出锅装盘。
方法: 烤,煎
工具: 烤箱/平底锅,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 锅中倒20ml食用油，油热后下大葱、大蒜、八角、香叶炒香。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入半包火锅底料和豆瓣酱炒出红油，放白糖、食盐、生抽调味，倒入与食材齐平的清水煮开。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 依次下芹菜段、豆芽、千张丝稍烫后铺洋葱丝，放上烤鱼，再铺干辣椒、灯笼椒、青花椒。
方法: 煮,铺
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 另起锅烧热油，浇在辣椒上激香，最后撒熟花生米、葱花、白芝麻、香菜，再煮5-6分钟即可。
方法: 浇油,煮
工具: 小锅,锅铲
时间: 5-6分钟

关联图谱:
- OUT REQUIRES 火锅底料 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒段 (Ingredient): category: 调料
- OUT REQUIRES 大葱 (Ingredient): ca
```

### pair_order=24
source: rerank_input

```text
菜品: 昂刺鱼豆腐汤
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼处理好后洗净，特别注意肚内的血丝，不洗干净会有腥味。放入大碗中，倒入料酒、10g姜片、5g盐，腌制15分钟。
方法: 腌制
工具: 碗
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 豆腐切块，放入凉水浸泡5分钟，捞出备用。
方法: 切,浸泡
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 煎鱼前，先用生姜片擦一下锅防止粘锅，倒入油（油量为15ml×鱼的条数），烧热后放入鱼煎2-3分钟，期间需要晃动一下鱼防止粘底，且需要翻一次身。
方法: 煎
工具: 炒锅,锅铲
时间: 2-3分钟

### 第4步
步骤: 步骤4
描述: 待鱼全部煎好后，倒入开水、5ml料酒、姜片，小火转至大火，盖上锅盖大火煮10分钟（水要稍微多一些，后面会蒸发掉一些）。
方法: 煮
工具: 炒锅,锅盖
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 见汤变白后倒入准备好的豆腐，调中火再煮5分钟，加入10g盐、3g胡椒粉调味，最后撒上葱花出锅。
方法: 煮,调味
工具: 锅铲
时间: 5分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### pair_order=25
source: rerank_input

```text
菜品: 清蒸鳜鱼
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳜鱼从腹部切开，去除鱼鳃和内脏，打去鱼鳞，用刀在表皮上刮去粘液（可让摊主代劳）
方法: 切,清理
工具: 刀

### 第2步
步骤: 步骤2
描述: 鳜鱼身上打上花刀，放姜片，可放少许猪油，装盘并在下面垫筷子以便受热均匀
方法: 切,摆盘
工具: 刀,筷子

### 第3步
步骤: 步骤3
描述: 大葱划开后去除中间的芯，只保留外面两层；小葱划开备用；红椒去籽去肉备用
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 将大葱、小葱、辣椒码在一起切成丝，泡在水里备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 锅中加大量水，水热后放入鳜鱼，盖上锅盖，大火蒸8-10分钟
方法: 蒸
工具: 蒸锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 蒸鱼期间另起一锅烧热油至冒烟
方法: 加热
工具: 锅

### 第7步
步骤: 步骤7
描述: 蒸好后倒掉蒸鱼的水，去除姜片，放上葱丝，浇上热油
方法: 倒,淋
工具: 锅,筷子

### 第8步
步骤: 步骤8
描述: 倒入生抽或蒸鱼豉油即可上桌
方法: 淋

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=26
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 蒸
关键技巧内容:
## 正文
# 蒸
## 方式
## 方式
## 蒸锅
### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
## 铁锅
### 铁锅

如果没有蒸锅，只有普通的铁锅（非平底锅），可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。

铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖
## 注意事项
## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.7811521887779236, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片切丝、香葱的葱白切段，葱绿切丝，切丝后放入冷水浸泡备用。
方法: 切
工具: 刀,案板,冷水碗
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鲈鱼处理好后洗净，用厨房纸擦干，两面分别划几刀，用盐洗掉鱼身的粘液，并用10g盐抹遍鱼身的内外，腌制10分钟以上。
方法: 洗,腌制,切
工具: 厨房纸,刀,案板,盆
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼肚内塞上姜和葱白，鱼身也撒上姜和葱白，量为备用的一半。蒸鱼的碟子用筷子将鱼跟碟子隔开蒸。
方法: 摆盘
工具: 碟子,筷子
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 水烧热感觉到水温后放进入鱼，大火清蒸10分钟。
方法: 蒸
工具: 蒸锅,大火
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 蒸好的鱼，用干净的盘子装起来并去除身上姜蒜。
方法: 装盘
工具: 干净盘子,筷子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 鱼身浇上15ml蒸鱼豉油。
方法: 浇汁
工具: 量勺
时间: 15秒

### 第7步
步骤: 步骤7
描述: 鱼身重新撒上姜和葱丝，锅内加上10ml食用油并烧热，将食用油淋至鱼身即可出菜。
方法: 淋油
工具: 锅,量勺,锅铲
时间: 30秒

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.6738912463188171, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳜鱼从腹部切开，去除鱼鳃和内脏，打去鱼鳞，用刀在表皮上刮去粘液（可让摊主代劳）
方法: 切,清理
工具: 刀

### 第2步
步骤: 步骤2
描述: 鳜鱼身上打上花刀，放姜片，可放少许猪油，装盘并在下面垫筷子以便受热均匀
方法: 切,摆盘
工具: 刀,筷子

### 第3步
步骤: 步骤3
描述: 大葱划开后去除中间的芯，只保留外面两层；小葱划开备用；红椒去籽去肉备用
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 将大葱、小葱、辣椒码在一起切成丝，泡在水里备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 锅中加大量水，水热后放入鳜鱼，盖上锅盖，大火蒸8-10分钟
方法: 蒸
工具: 蒸锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 蒸鱼期间另起一锅烧热油至冒烟
方法: 加热
工具: 锅

### 第7步
步骤: 步骤7
描述: 蒸好后倒掉蒸鱼的水，去除姜片，放上葱丝，浇上热油
方法: 倒,淋
工具: 锅,筷子

### 第8步
步骤: 步骤8
描述: 倒入生抽或蒸鱼豉油即可上桌
方法: 淋

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6931073665618896, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜蒜切碎，干辣椒切碎，与姜蒜一起备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第2步
步骤: 步骤2
描述: 锅中加入30-50ml油，小火加热至锅热。
方法: 加热
工具: 炒锅
时间: 约30秒

### 第3步
步骤: 步骤3
描述: 将擦干水分的鱼放入锅中，小火煎至底部金黄，期间晃动锅防止粘锅。
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 翻面，重复煎另一面至金黄。
方法: 煎
工具: 锅铲
时间: 约2-3分钟

### 第5步
步骤: 步骤5
描述: 加入姜蒜辣椒碎，翻炒出香味。
方法: 炒
工具: 锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 倒入适量料酒，迅速产生大量油烟，注意安全。
方法: 炝锅
工具: 锅铲
时间: 约15秒

### 第7步
步骤: 步骤7
描述: 加入醋、白砂糖、酱油（老抽），翻炒均匀。
方法: 炒
工具: 锅铲
时间: 约15秒

### 第8步
步骤: 步骤8
描述: 加入冷水，刚好淹没鱼身，转中火，盖锅盖1分钟后翻面，再盖锅盖继续炖煮3-4分钟。
方法: 炖
工具: 炒锅,锅盖
时间: 约4-5分钟

### 第9步
步骤: 步骤9
描述: 加入盐、小米椒、蚝油、味精，盖锅盖继续炖煮并适时翻面。
方法: 炖
工具: 锅铲,锅盖
时间: 约2-3分钟

### 第10步
步骤: 步骤10
描述: 汤汁收至鱼鳍下方位置时转小火，加入香菜和葱花，盖锅盖20秒后关火。
方法: 焖
工具: 锅盖
时间: 20秒

### 第11步
步骤: 步骤11
描述: 起锅装盘。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (Ingredient): category: 调料
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201000040, chunk_id=201000040_chunk_11, recipe_name=水煮鱼, category=水产, score=0.6867295503616333, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 巴沙鱼若从冷冻柜取出，放室温自然解冻5小时，再切片处理。
方法: 解冻
时间: 5小时

### 第2步
步骤: 步骤2
描述: 将巴沙鱼撇成约5cm长、3cm宽的薄片。
方法: 切
工具: 刀

### 第3步
步骤: 步骤3
描述: 将鱼片放入大不锈钢碗中，加入30g豆瓣酱、3g盐、10ml藤椒油、3g白胡椒粉，用手抓匀后加入5ml菜籽油封味，常温静置至少30分钟入味。
方法: 腌制
工具: 大不锈钢碗
时间: 30分钟

### 第4步
步骤: 步骤4
描述: 大蒜切成蒜末；以300g花菜、200g生菜为例，将蔬菜洗净。
方法: 切,洗
工具: 刀,盆

### 第5步
步骤: 步骤5
描述: 花菜开水锅焯水备用；生菜洗净晾干后炒熟备用（不用放油）。
方法: 焯水,炒
工具: 锅,漏勺

### 第6步
步骤: 步骤6
描述: 热锅冷油（菜籽油20ml），加入10g豆瓣酱、10g豆豉（可选）和蒜末，中火慢炒。
方法: 炒
工具: 炒锅,锅铲

### 第7步
步骤: 步骤7
描述: 加入150ml热水，水开后放入腌制好的鱼片，轻轻翻动使其散开，加入2g盐和2g糖调味，水再次沸腾即可盛盘。
方法: 煮
工具: 锅,漏勺

### 第8步
步骤: 步骤8
描述: 先将熟蔬菜盛至大碗中，再将热鱼片铺在蔬菜上，浇上锅中剩余热汤即可。
方法: 盛盘
工具: 大碗

关联图谱:
- OUT REQUIRES 巴沙鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 蔬菜（土豆片/豆芽/花菜/生菜等） (Ingredient): category: 蔬菜
- OUT REQUIRES 红油豆瓣酱 (Ingredient): category: 调料
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6865550875663757, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 草鱼从背部切开，两面沿背部划几刀，不要划破鱼肚；用热水或刷子洗净表面粘液。
方法: 切,清洗
工具: 刀,刷子
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 鱼放入容器，加料酒、白胡椒粉、食盐抹匀，腌制二十分钟入味。
方法: 腌制
工具: 容器
时间: 20分钟

### 第3步
步骤: 步骤3
描述: 大葱切块，大蒜粒对半切，与八角、香叶、桂皮放同一容器；干辣椒段、灯笼椒切段放另一容器；芹菜切段；豆芽、千张焯水，千张切丝；洋葱切丝。
方法: 切,焯水
工具: 刀,案板,锅,漏勺
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 烤箱版：烤盘刷底油，鱼皮朝下烤至两面金黄，撒孜然粉。无烤箱版：热锅热油，锅边撒少量盐防粘，下鱼煎至两面金黄，撒孜然粉后出锅装盘。
方法: 烤,煎
工具: 烤箱/平底锅,锅铲
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 锅中倒20ml食用油，油热后下大葱、大蒜、八角、香叶炒香。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入半包火锅底料和豆瓣酱炒出红油，放白糖、食盐、生抽调味，倒入与食材齐平的清水煮开。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 3分钟

### 第7步
步骤: 步骤7
描述: 依次下芹菜段、豆芽、千张丝稍烫后铺洋葱丝，放上烤鱼，再铺干辣椒、灯笼椒、青花椒。
方法: 煮,铺
工具: 炒锅,锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 另起锅烧热油，浇在辣椒上激香，最后撒熟花生米、葱花、白芝麻、香菜，再煮5-6分钟即可。
方法: 浇油,煮
工具: 小锅,锅铲
时间: 5-6分钟

关联图谱:
- OUT REQUIRES 火锅底料 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒段 (Ingredient): category: 调料
- OUT REQUIRES 大葱 (Ingredient): category: 蔬菜
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.7116531729698181, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鱼清洗干净，确保无鱼鳞等异物
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 将鱼头朝左，鱼肚朝下，右手持刀。刀竖直切下1cm，按紧鱼身往左片3-4cm，再将鱼片中间轻轻划一刀
方法: 切
工具: 菜刀,案板

### 第3步
步骤: 步骤3
描述: 将鱼放进盆里，然后将大姜切片，大葱切段，用吃奶的力气将大葱大姜里的汁水挤到盆中
方法: 切,挤汁
工具: 盆,菜刀

### 第4步
步骤: 步骤4
描述: 加入20g盐、25g料酒，给鲤鱼搓澡，涂抹均匀，腌制30分钟以上
方法: 腌制
工具: 盆
时间: 30分钟

### 第5步
步骤: 步骤5
描述: 在干净盆中加入100g面粉、200g淀粉、180g水、5g盐，搅拌均匀后加入一个鸡蛋，再次搅匀成可拉丝面糊
方法: 搅拌
工具: 盆

### 第6步
步骤: 步骤6
描述: 等待30分钟
方法: 静置
时间: 30分钟

### 第7步
步骤: 步骤7
描述: 将鱼放在案板上，用干毛巾擦干鱼身水分，盆冲洗干净并擦干
方法: 擦干
工具: 干毛巾,盆

### 第8步
步骤: 步骤8
描述: 起锅烧油，加入约1L油，油温烧至7成热（200-240℃）
方法: 炸
工具: 锅,锅铲,笊篱

### 第9步
步骤: 步骤9
描述: 捏鱼尾，鱼头先入油锅，用勺子淋热油定型，面糊成型后整鱼入锅，用笊篱托鱼头防糊
方法: 炸
工具: 锅,锅铲,笊篱

### 第10步
步骤: 步骤10
描述: 用锅铲和笊篱配合给鱼翻身，再炸2分钟，出锅装盘
方法: 炸
工具: 锅铲,笊篱,盘子
时间: 2分钟

### 第11步
步骤: 步骤11
描述: 将锅中油倒出，锅刷干净
方法: 倒油,清洗
工具: 锅

### 第12步
步骤: 步骤12
描述: 小碗混合50g清水、40g番茄酱、20g白糖、10g白醋，搅拌均匀
方法: 搅拌
工具: 小碗

### 第13步
步骤: 步骤13
描述: 另取小碗，10g淀粉加10g水调成水淀粉
方法: 搅拌
工具: 小碗

### 第14步
步骤: 步骤14
描述: 大火烧热锅，倒入料汁，烧开后转小火，加入水淀粉边倒边搅，20秒后关火
方法: 煮,搅拌
工具: 锅,勺子
时间: 20秒

### 第15步
步骤: 步骤15
描述: 将糖醋汁均匀浇在鱼身上，撒香菜或葱花点缀即可
方法: 浇汁
工具: 勺子,盘子

关联图谱:
- OUT REQUIRES 香菜 (Ingredient): category: 蔬菜
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 番茄酱 (Ingredient): category: 调料
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.7118656635284424, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼开背杀好（让卖鱼的杀好，千万不要剖腹杀鱼，切记是开背），清洗干净
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 鱼表面用盐涂抹均匀，倒入料酒约80ml、姜末20g，放入冰箱保鲜层进行腌制1-2天
方法: 腌制
工具: 盆,冰箱
时间: 1-2天

### 第3步
步骤: 步骤3
描述: 取出腌制好的鱼，用绳挂起晾晒至半干（约1-2天，具体时间需结合气温与阳光）
方法: 晾晒
工具: 绳
时间: 1-2天

### 第4步
步骤: 步骤4
描述: 食用前请将鱼用清水清洗，沥干水分（防止水遇油飞溅）
方法: 清洗
工具: 盆

### 第5步
步骤: 步骤5
描述: 开大火将锅烧热，迅速改小火，锅中放油，尽量保持整个锅表面有油，将鱼沿锅边划入锅内（先煎鱼背面）
方法: 煎
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 鱼入锅后（和翻面后），不要着急移动鱼的位置（此时容易破皮），煎约30秒后，尝试晃动锅
方法: 煎
工具: 炒锅
时间: 30秒

### 第7步
步骤: 步骤7
描述: 背面煎约1分钟后，翻面煎约1-2分钟，煎至两面金黄
方法: 煎
工具: 锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入豆瓣酱炒出香味，放入姜蒜
方法: 炒
工具: 锅铲

### 第9步
步骤: 步骤9
描述: 炒出佐料香味后，加入料酒、生抽、老抽，倒入热水，水量和鱼平齐或者少点
方法: 炒,煮
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 此时改中大火，煮5-10分钟，后放入青椒段、白糖、鸡精、十三香、陈醋
方法: 煮
工具: 锅铲
时间: 5-10分钟

### 第11步
步骤: 步骤11
描述: 改小火2-5分钟，放入葱、香菜，即可出锅
方法: 焖
工具: 锅铲
时间: 2-5分钟

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 姜沫 (Ingredient): category: 调料
- OUT REQUIRES 料酒 (Ingredient): category: 调料
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6811927556991577, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼处理好后洗净，特别注意肚内的血丝，不洗干净会有腥味。放入大碗中，倒入料酒、10g姜片、5g盐，腌制15分钟。
方法: 腌制
工具: 碗
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 豆腐切块，放入凉水浸泡5分钟，捞出备用。
方法: 切,浸泡
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 煎鱼前，先用生姜片擦一下锅防止粘锅，倒入油（油量为15ml×鱼的条数），烧热后放入鱼煎2-3分钟，期间需要晃动一下鱼防止粘底，且需要翻一次身。
方法: 煎
工具: 炒锅,锅铲
时间: 2-3分钟

### 第4步
步骤: 步骤4
描述: 待鱼全部煎好后，倒入开水、5ml料酒、姜片，小火转至大火，盖上锅盖大火煮10分钟（水要稍微多一些，后面会蒸发掉一些）。
方法: 煮
工具: 炒锅,锅盖
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 见汤变白后倒入准备好的豆腐，调中火再煮5分钟，加入10g盐、3g胡椒粉调味，最后撒上葱花出锅。
方法: 煮,调味
工具: 锅铲
时间: 5分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
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

### result_order=10
source: reranked_results
metadata_summary: node_id=201000258, recipe_name=鲈鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲈鱼
食材名称: 鲈鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=tipdoc_9e62e8f43239, recipe_name=蒸, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧文档: 蒸
分类: 烹饪技巧
标签: 学习蒸,方式,正文,注意事项,蒸,蒸锅,铁锅
摘要: 蒸 方式 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热 铁锅 如果没有蒸锅，只有普通的铁锅 非平底锅 ，可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。 铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
来源: tips/learn/学习蒸.md

补充信息: 技巧章节: 蒸
章节: 正文
分类: 烹饪技巧
摘要: 蒸
内容: # 蒸
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201000062, recipe_name=葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 葱
食材名称: 葱
类别: 蔬菜
关联图谱:
- IN REQUIRES 清蒸生蚝 (Recipe): category: 水产；difficulty: 3.0
- IN REQUIRES 素炒豆角 (Recipe): category: 素菜；difficulty: 2.0
```

### result_order=13
source: reranked_results
metadata_summary: node_id=201000262, recipe_name=蒸鱼豉油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸鱼豉油
食材名称: 蒸鱼豉油
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201000009, recipe_name=食用油, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 食用油
食材名称: 食用油
类别: 调料
关联图谱:
- IN REQUIRES 鲤鱼炖白菜 (Recipe): category: 水产；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 青椒土豆炒肉 (Recipe): category: 荤菜；difficulty: 3.0
```

### result_order=15
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_9e62e8f43239,tipchunk_6ce348d11822,tipchunk_9f97843cc8b2,tipchunk_a06f1b706233, recipe_name=蒸, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 蒸
关键技巧内容:
## 正文
# 蒸
## 方式
## 方式
## 蒸锅
### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
## 铁锅
### 铁锅

如果没有蒸锅，只有普通的铁锅（非平底锅），可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。

铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖
## 注意事项
## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
```

### result_order=16
source: reranked_results
metadata_summary: node_id=201000001, recipe_name=咖喱炒蟹, category=水产, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 海鲜
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

### result_order=17
source: reranked_results
metadata_summary: node_id=201004117, recipe_name=炒馍, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 炒馍
分类: 主食
菜系: 西北菜
难度: 3.0
主要食材: 辣椒粉, 五香粉, 孜然粉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=18
source: reranked_results
metadata_summary: node_id=201004544, recipe_name=日式肥牛丼饭, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 去腥
菜品: 日式肥牛丼饭
分类: 主食
菜系: 日式
难度: 4.0
主要食材: 味淋, 酱油, 老抽
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=19
source: reranked_results
metadata_summary: node_id=201004928, recipe_name=松仁玉米, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 松仁玉米
分类: 素菜
难度: 2.0
主要食材: 白砂糖, 淀粉, 熟松子仁
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=20
source: reranked_results
metadata_summary: node_id=201004341, recipe_name=韭菜盒子, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=21
source: reranked_results
metadata_summary: node_id=tipchunk_9f97843cc8b2, recipe_name=蒸 / 注意事项, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 注意事项
章节: 注意事项
分类: 烹饪技巧
摘要: 注意事项 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量， 特别是铁锅 ，避免干锅从而造成安全问题。 可选 使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
内容: ## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=22
source: reranked_results
metadata_summary: node_id=tipchunk_a06f1b706233, recipe_name=蒸 / 蒸锅, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 蒸锅
章节: 蒸锅
分类: 烹饪技巧
摘要: 蒸锅 蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。 蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
内容: ### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=23
source: reranked_results
metadata_summary: node_id=201004506, recipe_name=披萨饼皮, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 披萨饼皮
分类: 主食
难度: 4.0
主要食材: 中筋面粉, 食用盐, 橄榄油
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=24
source: reranked_results
metadata_summary: node_id=tipchunk_6ce348d11822, recipe_name=蒸 / 方式, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒸锅
技巧章节: 蒸 / 方式
章节: 方式
分类: 烹饪技巧
摘要: 方式
内容: ## 方式
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueChunk (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
```

### result_order=25
source: reranked_results
metadata_summary: node_id=201000519, recipe_name=太阳蛋, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 火候
菜品: 太阳蛋
分类: 早餐
难度: 2.0
主要食材: 盐, 鸡蛋, 油
关联图谱:
- OUT REQUIRES 盐 (Ingredient): category: 调料
- OUT REQUIRES 鸡蛋 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=26
source: reranked_results
metadata_summary: node_id=201000027, recipe_name=姜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 姜
食材名称: 姜
类别: 蔬菜
关联图谱:
- IN REQUIRES 香煎五花肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 地三鲜 (Recipe): category: 素菜；cuisineType: 东北菜；difficulty: 3.0
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.7811521887779236, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片切丝、香葱的葱白切段，葱绿切丝，切丝后放入冷水浸泡备用。
方法: 切
工具: 刀,案板,冷水碗
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鲈鱼处理好后洗净，用厨房纸擦干，两面分别划几刀，用盐洗掉鱼身的粘液，并用10g盐抹遍鱼身的内外，腌制10分钟以上。
方法: 洗,腌制,切
工具: 厨房纸,刀,案板,盆
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼肚内塞上姜和葱白，鱼身也撒上姜和葱白，量为备用的一半。蒸鱼的碟子用筷子将鱼跟碟子隔开蒸。
方法: 摆盘
工具: 碟子,筷子
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 水烧热感觉到水温后放进入鱼，大火清蒸10分钟。
方法: 蒸
工具: 蒸锅,大火
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 蒸好的鱼，用干净的盘子装起来并去除身上姜蒜。
方法: 装盘
工具: 干净盘子,筷子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 鱼身浇上15ml蒸鱼豉油。
方法: 浇汁
工具: 量勺
时间: 15秒

### 第7步
步骤: 步骤7
描述: 鱼身重新撒上姜和葱丝，锅内加上10ml食用油并烧热，将食用油淋至鱼身即可出菜。
方法: 淋油
工具: 锅,量勺,锅铲
时间: 30秒

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.6738912463188171, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳜鱼从腹部切开，去除鱼鳃和内脏，打去鱼鳞，用刀在表皮上刮去粘液（可让摊主代劳）
方法: 切,清理
工具: 刀

### 第2步
步骤: 步骤2
描述: 鳜鱼身上打上花刀，放姜片，可放少许猪油，装盘并在下面垫筷子以便受热均匀
方法: 切,摆盘
工具: 刀,筷子

### 第3步
步骤: 步骤3
描述: 大葱划开后去除中间的芯，只保留外面两层；小葱划开备用；红椒去籽去肉备用
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 将大葱、小葱、辣椒码在一起切成丝，泡在水里备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 锅中加大量水，水热后放入鳜鱼，盖上锅盖，大火蒸8-10分钟
方法: 蒸
工具: 蒸锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 蒸鱼期间另起一锅烧热油至冒烟
方法: 加热
工具: 锅

### 第7步
步骤: 步骤7
描述: 蒸好后倒掉蒸鱼的水，去除姜片，放上葱丝，浇上热油
方法: 倒,淋
工具: 锅,筷子

### 第8步
步骤: 步骤8
描述: 倒入生抽或蒸鱼豉油即可上桌
方法: 淋

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6931073665618896, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜蒜切碎，干辣椒切碎，与姜蒜一起备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第2步
步骤: 步骤2
描述: 锅中加入30-50ml油，小火加热至锅热。
方法: 加热
工具: 炒锅
时间: 约30秒

### 第3步
步骤: 步骤3
描述: 将擦干水分的鱼放入锅中，小火煎至底部金黄，期间晃动锅防止粘锅。
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 翻面，重复煎另一面至金黄。
方法: 煎
工具: 锅铲
时间: 约2-3分钟

### 第5步
步骤: 步骤5
描述: 加入姜蒜辣椒碎，翻炒出香味。
方法: 炒
工具: 锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 倒入适量料酒，迅速产生大量油烟，注意安全。
方法: 炝锅
工具: 锅铲
时间: 约15秒

### 第7步
步骤: 步骤7
描述: 加入醋、白砂糖、酱油（老抽），翻炒均匀。
方法: 炒
工具: 锅铲
时间: 约15秒

### 第8步
步骤: 步骤8
描述: 加入冷水，刚好淹没鱼身，转中火，盖锅盖1分钟后翻面，再盖锅盖继续炖煮3-4分钟。
方法: 炖
工具: 炒锅,锅盖
时间: 约4-5分钟

### 第9步
步骤: 步骤9
描述: 加入盐、小米椒、蚝油、味精，盖锅盖继续炖煮并适时翻面。
方法: 炖
工具: 锅铲,锅盖
时间: 约2-3分钟

### 第10步
步骤: 步骤10
描述: 汤汁收至鱼鳍下方位置时转小火，加入香菜和葱花，盖锅盖20秒后关火。
方法: 焖
工具: 锅盖
时间: 20秒

### 第11步
步骤: 步骤11
描述: 起锅装盘。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (Ingredient): category: 调料
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6811927556991577, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼处理好后洗净，特别注意肚内的血丝，不洗干净会有腥味。放入大碗中，倒入料酒、10g姜片、5g盐，腌制15分钟。
方法: 腌制
工具: 碗
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 豆腐切块，放入凉水浸泡5分钟，捞出备用。
方法: 切,浸泡
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 煎鱼前，先用生姜片擦一下锅防止粘锅，倒入油（油量为15ml×鱼的条数），烧热后放入鱼煎2-3分钟，期间需要晃动一下鱼防止粘底，且需要翻一次身。
方法: 煎
工具: 炒锅,锅铲
时间: 2-3分钟

### 第4步
步骤: 步骤4
描述: 待鱼全部煎好后，倒入开水、5ml料酒、姜片，小火转至大火，盖上锅盖大火煮10分钟（水要稍微多一些，后面会蒸发掉一些）。
方法: 煮
工具: 炒锅,锅盖
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 见汤变白后倒入准备好的豆腐，调中火再煮5分钟，加入10g盐、3g胡椒粉调味，最后撒上葱花出锅。
方法: 煮,调味
工具: 锅铲
时间: 5分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_9e62e8f43239,tipchunk_6ce348d11822,tipchunk_9f97843cc8b2,tipchunk_a06f1b706233, recipe_name=蒸, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 蒸
关键技巧内容:
## 正文
# 蒸
## 方式
## 方式
## 蒸锅
### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
## 铁锅
### 铁锅

如果没有蒸锅，只有普通的铁锅（非平底锅），可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。

铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖
## 注意事项
## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.7811521887779236, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片切丝、香葱的葱白切段，葱绿切丝，切丝后放入冷水浸泡备用。
方法: 切
工具: 刀,案板,冷水碗
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鲈鱼处理好后洗净，用厨房纸擦干，两面分别划几刀，用盐洗掉鱼身的粘液，并用10g盐抹遍鱼身的内外，腌制10分钟以上。
方法: 洗,腌制,切
工具: 厨房纸,刀,案板,盆
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼肚内塞上姜和葱白，鱼身也撒上姜和葱白，量为备用的一半。蒸鱼的碟子用筷子将鱼跟碟子隔开蒸。
方法: 摆盘
工具: 碟子,筷子
时间: 1分钟

### 第4步
步骤: 步骤4
描述: 水烧热感觉到水温后放进入鱼，大火清蒸10分钟。
方法: 蒸
工具: 蒸锅,大火
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 蒸好的鱼，用干净的盘子装起来并去除身上姜蒜。
方法: 装盘
工具: 干净盘子,筷子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 鱼身浇上15ml蒸鱼豉油。
方法: 浇汁
工具: 量勺
时间: 15秒

### 第7步
步骤: 步骤7
描述: 鱼身重新撒上姜和葱丝，锅内加上10ml食用油并烧热，将食用油淋至鱼身即可出菜。
方法: 淋油
工具: 锅,量勺,锅铲
时间: 30秒

关联图谱:
- OUT REQUIRES 香葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 鲈鱼 (Ingredient): category: 蛋白质
- OUT REQUIRES 食用盐 (Ingredient): category: 调料
```

### result_order=1
source: generation_context
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.6738912463188171, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳜鱼从腹部切开，去除鱼鳃和内脏，打去鱼鳞，用刀在表皮上刮去粘液（可让摊主代劳）
方法: 切,清理
工具: 刀

### 第2步
步骤: 步骤2
描述: 鳜鱼身上打上花刀，放姜片，可放少许猪油，装盘并在下面垫筷子以便受热均匀
方法: 切,摆盘
工具: 刀,筷子

### 第3步
步骤: 步骤3
描述: 大葱划开后去除中间的芯，只保留外面两层；小葱划开备用；红椒去籽去肉备用
方法: 切
工具: 刀

### 第4步
步骤: 步骤4
描述: 将大葱、小葱、辣椒码在一起切成丝，泡在水里备用
方法: 切
工具: 刀

### 第5步
步骤: 步骤5
描述: 锅中加大量水，水热后放入鳜鱼，盖上锅盖，大火蒸8-10分钟
方法: 蒸
工具: 蒸锅,锅盖
时间: 8-10分钟

### 第6步
步骤: 步骤6
描述: 蒸鱼期间另起一锅烧热油至冒烟
方法: 加热
工具: 锅

### 第7步
步骤: 步骤7
描述: 蒸好后倒掉蒸鱼的水，去除姜片，放上葱丝，浇上热油
方法: 倒,淋
工具: 锅,筷子

### 第8步
步骤: 步骤8
描述: 倒入生抽或蒸鱼豉油即可上桌
方法: 淋

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: generation_context
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6931073665618896, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜蒜切碎，干辣椒切碎，与姜蒜一起备用。
方法: 切
工具: 刀,案板
时间: 约3分钟

### 第2步
步骤: 步骤2
描述: 锅中加入30-50ml油，小火加热至锅热。
方法: 加热
工具: 炒锅
时间: 约30秒

### 第3步
步骤: 步骤3
描述: 将擦干水分的鱼放入锅中，小火煎至底部金黄，期间晃动锅防止粘锅。
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 翻面，重复煎另一面至金黄。
方法: 煎
工具: 锅铲
时间: 约2-3分钟

### 第5步
步骤: 步骤5
描述: 加入姜蒜辣椒碎，翻炒出香味。
方法: 炒
工具: 锅铲
时间: 约30秒

### 第6步
步骤: 步骤6
描述: 倒入适量料酒，迅速产生大量油烟，注意安全。
方法: 炝锅
工具: 锅铲
时间: 约15秒

### 第7步
步骤: 步骤7
描述: 加入醋、白砂糖、酱油（老抽），翻炒均匀。
方法: 炒
工具: 锅铲
时间: 约15秒

### 第8步
步骤: 步骤8
描述: 加入冷水，刚好淹没鱼身，转中火，盖锅盖1分钟后翻面，再盖锅盖继续炖煮3-4分钟。
方法: 炖
工具: 炒锅,锅盖
时间: 约4-5分钟

### 第9步
步骤: 步骤9
描述: 加入盐、小米椒、蚝油、味精，盖锅盖继续炖煮并适时翻面。
方法: 炖
工具: 锅铲,锅盖
时间: 约2-3分钟

### 第10步
步骤: 步骤10
描述: 汤汁收至鱼鳍下方位置时转小火，加入香菜和葱花，盖锅盖20秒后关火。
方法: 焖
工具: 锅盖
时间: 20秒

### 第11步
步骤: 步骤11
描述: 起锅装盘。
方法: 装盘
工具: 锅铲
时间: 约10秒

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (Ingredient): category: 调料
```

### result_order=3
source: generation_context
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6811927556991577, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鱼处理好后洗净，特别注意肚内的血丝，不洗干净会有腥味。放入大碗中，倒入料酒、10g姜片、5g盐，腌制15分钟。
方法: 腌制
工具: 碗
时间: 15分钟

### 第2步
步骤: 步骤2
描述: 豆腐切块，放入凉水浸泡5分钟，捞出备用。
方法: 切,浸泡
工具: 刀,案板,盆
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 煎鱼前，先用生姜片擦一下锅防止粘锅，倒入油（油量为15ml×鱼的条数），烧热后放入鱼煎2-3分钟，期间需要晃动一下鱼防止粘底，且需要翻一次身。
方法: 煎
工具: 炒锅,锅铲
时间: 2-3分钟

### 第4步
步骤: 步骤4
描述: 待鱼全部煎好后，倒入开水、5ml料酒、姜片，小火转至大火，盖上锅盖大火煮10分钟（水要稍微多一些，后面会蒸发掉一些）。
方法: 煮
工具: 炒锅,锅盖
时间: 10分钟

### 第5步
步骤: 步骤5
描述: 见汤变白后倒入准备好的豆腐，调中火再煮5分钟，加入10g盐、3g胡椒粉调味，最后撒上葱花出锅。
方法: 煮,调味
工具: 锅铲
时间: 5分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT BELONGS_TO 汤类 (RecipeCategory)
```

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_9e62e8f43239,tipchunk_6ce348d11822,tipchunk_9f97843cc8b2,tipchunk_a06f1b706233, recipe_name=蒸, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 蒸
关键技巧内容:
## 正文
# 蒸
## 方式
## 方式
## 蒸锅
### 蒸锅

蒸锅为多层结构，最底部用于盛水，利用水开后产生的水蒸气的热量，加热上层食物。

蒸锅最底层加入适量水——将食物放于上层蒸屉中——蒸锅放于火上加热
## 铁锅
### 铁锅

如果没有蒸锅，只有普通的铁锅（非平底锅），可以在锅底放置一个三脚架，并注入足够的水，以此达到类似于蒸锅的效果。

铁锅底部加入足量水———放入三脚架———将食物置于三脚架上———开火关盖
## 注意事项
## 注意事项

* 由于热源为水蒸气，较低的蒸屉中的食物底部可能被水浸湿。可将蒸笼布放在食物底下以避免这种情况。用筷子搭个放食物的简易支架也可以。
* 可以利用智能设备设置计时器，提醒关火，以防忘记以致烧干。
* 在使用蒸笼制作食品的过程中，需要注意底部区域的剩余水量，**特别是铁锅**，避免干锅从而造成安全问题。
* （可选）使用铁锅蒸食物时，可以在三脚架上面放置一个蒸盘。
```

