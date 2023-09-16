<!--
# 向量搜索如何优化零售货运路线
https://thenewstack.io/how-vector-search-can-optimize-retail-trucking-routes/
https://cdn.thenewstack.io/media/2023/08/7d65b9a1-semi_dalle2.jpg
Image from DALL-E.
 -->

如何找到最佳路线以提高运送时间效率以及装卸货物效率的探讨。

译自 [How Vector Search Can Optimize Retail Trucking Routes](https://thenewstack.io/how-vector-search-can-optimize-retail-trucking-routes/) 。

向量和向量搜索是大型语言模型(LLM)的关键组成部分，但它们在许多其他应用程序的众多用例中也非常有用，这些应用程序可能超出了你的考虑范围。比如最有效地运送零售商品的方法怎么样?

在本系列文章的前两篇文章中，我讲述了一个假设的承包商的故事，他被聘请帮助一家[大型零售商实施 AI/ML 解决方案](https://thenewstack.io/an-e-tailers-journey-to-real-time-ai-recommendations/)，然后我探讨了这位分布式系统和 AI 专家如何利用向量搜索来[推动该公司的客户促销结果](https://thenewstack.io/how-vector-search-can-influence-customer-shopping-habits/)。现在，我将带您了解这个承包商如何使用向量搜索来优化卡车路线。

## 问题

当我们正在研究缩小(并最终禁用)[第一篇文章](https://thenewstack.io/an-e-tailers-journey-to-real-time-ai-recommendations/)中的推荐批处理作业的选择时，运输服务团队邀请我们参加一次会议。他们听说我们如何帮助推销团队，想知道我们是否可以看一下他们的一个问题。

BigBoxCo 的产品是从机场和海运港口用卡车运来的。一旦到达配送中心(DC)，它们就会被贴标签并分拆成较小的装运量，以运送到各个实体店。虽然这一环节我们有自己的半挂车，但车队组织效率不高。

目前，司机在卡车的数字设备上得到一份店铺列表，主管建议一条路线。然而，司机经常对店铺停靠顺序有异议，经常无视主管的路线建议。当然，这导致预期装运和补货时间以及总耗时有差异。

了解这一点，DC 员工无法完全填充每辆卡车的集装箱，因为他们必须在卡车上留出空间访问每个店铺的产品托盘。理想情况下，产品托盘应该按第一家店铺的托盘放在挂车中最容易访问的位置。

## 改善体验

运输服务团队希望我们检查可用的数据，看看是否有更智能的方法来解决这个问题。例如，如果有一种方法可以通过确定驾驶员应该访问商店的顺序来预先确定最佳路线，那会怎样呢？

这与“[旅行推销员问题](https://blog.route4me.com/traveling-salesman-problem/)”(TSP)类似，在这个假设问题中，一个推销员得到了一份要访问的城市列表，需要弄清楚它们之间最有效的路线。虽然 TSP 的编码实现可以变得相当复杂，但我们可能能够使用 Apache Cassandra 的[向量搜索](https://www.datastax.com/guides/what-is-vector-search?filter=%7B%7D&utm_source=thenewstack&utm_medium=byline&utm_campaign=vector-search&utm_term=all-plays&utm_content=etailers-journey)功能来解决这个问题。

显而易见的方法是绘制每个目的地城市的每个地理位置坐标。然而，这些城市只分布在一个本地都市圈内，这意味着纬度和经度的整数部分大多相同。这不会导致易于检测的变化，所以我们应该通过只考虑[地理 URI 模式](https://wiki.openstreetmap.org/wiki/Geo_URI_scheme)小数点右侧的数字来重新关注该数据。

例如，Rogersville(BigBoxCo 商店位置之一)的地理 URI 为 45.200，-93.567。如果我们查看每个坐标的小数点右侧，到达调整后的坐标 200，-567(而不是 45.200，-93.567)，我们将能够更容易地从这个和其他向量中检测出变化。

对我们商店所在的本地都市圈城市采用这种方法，我们得到以下数据：

![](https://cdn.thenewstack.io/media/2023/08/e55fe5ce-image1.jpg)
*表1 - 每个拥有 BigBoxCo 商店的城市以及 Farley 配送中心的调整后的地理URI方案坐标。*

有了这样简化的坐标列表，让我们看看如何使用它们。

## 实现

现在我们有数据了，我们可以在 Cassandra 集群中创建一个二维向量表。我们还需要在向量列上创建一个附加的二级索引(SASI):

```sql
CREATE TABLE bigbox.location_vectors (
    location_id text PRIMARY KEY，
    location_name text，
    location_vector vector<float， 2>);
CREATE CUSTOM INDEX ON bigbox.location_vectors (location_vector) USING 'StorageAttachedIndex';
```

这将使我们能够使用矢量搜索来确定访问每个城市的顺序。但是，需要注意的是，向量搜索基于余弦的距离计算，假设这些点在平面上。我们知道，地球不是平面。在大地理区域计算距离应该使用哈弗森公式等其他方法，它考虑到球体的特性。但对于我们在一个小的本地都市圈的目的，计算近似最近邻(ANN)应该能很好地工作。

现在让我们将城市向量加载到表中，这样我们应该可以查询它：

```sql
INSERT INTO bigbox.location_vectors (location_id， location_name， location_vector) VALUES ('B1643'，'Farley'，[86， -263]);

INSERT INTO bigbox.location_vectors (location_id， location_name， location_vector) VALUES (B9787，'Zarconia'，[37， -359]);  

INSERT INTO bigbox.location_vectors (location_id， location_name， location_vector) VALUES (B2346，'Parktown'，[-52， -348]);

INSERT INTO bigbox.location_vectors (location_id， location_name， location_vector) VALUES ('B1643'，'Victoriaville'，[94， -356]);

INSERT INTO bigbox.location_vectors (location_id， location_name， location_vector) VALUES ('B6789'，'Rockton'，[11， -456]);

INSERT INTO bigbox.location_vectors (location_id， location_name， location_vector) VALUES ('B2345'，'Maplewood'，[73， -456]);

INSERT INTO bigbox.location_vectors (location_id， location_name， location_vector) VALUES ('B5243'，'Rogersville'，[200， -567]);
```

要开始一个路线，我们首先要考虑 Farley 的仓库配送中心，我们将其存储为一个[86，-263]的向量。我们可以通过查询 location_vectors 表来获取 Farley 向量的近似最近邻开始：

```sql
SELECT location_id， location_name， location_vector， similarity_cosine(location_vector，[86， -263]) AS similarity
FROM location_vectors
ORDER BY location_vector
ANN OF [86， -263] LIMIT 7;
```

查询的结果如下:

```markdown
 location_id | location_name | location_vector | similarity
-------------+---------------+-----------------+------------
       B1643 |        Farley |      [86， -263] |          1
       B5243 |   Rogersville |     [200， -567] |   0.999867
       B1566 | Victoriaville |      [94， -356] |   0.999163
       B2345 |     Maplewood |      [73， -456] |   0.993827
       B9787 |      Zarconia |      [37， -359] |   0.988665
       B6789 |       Rockton |      [11， -456] |   0.978847
       B2346 |      Parktown |     [-52， -348] |   0.947053

(7 rows)
```

注意，我们还包括了 `similarity_cosine` 函数的结果，以便我们可以看到 ANN 结果的相似度。如我们所见，在顶部忽略 Farley(我们的起点 100% 匹配)后，Rogersville 城被返回为近似最近邻。

接下来，让我们构建一个微服务端点，该端点基本上根据起始点和返回的顶部 ANN 遍历城市。它还需要忽略它已经去过的城市。因此，我们构建一个可以 POST 到的方法，以便我们可以在请求正文中提供起始城市的 ID 以及建议路线中的城市列表：

```bash
curl -s -XPOST http://127.0.0.1:8080/transportsvc/citylist/B1643 \-d'["Rockton"，"Parktown"，"Rogersville"，"Victoriaville"，"Maplewood"，"Zarconia"]' -H 'Content-Type: application/json'
```

使用 location_id “B1643”(Farley)调用此服务会返回以下输出：

```json
["Rogersville"，"Victoriaville"，"Maplewood"，"Zarconia"，"Rockton"，"Parktown"]
```

所以这在为我们的卡车路线提供一些系统性指导方面效果很好。但是，我们的服务端点和(通过代理)我们的 ANN 查询并不了解连接每个城市的高速公路系统。目前，它简单地假设我们的卡车可以直接“笔直”前往每个城市。

现实情况是，我们知道事情并非如此。事实上，让我们看一看地图，上面标出了我们都市圈的每个城市和连接的高速公路(图1)。

![](https://cdn.thenewstack.io/media/2023/08/d93f8658-screenshot-2023-08-10-at-12.31.56-pm.png)
<!-- 图1 - 我们当地都市圈的地图，显示了每个拥有BigBoxCo商店的城市以及连接的高速公路系统。每条高速公路都显示了它们的名称，用不同的颜色进行了区分。 -->

这里增加准确度的一种方法是为高速公路段创建向量。事实上，我们可以创建一个高速公路表，并根据它们与彼此和我们的城市的交叉点生成每个高速公路段的向量。

```sql
CREATE TABLE highway_vectors (
    highway_name TEXT PRIMARY KEY，
    highway_vector vector<float，4>);

CREATE CUSTOM INDEX ON highway_vectors(highway_vector) USING 'StorageAttachedIndex';
```

然后，我们可以为每条高速公路插入向量。我们还将为高速公路段的每个方向创建条目，以便我们的 ANN 查询可以使用任一城市作为起点或终点。例如:

```sql
INSERT INTO highway_vectors(highway_name，highway_vector)
VALUES('610-E2'，[94，-356，86，-263]);
INSERT INTO highway_vectors(highway_name，highway_vector)  
VALUES('610-W2'，[86，-263，94，-356]);
```

根据我们的原始查询结果，我们可以运行另一个查询来获取 Farley(86，-263)和Rogersville(200，-567)坐标的高速公路向量的近似最近邻：

```sql
SELECT * FROM highway_vectors
ORDER BY highway_vector
ANN OF [86，-263，200，-567]
LIMIT 4;

 highway_name | highway_vector  
--------------+-----------------------
       610-W2 |  [86， -263， 94， -356]
         54NW | [73， -456， 200， -567]
        610-W |  [94， -356， 73， -456]
        81-NW |  [37， -359， 94， -356]

(4 rows)
```

如果我们看图 1 所示的地图，我们可以看到 Farley 和 Rogersville 确实通过 610 号和 54 号高速相连接。我们正在取得进展!

我们可以构建另一个服务端点，根据起始和终点城市的坐标在两城市之间建立高速公路路线。为了真正完成这个服务，我们还需要它消除任何“孤立”的返回高速公路(不在我们预期路线上的高速公路)，并包括我们可能要在路上停靠的任何有商店的城市。

如果我们使用 Farley(B1643)和 Rogersville(B5243)的 location_id，我们应该得到这样的输出：

```bash
curl -s -XGET http://127.0.0.1:8080/transportsvc/highways/from/B1643/to/B5243 \-H 'Content-Type: application/json'

{"highways":[
    {"highway_name":"610-W2"， 
        "Highway_vector":{"values":[86.0，-263.0，94.0，-356.0]}}，
    {"highway_name":"54NW"，
        "highway_vector":{"values":[73.0，-456.0，200.0，-567.0]}}，
    {"highway_name":"610-W"，
        "highway_vector":{"values":[94.0，-356.0，73.0，-456.0]}}]，
 "citiesOnRoute":["Maplewood"，"Victoriaville"]}
```

## 结论和下一步

这些新的运输服务对我们的司机和 DC 管理来说应该是一个巨大的帮助。他们现在应该会在店与店之间获得数学意义上的路线的确定结果。一个好的附带效益是 DC 员工也可以更高效地加载货物。有了提前的路线，他们可以使用后进先出(LIFO)的方法将托盘装载到卡车上，利用更多的可用空间。

虽然这是迈出的第一步，但如果这个计划被证明是成功的，我们可以进行一些未来的改进。订阅交通服务将有助于路线规划和改造。这将允许根据一个或多个高速公路上的重大本地交通事件重新计算路线。

我们还可以使用 n 向量方法进行坐标定位，而不是使用缩写的纬度和经度坐标。这里的优势是我们的坐标已经转换为向量，这可能会导致更准确的近似最近邻近似。

查看这个 GitHub 存储库获取上述描述的[示例运输服务端点的代码](https://github.com/aar0np/CustomerPromotionVectorSearch/tree/main/src/main/java)，并了解 [DataStax 如何使用矢量搜索实现生成式 AI](https://www.datastax.com/?utm_source=thenewstack&utm_medium=byline&utm_campaign=vector-search&utm_term=all-plays&utm_content=etailers-journey)。