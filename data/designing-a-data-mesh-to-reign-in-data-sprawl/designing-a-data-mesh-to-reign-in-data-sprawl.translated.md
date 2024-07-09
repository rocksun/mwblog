# 设计数据网格以控制数据蔓延

![数据网格设计以控制数据蔓延的特色图片](https://cdn.thenewstack.io/media/2024/07/464d562a-data-mesh-reign-data-sprawl-1024x576.jpg)

我尽可能地喜欢[接听客户电话](https://thenewstack.io/want-killer-features-foster-dev-user-communication/)。我喜欢听后端团队在做什么，他们在构建什么，什么有效，什么无效。他们正在考虑什么策略，他们放弃了哪些代码语言，他们正在努力解决什么问题以及他们正在探索什么解决方案。

我喜欢这些电话，因为我总是充满好奇。看到不同的开发人员采用各种方法来解决类似的问题，这很有趣。我也喜欢这些电话，因为我是一个未来主义者（也称为“急躁”）。我迫不及待地想看看各种文本编辑器热潮中会涌现出哪些趋势。我坚信，最好的代码是尚未编写的代码。

最近在对话中越来越频繁地出现的一个趋势是数据网格。为了摆脱单体架构并创建更敏捷的数据访问，公司采用了微服务来解锁消费者/生产者访问权限并加快应用程序开发。但这样做也无意中造成了蔓延。运营数据变得越来越分散，为了控制它，越来越多的团队将数据网格视为解决方案。

我将从数据网格及其历史背景开始，然后分享一些关于为您的组织创建强大的数据网格基础的建议。

## 什么是数据网格？

数据网格是一种分散的数据架构——本身是软件架构的一个子类别——旨在帮助企业变得更加数据驱动。

正如我的同事[Rajoshi Ghosh](https://www.linkedin.com/in/rajoshighosh/) 所描述的那样，“[数据网格背后的理念](https://hasura.io/blog/graphql-and-the-data-mesh-developer-productivity-in-an-age-of-exploding-data?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=why-data-mesh-demands-more-attention)是创建一个架构，通过将数据视为产品并实施开放标准化来解锁对越来越多的分布式域数据集的访问，从而实现可互操作的分布式数据产品的生态系统。”

## 数据网格的历史

数据网格主要由[ThoughtWorks](https://en.wikipedia.org/wiki/Thoughtworks)的[Zhamak Dehghani](https://www.linkedin.com/in/zhamak-dehghani/)于 2019 年发明。ThoughtWorks 是一家有影响力的科技公司，其首席科学家[Martin Fowler](https://www.linkedin.com/in/martin-fowler-com/)帮助在 2001 年创造了另一个软件领域的重大理念——[敏捷开发](https://thenewstack.io/heres-what-a-software-architect-does-in-an-agile-team/)。敏捷是微软 Windows XP 在 2001 年发布后对极限编程 (XP) 的重新命名。与 XP 一样，敏捷也被定义为一组指导“原则”，但去掉了 XP 的实现细节。

虽然数据网格更像是敏捷的弟弟，而不是后代，但它也以 ThoughtWorks 的“家庭风格”被定义为一组模糊的原则。数据网格也是领域驱动设计 (DDD) 的后代，由软件设计顾问 Eric Evans 于 2003 年创建。与数据网格一样，DDD 也建议去中心化，尽管更多的是在软件团队及其流程的组织方式上，而不是在软件产品本身。

除了软件设计理论的历史之外，还有软件设计现实的历史，尤其是在数据系统的设计方面。一个标志着近期数据系统历史开端的良好候选者是大数据和[云计算](https://thenewstack.io/cloud-native/) 的兴起，大约在 2010 年。云计算和商品硬件加速了基础设施成本的下降趋势，降低了生成和存储数据的成本。智能手机和广告网络充分利用了新增的容量，产生了比以往任何时候都大得多的数据量。当时使用的标准数据处理工具——[数据仓库、数据集市和数据立方体](https://aws.amazon.com/what-is/data-mart/)——建立在已有数十年历史的技术之上。即使在计算总和和平均值等简单情况下，它们也难以处理这些海量数据。
这个新时代被称为“大数据”，专门的横向扩展 NoSQL 数据处理系统（如 Apache Hadoop 和 Apache Spark）应运而生，以处理来自智能手机和广告网络的海量数据。这些工具解决问题的一个关键方法是“将计算推送到数据”。将计算推送到数据是一项艰巨的技术挑战，这有助于推动数据的集中化，因为第一个通用横向扩展 SQL 软件解决方案，[AWS](https://aws.amazon.com/?utm_content=inline+mention) Redshift 和 [Google](https://cloud.google.com/?utm_content=inline+mention) [BigQuery](https://en.wikipedia.org/wiki/BigQuery)，五年后才变得可用。

这些因素保留甚至加剧了数据系统中现有的集中化偏见，所有这些都是由技术驱动和决定的。从上一代垂直扩展的数据仓库到当前一代横向扩展的数据仓库，再到为 Hadoop 和 Spark 批处理作业分析提供数据的提取-转换-加载 (ETL) 管道，这些都是需要特定技能的专门技术，因此需要集中化。

集中化的趋势仍在继续，但随着数据技术的不断发展，对专业化的需求已经放缓。像 AWS Redshift [Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) 和 AWS [Athena](https://aws.amazon.com/what-is/presto/) 这样的产品彻底分离了计算和存储，在对象存储中的异构数据上提供了 SQL 接口，降低了对转换（“ETL”中的“T”）的需求，并鼓励将原始数据转储到 AWS S3、Google Cloud Storage 或 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure Blob Storage 中的数据湖中。下一代数据仓库，如 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 和 ClickHouse，通过完全消除对专门的数据仓库模式设计的需求，延续了这一趋势。

专业化只是推动集中化的力量之一。其他因素包括数据治理、数据管理以及任何替代方案的技术障碍。这将我们带到了 2019 年，为数据网格奠定了基础。

Dehghani 确定了推动去中心化的反作用力，将其阐述为线索并将其编织成一个叙述。然后，她将这个叙述与 DDD 和微服务等先前的大想法联系起来，敦促从业人员克服涉及数据治理、管理等的障碍，提炼出一套指导原则，并将整个包命名为“数据网格”。

她概述的四个指导原则是：

**领域所有权：**根据业务部门划分数据架构，并将这些组件的责任分配给这些业务部门。**数据作为产品：**将这些业务部门对其数据组件的责任提升，要求他们对数据的质量水平与对任何产品的质量水平相同。**自助数据平台：**为这些业务部门提供软件和硬件基础设施，使他们能够履行其提升的责任。**联邦计算治理：**促进协作，以便可以最佳地将遵守治理政策的责任在这些业务部门和中央机构之间共享。
然而，她没有给出具体的实施细节和关于如何*获得*数据网格的可操作建议。*这*将我们带到了 2024 年，为当前的（数据）网格状态奠定了基础。

## 将技术与数据网格原则相一致
在用于实现数据网格的技术中，自助平台是必不可少的。这可以沿着两个维度进行分析：数据是什么，以及如何提供数据。

### 数据
数据通常分为两大类：运营数据和分析数据。

- 运营数据包括传统的联机事务处理 (OLTP) 数据，用于促进正在进行的业务功能，需要低延迟和高最新性，允许低容量，并且包含读写操作的混合。
- 分析数据涉及传统的联机分析处理 (OLAP) 数据，用于决策支持，需要高容量，允许高延迟和低最新性，并且仅包含读取操作。
### 服务
提供数据通常使用查询语言或 API 进行。

- 查询语言是一种通用的、高度灵活的、高表达性的语言，它在一个操作中表示临时数据请求的全部意图。它通常用于 OLAP over OLTP，并为决策支持和商业智能 (BI) 系统提供支持，例如 SQL。
- API 是专门的、高度不灵活的、低表达性的远程过程调用 (RPC) 集，它表示预先确定的数据请求，通常用于 OLAP over OLTP，并为桌面和移动应用程序提供支持，例如 REST
数据网格可以覆盖操作数据、分析数据或两者。因此，数据网格可以由查询语言、API 或两者提供支持。候选查询语言列表非常短：[SQL](https://roadmap.sh/sql) 和 [GraphQL](https://roadmap.sh/graphql)。候选 API 格式列表同样很短：REST 和 GraphQL。细心的读者会注意到这两个列表中都出现了 GraphQL；稍后会对此进行更多说明。

## 将数据网格变为现实
三种技术应运而生，使数据网格成为现实：数据目录、API 网关和分布式查询引擎。

**数据目录**
诸如 [Atlan](https://atlan.com/)、[Collibra](https://www.collibra.com/) 和 [Amundsen](https://www.amundsen.io/) 之类的  数据目录遵循四个指导原则中的三个：领域所有权、数据作为产品和联邦计算治理。它们往往在第四个原则，即自助数据平台方面有所欠缺。一些数据目录，特别是 [Alation](https://www.alation.com/) 和 [OpenMetadata](https://open-metadata.org/)，确实提供有限的自助数据平台，使用直通 SQL。但是，它们通常缺乏从多个来源混合和连接异构数据的能力，阻碍了它们发展成为成熟的数据网格。

**API 网关**
诸如 [Hasura](https://hasura.io/?utm_content=inline+mention) 和 [Apollo Router](https://www.apollographql.com/docs/router/) 之类的 API 网关往往只关注一个指导原则：自助数据平台。两者都通过选择 GraphQL 来实现这一点，GraphQL 既是查询语言，也是 API 格式。

作为查询语言，GraphQL 的功能可能不如 SQL 强大；但是，它的局限性与其一致性、机器可读性和自描述性相结合，使 GraphQL 成为从多个来源获取异构数据的有效自助数据平台。此外，GraphQL 作为查询语言和 API 格式的双重角色，涵盖了分析 OLAP 数据和操作 OLTP 数据。

GraphQL 和 API 网关往往在领域所有权、数据作为产品和联邦计算治理原则方面有所欠缺。然而，随着 [Hasura Schema Registry](https://hasura.io/blog/breeze-through-collaboration-with-the-hasura-schema-registry)、The Guild 的 [Hive](https://the-guild.dev/graphql/hive) 和 [Apollo Studio](https://studio.apollographql.com/) 的推出，这方面取得了一些进展。

**分布式查询引擎**
不可忽视的是分布式查询引擎，例如 [Trino](https://trino.io/) 和 [PrestoDB](https://prestodb.io/)。它们以更复杂的执行模型为基础，在 Atlan 和 OpenMetadata 等数据目录的简单直通 SQL 之上添加了跨数据库连接、谓词下推和相对高效的查询处理。较大的延迟可能会限制它们在操作数据方面的效用，但至少对于数据网格的分析数据工作负载来说，它们非常有前景。

## 构建理想的数据网格配方
目前，将理论付诸实践的真正数据网格必须从各个部分拼凑而成。市场上很少有（如果有的话）产品能够充分遵循所有四个指导原则。创建数据网格的配方将包括以下两个组件：

**数据目录：**领域所有权、数据作为产品和联邦计算治理需要一套庞大的服务，包括血缘关系、来源、质量指标、文档和协作。到目前为止，只有数据目录真正提供了完整的套件：因此，数据目录是数据网格配方中不可或缺的一部分。**API 网关：**如果操作数据工作负载属于您的数据网格工作负载，那么 [API 网关几乎是“必不可少的”。](https://hasura.io/blog/elevating-your-api-strategy-with-hasura) 很少的选择都使用 GraphQL，因此 GraphQL 也必须出现在您的数据网格配方中。两个领先的选择，Hasura 和 Apollo Router，[可以很好地协同工作](https://hasura.io/blog/accelerate-your-apollo-graphql-federation-journey-with-hasura?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=why-data-mesh-demands-more-attention)，但是只有 Hasura 才能真正为使用 GraphQL 调整现有数据源做好准备。
分布式查询引擎（如 Trino 或 Presto）是增强数据网格自助数据平台的另一种选择，但代价是增加了操作复杂性。

## 总结
从这些组件构建和部署数据网格是一项艰巨的任务，涉及本文介绍范围之外的细节。希望它有助于阐明数据网格的历史，解释它如何在整体数据策略中发挥作用，消除围绕数据网格的一些模糊性，建立关于数据网格的心理模型，并提供具体可行的建议，将数据网格从理论变为实践。
有一点我确信：我们仅仅触及了它的潜力表面。许多人正在认识到它在机器学习、分析或数据密集型应用中的效用，所有这些都成为当今数据生态系统中竞争的必备条件。再次引用 Rajoshi 的话，[使用数据网格](https://hasura.io/blog/graphql-and-the-data-mesh-developer-productivity-in-an-age-of-exploding-data?utm_campaign=the-new-stack&utm_source=the-new-stack&utm_medium=referral&utm_content=why-data-mesh-demands-more-attention)，“组织能够更好地应对数据驱动型应用程序开发不断变化的需求，为数字时代设定了效率的新标准。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看所有播客、访谈、演示等。