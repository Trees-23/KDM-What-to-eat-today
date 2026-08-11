# Recall Content

audit_id: 20260811_173400_161_6be9ded1
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201002822, recipe_name=鳜鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鳜鱼
食材名称: 鳜鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: entity_level
metadata_summary: node_id=201002821, recipe_name=清蒸鳜鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 清蒸鳜鱼
菜品名称: 清蒸鳜鱼
分类: 荤菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

## Hybrid Retrieval / Topic Branch Raw Results
### result_order=0
source: topic_level
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
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
source: topic_level
metadata_summary: node_id=201002627, recipe_name=徽派红烧肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 徽菜
菜品: 徽派红烧肉
分类: 荤菜
菜系: 徽菜
难度: 4.0
主要食材: 蒜头, 五香粉, 五花肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.7233839631080627, search_type=vector_enhanced

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

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201003245, chunk_id=201003245_chunk_637, recipe_name=豆豉鲮鱼油麦菜, category=荤菜, score=0.673103392124176, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 油麦菜洗净后切段；鲮鱼罐头打开后，把鲮鱼主刺去除，切成小段后备用；大蒜切成末。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 锅热倒入食用油，油热后加入洗净的油麦菜，炒到萎蔫出水后盛出备用，倒掉炒制出的水分。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 重新热锅后，加入鲮鱼罐头中的油，放入蒜末煸香。
方法: 煸
工具: 炒锅,锅铲
时间: 30秒

### 第4步
步骤: 步骤4
描述: 蒜末煸香后加入鲮鱼罐头中的豆豉，翻拌后加入切碎的鲮鱼块，再次翻拌。
方法: 翻拌
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 翻拌均匀后加入油麦菜，加入生抽和糖调味，简单翻拌即可出锅装盘。
方法: 翻拌
工具: 锅铲
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201000472, chunk_id=201000472_chunk_87, recipe_name=鳊鱼炖豆腐, category=水产, score=0.6720463037490845, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳊鱼改刀，放上姜片和料酒腌制5-10分钟
方法: 切,腌制
工具: 刀,盆
时间: 5-10分钟

### 第2步
步骤: 步骤2
描述: 老豆腐切块后放入水中备用
方法: 切
工具: 刀,案板,盆

### 第3步
步骤: 步骤3
描述: 锅中加油，可以放点盐在锅里，防止煎鱼的时候粘锅，把腌制的鱼用厨房纸擦干水分，把鱼放到锅中，两面都煎一下
方法: 煎
工具: 炒锅,锅铲,厨房纸
时间: 每面2-4分钟

### 第4步
步骤: 步骤4
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入葱姜蒜、干辣椒、香叶、八角炒出味道
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 炒出佐料香味后，加入料酒、生抽、老抽、冰糖、桂皮，倒入热水，水量和鱼平齐或者少点
方法: 炖
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 大火烧开后，放入老豆腐，豆腐贴在锅边，加入食盐，转小火
方法: 炖
工具: 炒锅

### 第7步
步骤: 步骤7
描述: 小火烧10-15分钟，然后大火收点汁，即可出锅
方法: 炖,收汁
工具: 炒锅
时间: 10-15分钟

关联图谱:
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 八角 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6513749957084656, search_type=vector_enhanced

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
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_556, recipe_name=清蒸鳜鱼, category=荤菜, score=0.6490607857704163, search_type=vector_enhanced

```text
## 所需食材
1. 大葱(1节)
2. 姜片(3片)
3. 小葱(2根)
4. 生抽(30g)
5. 红辣椒(1颗)
6. 食用油(20ml)
7. 鳜鱼(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6365498304367065, search_type=vector_enhanced

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

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.6361489295959473, search_type=vector_enhanced

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
source: vector_enhanced
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6356806755065918, search_type=vector_enhanced

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

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6299989819526672, search_type=vector_enhanced

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
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.6272690892219543, search_type=vector_enhanced

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

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201002822, recipe_name=鳜鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鳜鱼
食材名称: 鳜鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201002821, recipe_name=清蒸鳜鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 清蒸鳜鱼
菜品名称: 清蒸鳜鱼
分类: 荤菜
难度: 3.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
```

### result_order=2
source: branch_grouped
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
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
source: branch_grouped
metadata_summary: node_id=201002627, recipe_name=徽派红烧肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 徽菜
菜品: 徽派红烧肉
分类: 荤菜
菜系: 徽菜
难度: 4.0
主要食材: 蒜头, 五香粉, 五花肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.7233839631080627, search_type=vector_enhanced

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

### result_order=7
source: branch_grouped
metadata_summary: node_id=201003245, chunk_id=201003245_chunk_637, recipe_name=豆豉鲮鱼油麦菜, category=荤菜, score=0.673103392124176, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 油麦菜洗净后切段；鲮鱼罐头打开后，把鲮鱼主刺去除，切成小段后备用；大蒜切成末。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 锅热倒入食用油，油热后加入洗净的油麦菜，炒到萎蔫出水后盛出备用，倒掉炒制出的水分。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 重新热锅后，加入鲮鱼罐头中的油，放入蒜末煸香。
方法: 煸
工具: 炒锅,锅铲
时间: 30秒

### 第4步
步骤: 步骤4
描述: 蒜末煸香后加入鲮鱼罐头中的豆豉，翻拌后加入切碎的鲮鱼块，再次翻拌。
方法: 翻拌
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 翻拌均匀后加入油麦菜，加入生抽和糖调味，简单翻拌即可出锅装盘。
方法: 翻拌
工具: 锅铲
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=201000472, chunk_id=201000472_chunk_87, recipe_name=鳊鱼炖豆腐, category=水产, score=0.6720463037490845, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳊鱼改刀，放上姜片和料酒腌制5-10分钟
方法: 切,腌制
工具: 刀,盆
时间: 5-10分钟

### 第2步
步骤: 步骤2
描述: 老豆腐切块后放入水中备用
方法: 切
工具: 刀,案板,盆

### 第3步
步骤: 步骤3
描述: 锅中加油，可以放点盐在锅里，防止煎鱼的时候粘锅，把腌制的鱼用厨房纸擦干水分，把鱼放到锅中，两面都煎一下
方法: 煎
工具: 炒锅,锅铲,厨房纸
时间: 每面2-4分钟

### 第4步
步骤: 步骤4
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入葱姜蒜、干辣椒、香叶、八角炒出味道
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 炒出佐料香味后，加入料酒、生抽、老抽、冰糖、桂皮，倒入热水，水量和鱼平齐或者少点
方法: 炖
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 大火烧开后，放入老豆腐，豆腐贴在锅边，加入食盐，转小火
方法: 炖
工具: 炒锅

### 第7步
步骤: 步骤7
描述: 小火烧10-15分钟，然后大火收点汁，即可出锅
方法: 炖,收汁
工具: 炒锅
时间: 10-15分钟

关联图谱:
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 八角 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6513749957084656, search_type=vector_enhanced

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

### result_order=10
source: branch_grouped
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_556, recipe_name=清蒸鳜鱼, category=荤菜, score=0.6490607857704163, search_type=vector_enhanced

```text
## 所需食材
1. 大葱(1节)
2. 姜片(3片)
3. 小葱(2根)
4. 生抽(30g)
5. 红辣椒(1颗)
6. 食用油(20ml)
7. 鳜鱼(500g)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6365498304367065, search_type=vector_enhanced

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

### result_order=12
source: branch_grouped
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.6361489295959473, search_type=vector_enhanced

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

### result_order=13
source: branch_grouped
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6356806755065918, search_type=vector_enhanced

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

### result_order=14
source: branch_grouped
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6299989819526672, search_type=vector_enhanced

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
source: branch_grouped
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.6272690892219543, search_type=vector_enhanced

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

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201002822, recipe_name=鳜鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鳜鱼
食材名称: 鳜鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.7233839631080627, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
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
source: merged_candidates
metadata_summary: node_id=201002627, recipe_name=徽派红烧肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 徽菜
菜品: 徽派红烧肉
分类: 荤菜
菜系: 徽菜
难度: 4.0
主要食材: 蒜头, 五香粉, 五花肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201003245, chunk_id=201003245_chunk_637, recipe_name=豆豉鲮鱼油麦菜, category=荤菜, score=0.673103392124176, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 油麦菜洗净后切段；鲮鱼罐头打开后，把鲮鱼主刺去除，切成小段后备用；大蒜切成末。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 锅热倒入食用油，油热后加入洗净的油麦菜，炒到萎蔫出水后盛出备用，倒掉炒制出的水分。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 重新热锅后，加入鲮鱼罐头中的油，放入蒜末煸香。
方法: 煸
工具: 炒锅,锅铲
时间: 30秒

### 第4步
步骤: 步骤4
描述: 蒜末煸香后加入鲮鱼罐头中的豆豉，翻拌后加入切碎的鲮鱼块，再次翻拌。
方法: 翻拌
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 翻拌均匀后加入油麦菜，加入生抽和糖调味，简单翻拌即可出锅装盘。
方法: 翻拌
工具: 锅铲
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201000472, chunk_id=201000472_chunk_87, recipe_name=鳊鱼炖豆腐, category=水产, score=0.6720463037490845, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳊鱼改刀，放上姜片和料酒腌制5-10分钟
方法: 切,腌制
工具: 刀,盆
时间: 5-10分钟

### 第2步
步骤: 步骤2
描述: 老豆腐切块后放入水中备用
方法: 切
工具: 刀,案板,盆

### 第3步
步骤: 步骤3
描述: 锅中加油，可以放点盐在锅里，防止煎鱼的时候粘锅，把腌制的鱼用厨房纸擦干水分，把鱼放到锅中，两面都煎一下
方法: 煎
工具: 炒锅,锅铲,厨房纸
时间: 每面2-4分钟

### 第4步
步骤: 步骤4
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入葱姜蒜、干辣椒、香叶、八角炒出味道
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 炒出佐料香味后，加入料酒、生抽、老抽、冰糖、桂皮，倒入热水，水量和鱼平齐或者少点
方法: 炖
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 大火烧开后，放入老豆腐，豆腐贴在锅边，加入食盐，转小火
方法: 炖
工具: 炒锅

### 第7步
步骤: 步骤7
描述: 小火烧10-15分钟，然后大火收点汁，即可出锅
方法: 炖,收汁
工具: 炒锅
时间: 10-15分钟

关联图谱:
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 八角 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6513749957084656, search_type=vector_enhanced

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

### result_order=9
source: merged_candidates
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6365498304367065, search_type=vector_enhanced

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
source: merged_candidates
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.6361489295959473, search_type=vector_enhanced

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

### result_order=11
source: merged_candidates
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6356806755065918, search_type=vector_enhanced

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

### result_order=12
source: merged_candidates
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6299989819526672, search_type=vector_enhanced

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

### result_order=13
source: merged_candidates
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.6272690892219543, search_type=vector_enhanced

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

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 鳜鱼
食材名称: 鳜鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=1
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

### pair_order=2
source: rerank_input

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
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

### pair_order=5
source: rerank_input

```text
命中关键词: 徽菜
菜品: 徽派红烧肉
分类: 荤菜
菜系: 徽菜
难度: 4.0
主要食材: 蒜头, 五香粉, 五花肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=6
source: rerank_input

```text
菜品: 豆豉鲮鱼油麦菜
菜系: 粤菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 油麦菜洗净后切段；鲮鱼罐头打开后，把鲮鱼主刺去除，切成小段后备用；大蒜切成末。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 锅热倒入食用油，油热后加入洗净的油麦菜，炒到萎蔫出水后盛出备用，倒掉炒制出的水分。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 重新热锅后，加入鲮鱼罐头中的油，放入蒜末煸香。
方法: 煸
工具: 炒锅,锅铲
时间: 30秒

### 第4步
步骤: 步骤4
描述: 蒜末煸香后加入鲮鱼罐头中的豆豉，翻拌后加入切碎的鲮鱼块，再次翻拌。
方法: 翻拌
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 翻拌均匀后加入油麦菜，加入生抽和糖调味，简单翻拌即可出锅装盘。
方法: 翻拌
工具: 锅铲
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=7
source: rerank_input

```text
菜品: 鳊鱼炖豆腐
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳊鱼改刀，放上姜片和料酒腌制5-10分钟
方法: 切,腌制
工具: 刀,盆
时间: 5-10分钟

### 第2步
步骤: 步骤2
描述: 老豆腐切块后放入水中备用
方法: 切
工具: 刀,案板,盆

### 第3步
步骤: 步骤3
描述: 锅中加油，可以放点盐在锅里，防止煎鱼的时候粘锅，把腌制的鱼用厨房纸擦干水分，把鱼放到锅中，两面都煎一下
方法: 煎
工具: 炒锅,锅铲,厨房纸
时间: 每面2-4分钟

### 第4步
步骤: 步骤4
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入葱姜蒜、干辣椒、香叶、八角炒出味道
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 炒出佐料香味后，加入料酒、生抽、老抽、冰糖、桂皮，倒入热水，水量和鱼平齐或者少点
方法: 炖
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 大火烧开后，放入老豆腐，豆腐贴在锅边，加入食盐，转小火
方法: 炖
工具: 炒锅

### 第7步
步骤: 步骤7
描述: 小火烧10-15分钟，然后大火收点汁，即可出锅
方法: 炖,收汁
工具: 炒锅
时间: 10-15分钟

关联图谱:
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 八角 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
```

### pair_order=8
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

### pair_order=9
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

### pair_order=10
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

### pair_order=11
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

### pair_order=12
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

### pair_order=13
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

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.7233839631080627, search_type=vector_enhanced

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

### result_order=1
source: reranked_results
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6365498304367065, search_type=vector_enhanced

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
source: reranked_results
metadata_summary: node_id=201003245, chunk_id=201003245_chunk_637, recipe_name=豆豉鲮鱼油麦菜, category=荤菜, score=0.673103392124176, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 油麦菜洗净后切段；鲮鱼罐头打开后，把鲮鱼主刺去除，切成小段后备用；大蒜切成末。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 锅热倒入食用油，油热后加入洗净的油麦菜，炒到萎蔫出水后盛出备用，倒掉炒制出的水分。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 重新热锅后，加入鲮鱼罐头中的油，放入蒜末煸香。
方法: 煸
工具: 炒锅,锅铲
时间: 30秒

### 第4步
步骤: 步骤4
描述: 蒜末煸香后加入鲮鱼罐头中的豆豉，翻拌后加入切碎的鲮鱼块，再次翻拌。
方法: 翻拌
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 翻拌均匀后加入油麦菜，加入生抽和糖调味，简单翻拌即可出锅装盘。
方法: 翻拌
工具: 锅铲
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201000472, chunk_id=201000472_chunk_87, recipe_name=鳊鱼炖豆腐, category=水产, score=0.6720463037490845, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳊鱼改刀，放上姜片和料酒腌制5-10分钟
方法: 切,腌制
工具: 刀,盆
时间: 5-10分钟

### 第2步
步骤: 步骤2
描述: 老豆腐切块后放入水中备用
方法: 切
工具: 刀,案板,盆

### 第3步
步骤: 步骤3
描述: 锅中加油，可以放点盐在锅里，防止煎鱼的时候粘锅，把腌制的鱼用厨房纸擦干水分，把鱼放到锅中，两面都煎一下
方法: 煎
工具: 炒锅,锅铲,厨房纸
时间: 每面2-4分钟

### 第4步
步骤: 步骤4
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入葱姜蒜、干辣椒、香叶、八角炒出味道
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 炒出佐料香味后，加入料酒、生抽、老抽、冰糖、桂皮，倒入热水，水量和鱼平齐或者少点
方法: 炖
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 大火烧开后，放入老豆腐，豆腐贴在锅边，加入食盐，转小火
方法: 炖
工具: 炒锅

### 第7步
步骤: 步骤7
描述: 小火烧10-15分钟，然后大火收点汁，即可出锅
方法: 炖,收汁
工具: 炒锅
时间: 10-15分钟

关联图谱:
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 八角 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201002822, recipe_name=鳜鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鳜鱼
食材名称: 鳜鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201000290, chunk_id=201000290_chunk_54, recipe_name=糖醋鲤鱼, category=水产, score=0.6272690892219543, search_type=vector_enhanced

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
metadata_summary: node_id=201000223, chunk_id=201000223_chunk_42, recipe_name=烤鱼, category=水产, score=0.6513749957084656, search_type=vector_enhanced

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

### result_order=7
source: reranked_results
metadata_summary: node_id=201003916, chunk_id=201003916_chunk_770, recipe_name=昂刺鱼豆腐汤, category=汤类, score=0.6299989819526672, search_type=vector_enhanced

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
metadata_summary: node_id=201000424, chunk_id=201000424_chunk_79, recipe_name=香煎翘嘴鱼, category=水产, score=0.6361489295959473, search_type=vector_enhanced

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

### result_order=9
source: reranked_results
metadata_summary: node_id=201000073, chunk_id=201000073_chunk_18, recipe_name=红烧鱼, category=水产, score=0.6356806755065918, search_type=vector_enhanced

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

### result_order=10
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
metadata_summary: node_id=201002627, recipe_name=徽派红烧肉, category=荤菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 徽菜
菜品: 徽派红烧肉
分类: 荤菜
菜系: 徽菜
难度: 4.0
主要食材: 蒜头, 五香粉, 五花肉
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=13
source: reranked_results
metadata_summary: node_id=200000000, recipe_name=菜谱, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 菜谱
菜品名称: 菜谱
分类: 未知
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.7233839631080627, search_type=vector_enhanced

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

### result_order=1
source: top_k_final
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6365498304367065, search_type=vector_enhanced

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
source: top_k_final
metadata_summary: node_id=201003245, chunk_id=201003245_chunk_637, recipe_name=豆豉鲮鱼油麦菜, category=荤菜, score=0.673103392124176, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 油麦菜洗净后切段；鲮鱼罐头打开后，把鲮鱼主刺去除，切成小段后备用；大蒜切成末。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 锅热倒入食用油，油热后加入洗净的油麦菜，炒到萎蔫出水后盛出备用，倒掉炒制出的水分。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 重新热锅后，加入鲮鱼罐头中的油，放入蒜末煸香。
方法: 煸
工具: 炒锅,锅铲
时间: 30秒

### 第4步
步骤: 步骤4
描述: 蒜末煸香后加入鲮鱼罐头中的豆豉，翻拌后加入切碎的鲮鱼块，再次翻拌。
方法: 翻拌
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 翻拌均匀后加入油麦菜，加入生抽和糖调味，简单翻拌即可出锅装盘。
方法: 翻拌
工具: 锅铲
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201000472, chunk_id=201000472_chunk_87, recipe_name=鳊鱼炖豆腐, category=水产, score=0.6720463037490845, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳊鱼改刀，放上姜片和料酒腌制5-10分钟
方法: 切,腌制
工具: 刀,盆
时间: 5-10分钟

### 第2步
步骤: 步骤2
描述: 老豆腐切块后放入水中备用
方法: 切
工具: 刀,案板,盆

### 第3步
步骤: 步骤3
描述: 锅中加油，可以放点盐在锅里，防止煎鱼的时候粘锅，把腌制的鱼用厨房纸擦干水分，把鱼放到锅中，两面都煎一下
方法: 煎
工具: 炒锅,锅铲,厨房纸
时间: 每面2-4分钟

### 第4步
步骤: 步骤4
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入葱姜蒜、干辣椒、香叶、八角炒出味道
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 炒出佐料香味后，加入料酒、生抽、老抽、冰糖、桂皮，倒入热水，水量和鱼平齐或者少点
方法: 炖
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 大火烧开后，放入老豆腐，豆腐贴在锅边，加入食盐，转小火
方法: 炖
工具: 炒锅

### 第7步
步骤: 步骤7
描述: 小火烧10-15分钟，然后大火收点汁，即可出锅
方法: 炖,收汁
工具: 炒锅
时间: 10-15分钟

关联图谱:
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 八角 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201002822, recipe_name=鳜鱼, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鳜鱼
食材名称: 鳜鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201002821, chunk_id=201002821_chunk_557, recipe_name=清蒸鳜鱼, category=荤菜, score=0.7233839631080627, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=1
source: generation_context
metadata_summary: node_id=201000257, chunk_id=201000257_chunk_46, recipe_name=清蒸鲈鱼, category=水产, score=0.6365498304367065, search_type=vector_enhanced, route_strategy=hybrid_traditional

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
source: generation_context
metadata_summary: node_id=201003245, chunk_id=201003245_chunk_637, recipe_name=豆豉鲮鱼油麦菜, category=荤菜, score=0.673103392124176, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 油麦菜洗净后切段；鲮鱼罐头打开后，把鲮鱼主刺去除，切成小段后备用；大蒜切成末。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 锅热倒入食用油，油热后加入洗净的油麦菜，炒到萎蔫出水后盛出备用，倒掉炒制出的水分。
方法: 炒
工具: 炒锅,锅铲
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 重新热锅后，加入鲮鱼罐头中的油，放入蒜末煸香。
方法: 煸
工具: 炒锅,锅铲
时间: 30秒

### 第4步
步骤: 步骤4
描述: 蒜末煸香后加入鲮鱼罐头中的豆豉，翻拌后加入切碎的鲮鱼块，再次翻拌。
方法: 翻拌
工具: 锅铲
时间: 30秒

### 第5步
步骤: 步骤5
描述: 翻拌均匀后加入油麦菜，加入生抽和糖调味，简单翻拌即可出锅装盘。
方法: 翻拌
工具: 锅铲
时间: 30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201000472, chunk_id=201000472_chunk_87, recipe_name=鳊鱼炖豆腐, category=水产, score=0.6720463037490845, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鳊鱼改刀，放上姜片和料酒腌制5-10分钟
方法: 切,腌制
工具: 刀,盆
时间: 5-10分钟

### 第2步
步骤: 步骤2
描述: 老豆腐切块后放入水中备用
方法: 切
工具: 刀,案板,盆

### 第3步
步骤: 步骤3
描述: 锅中加油，可以放点盐在锅里，防止煎鱼的时候粘锅，把腌制的鱼用厨房纸擦干水分，把鱼放到锅中，两面都煎一下
方法: 煎
工具: 炒锅,锅铲,厨房纸
时间: 每面2-4分钟

### 第4步
步骤: 步骤4
描述: 等两面都煎好时，把鱼推向锅边一点，留点空间放入葱姜蒜、干辣椒、香叶、八角炒出味道
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 炒出佐料香味后，加入料酒、生抽、老抽、冰糖、桂皮，倒入热水，水量和鱼平齐或者少点
方法: 炖
工具: 炒锅

### 第6步
步骤: 步骤6
描述: 大火烧开后，放入老豆腐，豆腐贴在锅边，加入食盐，转小火
方法: 炖
工具: 炒锅

### 第7步
步骤: 步骤7
描述: 小火烧10-15分钟，然后大火收点汁，即可出锅
方法: 炖,收汁
工具: 炒锅
时间: 10-15分钟

关联图谱:
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 八角 (Ingredient): category: 调料
- OUT REQUIRES 干辣椒 (Ingredient): category: 调料
```

### result_order=4
source: generation_context
metadata_summary: node_id=201002822, recipe_name=鳜鱼, retrieval_level=entity, search_type=entity_level, route_strategy=hybrid_traditional

```text
命中关键词: 鳜鱼
食材名称: 鳜鱼
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

