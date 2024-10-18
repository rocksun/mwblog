
<!--
title: 为什么 NoSQL 部署无法扩展？
cover: https://cdn.thenewstack.io/media/2024/10/963d1ed9-leif-christoph-gottwald-im8dxcck1sy-unsplash-scaled.jpg
-->

NoSQL 在规模化方面存在困难，而分布式 SQL 提供了更强大的解决方案。

> 译自 [Why NoSQL Deployments Are Failing at Scale](https://thenewstack.io/why-nosql-deployments-are-failing-at-scale/)，作者 Sunny Bains。

为什么技术会过时？没有一个统一的答案。有时，它会被更好的东西取代。其他时候，是潜在的需求发生了变化。服务于新兴市场需求的技术，在市场成熟时可能被证明是不够的。

这就是许多企业对 [NoSQL](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/) 的发现。这也是为什么今天这么多 NoSQL 实现都在苦苦挣扎的原因。

不久之前，在大数据的早期，Hadoop 是每个人都在谈论的名字。传统的基于 SQL 的数据存储被认为已经过时。每家获得风险投资的初创公司似乎都在使用 NoSQL 键值存储。他们追随着谷歌、Facebook 和雅虎等科技巨头的脚步，这些公司开发了 NoSQL 技术来管理其快速增长。初创公司自然而然地会使用那些推动其前辈取得全球成功的工具。

但奇怪的事情发生了。那些成功的初创公司开始抛弃他们的 NoSQL 数据库。

以 HBase 为例，它是一个作为标准 Apache Hadoop 包的一部分分发的数据库。HBase 以谷歌著名的 BigTable 为模型，其流行度在几年内飙升，然后稳步下降。

![](https://cdn.thenewstack.io/media/2024/10/714b4c9f-picture1.png)

看看上面的图表，人们可能会认为在 2017 年，出现了一个新的数据库来取代 HBase——也许是一个 [存储和访问](https://thenewstack.io/leveraging-web-workers-to-safely-store-access-tokens/) 数据更快或可以处理更多信息的数据库。但事实并非如此。HBase 仍然是存储和检索数据的最佳选择。它受欢迎程度的下降与它的原始能力无关。这与它的用户试图解决的问题的复杂性有关。

在 SaaS 和大数据的早期，初创公司忙于跟上客户增长的步伐。他们需要一种廉价的 [方式来存储和管理大量](https://thenewstack.io/5-ways-ai-improves-knowledge-management/) 的高速数据。像 HBase 这样的 NoSQL 工具很好地填补了这一角色。但是查询这些数据呢？保持数据的一致性呢？这些都是以后要解决的问题。

最终，那个时候到来了。当它到来的时候，很明显，建立在 NoSQL 基础上的公司存在着巨大的维护问题。他们在编写查询时遇到了麻烦。数据变得不可靠。新的 [应用程序越来越难构建](https://thenewstack.io/how-to-build-applications-over-streaming-data-the-right-way/)。NoSQL 最初非常划算，但随着业务变得越来越复杂，它开始 *增加* 成本。

此时，许多运行 HBase 的公司已经不再是初创公司。他们已经扩展到全球各地。他们创建了其他人用来建立企业的平台。他们正在招聘数据分析师。他们开始考虑停机时间和 SLA。他们不再仅仅是试图保留数据。他们试图利用它。

就在那时，NoSQL 的局限性变得明显起来，并成为一个真正的问题。

对于 HBase 来说，这些局限性包括：

*   **缺乏事务支持：** 这意味着用户无法获得现代关系数据库典型的 ACID 属性。数据可能会损坏或逻辑上不一致。拥有的数据越多，当数据质量下降时，就越难通过蛮力找到问题。
*   **缺乏二级索引：** HBase 缺乏二级索引意味着所有内容都必须通过蛮力扫描来查找。当您不需要查找数据时，这不是问题。当您拥有相对较少量的数据时，这不是问题。但是，当您需要在 TB 级别的海量数据中找到一根针时，缺乏二级索引会使每个查询的计算成本都很高。
*   **单点故障：** HBase 使用 HDFS 文件系统（及其集中式 NameNode 目录）会造成依赖关系，使其极易受到崩溃的影响。
*   **不友好的界面：** NoSQL 缺乏关系架构在快速存储数据方面是一个优势，但在查询数据时却是一个根本问题。NoSQL 并没有消除对关系模式的需求。它只是将负担强加给了应用程序，而应用程序的维护要困难得多，成本也高得多。使用数据结构更改显式 SQL 数据库模式比修改嵌入在应用程序中的隐式模式要容易得多。

随着时间的推移，这些在规模上运行 NoSQL 的基本问题变得不容忽视。一些人试图找到折衷方案。较新的 NoSQL 数据库试图在 HBase 的键值架构上构建结构层，并添加具有 SQL 或类 SQL 功能的事务。

正如麻省理工学院的 Michael Stonebreaker [所说](https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf)：“尽管强烈反对 SQL 很糟糕，但在 2010 年代末，几乎所有 NoSQL DBMS 都添加了 SQL 接口。” 他补充道：“许多剩余的 NoSQL DBMS 也添加了强一致性 (ACID) 事务。因此，NoSQL 的信息已经从‘不要使用 SQL——它太慢了！’变成了‘不仅限于 SQL’（即，SQL 对于某些事情来说是可以的）。”

随着时间的推移，NoSQL 产品变得越来越像 RDBMS 产品。但本质区别依然存在。根据定义，NoSQL 解决方案缺乏模式。这既是它们的优势，也是它们的劣势。没有数据模式可以实现快速存储和检索。这也使得分析和事务更加困难。如果模式没有在数据库中实现，则必须在查询中实例化。例如，如果需要将数据分片到不同的服务器上，则必须在应用程序代码中反映这种变化。一些 NoSQL 解决方案允许在外部定义模式，但这种方法在实践中容易出错。模式迁移是脆弱的、令人头疼的操作。

更改数据库的困难阻碍了新的应用程序开发。这使得创新变得更加困难，很少有企业能够长期容忍这种情况。

Pinterest 就是一个很好的例子。它是 HBase 的早期采用者之一。根据 Pinterest Engineering 的一篇[博客文章](https://medium.com/pinterest-engineering/hbase-deprecation-at-pinterest-8a99e6c8e6b7)，它曾在 HBase 上运行“50 个集群、9000 个 AWS EC2 实例和超过 6 PB 的数据”。HBase 完成了这项工作。但随着时间的推移，随着 Pinterest 的发展，它认为 HBase 的缺点超过了它的优势。它的[功能太少，管理成本太高](https://thenewstack.io/whats-the-future-of-feature-management-feature-flags/)。随着其他企业开始得出相同的结论，找到精通 HBase 的工程师变得越来越难。最终，Pinterest 迁移到了一种名为 TiDB 的开源、兼容 MySQL 的分布式 SQL 解决方案。通过这样做，该公司提高了开发速度和查询延迟，同时使性能更加可预测。

这对某些人来说可能是一个惊喜。多年来，人们一直误以为 SQL 本质上比 NoSQL 慢且效率低。但事实并非如此。云计算和横向扩展的进步使得最近的 SQL 解决方案在原始性能方面更接近于 NoSQL 解决方案，同时仍然提供 RDBMS 的所有优势。分布式 SQL 不再局限于数据库功能的一个方面（存储和检索），而是致力于在广泛的事务和分析用例中提供高性能，这使其对[需求复杂、利益相关者众多](https://thenewstack.io/5-signs-your-business-needs-an-operations-intervention/)的成熟企业具有吸引力。

具有讽刺意味的是，Pinterest 和类似公司从 NoSQL 转向分布式 SQL，就像它们当初采用 NoSQL 一样，是在追随 Google 的脚步。TiDB 和其他分布式 SQL 解决方案是 Google Spanner 的后代。这是 Google 为解决 BigTable 问题而创建的软件，而 BigTable 是催生 HBase 的技术。

在某种程度上，SaaS 行业只是重现了过去二十年来 Google 和其他科技巨头所经历的历程。在这里，我们有一种技术（SQL/RDBMS），据说是被另一种技术（NoSQL）淘汰了，而现在又被它所淘汰的技术的更现代版本所取代。

谁又能说车轮不会再次转动呢？最后一次引用 Stonebreaker 的话，“风水轮流转。新一波的开发者会声称 SQL 和[关系模型]不足以满足新兴应用领域的需求。然后，人们会提出新的查询语言和数据模型来克服这些问题。” 但他指出，没有一个能够真正威胁到基于 SQL 的 RDBMS 的地位。

这是一个有益的提醒，多年来，传统的 relational database 已经证明了自己具有非凡的吸收创新的能力，从集群到[云再到向量搜索](https://thenewstack.io/datastax-adds-vector-search-to-astra-db-on-google-cloud/)。数据库架构的趋势来来去去，但不知何故，当尘埃落定，SQL 似乎总是屹立不倒。
