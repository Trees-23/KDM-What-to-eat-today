# Recall Content

audit_id: 20260811_172847_741_6669bc1b
## Hybrid Retrieval / Entity Branch Raw Results
### result_order=0
source: entity_level
metadata_summary: node_id=201004679, recipe_name=鸡肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡肉
食材名称: 鸡肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
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
metadata_summary: node_id=201002255, chunk_id=201002255_chunk_465, recipe_name=口水鸡, category=荤菜, score=0.6093879342079163, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，1颗小葱切段，15颗花椒备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鸡肉洗净，放入锅中，加清水没过鸡肉，放入姜片、葱段和花椒，大火烧开
方法: 煮
工具: 锅
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 水开后转中小火煮20分钟，关火
方法: 煮
工具: 锅
时间: 20分钟

### 第4步
步骤: 步骤4
描述: 取出鸡肉，放入冰水中迅速冷却至冰凉
方法: 冷却
工具: 盆,冰水
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 取出鸡肉，切块摆盘备用
方法: 切
工具: 刀,案板,盘子
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 小火将锅烧热，倒入花生，烘烤至表皮爆裂，注意翻动防糊
方法: 炒,烘烤
工具: 锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 一颗葱切段，蒜拍末，花椒15颗，花生去皮后切碎
方法: 切,拍
工具: 刀,案板
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 锅内倒油烧热，放入葱段、花椒和一半蒜末炒香
方法: 炒
工具: 锅,锅铲
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 油温升至8成热后关火，滤出热油
方法: 炸,过滤
工具: 锅,滤网,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 将热油倒入盛辣椒粉的碗中，搅拌并滤出红油
方法: 炸,搅拌,过滤
工具: 碗,筷子,滤网
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 在红油中加入剩余蒜末、生抽、醋、盐、味精、糖、香油、花椒粉，拌匀放凉
方法: 搅拌
工具: 碗,筷子
时间: 2分钟

### 第12步
步骤: 步骤12
描述: 鸡肉上撒花生碎，淋红油，撒香菜即成
方法: 淋,撒
工具: 勺子,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=1
source: vector_enhanced
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_533, recipe_name=新疆大盘鸡, category=荤菜, score=0.6050660014152527, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鸡腿肉剁成块状，用清水加盐浸泡5分钟去除血水与腥味，然后沥干备用。
方法: 切,浸泡
工具: 刀,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 葱、蒜、干线椒、土豆等洗净；土豆削皮。
方法: 清洗,削皮
工具: 刀,案板
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 葱白切成长约4cm的段；菜椒、甜椒切块；土豆切成4cm×4cm滚刀块。
方法: 切
工具: 刀,案板
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 锅中倒入油，加入白砂糖，小火炒糖色至焦黄色，立即倒入沥干鸡肉翻炒上色。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 加入花椒、香叶、香果、干线椒等香料继续翻炒出香味。
方法: 炒
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入5g盐、7ml生抽、10g蚝油、100g料酒（或啤酒）和1升清水，中火煮沸后转小火慢炖。
方法: 炖
工具: 锅铲
时间: 20分钟

### 第7步
步骤: 步骤7
描述: 汤汁收至鸡肉即将露出时，将土豆块铺在表面，不翻动，盖盖继续炖。
方法: 炖
工具: 锅盖
时间: 10分钟

### 第8步
步骤: 步骤8
描述: 加入大葱段、菜椒和甜椒块，继续炖至汤汁浓稠，最后翻面让土豆吸汁，关火盛出。
方法: 炖,收汁
工具: 锅铲
时间: 5-10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=2
source: vector_enhanced
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_441, recipe_name=黄焖鸡, category=荤菜, score=0.5997363328933716, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡腿洗净，剁成4cm大小的块
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生姜切片、干辣椒切成小圈
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 香菇切片，青椒切成细长的马蹄状；若为干香菇，洗净灰尘后泡一晚上并留香菇水备用
方法: 切,泡发
工具: 刀,案板,盆

### 第4步
步骤: 步骤4
描述: 若有土豆，切为与鸡肉大小类似的滚刀块
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 炒糖色：锅里倒入底油，冷油时放入白糖；小火慢慢加热，待糖融化并变成较深的棕色，期间不断搅拌
方法: 炒
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第6步
步骤: 步骤6
描述: 迅速倒入鸡块，转大火快速翻炒，烹入料酒继续翻炒片刻
方法: 炒
工具: 炒锅,锅铲
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入生姜片和干辣椒炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 放入酱油炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 倒入香菇水或清水，以能淹住鸡肉为准
方法: 倒
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 加入香菇片、白胡椒粉、盐、土豆，翻炒均匀后盖上锅盖焖煮，转中小火15-20分钟，可转至砂锅
方法: 炒,焖
工具: 炒锅/砂锅,锅盖
时间: 15-20分钟

### 第11步
步骤: 步骤11
描述: 鸡肉软烂、汤汁浓稠后放入青椒，加入味精兜炒均匀，青椒断生即可关火
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=3
source: vector_enhanced
metadata_summary: node_id=tipdoc_e5959b9d0464, chunk_id=tipdoc_e5959b9d0464_chunk_1299, recipe_name=腌（肉）, category=烹饪技巧, score=0.5783764719963074, search_type=vector_enhanced

```text
## 菜品实战示例

- 洋葱炒牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑，需炒制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 白砂糖 2.5-10g（约 1-4 茶匙，根据口味甜度选择）
 - 孜然粉 5g（约 2 茶匙）
 - 生粉 10-15g（约 1 小把）
 - 油 10ml（约 2 汤匙）
 - （可选）十三香 1g（约 0.5 茶匙）
 - （可选）黑胡椒粉 1g（约 0.5 茶匙）

- 蚝油牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑且上浆感足，此菜口感偏甜，需炒制
 - 生抽 5ml（约 1 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 蚝油 10-20ml（约 2-4 汤匙，根据口味咸度选择，蚝油比较咸）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 生粉 25-35g（约 1 大把）
 - 油 10ml（约 2 汤匙）

- 五香盐酥鸡：以一人份的 150g 鸡胸肉为例。鸡肉应切成骰子形状，需炸制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 五香粉 5g（约 2 茶匙）或十三香 2.5-5g（约 1-2 茶匙）
 - （可选）孜然粉 1g（约 0.5 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）

- 蜜汁烤鸡翅：以一人份的 250g 带骨鸡翅中为例。鸡翅上应切几道花刀，成菜咸甜，但突出甜口，需烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 蜂蜜/糖浆 10-20ml（约 2-4 汤匙，根据口味甜度选择。如白砂糖超过或等于 10g，建议只加入 10ml）
 - （可选）五香粉 2.5g（约 1 茶匙。不可用十三香）

- 香烤三文鱼：以一人份的 200g 去骨三文鱼排为例。鱼肉不应改刀，需烤箱烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 红糖 10-20g（约 4-8 茶匙，根据口味甜度选择）
 - 意大利黑醋/镇江香醋 2.5-5ml（约 0.5-1 汤匙，根据口味酸度选择）
 - 肉豆蔻粉 2.5g（约 1 茶匙）
 - 百里香粉 1g（约 0.5 茶匙）
 - 姜粉 1g（约 0.5 茶匙）
 - 迷迭香粉 1-2g（约 0.5-1 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）
 - （可选）干辣椒碎 2.5-10g（约 1-4 茶匙，根据口味辣度选择）
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 腌（肉） / 腌渍基本概念 (TechniqueChunk): category: 烹饪技巧
```

### result_order=4
source: vector_enhanced
metadata_summary: node_id=201002203, chunk_id=201002203_chunk_457, recipe_name=凉拌鸡丝, category=荤菜, score=0.5776276588439941, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 锅中倒入4升水
工具: 锅

### 第3步
步骤: 步骤3
描述: 加入鸡胸肉、姜片
方法: 加
工具: 锅

### 第4步
步骤: 步骤4
描述: 倒入20毫升料酒
方法: 加
工具: 锅

### 第5步
步骤: 步骤5
描述: 开大火不盖盖将水烧开
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 水开后转中火，用勺子将浮沫捞出
方法: 煮,捞
工具: 锅,勺子

### 第7步
步骤: 步骤7
描述: 继续煮5-7分钟，如果是非冷冻肉煮5分钟，冷冻肉煮7分钟；用筷子插入鸡胸肉，如果能轻松插入，代表鸡肉熟了，否则延长煮制时间
方法: 煮
工具: 锅,筷子
时间: 5-7分钟

### 第8步
步骤: 步骤8
描述: 用凉白开水冲泡鸡胸肉，使鸡胸肉降至室温
方法: 冲
工具: 盆

### 第9步
步骤: 步骤9
描述: 顺着鸡胸肉纹理将鸡胸肉撕成细丝
方法: 撕
工具: 手

### 第10步
步骤: 步骤10
描述: 准备一个碗，碗中加入准备好的麻油、生抽、香醋、白糖、盐，搅拌料汁，使糖和盐尽量溶化
方法: 搅拌
工具: 碗,筷子

### 第11步
步骤: 步骤11
描述: 将料汁倒入鸡丝中，搅拌均匀
方法: 拌
工具: 碗,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=5
source: vector_enhanced
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.575760543346405, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=6
source: vector_enhanced
metadata_summary: node_id=201004172, chunk_id=201004172_chunk_827, recipe_name=煮泡面加蛋, category=主食, score=0.5717189908027649, search_type=vector_enhanced

```text
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=7
source: vector_enhanced
metadata_summary: node_id=201003707, chunk_id=201003707_chunk_725, recipe_name=生汆丸子汤, category=汤类, score=0.5707718729972839, search_type=vector_enhanced

```text
## 所需食材
1. 前腿肉(500克)
2. 土豆淀粉(40克)
3. 小香葱
4. 木耳
5. 熟豆油
6. 盐(30克)
7. 粉丝
8. 胡椒粉(10克)
9. 葱姜花椒水(400克)
10. 香油(3滴)
11. 香菜(1小颗)
12. 鸡粉
13. 鸡蛋清(1个)
14. 黄花

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=8
source: vector_enhanced
metadata_summary: node_id=201002434, chunk_id=201002434_chunk_496, recipe_name=姜葱捞鸡, category=荤菜, score=0.5661523938179016, search_type=vector_enhanced

```text
## 所需食材
1. 姜(50克)
2. 油(35毫升)
3. 盐(5克)
4. 盐焗鸡粉(5克)
5. 糖(5克)
6. 葱(1根)
7. 鸡腿(400克)
8. 鸡腿(4个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=9
source: vector_enhanced
metadata_summary: node_id=201001526, chunk_id=201001526_chunk_333, recipe_name=商芝肉, category=荤菜, score=0.5612736344337463, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将肉刮洗干净，入煮锅煮至六成熟（变色为白），捞出趁热用蜂蜜、醋涂抹肉皮。
方法: 煮,涂抹
工具: 煮锅,刷子或勺子
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅内放入熟猪油，用旺火烧至八成熟（约200度，油表有大量青烟，油状平静），将肉块皮朝下投入，炸至呈金红色时，捞入凉肉煮锅中泡软。
方法: 炸
工具: 炒锅,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 将肉放在案板上，切成10 cm长、0.6 cm厚的片，仍然皮朝下，整齐装入蒸碗内。
方法: 切
工具: 刀,案板,蒸碗
时间: 约5分钟

### 第4步
步骤: 步骤4
描述: 将5克大葱切成2.4 cm长的段，5克切成2.4 cm长的斜形片；姜去皮洗净，1.5克切成片，5克切成末；摊的鸡蛋皮切成2.4 cm长的等腰三角形片。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第5步
步骤: 步骤5
描述: 商芝入沸水锅中煮软捞出，去除老茎、杂质，淘洗干净，切成3 cm长的段，放入碗中，加酱油5克、精盐1克、熟猪油10克拌匀，盖在肉片上。
方法: 煮,拌
工具: 煮锅,碗,筷子
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 另将鸡汤100克放入一小碗中，加酱油5克、精盐0.5克、料酒15克搅匀，浇入蒸碗，再放入姜片、葱段、八角，上笼用旺火蒸约半小时后，转用小火继续蒸约一小时三十分钟。
方法: 蒸
工具: 蒸锅,小碗
时间: 2小时

### 第7步
步骤: 步骤7
描述: 熟烂后取出，拣去姜、葱、八角，倒、过滤原汁，将肉扣入汤盘。
方法: 过滤,扣盘
工具: 滤网,汤盘
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 炒锅内放入鸡汤100克，加入原汁，用旺火烧沸，下入姜末、葱片、味精后搅匀，投入摊鸡蛋皮，淋芝麻油，浇入汤盘即成。
方法: 烧,淋
工具: 炒锅,汤勺
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Branches Before Merge
### result_order=0
source: branch_grouped
metadata_summary: node_id=201004679, recipe_name=鸡肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡肉
食材名称: 鸡肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
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
metadata_summary: node_id=201002255, chunk_id=201002255_chunk_465, recipe_name=口水鸡, category=荤菜, score=0.6093879342079163, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，1颗小葱切段，15颗花椒备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鸡肉洗净，放入锅中，加清水没过鸡肉，放入姜片、葱段和花椒，大火烧开
方法: 煮
工具: 锅
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 水开后转中小火煮20分钟，关火
方法: 煮
工具: 锅
时间: 20分钟

### 第4步
步骤: 步骤4
描述: 取出鸡肉，放入冰水中迅速冷却至冰凉
方法: 冷却
工具: 盆,冰水
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 取出鸡肉，切块摆盘备用
方法: 切
工具: 刀,案板,盘子
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 小火将锅烧热，倒入花生，烘烤至表皮爆裂，注意翻动防糊
方法: 炒,烘烤
工具: 锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 一颗葱切段，蒜拍末，花椒15颗，花生去皮后切碎
方法: 切,拍
工具: 刀,案板
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 锅内倒油烧热，放入葱段、花椒和一半蒜末炒香
方法: 炒
工具: 锅,锅铲
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 油温升至8成热后关火，滤出热油
方法: 炸,过滤
工具: 锅,滤网,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 将热油倒入盛辣椒粉的碗中，搅拌并滤出红油
方法: 炸,搅拌,过滤
工具: 碗,筷子,滤网
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 在红油中加入剩余蒜末、生抽、醋、盐、味精、糖、香油、花椒粉，拌匀放凉
方法: 搅拌
工具: 碗,筷子
时间: 2分钟

### 第12步
步骤: 步骤12
描述: 鸡肉上撒花生碎，淋红油，撒香菜即成
方法: 淋,撒
工具: 勺子,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: branch_grouped
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_533, recipe_name=新疆大盘鸡, category=荤菜, score=0.6050660014152527, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鸡腿肉剁成块状，用清水加盐浸泡5分钟去除血水与腥味，然后沥干备用。
方法: 切,浸泡
工具: 刀,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 葱、蒜、干线椒、土豆等洗净；土豆削皮。
方法: 清洗,削皮
工具: 刀,案板
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 葱白切成长约4cm的段；菜椒、甜椒切块；土豆切成4cm×4cm滚刀块。
方法: 切
工具: 刀,案板
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 锅中倒入油，加入白砂糖，小火炒糖色至焦黄色，立即倒入沥干鸡肉翻炒上色。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 加入花椒、香叶、香果、干线椒等香料继续翻炒出香味。
方法: 炒
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入5g盐、7ml生抽、10g蚝油、100g料酒（或啤酒）和1升清水，中火煮沸后转小火慢炖。
方法: 炖
工具: 锅铲
时间: 20分钟

### 第7步
步骤: 步骤7
描述: 汤汁收至鸡肉即将露出时，将土豆块铺在表面，不翻动，盖盖继续炖。
方法: 炖
工具: 锅盖
时间: 10分钟

### 第8步
步骤: 步骤8
描述: 加入大葱段、菜椒和甜椒块，继续炖至汤汁浓稠，最后翻面让土豆吸汁，关火盛出。
方法: 炖,收汁
工具: 锅铲
时间: 5-10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: branch_grouped
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_441, recipe_name=黄焖鸡, category=荤菜, score=0.5997363328933716, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡腿洗净，剁成4cm大小的块
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生姜切片、干辣椒切成小圈
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 香菇切片，青椒切成细长的马蹄状；若为干香菇，洗净灰尘后泡一晚上并留香菇水备用
方法: 切,泡发
工具: 刀,案板,盆

### 第4步
步骤: 步骤4
描述: 若有土豆，切为与鸡肉大小类似的滚刀块
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 炒糖色：锅里倒入底油，冷油时放入白糖；小火慢慢加热，待糖融化并变成较深的棕色，期间不断搅拌
方法: 炒
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第6步
步骤: 步骤6
描述: 迅速倒入鸡块，转大火快速翻炒，烹入料酒继续翻炒片刻
方法: 炒
工具: 炒锅,锅铲
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入生姜片和干辣椒炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 放入酱油炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 倒入香菇水或清水，以能淹住鸡肉为准
方法: 倒
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 加入香菇片、白胡椒粉、盐、土豆，翻炒均匀后盖上锅盖焖煮，转中小火15-20分钟，可转至砂锅
方法: 炒,焖
工具: 炒锅/砂锅,锅盖
时间: 15-20分钟

### 第11步
步骤: 步骤11
描述: 鸡肉软烂、汤汁浓稠后放入青椒，加入味精兜炒均匀，青椒断生即可关火
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
source: branch_grouped
metadata_summary: node_id=tipdoc_e5959b9d0464, chunk_id=tipdoc_e5959b9d0464_chunk_1299, recipe_name=腌（肉）, category=烹饪技巧, score=0.5783764719963074, search_type=vector_enhanced

```text
## 菜品实战示例

- 洋葱炒牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑，需炒制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 白砂糖 2.5-10g（约 1-4 茶匙，根据口味甜度选择）
 - 孜然粉 5g（约 2 茶匙）
 - 生粉 10-15g（约 1 小把）
 - 油 10ml（约 2 汤匙）
 - （可选）十三香 1g（约 0.5 茶匙）
 - （可选）黑胡椒粉 1g（约 0.5 茶匙）

- 蚝油牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑且上浆感足，此菜口感偏甜，需炒制
 - 生抽 5ml（约 1 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 蚝油 10-20ml（约 2-4 汤匙，根据口味咸度选择，蚝油比较咸）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 生粉 25-35g（约 1 大把）
 - 油 10ml（约 2 汤匙）

- 五香盐酥鸡：以一人份的 150g 鸡胸肉为例。鸡肉应切成骰子形状，需炸制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 五香粉 5g（约 2 茶匙）或十三香 2.5-5g（约 1-2 茶匙）
 - （可选）孜然粉 1g（约 0.5 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）

- 蜜汁烤鸡翅：以一人份的 250g 带骨鸡翅中为例。鸡翅上应切几道花刀，成菜咸甜，但突出甜口，需烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 蜂蜜/糖浆 10-20ml（约 2-4 汤匙，根据口味甜度选择。如白砂糖超过或等于 10g，建议只加入 10ml）
 - （可选）五香粉 2.5g（约 1 茶匙。不可用十三香）

- 香烤三文鱼：以一人份的 200g 去骨三文鱼排为例。鱼肉不应改刀，需烤箱烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 红糖 10-20g（约 4-8 茶匙，根据口味甜度选择）
 - 意大利黑醋/镇江香醋 2.5-5ml（约 0.5-1 汤匙，根据口味酸度选择）
 - 肉豆蔻粉 2.5g（约 1 茶匙）
 - 百里香粉 1g（约 0.5 茶匙）
 - 姜粉 1g（约 0.5 茶匙）
 - 迷迭香粉 1-2g（约 0.5-1 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）
 - （可选）干辣椒碎 2.5-10g（约 1-4 茶匙，根据口味辣度选择）
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 腌（肉） / 腌渍基本概念 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
source: branch_grouped
metadata_summary: node_id=201002203, chunk_id=201002203_chunk_457, recipe_name=凉拌鸡丝, category=荤菜, score=0.5776276588439941, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 锅中倒入4升水
工具: 锅

### 第3步
步骤: 步骤3
描述: 加入鸡胸肉、姜片
方法: 加
工具: 锅

### 第4步
步骤: 步骤4
描述: 倒入20毫升料酒
方法: 加
工具: 锅

### 第5步
步骤: 步骤5
描述: 开大火不盖盖将水烧开
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 水开后转中火，用勺子将浮沫捞出
方法: 煮,捞
工具: 锅,勺子

### 第7步
步骤: 步骤7
描述: 继续煮5-7分钟，如果是非冷冻肉煮5分钟，冷冻肉煮7分钟；用筷子插入鸡胸肉，如果能轻松插入，代表鸡肉熟了，否则延长煮制时间
方法: 煮
工具: 锅,筷子
时间: 5-7分钟

### 第8步
步骤: 步骤8
描述: 用凉白开水冲泡鸡胸肉，使鸡胸肉降至室温
方法: 冲
工具: 盆

### 第9步
步骤: 步骤9
描述: 顺着鸡胸肉纹理将鸡胸肉撕成细丝
方法: 撕
工具: 手

### 第10步
步骤: 步骤10
描述: 准备一个碗，碗中加入准备好的麻油、生抽、香醋、白糖、盐，搅拌料汁，使糖和盐尽量溶化
方法: 搅拌
工具: 碗,筷子

### 第11步
步骤: 步骤11
描述: 将料汁倒入鸡丝中，搅拌均匀
方法: 拌
工具: 碗,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: branch_grouped
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.575760543346405, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=9
source: branch_grouped
metadata_summary: node_id=201004172, chunk_id=201004172_chunk_827, recipe_name=煮泡面加蛋, category=主食, score=0.5717189908027649, search_type=vector_enhanced

```text
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=10
source: branch_grouped
metadata_summary: node_id=201003707, chunk_id=201003707_chunk_725, recipe_name=生汆丸子汤, category=汤类, score=0.5707718729972839, search_type=vector_enhanced

```text
## 所需食材
1. 前腿肉(500克)
2. 土豆淀粉(40克)
3. 小香葱
4. 木耳
5. 熟豆油
6. 盐(30克)
7. 粉丝
8. 胡椒粉(10克)
9. 葱姜花椒水(400克)
10. 香油(3滴)
11. 香菜(1小颗)
12. 鸡粉
13. 鸡蛋清(1个)
14. 黄花

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=11
source: branch_grouped
metadata_summary: node_id=201002434, chunk_id=201002434_chunk_496, recipe_name=姜葱捞鸡, category=荤菜, score=0.5661523938179016, search_type=vector_enhanced

```text
## 所需食材
1. 姜(50克)
2. 油(35毫升)
3. 盐(5克)
4. 盐焗鸡粉(5克)
5. 糖(5克)
6. 葱(1根)
7. 鸡腿(400克)
8. 鸡腿(4个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=12
source: branch_grouped
metadata_summary: node_id=201001526, chunk_id=201001526_chunk_333, recipe_name=商芝肉, category=荤菜, score=0.5612736344337463, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将肉刮洗干净，入煮锅煮至六成熟（变色为白），捞出趁热用蜂蜜、醋涂抹肉皮。
方法: 煮,涂抹
工具: 煮锅,刷子或勺子
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅内放入熟猪油，用旺火烧至八成熟（约200度，油表有大量青烟，油状平静），将肉块皮朝下投入，炸至呈金红色时，捞入凉肉煮锅中泡软。
方法: 炸
工具: 炒锅,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 将肉放在案板上，切成10 cm长、0.6 cm厚的片，仍然皮朝下，整齐装入蒸碗内。
方法: 切
工具: 刀,案板,蒸碗
时间: 约5分钟

### 第4步
步骤: 步骤4
描述: 将5克大葱切成2.4 cm长的段，5克切成2.4 cm长的斜形片；姜去皮洗净，1.5克切成片，5克切成末；摊的鸡蛋皮切成2.4 cm长的等腰三角形片。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第5步
步骤: 步骤5
描述: 商芝入沸水锅中煮软捞出，去除老茎、杂质，淘洗干净，切成3 cm长的段，放入碗中，加酱油5克、精盐1克、熟猪油10克拌匀，盖在肉片上。
方法: 煮,拌
工具: 煮锅,碗,筷子
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 另将鸡汤100克放入一小碗中，加酱油5克、精盐0.5克、料酒15克搅匀，浇入蒸碗，再放入姜片、葱段、八角，上笼用旺火蒸约半小时后，转用小火继续蒸约一小时三十分钟。
方法: 蒸
工具: 蒸锅,小碗
时间: 2小时

### 第7步
步骤: 步骤7
描述: 熟烂后取出，拣去姜、葱、八角，倒、过滤原汁，将肉扣入汤盘。
方法: 过滤,扣盘
工具: 滤网,汤盘
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 炒锅内放入鸡汤100克，加入原汁，用旺火烧沸，下入姜末、葱片、味精后搅匀，投入摊鸡蛋皮，淋芝麻油，浇入汤盘即成。
方法: 烧,淋
工具: 炒锅,汤勺
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Merged Candidates
### result_order=0
source: merged_candidates
metadata_summary: node_id=201004679, recipe_name=鸡肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡肉
食材名称: 鸡肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
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
metadata_summary: node_id=201002255, chunk_id=201002255_chunk_465, recipe_name=口水鸡, category=荤菜, score=0.6093879342079163, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，1颗小葱切段，15颗花椒备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鸡肉洗净，放入锅中，加清水没过鸡肉，放入姜片、葱段和花椒，大火烧开
方法: 煮
工具: 锅
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 水开后转中小火煮20分钟，关火
方法: 煮
工具: 锅
时间: 20分钟

### 第4步
步骤: 步骤4
描述: 取出鸡肉，放入冰水中迅速冷却至冰凉
方法: 冷却
工具: 盆,冰水
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 取出鸡肉，切块摆盘备用
方法: 切
工具: 刀,案板,盘子
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 小火将锅烧热，倒入花生，烘烤至表皮爆裂，注意翻动防糊
方法: 炒,烘烤
工具: 锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 一颗葱切段，蒜拍末，花椒15颗，花生去皮后切碎
方法: 切,拍
工具: 刀,案板
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 锅内倒油烧热，放入葱段、花椒和一半蒜末炒香
方法: 炒
工具: 锅,锅铲
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 油温升至8成热后关火，滤出热油
方法: 炸,过滤
工具: 锅,滤网,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 将热油倒入盛辣椒粉的碗中，搅拌并滤出红油
方法: 炸,搅拌,过滤
工具: 碗,筷子,滤网
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 在红油中加入剩余蒜末、生抽、醋、盐、味精、糖、香油、花椒粉，拌匀放凉
方法: 搅拌
工具: 碗,筷子
时间: 2分钟

### 第12步
步骤: 步骤12
描述: 鸡肉上撒花生碎，淋红油，撒香菜即成
方法: 淋,撒
工具: 勺子,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: merged_candidates
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_533, recipe_name=新疆大盘鸡, category=荤菜, score=0.6050660014152527, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鸡腿肉剁成块状，用清水加盐浸泡5分钟去除血水与腥味，然后沥干备用。
方法: 切,浸泡
工具: 刀,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 葱、蒜、干线椒、土豆等洗净；土豆削皮。
方法: 清洗,削皮
工具: 刀,案板
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 葱白切成长约4cm的段；菜椒、甜椒切块；土豆切成4cm×4cm滚刀块。
方法: 切
工具: 刀,案板
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 锅中倒入油，加入白砂糖，小火炒糖色至焦黄色，立即倒入沥干鸡肉翻炒上色。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 加入花椒、香叶、香果、干线椒等香料继续翻炒出香味。
方法: 炒
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入5g盐、7ml生抽、10g蚝油、100g料酒（或啤酒）和1升清水，中火煮沸后转小火慢炖。
方法: 炖
工具: 锅铲
时间: 20分钟

### 第7步
步骤: 步骤7
描述: 汤汁收至鸡肉即将露出时，将土豆块铺在表面，不翻动，盖盖继续炖。
方法: 炖
工具: 锅盖
时间: 10分钟

### 第8步
步骤: 步骤8
描述: 加入大葱段、菜椒和甜椒块，继续炖至汤汁浓稠，最后翻面让土豆吸汁，关火盛出。
方法: 炖,收汁
工具: 锅铲
时间: 5-10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=5
source: merged_candidates
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_441, recipe_name=黄焖鸡, category=荤菜, score=0.5997363328933716, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡腿洗净，剁成4cm大小的块
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生姜切片、干辣椒切成小圈
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 香菇切片，青椒切成细长的马蹄状；若为干香菇，洗净灰尘后泡一晚上并留香菇水备用
方法: 切,泡发
工具: 刀,案板,盆

### 第4步
步骤: 步骤4
描述: 若有土豆，切为与鸡肉大小类似的滚刀块
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 炒糖色：锅里倒入底油，冷油时放入白糖；小火慢慢加热，待糖融化并变成较深的棕色，期间不断搅拌
方法: 炒
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第6步
步骤: 步骤6
描述: 迅速倒入鸡块，转大火快速翻炒，烹入料酒继续翻炒片刻
方法: 炒
工具: 炒锅,锅铲
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入生姜片和干辣椒炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 放入酱油炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 倒入香菇水或清水，以能淹住鸡肉为准
方法: 倒
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 加入香菇片、白胡椒粉、盐、土豆，翻炒均匀后盖上锅盖焖煮，转中小火15-20分钟，可转至砂锅
方法: 炒,焖
工具: 炒锅/砂锅,锅盖
时间: 15-20分钟

### 第11步
步骤: 步骤11
描述: 鸡肉软烂、汤汁浓稠后放入青椒，加入味精兜炒均匀，青椒断生即可关火
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=6
source: merged_candidates
metadata_summary: node_id=tipdoc_e5959b9d0464, chunk_id=tipdoc_e5959b9d0464_chunk_1299, recipe_name=腌（肉）, category=烹饪技巧, score=0.5783764719963074, search_type=vector_enhanced

```text
## 菜品实战示例

- 洋葱炒牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑，需炒制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 白砂糖 2.5-10g（约 1-4 茶匙，根据口味甜度选择）
 - 孜然粉 5g（约 2 茶匙）
 - 生粉 10-15g（约 1 小把）
 - 油 10ml（约 2 汤匙）
 - （可选）十三香 1g（约 0.5 茶匙）
 - （可选）黑胡椒粉 1g（约 0.5 茶匙）

- 蚝油牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑且上浆感足，此菜口感偏甜，需炒制
 - 生抽 5ml（约 1 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 蚝油 10-20ml（约 2-4 汤匙，根据口味咸度选择，蚝油比较咸）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 生粉 25-35g（约 1 大把）
 - 油 10ml（约 2 汤匙）

- 五香盐酥鸡：以一人份的 150g 鸡胸肉为例。鸡肉应切成骰子形状，需炸制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 五香粉 5g（约 2 茶匙）或十三香 2.5-5g（约 1-2 茶匙）
 - （可选）孜然粉 1g（约 0.5 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）

- 蜜汁烤鸡翅：以一人份的 250g 带骨鸡翅中为例。鸡翅上应切几道花刀，成菜咸甜，但突出甜口，需烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 蜂蜜/糖浆 10-20ml（约 2-4 汤匙，根据口味甜度选择。如白砂糖超过或等于 10g，建议只加入 10ml）
 - （可选）五香粉 2.5g（约 1 茶匙。不可用十三香）

- 香烤三文鱼：以一人份的 200g 去骨三文鱼排为例。鱼肉不应改刀，需烤箱烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 红糖 10-20g（约 4-8 茶匙，根据口味甜度选择）
 - 意大利黑醋/镇江香醋 2.5-5ml（约 0.5-1 汤匙，根据口味酸度选择）
 - 肉豆蔻粉 2.5g（约 1 茶匙）
 - 百里香粉 1g（约 0.5 茶匙）
 - 姜粉 1g（约 0.5 茶匙）
 - 迷迭香粉 1-2g（约 0.5-1 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）
 - （可选）干辣椒碎 2.5-10g（约 1-4 茶匙，根据口味辣度选择）
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 腌（肉） / 腌渍基本概念 (TechniqueChunk): category: 烹饪技巧
```

### result_order=7
source: merged_candidates
metadata_summary: node_id=201002203, chunk_id=201002203_chunk_457, recipe_name=凉拌鸡丝, category=荤菜, score=0.5776276588439941, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 锅中倒入4升水
工具: 锅

### 第3步
步骤: 步骤3
描述: 加入鸡胸肉、姜片
方法: 加
工具: 锅

### 第4步
步骤: 步骤4
描述: 倒入20毫升料酒
方法: 加
工具: 锅

### 第5步
步骤: 步骤5
描述: 开大火不盖盖将水烧开
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 水开后转中火，用勺子将浮沫捞出
方法: 煮,捞
工具: 锅,勺子

### 第7步
步骤: 步骤7
描述: 继续煮5-7分钟，如果是非冷冻肉煮5分钟，冷冻肉煮7分钟；用筷子插入鸡胸肉，如果能轻松插入，代表鸡肉熟了，否则延长煮制时间
方法: 煮
工具: 锅,筷子
时间: 5-7分钟

### 第8步
步骤: 步骤8
描述: 用凉白开水冲泡鸡胸肉，使鸡胸肉降至室温
方法: 冲
工具: 盆

### 第9步
步骤: 步骤9
描述: 顺着鸡胸肉纹理将鸡胸肉撕成细丝
方法: 撕
工具: 手

### 第10步
步骤: 步骤10
描述: 准备一个碗，碗中加入准备好的麻油、生抽、香醋、白糖、盐，搅拌料汁，使糖和盐尽量溶化
方法: 搅拌
工具: 碗,筷子

### 第11步
步骤: 步骤11
描述: 将料汁倒入鸡丝中，搅拌均匀
方法: 拌
工具: 碗,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=8
source: merged_candidates
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.575760543346405, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=9
source: merged_candidates
metadata_summary: node_id=201004172, chunk_id=201004172_chunk_827, recipe_name=煮泡面加蛋, category=主食, score=0.5717189908027649, search_type=vector_enhanced

```text
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=10
source: merged_candidates
metadata_summary: node_id=201003707, chunk_id=201003707_chunk_725, recipe_name=生汆丸子汤, category=汤类, score=0.5707718729972839, search_type=vector_enhanced

```text
## 所需食材
1. 前腿肉(500克)
2. 土豆淀粉(40克)
3. 小香葱
4. 木耳
5. 熟豆油
6. 盐(30克)
7. 粉丝
8. 胡椒粉(10克)
9. 葱姜花椒水(400克)
10. 香油(3滴)
11. 香菜(1小颗)
12. 鸡粉
13. 鸡蛋清(1个)
14. 黄花

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=11
source: merged_candidates
metadata_summary: node_id=201002434, chunk_id=201002434_chunk_496, recipe_name=姜葱捞鸡, category=荤菜, score=0.5661523938179016, search_type=vector_enhanced

```text
## 所需食材
1. 姜(50克)
2. 油(35毫升)
3. 盐(5克)
4. 盐焗鸡粉(5克)
5. 糖(5克)
6. 葱(1根)
7. 鸡腿(400克)
8. 鸡腿(4个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=12
source: merged_candidates
metadata_summary: node_id=201001526, chunk_id=201001526_chunk_333, recipe_name=商芝肉, category=荤菜, score=0.5612736344337463, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将肉刮洗干净，入煮锅煮至六成熟（变色为白），捞出趁热用蜂蜜、醋涂抹肉皮。
方法: 煮,涂抹
工具: 煮锅,刷子或勺子
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅内放入熟猪油，用旺火烧至八成熟（约200度，油表有大量青烟，油状平静），将肉块皮朝下投入，炸至呈金红色时，捞入凉肉煮锅中泡软。
方法: 炸
工具: 炒锅,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 将肉放在案板上，切成10 cm长、0.6 cm厚的片，仍然皮朝下，整齐装入蒸碗内。
方法: 切
工具: 刀,案板,蒸碗
时间: 约5分钟

### 第4步
步骤: 步骤4
描述: 将5克大葱切成2.4 cm长的段，5克切成2.4 cm长的斜形片；姜去皮洗净，1.5克切成片，5克切成末；摊的鸡蛋皮切成2.4 cm长的等腰三角形片。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第5步
步骤: 步骤5
描述: 商芝入沸水锅中煮软捞出，去除老茎、杂质，淘洗干净，切成3 cm长的段，放入碗中，加酱油5克、精盐1克、熟猪油10克拌匀，盖在肉片上。
方法: 煮,拌
工具: 煮锅,碗,筷子
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 另将鸡汤100克放入一小碗中，加酱油5克、精盐0.5克、料酒15克搅匀，浇入蒸碗，再放入姜片、葱段、八角，上笼用旺火蒸约半小时后，转用小火继续蒸约一小时三十分钟。
方法: 蒸
工具: 蒸锅,小碗
时间: 2小时

### 第7步
步骤: 步骤7
描述: 熟烂后取出，拣去姜、葱、八角，倒、过滤原汁，将肉扣入汤盘。
方法: 过滤,扣盘
工具: 滤网,汤盘
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 炒锅内放入鸡汤100克，加入原汁，用旺火烧沸，下入姜末、葱片、味精后搅匀，投入摊鸡蛋皮，淋芝麻油，浇入汤盘即成。
方法: 烧,淋
工具: 炒锅,汤勺
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
```

## Hybrid Retrieval / Technique Expanded Context
### result_order=0
source: technique_expansion
metadata_summary: node_id=technique_expansion:tipdoc_e5959b9d0464,tipdoc_820d789ff48e, recipe_name=如何决策吃什么、腌（肉）, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么、腌（肉）
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
## 正文
# 腌（肉）
## 注意
## 注意

此处所描述的腌渍是食材烹饪前处理的步骤，并非制作咸肉或腌制香肠等成品
## 腌渍
## 腌渍

在烹饪前腌制肉类是让肉类预先入味的常用方法。一般腌渍的对象是生肉。根据菜品的需求，可以自行确定肉类改刀的大小。

 例如炸鸡米花，鸡胸肉是在改刀为骰子大小的小块后放入碗中腌渍
 例如烤全羊，羊腿，半扇或整扇羊肉不必改刀即可用大量调味料涂抹在表面从而腌渍入味

根据菜品的不同，腌渍所选的调味料、辅料可以是任何种类。有时候为了不同的口味，辅料也可能需要预先处理。
## 腌渍基本概念
## 腌渍基本概念

此处介绍的是正常口味的腌渍过程。

- 一般来说，肉量越大（比如一次性腌渍 5kg 鸡翅），体积越大（比如一整个羊腿），口味越重，则需要调味料和辅料越多
- 一般来说，计划腌渍的时间越长，使用的调味料和辅料越少
- 腌渍时应使用料均匀覆盖在所有的表面。如果是肉片、肉丝，应该用手尽量抓匀、搅匀。如果是整个羊腿，应该用手或刷子在表面刷匀
- 一般炒肉、炸肉需要提前腌渍。炒肉应该保证肉鲜嫩的口感，烹调往往需要大火且时间较短。短时间烹饪不容易入味时，提前腌渍就能弥补口味的不足
```

## Hybrid Retrieval / Rerank Input Texts
### pair_order=0
source: rerank_input

```text
命中关键词: 鸡肉
食材名称: 鸡肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
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
菜品: 口水鸡
菜系: 川菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，1颗小葱切段，15颗花椒备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鸡肉洗净，放入锅中，加清水没过鸡肉，放入姜片、葱段和花椒，大火烧开
方法: 煮
工具: 锅
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 水开后转中小火煮20分钟，关火
方法: 煮
工具: 锅
时间: 20分钟

### 第4步
步骤: 步骤4
描述: 取出鸡肉，放入冰水中迅速冷却至冰凉
方法: 冷却
工具: 盆,冰水
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 取出鸡肉，切块摆盘备用
方法: 切
工具: 刀,案板,盘子
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 小火将锅烧热，倒入花生，烘烤至表皮爆裂，注意翻动防糊
方法: 炒,烘烤
工具: 锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 一颗葱切段，蒜拍末，花椒15颗，花生去皮后切碎
方法: 切,拍
工具: 刀,案板
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 锅内倒油烧热，放入葱段、花椒和一半蒜末炒香
方法: 炒
工具: 锅,锅铲
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 油温升至8成热后关火，滤出热油
方法: 炸,过滤
工具: 锅,滤网,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 将热油倒入盛辣椒粉的碗中，搅拌并滤出红油
方法: 炸,搅拌,过滤
工具: 碗,筷子,滤网
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 在红油中加入剩余蒜末、生抽、醋、盐、味精、糖、香油、花椒粉，拌匀放凉
方法: 搅拌
工具: 碗,筷子
时间: 2分钟

### 第12步
步骤: 步骤12
描述: 鸡肉上撒花生碎，淋红油，撒香菜即成
方法: 淋,撒
工具: 勺子,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT 
```

### pair_order=4
source: rerank_input

```text
菜品: 新疆大盘鸡
菜系: 西北菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鸡腿肉剁成块状，用清水加盐浸泡5分钟去除血水与腥味，然后沥干备用。
方法: 切,浸泡
工具: 刀,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 葱、蒜、干线椒、土豆等洗净；土豆削皮。
方法: 清洗,削皮
工具: 刀,案板
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 葱白切成长约4cm的段；菜椒、甜椒切块；土豆切成4cm×4cm滚刀块。
方法: 切
工具: 刀,案板
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 锅中倒入油，加入白砂糖，小火炒糖色至焦黄色，立即倒入沥干鸡肉翻炒上色。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 加入花椒、香叶、香果、干线椒等香料继续翻炒出香味。
方法: 炒
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入5g盐、7ml生抽、10g蚝油、100g料酒（或啤酒）和1升清水，中火煮沸后转小火慢炖。
方法: 炖
工具: 锅铲
时间: 20分钟

### 第7步
步骤: 步骤7
描述: 汤汁收至鸡肉即将露出时，将土豆块铺在表面，不翻动，盖盖继续炖。
方法: 炖
工具: 锅盖
时间: 10分钟

### 第8步
步骤: 步骤8
描述: 加入大葱段、菜椒和甜椒块，继续炖至汤汁浓稠，最后翻面让土豆吸汁，关火盛出。
方法: 炖,收汁
工具: 锅铲
时间: 5-10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### pair_order=5
source: rerank_input

```text
菜品: 黄焖鸡
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡腿洗净，剁成4cm大小的块
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生姜切片、干辣椒切成小圈
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 香菇切片，青椒切成细长的马蹄状；若为干香菇，洗净灰尘后泡一晚上并留香菇水备用
方法: 切,泡发
工具: 刀,案板,盆

### 第4步
步骤: 步骤4
描述: 若有土豆，切为与鸡肉大小类似的滚刀块
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 炒糖色：锅里倒入底油，冷油时放入白糖；小火慢慢加热，待糖融化并变成较深的棕色，期间不断搅拌
方法: 炒
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第6步
步骤: 步骤6
描述: 迅速倒入鸡块，转大火快速翻炒，烹入料酒继续翻炒片刻
方法: 炒
工具: 炒锅,锅铲
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入生姜片和干辣椒炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 放入酱油炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 倒入香菇水或清水，以能淹住鸡肉为准
方法: 倒
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 加入香菇片、白胡椒粉、盐、土豆，翻炒均匀后盖上锅盖焖煮，转中小火15-20分钟，可转至砂锅
方法: 炒,焖
工具: 炒锅/砂锅,锅盖
时间: 15-20分钟

### 第11步
步骤: 步骤11
描述: 鸡肉软烂、汤汁浓稠后放入青椒，加入味精兜炒均匀，青椒断生即可关火
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=6
source: rerank_input

```text
菜系: 技巧知识
## 菜品实战示例

- 洋葱炒牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑，需炒制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 白砂糖 2.5-10g（约 1-4 茶匙，根据口味甜度选择）
 - 孜然粉 5g（约 2 茶匙）
 - 生粉 10-15g（约 1 小把）
 - 油 10ml（约 2 汤匙）
 - （可选）十三香 1g（约 0.5 茶匙）
 - （可选）黑胡椒粉 1g（约 0.5 茶匙）

- 蚝油牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑且上浆感足，此菜口感偏甜，需炒制
 - 生抽 5ml（约 1 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 蚝油 10-20ml（约 2-4 汤匙，根据口味咸度选择，蚝油比较咸）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 生粉 25-35g（约 1 大把）
 - 油 10ml（约 2 汤匙）

- 五香盐酥鸡：以一人份的 150g 鸡胸肉为例。鸡肉应切成骰子形状，需炸制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 五香粉 5g（约 2 茶匙）或十三香 2.5-5g（约 1-2 茶匙）
 - （可选）孜然粉 1g（约 0.5 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）

- 蜜汁烤鸡翅：以一人份的 250g 带骨鸡翅中为例。鸡翅上应切几道花刀，成菜咸甜，但突出甜口，需烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 蜂蜜/糖浆 10-20ml（约 2-4 汤匙，根据口味甜度选择。如白砂糖超过或等于 10g，建议只加入 10ml）
 - （可选）五香粉 2.5g（约 1 茶匙。不可用十三香）

- 香烤三文鱼：以一人份的 200g 去骨三文鱼排为例。鱼肉不应改刀，需烤箱烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约
```

### pair_order=7
source: rerank_input

```text
菜品: 凉拌鸡丝
菜系: 未知
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 锅中倒入4升水
工具: 锅

### 第3步
步骤: 步骤3
描述: 加入鸡胸肉、姜片
方法: 加
工具: 锅

### 第4步
步骤: 步骤4
描述: 倒入20毫升料酒
方法: 加
工具: 锅

### 第5步
步骤: 步骤5
描述: 开大火不盖盖将水烧开
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 水开后转中火，用勺子将浮沫捞出
方法: 煮,捞
工具: 锅,勺子

### 第7步
步骤: 步骤7
描述: 继续煮5-7分钟，如果是非冷冻肉煮5分钟，冷冻肉煮7分钟；用筷子插入鸡胸肉，如果能轻松插入，代表鸡肉熟了，否则延长煮制时间
方法: 煮
工具: 锅,筷子
时间: 5-7分钟

### 第8步
步骤: 步骤8
描述: 用凉白开水冲泡鸡胸肉，使鸡胸肉降至室温
方法: 冲
工具: 盆

### 第9步
步骤: 步骤9
描述: 顺着鸡胸肉纹理将鸡胸肉撕成细丝
方法: 撕
工具: 手

### 第10步
步骤: 步骤10
描述: 准备一个碗，碗中加入准备好的麻油、生抽、香醋、白糖、盐，搅拌料汁，使糖和盐尽量溶化
方法: 搅拌
工具: 碗,筷子

### 第11步
步骤: 步骤11
描述: 将料汁倒入鸡丝中，搅拌均匀
方法: 拌
工具: 碗,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=8
source: rerank_input

```text
菜系: 技巧知识
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### pair_order=9
source: rerank_input

```text
菜品: 煮泡面加蛋
菜系: 未知
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### pair_order=10
source: rerank_input

```text
菜品: 生汆丸子汤
菜系: 未知
## 所需食材
1. 前腿肉(500克)
2. 土豆淀粉(40克)
3. 小香葱
4. 木耳
5. 熟豆油
6. 盐(30克)
7. 粉丝
8. 胡椒粉(10克)
9. 葱姜花椒水(400克)
10. 香油(3滴)
11. 香菜(1小颗)
12. 鸡粉
13. 鸡蛋清(1个)
14. 黄花

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### pair_order=11
source: rerank_input

```text
菜品: 姜葱捞鸡
菜系: 粤菜
## 所需食材
1. 姜(50克)
2. 油(35毫升)
3. 盐(5克)
4. 盐焗鸡粉(5克)
5. 糖(5克)
6. 葱(1根)
7. 鸡腿(400克)
8. 鸡腿(4个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### pair_order=12
source: rerank_input

```text
菜品: 商芝肉
菜系: 西北菜
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将肉刮洗干净，入煮锅煮至六成熟（变色为白），捞出趁热用蜂蜜、醋涂抹肉皮。
方法: 煮,涂抹
工具: 煮锅,刷子或勺子
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅内放入熟猪油，用旺火烧至八成熟（约200度，油表有大量青烟，油状平静），将肉块皮朝下投入，炸至呈金红色时，捞入凉肉煮锅中泡软。
方法: 炸
工具: 炒锅,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 将肉放在案板上，切成10 cm长、0.6 cm厚的片，仍然皮朝下，整齐装入蒸碗内。
方法: 切
工具: 刀,案板,蒸碗
时间: 约5分钟

### 第4步
步骤: 步骤4
描述: 将5克大葱切成2.4 cm长的段，5克切成2.4 cm长的斜形片；姜去皮洗净，1.5克切成片，5克切成末；摊的鸡蛋皮切成2.4 cm长的等腰三角形片。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第5步
步骤: 步骤5
描述: 商芝入沸水锅中煮软捞出，去除老茎、杂质，淘洗干净，切成3 cm长的段，放入碗中，加酱油5克、精盐1克、熟猪油10克拌匀，盖在肉片上。
方法: 煮,拌
工具: 煮锅,碗,筷子
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 另将鸡汤100克放入一小碗中，加酱油5克、精盐0.5克、料酒15克搅匀，浇入蒸碗，再放入姜片、葱段、八角，上笼用旺火蒸约半小时后，转用小火继续蒸约一小时三十分钟。
方法: 蒸
工具: 蒸锅,小碗
时间: 2小时

### 第7步
步骤: 步骤7
描述: 熟烂后取出，拣去姜、葱、八角，倒、过滤原汁，将肉扣入汤盘。
方法: 过滤,扣盘
工具: 滤网,汤盘
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 炒锅内放入鸡汤100克，加入原汁，用旺火烧沸，下入姜末、葱片、味精后搅匀，投入摊鸡蛋皮，淋芝麻油，浇入汤盘即成。
方法: 烧,淋
工具: 炒锅,汤勺
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Re
```

### pair_order=13
source: rerank_input

```text
分类: 烹饪技巧
技巧文档扩展上下文: 如何决策吃什么、腌（肉）
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
## 正文
# 腌（肉）
## 注意
## 注意

此处所描述的腌渍是食材烹饪前处理的步骤，并非制作咸肉或腌制香肠等成品
## 腌渍
## 腌渍

在烹饪前腌制肉类是让肉类预先入味的常用方法。一般腌渍的对象是生肉。根据菜品的需求，可以自行确定肉类改刀的大小。

 例如炸鸡米花，鸡胸肉是在改刀为骰子大小的小块后放入碗中腌渍
 例如烤全羊，羊腿，半扇或整扇羊肉不必改刀即可用大量调味料涂抹在表面从而腌渍入味

根据菜品的不同，腌渍所选的调味料、辅料可以是任何种类。有时候为了不同的口味，辅料也可能需要预先处理。
## 腌渍基本概念
## 腌渍基本概念

此处介绍的是正常口味的腌渍过程。

- 一般来说，肉量越大（比如一次性腌渍 5kg 鸡翅），体积越大（比如一整个羊
```

## Hybrid Retrieval / Reranked Results
### result_order=0
source: reranked_results
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.575760543346405, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=1
source: reranked_results
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_441, recipe_name=黄焖鸡, category=荤菜, score=0.5997363328933716, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡腿洗净，剁成4cm大小的块
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生姜切片、干辣椒切成小圈
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 香菇切片，青椒切成细长的马蹄状；若为干香菇，洗净灰尘后泡一晚上并留香菇水备用
方法: 切,泡发
工具: 刀,案板,盆

### 第4步
步骤: 步骤4
描述: 若有土豆，切为与鸡肉大小类似的滚刀块
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 炒糖色：锅里倒入底油，冷油时放入白糖；小火慢慢加热，待糖融化并变成较深的棕色，期间不断搅拌
方法: 炒
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第6步
步骤: 步骤6
描述: 迅速倒入鸡块，转大火快速翻炒，烹入料酒继续翻炒片刻
方法: 炒
工具: 炒锅,锅铲
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入生姜片和干辣椒炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 放入酱油炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 倒入香菇水或清水，以能淹住鸡肉为准
方法: 倒
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 加入香菇片、白胡椒粉、盐、土豆，翻炒均匀后盖上锅盖焖煮，转中小火15-20分钟，可转至砂锅
方法: 炒,焖
工具: 炒锅/砂锅,锅盖
时间: 15-20分钟

### 第11步
步骤: 步骤11
描述: 鸡肉软烂、汤汁浓稠后放入青椒，加入味精兜炒均匀，青椒断生即可关火
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: reranked_results
metadata_summary: node_id=tipdoc_e5959b9d0464, chunk_id=tipdoc_e5959b9d0464_chunk_1299, recipe_name=腌（肉）, category=烹饪技巧, score=0.5783764719963074, search_type=vector_enhanced

```text
## 菜品实战示例

- 洋葱炒牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑，需炒制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 白砂糖 2.5-10g（约 1-4 茶匙，根据口味甜度选择）
 - 孜然粉 5g（约 2 茶匙）
 - 生粉 10-15g（约 1 小把）
 - 油 10ml（约 2 汤匙）
 - （可选）十三香 1g（约 0.5 茶匙）
 - （可选）黑胡椒粉 1g（约 0.5 茶匙）

- 蚝油牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑且上浆感足，此菜口感偏甜，需炒制
 - 生抽 5ml（约 1 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 蚝油 10-20ml（约 2-4 汤匙，根据口味咸度选择，蚝油比较咸）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 生粉 25-35g（约 1 大把）
 - 油 10ml（约 2 汤匙）

- 五香盐酥鸡：以一人份的 150g 鸡胸肉为例。鸡肉应切成骰子形状，需炸制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 五香粉 5g（约 2 茶匙）或十三香 2.5-5g（约 1-2 茶匙）
 - （可选）孜然粉 1g（约 0.5 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）

- 蜜汁烤鸡翅：以一人份的 250g 带骨鸡翅中为例。鸡翅上应切几道花刀，成菜咸甜，但突出甜口，需烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 蜂蜜/糖浆 10-20ml（约 2-4 汤匙，根据口味甜度选择。如白砂糖超过或等于 10g，建议只加入 10ml）
 - （可选）五香粉 2.5g（约 1 茶匙。不可用十三香）

- 香烤三文鱼：以一人份的 200g 去骨三文鱼排为例。鱼肉不应改刀，需烤箱烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 红糖 10-20g（约 4-8 茶匙，根据口味甜度选择）
 - 意大利黑醋/镇江香醋 2.5-5ml（约 0.5-1 汤匙，根据口味酸度选择）
 - 肉豆蔻粉 2.5g（约 1 茶匙）
 - 百里香粉 1g（约 0.5 茶匙）
 - 姜粉 1g（约 0.5 茶匙）
 - 迷迭香粉 1-2g（约 0.5-1 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）
 - （可选）干辣椒碎 2.5-10g（约 1-4 茶匙，根据口味辣度选择）
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 腌（肉） / 腌渍基本概念 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: reranked_results
metadata_summary: node_id=201002255, chunk_id=201002255_chunk_465, recipe_name=口水鸡, category=荤菜, score=0.6093879342079163, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，1颗小葱切段，15颗花椒备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鸡肉洗净，放入锅中，加清水没过鸡肉，放入姜片、葱段和花椒，大火烧开
方法: 煮
工具: 锅
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 水开后转中小火煮20分钟，关火
方法: 煮
工具: 锅
时间: 20分钟

### 第4步
步骤: 步骤4
描述: 取出鸡肉，放入冰水中迅速冷却至冰凉
方法: 冷却
工具: 盆,冰水
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 取出鸡肉，切块摆盘备用
方法: 切
工具: 刀,案板,盘子
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 小火将锅烧热，倒入花生，烘烤至表皮爆裂，注意翻动防糊
方法: 炒,烘烤
工具: 锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 一颗葱切段，蒜拍末，花椒15颗，花生去皮后切碎
方法: 切,拍
工具: 刀,案板
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 锅内倒油烧热，放入葱段、花椒和一半蒜末炒香
方法: 炒
工具: 锅,锅铲
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 油温升至8成热后关火，滤出热油
方法: 炸,过滤
工具: 锅,滤网,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 将热油倒入盛辣椒粉的碗中，搅拌并滤出红油
方法: 炸,搅拌,过滤
工具: 碗,筷子,滤网
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 在红油中加入剩余蒜末、生抽、醋、盐、味精、糖、香油、花椒粉，拌匀放凉
方法: 搅拌
工具: 碗,筷子
时间: 2分钟

### 第12步
步骤: 步骤12
描述: 鸡肉上撒花生碎，淋红油，撒香菜即成
方法: 淋,撒
工具: 勺子,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: reranked_results
metadata_summary: node_id=technique_expansion:tipdoc_e5959b9d0464,tipdoc_820d789ff48e, recipe_name=如何决策吃什么、腌（肉）, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么、腌（肉）
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
## 正文
# 腌（肉）
## 注意
## 注意

此处所描述的腌渍是食材烹饪前处理的步骤，并非制作咸肉或腌制香肠等成品
## 腌渍
## 腌渍

在烹饪前腌制肉类是让肉类预先入味的常用方法。一般腌渍的对象是生肉。根据菜品的需求，可以自行确定肉类改刀的大小。

 例如炸鸡米花，鸡胸肉是在改刀为骰子大小的小块后放入碗中腌渍
 例如烤全羊，羊腿，半扇或整扇羊肉不必改刀即可用大量调味料涂抹在表面从而腌渍入味

根据菜品的不同，腌渍所选的调味料、辅料可以是任何种类。有时候为了不同的口味，辅料也可能需要预先处理。
## 腌渍基本概念
## 腌渍基本概念

此处介绍的是正常口味的腌渍过程。

- 一般来说，肉量越大（比如一次性腌渍 5kg 鸡翅），体积越大（比如一整个羊腿），口味越重，则需要调味料和辅料越多
- 一般来说，计划腌渍的时间越长，使用的调味料和辅料越少
- 腌渍时应使用料均匀覆盖在所有的表面。如果是肉片、肉丝，应该用手尽量抓匀、搅匀。如果是整个羊腿，应该用手或刷子在表面刷匀
- 一般炒肉、炸肉需要提前腌渍。炒肉应该保证肉鲜嫩的口感，烹调往往需要大火且时间较短。短时间烹饪不容易入味时，提前腌渍就能弥补口味的不足
```

### result_order=5
source: reranked_results
metadata_summary: node_id=201002647, chunk_id=201002647_chunk_533, recipe_name=新疆大盘鸡, category=荤菜, score=0.6050660014152527, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将鸡腿肉剁成块状，用清水加盐浸泡5分钟去除血水与腥味，然后沥干备用。
方法: 切,浸泡
工具: 刀,盆
时间: 5分钟

### 第2步
步骤: 步骤2
描述: 葱、蒜、干线椒、土豆等洗净；土豆削皮。
方法: 清洗,削皮
工具: 刀,案板
时间: 3-5分钟

### 第3步
步骤: 步骤3
描述: 葱白切成长约4cm的段；菜椒、甜椒切块；土豆切成4cm×4cm滚刀块。
方法: 切
工具: 刀,案板
时间: 5分钟

### 第4步
步骤: 步骤4
描述: 锅中倒入油，加入白砂糖，小火炒糖色至焦黄色，立即倒入沥干鸡肉翻炒上色。
方法: 炒
工具: 炒锅,锅铲
时间: 2-3分钟

### 第5步
步骤: 步骤5
描述: 加入花椒、香叶、香果、干线椒等香料继续翻炒出香味。
方法: 炒
工具: 锅铲
时间: 1分钟

### 第6步
步骤: 步骤6
描述: 加入5g盐、7ml生抽、10g蚝油、100g料酒（或啤酒）和1升清水，中火煮沸后转小火慢炖。
方法: 炖
工具: 锅铲
时间: 20分钟

### 第7步
步骤: 步骤7
描述: 汤汁收至鸡肉即将露出时，将土豆块铺在表面，不翻动，盖盖继续炖。
方法: 炖
工具: 锅盖
时间: 10分钟

### 第8步
步骤: 步骤8
描述: 加入大葱段、菜椒和甜椒块，继续炖至汤汁浓稠，最后翻面让土豆吸汁，关火盛出。
方法: 炖,收汁
工具: 锅铲
时间: 5-10分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=6
source: reranked_results
metadata_summary: node_id=201002203, chunk_id=201002203_chunk_457, recipe_name=凉拌鸡丝, category=荤菜, score=0.5776276588439941, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，备用
方法: 切
工具: 刀

### 第2步
步骤: 步骤2
描述: 锅中倒入4升水
工具: 锅

### 第3步
步骤: 步骤3
描述: 加入鸡胸肉、姜片
方法: 加
工具: 锅

### 第4步
步骤: 步骤4
描述: 倒入20毫升料酒
方法: 加
工具: 锅

### 第5步
步骤: 步骤5
描述: 开大火不盖盖将水烧开
方法: 煮
工具: 锅

### 第6步
步骤: 步骤6
描述: 水开后转中火，用勺子将浮沫捞出
方法: 煮,捞
工具: 锅,勺子

### 第7步
步骤: 步骤7
描述: 继续煮5-7分钟，如果是非冷冻肉煮5分钟，冷冻肉煮7分钟；用筷子插入鸡胸肉，如果能轻松插入，代表鸡肉熟了，否则延长煮制时间
方法: 煮
工具: 锅,筷子
时间: 5-7分钟

### 第8步
步骤: 步骤8
描述: 用凉白开水冲泡鸡胸肉，使鸡胸肉降至室温
方法: 冲
工具: 盆

### 第9步
步骤: 步骤9
描述: 顺着鸡胸肉纹理将鸡胸肉撕成细丝
方法: 撕
工具: 手

### 第10步
步骤: 步骤10
描述: 准备一个碗，碗中加入准备好的麻油、生抽、香醋、白糖、盐，搅拌料汁，使糖和盐尽量溶化
方法: 搅拌
工具: 碗,筷子

### 第11步
步骤: 步骤11
描述: 将料汁倒入鸡丝中，搅拌均匀
方法: 拌
工具: 碗,筷子

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=7
source: reranked_results
metadata_summary: node_id=201001526, chunk_id=201001526_chunk_333, recipe_name=商芝肉, category=荤菜, score=0.5612736344337463, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 将肉刮洗干净，入煮锅煮至六成熟（变色为白），捞出趁热用蜂蜜、醋涂抹肉皮。
方法: 煮,涂抹
工具: 煮锅,刷子或勺子
时间: 约10分钟

### 第2步
步骤: 步骤2
描述: 炒锅内放入熟猪油，用旺火烧至八成熟（约200度，油表有大量青烟，油状平静），将肉块皮朝下投入，炸至呈金红色时，捞入凉肉煮锅中泡软。
方法: 炸
工具: 炒锅,漏勺
时间: 约2-3分钟

### 第3步
步骤: 步骤3
描述: 将肉放在案板上，切成10 cm长、0.6 cm厚的片，仍然皮朝下，整齐装入蒸碗内。
方法: 切
工具: 刀,案板,蒸碗
时间: 约5分钟

### 第4步
步骤: 步骤4
描述: 将5克大葱切成2.4 cm长的段，5克切成2.4 cm长的斜形片；姜去皮洗净，1.5克切成片，5克切成末；摊的鸡蛋皮切成2.4 cm长的等腰三角形片。
方法: 切
工具: 刀,案板
时间: 约5分钟

### 第5步
步骤: 步骤5
描述: 商芝入沸水锅中煮软捞出，去除老茎、杂质，淘洗干净，切成3 cm长的段，放入碗中，加酱油5克、精盐1克、熟猪油10克拌匀，盖在肉片上。
方法: 煮,拌
工具: 煮锅,碗,筷子
时间: 约5分钟

### 第6步
步骤: 步骤6
描述: 另将鸡汤100克放入一小碗中，加酱油5克、精盐0.5克、料酒15克搅匀，浇入蒸碗，再放入姜片、葱段、八角，上笼用旺火蒸约半小时后，转用小火继续蒸约一小时三十分钟。
方法: 蒸
工具: 蒸锅,小碗
时间: 2小时

### 第7步
步骤: 步骤7
描述: 熟烂后取出，拣去姜、葱、八角，倒、过滤原汁，将肉扣入汤盘。
方法: 过滤,扣盘
工具: 滤网,汤盘
时间: 约2分钟

### 第8步
步骤: 步骤8
描述: 炒锅内放入鸡汤100克，加入原汁，用旺火烧沸，下入姜末、葱片、味精后搅匀，投入摊鸡蛋皮，淋芝麻油，浇入汤盘即成。
方法: 烧,淋
工具: 炒锅,汤勺
时间: 约1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 五星 (DifficultyLevel)
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
metadata_summary: node_id=201002434, chunk_id=201002434_chunk_496, recipe_name=姜葱捞鸡, category=荤菜, score=0.5661523938179016, search_type=vector_enhanced

```text
## 所需食材
1. 姜(50克)
2. 油(35毫升)
3. 盐(5克)
4. 盐焗鸡粉(5克)
5. 糖(5克)
6. 葱(1根)
7. 鸡腿(400克)
8. 鸡腿(4个)

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=10
source: reranked_results
metadata_summary: node_id=201003707, chunk_id=201003707_chunk_725, recipe_name=生汆丸子汤, category=汤类, score=0.5707718729972839, search_type=vector_enhanced

```text
## 所需食材
1. 前腿肉(500克)
2. 土豆淀粉(40克)
3. 小香葱
4. 木耳
5. 熟豆油
6. 盐(30克)
7. 粉丝
8. 胡椒粉(10克)
9. 葱姜花椒水(400克)
10. 香油(3滴)
11. 香菜(1小颗)
12. 鸡粉
13. 鸡蛋清(1个)
14. 黄花

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 汤类 (Category)
- OUT DIFFICULTY_LEVEL 四星 (DifficultyLevel)
```

### result_order=11
source: reranked_results
metadata_summary: node_id=201004172, chunk_id=201004172_chunk_827, recipe_name=煮泡面加蛋, category=主食, score=0.5717189908027649, search_type=vector_enhanced

```text
## 标签
可加入火腿肠、生菜、小肉丝、辣条、鱼干、虾仁、鸡腿等配料,鸡蛋可用生鸡蛋、熟鸡蛋、卤蛋等
关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 主食 (Category)
- OUT BELONGS_TO 主食 (RecipeCategory)
```

### result_order=12
source: reranked_results
metadata_summary: node_id=201004679, recipe_name=鸡肉, retrieval_level=entity, search_type=entity_level

```text
命中关键词: 鸡肉
食材名称: 鸡肉
类别: 蛋白质
关联图谱:
- OUT HAS_CONCEPT_TYPE Ingredient (ConceptType)
- OUT BELONGS_TO_CATEGORY 蛋白质 (Category)
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
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.575760543346405, search_type=vector_enhanced

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=1
source: top_k_final
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_441, recipe_name=黄焖鸡, category=荤菜, score=0.5997363328933716, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡腿洗净，剁成4cm大小的块
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生姜切片、干辣椒切成小圈
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 香菇切片，青椒切成细长的马蹄状；若为干香菇，洗净灰尘后泡一晚上并留香菇水备用
方法: 切,泡发
工具: 刀,案板,盆

### 第4步
步骤: 步骤4
描述: 若有土豆，切为与鸡肉大小类似的滚刀块
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 炒糖色：锅里倒入底油，冷油时放入白糖；小火慢慢加热，待糖融化并变成较深的棕色，期间不断搅拌
方法: 炒
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第6步
步骤: 步骤6
描述: 迅速倒入鸡块，转大火快速翻炒，烹入料酒继续翻炒片刻
方法: 炒
工具: 炒锅,锅铲
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入生姜片和干辣椒炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 放入酱油炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 倒入香菇水或清水，以能淹住鸡肉为准
方法: 倒
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 加入香菇片、白胡椒粉、盐、土豆，翻炒均匀后盖上锅盖焖煮，转中小火15-20分钟，可转至砂锅
方法: 炒,焖
工具: 炒锅/砂锅,锅盖
时间: 15-20分钟

### 第11步
步骤: 步骤11
描述: 鸡肉软烂、汤汁浓稠后放入青椒，加入味精兜炒均匀，青椒断生即可关火
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: top_k_final
metadata_summary: node_id=tipdoc_e5959b9d0464, chunk_id=tipdoc_e5959b9d0464_chunk_1299, recipe_name=腌（肉）, category=烹饪技巧, score=0.5783764719963074, search_type=vector_enhanced

```text
## 菜品实战示例

- 洋葱炒牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑，需炒制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 白砂糖 2.5-10g（约 1-4 茶匙，根据口味甜度选择）
 - 孜然粉 5g（约 2 茶匙）
 - 生粉 10-15g（约 1 小把）
 - 油 10ml（约 2 汤匙）
 - （可选）十三香 1g（约 0.5 茶匙）
 - （可选）黑胡椒粉 1g（约 0.5 茶匙）

- 蚝油牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑且上浆感足，此菜口感偏甜，需炒制
 - 生抽 5ml（约 1 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 蚝油 10-20ml（约 2-4 汤匙，根据口味咸度选择，蚝油比较咸）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 生粉 25-35g（约 1 大把）
 - 油 10ml（约 2 汤匙）

- 五香盐酥鸡：以一人份的 150g 鸡胸肉为例。鸡肉应切成骰子形状，需炸制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 五香粉 5g（约 2 茶匙）或十三香 2.5-5g（约 1-2 茶匙）
 - （可选）孜然粉 1g（约 0.5 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）

- 蜜汁烤鸡翅：以一人份的 250g 带骨鸡翅中为例。鸡翅上应切几道花刀，成菜咸甜，但突出甜口，需烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 蜂蜜/糖浆 10-20ml（约 2-4 汤匙，根据口味甜度选择。如白砂糖超过或等于 10g，建议只加入 10ml）
 - （可选）五香粉 2.5g（约 1 茶匙。不可用十三香）

- 香烤三文鱼：以一人份的 200g 去骨三文鱼排为例。鱼肉不应改刀，需烤箱烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 红糖 10-20g（约 4-8 茶匙，根据口味甜度选择）
 - 意大利黑醋/镇江香醋 2.5-5ml（约 0.5-1 汤匙，根据口味酸度选择）
 - 肉豆蔻粉 2.5g（约 1 茶匙）
 - 百里香粉 1g（约 0.5 茶匙）
 - 姜粉 1g（约 0.5 茶匙）
 - 迷迭香粉 1-2g（约 0.5-1 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）
 - （可选）干辣椒碎 2.5-10g（约 1-4 茶匙，根据口味辣度选择）
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 腌（肉） / 腌渍基本概念 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: top_k_final
metadata_summary: node_id=201002255, chunk_id=201002255_chunk_465, recipe_name=口水鸡, category=荤菜, score=0.6093879342079163, search_type=vector_enhanced

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，1颗小葱切段，15颗花椒备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鸡肉洗净，放入锅中，加清水没过鸡肉，放入姜片、葱段和花椒，大火烧开
方法: 煮
工具: 锅
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 水开后转中小火煮20分钟，关火
方法: 煮
工具: 锅
时间: 20分钟

### 第4步
步骤: 步骤4
描述: 取出鸡肉，放入冰水中迅速冷却至冰凉
方法: 冷却
工具: 盆,冰水
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 取出鸡肉，切块摆盘备用
方法: 切
工具: 刀,案板,盘子
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 小火将锅烧热，倒入花生，烘烤至表皮爆裂，注意翻动防糊
方法: 炒,烘烤
工具: 锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 一颗葱切段，蒜拍末，花椒15颗，花生去皮后切碎
方法: 切,拍
工具: 刀,案板
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 锅内倒油烧热，放入葱段、花椒和一半蒜末炒香
方法: 炒
工具: 锅,锅铲
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 油温升至8成热后关火，滤出热油
方法: 炸,过滤
工具: 锅,滤网,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 将热油倒入盛辣椒粉的碗中，搅拌并滤出红油
方法: 炸,搅拌,过滤
工具: 碗,筷子,滤网
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 在红油中加入剩余蒜末、生抽、醋、盐、味精、糖、香油、花椒粉，拌匀放凉
方法: 搅拌
工具: 碗,筷子
时间: 2分钟

### 第12步
步骤: 步骤12
描述: 鸡肉上撒花生碎，淋红油，撒香菜即成
方法: 淋,撒
工具: 勺子,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: top_k_final
metadata_summary: node_id=technique_expansion:tipdoc_e5959b9d0464,tipdoc_820d789ff48e, recipe_name=如何决策吃什么、腌（肉）, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion

```text
技巧文档扩展上下文: 如何决策吃什么、腌（肉）
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
## 正文
# 腌（肉）
## 注意
## 注意

此处所描述的腌渍是食材烹饪前处理的步骤，并非制作咸肉或腌制香肠等成品
## 腌渍
## 腌渍

在烹饪前腌制肉类是让肉类预先入味的常用方法。一般腌渍的对象是生肉。根据菜品的需求，可以自行确定肉类改刀的大小。

 例如炸鸡米花，鸡胸肉是在改刀为骰子大小的小块后放入碗中腌渍
 例如烤全羊，羊腿，半扇或整扇羊肉不必改刀即可用大量调味料涂抹在表面从而腌渍入味

根据菜品的不同，腌渍所选的调味料、辅料可以是任何种类。有时候为了不同的口味，辅料也可能需要预先处理。
## 腌渍基本概念
## 腌渍基本概念

此处介绍的是正常口味的腌渍过程。

- 一般来说，肉量越大（比如一次性腌渍 5kg 鸡翅），体积越大（比如一整个羊腿），口味越重，则需要调味料和辅料越多
- 一般来说，计划腌渍的时间越长，使用的调味料和辅料越少
- 腌渍时应使用料均匀覆盖在所有的表面。如果是肉片、肉丝，应该用手尽量抓匀、搅匀。如果是整个羊腿，应该用手或刷子在表面刷匀
- 一般炒肉、炸肉需要提前腌渍。炒肉应该保证肉鲜嫩的口感，烹调往往需要大火且时间较短。短时间烹饪不容易入味时，提前腌渍就能弥补口味的不足
```

## Final Prompt Context
### result_order=0
source: generation_context
metadata_summary: node_id=tipdoc_820d789ff48e, chunk_id=tipdoc_820d789ff48e_chunk_1241, recipe_name=如何决策吃什么, category=通用知识, score=0.575760543346405, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 菜的选择
### 菜的选择

* 如果人数超过 8 人，考虑在荤菜中增加鱼类荤菜。
* 如果有小孩，考虑增加有甜味的菜。
* 考虑增加特色菜、拿手菜。
* 注意决策荤菜时不要全部使用同一种动物的肉。考虑顺序为：`猪肉`、`鸡肉`、`牛肉`、`羊肉`、`鸭肉`、`鱼肉`。
* 不要选择奇奇怪怪的动物做荤菜。
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 通用知识 (Category)
- OUT HAS_CHUNK 如何决策吃什么 (TechniqueChunk): category: 通用知识
```

### result_order=1
source: generation_context
metadata_summary: node_id=201002122, chunk_id=201002122_chunk_441, recipe_name=黄焖鸡, category=荤菜, score=0.5997363328933716, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 鸡腿洗净，剁成4cm大小的块
方法: 切
工具: 刀,案板

### 第2步
步骤: 步骤2
描述: 生姜切片、干辣椒切成小圈
方法: 切
工具: 刀,案板

### 第3步
步骤: 步骤3
描述: 香菇切片，青椒切成细长的马蹄状；若为干香菇，洗净灰尘后泡一晚上并留香菇水备用
方法: 切,泡发
工具: 刀,案板,盆

### 第4步
步骤: 步骤4
描述: 若有土豆，切为与鸡肉大小类似的滚刀块
方法: 切
工具: 刀,案板

### 第5步
步骤: 步骤5
描述: 炒糖色：锅里倒入底油，冷油时放入白糖；小火慢慢加热，待糖融化并变成较深的棕色，期间不断搅拌
方法: 炒
工具: 炒锅,锅铲
时间: 约2-3分钟

### 第6步
步骤: 步骤6
描述: 迅速倒入鸡块，转大火快速翻炒，烹入料酒继续翻炒片刻
方法: 炒
工具: 炒锅,锅铲
时间: 约1分钟

### 第7步
步骤: 步骤7
描述: 加入生姜片和干辣椒炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第8步
步骤: 步骤8
描述: 放入酱油炒匀
方法: 炒
工具: 锅铲
时间: 约30秒

### 第9步
步骤: 步骤9
描述: 倒入香菇水或清水，以能淹住鸡肉为准
方法: 倒
工具: 锅铲

### 第10步
步骤: 步骤10
描述: 加入香菇片、白胡椒粉、盐、土豆，翻炒均匀后盖上锅盖焖煮，转中小火15-20分钟，可转至砂锅
方法: 炒,焖
工具: 炒锅/砂锅,锅盖
时间: 15-20分钟

### 第11步
步骤: 步骤11
描述: 鸡肉软烂、汤汁浓稠后放入青椒，加入味精兜炒均匀，青椒断生即可关火
方法: 炒
工具: 锅铲
时间: 约30秒

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT DIFFICULTY_LEVEL 三星 (DifficultyLevel)
```

### result_order=2
source: generation_context
metadata_summary: node_id=tipdoc_e5959b9d0464, chunk_id=tipdoc_e5959b9d0464_chunk_1299, recipe_name=腌（肉）, category=烹饪技巧, score=0.5783764719963074, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 菜品实战示例

- 洋葱炒牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑，需炒制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 白砂糖 2.5-10g（约 1-4 茶匙，根据口味甜度选择）
 - 孜然粉 5g（约 2 茶匙）
 - 生粉 10-15g（约 1 小把）
 - 油 10ml（约 2 汤匙）
 - （可选）十三香 1g（约 0.5 茶匙）
 - （可选）黑胡椒粉 1g（约 0.5 茶匙）

- 蚝油牛肉：以一人份的 150g 牛肉为例。牛肉应切片，成菜口感应嫩滑且上浆感足，此菜口感偏甜，需炒制
 - 生抽 5ml（约 1 汤匙）
 - 料酒 5ml（约 1 汤匙）
 - 蚝油 10-20ml（约 2-4 汤匙，根据口味咸度选择，蚝油比较咸）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 生粉 25-35g（约 1 大把）
 - 油 10ml（约 2 汤匙）

- 五香盐酥鸡：以一人份的 150g 鸡胸肉为例。鸡肉应切成骰子形状，需炸制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 五香粉 5g（约 2 茶匙）或十三香 2.5-5g（约 1-2 茶匙）
 - （可选）孜然粉 1g（约 0.5 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）

- 蜜汁烤鸡翅：以一人份的 250g 带骨鸡翅中为例。鸡翅上应切几道花刀，成菜咸甜，但突出甜口，需烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 白砂糖 5-15g（约 2-6 茶匙，根据口味甜度选择）
 - 蜂蜜/糖浆 10-20ml（约 2-4 汤匙，根据口味甜度选择。如白砂糖超过或等于 10g，建议只加入 10ml）
 - （可选）五香粉 2.5g（约 1 茶匙。不可用十三香）

- 香烤三文鱼：以一人份的 200g 去骨三文鱼排为例。鱼肉不应改刀，需烤箱烤制
 - 生抽 10ml（约 2 汤匙）
 - 料酒 2.5ml（约 0.5 汤匙）
 - 红糖 10-20g（约 4-8 茶匙，根据口味甜度选择）
 - 意大利黑醋/镇江香醋 2.5-5ml（约 0.5-1 汤匙，根据口味酸度选择）
 - 肉豆蔻粉 2.5g（约 1 茶匙）
 - 百里香粉 1g（约 0.5 茶匙）
 - 姜粉 1g（约 0.5 茶匙）
 - 迷迭香粉 1-2g（约 0.5-1 茶匙）
 - （可选）白胡椒粉 1g（约 0.5 茶匙）
 - （可选）干辣椒碎 2.5-10g（约 1-4 茶匙，根据口味辣度选择）
关联图谱:
- OUT HAS_CONCEPT_TYPE TechniqueDoc (ConceptType)
- OUT BELONGS_TO_CATEGORY 烹饪技巧 (Category)
- OUT HAS_CHUNK 腌（肉） / 腌渍基本概念 (TechniqueChunk): category: 烹饪技巧
```

### result_order=3
source: generation_context
metadata_summary: node_id=201002255, chunk_id=201002255_chunk_465, recipe_name=口水鸡, category=荤菜, score=0.6093879342079163, search_type=vector_enhanced, route_strategy=hybrid_traditional

```text
## 制作步骤

### 第1步
步骤: 步骤1
描述: 姜切片，1颗小葱切段，15颗花椒备用
方法: 切
工具: 刀,案板
时间: 2分钟

### 第2步
步骤: 步骤2
描述: 鸡肉洗净，放入锅中，加清水没过鸡肉，放入姜片、葱段和花椒，大火烧开
方法: 煮
工具: 锅
时间: 5分钟

### 第3步
步骤: 步骤3
描述: 水开后转中小火煮20分钟，关火
方法: 煮
工具: 锅
时间: 20分钟

### 第4步
步骤: 步骤4
描述: 取出鸡肉，放入冰水中迅速冷却至冰凉
方法: 冷却
工具: 盆,冰水
时间: 5分钟

### 第5步
步骤: 步骤5
描述: 取出鸡肉，切块摆盘备用
方法: 切
工具: 刀,案板,盘子
时间: 3分钟

### 第6步
步骤: 步骤6
描述: 小火将锅烧热，倒入花生，烘烤至表皮爆裂，注意翻动防糊
方法: 炒,烘烤
工具: 锅,锅铲
时间: 3-4分钟

### 第7步
步骤: 步骤7
描述: 一颗葱切段，蒜拍末，花椒15颗，花生去皮后切碎
方法: 切,拍
工具: 刀,案板
时间: 2分钟

### 第8步
步骤: 步骤8
描述: 锅内倒油烧热，放入葱段、花椒和一半蒜末炒香
方法: 炒
工具: 锅,锅铲
时间: 1分钟

### 第9步
步骤: 步骤9
描述: 油温升至8成热后关火，滤出热油
方法: 炸,过滤
工具: 锅,滤网,碗
时间: 30秒

### 第10步
步骤: 步骤10
描述: 将热油倒入盛辣椒粉的碗中，搅拌并滤出红油
方法: 炸,搅拌,过滤
工具: 碗,筷子,滤网
时间: 1分钟

### 第11步
步骤: 步骤11
描述: 在红油中加入剩余蒜末、生抽、醋、盐、味精、糖、香油、花椒粉，拌匀放凉
方法: 搅拌
工具: 碗,筷子
时间: 2分钟

### 第12步
步骤: 步骤12
描述: 鸡肉上撒花生碎，淋红油，撒香菜即成
方法: 淋,撒
工具: 勺子,盘子
时间: 1分钟

关联图谱:
- OUT HAS_CONCEPT_TYPE Recipe (ConceptType)
- OUT BELONGS_TO_CATEGORY 荤菜 (Category)
- OUT BELONGS_TO 荤菜 (RecipeCategory)
```

### result_order=4
source: generation_context
metadata_summary: node_id=technique_expansion:tipdoc_e5959b9d0464,tipdoc_820d789ff48e, recipe_name=如何决策吃什么、腌（肉）, category=烹饪技巧, retrieval_level=context_expansion, search_type=technique_expansion, route_strategy=hybrid_traditional

```text
技巧文档扩展上下文: 如何决策吃什么、腌（肉）
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
## 正文
# 腌（肉）
## 注意
## 注意

此处所描述的腌渍是食材烹饪前处理的步骤，并非制作咸肉或腌制香肠等成品
## 腌渍
## 腌渍

在烹饪前腌制肉类是让肉类预先入味的常用方法。一般腌渍的对象是生肉。根据菜品的需求，可以自行确定肉类改刀的大小。

 例如炸鸡米花，鸡胸肉是在改刀为骰子大小的小块后放入碗中腌渍
 例如烤全羊，羊腿，半扇或整扇羊肉不必改刀即可用大量调味料涂抹在表面从而腌渍入味

根据菜品的不同，腌渍所选的调味料、辅料可以是任何种类。有时候为了不同的口味，辅料也可能需要预先处理。
## 腌渍基本概念
## 腌渍基本概念

此处介绍的是正常口味的腌渍过程。

- 一般来说，肉量越大（比如一次性腌渍 5kg 鸡翅），体积越大（比如一整个羊腿），口味越重，则需要调味料和辅料越多
- 一般来说，计划腌渍的时间越长，使用的调味料和辅料越少
- 腌渍时应使用料均匀覆盖在所有的表面。如果是肉片、肉丝，应该用手尽量抓匀、搅匀。如果是整个羊腿，应该用手或刷子在表面刷匀
- 一般炒肉、炸肉需要提前腌渍。炒肉应该保证肉鲜嫩的口感，烹调往往需要大火且时间较短。短时间烹饪不容易入味时，提前腌渍就能弥补口味的不足
```

