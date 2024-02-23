<!--
title: 2024年流数据路线图：引领实时革命
cover: https://cdn.thenewstack.io/media/2024/02/d2c13b39-stream-8504869_1280-1024x633.jpg
-->

克服批处理架构，拥抱流数据优势，是实现强大人工智能部署的基础。

> 译自 [2024 Streaming Roadmap: Navigating the Real-Time Revolution](https://thenewstack.io/2024-streaming-roadmap-navigating-the-real-time-revolution/)，作者 Filip Yonov 是 Aiven 的产品管理总监，负责流平台。Aiven 流平台提供了一个综合生态系统，集成了像 Apache Kafka 和 Apache Flink 这样的最佳流产品，部署在多个云环境中。

[生成式人工智能](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/)（GenAI）和[大语言模型](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)（LLMs）将重塑我们的生活、工作和业务方式。随着人工智能实现更自然的人机交互，利用这些技术的公司必须优先考虑有效的数据管理，以真正获得竞争优势。

[研究](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier%23key-insights)表明，生成式人工智能可能为全球经济增加数万亿美元，2023年公司进一步扩大和巩固了他们的人工智能和数据投资策略，未来将继续如此。

实时数据流对于实现以人工智能为先的企业的承诺至关重要。关键在于，企业在当下运营，为了提供丰富、个性化的用户体验，以人工智能为中心的架构必须以规模化的方式以即时性和低延迟处理数据，这仅可以通过流技术实现，例如 [Apache Kafka](https://kafka.apache.org/) 和 [Apache Flink](https://flink.apache.org/)。

因此，克服面向批处理的架构并拥抱流数据的优势是朝着强大的人工智能部署迈出的基础性步骤。这种演变，以及[机器学习](https://thenewstack.io/ai-machine-learning-and-the-future-of-software-development/)（ML）的快速增长，正在推动主要的市场变革，正如 Forrester 在其[2023年第四季度报告](https://www.forrester.com/report/the-forrester-wave-tm-streaming-data-platforms-q4-2023/RES178464)中将流数据平台认定为新兴软件类别所强调的那样。

2024年，对于我们在流数据领域的人来说，焦点不仅仅是人工智能。[自带云](https://aiven.io/blog/optimize-your-cloud-data-infrastructure-spend-with-byoc)（BYOC）部署模型为扩展托管流式服务提供了一种高效的机制。通过构建在Apache Flink上的应用程序，机器学习正在进入实时环境，而像[Apache Iceberg](https://iceberg.apache.org/)、[Apache Hudi](https://hudi.apache.org/)和[Apache Paimon](https://paimon.apache.org/)这样的开源表格式正在简化ETL，将Kafka定位为企业的摄入层。与此同时，[数据网格](https://thenewstack.io/the-real-time-data-mesh-and-its-place-in-modern-it-stacks/)架构和[流式治理](https://www.klaw-project.io/)正日益成为业务需求，并将影响将组织转型为本地实时运营的最佳实践。

## 拥抱BYOC及其更多：在流式中实现灵活性和成本控制

随着我们进入2024年，流数据更易访问的趋势将日益显著。自带云（BYOC）模型引领着这一变革，为企业提供了一种成本效益高、灵活的方式来管理其流式工作负载，同时最大限度地利用现有的云承诺。但BYOC只是开始——一种更广泛的趋势正在重塑流式领域，用户要求跨多云环境无缝工作并且更具成本效益的解决方案。

这一趋势的一个重要方面是计算和存储的分离。这种变化使企业能够独立扩展其流式资源，从而实现更高效的利用和成本节省。在传统的数据流设置中，计算和存储紧密耦合，导致效率低下和成本较高，特别是在处理波动工作负载时。尽管一些供应商多年来一直提供分层存储，但Kafka的分层存储（目前处于[预览](https://kafka.apache.org/36/documentation/)阶段）的真正优势尚未在规模上得以实现。

在2024年，预计BYOC部署能力将进一步简化和自动化。我们还将目睹存储和计算的真正分离，为流数据工作流提供前所未有的弹性和成本节省。有趣的是，一些创新方法已经出现，利用与亚马逊S3的直接集成作为Kafka的存储层，并消除了对Kafka的网络需求量大的设计。结合亚马逊[S3 Express](https://aws.amazon.com/s3/storage-classes/express-one-zone/)的低延迟对象存储，这为云原生、解耦式的流式处理打开了一种强大的方式——这是一个值得在未来的博客文章中进行更深入探讨的概念。

## 开放式表格式——领先的实时和批处理统一

我经常被问到，“为什么不把[Kafka用于一切](https://thenewstack.io/confluent-wants-to-make-batch-processing-a-thing-of-the-past/)？”虽然我认识到实时数据的力量，但数据的真正价值在于其流动之外：在其实用性、集成和生命周期管理中。

开放式表格式正在重塑我们对数据湖的方法，增强其寿命和效用，并为大规模的高级流式使用案例奠定基础。数据湖中的流数据将成为一流公民和默认的摄入层。在2024年，我们将见证数据乌托邦的第一迹象——Kafka中的实时流式处理，对象存储中的历史数据，但始终可以通过类似Iceberg/Hudi或Paimon的开放式表格式进行查询准备。

Kafka正超越其作为传输层的角色，与云对象存储（如亚马逊S3、Google云存储、Azure Blob存储）紧密集成，以赋予长期分析以权力。像Apache Hudi和Apache Paimon这样的项目，专为事务性和流式数据湖架构而设计，将Kafka定位为[增量处理](https://hudi.apache.org/blog/2020/08/18/hudi-incremental-processing-on-data-lakes/)的真实来源。虽然Iceberg在2024年无疑将领先，但互操作性和跨格式兼容性确实是必需的——[OneTable](https://onetable.dev/)，承诺在主要湖格式之间实现无缝交互，是一个值得关注的项目。

围绕湖格式的炒作是合理的，但实时连接在哪里？当历史上下文容易访问时，流数据获得战略价值。想象一下，将您的欺诈检测ML算法的注意力从几分钟扩展到一整年的数据！

事务性数据湖架构，由开放式表格式和流式处理驱动，提供了这一强大组合。开放式表格式是一个改变游戏规则的因素：通过超越Parquet等传统结构，并与摄入层无缝集成，这些格式使企业能够统一实时和批处理数据。这种统一为真正具有差异化的人工智能竞争优势奠定了基础。数据管理的这种演变不仅仅是程序性更新；它在本质上是根本性的，并将在未来几年推动数据转型。

## Apache Flink：加速实时决策

虽然2023年看到主要参与者推出基于Flink的托管服务，但由于其被认为复杂和缺乏流畅工具化而受到阻碍。挑战在于业务用户不直接使用流数据。然而，2024年将为Flink带来重大升级，使其面向数据科学家和业务分析师等更广泛的受众开放。这可能将由像Apache Paimon这样的框架领导，它结合了流处理的强大功能与流畅的声明式ETL操作和湖屋能力。

Flink的崛起反映了Apache Spark在批处理数据处理中的主导地位。Spark定义了企业如何处理湖中的非结构化数据，为以人为中心的决策制定提供了机器学习、商业智能（BI）和报告支持。现在，随着人工智能的普及，对数据流的持续处理以供应不断发展的人工智能模型的需求不断增加。

Flink 承担起这一角色，提供了规模化的即时、即时计算。这使企业能够基于毫秒级的新鲜数据自动化决策。例如，[TikTok](https://arxiv.org/pdf/2209.07663.pdf) 使用 Flink 实时优化其强大的推荐引擎。基于用户的瞬间行为（点赞、跳过、分享），Flink 持续更新推荐内容，使用户的订阅变得指数级更加准确，并将实时响应转化为竞争优势。

在一个由人工智能驱动的世界中，速度不是奢侈品；而是必需品。Flink 让机器以前所未有的精确度实时做出决策。随着企业寻求提供超个性化体验，从以人为中心到以机器速度决策的转变变得至关重要。Flink 不仅仅是一个工具；它是一个新时代人工智能驱动的实时策略的引擎。2024年将见证其采用率飙升。

## 数据网格和流式管理：从原则到必要条件

在 [Aiven](https://aiven.io/)，我们通过强大的治理工具、[自助式流式处理](https://www.klaw-project.io/)、精细的访问控制和我们的 Terraform Provider，赋予客户采用数据网格原则的能力。在2024年，企业对流式管理的投资将变得至关重要，以确保应用程序跨实时数据的可靠性、灵活性和可用性。这是一个多方面的学科：追踪数据谱系，保证准确性，丰富元数据和安全目录——所有这些都是为了使数据在速度和规模上更易于访问和使用。

早期实施治理可将更快、更相关的数据传递给业务团队。这还能减少低价值数据的噪音，降低存储成本和潜在风险。随着治理价值被广泛认可，2024年将会有更多公司主动集成流式处理治理。历史上，只有大型企业才能创建可重用的数据资产，但治理软件的进步正在使这一能力民主化。

“[数据即产品](https://towardsdatascience.com/data-as-a-product-vs-data-products-what-are-the-differences-b43ddbb0f123)”的战略将成为主流，推动实时数据领域的效率提升和创新推动。挑战在于在不牺牲安全性的前提下对共享数据进行情境化。随着数据向下游传递，这变得更加复杂和昂贵。在源头嵌入治理提供了对其背景和价值的更清晰理解——且证明更具成本效益。

尽管多个团队可以从共享对同一数据的访问中获益，以构建服务和应用程序，但为非起始用户安全、情境化和全面地呈现这些数据存在挑战。随着数据离源头越来越远，提供上下文变得更加复杂和昂贵。在源头启动数据治理流程不仅具有成本效益，还提供了对数据来源、价值和含义的更深入理解。

将新数据治理能力集成到云数据仓库、数据库和其他数据基础设施服务等产品中，旨在满足这些不断发展的需求。

这意味着开发人员在创建和共享可重复使用的数据产品时不再需要手动构建基础架构。这将极大地帮助公司的分析和业务层采用实时数据。

## 流数据革命

我对流数据改变企业的潜力持乐观态度。在 Aiven，我们致力于推动数据流技术的边界，并培育一个充满活力、开放的生态系统。2024年将见证流数据作为现代企业不可或缺的支柱得到巩固，发挥与数据湖和数据仓库一样重要的作用，推动战略决策。
