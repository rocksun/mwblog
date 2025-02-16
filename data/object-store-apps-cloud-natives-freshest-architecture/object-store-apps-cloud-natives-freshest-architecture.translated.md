# 对象存储应用：云原生最新鲜的架构

![对象存储应用：云原生最新鲜的架构的特色图片](https://cdn.thenewstack.io/media/2025/02/660865a8-steps-3614468_1280-1024x682.jpg)

也许是自 2006 年 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 推出其 [Simple Storage Service](https://aws.amazon.com/pm/serv-s3)(s3) 以来，对象存储再次成为热门。

越来越多的初创公司和最终用户发现，使用云对象存储作为持久层可以节省资金和工程时间，否则需要这些资金和时间来确保一致性。

廉价的对象存储推动了最近 Delta Lake 和 Apache Iceberg 之间的 [开放数据格式之战](https://thenewstack.io/showdown-at-the-lakehouse-databricks-muscles-up-with-tabular/)，因为两者都依赖对象存储来允许客户构建用于分析的、备受要求的开放数据格式。

对象存储也是 WarpStream 成功的秘诀，该公司使用该技术开创了一种新的、更具成本效益的 Kafka 运行方式。

主要的 Kafka 发行商 [Confluent](https://www.confluent.io/?utm_content=inline+mention) 注意到了这一点并收购了该公司。Confluent 的竞争对手 [Redpanda](https://redpanda.com/?utm_content=inline+mention) 也 [以完全不同的方式](https://thenewstack.io/how-to-introduce-real-time-data-predictions-with-redpanda/) 使用该技术，通过分层架构加速 Kafka 事务。

“[Docker](https://www.docker.com/?utm_content=inline+mention) 首席技术官 [Justin Cormack](https://github.com/justincormack) 在 KubeCon+CloudNativeCon NA 2024 的题为“[对象存储就是你所需要的一切](https://www.youtube.com/watch?v=ei0wwTy6_G4)”的演讲中承认：“人们一直在问我，你为什么要谈论对象存储，以及为什么是现在？这难道不有点无聊吗？”

Cormack 随后告诉 TNS：“但在过去几年里，人们已经开始使用对象存储作为唯一的后端来构建真正的应用程序。有很多这样的应用程序，而且它们非常有趣。”

初创公司正在利用对象存储作为持久层，在其上构建应用程序。这种方法解决了所有棘手的工程问题，例如管理并发和状态，更不用说备份和冗余了。

他告诉 TNS，对象存储意味着“无限的廉价存储”。这非常适合 [云原生开发](https://thenewstack.io/cloud-native/)。“任何有界的东西都会让开发者感到烦恼。”

它还被用于构建数据库、可观测性平台、虚拟磁盘以及谁知道的其他东西？

[MinIO](https://min.io/?utm_content=inline+mention) 的 AI 解决方案工程师 [Keith Pijanowski](https://www.linkedin.com/in/keithpij/) 补充说：“几乎每种你可能需要的存储类型都有解决方案，它们都使用对象存储。”MinIO 提供了一个 [类似 S3 的开源对象存储](https://min.io/product/overview) 文件系统，供企业使用。

## 高延迟、高吞吐量

在提出 S3 的 [想法](https://press.aboutamazon.com/2006/3/amazon-web-services-launches) 时，亚马逊负责人 Jeff Bezos 特别指出，他想要“Web 的 `malloc`”。这个 C 编程语言调用提供了一种让开发者用一行代码分配内存的方法。S3 的想法是，它应该让云开发者能够同样轻松地分配存储。

也就是说，S3 以及一般的对象存储，具有一些开发者应该了解的性能特征。换句话说，你必须知道如何使用它。

对象存储可以无限扩展，或者如果你使用的是内部版本（例如 MinIO），则仅受其运行的物理存储的限制。

![](https://cdn.thenewstack.io/media/2025/01/73a5be2e-justin-cormack-2-300x225.jpg)

Justin Cormack

从架构上讲，对象存储基本上是一个可以通过 http API 访问的键值存储。但它是 [非 POSIX](https://thenewstack.io/google-cloud-offers-posix-compliant-file-storage-red-hat-gluster/) 的。它不是一个功能齐全的文件系统。它具有一些文件列表功能，但很少有其他接口命令。最大的缺点是对象文件不能增量更新。一个更改就需要更新整个文件。

高度并行的对象存储仍然具有一定的延迟，但可以通过更大的并行性来扩展。

你可以在 AWS 上运行单个连接，从中获得 5 Gib 的吞吐量，*但是*你可以拥有任意数量的连接。

对于像 AWS S3 这样的服务，对象存储会在可用区之间复制，因此你可以免费获得复制、一致性和备份。就可靠性而言，它提供了 99.999999999%（“11 个 9”）的正常运行时间，最多可容纳 280 万亿个对象。
而且，对象存储在很大程度上是廉价的。存储数据便宜，网络也便宜。因为它易于使用，所以你可以编写一个非常简单的程序来使用它。

Cormack 说：“拥有简单的原语可以让你投入精力使其可靠。这让你有信心可以安全地在它们之上构建应用程序。”

## 数据库的好消息

随着时间的推移，S3 API 成为对象存储的事实标准接口，为 MinIO 和 [Ceph](https://thenewstack.io/ceph-20-years-of-cutting-edge-storage-at-the-edge/) 以及其他实现铺平了道路。

对象存储的最初用例似乎主要用于网站，这些网站通常逐页更新。但进一步的用例推动了对并行性的需求，这意味着必须管理谁写什么。

管理并发的一种常用方法是使用数据库，例如 DynamoDB，来管理并发。这是 Docker 使用 Docker Hub 采用的方法。

“它为你提供了一个互斥并发原语，你可以使用它来让多个应用程序写入内容。

应用程序开发人员易用性的一个重大飞跃是 [2024 年新增的](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/) S3 接口的新命令，用于在对象尚不存在时写入对象（带有 IF-NONE-MATCH 的 PUT），现在 [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-requests.html)、[Minio](https://github.com/minio/minio) 和 [Cloudflare R2](https://developers.cloudflare.com/r2/) 都支持该命令。

可以使用此命令创建一系列有序文件 001、002、003 等的应用程序。如果有多个服务器写入文件，则文件仍然按照先到先得的原则以递增方式编号。

实际上，这些顺序文件[可以是一个日志](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)，这是数据库的基本原语。这允许你使用对象存储本身而不是单独的数据库来实现并发。

## 开放数据之战

Cormack 说：“你可以从日志构建任何存储系统。” 这些可以是预写日志、提交日志或事务日志。

Apache Delta Lake [使用此原语](https://dl.acm.org/doi/10.14778/3415478.3415560) 来创建符合 ACID 的数据存储，而 Apache Iceberg 也依赖于对象存储。去年，大量客户涌向这些开放格式中的一种或另一种，以此作为[将数据保持为开放格式](https://www.dremio.com/why-dremio/)的一种方式。两者都使用 [Parquet 文件作为表](https://thenewstack.io/an-introduction-to-apache-parquet/)。

Phil Eaton [提供了一个示例](https://notes.eatonphil.com/2024-09-29-build-a-serverless-acid-database-with-this-one-neat-trick.html)，说明如何使用 [Go 编程语言](https://thenewstack.io/introduction-to-go-programming-language/) 构建基于 Delta Lake 的数据库。

Cormack 说：“这些东西有很多不错的属性，对开发人员来说很有趣。”

## “自带存储桶”

WarpStream 是一个与 S3 兼容的 Kafka 数据存储实现，它[承诺“零磁盘”管理和无限可扩展性](https://www.warpstream.com/bring-your-own-cloud-kafka-data-streaming)。该公司[最近被](https://thenewstack.io/with-warpstream-confluent-got-a-new-type-of-kafka-platform/) Confluent 收购，后者随后将其作为“自带云”服务提供。

RedPanda 宣称比 [Confluent 的高级 Kafka 云产品](https://www.confluent.io/lp/confluent-cloud) 吞吐量更快，部分原因是使用 SSD 作为缓存层，然后将最终结果卸载到 S3。

WarpStream 走了另一条路，提供了一种速度较慢但运行成本*低得多*的服务。

事实证明，许多用户并不介意为了降低运营成本而牺牲一点延迟。许多应用程序根本不需要超低延迟。

秘诀：WarpStream 构建在 S3 之上。

使用 AWS，你无需为跨可用区的流量付费，因此 WarpStream 的妙处在于利用这一点来降低跨可用区发送 Kafka 消息的成本，从而完全消除了使用 EBS 等服务会产生的跨区域费用。

Cormack 指出：“这是运行 Kafka 最便宜的方式。”

此外，WarpStream 提供了一种简单的服务模式：客户管理自己的 S3 存储桶，而 WarpStream 提供了一个控制平面。

Cormack 告诉 TNS：“它的运营管理非常非常简单，因为它只是对象存储和语句计算。”

## 对象存储的其他创新用途

环顾生态系统，可以发现对象存储的许多其他创新用途。

一个用于[虚拟磁盘](https://dl.acm.org/doi/10.1145/3492321.3524271)的开源项目使用了该技术。为了构建横向扩展磁盘，研究人员使用 SSD 作为缓存，然后将更改作为日志发送到 S3。
理论上，它可以作为 Amazon Elastic Block Storage (EBS) 的一个[更便宜的替代方案](https://github.com/asch/dis)。

[SlateDB](https://thenewstack.io/slatedb-bottomless-databases-built-on-cloud-object-stores/) 是一个键值存储，它利用了这种架构。它具有较高的写入延迟，但提供完全持久性并且可以无限扩展。
[TurboPuffer](https://turbopuffer.com/) 是一个构建在对象存储之上的[向量数据库](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/)。
由于对象存储完成了确保可靠性的所有工作，因此开发人员只需附加临时组件即可构建云原生应用程序。

在云原生世界中，可靠性通常被定义为拥有大量的 Pod。但是，如果您构建一个数据库，确保持久性将成为一项主要工作，“但是如果您使用对象存储，所有这些事情都会为您完成，”Cormack 说。

“最终你会得到一个非常不同的可靠性故事。”

## 自带存储桶

[Matt Klein](https://thenewstack.io/matt-klein-on-the-success-of-envoy-and-the-future-of-the-service-mesh/)，因 [Envoy 代理而闻名](https://thenewstack.io/tetrate-bloomberg-collaborate-on-envoy-based-ai-gateways/)，创建了 [BitDrift](https://bitdrift.io/)，通过对象存储以“[自带存储桶](https://thenewstack.io/why-you-might-bring-your-own-s3-bucket-byob-to-the-observability-party/)”的方式来降低可观测性的成本。
这也更亲切地被称为“[自带云](https://thenewstack.io/should-you-bring-your-own-cloud/)”，WarpStream 使用了这个术语，[Buildkite 也是如此](https://thenewstack.io/should-you-bring-your-own-cloud/)，它的持续交付平台可以加速测试，但以并行方式运行它们。

“你不能一个接一个地运行测试。否则，按顺序运行测试将花费数周、数月、数年，甚至在某些情况下。所以你必须瘫痪，你必须同时运行它们，”Buildkite 首席执行官 Keith Pitt 告诉 TNS。

## 你不需要 Raft

更多的可能性比比皆是。

它可以用于云原生应用程序的[领导者选举](https://www.morling.dev/blog/leader-election-with-s3-conditional-writes/)。

“你注意到的是，你不需要构建大量的分布式系统原语，因为你已经有了这个一致的后端可以使用，”Cormack 说。“你得到了一个并发原语，你真的可以在它之上构建东西。”

[云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 的任何需要 [Raft 实现](https://thenewstack.io/raft-native-the-foundation-for-streaming-datas-best-future/)（Vitess、etcd）以进行负载平衡和并发的 [Landscape 技术](https://landscape.cncf.io/) 都是重写以在对象存储上运行的良好候选者，Cormack 指出。

“如果可以避免，你就不必做这些事情，”Cormack 说。“在对象存储上构建持久层意味着你不必这样做。”

“如果你正在构建涉及数据的东西，这是一个非常有吸引力的选择，这几乎就是一切，”Cormack 说。

## 家里的对象存储

虽然许多应用程序都是在 Amazon S3 上构建的——或者其他云对象存储，例如 [DigitalOcean Spaces](https://www.digitalocean.com/products/spaces)、[Azure Blob Storage](https://news.microsoft.com/?utm_content=inline+mention) 和 [Google Cloud Storage](https://cloud.google.com/?utm_content=inline+mention)——MinIO 的 Pijanowski 指出，该架构也可以在内部使用。

MinIO 与 [Dremio](https://www.dremio.com/why-dremio/) 和 [StarBurst](https://www.starburst.io/) 建立了合作伙伴关系，为客户提供在本地轻松设置具有无限扩展能力的数据仓库。对于云 Kubernetes 部署的替代方案，该公司还与 VMware 合作，为那些希望使用 [VMware Cloud Foundation](https://thenewstack.io/vmwares-private-cloud-shift-under-broadcom/) 构建私有部署的人提供服务。

对象存储曾经是一种有点小众的技术，现在正成为现代云的基本构建块，从而导致了新一波云原生应用程序的出现，这些应用程序开发速度更快、更易于维护且运行成本更低。

Cormack 的完整演讲可以在这里欣赏：

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)