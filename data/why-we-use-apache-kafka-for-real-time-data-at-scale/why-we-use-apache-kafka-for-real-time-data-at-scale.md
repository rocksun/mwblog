
<!--
title: 为什么我们在规模化实时数据中使用Apache Kafka
cover: https://cdn.thenewstack.io/media/2024/07/8eb38c8c-kafka-real-time-data-scale.jpg
-->

了解网络安全供应商 SecurityScorecard 如何利用数据流来增强其业务能力。

> 译自 [Why We Use Apache Kafka for Real-Time Data at Scale](https://thenewstack.io/why-we-use-apache-kafka-for-real-time-data-at-scale/)，作者 Brandon Brown; Jared Smith。

在一个数字威胁不断演变的世界中，拥有准确的实时数据进行安全扫描至关重要。最新的数据是 [SecurityScorecard](https://securityscorecard.com/) 的生命线。该公司通过利用互联网资源来识别潜在漏洞，包括暴露的服务器、可疑 IP 地址、被盗员工帐户、受恶意软件感染的设备等，为组织提供全面的安全态势视图。

为了跟上不断增加的安全威胁数量，SecurityScorecard 分析了 300 多种问题类型，每天识别出 2000 多亿个安全漏洞。数据收集和处理不仅需要大量数据，还需要准确的、大规模的实时数据。这种需求促使 SecurityScorecard 采用 [数据流](https://www.youtube.com/watch?v=_RcnZ2XfuXw)，并使用 Confluent Cloud 和 Confluent Platform 的组合来构建流数据管道，以更快地扩展并更好地治理数据。

## 用于数据流和处理的实时管道

SecurityScorecard 构建的解决方案从数字来源挖掘数据以识别安全风险。数据流帮助该公司通过在毫秒内分析信息来检测不断变化的威胁，而不是数周或数月。该公司在其平台上构建了开源 [Apache Kafka](https://thenewstack.io/ditching-databases-for-apache-kafka-as-system-of-record/)，因为没有其他系统提供构建所需任何内容的基本工具。

SecurityScorecard 的威胁研究团队过去曾自行管理 Kafka，但每天花费 8 个小时进行维护会分散产品开发时间。该团队依靠 [批处理管道将数据传输](https://thenewstack.io/the-unfortunate-reality-about-data-pipelines/) 到和从 [AWS](https://aws.amazon.com/?utm_content=inline+mention) S3。他们还使用昂贵的基于 REST API 的通信来进行系统之间的数据交换，并使用 RabbitMQ 进行流处理活动。

为了减轻负担，SecurityScorecard 的威胁研究开发团队创建了 [Horus](https://support.securityscorecard.com/hc/en-us/articles/8528362400539-How-SecurityScorecard-collects-data-for-ASI)，这是一个全球分布式系统，能够在 Confluent 之上运行任何基于代理的代码，无论在世界上的任何地方。Horus 使用实时流管道和连接器来处理数据。该团队编写了基于 Python 的应用程序，并将其作为代理部署到此系统中。目前，这些代理已部署在全球各地，以执行诸如 IPv4 扫描、网络爬取、漏洞检测以及与合作伙伴数据源的 API 集成等任务。

自构建 Horus 以来，SecurityScorecard 在流式基础设施方面节省了超过 200 万美元，而这笔钱原本需要用于内部管理开源 Kafka。

除了 Horus 之外，SecurityScorecard 的威胁研究团队还在流式平台上实施了所有 [新系统并刷新了旧系统](https://support.securityscorecard.com/hc/en-us/articles/8528362400539-How-SecurityScorecard-collects-data-for-ASI)。其中一些包括深层和暗网泄露的凭据、泄露密码的集合以及黑客聊天，以及来自 90 多个国家/地区的蜜罐的全球被动传感器数据同步到 Kafka。此外，[BreachDetails](https://support.securityscorecard.com/hc/en-us/articles/19200200869915-Use-BreachDetails-to-respond-faster-to-breaches-in-your-ecosystem)，一个定制的违规事件收集系统，监控公共网络和政府网站以查找数据泄露通知，让客户知道他们的供应商何时遇到安全事件。

## 数据治理和效率的放大

数据治理对 SecurityScorecard 至关重要。该公司使用自定义构建的 Protobuf 库来管理对敏感数据的访问。SecurityScorecard 的目标是使多个团队能够更轻松地共享和治理相同的数据源。Confluent 的 Stream Governance 功能和基于角色的访问控制将允许数据平台团队控制对集群的访问。随着数据治理变得越来越细化，SecurityScorecard 可以将流式传输扩展到更多团队，以增强安全性。

Confluent 在 SecurityScorecard 扫描网络并爬取网页内容的能力中发挥着至关重要的作用，从追踪违规事件的数据库中抽出数十亿条记录。这使得任何团队都可以“重播”数据。完全托管的连接器（包括 PostgreSQL 和 AWS S3 Sink 连接器）可让公司内的团队出于各种目的访问流数据。这些源连接器会创建充当资产历史记录的数据档案并实时将数据源连接在一起，以便在整个企业中实现一致的数据层。

完全托管系统的高效性已经解放了 SecurityScorecard 中的两个全职角色。一项新产品，即攻击面情报 (ASI) 模块，通过 Confluent 聚合了来自 SecurityScorecard 的数 PB 流数据，并通过 Kafka Connect 将其传输到数据接收器，从而允许客户搜索整个互联网，以查找开放端口、易受攻击的机器、威胁行为者、恶意软件和其他信息。另一款产品，即自动供应商检测 (AVD)，会实时处理网络爬虫数据和合作伙伴数据，以提供客户供应链安全性的完整视图，通过数据流突出显示客户与其供应商之间的连接。

## 克服混合云环境中的数据瓶颈

以前，SecurityScorecard 架构团队的首席软件工程师 Brandon Brown 在升级 Kafka 版本和管理 Amazon Managed Streaming (MSK) 运营需求方面遇到了重大挑战。在扩展过程中，这些任务消耗了宝贵的时间，而这些时间本来可以用来开发业务应用程序。

MSK 无法满足 SecurityScorecard 的运营需求，而且像进行版本升级等操作极其困难且需要手动完成。该团队需要搞清楚集群大小，并且在决定设置代理数量时遇到了挑战。

自迁移到 Confluent Cloud 以来，集群和连接器管理等困难任务变得更加简单且可靠。Brown 估计，解决这个运营方程式使他的团队每年节省约 125,000 美元。此次迁移还减轻了额外的运营开销，将第 2 天的运营负担降低了 80%，总体将预计的年度运营成本降低了 48.3%。

大型 JSON 文件还在构建数据管道时提出了挑战。它们需要大量的处理时间。Brown 开发了一种扇出流程，将消息放入具有架构的特定主题中，允许团队订阅特定主题并更快地从 Kafka 集群中使用数据。现在，Brown 的团队使用不需要过滤的二进制消息。

## 无与伦比的可扩展性和数据治理

SecurityScorecard 曾用于在一个半月内扫描 80 个端口，但现在可以在 10 天内扫描超过 2,000 个端口。这一成就帮助公司获得了需要访问大量数据的新客户。它还简化了公司的系统，并将导入和处理的数据从 10 倍扩展到 100 倍。

未来，威胁研究和数据平台团队一直在使用流数据管道来增强所有团队的数据发现和共享能力。他们计划与核心工程团队合作，利用 Apache Flink 来减少用于简单连接任务的自定义服务部署，从而增强实时数据处理能力、整合可观察性并降低基础设施成本。

## 构建可信并且实时的流式数据管道时的建议

构建流式数据管道时，您应该确立时间性的定义，与其他团队交互时总是使用模式，利用生态系统，并且只开发和维护绝对必要的内容。 

时间线之所以重要，是因为它限制了在出现问题时您需要多快做出反应，并且它还允许您定义实际的服务级别协议 (SLA) 以识别异常。模式确保您的消费者了解他们将得到的内容的形状，并允许团队设置数据质量规则，以尽早标记问题。利用生态系统让您可以利用丰富的知识和久经考验的系统。

构建可信并且实时的流式数据管道时的建议： 构建流式数据管道时，您应该确立时间性的定义，与其他团队交互时总是使用模式，利用生态系统，并且只开发和维护绝对必要的内容。 时间性之所以重要，是因为它限制了在出现问题时您需要多快做出反应，并且它还允许您定义实际的服务级别协议 (SLA) 以识别异常。模式确保您的消费者了解他们将得到的内容的形状，并允许团队设置数据质量规则，以尽早标记问题。利用生态系统让您可以利用丰富的知识和久经考验的系统。


