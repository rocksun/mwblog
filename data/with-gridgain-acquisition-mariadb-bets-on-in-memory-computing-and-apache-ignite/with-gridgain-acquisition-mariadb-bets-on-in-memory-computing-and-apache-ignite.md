<!--
title: MariaDB 收购 GridGain，押注内存计算和 Apache Ignite
cover: https://cdn.thenewstack.io/media/2026/03/50c6c1f0-a-stylised-computer-expansion-card.jpg
summary: MariaDB 收购 GridGain，旨在将关系型数据库与 GridGain 的内存计算平台（包括 Apache Ignite）结合。此举旨在解决 AI 应用面临的“AI 延迟鸿沟”，通过内存处理实现更快的数据访问，简化开发人员技术栈，以应对现代 AI 工作负载对实时数据的需求。
-->

MariaDB 收购 GridGain，旨在将关系型数据库与 GridGain 的内存计算平台（包括 Apache Ignite）结合。此举旨在解决 AI 应用面临的“AI 延迟鸿沟”，通过内存处理实现更快的数据访问，简化开发人员技术栈，以应对现代 AI 工作负载对实时数据的需求。

> 译自：[With GridGain acquisition, MariaDB bets on in-memory computing and Apache Ignite](https://thenewstack.io/with-gridgain-acquisition-mariadb-bets-on-in-memory-computing-and-apache-ignite/)
> 
> 作者：Paul Sawers

[MariaDB](https://mariadb.com/) 是开源数据库领域的坚定支持者之一。在 [2010 年](https://www.crn.com/news/components-peripherals/222600081/oracle-sun-acquisition-a-done-deal) Oracle 收购 Sun Microsystems 后，从 MySQL 分支项目诞生，十多年来一直是网络应用和企业系统的基石。

但数据库的需求正在发生变化。随着公司试验人工智能系统和所谓的“智能代理应用”（能够规划任务并查询企业数据），开发人员遇到一个屡见不鲜的限制：许多支撑业务系统的数据库设计于一个毫秒级响应时间被认为足够快，而人工智能工作负载闻所未闻的时代。

MariaDB 相信它有办法解决这个问题。周一，该公司[宣布](https://mariadb.com/newsroom/press-releases/mariadb-to-acquire-gridgain-architecting-the-real-time-foundation-for-the-agentic-enterprise/)已同意收购 [GridGain Systems](https://www.gridgain.com/)，该公司是商业 GridGain 内存计算平台背后的公司，也是开源 [Apache Ignite](https://ignite.apache.org/) 项目的原始创建者。这笔交易将结合 MariaDB 的关系型数据库与 GridGain 的内存数据处理技术，以支持依赖更快访问大型数据集的人工智能应用。

## 应对“AI 延迟鸿沟”

随着开发人员试验人工智能驱动的软件，一个新兴的挑战是应用程序检索和更新数据的速度。[Vikas Mathur](https://www.linkedin.com/in/v-mathur/)，MariaDB 的首席产品官，告诉 *The New Stack*，许多组织不愿让 AI 代理直接与操作型数据库交互，因为大量的自动化查询可能会使仍在运行核心业务应用程序的系统不堪重负。

Mathur 说，困难源于企业数据当前的存储方式，重要的数据集分散在不同的系统中，而 AI 工具很少被允许直接访问。

> “要构建有效的人工智能应用程序，你需要实时数据来为代理提供上下文。”

Mathur 说：“要构建有效的人工智能应用程序，你需要实时数据来为代理提供上下文。如今，这些数据通常分散在遗留的孤岛中，而且 AI 往往无法访问；组织担心代理推送繁重的读取查询会减慢或导致现有关键任务企业应用程序崩溃。这意味着由于技术脆弱性和这些组织限制，在生产中大规模部署智能代理应用程序几乎是不可能的——这就是 AI 延迟鸿沟。”

他说，结果是，由于基础设施难以跟上代理生成请求的量，在生产环境中部署人工智能系统可能会变得困难。

因此，MariaDB 正在押注将其关系型数据库与 GridGain 的内存计算层配对可以解决这个问题。该层旨在快速响应大量请求，而 MariaDB 则继续处理企业数据库所期望的持久存储和事务保证。

## 内存计算为何重要

GridGain 的技术根源可追溯到 [Apache Ignite](https://thenewstack.io/apache-streaming-projects-exploratory-guide/)，一个大约在 2014 年在内部开发并捐赠给 Apache Software Foundation 的开源分布式数据库和缓存系统。

Ignite 旨在直接在内存中处理大量数据，而不是从磁盘检索。对于从事 AI 系统的开发人员来说，这种架构很重要，因为代理在执行任务时通常会维护上下文信息并反复查询底层数据集。

Mathur 表示，将这些信息保存在内存中，可以使 AI 代理快速访问上下文，并在交互过程中保持状态。

Mathur 说：“有了内存层，代理可以在亚毫秒级内访问其上下文。这使得代理更容易更新长期上下文，而不是每次都重建该上下文。”

MariaDB 表示，这种结合可以使开发人员运行更直接地与操作型企业数据交互的 AI 应用程序，同时保持传统关系型数据库的持久性保证。

[Lalit Ahuja](https://www.linkedin.com/in/lahuja/)，GridGain 的首席技术官，表示此次收购旨在将高速内存处理更接近企业已经依赖的事务数据数据库。

Ahuja 在一份声明中说：“如今的企业无法承受由数据孤岛架构引入的延迟。有了 MariaDB 和 GridGain，企业客户将获得一个统一的平台，在不放弃持久性的情况下提供高性能。”

## 为开发人员提供更简单的技术栈？

MariaDB 的另一个卖点侧重于复杂性。如今构建 AI 系统的开发人员通常依赖于多种不同的技术：用于事务数据的关系型数据库、用于嵌入的向量数据库、用于加速查询的缓存层以及用于编排的额外工具。

Mathur 表示，这种安排可能导致开发人员需要将多个系统拼接起来，以维护应用程序状态并检索相关信息。

他说：“MariaDB 可以通过将向量数据类型、向量索引和向量搜索嵌入到我们的核心数据库存储引擎中来完成连接各层的繁重工作，”并补充说 GridGain 的内存技术将提供该架构的另一部分。“通过收购 GridGain 的协议，开发人员可以将缓存层与数据库紧密结合，提供统一、集成的方法。”

凭借 MariaDB 和 Apache Ignite 各自的开源基础，组织当然可以在自己的环境中运行这些软件。然而，该公司计划通过托管云服务提供组合平台，称这可以减少开发团队的运营负担。

当被问及此次收购对 Apache Ignite 社区意味着什么时，MariaDB 表示计划继续与 Apache Software Foundation 合作，但没有具体说明该项目未来方向的任何具体承诺。

Mathur 说：“[MariaDB Community Server](https://mariadb.com/products/community-server/) 仍然是我们创新的主要引擎，也是我们生态系统的基础。我们致力于确保它是现代应用程序最可靠的开源数据库，并期待与 Apache Software Foundation 合作，共同塑造 Apache Ignite 的未来。”

值得注意的是，MariaDB 公司近年来经历了动荡。该公司于 [2022 年](https://www.theregister.com/2022/12/21/mariadb_uses_spac_to_begin/) [通过 SPAC 合并](https://www.theregister.com/2022/12/21/mariadb_uses_spac_to_begin/)上市，随后于 [2024 年](https://techcrunch.com/2024/09/10/mariadb-goes-private-with-new-ceo-as-k1-closes-acquisition/)[被](https://techcrunch.com/2024/09/10/mariadb-goes-private-with-new-ceo-as-k1-closes-acquisition/)投资公司 K1 Investment Management 私有化。大约在同一时间，[Rohit de Souza](https://www.linkedin.com/in/rohit-de-souza-42b3871/) 接任首席执行官，这标志着重新关注重建与开源社区的联系并完善公司的产品战略。

这种方法是否能引起开发人员的共鸣仍有待观察。近年来，数据库基础设施领域变得拥挤，超大规模云提供商提供自己的数据服务，同时专业 AI 数据平台的生态系统也在不断发展。

尽管如此，MariaDB 似乎正在押注，熟悉的关系型基础与更快的内存处理相结合，可能会吸引那些试图将 AI 系统连接到已存在于企业数据库中的大型数据集的组织。