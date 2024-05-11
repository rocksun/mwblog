
<!--
title: 为什么Apache Cassandra 5.0是游戏规则的改变者？
cover: https://cdn.thenewstack.io/media/2024/05/76972a90-cassandra2.png
-->

新功能为团队提供了一个特别诱人的游乐场，可以进行有趣且开创性的工作，包括生成式 AI 计划。

> 译自 [Why Apache Cassandra 5.0 Is a Game-Changer for Developers](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/)，作者 Anil Inamdar。

开源 Apache Cassandra 5.0 的发布，[现已进入公开测试阶段，预计很快将进入 GA 阶段](https://cassandra.apache.org/_/index.html)，增加了多项功能，使 NoSQL 数据库对企业的关键任务用例更具吸引力。从开发人员的角度来看，这些新功能为团队提供了一个特别诱人的平台，可以开展有趣且开创性的工作，当然也包括生成式 AI 计划。

Cassandra 5.0 还对开发人员体验本身进行了一些改进，使开发人员使用数据库时更加高效——坦率地说，也更愉快。

## 最适合开发人员的 Cassandra

Apache Cassandra 项目背后的活跃[开源](https://thenewstack.io/open-source/) 社区将开发人员的易用性作为优先事项。例如，新的存储附加索引 (SAI) 功能允许开发人员对非主键列创建更有效的查询，并使用辅助索引，其开销和复杂性低于以前版本。

Cassandra 5.0 改进的工具和护栏还使开发人员能够在管理数据时以更高的安全性和控制力更快地工作。这些新的护栏可以防止可能导致错误配置的操作，并设计了其他限制，以简化数据一致性的维护。另一个示例是，新添加的用于监视系统低点的虚拟表使开发人员能够更好地完成工作。

值得注意的是，Cassandra 承诺继续这一趋势，以改善其开发人员体验：Cassandra 5.1 预计将增加对 ACID 事务的支持。这将启用类似 SQL 的功能，并降低进入门槛，以便[习惯于关系数据库的开发人员](https://thenewstack.io/4-forecasts-for-the-future-of-developer-relations/) 可以感到宾至如归。

## 更平缓的学习曲线和更简单的迁移坡道

随着 Cassandra 5.0 的新功能激发更多采用，开发人员会发现仍然存在学习曲线需要克服，但与以前版本相比，这个曲线并不那么陡峭。我预计开发人员会相对较快地将 Cassandra 5.0 引入开发和测试环境，这反过来将使部署更快地进入生产环境。

Cassandra 5.0 将吸引首次寻求迁移到该数据库的人员，开发人员还将发现大量可利用的资源。[Apache Cassandra 5.0 网站](https://cassandra.apache.org/_/Apache-Cassandra-5.0-Moving-Toward-an-AI-Driven-Future.html) 提供了广泛的文档，以及与 Cassandra 社区互动用的论坛。邮件列表、市政厅、贡献者会议和其他活动也提供了深入了解最佳实践的宝贵机会。

## 扩展用例

[Planet Cassandra](https://planetcassandra.org/) 是开发人员可以探索以研究现有用例和策略的另一宝贵资源。传统上，Cassandra 在可扩展 Web 应用程序以及利用数据库强大的写入吞吐量和处理海量数据的能力的消息传递和监视系统等用例中表现出色。Cassandra 5.0 继续提供这些优势并支持这些用例，同时还引入了将在其他几个方面扩展其使用范围的功能。

其中最重要的可能是，Cassandra 5.0 添加了本机向量索引——一种用于处理嵌入向量的新的向量数据类型——以及相关的新的 Cassandra 查询语言函数，现在将数据库定位为 AI 工作负载的理想选择。[从事 AI 应用用例的开发人员](https://thenewstack.io/the-developer-case-for-using-tim-berners-lees-solid/) 需要一个可扩展且高性能的向量数据库来处理赋予 AI 模型其智能所需的大量“智能数据”，最大程度地减少幻觉并提供可靠的体验。Cassandra 5.0 现在提供了智能数据基础设施开发人员所寻求的，Apache Cassandra 项目本身承认其正在向 AI 驱动的未来迈进。

Cassandra 5.0 的另一项新增功能是存储附加索引 (SAI)，它增强了对多种数据类型的索引，包括一些与 AI 使用案例相关的数据类型，例如向量搜索和全文搜索。SAI 通过同时处理多个列索引而提高了 Cassandra 查询性能，同时不会影响可扩展性。因此，SAI 充当高级过滤引擎，减少了维护多个特定于查询的表的需求，从而支持数据建模和客户端应用程序的使用，同时减少数据副本（因此使用更少的磁盘空间并简化数据安全性）。

SAI 还使 Cassandra 5.0 成为一种特别通用且强大的索引解决方案，它可以出色地处理临时查询和高基数或低基数数据，即使在处理意外或不断变化的查询模式时也能提供卓越的性能。

最后，Cassandra 5.0 使开发人员能够利用 NoSQL 的灵活性，同时满足当今最数据密集型企业应用程序的严苛要求。毫无疑问，Cassandra 5.0 比以往任何时候都更能支持涉及更复杂的分析和事务应用程序的用例。
