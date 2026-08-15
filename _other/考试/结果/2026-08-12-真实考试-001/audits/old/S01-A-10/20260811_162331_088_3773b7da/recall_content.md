# Recall Content

audit_id: 20260811_162331_088_3773b7da
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201000100, recipe_name=红烧鱼头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 红烧鱼头
菜品名称: 红烧鱼头
分类: 水产
难度: 4.0
关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
```

### result_order=1
source: entity_level
metadata_summary: node_id=201000101, recipe_name=鱼头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鱼头
食材名称: 鱼头
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: entity_level
metadata_summary: node_id=201000193, recipe_name=生姜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 生姜
食材名称: 生姜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=3
source: entity_level
metadata_summary: node_id=201000102, recipe_name=大葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 大葱
食材名称: 大葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=4
source: entity_level
metadata_summary: node_id=201000008, recipe_name=大蒜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 大蒜
食材名称: 大蒜
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=5
source: entity_level
metadata_summary: node_id=201000028, recipe_name=料酒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 料酒
食材名称: 料酒
类别: 调料
关联图谱:
- IN REQUIRES 茭白炒肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 商芝肉 (Recipe): category: 荤菜；cuisineType: 西北菜；difficulty: 5.0
```

### result_order=6
source: entity_level
metadata_summary: node_id=201000112, recipe_name=生抽, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 生抽
食材名称: 生抽
类别: 调料
关联图谱:
- IN REQUIRES 茶叶蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 香辣鸡爪煲 (Recipe): category: 荤菜；cuisineType: 川菜；difficulty: 4.0
```

### result_order=7
source: entity_level
metadata_summary: node_id=201000113, recipe_name=老抽, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 老抽
食材名称: 老抽
类别: 调料
关联图谱:
- IN REQUIRES 酱牛肉 (Recipe): category: 荤菜；difficulty: 5.0
- IN REQUIRES 乡村啤酒鸭 (Recipe): category: 荤菜；difficulty: 4.0
```

### result_order=8
source: entity_level
metadata_summary: node_id=201000134, recipe_name=白糖, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 白糖
食材名称: 白糖
类别: 调料
关联图谱:
- IN REQUIRES 凉粉 (Recipe): category: 主食；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 微波炉蛋糕 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=9
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

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201004466, recipe_name=意式肉酱面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 意式肉酱面
分类: 主食
菜系: 意大利
难度: 1.0
主要食材: 食用油, 肉沫, 意大利面
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: topic_level
metadata_summary: node_id=201005481, recipe_name=炒滑蛋, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炒滑蛋
分类: 素菜
难度: 1.0
主要食材: 牛奶, 鸡蛋, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=2
source: topic_level
metadata_summary: node_id=201005312, recipe_name=凉拌木耳, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 凉拌木耳
分类: 素菜
难度: 2.0
主要食材: 干木耳, 盐, 白糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=3
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

### result_order=4
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

### result_order=5
source: topic_level
metadata_summary: node_id=201000775, recipe_name=炸串酱料, category=调料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炸串酱料
分类: 调料
难度: 2.0
主要食材: 五香粉, 鸡精, 麻辣鲜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=6
source: topic_level
metadata_summary: node_id=201000628, recipe_name=燕麦鸡蛋饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=7
source: topic_level
metadata_summary: node_id=201005272, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 鸡蛋火腿炒黄瓜
分类: 素菜
难度: 2.0
主要食材: 生抽, 火腿肠, 鸡蛋
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
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

### result_order=9
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

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201000100, chunk_id=201000100_chunk_20, recipe_name=红烧鱼头, category=水产, score=0.7892471551895142, search_type=vector_enhanced

```text
# 红烧鱼头
难度: 4.0星

时间信息: 准备时间: 1-2小时（腌制）+ 15分钟（切配）, 烹饪时间: 约30分钟（炒制+焖煮+收汁）
份量: 2人

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_16, recipe_name=红烧鱼, category=水产, score=0.7241820693016052, search_type=vector_enhanced

```text
# 红烧鱼
难度: 4.0星

时间信息: 准备时间: 约10分钟（切配姜蒜辣椒、处理鱼）, 烹饪时间: 约8-10分钟（煎鱼+炖煮+收汁）
份量: 1条鱼（1-2人）

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (Ingredient): category: 调料
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.72178053855896, search_type=vector_enhanced

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

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201000100, chunk_id=201000100_chunk_22, recipe_name=红烧鱼头, category=水产, score=0.7139914631843567, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、香菜、美人椒分别清洗干净；干辣椒与八角稍微冲洗。
方法: 清洗
工具: 刀,案板,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 大葱切两半：葱白切段约4 cm，葱叶切段后劈四瓣；姜切3 mm片；蒜拍碎；两棵香菜切1.5 cm碎；美人椒切3 mm圈；干辣椒切四段。
方法: 切
工具: 刀,案板
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼头去鳞、清理内脏、剁去鱼鳍、清理鱼鳃，将鱼头下巴与鱼身连接处剁开，鱼身切块，鱼头剁成4-6瓣，再次清洗血水。
方法: 剁,清洗
工具: 菜刀,盆
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 将鱼块放入盆中，加5 g盐、10 g生抽、10 g料酒、切碎的葱叶段、1/3姜片拌匀，静置腌制1-2小时。
方法: 腌制
工具: 盆
时间: 1-2小时

### 第5步
步骤: 步骤5
描述: 锅中加30 ml油，小火加热，放入姜片炒至金黄出汁。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第6步
步骤: 步骤6
描述: 加入葱白段翻炒至略发白，再加入蒜碎、八角、干辣椒翻炒5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 倒入腌制好的鱼头翻炒2-3分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 加入500 ml清水，调入2 g盐、3 g鸡精、5 g生抽、3 g老抽、5 g料酒、2 g黑胡椒粉、3 g陈醋，放入两棵香菜，盖锅盖，大火烧开后转中火慢焖。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第9步
步骤: 步骤9
描述: 汤汁减半时开盖，大火收汁至剩余1/3，关火。将汤汁均匀淋在鱼头上，香菜垫底装饰，再放上剩余香菜和美人椒圈。
方法: 收汁,装盘
工具: 锅铲,小盆
时间: 5分钟

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6915249228477478, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201000127, chunk_id=201000127_chunk_26, recipe_name=红烧鲤鱼, category=水产, score=0.6840590834617615, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、干辣椒分别清洗干净。
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 葱白处切段，每段长度约4cm，再将每段劈为四瓣。
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 姜切片，每片厚度约3mm。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 一个大蒜拍碎切末，其余蒜切为二瓣。
方法: 拍,切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 干辣椒切四段。
方法: 切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 五花肉切片，约4cm×4cm。
方法: 切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 清洗鱼。
方法: 清洗
工具: 盆

### 第8步
步骤: 步骤8
描述: 鱼背肉厚处拉几道斜口，方便入味。
方法: 切
工具: 刀,案板

### 第9步
步骤: 步骤9
描述: 锅里多倒点油，烧至7成热（刚刚开始冒烟），下入鱼炸1分钟至鱼皮稍稍变硬捞出备用，炸鱼的油倒出，锅里留一点底油。
方法: 炸
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 将锅里底油烧热，下入五花肉，煸出香味。
方法: 煸
工具: 炒锅,锅铲

### 第11步
步骤: 步骤11
描述: 放入干辣椒、葱、姜、蒜瓣，翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第12步
步骤: 步骤12
描述: 将炸好的鱼倒入锅中。
方法: 倒
工具: 锅铲

### 第13步
步骤: 步骤13
描述: 沿锅边倒入料酒50ml、陈醋50ml、味极鲜50ml、老抽20ml、蚝油5ml、盐5g、白糖50g、清水没过鱼面。
方法: 倒
工具: 锅铲

### 第14步
步骤: 步骤14
描述: 调至中火，将水烧开。
方法: 烧
工具: 炒锅

### 第15步
步骤: 步骤15
描述: 调至小火，慢焖入味。
方法: 焖
工具: 炒锅,锅盖

### 第16步
步骤: 步骤16
描述: 15分钟后，打开锅盖，挑出锅里的葱、姜、蒜、干辣椒。
方法: 挑
工具: 筷子
时间: 15分钟

### 第17步
步骤: 步骤17
描述: 调至大火收汁，汤汁剩余1/4时，撒点蒜末，关火盛出。
方法: 收汁,撒,关火
工具: 锅铲

关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6826379299163818, search_type=vector_enhanced

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

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.6757845282554626, search_type=vector_enhanced

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

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6725603342056274, search_type=vector_enhanced

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
metadata_summary: node_id=201000453, chunk_id=201000453_chunk_83, recipe_name=鲤鱼炖白菜, category=水产, score=0.6721473932266235, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲤鱼清洗干净，改刀（在鱼身上多划几个伤口，方便入味）
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 娃娃菜清洗干净放入盘中备用
方法: 清洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 锅中加油，等油热放入“少盐”“姜”“蒜”“郫县豆瓣酱”“桂皮”“八角”炒出香味
方法: 炒
工具: 锅,锅铲

### 第4步
步骤: 步骤4
描述: 把鱼放锅里煎（3分钟）每30秒需要翻面
方法: 煎
工具: 锅,锅铲
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 加入“水”（水量尽量和鱼平齐，可以少一点点）放入“生抽”“老抽”“娃娃菜”
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 大火炖15-20分钟，汤汁快干时添加“盐”即可出锅
方法: 炖
工具: 锅
时间: 15-20分钟

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201000100, recipe_name=红烧鱼头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 红烧鱼头
菜品名称: 红烧鱼头
分类: 水产
难度: 4.0
关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201000101, recipe_name=鱼头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鱼头
食材名称: 鱼头
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000193, recipe_name=生姜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 生姜
食材名称: 生姜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=3
source: branch_grouped
metadata_summary: node_id=201000102, recipe_name=大葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 大葱
食材名称: 大葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201000008, recipe_name=大蒜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 大蒜
食材名称: 大蒜
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201000028, recipe_name=料酒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 料酒
食材名称: 料酒
类别: 调料
关联图谱:
- IN REQUIRES 茭白炒肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 商芝肉 (Recipe): category: 荤菜；cuisineType: 西北菜；difficulty: 5.0
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201000112, recipe_name=生抽, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 生抽
食材名称: 生抽
类别: 调料
关联图谱:
- IN REQUIRES 茶叶蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 香辣鸡爪煲 (Recipe): category: 荤菜；cuisineType: 川菜；difficulty: 4.0
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201000113, recipe_name=老抽, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 老抽
食材名称: 老抽
类别: 调料
关联图谱:
- IN REQUIRES 酱牛肉 (Recipe): category: 荤菜；difficulty: 5.0
- IN REQUIRES 乡村啤酒鸭 (Recipe): category: 荤菜；difficulty: 4.0
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201000134, recipe_name=白糖, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 白糖
食材名称: 白糖
类别: 调料
关联图谱:
- IN REQUIRES 凉粉 (Recipe): category: 主食；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 微波炉蛋糕 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=9
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

### result_order=10
source: branch_grouped
metadata_summary: node_id=201004466, recipe_name=意式肉酱面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 意式肉酱面
分类: 主食
菜系: 意大利
难度: 1.0
主要食材: 食用油, 肉沫, 意大利面
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201005481, recipe_name=炒滑蛋, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炒滑蛋
分类: 素菜
难度: 1.0
主要食材: 牛奶, 鸡蛋, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201005312, recipe_name=凉拌木耳, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 凉拌木耳
分类: 素菜
难度: 2.0
主要食材: 干木耳, 盐, 白糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=13
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

### result_order=14
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

### result_order=15
source: branch_grouped
metadata_summary: node_id=201000775, recipe_name=炸串酱料, category=调料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炸串酱料
分类: 调料
难度: 2.0
主要食材: 五香粉, 鸡精, 麻辣鲜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=16
source: branch_grouped
metadata_summary: node_id=201000628, recipe_name=燕麦鸡蛋饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=17
source: branch_grouped
metadata_summary: node_id=201005272, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 鸡蛋火腿炒黄瓜
分类: 素菜
难度: 2.0
主要食材: 生抽, 火腿肠, 鸡蛋
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=18
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

### result_order=19
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

### result_order=20
source: branch_grouped
metadata_summary: node_id=201000100, chunk_id=201000100_chunk_20, recipe_name=红烧鱼头, category=水产, score=0.7892471551895142, search_type=vector_enhanced

```text
# 红烧鱼头
难度: 4.0星

时间信息: 准备时间: 1-2小时（腌制）+ 15分钟（切配）, 烹饪时间: 约30分钟（炒制+焖煮+收汁）
份量: 2人

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=21
source: branch_grouped
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_16, recipe_name=红烧鱼, category=水产, score=0.7241820693016052, search_type=vector_enhanced

```text
# 红烧鱼
难度: 4.0星

时间信息: 准备时间: 约10分钟（切配姜蒜辣椒、处理鱼）, 烹饪时间: 约8-10分钟（煎鱼+炖煮+收汁）
份量: 1条鱼（1-2人）

关联图谱:
- OUT REQUIRES 油 (Ingredient): category: 调料
- OUT REQUIRES 酱油 (Ingredient): category: 调料
- OUT REQUIRES 味精 (Ingredient): category: 调料
```

### result_order=22
source: branch_grouped
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.72178053855896, search_type=vector_enhanced

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

### result_order=23
source: branch_grouped
metadata_summary: node_id=201000100, chunk_id=201000100_chunk_22, recipe_name=红烧鱼头, category=水产, score=0.7139914631843567, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、香菜、美人椒分别清洗干净；干辣椒与八角稍微冲洗。
方法: 清洗
工具: 刀,案板,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 大葱切两半：葱白切段约4 cm，葱叶切段后劈四瓣；姜切3 mm片；蒜拍碎；两棵香菜切1.5 cm碎；美人椒切3 mm圈；干辣椒切四段。
方法: 切
工具: 刀,案板
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼头去鳞、清理内脏、剁去鱼鳍、清理鱼鳃，将鱼头下巴与鱼身连接处剁开，鱼身切块，鱼头剁成4-6瓣，再次清洗血水。
方法: 剁,清洗
工具: 菜刀,盆
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 将鱼块放入盆中，加5 g盐、10 g生抽、10 g料酒、切碎的葱叶段、1/3姜片拌匀，静置腌制1-2小时。
方法: 腌制
工具: 盆
时间: 1-2小时

### 第5步
步骤: 步骤5
描述: 锅中加30 ml油，小火加热，放入姜片炒至金黄出汁。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第6步
步骤: 步骤6
描述: 加入葱白段翻炒至略发白，再加入蒜碎、八角、干辣椒翻炒5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 倒入腌制好的鱼头翻炒2-3分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 加入500 ml清水，调入2 g盐、3 g鸡精、5 g生抽、3 g老抽、5 g料酒、2 g黑胡椒粉、3 g陈醋，放入两棵香菜，盖锅盖，大火烧开后转中火慢焖。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第9步
步骤: 步骤9
描述: 汤汁减半时开盖，大火收汁至剩余1/3，关火。将汤汁均匀淋在鱼头上，香菜垫底装饰，再放上剩余香菜和美人椒圈。
方法: 收汁,装盘
工具: 锅铲,小盆
时间: 5分钟

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=24
source: branch_grouped
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6915249228477478, search_type=vector_enhanced

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

### result_order=25
source: branch_grouped
metadata_summary: node_id=201000127, chunk_id=201000127_chunk_26, recipe_name=红烧鲤鱼, category=水产, score=0.6840590834617615, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、干辣椒分别清洗干净。
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 葱白处切段，每段长度约4cm，再将每段劈为四瓣。
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 姜切片，每片厚度约3mm。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 一个大蒜拍碎切末，其余蒜切为二瓣。
方法: 拍,切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 干辣椒切四段。
方法: 切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 五花肉切片，约4cm×4cm。
方法: 切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 清洗鱼。
方法: 清洗
工具: 盆

### 第8步
步骤: 步骤8
描述: 鱼背肉厚处拉几道斜口，方便入味。
方法: 切
工具: 刀,案板

### 第9步
步骤: 步骤9
描述: 锅里多倒点油，烧至7成热（刚刚开始冒烟），下入鱼炸1分钟至鱼皮稍稍变硬捞出备用，炸鱼的油倒出，锅里留一点底油。
方法: 炸
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 将锅里底油烧热，下入五花肉，煸出香味。
方法: 煸
工具: 炒锅,锅铲

### 第11步
步骤: 步骤11
描述: 放入干辣椒、葱、姜、蒜瓣，翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第12步
步骤: 步骤12
描述: 将炸好的鱼倒入锅中。
方法: 倒
工具: 锅铲

### 第13步
步骤: 步骤13
描述: 沿锅边倒入料酒50ml、陈醋50ml、味极鲜50ml、老抽20ml、蚝油5ml、盐5g、白糖50g、清水没过鱼面。
方法: 倒
工具: 锅铲

### 第14步
步骤: 步骤14
描述: 调至中火，将水烧开。
方法: 烧
工具: 炒锅

### 第15步
步骤: 步骤15
描述: 调至小火，慢焖入味。
方法: 焖
工具: 炒锅,锅盖

### 第16步
步骤: 步骤16
描述: 15分钟后，打开锅盖，挑出锅里的葱、姜、蒜、干辣椒。
方法: 挑
工具: 筷子
时间: 15分钟

### 第17步
步骤: 步骤17
描述: 调至大火收汁，汤汁剩余1/4时，撒点蒜末，关火盛出。
方法: 收汁,撒,关火
工具: 锅铲

关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=26
source: branch_grouped
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6826379299163818, search_type=vector_enhanced

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

### result_order=27
source: branch_grouped
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.6757845282554626, search_type=vector_enhanced

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

### result_order=28
source: branch_grouped
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6725603342056274, search_type=vector_enhanced

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
metadata_summary: node_id=201000453, chunk_id=201000453_chunk_83, recipe_name=鲤鱼炖白菜, category=水产, score=0.6721473932266235, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲤鱼清洗干净，改刀（在鱼身上多划几个伤口，方便入味）
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 娃娃菜清洗干净放入盘中备用
方法: 清洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 锅中加油，等油热放入“少盐”“姜”“蒜”“郫县豆瓣酱”“桂皮”“八角”炒出香味
方法: 炒
工具: 锅,锅铲

### 第4步
步骤: 步骤4
描述: 把鱼放锅里煎（3分钟）每30秒需要翻面
方法: 煎
工具: 锅,锅铲
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 加入“水”（水量尽量和鱼平齐，可以少一点点）放入“生抽”“老抽”“娃娃菜”
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 大火炖15-20分钟，汤汁快干时添加“盐”即可出锅
方法: 炖
工具: 锅
时间: 15-20分钟

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201000100, chunk_id=201000100_chunk_22, recipe_name=红烧鱼头, category=水产, score=0.7139914631843567, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、香菜、美人椒分别清洗干净；干辣椒与八角稍微冲洗。
方法: 清洗
工具: 刀,案板,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 大葱切两半：葱白切段约4 cm，葱叶切段后劈四瓣；姜切3 mm片；蒜拍碎；两棵香菜切1.5 cm碎；美人椒切3 mm圈；干辣椒切四段。
方法: 切
工具: 刀,案板
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼头去鳞、清理内脏、剁去鱼鳍、清理鱼鳃，将鱼头下巴与鱼身连接处剁开，鱼身切块，鱼头剁成4-6瓣，再次清洗血水。
方法: 剁,清洗
工具: 菜刀,盆
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 将鱼块放入盆中，加5 g盐、10 g生抽、10 g料酒、切碎的葱叶段、1/3姜片拌匀，静置腌制1-2小时。
方法: 腌制
工具: 盆
时间: 1-2小时

### 第5步
步骤: 步骤5
描述: 锅中加30 ml油，小火加热，放入姜片炒至金黄出汁。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第6步
步骤: 步骤6
描述: 加入葱白段翻炒至略发白，再加入蒜碎、八角、干辣椒翻炒5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 倒入腌制好的鱼头翻炒2-3分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 加入500 ml清水，调入2 g盐、3 g鸡精、5 g生抽、3 g老抽、5 g料酒、2 g黑胡椒粉、3 g陈醋，放入两棵香菜，盖锅盖，大火烧开后转中火慢焖。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第9步
步骤: 步骤9
描述: 汤汁减半时开盖，大火收汁至剩余1/3，关火。将汤汁均匀淋在鱼头上，香菜垫底装饰，再放上剩余香菜和美人椒圈。
方法: 收汁,装盘
工具: 锅铲,小盆
时间: 5分钟

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201000101, recipe_name=鱼头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鱼头
食材名称: 鱼头
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000193, recipe_name=生姜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 生姜
食材名称: 生姜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=3
source: merged_candidates
metadata_summary: node_id=201000102, recipe_name=大葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 大葱
食材名称: 大葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201000008, recipe_name=大蒜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 大蒜
食材名称: 大蒜
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201000028, recipe_name=料酒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 料酒
食材名称: 料酒
类别: 调料
关联图谱:
- IN REQUIRES 茭白炒肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 商芝肉 (Recipe): category: 荤菜；cuisineType: 西北菜；difficulty: 5.0
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201000112, recipe_name=生抽, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 生抽
食材名称: 生抽
类别: 调料
关联图谱:
- IN REQUIRES 茶叶蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 香辣鸡爪煲 (Recipe): category: 荤菜；cuisineType: 川菜；difficulty: 4.0
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201000113, recipe_name=老抽, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 老抽
食材名称: 老抽
类别: 调料
关联图谱:
- IN REQUIRES 酱牛肉 (Recipe): category: 荤菜；difficulty: 5.0
- IN REQUIRES 乡村啤酒鸭 (Recipe): category: 荤菜；difficulty: 4.0
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201000134, recipe_name=白糖, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 白糖
食材名称: 白糖
类别: 调料
关联图谱:
- IN REQUIRES 凉粉 (Recipe): category: 主食；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 微波炉蛋糕 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=9
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

### result_order=10
source: merged_candidates
metadata_summary: node_id=201004466, recipe_name=意式肉酱面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 意式肉酱面
分类: 主食
菜系: 意大利
难度: 1.0
主要食材: 食用油, 肉沫, 意大利面
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201005481, recipe_name=炒滑蛋, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炒滑蛋
分类: 素菜
难度: 1.0
主要食材: 牛奶, 鸡蛋, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201005312, recipe_name=凉拌木耳, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 凉拌木耳
分类: 素菜
难度: 2.0
主要食材: 干木耳, 盐, 白糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=13
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

### result_order=14
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

### result_order=15
source: merged_candidates
metadata_summary: node_id=201000775, recipe_name=炸串酱料, category=调料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炸串酱料
分类: 调料
难度: 2.0
主要食材: 五香粉, 鸡精, 麻辣鲜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=16
source: merged_candidates
metadata_summary: node_id=201000628, recipe_name=燕麦鸡蛋饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=17
source: merged_candidates
metadata_summary: node_id=201005272, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 鸡蛋火腿炒黄瓜
分类: 素菜
难度: 2.0
主要食材: 生抽, 火腿肠, 鸡蛋
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=18
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

### result_order=19
source: merged_candidates
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

### result_order=20
source: merged_candidates
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6826379299163818, search_type=vector_enhanced

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

### result_order=21
source: merged_candidates
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.72178053855896, search_type=vector_enhanced

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

### result_order=22
source: merged_candidates
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6915249228477478, search_type=vector_enhanced

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

### result_order=23
source: merged_candidates
metadata_summary: node_id=201000127, chunk_id=201000127_chunk_26, recipe_name=红烧鲤鱼, category=水产, score=0.6840590834617615, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、干辣椒分别清洗干净。
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 葱白处切段，每段长度约4cm，再将每段劈为四瓣。
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 姜切片，每片厚度约3mm。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 一个大蒜拍碎切末，其余蒜切为二瓣。
方法: 拍,切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 干辣椒切四段。
方法: 切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 五花肉切片，约4cm×4cm。
方法: 切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 清洗鱼。
方法: 清洗
工具: 盆

### 第8步
步骤: 步骤8
描述: 鱼背肉厚处拉几道斜口，方便入味。
方法: 切
工具: 刀,案板

### 第9步
步骤: 步骤9
描述: 锅里多倒点油，烧至7成热（刚刚开始冒烟），下入鱼炸1分钟至鱼皮稍稍变硬捞出备用，炸鱼的油倒出，锅里留一点底油。
方法: 炸
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 将锅里底油烧热，下入五花肉，煸出香味。
方法: 煸
工具: 炒锅,锅铲

### 第11步
步骤: 步骤11
描述: 放入干辣椒、葱、姜、蒜瓣，翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第12步
步骤: 步骤12
描述: 将炸好的鱼倒入锅中。
方法: 倒
工具: 锅铲

### 第13步
步骤: 步骤13
描述: 沿锅边倒入料酒50ml、陈醋50ml、味极鲜50ml、老抽20ml、蚝油5ml、盐5g、白糖50g、清水没过鱼面。
方法: 倒
工具: 锅铲

### 第14步
步骤: 步骤14
描述: 调至中火，将水烧开。
方法: 烧
工具: 炒锅

### 第15步
步骤: 步骤15
描述: 调至小火，慢焖入味。
方法: 焖
工具: 炒锅,锅盖

### 第16步
步骤: 步骤16
描述: 15分钟后，打开锅盖，挑出锅里的葱、姜、蒜、干辣椒。
方法: 挑
工具: 筷子
时间: 15分钟

### 第17步
步骤: 步骤17
描述: 调至大火收汁，汤汁剩余1/4时，撒点蒜末，关火盛出。
方法: 收汁,撒,关火
工具: 锅铲

关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=24
source: merged_candidates
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.6757845282554626, search_type=vector_enhanced

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

### result_order=25
source: merged_candidates
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6725603342056274, search_type=vector_enhanced

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

### result_order=26
source: merged_candidates
metadata_summary: node_id=201000453, chunk_id=201000453_chunk_83, recipe_name=鲤鱼炖白菜, category=水产, score=0.6721473932266235, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲤鱼清洗干净，改刀（在鱼身上多划几个伤口，方便入味）
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 娃娃菜清洗干净放入盘中备用
方法: 清洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 锅中加油，等油热放入“少盐”“姜”“蒜”“郫县豆瓣酱”“桂皮”“八角”炒出香味
方法: 炒
工具: 锅,锅铲

### 第4步
步骤: 步骤4
描述: 把鱼放锅里煎（3分钟）每30秒需要翻面
方法: 煎
工具: 锅,锅铲
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 加入“水”（水量尽量和鱼平齐，可以少一点点）放入“生抽”“老抽”“娃娃菜”
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 大火炖15-20分钟，汤汁快干时添加“盐”即可出锅
方法: 炖
工具: 锅
时间: 15-20分钟

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
菜品: 红烧鱼头
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、香菜、美人椒分别清洗干净；干辣椒与八角稍微冲洗。
方法: 清洗
工具: 刀,案板,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 大葱切两半：葱白切段约4 cm，葱叶切段后劈四瓣；姜切3 mm片；蒜拍碎；两棵香菜切1.5 cm碎；美人椒切3 mm圈；干辣椒切四段。
方法: 切
工具: 刀,案板
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼头去鳞、清理内脏、剁去鱼鳍、清理鱼鳃，将鱼头下巴与鱼身连接处剁开，鱼身切块，鱼头剁成4-6瓣，再次清洗血水。
方法: 剁,清洗
工具: 菜刀,盆
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 将鱼块放入盆中，加5 g盐、10 g生抽、10 g料酒、切碎的葱叶段、1/3姜片拌匀，静置腌制1-2小时。
方法: 腌制
工具: 盆
时间: 1-2小时

### 第5步
步骤: 步骤5
描述: 锅中加30 ml油，小火加热，放入姜片炒至金黄出汁。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第6步
步骤: 步骤6
描述: 加入葱白段翻炒至略发白，再加入蒜碎、八角、干辣椒翻炒5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 倒入腌制好的鱼头翻炒2-3分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 加入500 ml清水，调入2 g盐、3 g鸡精、5 g生抽、3 g老抽、5 g料酒、2 g黑胡椒粉、3 g陈醋，放入两棵香菜，盖锅盖，大火烧开后转中火慢焖。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第9步
步骤: 步骤9
描述: 汤汁减半时开盖，大火收汁至剩余1/3，关火。将汤汁均匀淋在鱼头上，香菜垫底装饰，再放上剩余香菜和美人椒圈。
方法: 收汁,装盘
工具: 锅铲,小盆
时间: 5分钟

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingre
```

### pair_order=1
source: rerank_input

```text
命中关键词: 鱼头
食材名称: 鱼头
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 生姜
食材名称: 生姜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 大葱
食材名称: 大葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 大蒜
食材名称: 大蒜
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### pair_order=5
source: rerank_input

```text
命中关键词: 料酒
食材名称: 料酒
类别: 调料
关联图谱:
- IN REQUIRES 茭白炒肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 商芝肉 (Recipe): category: 荤菜；cuisineType: 西北菜；difficulty: 5.0
```

### pair_order=6
source: rerank_input

```text
命中关键词: 生抽
食材名称: 生抽
类别: 调料
关联图谱:
- IN REQUIRES 茶叶蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 香辣鸡爪煲 (Recipe): category: 荤菜；cuisineType: 川菜；difficulty: 4.0
```

### pair_order=7
source: rerank_input

```text
命中关键词: 老抽
食材名称: 老抽
类别: 调料
关联图谱:
- IN REQUIRES 酱牛肉 (Recipe): category: 荤菜；difficulty: 5.0
- IN REQUIRES 乡村啤酒鸭 (Recipe): category: 荤菜；difficulty: 4.0
```

### pair_order=8
source: rerank_input

```text
命中关键词: 白糖
食材名称: 白糖
类别: 调料
关联图谱:
- IN REQUIRES 凉粉 (Recipe): category: 主食；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 微波炉蛋糕 (Recipe): category: 早餐；difficulty: 1.0
```

### pair_order=9
source: rerank_input

```text
命中关键词: 食用油
食材名称: 食用油
类别: 调料
关联图谱:
- IN REQUIRES 鲤鱼炖白菜 (Recipe): category: 水产；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 青椒土豆炒肉 (Recipe): category: 荤菜；difficulty: 3.0
```

### pair_order=10
source: rerank_input

```text
命中关键词: 调味
菜品: 意式肉酱面
分类: 主食
菜系: 意大利
难度: 1.0
主要食材: 食用油, 肉沫, 意大利面
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=11
source: rerank_input

```text
命中关键词: 调味
菜品: 炒滑蛋
分类: 素菜
难度: 1.0
主要食材: 牛奶, 鸡蛋, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### pair_order=12
source: rerank_input

```text
命中关键词: 调味
菜品: 凉拌木耳
分类: 素菜
难度: 2.0
主要食材: 干木耳, 盐, 白糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=13
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

### pair_order=14
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

### pair_order=15
source: rerank_input

```text
命中关键词: 调味
菜品: 炸串酱料
分类: 调料
难度: 2.0
主要食材: 五香粉, 鸡精, 麻辣鲜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### pair_order=16
source: rerank_input

```text
命中关键词: 调味
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### pair_order=17
source: rerank_input

```text
命中关键词: 调味
菜品: 鸡蛋火腿炒黄瓜
分类: 素菜
难度: 2.0
主要食材: 生抽, 火腿肠, 鸡蛋
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=18
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

### pair_order=19
source: rerank_input

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

### pair_order=20
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

### pair_order=21
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

### pair_order=22
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

### pair_order=23
source: rerank_input

```text
菜品: 红烧鲤鱼
分类: 水产
菜系: 鲁菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、干辣椒分别清洗干净。
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 葱白处切段，每段长度约4cm，再将每段劈为四瓣。
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 姜切片，每片厚度约3mm。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 一个大蒜拍碎切末，其余蒜切为二瓣。
方法: 拍,切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 干辣椒切四段。
方法: 切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 五花肉切片，约4cm×4cm。
方法: 切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 清洗鱼。
方法: 清洗
工具: 盆

### 第8步
步骤: 步骤8
描述: 鱼背肉厚处拉几道斜口，方便入味。
方法: 切
工具: 刀,案板

### 第9步
步骤: 步骤9
描述: 锅里多倒点油，烧至7成热（刚刚开始冒烟），下入鱼炸1分钟至鱼皮稍稍变硬捞出备用，炸鱼的油倒出，锅里留一点底油。
方法: 炸
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 将锅里底油烧热，下入五花肉，煸出香味。
方法: 煸
工具: 炒锅,锅铲

### 第11步
步骤: 步骤11
描述: 放入干辣椒、葱、姜、蒜瓣，翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第12步
步骤: 步骤12
描述: 将炸好的鱼倒入锅中。
方法: 倒
工具: 锅铲

### 第13步
步骤: 步骤13
描述: 沿锅边倒入料酒50ml、陈醋50ml、味极鲜50ml、老抽20ml、蚝油5ml、盐5g、白糖50g、清水没过鱼面。
方法: 倒
工具: 锅铲

### 第14步
步骤: 步骤14
描述: 调至中火，将水烧开。
方法: 烧
工具: 炒锅

### 第15步
步骤: 步骤15
描述: 调至小火，慢焖入味。
方法: 焖
工具: 炒锅,锅
```

### pair_order=24
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

### pair_order=25
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

### pair_order=26
source: rerank_input

```text
菜品: 鲤鱼炖白菜
分类: 水产
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲤鱼清洗干净，改刀（在鱼身上多划几个伤口，方便入味）
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 娃娃菜清洗干净放入盘中备用
方法: 清洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 锅中加油，等油热放入“少盐”“姜”“蒜”“郫县豆瓣酱”“桂皮”“八角”炒出香味
方法: 炒
工具: 锅,锅铲

### 第4步
步骤: 步骤4
描述: 把鱼放锅里煎（3分钟）每30秒需要翻面
方法: 煎
工具: 锅,锅铲
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 加入“水”（水量尽量和鱼平齐，可以少一点点）放入“生抽”“老抽”“娃娃菜”
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 大火炖15-20分钟，汤汁快干时添加“盐”即可出锅
方法: 炖
工具: 锅
时间: 15-20分钟

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201000100, chunk_id=201000100_chunk_22, recipe_name=红烧鱼头, category=水产, score=0.7139914631843567, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、香菜、美人椒分别清洗干净；干辣椒与八角稍微冲洗。
方法: 清洗
工具: 刀,案板,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 大葱切两半：葱白切段约4 cm，葱叶切段后劈四瓣；姜切3 mm片；蒜拍碎；两棵香菜切1.5 cm碎；美人椒切3 mm圈；干辣椒切四段。
方法: 切
工具: 刀,案板
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼头去鳞、清理内脏、剁去鱼鳍、清理鱼鳃，将鱼头下巴与鱼身连接处剁开，鱼身切块，鱼头剁成4-6瓣，再次清洗血水。
方法: 剁,清洗
工具: 菜刀,盆
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 将鱼块放入盆中，加5 g盐、10 g生抽、10 g料酒、切碎的葱叶段、1/3姜片拌匀，静置腌制1-2小时。
方法: 腌制
工具: 盆
时间: 1-2小时

### 第5步
步骤: 步骤5
描述: 锅中加30 ml油，小火加热，放入姜片炒至金黄出汁。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第6步
步骤: 步骤6
描述: 加入葱白段翻炒至略发白，再加入蒜碎、八角、干辣椒翻炒5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 倒入腌制好的鱼头翻炒2-3分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 加入500 ml清水，调入2 g盐、3 g鸡精、5 g生抽、3 g老抽、5 g料酒、2 g黑胡椒粉、3 g陈醋，放入两棵香菜，盖锅盖，大火烧开后转中火慢焖。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第9步
步骤: 步骤9
描述: 汤汁减半时开盖，大火收汁至剩余1/3，关火。将汤汁均匀淋在鱼头上，香菜垫底装饰，再放上剩余香菜和美人椒圈。
方法: 收汁,装盘
工具: 锅铲,小盆
时间: 5分钟

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6826379299163818, search_type=vector_enhanced

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

### result_order=2
source: reranked_results
metadata_summary: node_id=201000127, chunk_id=201000127_chunk_26, recipe_name=红烧鲤鱼, category=水产, score=0.6840590834617615, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、干辣椒分别清洗干净。
方法: 清洗
工具: 盆

### 第2步
步骤: 步骤2
描述: 葱白处切段，每段长度约4cm，再将每段劈为四瓣。
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 姜切片，每片厚度约3mm。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 一个大蒜拍碎切末，其余蒜切为二瓣。
方法: 拍,切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 干辣椒切四段。
方法: 切
工具: 刀,案板

### 第6步
步骤: 步骤6
描述: 五花肉切片，约4cm×4cm。
方法: 切
工具: 刀,案板

### 第7步
步骤: 步骤7
描述: 清洗鱼。
方法: 清洗
工具: 盆

### 第8步
步骤: 步骤8
描述: 鱼背肉厚处拉几道斜口，方便入味。
方法: 切
工具: 刀,案板

### 第9步
步骤: 步骤9
描述: 锅里多倒点油，烧至7成热（刚刚开始冒烟），下入鱼炸1分钟至鱼皮稍稍变硬捞出备用，炸鱼的油倒出，锅里留一点底油。
方法: 炸
工具: 炒锅,锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 将锅里底油烧热，下入五花肉，煸出香味。
方法: 煸
工具: 炒锅,锅铲

### 第11步
步骤: 步骤11
描述: 放入干辣椒、葱、姜、蒜瓣，翻炒1分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第12步
步骤: 步骤12
描述: 将炸好的鱼倒入锅中。
方法: 倒
工具: 锅铲

### 第13步
步骤: 步骤13
描述: 沿锅边倒入料酒50ml、陈醋50ml、味极鲜50ml、老抽20ml、蚝油5ml、盐5g、白糖50g、清水没过鱼面。
方法: 倒
工具: 锅铲

### 第14步
步骤: 步骤14
描述: 调至中火，将水烧开。
方法: 烧
工具: 炒锅

### 第15步
步骤: 步骤15
描述: 调至小火，慢焖入味。
方法: 焖
工具: 炒锅,锅盖

### 第16步
步骤: 步骤16
描述: 15分钟后，打开锅盖，挑出锅里的葱、姜、蒜、干辣椒。
方法: 挑
工具: 筷子
时间: 15分钟

### 第17步
步骤: 步骤17
描述: 调至大火收汁，汤汁剩余1/4时，撒点蒜末，关火盛出。
方法: 收汁,撒,关火
工具: 锅铲

关联图谱:
- OUT REQUIRES 蒜瓣 (Ingredient): category: 蔬菜
- OUT REQUIRES 清水 (Ingredient): category: 其他
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.72178053855896, search_type=vector_enhanced

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

### result_order=4
source: reranked_results
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6915249228477478, search_type=vector_enhanced

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
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.6757845282554626, search_type=vector_enhanced

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

### result_order=6
source: reranked_results
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

### result_order=7
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

### result_order=8
source: reranked_results
metadata_summary: node_id=201000453, chunk_id=201000453_chunk_83, recipe_name=鲤鱼炖白菜, category=水产, score=0.6721473932266235, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲤鱼清洗干净，改刀（在鱼身上多划几个伤口，方便入味）
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 娃娃菜清洗干净放入盘中备用
方法: 清洗
工具: 盆

### 第3步
步骤: 步骤3
描述: 锅中加油，等油热放入“少盐”“姜”“蒜”“郫县豆瓣酱”“桂皮”“八角”炒出香味
方法: 炒
工具: 锅,锅铲

### 第4步
步骤: 步骤4
描述: 把鱼放锅里煎（3分钟）每30秒需要翻面
方法: 煎
工具: 锅,锅铲
时间: 3分钟

### 第5步
步骤: 步骤5
描述: 加入“水”（水量尽量和鱼平齐，可以少一点点）放入“生抽”“老抽”“娃娃菜”
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 大火炖15-20分钟，汤汁快干时添加“盐”即可出锅
方法: 炖
工具: 锅
时间: 15-20分钟

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
- OUT REQUIRES 盐 (Ingredient): category: 调料
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201004466, recipe_name=意式肉酱面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 意式肉酱面
分类: 主食
菜系: 意大利
难度: 1.0
主要食材: 食用油, 肉沫, 意大利面
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201000775, recipe_name=炸串酱料, category=调料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炸串酱料
分类: 调料
难度: 2.0
主要食材: 五香粉, 鸡精, 麻辣鲜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201000101, recipe_name=鱼头, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鱼头
食材名称: 鱼头
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=12
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

### result_order=13
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

### result_order=14
source: reranked_results
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6725603342056274, search_type=vector_enhanced

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

### result_order=15
source: reranked_results
metadata_summary: node_id=201000628, recipe_name=燕麦鸡蛋饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=16
source: reranked_results
metadata_summary: node_id=201005272, recipe_name=鸡蛋火腿炒黄瓜, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 鸡蛋火腿炒黄瓜
分类: 素菜
难度: 2.0
主要食材: 生抽, 火腿肠, 鸡蛋
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=17
source: reranked_results
metadata_summary: node_id=201005312, recipe_name=凉拌木耳, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 凉拌木耳
分类: 素菜
难度: 2.0
主要食材: 干木耳, 盐, 白糖
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=18
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

### result_order=19
source: reranked_results
metadata_summary: node_id=201005481, recipe_name=炒滑蛋, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炒滑蛋
分类: 素菜
难度: 1.0
主要食材: 牛奶, 鸡蛋, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 一星 (DifficultyLevel)
```

### result_order=20
source: reranked_results
metadata_summary: node_id=201000028, recipe_name=料酒, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 料酒
食材名称: 料酒
类别: 调料
关联图谱:
- IN REQUIRES 茭白炒肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 商芝肉 (Recipe): category: 荤菜；cuisineType: 西北菜；difficulty: 5.0
```

### result_order=21
source: reranked_results
metadata_summary: node_id=201000134, recipe_name=白糖, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 白糖
食材名称: 白糖
类别: 调料
关联图谱:
- IN REQUIRES 凉粉 (Recipe): category: 主食；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 微波炉蛋糕 (Recipe): category: 早餐；difficulty: 1.0
```

### result_order=22
source: reranked_results
metadata_summary: node_id=201000112, recipe_name=生抽, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 生抽
食材名称: 生抽
类别: 调料
关联图谱:
- IN REQUIRES 茶叶蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 香辣鸡爪煲 (Recipe): category: 荤菜；cuisineType: 川菜；difficulty: 4.0
```

### result_order=23
source: reranked_results
metadata_summary: node_id=201000102, recipe_name=大葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 大葱
食材名称: 大葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=24
source: reranked_results
metadata_summary: node_id=201000193, recipe_name=生姜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 生姜
食材名称: 生姜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=25
source: reranked_results
metadata_summary: node_id=201000113, recipe_name=老抽, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 老抽
食材名称: 老抽
类别: 调料
关联图谱:
- IN REQUIRES 酱牛肉 (Recipe): category: 荤菜；difficulty: 5.0
- IN REQUIRES 乡村啤酒鸭 (Recipe): category: 荤菜；difficulty: 4.0
```

### result_order=26
source: reranked_results
metadata_summary: node_id=201000008, recipe_name=大蒜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 大蒜
食材名称: 大蒜
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201000100, chunk_id=201000100_chunk_22, recipe_name=红烧鱼头, category=水产, score=0.7139914631843567, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、香菜、美人椒分别清洗干净；干辣椒与八角稍微冲洗。
方法: 清洗
工具: 刀,案板,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 大葱切两半：葱白切段约4 cm，葱叶切段后劈四瓣；姜切3 mm片；蒜拍碎；两棵香菜切1.5 cm碎；美人椒切3 mm圈；干辣椒切四段。
方法: 切
工具: 刀,案板
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼头去鳞、清理内脏、剁去鱼鳍、清理鱼鳃，将鱼头下巴与鱼身连接处剁开，鱼身切块，鱼头剁成4-6瓣，再次清洗血水。
方法: 剁,清洗
工具: 菜刀,盆
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 将鱼块放入盆中，加5 g盐、10 g生抽、10 g料酒、切碎的葱叶段、1/3姜片拌匀，静置腌制1-2小时。
方法: 腌制
工具: 盆
时间: 1-2小时

### 第5步
步骤: 步骤5
描述: 锅中加30 ml油，小火加热，放入姜片炒至金黄出汁。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第6步
步骤: 步骤6
描述: 加入葱白段翻炒至略发白，再加入蒜碎、八角、干辣椒翻炒5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 倒入腌制好的鱼头翻炒2-3分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 加入500 ml清水，调入2 g盐、3 g鸡精、5 g生抽、3 g老抽、5 g料酒、2 g黑胡椒粉、3 g陈醋，放入两棵香菜，盖锅盖，大火烧开后转中火慢焖。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第9步
步骤: 步骤9
描述: 汤汁减半时开盖，大火收汁至剩余1/3，关火。将汤汁均匀淋在鱼头上，香菜垫底装饰，再放上剩余香菜和美人椒圈。
方法: 收汁,装盘
工具: 锅铲,小盆
时间: 5分钟

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6826379299163818, search_type=vector_enhanced

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

### result_order=2
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

### result_order=3
source: top_k_final
metadata_summary: node_id=201004466, recipe_name=意式肉酱面, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 意式肉酱面
分类: 主食
菜系: 意大利
难度: 1.0
主要食材: 食用油, 肉沫, 意大利面
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201000775, recipe_name=炸串酱料, category=调料, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 调味
菜品: 炸串酱料
分类: 调料
难度: 2.0
主要食材: 五香粉, 鸡精, 麻辣鲜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201000100, chunk_id=201000100_chunk_22, recipe_name=红烧鱼头, category=水产, score=0.7139914631843567, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱、姜、蒜、香菜、美人椒分别清洗干净；干辣椒与八角稍微冲洗。
方法: 清洗
工具: 刀,案板,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 大葱切两半：葱白切段约4 cm，葱叶切段后劈四瓣；姜切3 mm片；蒜拍碎；两棵香菜切1.5 cm碎；美人椒切3 mm圈；干辣椒切四段。
方法: 切
工具: 刀,案板
时间: 10分钟

### 第3步
步骤: 步骤3
描述: 鱼头去鳞、清理内脏、剁去鱼鳍、清理鱼鳃，将鱼头下巴与鱼身连接处剁开，鱼身切块，鱼头剁成4-6瓣，再次清洗血水。
方法: 剁,清洗
工具: 菜刀,盆
时间: 10分钟

### 第4步
步骤: 步骤4
描述: 将鱼块放入盆中，加5 g盐、10 g生抽、10 g料酒、切碎的葱叶段、1/3姜片拌匀，静置腌制1-2小时。
方法: 腌制
工具: 盆
时间: 1-2小时

### 第5步
步骤: 步骤5
描述: 锅中加30 ml油，小火加热，放入姜片炒至金黄出汁。
方法: 炒
工具: 炒锅,锅铲
时间: 1-2分钟

### 第6步
步骤: 步骤6
描述: 加入葱白段翻炒至略发白，再加入蒜碎、八角、干辣椒翻炒5秒。
方法: 炒
工具: 炒锅,锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 倒入腌制好的鱼头翻炒2-3分钟。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第8步
步骤: 步骤8
描述: 加入500 ml清水，调入2 g盐、3 g鸡精、5 g生抽、3 g老抽、5 g料酒、2 g黑胡椒粉、3 g陈醋，放入两棵香菜，盖锅盖，大火烧开后转中火慢焖。
方法: 煮,焖
工具: 炒锅,锅盖
时间: 15分钟

### 第9步
步骤: 步骤9
描述: 汤汁减半时开盖，大火收汁至剩余1/3，关火。将汤汁均匀淋在鱼头上，香菜垫底装饰，再放上剩余香菜和美人椒圈。
方法: 收汁,装盘
工具: 锅铲,小盆
时间: 5分钟

关联图谱:
- OUT REQUIRES 黑胡椒粉 (Ingredient): category: 调料
- OUT REQUIRES 鱼头 (Ingredient): category: 蛋白质
- OUT REQUIRES 油 (Ingredient): category: 调料
```

### result_order=1
source: generation_context
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6826379299163818, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=2
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

### result_order=3
source: generation_context
metadata_summary: node_id=201004466, recipe_name=意式肉酱面, category=主食, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 调味
菜品: 意式肉酱面
分类: 主食
菜系: 意大利
难度: 1.0
主要食材: 食用油, 肉沫, 意大利面
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=4
source: generation_context
metadata_summary: node_id=201000775, recipe_name=炸串酱料, category=调料, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 调味
菜品: 炸串酱料
分类: 调料
难度: 2.0
主要食材: 五香粉, 鸡精, 麻辣鲜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
- OUT DIFFICULTY_LEVEL 二星 (DifficultyLevel)
```

