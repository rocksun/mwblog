<!--
title:  2024年无服务器计算与事件流状况报告
cover: https://cdn.thenewstack.io/media/2023/11/bde059db-event-streaming-serverless-1024x683.jpg
-->

了解无服务器计算和事件流如何在当今技术领域演变、交汇并日益受到青睐。

> 译自 [State of Serverless Computing and Event Streaming in 2024](https://thenewstack.io/state-of-serverless-computing-and-event-streaming-in-2024/)，作者 Tun Shwe。

将事件流与无服务器计算相结合，常常能产生一个高效低成本的解决方案，用于处理流数据，极大地减少了基础设施管理和维护的复杂性。这种协同作用使开发人员能更专注于应用程序逻辑，而减少对基础操作问题的关注，从而加快开发速度。

直到不久以前，无服务器事件流意味着使用事件流平台和流处理引擎(由供应商或内部管理)，并在适当情况下(例如短期的无状态工作负载)辅之以函数即服务(FaaS)技术。考虑到 FaaS 是唯一的无服务器组件，把这种设置称为“无服务器”可能过于慷慨。

然而，由于无服务器技术的进步，我们不再仅仅依赖于函数即服务（FaaS）。其他替代方案，如无服务器容器即服务（CaaS）工具，越来越被用作事件流使用案例的基础。

## 无服务器计算的当前状态

> "在过去的一年中，在 Azure 和 Google Cloud 上运行的组织中的无服务器采用率分别增长了6%和7%，而 AWS 的增长率为3%。我们超过70%的 AWS 客户和60%的 Google Cloud 客户当前使用一个或多个无服务器解决方案，Azure 紧随其后，为49%。"
> — 无服务器状态，Datadog，2023

无服务器的日益普及是可以理解的。跨越各个行业的许多组织都在采用无服务器计算，被成本效率、按需扩展性、运营开销降低和更快的上市时间等诱人承诺所吸引。

无服务器的采用也得益于多样化的工具生态系统的兴起。除了FaaS(例如 AWS Lambda、Microsoft Azure Functions 和 Google Cloud Functions)之外，无服务器景观已经扩展到更广泛的服务和功能范围，包括:

- 无服务器应用平台，例如Netlify和Vercel。
- 无服务器数据库，例如[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline-mention) Atlas、FaunaDB和InfluxDB Cloud。
- 无服务器API管理平台，包括AWS API Gateway和Azure API Management。
- 无服务器框架，例如Zappa、Serverless Framework、Claudia.js和Ruby on Jets。
- 无服务器CaaS解决方案，例如AWS Fargate和Knative。

## 无服务器方法：FaaS对比CaaS

在FaaS的替代方案中，无服务器CaaS正在迅速成为关注的焦点。Datadog的2022年《无服务器状态》报告显示，在2022年，Google Cloud Run是在Google Cloud中部署无服务器应用程序的增长最快的方法。2023年的报告表明，跨所有主要云提供商，无服务器CaaS的采用继续加剧。

无服务器CaaS的兴起并不令人惊讶，因为它带来了更大的灵活性，并消除了FaaS的一些缺点:

| 标准 | FaaS | CaaS |
| - | - | - |
| 延迟 | 由于频繁的冷启动，延迟可能不可预测并很慢。这可能会对需要实时响应的应用程序造成问题。 | 启动容器可能需要比启动轻量级函数更多的时间。然而，容器的生命周期更长。因此，一旦启动了容器，就不会遇到冷启动问题。这将总体上导致更低和更可预测的延迟。 |
| 状态 | 通常是无状态的，这对需要有状态行为的应用程序是一个限制(例如，窗口化，聚合)。 | CaaS通常支持有状态和无状态应用程序。 |
| 运行时和可移植性 | FaaS产品往往与特定的云提供商绑定。每个提供商都有自己的运行时环境和限制，这可能会影响FaaS的可移植性。 | 由于使用容器，可移植性更高。这些容器可以在环境之间移动(例如，不同的云提供商，本地)，几乎不需要或根本不需要更改。 |
| 工作负载类型 | 短期的、不常见的事件驱动型工作负载。中等吞吐量。 | 长期运行的、持续的工作负载。高吞吐量。 |
| 执行 | 对于大多数FaaS解决方案，每个实例一次只处理一个请求。这对高流量应用程序来说可能是一个重大的限制。 | 能够同时处理多个请求，提供更高效的资源利用率和更好的高流量应用程序性能。  |

FaaS和CaaS之间的这些差异，在事件流应用程序的背景下尤其相关。总的来说，CaaS模型是一个更可靠、通用和适合处理高频数据流的方法。

## 事件流的当前状态

事件流(或数据流)已经成为现代架构不可或缺的一部分，使组织能够实时收集、处理、存储和分析数据。根据[Confluent的“2023数据流报告”](https://assets.confluent.io/m/52436fc9cd4844f4/original/20230510-RPT-Data_Streaming_Report.pdf?utm_medium=report&utm_campaign=tm.campaigns_cd.brand-2023q2-brandhub&session_ref=https://www.google.com/&_ga=2.154755576.1903591368.1699262965-1579094558.1689094137&_gl=1*8o5393*_ga*MTU3OTA5NDU1OC4xNjg5MDk0MTM3*_ga_D2D3EGKSGD*MTY5OTQ1MTcwMC44Ni4xLjE2OTk0NTE3MDMuNTcuMC4w)，数据流在IT投资议程中占有重要地位:

> “89%的受访者表示，数据流投资很重要，其中44%将其列为首要的战略优先事项。”
> — 数据流报告，Confluent，2023

除了事件流平台，还有各种流处理技术作为补充，如Apache Flink、Apache Storm、Apache Samza、Apache Beam、Kafka Streams、ksqlDB和Faust，每种技术都有自己的优势。例如，Beam提供了一个统一的API来处理批处理和流数据，而ksqlDB通过只依赖SQL查询来简化流应用程序的开发。

毫无疑问，事件流正在持续存在并继续增长其重要性。也就是说，[流数据可能难以处理](https://quix.io/blog/why-is-streaming-data-so-hard-to-handle)。当今可用的大多数流技术都难以使用，自主管理流架构既不容易，也不便宜。例如，我在之前的一篇文章中谈到了[托管和管理Kafka的许多挑战](https://thenewstack.io/decoding-kafka-why-its-worth-the-complexity/)；读一读这篇文章，可以了解所涉及的内容。

## 无服务器和事件流的交汇

2019年，[Neil Avery](https://www.linkedin.com/in/neilavery/?originalSubdomain=uk)(Confluent首席技术官办公室的前技术专家)发表了[一篇博文](https://www.confluent.io/blog/journey-to-event-driven-part-3-affinity-between-events-streams-serverless/)，分析了事件流和无服务器计算之间的关系。Neil 的帖子讨论了FaaS如何与事件流配合。关注FaaS是有意义的，因为当时FaaS是无服务器计算的主要形式。Neil 的文章非常值得一读，它展示了FaaS如何用来补充事件流，以及FaaS的局限性，例如冷启动和不适合有状态流处理。

快进到2023年。由于最近的技术进步，无服务器和事件流之间有了更好、更紧密的协同效应，这远远超出了FaaS。以下是一些将无服务器计算(FaaS以外)与事件流相结合的新兴工具和趋势。

## 无服务器流处理

传统的流处理通常涉及一个架构，其中许多移动部件管理分布式基础设施并使用复杂的流处理引擎。例如，Apache Spark 是最受欢迎的处理引擎之一，但众所周知，部署、管理、调优和调试都很困难(阅读有关使用Spark的优势、劣势和丑陋的更多信息)。根据用例，实现可靠、可扩展的流处理功能可能需要几天到几周的时间。除此之外，您还需要处理连续的监控、维护和优化。您甚至可能需要一个专门的团队来处理这种开销。总而言之，传统的流处理具有挑战性、昂贵且耗时。

相比之下，无服务器流处理消除了管理复杂架构和基础架构的头痛。它也更加节省成本，因为您只支付所使用的资源。无服务器流处理解决方案开始出现是很自然的。一个例子是[Google Cloud上的Spark](https://cloud.google.com/solutions/spark)。谷歌声称这是行业首个自动扩缩的无服务器Spark，它完全消除了手动基础设施配置和调优。

我之前提到，CaaS正在作为一种无服务器方法兴起。一般来说，无服务器CaaS流处理解决方案具有以下特点:

- 可预测的低延迟，最小化处理延迟。
- 高吞吐量（可达每秒数千或数百万事件）。
- 适用于既有状态又无状态的处理工作负载。
- 适用于实时数据处理以及批处理。
- 最适合长时间运行、计算密集型或具有可变或不可预测工作负载的流程。
- 能够同时处理多个数据处理任务（并发性）。
- 无需提供、维护或扩展服务器基础设施。

[Bytewax](https://bytewax.io/)就是一个可以与无服务器CaaS模型结合使用的流处理技术的例子。Bytewax是一个开源的[Python](https://roadmap.sh/python)库和分布式流处理引擎，用于构建流数据管道。在其他选择之中，您可以使用容器运行Bytewax数据流。这意味着您可以在Amazon Elastic Kubernetes服务(EKS)或Amazon弹性容器服务(ECS)上运行Bytewax数据流。然后，您可以将这些容器部署到AWS Fargate，这是亚马逊的无服务器计算引擎。这样，您可以从无服务器流处理功能中受益，而不需要配置、配置或扩展容器群集服务器。

[Quix Streams](https://github.com/quixio/quix-streams) 是另一个开源的 Python 流处理库，它抽象了开发流应用程序和实时处理数据的复杂性。作为原生云的，它可以部署到任何 Kubernetes 集群。它也可以与 [Quix Cloud](https://quix.io/) 配合使用，Quix Cloud 属于无服务器 CaaS 类别。在底层，Quix Cloud 是一个完全托管的平台，使用 Kafka、[Docker](https://www.docker.com/?utm_content=inline-mention)、Git、容器化微服务和无服务器计算环境来托管流应用程序。其目的是使开发人员能够在消除配置、管理和扩展容器和基础设施的运维开销的同时构建、部署和监控应用程序。

例如，AI软件公司[CKDelta](https://www.ckdelta.ie/)使用Quix的无服务器流处理功能。[CKDelta使用Quix](https://quix.io/customer-stories/ck-delta)提供了一个事件流应用程序，该应用程序使用机器学习每天从新加坡180个地铁站处理40GB的Wi-Fi数据。具体来说，该应用程序持续收集高吞吐量的数据，并执行预测分析以预测车站的人群密度。

如果您好奇可以使用Quix构建的其他类型的无服务器事件流应用程序，可以看看这些[交互式模板](https://quix.io/templates)。

## 无服务器消息代理

在超越无服务器流处理的同时，无服务器消息代理正在崭露头角。一个例子是[Amazon MSK Serverless](https://aws.amazon.com/msk/features/msk-serverless/)，这是Amazon MSK的一种新的集群类型。虽然常规的MSK需要手动设置和管理Kafka集群，并根据提供的容量收费（无论使用情况如何），但MSK Serverless会根据需求自动管理和扩展Kafka基础设施，并根据实际使用情况收费。

[Apache EventMesh](https://eventmesh.apache.org/)是无服务器基于事件的中间件的另一个例子。EventMesh起源于WeBank，现在是Apache Software Foundation的一个顶级项目。尽管还处于初期阶段，EventMesh在GitHub上已经获得了近1500个星和近600个分叉，这是一个令人鼓舞的迹象。看到EventMesh如何发展，以及是否会出现类似的项目，将会很有趣。

## 结论

事件流已成为现代软件架构的支柱。与此同时，无服务器计算在过去几年取得了令人瞩目的进展；过去FaaS几乎是无服务器的唯一表达方式的时代已经过去。

考虑到处理事件流有多么困难，以及无服务器计算如何大规模简化从流数据中提取价值的过程，看到无服务器事件流解决方案崭露头角（或组织采用它们）并不奇怪。这些工具通常具有友好的定价模型（只支付实际使用的部分），并使企业能够实时收集和处理数据流，而无需考虑底层基础设施和容量规划。

今天的一个不断上升的趋势是将无服务器CaaS和流处理结合起来。无服务器CaaS将容器化的可伸缩性和灵活性与无服务器架构的简单性和成本效益结合在一起。这是处理动态、高容量、高频率数据流的强大基础，因此我期待在这个领域看到更多的竞争者。
