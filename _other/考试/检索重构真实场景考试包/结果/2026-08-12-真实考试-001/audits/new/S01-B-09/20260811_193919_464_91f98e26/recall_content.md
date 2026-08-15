# Recall Content

audit_id: 20260811_193919_464_91f98e26
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201004478, recipe_name=扬州炒饭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 扬州炒饭
菜品名称: 扬州炒饭
分类: 主食
菜系: 苏菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
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

### result_order=2
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

### result_order=3
source: entity_level
metadata_summary: node_id=201000579, recipe_name=火腿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 火腿
食材名称: 火腿
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=4
source: entity_level
metadata_summary: node_id=201003785, recipe_name=虾仁, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 虾仁
食材名称: 虾仁
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=5
source: entity_level
metadata_summary: node_id=201003831, recipe_name=豌豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豌豆
食材名称: 豌豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=6
source: entity_level
metadata_summary: node_id=201001855, recipe_name=胡萝卜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 胡萝卜
食材名称: 胡萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
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

### result_order=9
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

## Hybrid Retrieval / Vector Branch Raw Results
### result_order=0
source: vector_enhanced
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_892, recipe_name=扬州炒饭, category=主食, score=0.7249600887298584, search_type=vector_enhanced

```text
# 扬州炒饭

菜系: 苏菜
难度: 4.0星

时间信息: 准备时间: 约15分钟（切丁、打蛋、焯水）, 烹饪时间: 约10分钟（炒制）
份量: 1-2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1173, recipe_name=炒/煎, category=烹饪技巧, score=0.6780569553375244, search_type=vector_enhanced

```text
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6669681072235107, search_type=vector_enhanced

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

### result_order=3
source: vector_enhanced
metadata_summary: node_id=201004943, chunk_id=201004943_chunk_974, recipe_name=水油焖蔬菜, category=素菜, score=0.6651962399482727, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洗净蔬菜
方法: 洗
工具: 盆
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入150ml水，并烧开
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 加入3g盐
方法: 调味
工具: 锅
时间: 5秒

### 第4步
步骤: 步骤4
描述: （可选）加入3ml蚝油
方法: 调味
工具: 锅
时间: 5秒

### 第5步
步骤: 步骤5
描述: 加入2ml食用油
方法: 调味
工具: 锅
时间: 5秒

### 第6步
步骤: 步骤6
描述: 下菜，翻拌一下，然后盖上锅盖焖1分钟
方法: 焖,翻拌
工具: 锅,锅铲
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 盛盘
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6614528298377991, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.657917857170105, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6552407741546631, search_type=vector_enhanced

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

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201004801, chunk_id=201004801_chunk_952, recipe_name=韩式拌饭, category=主食, score=0.6540777683258057, search_type=vector_enhanced

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

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_845, recipe_name=蛋包饭, category=主食, score=0.6533525586128235, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱、胡萝卜、火腿肠或鸡胸肉切成小丁，备用
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 热锅，锅中倒入10ml食用油，等待10秒加热
方法: 加热
工具: 炒锅
时间: 10秒

### 第3步
步骤: 步骤3
描述: 先放入洋葱丁翻炒1分钟，出香味后加入胡萝卜、玉米粒、青豆继续翻炒2分钟
方法: 炒
工具: 锅铲
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 加入火腿肠或鸡胸肉丁，炒至变色
方法: 炒
工具: 锅铲
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 加入米饭炒散后，加入番茄酱20ml，翻炒均匀，炒饭完成，盛出备用
方法: 炒
工具: 锅铲
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 鸡蛋打散，加入10ml牛奶搅匀
方法: 搅拌
工具: 盆,筷子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 锅中放入5ml食用油，倒入蛋液，轻晃锅底让蛋液均匀铺满锅面
方法: 煎
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 用小火加热，待蛋液表面半熟状态时，将炒饭放入蛋液中央
方法: 煎
工具: 锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 用铲子将蛋皮折叠包住米饭，形成椭圆形状
方法: 折叠
工具: 锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 用锅铲轻轻推至盘中，整理外形，可在表面挤上少量番茄酱装饰
方法: 装盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201003571, chunk_id=201003571_chunk_701, recipe_name=牛油火锅底料, category=半成品, score=0.6530097723007202, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅置旺火，放入牛油烧至八成热（240±10°C），加入老姜100g、大葱100g、洋葱100g、大蒜100g炸干吸尽牛油腥味后捞出扔掉。
方法: 炸
工具: 锅
时间: 约2-3分钟

### 第2步
步骤: 步骤2
描述: 加入色拉油或菜籽油1000ml、纯猪油500g，待油温降至五成热（150±10°C）时放入糍粑辣椒3000g，持续翻炒5-8分钟。
方法: 炒
工具: 锅
时间: 5-8分钟

### 第3步
步骤: 步骤3
描述: 加入郫县豆瓣1000g炒散，转中小火慢炒至料渣略发白翻砂并发出沙沙声。
方法: 炒
工具: 锅
时间: 约10-15分钟

### 第4步
步骤: 步骤4
描述: 当油呈樱桃红色时，加入姜片150g、大蒜100g炒香约15秒。
方法: 炒
工具: 锅
时间: 15秒

### 第5步
步骤: 步骤5
描述: 加入剁碎的永川豆鼓10g、豆母子140g炒香，再加入红花椒150g、小茴香10g炒香。
方法: 炒
工具: 锅
时间: 约1-2分钟

### 第6步
步骤: 步骤6
描述: 放入颗粒香料100g（已打碎至4mm颗粒）继续炒香。
方法: 炒
工具: 锅
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入麦芽粉12.5g炒散，再沿锅边淋入52%VOL白酒150ml炒散。
方法: 炒
工具: 锅
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 作为底料：起锅装入容器，置于10-20°C环境静置5天后使用风味最佳。
方法: 静置
工具: 容器
时间: 5天

### 第9步
步骤: 步骤9
描述: 作为老油：起锅后趁热加入干辣椒面15g搅匀，静置24小时。
方法: 静置
工具: 容器
时间: 24小时

### 第10步
步骤: 步骤10
描述: 将底料倒入锅中，加入3/5开水（底料:开水=2:3），大火烧开并撇去浮沫。
方法: 煮
工具: 锅
时间: 约5分钟

### 第11步
步骤: 步骤11
描述: 转中小火慢熬25-30分钟出味后过滤去渣。
方法: 熬,过滤
工具: 锅,滤网
时间: 25-30分钟

### 第12步
步骤: 步骤12
描述: 静置待油水分离，将表面油脂撇出，重新倒入净锅炼干水分，起锅装容器即为火锅老油。
方法: 撇油,炼干
工具: 锅,容器
时间: 约10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201004478, recipe_name=扬州炒饭, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 扬州炒饭
菜品名称: 扬州炒饭
分类: 主食
菜系: 苏菜
难度: 4.0
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
```

### result_order=1
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

### result_order=2
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

### result_order=3
source: branch_grouped
metadata_summary: node_id=201000579, recipe_name=火腿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 火腿
食材名称: 火腿
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201003785, recipe_name=虾仁, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 虾仁
食材名称: 虾仁
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201003831, recipe_name=豌豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豌豆
食材名称: 豌豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=201001855, recipe_name=胡萝卜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 胡萝卜
食材名称: 胡萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=7
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

### result_order=8
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

### result_order=9
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

### result_order=14
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

### result_order=15
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

### result_order=16
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

### result_order=17
source: branch_grouped
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_892, recipe_name=扬州炒饭, category=主食, score=0.7249600887298584, search_type=vector_enhanced

```text
# 扬州炒饭

菜系: 苏菜
难度: 4.0星

时间信息: 准备时间: 约15分钟（切丁、打蛋、焯水）, 烹饪时间: 约10分钟（炒制）
份量: 1-2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=18
source: branch_grouped
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1173, recipe_name=炒/煎, category=烹饪技巧, score=0.6780569553375244, search_type=vector_enhanced

```text
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=19
source: branch_grouped
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6669681072235107, search_type=vector_enhanced

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

### result_order=20
source: branch_grouped
metadata_summary: node_id=201004943, chunk_id=201004943_chunk_974, recipe_name=水油焖蔬菜, category=素菜, score=0.6651962399482727, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洗净蔬菜
方法: 洗
工具: 盆
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入150ml水，并烧开
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 加入3g盐
方法: 调味
工具: 锅
时间: 5秒

### 第4步
步骤: 步骤4
描述: （可选）加入3ml蚝油
方法: 调味
工具: 锅
时间: 5秒

### 第5步
步骤: 步骤5
描述: 加入2ml食用油
方法: 调味
工具: 锅
时间: 5秒

### 第6步
步骤: 步骤6
描述: 下菜，翻拌一下，然后盖上锅盖焖1分钟
方法: 焖,翻拌
工具: 锅,锅铲
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 盛盘
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=21
source: branch_grouped
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6614528298377991, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=22
source: branch_grouped
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.657917857170105, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=23
source: branch_grouped
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6552407741546631, search_type=vector_enhanced

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

### result_order=24
source: branch_grouped
metadata_summary: node_id=201004801, chunk_id=201004801_chunk_952, recipe_name=韩式拌饭, category=主食, score=0.6540777683258057, search_type=vector_enhanced

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

### result_order=25
source: branch_grouped
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_845, recipe_name=蛋包饭, category=主食, score=0.6533525586128235, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱、胡萝卜、火腿肠或鸡胸肉切成小丁，备用
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 热锅，锅中倒入10ml食用油，等待10秒加热
方法: 加热
工具: 炒锅
时间: 10秒

### 第3步
步骤: 步骤3
描述: 先放入洋葱丁翻炒1分钟，出香味后加入胡萝卜、玉米粒、青豆继续翻炒2分钟
方法: 炒
工具: 锅铲
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 加入火腿肠或鸡胸肉丁，炒至变色
方法: 炒
工具: 锅铲
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 加入米饭炒散后，加入番茄酱20ml，翻炒均匀，炒饭完成，盛出备用
方法: 炒
工具: 锅铲
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 鸡蛋打散，加入10ml牛奶搅匀
方法: 搅拌
工具: 盆,筷子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 锅中放入5ml食用油，倒入蛋液，轻晃锅底让蛋液均匀铺满锅面
方法: 煎
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 用小火加热，待蛋液表面半熟状态时，将炒饭放入蛋液中央
方法: 煎
工具: 锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 用铲子将蛋皮折叠包住米饭，形成椭圆形状
方法: 折叠
工具: 锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 用锅铲轻轻推至盘中，整理外形，可在表面挤上少量番茄酱装饰
方法: 装盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=26
source: branch_grouped
metadata_summary: node_id=201003571, chunk_id=201003571_chunk_701, recipe_name=牛油火锅底料, category=半成品, score=0.6530097723007202, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅置旺火，放入牛油烧至八成热（240±10°C），加入老姜100g、大葱100g、洋葱100g、大蒜100g炸干吸尽牛油腥味后捞出扔掉。
方法: 炸
工具: 锅
时间: 约2-3分钟

### 第2步
步骤: 步骤2
描述: 加入色拉油或菜籽油1000ml、纯猪油500g，待油温降至五成热（150±10°C）时放入糍粑辣椒3000g，持续翻炒5-8分钟。
方法: 炒
工具: 锅
时间: 5-8分钟

### 第3步
步骤: 步骤3
描述: 加入郫县豆瓣1000g炒散，转中小火慢炒至料渣略发白翻砂并发出沙沙声。
方法: 炒
工具: 锅
时间: 约10-15分钟

### 第4步
步骤: 步骤4
描述: 当油呈樱桃红色时，加入姜片150g、大蒜100g炒香约15秒。
方法: 炒
工具: 锅
时间: 15秒

### 第5步
步骤: 步骤5
描述: 加入剁碎的永川豆鼓10g、豆母子140g炒香，再加入红花椒150g、小茴香10g炒香。
方法: 炒
工具: 锅
时间: 约1-2分钟

### 第6步
步骤: 步骤6
描述: 放入颗粒香料100g（已打碎至4mm颗粒）继续炒香。
方法: 炒
工具: 锅
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入麦芽粉12.5g炒散，再沿锅边淋入52%VOL白酒150ml炒散。
方法: 炒
工具: 锅
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 作为底料：起锅装入容器，置于10-20°C环境静置5天后使用风味最佳。
方法: 静置
工具: 容器
时间: 5天

### 第9步
步骤: 步骤9
描述: 作为老油：起锅后趁热加入干辣椒面15g搅匀，静置24小时。
方法: 静置
工具: 容器
时间: 24小时

### 第10步
步骤: 步骤10
描述: 将底料倒入锅中，加入3/5开水（底料:开水=2:3），大火烧开并撇去浮沫。
方法: 煮
工具: 锅
时间: 约5分钟

### 第11步
步骤: 步骤11
描述: 转中小火慢熬25-30分钟出味后过滤去渣。
方法: 熬,过滤
工具: 锅,滤网
时间: 25-30分钟

### 第12步
步骤: 步骤12
描述: 静置待油水分离，将表面油脂撇出，重新倒入净锅炼干水分，起锅装容器即为火锅老油。
方法: 撇油,炼干
工具: 锅,容器
时间: 约10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_892, recipe_name=扬州炒饭, category=主食, score=0.7249600887298584, search_type=vector_enhanced

```text
# 扬州炒饭

菜系: 苏菜
难度: 4.0星

时间信息: 准备时间: 约15分钟（切丁、打蛋、焯水）, 烹饪时间: 约10分钟（炒制）
份量: 1-2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
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

### result_order=2
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

### result_order=3
source: merged_candidates
metadata_summary: node_id=201000579, recipe_name=火腿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 火腿
食材名称: 火腿
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201003785, recipe_name=虾仁, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 虾仁
食材名称: 虾仁
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201003831, recipe_name=豌豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豌豆
食材名称: 豌豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=201001855, recipe_name=胡萝卜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 胡萝卜
食材名称: 胡萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=7
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

### result_order=8
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

### result_order=9
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

### result_order=14
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

### result_order=15
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

### result_order=16
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

### result_order=17
source: merged_candidates
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1173, recipe_name=炒/煎, category=烹饪技巧, score=0.6780569553375244, search_type=vector_enhanced

```text
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=18
source: merged_candidates
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6669681072235107, search_type=vector_enhanced

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

### result_order=19
source: merged_candidates
metadata_summary: node_id=201004943, chunk_id=201004943_chunk_974, recipe_name=水油焖蔬菜, category=素菜, score=0.6651962399482727, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洗净蔬菜
方法: 洗
工具: 盆
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入150ml水，并烧开
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 加入3g盐
方法: 调味
工具: 锅
时间: 5秒

### 第4步
步骤: 步骤4
描述: （可选）加入3ml蚝油
方法: 调味
工具: 锅
时间: 5秒

### 第5步
步骤: 步骤5
描述: 加入2ml食用油
方法: 调味
工具: 锅
时间: 5秒

### 第6步
步骤: 步骤6
描述: 下菜，翻拌一下，然后盖上锅盖焖1分钟
方法: 焖,翻拌
工具: 锅,锅铲
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 盛盘
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=20
source: merged_candidates
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6614528298377991, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=21
source: merged_candidates
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.657917857170105, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=22
source: merged_candidates
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6552407741546631, search_type=vector_enhanced

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

### result_order=23
source: merged_candidates
metadata_summary: node_id=201004801, chunk_id=201004801_chunk_952, recipe_name=韩式拌饭, category=主食, score=0.6540777683258057, search_type=vector_enhanced

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

### result_order=24
source: merged_candidates
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_845, recipe_name=蛋包饭, category=主食, score=0.6533525586128235, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱、胡萝卜、火腿肠或鸡胸肉切成小丁，备用
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 热锅，锅中倒入10ml食用油，等待10秒加热
方法: 加热
工具: 炒锅
时间: 10秒

### 第3步
步骤: 步骤3
描述: 先放入洋葱丁翻炒1分钟，出香味后加入胡萝卜、玉米粒、青豆继续翻炒2分钟
方法: 炒
工具: 锅铲
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 加入火腿肠或鸡胸肉丁，炒至变色
方法: 炒
工具: 锅铲
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 加入米饭炒散后，加入番茄酱20ml，翻炒均匀，炒饭完成，盛出备用
方法: 炒
工具: 锅铲
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 鸡蛋打散，加入10ml牛奶搅匀
方法: 搅拌
工具: 盆,筷子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 锅中放入5ml食用油，倒入蛋液，轻晃锅底让蛋液均匀铺满锅面
方法: 煎
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 用小火加热，待蛋液表面半熟状态时，将炒饭放入蛋液中央
方法: 煎
工具: 锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 用铲子将蛋皮折叠包住米饭，形成椭圆形状
方法: 折叠
工具: 锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 用锅铲轻轻推至盘中，整理外形，可在表面挤上少量番茄酱装饰
方法: 装盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=25
source: merged_candidates
metadata_summary: node_id=201003571, chunk_id=201003571_chunk_701, recipe_name=牛油火锅底料, category=半成品, score=0.6530097723007202, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅置旺火，放入牛油烧至八成热（240±10°C），加入老姜100g、大葱100g、洋葱100g、大蒜100g炸干吸尽牛油腥味后捞出扔掉。
方法: 炸
工具: 锅
时间: 约2-3分钟

### 第2步
步骤: 步骤2
描述: 加入色拉油或菜籽油1000ml、纯猪油500g，待油温降至五成热（150±10°C）时放入糍粑辣椒3000g，持续翻炒5-8分钟。
方法: 炒
工具: 锅
时间: 5-8分钟

### 第3步
步骤: 步骤3
描述: 加入郫县豆瓣1000g炒散，转中小火慢炒至料渣略发白翻砂并发出沙沙声。
方法: 炒
工具: 锅
时间: 约10-15分钟

### 第4步
步骤: 步骤4
描述: 当油呈樱桃红色时，加入姜片150g、大蒜100g炒香约15秒。
方法: 炒
工具: 锅
时间: 15秒

### 第5步
步骤: 步骤5
描述: 加入剁碎的永川豆鼓10g、豆母子140g炒香，再加入红花椒150g、小茴香10g炒香。
方法: 炒
工具: 锅
时间: 约1-2分钟

### 第6步
步骤: 步骤6
描述: 放入颗粒香料100g（已打碎至4mm颗粒）继续炒香。
方法: 炒
工具: 锅
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入麦芽粉12.5g炒散，再沿锅边淋入52%VOL白酒150ml炒散。
方法: 炒
工具: 锅
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 作为底料：起锅装入容器，置于10-20°C环境静置5天后使用风味最佳。
方法: 静置
工具: 容器
时间: 5天

### 第9步
步骤: 步骤9
描述: 作为老油：起锅后趁热加入干辣椒面15g搅匀，静置24小时。
方法: 静置
工具: 容器
时间: 24小时

### 第10步
步骤: 步骤10
描述: 将底料倒入锅中，加入3/5开水（底料:开水=2:3），大火烧开并撇去浮沫。
方法: 煮
工具: 锅
时间: 约5分钟

### 第11步
步骤: 步骤11
描述: 转中小火慢熬25-30分钟出味后过滤去渣。
方法: 熬,过滤
工具: 锅,滤网
时间: 25-30分钟

### 第12步
步骤: 步骤12
描述: 静置待油水分离，将表面油脂撇出，重新倒入净锅炼干水分，起锅装容器即为火锅老油。
方法: 撇油,炼干
工具: 锅,容器
时间: 约10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_29af79a321e3, recipe_name=炒/煎, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 炒/煎
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
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
# 扬州炒饭

菜系: 苏菜
难度: 4.0星

时间信息: 准备时间: 约15分钟（切丁、打蛋、焯水）, 烹饪时间: 约10分钟（炒制）
份量: 1-2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=1
source: rerank_input

```text
命中关键词: 米饭
食材名称: 米饭
类别: 淀粉类
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 淀粉类 (Category)
```

### pair_order=2
source: rerank_input

```text
命中关键词: 鸡蛋
食材名称: 鸡蛋
类别: 蛋白质
关联图谱:
- IN REQUIRES 溏心蛋 (Recipe): category: 早餐；difficulty: 3.0
- IN REQUIRES 美式炒蛋 (Recipe): category: 早餐；difficulty: 2.0
```

### pair_order=3
source: rerank_input

```text
命中关键词: 火腿
食材名称: 火腿
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=4
source: rerank_input

```text
命中关键词: 虾仁
食材名称: 虾仁
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### pair_order=5
source: rerank_input

```text
命中关键词: 豌豆
食材名称: 豌豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=6
source: rerank_input

```text
命中关键词: 胡萝卜
食材名称: 胡萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### pair_order=7
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

### pair_order=8
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

### pair_order=9
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

### pair_order=13
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

### pair_order=14
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

### pair_order=15
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

### pair_order=16
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

### pair_order=17
source: rerank_input

```text
菜系: 技巧知识
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### pair_order=18
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

### pair_order=19
source: rerank_input

```text
菜品: 水油焖蔬菜
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洗净蔬菜
方法: 洗
工具: 盆
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入150ml水，并烧开
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 加入3g盐
方法: 调味
工具: 锅
时间: 5秒

### 第4步
步骤: 步骤4
描述: （可选）加入3ml蚝油
方法: 调味
工具: 锅
时间: 5秒

### 第5步
步骤: 步骤5
描述: 加入2ml食用油
方法: 调味
工具: 锅
时间: 5秒

### 第6步
步骤: 步骤6
描述: 下菜，翻拌一下，然后盖上锅盖焖1分钟
方法: 焖,翻拌
工具: 锅,锅铲
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 盛盘
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=20
source: rerank_input

```text
菜品: 炸酱面
菜系: 鲁菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=21
source: rerank_input

```text
菜品: 素炒豆角
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### pair_order=22
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

### pair_order=23
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

### pair_order=24
source: rerank_input

```text
菜品: 蛋包饭
菜系: 日式
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱、胡萝卜、火腿肠或鸡胸肉切成小丁，备用
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 热锅，锅中倒入10ml食用油，等待10秒加热
方法: 加热
工具: 炒锅
时间: 10秒

### 第3步
步骤: 步骤3
描述: 先放入洋葱丁翻炒1分钟，出香味后加入胡萝卜、玉米粒、青豆继续翻炒2分钟
方法: 炒
工具: 锅铲
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 加入火腿肠或鸡胸肉丁，炒至变色
方法: 炒
工具: 锅铲
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 加入米饭炒散后，加入番茄酱20ml，翻炒均匀，炒饭完成，盛出备用
方法: 炒
工具: 锅铲
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 鸡蛋打散，加入10ml牛奶搅匀
方法: 搅拌
工具: 盆,筷子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 锅中放入5ml食用油，倒入蛋液，轻晃锅底让蛋液均匀铺满锅面
方法: 煎
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 用小火加热，待蛋液表面半熟状态时，将炒饭放入蛋液中央
方法: 煎
工具: 锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 用铲子将蛋皮折叠包住米饭，形成椭圆形状
方法: 折叠
工具: 锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 用锅铲轻轻推至盘中，整理外形，可在表面挤上少量番茄酱装饰
方法: 装盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=25
source: rerank_input

```text
菜品: 牛油火锅底料
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅置旺火，放入牛油烧至八成热（240±10°C），加入老姜100g、大葱100g、洋葱100g、大蒜100g炸干吸尽牛油腥味后捞出扔掉。
方法: 炸
工具: 锅
时间: 约2-3分钟

### 第2步
步骤: 步骤2
描述: 加入色拉油或菜籽油1000ml、纯猪油500g，待油温降至五成热（150±10°C）时放入糍粑辣椒3000g，持续翻炒5-8分钟。
方法: 炒
工具: 锅
时间: 5-8分钟

### 第3步
步骤: 步骤3
描述: 加入郫县豆瓣1000g炒散，转中小火慢炒至料渣略发白翻砂并发出沙沙声。
方法: 炒
工具: 锅
时间: 约10-15分钟

### 第4步
步骤: 步骤4
描述: 当油呈樱桃红色时，加入姜片150g、大蒜100g炒香约15秒。
方法: 炒
工具: 锅
时间: 15秒

### 第5步
步骤: 步骤5
描述: 加入剁碎的永川豆鼓10g、豆母子140g炒香，再加入红花椒150g、小茴香10g炒香。
方法: 炒
工具: 锅
时间: 约1-2分钟

### 第6步
步骤: 步骤6
描述: 放入颗粒香料100g（已打碎至4mm颗粒）继续炒香。
方法: 炒
工具: 锅
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入麦芽粉12.5g炒散，再沿锅边淋入52%VOL白酒150ml炒散。
方法: 炒
工具: 锅
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 作为底料：起锅装入容器，置于10-20°C环境静置5天后使用风味最佳。
方法: 静置
工具: 容器
时间: 5天

### 第9步
步骤: 步骤9
描述: 作为老油：起锅后趁热加入干辣椒面15g搅匀，静置24小时。
方法: 静置
工具: 容器
时间: 24小时

### 第10步
步骤: 步骤10
描述: 将底料倒入锅中，加入3/5开水（底料:开水=2:3），大火烧开并撇去浮沫。
方法: 煮
工具: 锅
时间: 约5分钟

### 第11步
步骤: 步骤11
描述: 转中小火慢
```

### pair_order=26
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 炒/煎
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
* **若油锅起火，切不可倒水灭火**
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_892, recipe_name=扬州炒饭, category=主食, score=0.7249600887298584, search_type=vector_enhanced

```text
# 扬州炒饭

菜系: 苏菜
难度: 4.0星

时间信息: 准备时间: 约15分钟（切丁、打蛋、焯水）, 烹饪时间: 约10分钟（炒制）
份量: 1-2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6669681072235107, search_type=vector_enhanced

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

### result_order=2
source: reranked_results
metadata_summary: node_id=201004260, chunk_id=201004260_chunk_845, recipe_name=蛋包饭, category=主食, score=0.6533525586128235, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洋葱、胡萝卜、火腿肠或鸡胸肉切成小丁，备用
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 热锅，锅中倒入10ml食用油，等待10秒加热
方法: 加热
工具: 炒锅
时间: 10秒

### 第3步
步骤: 步骤3
描述: 先放入洋葱丁翻炒1分钟，出香味后加入胡萝卜、玉米粒、青豆继续翻炒2分钟
方法: 炒
工具: 锅铲
时间: 3分钟

### 第4步
步骤: 步骤4
描述: 加入火腿肠或鸡胸肉丁，炒至变色
方法: 炒
工具: 锅铲
时间: 2分钟

### 第5步
步骤: 步骤5
描述: 加入米饭炒散后，加入番茄酱20ml，翻炒均匀，炒饭完成，盛出备用
方法: 炒
工具: 锅铲
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 鸡蛋打散，加入10ml牛奶搅匀
方法: 搅拌
工具: 盆,筷子
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 锅中放入5ml食用油，倒入蛋液，轻晃锅底让蛋液均匀铺满锅面
方法: 煎
工具: 平底锅,锅铲
时间: 1分钟

### 第8步
步骤: 步骤8
描述: 用小火加热，待蛋液表面半熟状态时，将炒饭放入蛋液中央
方法: 煎
工具: 锅铲
时间: 2分钟

### 第9步
步骤: 步骤9
描述: 用铲子将蛋皮折叠包住米饭，形成椭圆形状
方法: 折叠
工具: 锅铲
时间: 1分钟

### 第10步
步骤: 步骤10
描述: 用锅铲轻轻推至盘中，整理外形，可在表面挤上少量番茄酱装饰
方法: 装盘
工具: 锅铲,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=3
source: reranked_results
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1173, recipe_name=炒/煎, category=烹饪技巧, score=0.6780569553375244, search_type=vector_enhanced

```text
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: reranked_results
metadata_summary: node_id=201004801, chunk_id=201004801_chunk_952, recipe_name=韩式拌饭, category=主食, score=0.6540777683258057, search_type=vector_enhanced

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
metadata_summary: node_id=technique_expansion:tipdoc_29af79a321e3, recipe_name=炒/煎, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 炒/煎
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
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201003571, chunk_id=201003571_chunk_701, recipe_name=牛油火锅底料, category=半成品, score=0.6530097723007202, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅置旺火，放入牛油烧至八成热（240±10°C），加入老姜100g、大葱100g、洋葱100g、大蒜100g炸干吸尽牛油腥味后捞出扔掉。
方法: 炸
工具: 锅
时间: 约2-3分钟

### 第2步
步骤: 步骤2
描述: 加入色拉油或菜籽油1000ml、纯猪油500g，待油温降至五成热（150±10°C）时放入糍粑辣椒3000g，持续翻炒5-8分钟。
方法: 炒
工具: 锅
时间: 5-8分钟

### 第3步
步骤: 步骤3
描述: 加入郫县豆瓣1000g炒散，转中小火慢炒至料渣略发白翻砂并发出沙沙声。
方法: 炒
工具: 锅
时间: 约10-15分钟

### 第4步
步骤: 步骤4
描述: 当油呈樱桃红色时，加入姜片150g、大蒜100g炒香约15秒。
方法: 炒
工具: 锅
时间: 15秒

### 第5步
步骤: 步骤5
描述: 加入剁碎的永川豆鼓10g、豆母子140g炒香，再加入红花椒150g、小茴香10g炒香。
方法: 炒
工具: 锅
时间: 约1-2分钟

### 第6步
步骤: 步骤6
描述: 放入颗粒香料100g（已打碎至4mm颗粒）继续炒香。
方法: 炒
工具: 锅
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入麦芽粉12.5g炒散，再沿锅边淋入52%VOL白酒150ml炒散。
方法: 炒
工具: 锅
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 作为底料：起锅装入容器，置于10-20°C环境静置5天后使用风味最佳。
方法: 静置
工具: 容器
时间: 5天

### 第9步
步骤: 步骤9
描述: 作为老油：起锅后趁热加入干辣椒面15g搅匀，静置24小时。
方法: 静置
工具: 容器
时间: 24小时

### 第10步
步骤: 步骤10
描述: 将底料倒入锅中，加入3/5开水（底料:开水=2:3），大火烧开并撇去浮沫。
方法: 煮
工具: 锅
时间: 约5分钟

### 第11步
步骤: 步骤11
描述: 转中小火慢熬25-30分钟出味后过滤去渣。
方法: 熬,过滤
工具: 锅,滤网
时间: 25-30分钟

### 第12步
步骤: 步骤12
描述: 静置待油水分离，将表面油脂撇出，重新倒入净锅炼干水分，起锅装容器即为火锅老油。
方法: 撇油,炼干
工具: 锅,容器
时间: 约10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201005031, chunk_id=201005031_chunk_998, recipe_name=素炒豆角, category=素菜, score=0.657917857170105, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 葱切花，蒜切沫，备用。
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生抽、老抽、耗油、盐混合调料汁，备用。
方法: 混合
工具: 碗或盆

### 第3步
步骤: 步骤3
描述: 小米椒切圈，备用。
方法: 切
工具: 刀,案板

### 第4步
步骤: 步骤4
描述: 豆角去筋，45°斜切4-10cm小段，备用。
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 起锅烧油(10ml-15ml)，冒烟后放入葱、小米椒，翻炒至闻到香味。
方法: 炒
工具: 炒锅,锅铲

### 第6步
步骤: 步骤6
描述: 加入豆角，翻炒30秒。
方法: 炒
工具: 锅铲
时间: 30秒

### 第7步
步骤: 步骤7
描述: 加入料汁，开大火翻炒2分钟。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 倒入150ml水，转中小火，盖上锅盖焖制8-10分钟。
方法: 焖
工具: 炒锅,锅盖
时间: 8-10分钟

### 第9步
步骤: 步骤9
描述: 加入蒜切沫，出锅。
方法: 炒
工具: 锅铲

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=8
source: reranked_results
metadata_summary: node_id=201004135, chunk_id=201004135_chunk_818, recipe_name=炸酱面, category=主食, score=0.6614528298377991, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 菜码切丝备用。
方法: 切
工具: 刀,案板
时间: 3分钟

### 第2步
步骤: 步骤2
描述: 葱切碎。油锅烧热，下葱和肉，炒至肉完全熟透（无红色）。
方法: 切,炒
工具: 刀,案板,炒锅,锅铲
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 下豆瓣酱和甜面酱，继续炒至微微粘稠。盛出，得到炸酱。
方法: 炒
工具: 锅铲
时间: 2分钟

### 第4步
步骤: 步骤4
描述: 取大碗，加凉水备用。
工具: 大碗
时间: 30秒

### 第5步
步骤: 步骤5
描述: 煮面条至断生（无白芯），盛入第4步装有凉水的碗中。
方法: 煮
工具: 锅,筷子
时间: 3-4分钟

### 第6步
步骤: 步骤6
描述: 立即控水捞出，盛入干净的碗中。
方法: 捞
工具: 筷子,漏勺
时间: 30秒

### 第7步
步骤: 步骤7
描述: 取第3步炸酱，倒入碗中，拌匀。然后取第1步菜码，倒入碗中，拌匀。
方法: 拌
工具: 筷子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=9
source: reranked_results
metadata_summary: node_id=201004943, chunk_id=201004943_chunk_974, recipe_name=水油焖蔬菜, category=素菜, score=0.6651962399482727, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 洗净蔬菜
方法: 洗
工具: 盆
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 锅中加入150ml水，并烧开
方法: 煮
工具: 锅
时间: 1分钟

### 第3步
步骤: 步骤3
描述: 加入3g盐
方法: 调味
工具: 锅
时间: 5秒

### 第4步
步骤: 步骤4
描述: （可选）加入3ml蚝油
方法: 调味
工具: 锅
时间: 5秒

### 第5步
步骤: 步骤5
描述: 加入2ml食用油
方法: 调味
工具: 锅
时间: 5秒

### 第6步
步骤: 步骤6
描述: 下菜，翻拌一下，然后盖上锅盖焖1分钟
方法: 焖,翻拌
工具: 锅,锅铲
时间: 1分钟

### 第7步
步骤: 步骤7
描述: 盛盘
方法: 装盘
工具: 锅铲
时间: 10秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 素菜 (Category)
- OUT BELONGS_TO 素菜 (RecipeCategory)
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201004196, chunk_id=201004196_chunk_833, recipe_name=肉蛋盖饭, category=主食, score=0.6552407741546631, search_type=vector_enhanced

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

### result_order=11
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

### result_order=12
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

### result_order=13
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

### result_order=14
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

### result_order=15
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

### result_order=19
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

### result_order=20
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

### result_order=21
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

### result_order=22
source: reranked_results
metadata_summary: node_id=201001855, recipe_name=胡萝卜, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 胡萝卜
食材名称: 胡萝卜
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=23
source: reranked_results
metadata_summary: node_id=201003831, recipe_name=豌豆, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 豌豆
食材名称: 豌豆
类别: 蔬菜
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蔬菜 (Category)
```

### result_order=24
source: reranked_results
metadata_summary: node_id=201000579, recipe_name=火腿, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 火腿
食材名称: 火腿
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

### result_order=25
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

### result_order=26
source: reranked_results
metadata_summary: node_id=201003785, recipe_name=虾仁, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 虾仁
食材名称: 虾仁
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
```

## Hybrid Retrieval / Top-K Final Retrieval Context
### result_order=0
source: top_k_final
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_892, recipe_name=扬州炒饭, category=主食, score=0.7249600887298584, search_type=vector_enhanced

```text
# 扬州炒饭

菜系: 苏菜
难度: 4.0星

时间信息: 准备时间: 约15分钟（切丁、打蛋、焯水）, 烹饪时间: 约10分钟（炒制）
份量: 1-2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6669681072235107, search_type=vector_enhanced

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

### result_order=2
source: top_k_final
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1173, recipe_name=炒/煎, category=烹饪技巧, score=0.6780569553375244, search_type=vector_enhanced

```text
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_29af79a321e3, recipe_name=炒/煎, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 炒/煎
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
```

### result_order=4
source: top_k_final
metadata_summary: node_id=201003571, chunk_id=201003571_chunk_701, recipe_name=牛油火锅底料, category=半成品, score=0.6530097723007202, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅置旺火，放入牛油烧至八成热（240±10°C），加入老姜100g、大葱100g、洋葱100g、大蒜100g炸干吸尽牛油腥味后捞出扔掉。
方法: 炸
工具: 锅
时间: 约2-3分钟

### 第2步
步骤: 步骤2
描述: 加入色拉油或菜籽油1000ml、纯猪油500g，待油温降至五成热（150±10°C）时放入糍粑辣椒3000g，持续翻炒5-8分钟。
方法: 炒
工具: 锅
时间: 5-8分钟

### 第3步
步骤: 步骤3
描述: 加入郫县豆瓣1000g炒散，转中小火慢炒至料渣略发白翻砂并发出沙沙声。
方法: 炒
工具: 锅
时间: 约10-15分钟

### 第4步
步骤: 步骤4
描述: 当油呈樱桃红色时，加入姜片150g、大蒜100g炒香约15秒。
方法: 炒
工具: 锅
时间: 15秒

### 第5步
步骤: 步骤5
描述: 加入剁碎的永川豆鼓10g、豆母子140g炒香，再加入红花椒150g、小茴香10g炒香。
方法: 炒
工具: 锅
时间: 约1-2分钟

### 第6步
步骤: 步骤6
描述: 放入颗粒香料100g（已打碎至4mm颗粒）继续炒香。
方法: 炒
工具: 锅
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入麦芽粉12.5g炒散，再沿锅边淋入52%VOL白酒150ml炒散。
方法: 炒
工具: 锅
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 作为底料：起锅装入容器，置于10-20°C环境静置5天后使用风味最佳。
方法: 静置
工具: 容器
时间: 5天

### 第9步
步骤: 步骤9
描述: 作为老油：起锅后趁热加入干辣椒面15g搅匀，静置24小时。
方法: 静置
工具: 容器
时间: 24小时

### 第10步
步骤: 步骤10
描述: 将底料倒入锅中，加入3/5开水（底料:开水=2:3），大火烧开并撇去浮沫。
方法: 煮
工具: 锅
时间: 约5分钟

### 第11步
步骤: 步骤11
描述: 转中小火慢熬25-30分钟出味后过滤去渣。
方法: 熬,过滤
工具: 锅,滤网
时间: 25-30分钟

### 第12步
步骤: 步骤12
描述: 静置待油水分离，将表面油脂撇出，重新倒入净锅炼干水分，起锅装容器即为火锅老油。
方法: 撇油,炼干
工具: 锅,容器
时间: 约10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=201004478, chunk_id=201004478_chunk_892, recipe_name=扬州炒饭, category=主食, score=0.7249600887298584, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
# 扬州炒饭

菜系: 苏菜
难度: 4.0星

时间信息: 准备时间: 约15分钟（切丁、打蛋、焯水）, 烹饪时间: 约10分钟（炒制）
份量: 1-2人

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=1
source: generation_context
metadata_summary: node_id=201004282, chunk_id=201004282_chunk_849, recipe_name=蛋炒饭, category=主食, score=0.6669681072235107, search_type=vector_enhanced, route_strategy=hybrid_traditional

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

### result_order=2
source: generation_context
metadata_summary: node_id=tipdoc_29af79a321e3, chunk_id=tipdoc_29af79a321e3_chunk_1173, recipe_name=炒/煎, category=烹饪技巧, score=0.6780569553375244, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 流程
### 流程

开火——直接将锅平放于火上，烧热——将油倒入锅中，烧热——放入菜品，翻炒——出锅前记得放调料

关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 炒/煎 / 器具 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_29af79a321e3, recipe_name=炒/煎, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 炒/煎
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
```

### result_order=4
source: generation_context
metadata_summary: node_id=201003571, chunk_id=201003571_chunk_701, recipe_name=牛油火锅底料, category=半成品, score=0.6530097723007202, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 锅置旺火，放入牛油烧至八成热（240±10°C），加入老姜100g、大葱100g、洋葱100g、大蒜100g炸干吸尽牛油腥味后捞出扔掉。
方法: 炸
工具: 锅
时间: 约2-3分钟

### 第2步
步骤: 步骤2
描述: 加入色拉油或菜籽油1000ml、纯猪油500g，待油温降至五成热（150±10°C）时放入糍粑辣椒3000g，持续翻炒5-8分钟。
方法: 炒
工具: 锅
时间: 5-8分钟

### 第3步
步骤: 步骤3
描述: 加入郫县豆瓣1000g炒散，转中小火慢炒至料渣略发白翻砂并发出沙沙声。
方法: 炒
工具: 锅
时间: 约10-15分钟

### 第4步
步骤: 步骤4
描述: 当油呈樱桃红色时，加入姜片150g、大蒜100g炒香约15秒。
方法: 炒
工具: 锅
时间: 15秒

### 第5步
步骤: 步骤5
描述: 加入剁碎的永川豆鼓10g、豆母子140g炒香，再加入红花椒150g、小茴香10g炒香。
方法: 炒
工具: 锅
时间: 约1-2分钟

### 第6步
步骤: 步骤6
描述: 放入颗粒香料100g（已打碎至4mm颗粒）继续炒香。
方法: 炒
工具: 锅
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入麦芽粉12.5g炒散，再沿锅边淋入52%VOL白酒150ml炒散。
方法: 炒
工具: 锅
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 作为底料：起锅装入容器，置于10-20°C环境静置5天后使用风味最佳。
方法: 静置
工具: 容器
时间: 5天

### 第9步
步骤: 步骤9
描述: 作为老油：起锅后趁热加入干辣椒面15g搅匀，静置24小时。
方法: 静置
工具: 容器
时间: 24小时

### 第10步
步骤: 步骤10
描述: 将底料倒入锅中，加入3/5开水（底料:开水=2:3），大火烧开并撇去浮沫。
方法: 煮
工具: 锅
时间: 约5分钟

### 第11步
步骤: 步骤11
描述: 转中小火慢熬25-30分钟出味后过滤去渣。
方法: 熬,过滤
工具: 锅,滤网
时间: 25-30分钟

### 第12步
步骤: 步骤12
描述: 静置待油水分离，将表面油脂撇出，重新倒入净锅炼干水分，起锅装容器即为火锅老油。
方法: 撇油,炼干
工具: 锅,容器
时间: 约10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 半成品 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

