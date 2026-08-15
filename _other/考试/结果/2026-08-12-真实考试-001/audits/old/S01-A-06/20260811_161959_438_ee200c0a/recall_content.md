# Recall Content

audit_id: 20260811_161959_438_ee200c0a
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201000386, recipe_name=蒜蓉虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒜蓉虾
菜品名称: 蒜蓉虾
分类: 水产
菜系: 粤菜
难度: 2.0
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
```

### result_order=1
source: entity_level
metadata_summary: node_id=201000497, recipe_name=鲜虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲜虾
食材名称: 鲜虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
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

### result_order=3
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

### result_order=4
source: entity_level
metadata_summary: node_id=201000339, recipe_name=小葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 小葱
食材名称: 小葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=5
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

### result_order=6
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

### result_order=7
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
metadata_summary: node_id=201005195, recipe_name=酸辣土豆丝, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 蒜香
菜品: 酸辣土豆丝
分类: 素菜
菜系: 川菜
难度: 2.0
主要食材: 红椒, 食用油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
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

### result_order=9
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

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201000386, chunk_id=201000386_chunk_68, recipe_name=蒜蓉虾, category=水产, score=0.792892575263977, search_type=vector_enhanced

```text
# 蒜蓉虾

菜系: 粤菜
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 3分钟
份量: 1

## 所需食材
1. 海虾(8只)
2. 生抽(5ml)
3. 蒜蓉酱(50g)
4. 食用油(20ml)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀从虾头中间切开，切到距离虾尾1 cm
方法: 切
工具: 刀
时间: 1-2分钟

### 第2步
步骤: 步骤2
描述: 将蒜蓉酱铺在虾身中间，放在盘子中
方法: 铺
工具: 盘子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 锅中倒入热水，将盘子放入锅中，大火蒸3分钟
方法: 蒸
工具: 蒸锅,盘子
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 烧热油，倒入虾盘中，倒入生抽
方法: 烧热,倒
工具: 锅,盘子
时间: 30秒
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.792692244052887, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.774455189704895, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201000272, chunk_id=201000272_chunk_50, recipe_name=白灼虾, category=水产, score=0.7724659442901611, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱切小块，姜切片，平铺平底锅。
方法: 切
工具: 刀,案板,平底锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 活虾冲洗一下（去除虾线、剪刀减掉虾腿虾须子都是可选操作），控水，铺在平底锅的洋葱、姜片之上。
方法: 冲洗,控水,铺
工具: 剪刀,盆
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅内倒入料酒，盖上锅盖，中火1分钟，小火5分钟，关火5分钟。
方法: 煮,焖
工具: 平底锅,锅盖
时间: 11分钟

### 第4步
步骤: 步骤4
描述: 制作蘸料：葱切成葱花、蒜切碎、倒入酱油、芝麻、香醋，搅拌之。
方法: 切,搅拌
工具: 刀,案板,碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 油烧热，淋入蘸料。
方法: 热油,淋
工具: 锅,勺子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 虾出锅，用干净的盘子装好。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.7681056261062622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201000206, chunk_id=201000206_chunk_38, recipe_name=油焖大虾, category=水产, score=0.7563009262084961, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 剪虾枪到根上，虾须虾爪都剪掉，沙包挑掉，开背虾线挑出来，洗净备用
方法: 切
工具: 剪刀,刀,案板,盆
时间: 约5-8分钟

### 第2步
步骤: 步骤2
描述: 炸料油：油温三成热放花椒，油热离火，放葱姜（不要让油变色最好），葱稍微变黄沥油
方法: 炸
工具: 炒锅,锅铲,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 下油，虾摆放整齐，两面变色后轻轻摁虾头
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 放姜米（姜切成细颗粒）、黄酒30g、水两小碗、盐3g、冰糖10克
方法: 炒
工具: 锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 大火烧开转小火盖盖子焖（中途不能再加汤水，不要开盖）
方法: 焖
工具: 炒锅,锅盖
时间: 约5-8分钟

### 第6步
步骤: 步骤6
描述: 皮亮虾弯就可以起锅，虾摆盘
方法: 摆盘
工具: 筷子,盘子
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 收汁：过滤后倒回锅里收浓，放葱油，汤汁剩余1/4时
方法: 收汁
工具: 锅铲,漏勺
时间: 约2-3分钟

### 第8步
步骤: 步骤8
描述: 浇汁，完成
方法: 浇汁
工具: 锅铲,勺子
时间: 约30秒

关联图谱:
- OUT REQUIRES 黄酒 (Ingredient): category: 调料
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 黑虎虾/明虾 (Ingredient): category: 蛋白质
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_91, recipe_name=黄油煎虾, category=水产, score=0.7503300905227661, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201000160, chunk_id=201000160_chunk_30, recipe_name=小龙虾, category=水产, score=0.7335136532783508, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小龙虾刷干净去虾线，葱切2cm葱段，姜蒜切末。
方法: 清洗,切
工具: 刷子,刀,案板
时间: 10-15分钟

### 第2步
步骤: 步骤2
描述: 烧油，油微热，下香叶、八角、桂皮、青花椒、花椒、子弹头辣椒。
方法: 煎,炒
工具: 炒锅
时间: 30-60秒

### 第3步
步骤: 步骤3
描述: 香料出香气之后下锅葱姜蒜。
方法: 炒
工具: 炒锅
时间: 30秒

### 第4步
步骤: 步骤4
描述: 葱姜蒜爆香后，加入郫县豆瓣、黄豆酱，炒出红油。
方法: 炒
工具: 炒锅
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 下小龙虾，翻炒至变色。
方法: 炒
工具: 炒锅
时间: 3-5分钟

### 第6步
步骤: 步骤6
描述: 加入啤酒，等啤酒烧开后加入生抽、盐。
方法: 煮,调味
工具: 炒锅
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 将小龙虾完全煮熟后出锅。
方法: 煮
工具: 炒锅
时间: 8-10分钟

关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201000184, chunk_id=201000184_chunk_34, recipe_name=干煎阿根廷红虾, category=水产, score=0.7166203856468201, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_70, recipe_name=蒜香黄油虾, category=水产, score=0.7141041159629822, search_type=vector_enhanced

```text
## 所需食材
1. 大蒜(20克)
2. 大虾(200克)
3. 无盐黄油(30克)
4. 柠檬(0.25个)
5. 橄榄油(10毫升)
6. 白葡萄酒(15毫升)

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201000386, recipe_name=蒜蓉虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 蒜蓉虾
菜品名称: 蒜蓉虾
分类: 水产
菜系: 粤菜
难度: 2.0
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
```

### result_order=1
source: branch_grouped
metadata_summary: node_id=201000497, recipe_name=鲜虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲜虾
食材名称: 鲜虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
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

### result_order=3
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

### result_order=4
source: branch_grouped
metadata_summary: node_id=201000339, recipe_name=小葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 小葱
食材名称: 小葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=5
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

### result_order=6
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

### result_order=7
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

### result_order=8
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

### result_order=9
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

### result_order=10
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

### result_order=11
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

### result_order=12
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

### result_order=13
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

### result_order=14
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

### result_order=15
source: branch_grouped
metadata_summary: node_id=201005195, recipe_name=酸辣土豆丝, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 蒜香
菜品: 酸辣土豆丝
分类: 素菜
菜系: 川菜
难度: 2.0
主要食材: 红椒, 食用油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=16
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

### result_order=17
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

### result_order=18
source: branch_grouped
metadata_summary: node_id=201000386, chunk_id=201000386_chunk_68, recipe_name=蒜蓉虾, category=水产, score=0.792892575263977, search_type=vector_enhanced

```text
# 蒜蓉虾

菜系: 粤菜
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 3分钟
份量: 1

## 所需食材
1. 海虾(8只)
2. 生抽(5ml)
3. 蒜蓉酱(50g)
4. 食用油(20ml)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀从虾头中间切开，切到距离虾尾1 cm
方法: 切
工具: 刀
时间: 1-2分钟

### 第2步
步骤: 步骤2
描述: 将蒜蓉酱铺在虾身中间，放在盘子中
方法: 铺
工具: 盘子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 锅中倒入热水，将盘子放入锅中，大火蒸3分钟
方法: 蒸
工具: 蒸锅,盘子
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 烧热油，倒入虾盘中，倒入生抽
方法: 烧热,倒
工具: 锅,盘子
时间: 30秒
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=19
source: branch_grouped
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.792692244052887, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=20
source: branch_grouped
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.774455189704895, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=21
source: branch_grouped
metadata_summary: node_id=201000272, chunk_id=201000272_chunk_50, recipe_name=白灼虾, category=水产, score=0.7724659442901611, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱切小块，姜切片，平铺平底锅。
方法: 切
工具: 刀,案板,平底锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 活虾冲洗一下（去除虾线、剪刀减掉虾腿虾须子都是可选操作），控水，铺在平底锅的洋葱、姜片之上。
方法: 冲洗,控水,铺
工具: 剪刀,盆
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅内倒入料酒，盖上锅盖，中火1分钟，小火5分钟，关火5分钟。
方法: 煮,焖
工具: 平底锅,锅盖
时间: 11分钟

### 第4步
步骤: 步骤4
描述: 制作蘸料：葱切成葱花、蒜切碎、倒入酱油、芝麻、香醋，搅拌之。
方法: 切,搅拌
工具: 刀,案板,碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 油烧热，淋入蘸料。
方法: 热油,淋
工具: 锅,勺子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 虾出锅，用干净的盘子装好。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=22
source: branch_grouped
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.7681056261062622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=23
source: branch_grouped
metadata_summary: node_id=201000206, chunk_id=201000206_chunk_38, recipe_name=油焖大虾, category=水产, score=0.7563009262084961, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 剪虾枪到根上，虾须虾爪都剪掉，沙包挑掉，开背虾线挑出来，洗净备用
方法: 切
工具: 剪刀,刀,案板,盆
时间: 约5-8分钟

### 第2步
步骤: 步骤2
描述: 炸料油：油温三成热放花椒，油热离火，放葱姜（不要让油变色最好），葱稍微变黄沥油
方法: 炸
工具: 炒锅,锅铲,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 下油，虾摆放整齐，两面变色后轻轻摁虾头
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 放姜米（姜切成细颗粒）、黄酒30g、水两小碗、盐3g、冰糖10克
方法: 炒
工具: 锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 大火烧开转小火盖盖子焖（中途不能再加汤水，不要开盖）
方法: 焖
工具: 炒锅,锅盖
时间: 约5-8分钟

### 第6步
步骤: 步骤6
描述: 皮亮虾弯就可以起锅，虾摆盘
方法: 摆盘
工具: 筷子,盘子
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 收汁：过滤后倒回锅里收浓，放葱油，汤汁剩余1/4时
方法: 收汁
工具: 锅铲,漏勺
时间: 约2-3分钟

### 第8步
步骤: 步骤8
描述: 浇汁，完成
方法: 浇汁
工具: 锅铲,勺子
时间: 约30秒

关联图谱:
- OUT REQUIRES 黄酒 (Ingredient): category: 调料
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 黑虎虾/明虾 (Ingredient): category: 蛋白质
```

### result_order=24
source: branch_grouped
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_91, recipe_name=黄油煎虾, category=水产, score=0.7503300905227661, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=25
source: branch_grouped
metadata_summary: node_id=201000160, chunk_id=201000160_chunk_30, recipe_name=小龙虾, category=水产, score=0.7335136532783508, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小龙虾刷干净去虾线，葱切2cm葱段，姜蒜切末。
方法: 清洗,切
工具: 刷子,刀,案板
时间: 10-15分钟

### 第2步
步骤: 步骤2
描述: 烧油，油微热，下香叶、八角、桂皮、青花椒、花椒、子弹头辣椒。
方法: 煎,炒
工具: 炒锅
时间: 30-60秒

### 第3步
步骤: 步骤3
描述: 香料出香气之后下锅葱姜蒜。
方法: 炒
工具: 炒锅
时间: 30秒

### 第4步
步骤: 步骤4
描述: 葱姜蒜爆香后，加入郫县豆瓣、黄豆酱，炒出红油。
方法: 炒
工具: 炒锅
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 下小龙虾，翻炒至变色。
方法: 炒
工具: 炒锅
时间: 3-5分钟

### 第6步
步骤: 步骤6
描述: 加入啤酒，等啤酒烧开后加入生抽、盐。
方法: 煮,调味
工具: 炒锅
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 将小龙虾完全煮熟后出锅。
方法: 煮
工具: 炒锅
时间: 8-10分钟

关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=26
source: branch_grouped
metadata_summary: node_id=201000184, chunk_id=201000184_chunk_34, recipe_name=干煎阿根廷红虾, category=水产, score=0.7166203856468201, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

### result_order=27
source: branch_grouped
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_70, recipe_name=蒜香黄油虾, category=水产, score=0.7141041159629822, search_type=vector_enhanced

```text
## 所需食材
1. 大蒜(20克)
2. 大虾(200克)
3. 无盐黄油(30克)
4. 柠檬(0.25个)
5. 橄榄油(10毫升)
6. 白葡萄酒(15毫升)

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201000386, chunk_id=201000386_chunk_68, recipe_name=蒜蓉虾, category=水产, score=0.792892575263977, search_type=vector_enhanced

```text
# 蒜蓉虾

菜系: 粤菜
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 3分钟
份量: 1

## 所需食材
1. 海虾(8只)
2. 生抽(5ml)
3. 蒜蓉酱(50g)
4. 食用油(20ml)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀从虾头中间切开，切到距离虾尾1 cm
方法: 切
工具: 刀
时间: 1-2分钟

### 第2步
步骤: 步骤2
描述: 将蒜蓉酱铺在虾身中间，放在盘子中
方法: 铺
工具: 盘子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 锅中倒入热水，将盘子放入锅中，大火蒸3分钟
方法: 蒸
工具: 蒸锅,盘子
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 烧热油，倒入虾盘中，倒入生抽
方法: 烧热,倒
工具: 锅,盘子
时间: 30秒
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=1
source: merged_candidates
metadata_summary: node_id=201000497, recipe_name=鲜虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲜虾
食材名称: 鲜虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=2
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

### result_order=3
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

### result_order=4
source: merged_candidates
metadata_summary: node_id=201000339, recipe_name=小葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 小葱
食材名称: 小葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=5
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

### result_order=6
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

### result_order=7
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

### result_order=8
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

### result_order=9
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

### result_order=10
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

### result_order=11
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

### result_order=12
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

### result_order=13
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

### result_order=14
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

### result_order=15
source: merged_candidates
metadata_summary: node_id=201005195, recipe_name=酸辣土豆丝, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 蒜香
菜品: 酸辣土豆丝
分类: 素菜
菜系: 川菜
难度: 2.0
主要食材: 红椒, 食用油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=16
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

### result_order=17
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

### result_order=18
source: merged_candidates
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.792692244052887, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=19
source: merged_candidates
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.774455189704895, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=20
source: merged_candidates
metadata_summary: node_id=201000272, chunk_id=201000272_chunk_50, recipe_name=白灼虾, category=水产, score=0.7724659442901611, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱切小块，姜切片，平铺平底锅。
方法: 切
工具: 刀,案板,平底锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 活虾冲洗一下（去除虾线、剪刀减掉虾腿虾须子都是可选操作），控水，铺在平底锅的洋葱、姜片之上。
方法: 冲洗,控水,铺
工具: 剪刀,盆
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅内倒入料酒，盖上锅盖，中火1分钟，小火5分钟，关火5分钟。
方法: 煮,焖
工具: 平底锅,锅盖
时间: 11分钟

### 第4步
步骤: 步骤4
描述: 制作蘸料：葱切成葱花、蒜切碎、倒入酱油、芝麻、香醋，搅拌之。
方法: 切,搅拌
工具: 刀,案板,碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 油烧热，淋入蘸料。
方法: 热油,淋
工具: 锅,勺子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 虾出锅，用干净的盘子装好。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=21
source: merged_candidates
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.7681056261062622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=22
source: merged_candidates
metadata_summary: node_id=201000206, chunk_id=201000206_chunk_38, recipe_name=油焖大虾, category=水产, score=0.7563009262084961, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 剪虾枪到根上，虾须虾爪都剪掉，沙包挑掉，开背虾线挑出来，洗净备用
方法: 切
工具: 剪刀,刀,案板,盆
时间: 约5-8分钟

### 第2步
步骤: 步骤2
描述: 炸料油：油温三成热放花椒，油热离火，放葱姜（不要让油变色最好），葱稍微变黄沥油
方法: 炸
工具: 炒锅,锅铲,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 下油，虾摆放整齐，两面变色后轻轻摁虾头
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 放姜米（姜切成细颗粒）、黄酒30g、水两小碗、盐3g、冰糖10克
方法: 炒
工具: 锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 大火烧开转小火盖盖子焖（中途不能再加汤水，不要开盖）
方法: 焖
工具: 炒锅,锅盖
时间: 约5-8分钟

### 第6步
步骤: 步骤6
描述: 皮亮虾弯就可以起锅，虾摆盘
方法: 摆盘
工具: 筷子,盘子
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 收汁：过滤后倒回锅里收浓，放葱油，汤汁剩余1/4时
方法: 收汁
工具: 锅铲,漏勺
时间: 约2-3分钟

### 第8步
步骤: 步骤8
描述: 浇汁，完成
方法: 浇汁
工具: 锅铲,勺子
时间: 约30秒

关联图谱:
- OUT REQUIRES 黄酒 (Ingredient): category: 调料
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 黑虎虾/明虾 (Ingredient): category: 蛋白质
```

### result_order=23
source: merged_candidates
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_91, recipe_name=黄油煎虾, category=水产, score=0.7503300905227661, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=24
source: merged_candidates
metadata_summary: node_id=201000160, chunk_id=201000160_chunk_30, recipe_name=小龙虾, category=水产, score=0.7335136532783508, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小龙虾刷干净去虾线，葱切2cm葱段，姜蒜切末。
方法: 清洗,切
工具: 刷子,刀,案板
时间: 10-15分钟

### 第2步
步骤: 步骤2
描述: 烧油，油微热，下香叶、八角、桂皮、青花椒、花椒、子弹头辣椒。
方法: 煎,炒
工具: 炒锅
时间: 30-60秒

### 第3步
步骤: 步骤3
描述: 香料出香气之后下锅葱姜蒜。
方法: 炒
工具: 炒锅
时间: 30秒

### 第4步
步骤: 步骤4
描述: 葱姜蒜爆香后，加入郫县豆瓣、黄豆酱，炒出红油。
方法: 炒
工具: 炒锅
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 下小龙虾，翻炒至变色。
方法: 炒
工具: 炒锅
时间: 3-5分钟

### 第6步
步骤: 步骤6
描述: 加入啤酒，等啤酒烧开后加入生抽、盐。
方法: 煮,调味
工具: 炒锅
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 将小龙虾完全煮熟后出锅。
方法: 煮
工具: 炒锅
时间: 8-10分钟

关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=25
source: merged_candidates
metadata_summary: node_id=201000184, chunk_id=201000184_chunk_34, recipe_name=干煎阿根廷红虾, category=水产, score=0.7166203856468201, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
分类: 水产
# 蒜蓉虾

菜系: 粤菜
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 3分钟
份量: 1

## 所需食材
1. 海虾(8只)
2. 生抽(5ml)
3. 蒜蓉酱(50g)
4. 食用油(20ml)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀从虾头中间切开，切到距离虾尾1 cm
方法: 切
工具: 刀
时间: 1-2分钟

### 第2步
步骤: 步骤2
描述: 将蒜蓉酱铺在虾身中间，放在盘子中
方法: 铺
工具: 盘子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 锅中倒入热水，将盘子放入锅中，大火蒸3分钟
方法: 蒸
工具: 蒸锅,盘子
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 烧热油，倒入虾盘中，倒入生抽
方法: 烧热,倒
工具: 锅,盘子
时间: 30秒
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### pair_order=1
source: rerank_input

```text
命中关键词: 鲜虾
食材名称: 鲜虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 大蒜
食材名称: 大蒜
类别: 调料
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 调料 (Category)
```

### pair_order=3
source: rerank_input

```text
命中关键词: 生姜
食材名称: 生姜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 小葱
食材名称: 小葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=5
source: rerank_input

```text
命中关键词: 生抽
食材名称: 生抽
类别: 调料
关联图谱:
- IN REQUIRES 茶叶蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 香辣鸡爪煲 (Recipe): category: 荤菜；cuisineType: 川菜；difficulty: 4.0
```

### pair_order=6
source: rerank_input

```text
命中关键词: 料酒
食材名称: 料酒
类别: 调料
关联图谱:
- IN REQUIRES 茭白炒肉 (Recipe): category: 荤菜；difficulty: 3.0
- IN REQUIRES 商芝肉 (Recipe): category: 荤菜；cuisineType: 西北菜；difficulty: 5.0
```

### pair_order=7
source: rerank_input

```text
命中关键词: 食用油
食材名称: 食用油
类别: 调料
关联图谱:
- IN REQUIRES 鲤鱼炖白菜 (Recipe): category: 水产；cuisineType: 川菜；difficulty: 3.0
- IN REQUIRES 青椒土豆炒肉 (Recipe): category: 荤菜；difficulty: 3.0
```

### pair_order=8
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

### pair_order=9
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

### pair_order=10
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

### pair_order=11
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

### pair_order=12
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

### pair_order=13
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

### pair_order=14
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

### pair_order=15
source: rerank_input

```text
命中关键词: 蒜香
菜品: 酸辣土豆丝
分类: 素菜
菜系: 川菜
难度: 2.0
主要食材: 红椒, 食用油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=16
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

### pair_order=17
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

### pair_order=18
source: rerank_input

```text
菜品: 芥末罗氏虾
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=19
source: rerank_input

```text
菜品: 芥末黄油罗氏虾
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### pair_order=20
source: rerank_input

```text
菜品: 白灼虾
分类: 水产
菜系: 粤菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱切小块，姜切片，平铺平底锅。
方法: 切
工具: 刀,案板,平底锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 活虾冲洗一下（去除虾线、剪刀减掉虾腿虾须子都是可选操作），控水，铺在平底锅的洋葱、姜片之上。
方法: 冲洗,控水,铺
工具: 剪刀,盆
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅内倒入料酒，盖上锅盖，中火1分钟，小火5分钟，关火5分钟。
方法: 煮,焖
工具: 平底锅,锅盖
时间: 11分钟

### 第4步
步骤: 步骤4
描述: 制作蘸料：葱切成葱花、蒜切碎、倒入酱油、芝麻、香醋，搅拌之。
方法: 切,搅拌
工具: 刀,案板,碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 油烧热，淋入蘸料。
方法: 热油,淋
工具: 锅,勺子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 虾出锅，用干净的盘子装好。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### pair_order=21
source: rerank_input

```text
菜品: 蒜香黄油虾
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### pair_order=22
source: rerank_input

```text
菜品: 油焖大虾
分类: 水产
菜系: 鲁菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 剪虾枪到根上，虾须虾爪都剪掉，沙包挑掉，开背虾线挑出来，洗净备用
方法: 切
工具: 剪刀,刀,案板,盆
时间: 约5-8分钟

### 第2步
步骤: 步骤2
描述: 炸料油：油温三成热放花椒，油热离火，放葱姜（不要让油变色最好），葱稍微变黄沥油
方法: 炸
工具: 炒锅,锅铲,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 下油，虾摆放整齐，两面变色后轻轻摁虾头
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 放姜米（姜切成细颗粒）、黄酒30g、水两小碗、盐3g、冰糖10克
方法: 炒
工具: 锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 大火烧开转小火盖盖子焖（中途不能再加汤水，不要开盖）
方法: 焖
工具: 炒锅,锅盖
时间: 约5-8分钟

### 第6步
步骤: 步骤6
描述: 皮亮虾弯就可以起锅，虾摆盘
方法: 摆盘
工具: 筷子,盘子
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 收汁：过滤后倒回锅里收浓，放葱油，汤汁剩余1/4时
方法: 收汁
工具: 锅铲,漏勺
时间: 约2-3分钟

### 第8步
步骤: 步骤8
描述: 浇汁，完成
方法: 浇汁
工具: 锅铲,勺子
时间: 约30秒

关联图谱:
- OUT REQUIRES 黄酒 (Ingredient): category: 调料
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 黑虎虾/明虾 (Ingredient): category: 蛋白质
```

### pair_order=23
source: rerank_input

```text
菜品: 黄油煎虾
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### pair_order=24
source: rerank_input

```text
分类: 水产
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小龙虾刷干净去虾线，葱切2cm葱段，姜蒜切末。
方法: 清洗,切
工具: 刷子,刀,案板
时间: 10-15分钟

### 第2步
步骤: 步骤2
描述: 烧油，油微热，下香叶、八角、桂皮、青花椒、花椒、子弹头辣椒。
方法: 煎,炒
工具: 炒锅
时间: 30-60秒

### 第3步
步骤: 步骤3
描述: 香料出香气之后下锅葱姜蒜。
方法: 炒
工具: 炒锅
时间: 30秒

### 第4步
步骤: 步骤4
描述: 葱姜蒜爆香后，加入郫县豆瓣、黄豆酱，炒出红油。
方法: 炒
工具: 炒锅
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 下小龙虾，翻炒至变色。
方法: 炒
工具: 炒锅
时间: 3-5分钟

### 第6步
步骤: 步骤6
描述: 加入啤酒，等啤酒烧开后加入生抽、盐。
方法: 煮,调味
工具: 炒锅
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 将小龙虾完全煮熟后出锅。
方法: 煮
工具: 炒锅
时间: 8-10分钟

关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### pair_order=25
source: rerank_input

```text
菜品: 干煎阿根廷红虾
分类: 水产
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201000386, chunk_id=201000386_chunk_68, recipe_name=蒜蓉虾, category=水产, score=0.792892575263977, search_type=vector_enhanced

```text
# 蒜蓉虾

菜系: 粤菜
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 3分钟
份量: 1

## 所需食材
1. 海虾(8只)
2. 生抽(5ml)
3. 蒜蓉酱(50g)
4. 食用油(20ml)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀从虾头中间切开，切到距离虾尾1 cm
方法: 切
工具: 刀
时间: 1-2分钟

### 第2步
步骤: 步骤2
描述: 将蒜蓉酱铺在虾身中间，放在盘子中
方法: 铺
工具: 盘子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 锅中倒入热水，将盘子放入锅中，大火蒸3分钟
方法: 蒸
工具: 蒸锅,盘子
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 烧热油，倒入虾盘中，倒入生抽
方法: 烧热,倒
工具: 锅,盘子
时间: 30秒
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.7681056261062622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=2
source: reranked_results
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.792692244052887, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201000319, chunk_id=201000319_chunk_58, recipe_name=芥末黄油罗氏虾, category=水产, score=0.774455189704895, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将罗氏虾剪掉头尾尖刺、触须和脚，剪刀把虾身开背，去除虾线。
方法: 切
工具: 剪刀
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 提前搅拌好芥末酱汁：酱油、蚝油、芥末、盐、糖，搅拌均匀！
方法: 搅拌
工具: 碗,筷子
时间: 约2分钟

### 第3步
步骤: 步骤3
描述: 洗好香菜，切段备用。
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第4步
步骤: 步骤4
描述: 罗氏虾沥掉水，锅中加入油，直接放入罗氏虾，中火，外表煎至金黄，捞出。
方法: 煎
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第5步
步骤: 步骤5
描述: 下入蒜蓉，大火，利用煎虾剩下的油继续煎炒蒜蓉，等到锅中白雾冒出，蒜蓉已经煎出香味，下虾和黄油，让虾充分吸收黄油香味。
方法: 炒
工具: 炒锅,锅铲
时间: 约2分钟

### 第6步
步骤: 步骤6
描述: 下入调好的酱汁，继续大火煮沸，翻炒虾，至酱汁收汁，加入酒（料酒、啤酒可以放30g，朗姆酒味道浓郁放15g即可）。
方法: 炒,煮
工具: 炒锅,锅铲
时间: 约3-4分钟

### 第7步
步骤: 步骤7
描述: 在等酱汁稍微收汁，加入香菜翻炒两下，即可出锅。
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT REQUIRES 芥末 (Ingredient): category: 调料
- OUT REQUIRES 白糖 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201000272, chunk_id=201000272_chunk_50, recipe_name=白灼虾, category=水产, score=0.7724659442901611, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱切小块，姜切片，平铺平底锅。
方法: 切
工具: 刀,案板,平底锅
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 活虾冲洗一下（去除虾线、剪刀减掉虾腿虾须子都是可选操作），控水，铺在平底锅的洋葱、姜片之上。
方法: 冲洗,控水,铺
工具: 剪刀,盆
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 锅内倒入料酒，盖上锅盖，中火1分钟，小火5分钟，关火5分钟。
方法: 煮,焖
工具: 平底锅,锅盖
时间: 11分钟

### 第4步
步骤: 步骤4
描述: 制作蘸料：葱切成葱花、蒜切碎、倒入酱油、芝麻、香醋，搅拌之。
方法: 切,搅拌
工具: 刀,案板,碗,筷子
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 油烧热，淋入蘸料。
方法: 热油,淋
工具: 锅,勺子
时间: 30秒

### 第6步
步骤: 步骤6
描述: 虾出锅，用干净的盘子装好。
方法: 装盘
工具: 盘子
时间: 30秒

关联图谱:
- OUT REQUIRES 蒜 (Ingredient): category: 蔬菜
- OUT REQUIRES 食用油 (Ingredient): category: 调料
- OUT REQUIRES 蚝油 (Ingredient): category: 调料
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201000160, chunk_id=201000160_chunk_30, recipe_name=小龙虾, category=水产, score=0.7335136532783508, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 小龙虾刷干净去虾线，葱切2cm葱段，姜蒜切末。
方法: 清洗,切
工具: 刷子,刀,案板
时间: 10-15分钟

### 第2步
步骤: 步骤2
描述: 烧油，油微热，下香叶、八角、桂皮、青花椒、花椒、子弹头辣椒。
方法: 煎,炒
工具: 炒锅
时间: 30-60秒

### 第3步
步骤: 步骤3
描述: 香料出香气之后下锅葱姜蒜。
方法: 炒
工具: 炒锅
时间: 30秒

### 第4步
步骤: 步骤4
描述: 葱姜蒜爆香后，加入郫县豆瓣、黄豆酱，炒出红油。
方法: 炒
工具: 炒锅
时间: 1-2分钟

### 第5步
步骤: 步骤5
描述: 下小龙虾，翻炒至变色。
方法: 炒
工具: 炒锅
时间: 3-5分钟

### 第6步
步骤: 步骤6
描述: 加入啤酒，等啤酒烧开后加入生抽、盐。
方法: 煮,调味
工具: 炒锅
时间: 2-3分钟

### 第7步
步骤: 步骤7
描述: 将小龙虾完全煮熟后出锅。
方法: 煮
工具: 炒锅
时间: 8-10分钟

关联图谱:
- OUT REQUIRES 桂皮 (Ingredient): category: 调料
- OUT REQUIRES 郫县豆瓣 (Ingredient): category: 调料
- OUT REQUIRES 姜 (Ingredient): category: 蔬菜
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201000206, chunk_id=201000206_chunk_38, recipe_name=油焖大虾, category=水产, score=0.7563009262084961, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 剪虾枪到根上，虾须虾爪都剪掉，沙包挑掉，开背虾线挑出来，洗净备用
方法: 切
工具: 剪刀,刀,案板,盆
时间: 约5-8分钟

### 第2步
步骤: 步骤2
描述: 炸料油：油温三成热放花椒，油热离火，放葱姜（不要让油变色最好），葱稍微变黄沥油
方法: 炸
工具: 炒锅,锅铲,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 下油，虾摆放整齐，两面变色后轻轻摁虾头
方法: 煎
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第4步
步骤: 步骤4
描述: 放姜米（姜切成细颗粒）、黄酒30g、水两小碗、盐3g、冰糖10克
方法: 炒
工具: 锅铲
时间: 约30秒

### 第5步
步骤: 步骤5
描述: 大火烧开转小火盖盖子焖（中途不能再加汤水，不要开盖）
方法: 焖
工具: 炒锅,锅盖
时间: 约5-8分钟

### 第6步
步骤: 步骤6
描述: 皮亮虾弯就可以起锅，虾摆盘
方法: 摆盘
工具: 筷子,盘子
时间: 约30秒

### 第7步
步骤: 步骤7
描述: 收汁：过滤后倒回锅里收浓，放葱油，汤汁剩余1/4时
方法: 收汁
工具: 锅铲,漏勺
时间: 约2-3分钟

### 第8步
步骤: 步骤8
描述: 浇汁，完成
方法: 浇汁
工具: 锅铲,勺子
时间: 约30秒

关联图谱:
- OUT REQUIRES 黄酒 (Ingredient): category: 调料
- OUT REQUIRES 葱 (Ingredient): category: 蔬菜
- OUT REQUIRES 黑虎虾/明虾 (Ingredient): category: 蛋白质
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201000496, chunk_id=201000496_chunk_91, recipe_name=黄油煎虾, category=水产, score=0.7503300905227661, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鲜虾摘除头部，顺带扯出虾线（这步处理不好可在下一步开背时取出虾线），使用剪刀剪开或菜刀片开虾背，沥干水分备用
方法: 切
工具: 剪刀,菜刀,案板

### 第2步
步骤: 步骤2
描述: 调制酱汁：小碗放入上述量的全部生抽、米酒、白糖、盐搅匀备用
方法: 搅拌
工具: 小碗,筷子

### 第3步
步骤: 步骤3
描述: 中大火热锅，热锅内放入食用油，等待10秒让油温升高
方法: 炒
工具: 炒锅
时间: 10秒

### 第4步
步骤: 步骤4
描述: 虾全部放入锅中，开始瓶磨黑胡椒，均匀地撒在虾上翻炒
方法: 炒
工具: 炒锅,锅铲

### 第5步
步骤: 步骤5
描述: 虾变色后加入黄油，黄油完全融化后倒入调制酱汁，继续翻炒
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 大火翻炒15秒收汁即可装盘
方法: 炒
工具: 炒锅,锅铲
时间: 15秒

关联图谱:
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 米酒 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201000184, chunk_id=201000184_chunk_34, recipe_name=干煎阿根廷红虾, category=水产, score=0.7166203856468201, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 阿根廷红虾提前1天从速冻取出放到冷藏里自然解冻，可买已开背去虾线的成品
方法: 解冻
工具: 冰箱
时间: 24小时

### 第2步
步骤: 步骤2
描述: 解冻好的红虾洗净擦干，用厨房用纸吸干水分
方法: 清洗,擦干
工具: 厨房用纸
时间: 2分钟

### 第3步
步骤: 步骤3
描述: 生姜切片，洋葱切小方块，香菜洗净叶茎分离，香菜叶切碎，大蒜压碎切末
方法: 切,压碎
工具: 刀,案板,压蒜器
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 大火热锅，倒入橄榄油，油温升高后放入生姜片、洋葱块和香菜茎煸炒
方法: 热锅,煸炒
工具: 平底锅,锅铲
时间: 1分钟

### 第5步
步骤: 步骤5
描述: 约1分钟后取出姜、洋葱和香菜茎，弃用
方法: 取出
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 调中大火，放入红虾单面煎2分钟，同时给每只虾刷一层油
方法: 煎
工具: 平底锅,刷子
时间: 2分钟

### 第7步
步骤: 步骤7
描述: 待底面虾壳微焦黄时翻面，撒入大蒜碎末，轻晃锅使受热均匀
方法: 翻面,撒料,晃动
工具: 锅铲,平底锅
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 加入20ml白葡萄酒继续煎1分钟
方法: 煎
工具: 平底锅
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 调中小火，均匀撒盐和黑胡椒，每只虾滴一滴生抽
方法: 调味
工具: 手
时间: 30秒

### 第10步
步骤: 步骤10
描述: 撒上香菜叶装盘，切好柠檬片摆盘边即可
方法: 装盘
工具: 刀
时间: 30秒

关联图谱:
- OUT REQUIRES 橄榄油 (Ingredient): category: 调料
- OUT REQUIRES 黑胡椒 (Ingredient): category: 调料
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201005195, recipe_name=酸辣土豆丝, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 蒜香
菜品: 酸辣土豆丝
分类: 素菜
菜系: 川菜
难度: 2.0
主要食材: 红椒, 食用油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=10
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

### result_order=11
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

### result_order=12
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

### result_order=15
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

### result_order=16
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

### result_order=17
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

### result_order=18
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
metadata_summary: node_id=201000497, recipe_name=鲜虾, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鲜虾
食材名称: 鲜虾
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=21
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

### result_order=22
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

### result_order=23
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
metadata_summary: node_id=201000339, recipe_name=小葱, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 小葱
食材名称: 小葱
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201000386, chunk_id=201000386_chunk_68, recipe_name=蒜蓉虾, category=水产, score=0.792892575263977, search_type=vector_enhanced

```text
# 蒜蓉虾

菜系: 粤菜
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 3分钟
份量: 1

## 所需食材
1. 海虾(8只)
2. 生抽(5ml)
3. 蒜蓉酱(50g)
4. 食用油(20ml)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀从虾头中间切开，切到距离虾尾1 cm
方法: 切
工具: 刀
时间: 1-2分钟

### 第2步
步骤: 步骤2
描述: 将蒜蓉酱铺在虾身中间，放在盘子中
方法: 铺
工具: 盘子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 锅中倒入热水，将盘子放入锅中，大火蒸3分钟
方法: 蒸
工具: 蒸锅,盘子
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 烧热油，倒入虾盘中，倒入生抽
方法: 烧热,倒
工具: 锅,盘子
时间: 30秒
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.7681056261062622, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=2
source: top_k_final
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.792692244052887, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201005195, recipe_name=酸辣土豆丝, category=素菜, retrieval_level=topic, search_type=topic_level

```text
命中关键词: 蒜香
菜品: 酸辣土豆丝
分类: 素菜
菜系: 川菜
难度: 2.0
主要食材: 红椒, 食用油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
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
metadata_summary: node_id=201000386, chunk_id=201000386_chunk_68, recipe_name=蒜蓉虾, category=水产, score=0.792892575263977, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
# 蒜蓉虾

菜系: 粤菜
难度: 2.0星

时间信息: 准备时间: 5分钟, 烹饪时间: 3分钟
份量: 1

## 所需食材
1. 海虾(8只)
2. 生抽(5ml)
3. 蒜蓉酱(50g)
4. 食用油(20ml)

## 制作步骤

### 第1步
步骤: 步骤1
描述: 用刀从虾头中间切开，切到距离虾尾1 cm
方法: 切
工具: 刀
时间: 1-2分钟

### 第2步
步骤: 步骤2
描述: 将蒜蓉酱铺在虾身中间，放在盘子中
方法: 铺
工具: 盘子
时间: 30秒

### 第3步
步骤: 步骤3
描述: 锅中倒入热水，将盘子放入锅中，大火蒸3分钟
方法: 蒸
工具: 蒸锅,盘子
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 烧热油，倒入虾盘中，倒入生抽
方法: 烧热,倒
工具: 锅,盘子
时间: 30秒
关联图谱:
- OUT REQUIRES 海虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 生抽 (Ingredient): category: 调料
- OUT REQUIRES 食用油 (Ingredient): category: 调料
```

### result_order=1
source: generation_context
metadata_summary: node_id=201000395, chunk_id=201000395_chunk_71, recipe_name=蒜香黄油虾, category=水产, score=0.7681056261062622, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 大虾去头去壳留尾，用牙签挑去虾线，洗净后用厨房纸吸干水分
方法: 切,腌制
工具: 牙签,厨房纸
时间: 约2分钟

### 第2步
步骤: 步骤2
描述: 大蒜切成蒜末，备用
方法: 切
工具: 刀,案板
时间: 约1分钟

### 第3步
步骤: 步骤3
描述: 中火加热平底锅，放入10ml橄榄油
方法: 加热
工具: 平底锅
时间: 约30秒

### 第4步
步骤: 步骤4
描述: 油热后放入大虾，每面煎1-1.5分钟至变色，取出备用
方法: 煎
工具: 平底锅,厨房用夹
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 同一锅中加入黄油，融化后放入蒜末，小火炒香（约30秒）
方法: 炒,融化
工具: 平底锅
时间: 30秒

### 第6步
步骤: 步骤6
描述: 如使用白葡萄酒，此时加入并煮至酒精挥发（约1分钟）
方法: 煮
工具: 平底锅
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 将虾放回锅中，与蒜香黄油酱汁翻炒均匀（约1分钟）
方法: 炒
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 挤入柠檬汁，翻炒均匀后立即关火
方法: 炒
工具: 平底锅
时间: 10秒

### 第9步
步骤: 步骤9
描述: 装盘，淋上锅中剩余酱汁
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT REQUIRES 大虾 (Ingredient): category: 蛋白质
- OUT REQUIRES 柠檬 (Ingredient): category: 蔬菜
- OUT REQUIRES 白葡萄酒 (Ingredient): category: 调料
```

### result_order=2
source: generation_context
metadata_summary: node_id=201003103, chunk_id=201003103_chunk_609, recipe_name=芥末罗氏虾, category=荤菜, score=0.792692244052887, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将虾从背部切开，去除虾线和沙袋，也可从腹部切开，炸出来会胀开，成菜比较漂亮；用清水洗干净，控干水分后可拍上生粉，也可不拍。
方法: 切,清洗,拍粉
工具: 刀,案板,盆
时间: 约5分钟

### 第2步
步骤: 步骤2
描述: 将2颗大蒜切成蒜末；准备碗汁，放入生抽、蚝油、白糖、胡椒粉、盐，依据个人口味挤入芥末，加清水稀释后加入生粉化开。
方法: 切,调制
工具: 刀,案板,碗,筷子
时间: 约3分钟

### 第3步
步骤: 步骤3
描述: 锅热倒入食用油，大概能覆盖锅底；放入控干水分的罗氏虾，慢慢煎制。
方法: 煎
工具: 炒锅,锅铲
时间: 约3分钟

### 第4步
步骤: 步骤4
描述: 虾油煎出来后（表现为锅中出现大量气泡），加入准备好的蒜蓉及小米辣；闻到蒜蓉的香味后，加入黄油。
方法: 炒
工具: 锅铲
时间: 约1分钟

### 第5步
步骤: 步骤5
描述: 黄油融化后翻拌均匀，加入准备好的碗汁；盖锅盖焖煮2分钟汤汁浓稠后出锅。
方法: 焖煮
工具: 锅铲,锅盖
时间: 2分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: generation_context
metadata_summary: node_id=201005195, recipe_name=酸辣土豆丝, category=素菜, retrieval_level=topic, search_type=topic_level, route_strategy=hybrid_traditional

```text
命中关键词: 蒜香
菜品: 酸辣土豆丝
分类: 素菜
菜系: 川菜
难度: 2.0
主要食材: 红椒, 食用油, 大蒜
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
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

