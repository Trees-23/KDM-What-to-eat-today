# Recall Content

audit_id: 20260811_173324_335_deb0499d
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
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

### result_order=1
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

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=201000628, recipe_name=燕麦鸡蛋饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 煎制
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

### result_order=1
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

### result_order=2
source: topic_level
metadata_summary: node_id=201005492, recipe_name=烤茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=3
source: topic_level
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
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
metadata_summary: node_id=201004341, recipe_name=韭菜盒子, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 煎制
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
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

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6305848956108093, search_type=vector_enhanced

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
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_44, recipe_name=清蒸鲈鱼, category=水产, score=0.6212850213050842, search_type=vector_enhanced

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
metadata_summary: node_id=201000337, chunk_id=201000337_chunk_63, recipe_name=葱油桂鱼, category=水产, score=0.6019703149795532, search_type=vector_enhanced

```text
## 标签
成功率高,容错性强,兼容各地口味,可替换鱼类：鲈鱼、多宝鱼等海鱼,不建议使用淡水鱼
关联图谱:
- OUT REQUIRES 植物油 (Ingredient): category: 调料
- OUT REQUIRES 小米辣 (Ingredient): category: 蔬菜
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.5975586175918579, search_type=vector_enhanced

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

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.5821714401245117, search_type=vector_enhanced

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

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201000337, chunk_id=201000337_chunk_62, recipe_name=葱油桂鱼, category=水产, score=0.5812851786613464, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 去菜市场买已经处理好的鱼（自己处理的话最好不要内脏），将鱼身表面的所有鳞片刮干净
方法: 处理
工具: 菜刀

### 第2步
步骤: 步骤2
描述: 用厨房用纸将鱼肚子里的贴骨血和黑膜擦干净（帖骨血会影响口感，黑膜是鱼腥味的来源）
方法: 清理
工具: 厨房纸

### 第3步
步骤: 步骤3
描述: 用菜刀在鱼身表面来回刮几次，将鱼身的黏液刮掉，进一步去除腥味，然后用清水将鱼内外冲洗干净
方法: 清理,冲洗
工具: 菜刀

### 第4步
步骤: 步骤4
描述: 将鱼平放在砧板，使用厨房纸将鱼内外的水分擦干，然后鱼头朝左，尾朝右，从鱼鳃边开始，每隔3cm纵向划一刀，深度达到鱼的脊椎骨即可，另一面使用同样的处理方式
方法: 切
工具: 砧板,厨房纸,菜刀

### 第5步
步骤: 步骤5
描述: 将鱼平放在盆中，确保盘中没有多余水分
方法: 摆放
工具: 塑料盆

### 第6步
步骤: 步骤6
描述: 取一块50g姜，用削皮刀把表面的皮去除并洗干净，然后切成厚度为3mm的姜片
方法: 去皮,切
工具: 削皮刀,菜刀

### 第7步
步骤: 步骤7
描述: 将小米辣洗干净、去蒂，切成厚度为2mm的小圆片（或切成1mm宽度的丝状）
方法: 切
工具: 菜刀

### 第8步
步骤: 步骤8
描述: 将小葱洗干净，去除根须，切成3cm的小段，稍微粗一点的小葱，可以沿中间劈开
方法: 切
工具: 菜刀

### 第9步
步骤: 步骤9
描述: 加入8g盐、25g料酒到盆中，带上一次性手套，对鱼进行全身按摩1分钟，确保鱼身每个部位都均匀涂抹了盐和料酒
方法: 腌制,按摩
工具: 塑料盆,一次性手套
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 在鱼身的每一个刀口中塞入一片姜片，鱼肚子中放入3片姜片，腌制10分钟
方法: 腌制
工具: 塑料盆
时间: 10分钟

### 第11步
步骤: 步骤11
描述: 在鱼腌制期间，在蒸锅中加入5L清水，烧开后，在蒸锅上放上蒸笼
方法: 烧水
工具: 蒸锅,蒸笼

### 第12步
步骤: 步骤12
描述: 鱼腌制好后，会析出水分，将多余水分和腌制用料酒、姜片倒掉，用清水冲洗干净鱼身和鱼肚，用厨房纸擦干
方法: 冲洗,擦干
工具: 厨房纸

### 第13步
步骤: 步骤13
描述: 将鱼平放在蒸鱼盘中，重新在鱼身、鱼肚刀口处塞入姜片
方法: 摆放
工具: 蒸鱼盘

### 第14步
步骤: 步骤14
描述: 将蒸鱼盘放入蒸笼中，盖上盖子，中火蒸20分钟
方法: 蒸
工具: 蒸笼,防烫夹
时间: 20分钟

### 第15步
步骤: 步骤15
描述: 用防烫夹将蒸鱼盘夹出，在鱼身和鱼周围淋上10g蒸鱼豉油
方法: 淋汁
工具: 防烫夹

### 第16步
步骤: 步骤16
描述: 在鱼身和周围均匀撒上小葱段和小米辣
方法: 撒料

### 第17步
步骤: 步骤17
描述: 在铁锅中倒入15g植物油，用中小火慢熬5分钟，不要用大火，否则油会挥发很快
方法: 熬油
工具: 铁锅
时间: 5分钟

### 第18步
步骤: 步骤18
描述: 将出锅后的热油均匀地慢慢地淋在鱼身上，鲜掉眉毛的葱油桂鱼就出炉啦！
方法: 淋油
工具: 铁锅

关联图谱:
- OUT REQUIRES 植物油 (Ingredient): category: 调料
- OUT REQUIRES 小米辣 (Ingredient): category: 蔬菜
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.5703058242797852, search_type=vector_enhanced

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

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201000453, chunk_id=201000453_chunk_83, recipe_name=鲤鱼炖白菜, category=水产, score=0.5673090815544128, search_type=vector_enhanced

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

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201000127, chunk_id=201000127_chunk_26, recipe_name=红烧鲤鱼, category=水产, score=0.5670437216758728, search_type=vector_enhanced

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

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201000040, chunk_id=201000040_chunk_11, recipe_name=水煮鱼, category=水产, score=0.5662153959274292, search_type=vector_enhanced

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

## Hybrid Retrieval / Branches Before Merge
### result_order=0
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

### result_order=1
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

### result_order=2
source: branch_grouped
metadata_summary: node_id=201000628, recipe_name=燕麦鸡蛋饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 煎制
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
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
metadata_summary: node_id=201005492, recipe_name=烤茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
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

### result_order=7
source: branch_grouped
metadata_summary: node_id=201004341, recipe_name=韭菜盒子, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 煎制
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
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

### result_order=9
source: branch_grouped
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6305848956108093, search_type=vector_enhanced

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

### result_order=10
source: branch_grouped
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_44, recipe_name=清蒸鲈鱼, category=水产, score=0.6212850213050842, search_type=vector_enhanced

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

### result_order=11
source: branch_grouped
metadata_summary: node_id=201000337, chunk_id=201000337_chunk_63, recipe_name=葱油桂鱼, category=水产, score=0.6019703149795532, search_type=vector_enhanced

```text
## 标签
成功率高,容错性强,兼容各地口味,可替换鱼类：鲈鱼、多宝鱼等海鱼,不建议使用淡水鱼
关联图谱:
- OUT REQUIRES 植物油 (Ingredient): category: 调料
- OUT REQUIRES 小米辣 (Ingredient): category: 蔬菜
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.5975586175918579, search_type=vector_enhanced

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

### result_order=13
source: branch_grouped
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.5821714401245117, search_type=vector_enhanced

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

### result_order=14
source: branch_grouped
metadata_summary: node_id=201000337, chunk_id=201000337_chunk_62, recipe_name=葱油桂鱼, category=水产, score=0.5812851786613464, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 去菜市场买已经处理好的鱼（自己处理的话最好不要内脏），将鱼身表面的所有鳞片刮干净
方法: 处理
工具: 菜刀

### 第2步
步骤: 步骤2
描述: 用厨房用纸将鱼肚子里的贴骨血和黑膜擦干净（帖骨血会影响口感，黑膜是鱼腥味的来源）
方法: 清理
工具: 厨房纸

### 第3步
步骤: 步骤3
描述: 用菜刀在鱼身表面来回刮几次，将鱼身的黏液刮掉，进一步去除腥味，然后用清水将鱼内外冲洗干净
方法: 清理,冲洗
工具: 菜刀

### 第4步
步骤: 步骤4
描述: 将鱼平放在砧板，使用厨房纸将鱼内外的水分擦干，然后鱼头朝左，尾朝右，从鱼鳃边开始，每隔3cm纵向划一刀，深度达到鱼的脊椎骨即可，另一面使用同样的处理方式
方法: 切
工具: 砧板,厨房纸,菜刀

### 第5步
步骤: 步骤5
描述: 将鱼平放在盆中，确保盘中没有多余水分
方法: 摆放
工具: 塑料盆

### 第6步
步骤: 步骤6
描述: 取一块50g姜，用削皮刀把表面的皮去除并洗干净，然后切成厚度为3mm的姜片
方法: 去皮,切
工具: 削皮刀,菜刀

### 第7步
步骤: 步骤7
描述: 将小米辣洗干净、去蒂，切成厚度为2mm的小圆片（或切成1mm宽度的丝状）
方法: 切
工具: 菜刀

### 第8步
步骤: 步骤8
描述: 将小葱洗干净，去除根须，切成3cm的小段，稍微粗一点的小葱，可以沿中间劈开
方法: 切
工具: 菜刀

### 第9步
步骤: 步骤9
描述: 加入8g盐、25g料酒到盆中，带上一次性手套，对鱼进行全身按摩1分钟，确保鱼身每个部位都均匀涂抹了盐和料酒
方法: 腌制,按摩
工具: 塑料盆,一次性手套
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 在鱼身的每一个刀口中塞入一片姜片，鱼肚子中放入3片姜片，腌制10分钟
方法: 腌制
工具: 塑料盆
时间: 10分钟

### 第11步
步骤: 步骤11
描述: 在鱼腌制期间，在蒸锅中加入5L清水，烧开后，在蒸锅上放上蒸笼
方法: 烧水
工具: 蒸锅,蒸笼

### 第12步
步骤: 步骤12
描述: 鱼腌制好后，会析出水分，将多余水分和腌制用料酒、姜片倒掉，用清水冲洗干净鱼身和鱼肚，用厨房纸擦干
方法: 冲洗,擦干
工具: 厨房纸

### 第13步
步骤: 步骤13
描述: 将鱼平放在蒸鱼盘中，重新在鱼身、鱼肚刀口处塞入姜片
方法: 摆放
工具: 蒸鱼盘

### 第14步
步骤: 步骤14
描述: 将蒸鱼盘放入蒸笼中，盖上盖子，中火蒸20分钟
方法: 蒸
工具: 蒸笼,防烫夹
时间: 20分钟

### 第15步
步骤: 步骤15
描述: 用防烫夹将蒸鱼盘夹出，在鱼身和鱼周围淋上10g蒸鱼豉油
方法: 淋汁
工具: 防烫夹

### 第16步
步骤: 步骤16
描述: 在鱼身和周围均匀撒上小葱段和小米辣
方法: 撒料

### 第17步
步骤: 步骤17
描述: 在铁锅中倒入15g植物油，用中小火慢熬5分钟，不要用大火，否则油会挥发很快
方法: 熬油
工具: 铁锅
时间: 5分钟

### 第18步
步骤: 步骤18
描述: 将出锅后的热油均匀地慢慢地淋在鱼身上，鲜掉眉毛的葱油桂鱼就出炉啦！
方法: 淋油
工具: 铁锅

关联图谱:
- OUT REQUIRES 植物油 (Ingredient): category: 调料
- OUT REQUIRES 小米辣 (Ingredient): category: 蔬菜
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=15
source: branch_grouped
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.5703058242797852, search_type=vector_enhanced

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

### result_order=16
source: branch_grouped
metadata_summary: node_id=201000453, chunk_id=201000453_chunk_83, recipe_name=鲤鱼炖白菜, category=水产, score=0.5673090815544128, search_type=vector_enhanced

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

### result_order=17
source: branch_grouped
metadata_summary: node_id=201000127, chunk_id=201000127_chunk_26, recipe_name=红烧鲤鱼, category=水产, score=0.5670437216758728, search_type=vector_enhanced

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

### result_order=18
source: branch_grouped
metadata_summary: node_id=201000040, chunk_id=201000040_chunk_11, recipe_name=水煮鱼, category=水产, score=0.5662153959274292, search_type=vector_enhanced

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

## Hybrid Retrieval / Merged Candidates
### result_order=0
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

### result_order=1
source: merged_candidates
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6305848956108093, search_type=vector_enhanced

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

### result_order=2
source: merged_candidates
metadata_summary: node_id=201000628, recipe_name=燕麦鸡蛋饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 煎制
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
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
metadata_summary: node_id=201005492, recipe_name=烤茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
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

### result_order=7
source: merged_candidates
metadata_summary: node_id=201004341, recipe_name=韭菜盒子, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 煎制
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
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

### result_order=9
source: merged_candidates
metadata_summary: node_id=201000337, chunk_id=201000337_chunk_62, recipe_name=葱油桂鱼, category=水产, score=0.5812851786613464, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 去菜市场买已经处理好的鱼（自己处理的话最好不要内脏），将鱼身表面的所有鳞片刮干净
方法: 处理
工具: 菜刀

### 第2步
步骤: 步骤2
描述: 用厨房用纸将鱼肚子里的贴骨血和黑膜擦干净（帖骨血会影响口感，黑膜是鱼腥味的来源）
方法: 清理
工具: 厨房纸

### 第3步
步骤: 步骤3
描述: 用菜刀在鱼身表面来回刮几次，将鱼身的黏液刮掉，进一步去除腥味，然后用清水将鱼内外冲洗干净
方法: 清理,冲洗
工具: 菜刀

### 第4步
步骤: 步骤4
描述: 将鱼平放在砧板，使用厨房纸将鱼内外的水分擦干，然后鱼头朝左，尾朝右，从鱼鳃边开始，每隔3cm纵向划一刀，深度达到鱼的脊椎骨即可，另一面使用同样的处理方式
方法: 切
工具: 砧板,厨房纸,菜刀

### 第5步
步骤: 步骤5
描述: 将鱼平放在盆中，确保盘中没有多余水分
方法: 摆放
工具: 塑料盆

### 第6步
步骤: 步骤6
描述: 取一块50g姜，用削皮刀把表面的皮去除并洗干净，然后切成厚度为3mm的姜片
方法: 去皮,切
工具: 削皮刀,菜刀

### 第7步
步骤: 步骤7
描述: 将小米辣洗干净、去蒂，切成厚度为2mm的小圆片（或切成1mm宽度的丝状）
方法: 切
工具: 菜刀

### 第8步
步骤: 步骤8
描述: 将小葱洗干净，去除根须，切成3cm的小段，稍微粗一点的小葱，可以沿中间劈开
方法: 切
工具: 菜刀

### 第9步
步骤: 步骤9
描述: 加入8g盐、25g料酒到盆中，带上一次性手套，对鱼进行全身按摩1分钟，确保鱼身每个部位都均匀涂抹了盐和料酒
方法: 腌制,按摩
工具: 塑料盆,一次性手套
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 在鱼身的每一个刀口中塞入一片姜片，鱼肚子中放入3片姜片，腌制10分钟
方法: 腌制
工具: 塑料盆
时间: 10分钟

### 第11步
步骤: 步骤11
描述: 在鱼腌制期间，在蒸锅中加入5L清水，烧开后，在蒸锅上放上蒸笼
方法: 烧水
工具: 蒸锅,蒸笼

### 第12步
步骤: 步骤12
描述: 鱼腌制好后，会析出水分，将多余水分和腌制用料酒、姜片倒掉，用清水冲洗干净鱼身和鱼肚，用厨房纸擦干
方法: 冲洗,擦干
工具: 厨房纸

### 第13步
步骤: 步骤13
描述: 将鱼平放在蒸鱼盘中，重新在鱼身、鱼肚刀口处塞入姜片
方法: 摆放
工具: 蒸鱼盘

### 第14步
步骤: 步骤14
描述: 将蒸鱼盘放入蒸笼中，盖上盖子，中火蒸20分钟
方法: 蒸
工具: 蒸笼,防烫夹
时间: 20分钟

### 第15步
步骤: 步骤15
描述: 用防烫夹将蒸鱼盘夹出，在鱼身和鱼周围淋上10g蒸鱼豉油
方法: 淋汁
工具: 防烫夹

### 第16步
步骤: 步骤16
描述: 在鱼身和周围均匀撒上小葱段和小米辣
方法: 撒料

### 第17步
步骤: 步骤17
描述: 在铁锅中倒入15g植物油，用中小火慢熬5分钟，不要用大火，否则油会挥发很快
方法: 熬油
工具: 铁锅
时间: 5分钟

### 第18步
步骤: 步骤18
描述: 将出锅后的热油均匀地慢慢地淋在鱼身上，鲜掉眉毛的葱油桂鱼就出炉啦！
方法: 淋油
工具: 铁锅

关联图谱:
- OUT REQUIRES 植物油 (Ingredient): category: 调料
- OUT REQUIRES 小米辣 (Ingredient): category: 蔬菜
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.5975586175918579, search_type=vector_enhanced

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

### result_order=11
source: merged_candidates
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.5821714401245117, search_type=vector_enhanced

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

### result_order=12
source: merged_candidates
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.5703058242797852, search_type=vector_enhanced

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

### result_order=13
source: merged_candidates
metadata_summary: node_id=201000453, chunk_id=201000453_chunk_83, recipe_name=鲤鱼炖白菜, category=水产, score=0.5673090815544128, search_type=vector_enhanced

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

### result_order=14
source: merged_candidates
metadata_summary: node_id=201000127, chunk_id=201000127_chunk_26, recipe_name=红烧鲤鱼, category=水产, score=0.5670437216758728, search_type=vector_enhanced

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

### result_order=15
source: merged_candidates
metadata_summary: node_id=201000040, chunk_id=201000040_chunk_11, recipe_name=水煮鱼, category=水产, score=0.5662153959274292, search_type=vector_enhanced

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

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 鲈鱼
食材名称: 鲈鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=1
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

### pair_order=2
source: rerank_input

```text
命中关键词: 煎制
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
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
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=5
source: rerank_input

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=6
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

### pair_order=7
source: rerank_input

```text
命中关键词: 煎制
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=8
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

### pair_order=9
source: rerank_input

```text
分类: 水产
菜系: 粤菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 去菜市场买已经处理好的鱼（自己处理的话最好不要内脏），将鱼身表面的所有鳞片刮干净
方法: 处理
工具: 菜刀

### 第2步
步骤: 步骤2
描述: 用厨房用纸将鱼肚子里的贴骨血和黑膜擦干净（帖骨血会影响口感，黑膜是鱼腥味的来源）
方法: 清理
工具: 厨房纸

### 第3步
步骤: 步骤3
描述: 用菜刀在鱼身表面来回刮几次，将鱼身的黏液刮掉，进一步去除腥味，然后用清水将鱼内外冲洗干净
方法: 清理,冲洗
工具: 菜刀

### 第4步
步骤: 步骤4
描述: 将鱼平放在砧板，使用厨房纸将鱼内外的水分擦干，然后鱼头朝左，尾朝右，从鱼鳃边开始，每隔3cm纵向划一刀，深度达到鱼的脊椎骨即可，另一面使用同样的处理方式
方法: 切
工具: 砧板,厨房纸,菜刀

### 第5步
步骤: 步骤5
描述: 将鱼平放在盆中，确保盘中没有多余水分
方法: 摆放
工具: 塑料盆

### 第6步
步骤: 步骤6
描述: 取一块50g姜，用削皮刀把表面的皮去除并洗干净，然后切成厚度为3mm的姜片
方法: 去皮,切
工具: 削皮刀,菜刀

### 第7步
步骤: 步骤7
描述: 将小米辣洗干净、去蒂，切成厚度为2mm的小圆片（或切成1mm宽度的丝状）
方法: 切
工具: 菜刀

### 第8步
步骤: 步骤8
描述: 将小葱洗干净，去除根须，切成3cm的小段，稍微粗一点的小葱，可以沿中间劈开
方法: 切
工具: 菜刀

### 第9步
步骤: 步骤9
描述: 加入8g盐、25g料酒到盆中，带上一次性手套，对鱼进行全身按摩1分钟，确保鱼身每个部位都均匀涂抹了盐和料酒
方法: 腌制,按摩
工具: 塑料盆,一次性手套
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 在鱼身的每一个刀口中塞入一片姜片，鱼肚子中放入3片姜片，腌制10分钟
方法: 腌制
工具: 塑料盆
时间: 10分钟

### 第11步
步骤: 步骤11
描述: 在鱼腌制期间，在蒸锅中加入5L清水，烧开后，在蒸锅上放上蒸笼
方法: 
```

### pair_order=10
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

### pair_order=11
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

### pair_order=12
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

### pair_order=13
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

### pair_order=14
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

### pair_order=15
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

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6305848956108093, search_type=vector_enhanced

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
metadata_summary: node_id=201000337, chunk_id=201000337_chunk_62, recipe_name=葱油桂鱼, category=水产, score=0.5812851786613464, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 去菜市场买已经处理好的鱼（自己处理的话最好不要内脏），将鱼身表面的所有鳞片刮干净
方法: 处理
工具: 菜刀

### 第2步
步骤: 步骤2
描述: 用厨房用纸将鱼肚子里的贴骨血和黑膜擦干净（帖骨血会影响口感，黑膜是鱼腥味的来源）
方法: 清理
工具: 厨房纸

### 第3步
步骤: 步骤3
描述: 用菜刀在鱼身表面来回刮几次，将鱼身的黏液刮掉，进一步去除腥味，然后用清水将鱼内外冲洗干净
方法: 清理,冲洗
工具: 菜刀

### 第4步
步骤: 步骤4
描述: 将鱼平放在砧板，使用厨房纸将鱼内外的水分擦干，然后鱼头朝左，尾朝右，从鱼鳃边开始，每隔3cm纵向划一刀，深度达到鱼的脊椎骨即可，另一面使用同样的处理方式
方法: 切
工具: 砧板,厨房纸,菜刀

### 第5步
步骤: 步骤5
描述: 将鱼平放在盆中，确保盘中没有多余水分
方法: 摆放
工具: 塑料盆

### 第6步
步骤: 步骤6
描述: 取一块50g姜，用削皮刀把表面的皮去除并洗干净，然后切成厚度为3mm的姜片
方法: 去皮,切
工具: 削皮刀,菜刀

### 第7步
步骤: 步骤7
描述: 将小米辣洗干净、去蒂，切成厚度为2mm的小圆片（或切成1mm宽度的丝状）
方法: 切
工具: 菜刀

### 第8步
步骤: 步骤8
描述: 将小葱洗干净，去除根须，切成3cm的小段，稍微粗一点的小葱，可以沿中间劈开
方法: 切
工具: 菜刀

### 第9步
步骤: 步骤9
描述: 加入8g盐、25g料酒到盆中，带上一次性手套，对鱼进行全身按摩1分钟，确保鱼身每个部位都均匀涂抹了盐和料酒
方法: 腌制,按摩
工具: 塑料盆,一次性手套
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 在鱼身的每一个刀口中塞入一片姜片，鱼肚子中放入3片姜片，腌制10分钟
方法: 腌制
工具: 塑料盆
时间: 10分钟

### 第11步
步骤: 步骤11
描述: 在鱼腌制期间，在蒸锅中加入5L清水，烧开后，在蒸锅上放上蒸笼
方法: 烧水
工具: 蒸锅,蒸笼

### 第12步
步骤: 步骤12
描述: 鱼腌制好后，会析出水分，将多余水分和腌制用料酒、姜片倒掉，用清水冲洗干净鱼身和鱼肚，用厨房纸擦干
方法: 冲洗,擦干
工具: 厨房纸

### 第13步
步骤: 步骤13
描述: 将鱼平放在蒸鱼盘中，重新在鱼身、鱼肚刀口处塞入姜片
方法: 摆放
工具: 蒸鱼盘

### 第14步
步骤: 步骤14
描述: 将蒸鱼盘放入蒸笼中，盖上盖子，中火蒸20分钟
方法: 蒸
工具: 蒸笼,防烫夹
时间: 20分钟

### 第15步
步骤: 步骤15
描述: 用防烫夹将蒸鱼盘夹出，在鱼身和鱼周围淋上10g蒸鱼豉油
方法: 淋汁
工具: 防烫夹

### 第16步
步骤: 步骤16
描述: 在鱼身和周围均匀撒上小葱段和小米辣
方法: 撒料

### 第17步
步骤: 步骤17
描述: 在铁锅中倒入15g植物油，用中小火慢熬5分钟，不要用大火，否则油会挥发很快
方法: 熬油
工具: 铁锅
时间: 5分钟

### 第18步
步骤: 步骤18
描述: 将出锅后的热油均匀地慢慢地淋在鱼身上，鲜掉眉毛的葱油桂鱼就出炉啦！
方法: 淋油
工具: 铁锅

关联图谱:
- OUT REQUIRES 植物油 (Ingredient): category: 调料
- OUT REQUIRES 小米辣 (Ingredient): category: 蔬菜
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.5975586175918579, search_type=vector_enhanced

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

### result_order=3
source: reranked_results
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.5703058242797852, search_type=vector_enhanced

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
metadata_summary: node_id=201000040, chunk_id=201000040_chunk_11, recipe_name=水煮鱼, category=水产, score=0.5662153959274292, search_type=vector_enhanced

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

### result_order=5
source: reranked_results
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.5821714401245117, search_type=vector_enhanced

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
metadata_summary: node_id=201000453, chunk_id=201000453_chunk_83, recipe_name=鲤鱼炖白菜, category=水产, score=0.5673090815544128, search_type=vector_enhanced

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

### result_order=7
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

### result_order=8
source: reranked_results
metadata_summary: node_id=201000127, chunk_id=201000127_chunk_26, recipe_name=红烧鲤鱼, category=水产, score=0.5670437216758728, search_type=vector_enhanced

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
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=13
source: reranked_results
metadata_summary: node_id=201004341, recipe_name=韭菜盒子, category=主食, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 煎制
菜品: 韭菜盒子
分类: 主食
难度: 3.0
主要食材: 香油, 韭菜, 盐
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=14
source: reranked_results
metadata_summary: node_id=201005492, recipe_name=烤茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 烤茄子
分类: 素菜
难度: 3.0
主要食材: 茄子, 食用油, 孜然
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=15
source: reranked_results
metadata_summary: node_id=201000628, recipe_name=燕麦鸡蛋饼, category=早餐, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 煎制
菜品: 燕麦鸡蛋饼
分类: 早餐
难度: 2.0
主要食材: 牛奶, 胡椒, 纯干燕麦片
关联图谱:
- OUT REQUIRES 牛奶 (Ingredient): category: 其他
- OUT REQUIRES 胡椒 (Ingredient): category: 调料
- OUT REQUIRES 纯干燕麦片 (Ingredient): category: 淀粉类
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6305848956108093, search_type=vector_enhanced

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
metadata_summary: node_id=201000337, chunk_id=201000337_chunk_62, recipe_name=葱油桂鱼, category=水产, score=0.5812851786613464, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 去菜市场买已经处理好的鱼（自己处理的话最好不要内脏），将鱼身表面的所有鳞片刮干净
方法: 处理
工具: 菜刀

### 第2步
步骤: 步骤2
描述: 用厨房用纸将鱼肚子里的贴骨血和黑膜擦干净（帖骨血会影响口感，黑膜是鱼腥味的来源）
方法: 清理
工具: 厨房纸

### 第3步
步骤: 步骤3
描述: 用菜刀在鱼身表面来回刮几次，将鱼身的黏液刮掉，进一步去除腥味，然后用清水将鱼内外冲洗干净
方法: 清理,冲洗
工具: 菜刀

### 第4步
步骤: 步骤4
描述: 将鱼平放在砧板，使用厨房纸将鱼内外的水分擦干，然后鱼头朝左，尾朝右，从鱼鳃边开始，每隔3cm纵向划一刀，深度达到鱼的脊椎骨即可，另一面使用同样的处理方式
方法: 切
工具: 砧板,厨房纸,菜刀

### 第5步
步骤: 步骤5
描述: 将鱼平放在盆中，确保盘中没有多余水分
方法: 摆放
工具: 塑料盆

### 第6步
步骤: 步骤6
描述: 取一块50g姜，用削皮刀把表面的皮去除并洗干净，然后切成厚度为3mm的姜片
方法: 去皮,切
工具: 削皮刀,菜刀

### 第7步
步骤: 步骤7
描述: 将小米辣洗干净、去蒂，切成厚度为2mm的小圆片（或切成1mm宽度的丝状）
方法: 切
工具: 菜刀

### 第8步
步骤: 步骤8
描述: 将小葱洗干净，去除根须，切成3cm的小段，稍微粗一点的小葱，可以沿中间劈开
方法: 切
工具: 菜刀

### 第9步
步骤: 步骤9
描述: 加入8g盐、25g料酒到盆中，带上一次性手套，对鱼进行全身按摩1分钟，确保鱼身每个部位都均匀涂抹了盐和料酒
方法: 腌制,按摩
工具: 塑料盆,一次性手套
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 在鱼身的每一个刀口中塞入一片姜片，鱼肚子中放入3片姜片，腌制10分钟
方法: 腌制
工具: 塑料盆
时间: 10分钟

### 第11步
步骤: 步骤11
描述: 在鱼腌制期间，在蒸锅中加入5L清水，烧开后，在蒸锅上放上蒸笼
方法: 烧水
工具: 蒸锅,蒸笼

### 第12步
步骤: 步骤12
描述: 鱼腌制好后，会析出水分，将多余水分和腌制用料酒、姜片倒掉，用清水冲洗干净鱼身和鱼肚，用厨房纸擦干
方法: 冲洗,擦干
工具: 厨房纸

### 第13步
步骤: 步骤13
描述: 将鱼平放在蒸鱼盘中，重新在鱼身、鱼肚刀口处塞入姜片
方法: 摆放
工具: 蒸鱼盘

### 第14步
步骤: 步骤14
描述: 将蒸鱼盘放入蒸笼中，盖上盖子，中火蒸20分钟
方法: 蒸
工具: 蒸笼,防烫夹
时间: 20分钟

### 第15步
步骤: 步骤15
描述: 用防烫夹将蒸鱼盘夹出，在鱼身和鱼周围淋上10g蒸鱼豉油
方法: 淋汁
工具: 防烫夹

### 第16步
步骤: 步骤16
描述: 在鱼身和周围均匀撒上小葱段和小米辣
方法: 撒料

### 第17步
步骤: 步骤17
描述: 在铁锅中倒入15g植物油，用中小火慢熬5分钟，不要用大火，否则油会挥发很快
方法: 熬油
工具: 铁锅
时间: 5分钟

### 第18步
步骤: 步骤18
描述: 将出锅后的热油均匀地慢慢地淋在鱼身上，鲜掉眉毛的葱油桂鱼就出炉啦！
方法: 淋油
工具: 铁锅

关联图谱:
- OUT REQUIRES 植物油 (Ingredient): category: 调料
- OUT REQUIRES 小米辣 (Ingredient): category: 蔬菜
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201000258, recipe_name=鲈鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲈鱼
食材名称: 鲈鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=3
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

### result_order=4
source: top_k_final
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6305848956108093, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
metadata_summary: node_id=201000337, chunk_id=201000337_chunk_62, recipe_name=葱油桂鱼, category=水产, score=0.5812851786613464, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 去菜市场买已经处理好的鱼（自己处理的话最好不要内脏），将鱼身表面的所有鳞片刮干净
方法: 处理
工具: 菜刀

### 第2步
步骤: 步骤2
描述: 用厨房用纸将鱼肚子里的贴骨血和黑膜擦干净（帖骨血会影响口感，黑膜是鱼腥味的来源）
方法: 清理
工具: 厨房纸

### 第3步
步骤: 步骤3
描述: 用菜刀在鱼身表面来回刮几次，将鱼身的黏液刮掉，进一步去除腥味，然后用清水将鱼内外冲洗干净
方法: 清理,冲洗
工具: 菜刀

### 第4步
步骤: 步骤4
描述: 将鱼平放在砧板，使用厨房纸将鱼内外的水分擦干，然后鱼头朝左，尾朝右，从鱼鳃边开始，每隔3cm纵向划一刀，深度达到鱼的脊椎骨即可，另一面使用同样的处理方式
方法: 切
工具: 砧板,厨房纸,菜刀

### 第5步
步骤: 步骤5
描述: 将鱼平放在盆中，确保盘中没有多余水分
方法: 摆放
工具: 塑料盆

### 第6步
步骤: 步骤6
描述: 取一块50g姜，用削皮刀把表面的皮去除并洗干净，然后切成厚度为3mm的姜片
方法: 去皮,切
工具: 削皮刀,菜刀

### 第7步
步骤: 步骤7
描述: 将小米辣洗干净、去蒂，切成厚度为2mm的小圆片（或切成1mm宽度的丝状）
方法: 切
工具: 菜刀

### 第8步
步骤: 步骤8
描述: 将小葱洗干净，去除根须，切成3cm的小段，稍微粗一点的小葱，可以沿中间劈开
方法: 切
工具: 菜刀

### 第9步
步骤: 步骤9
描述: 加入8g盐、25g料酒到盆中，带上一次性手套，对鱼进行全身按摩1分钟，确保鱼身每个部位都均匀涂抹了盐和料酒
方法: 腌制,按摩
工具: 塑料盆,一次性手套
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 在鱼身的每一个刀口中塞入一片姜片，鱼肚子中放入3片姜片，腌制10分钟
方法: 腌制
工具: 塑料盆
时间: 10分钟

### 第11步
步骤: 步骤11
描述: 在鱼腌制期间，在蒸锅中加入5L清水，烧开后，在蒸锅上放上蒸笼
方法: 烧水
工具: 蒸锅,蒸笼

### 第12步
步骤: 步骤12
描述: 鱼腌制好后，会析出水分，将多余水分和腌制用料酒、姜片倒掉，用清水冲洗干净鱼身和鱼肚，用厨房纸擦干
方法: 冲洗,擦干
工具: 厨房纸

### 第13步
步骤: 步骤13
描述: 将鱼平放在蒸鱼盘中，重新在鱼身、鱼肚刀口处塞入姜片
方法: 摆放
工具: 蒸鱼盘

### 第14步
步骤: 步骤14
描述: 将蒸鱼盘放入蒸笼中，盖上盖子，中火蒸20分钟
方法: 蒸
工具: 蒸笼,防烫夹
时间: 20分钟

### 第15步
步骤: 步骤15
描述: 用防烫夹将蒸鱼盘夹出，在鱼身和鱼周围淋上10g蒸鱼豉油
方法: 淋汁
工具: 防烫夹

### 第16步
步骤: 步骤16
描述: 在鱼身和周围均匀撒上小葱段和小米辣
方法: 撒料

### 第17步
步骤: 步骤17
描述: 在铁锅中倒入15g植物油，用中小火慢熬5分钟，不要用大火，否则油会挥发很快
方法: 熬油
工具: 铁锅
时间: 5分钟

### 第18步
步骤: 步骤18
描述: 将出锅后的热油均匀地慢慢地淋在鱼身上，鲜掉眉毛的葱油桂鱼就出炉啦！
方法: 淋油
工具: 铁锅

关联图谱:
- OUT REQUIRES 植物油 (Ingredient): category: 调料
- OUT REQUIRES 小米辣 (Ingredient): category: 蔬菜
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=2
source: generation_context
metadata_summary: node_id=201000258, recipe_name=鲈鱼, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 鲈鱼
食材名称: 鲈鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=3
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

### result_order=4
source: generation_context
metadata_summary: node_id=201005146, recipe_name=蒲烧茄子, category=素菜, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 烤制
菜品: 蒲烧茄子
分类: 素菜
难度: 3.0
主要食材: 老抽, 料酒, 小葱
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

