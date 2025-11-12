随着企业竞相在 [Kubernetes](https://thenewstack.io/kubernetes/) 环境中部署人工智能和数据密集型应用程序，标准的 [容器存储接口 (CSI)](https://thenewstack.io/kubernetes-storage-dynamic-volumes-and-the-container-storage-interface/) 已不足以满足新运营模式下的业务需求。

十年前，当 Kubernetes 首次崭露头角时，大多数容器化工作负载都是无状态的，不会在不同会话之间保存任何上下文。典型的 Node.js 或 NGINX 应用程序会根据可用元数据重新实例化，但它不会向持久性存储读取或写入数据。

## **Kubernetes 中有状态应用程序的兴起**

这些模式相对容易应用于无状态的 Web 应用程序，将微服务设计得尽可能无状态可以产生高度可靠、易于管理的系统。

然而，正如 [Brendan Burns](https://www.linkedin.com/in/brendan-burns-487aa590/)、[Joe Beda](https://twitter.com/jbeda)、[Kelsey Hightower](https://x.com/kelseyhightower) 和 [Lachlan Evenson](https://www.linkedin.com/in/lachlanevenson/) 在 [《Kubernetes：权威指南》](https://www.oreilly.com/library/view/kubernetes-up-and/9781098110192/) 中所写：“几乎每个具有任何复杂性的系统都在某处拥有状态，从数据库中的记录到为网络搜索引擎提供结果的索引分片。在某个时候，你必须将数据存储在某个地方。”

将这些数据与容器和容器编排解决方案集成通常是构建分布式系统中最复杂的方面。《Kubernetes：权威指南》的作者指出，[这种复杂性](https://thenewstack.io/kubernetes-complexity-realigns-platform-engineering-strategy) 源于“转向容器化架构也是转向解耦、不可变和声明式应用程序开发的过程。”

大约五年前，在 [Nutanix](https://www.nutanix.com/solutions/cloud-native?utm_medium=redirect&utm_content=inline-mention)，我们开始看到使用容器化数据库（如 Cassandra、Redis、PostgreSQL、MySQL 和 Kafka）的有状态应用程序数量有所增加。随着这一转变的进行，企业近期对人工智能的快速采用显著加速了这一进程。

这种加速不足为奇。正如 [Winder.AI](https://winder.ai) 的首席执行官兼创始人 [Phil Winder](https://www.linkedin.com/in/drphilwinder/) 在 [《强化学习》](https://www.oreilly.com/library/view/reinforcement-learning/9781492072386/) 中指出，人工智能是“数据科学的产物，而数据科学是一个研究由现象产生的数据的总体科学领域。”

换句话说，您组织的数据对于您可能通过人工智能追求的任何举措的成功都至关重要。

虽然数据因人工智能而变得重要，但它也是几乎所有应用程序的基础，例如用于改善用户体验的个性化推荐、用户行为分析、安全性、可观测性（例如日志和指标）、物联网 (IoT) 和边缘计算。

Gartner 分析师 [Julia Palmer](https://www.linkedin.com/in/juliagartner/) 的一个推论是，她 [预测](https://www.gartner.com/en/documents/4489199)：“到 2027 年，80% 的 Kubernetes 部署将需要持久性容器存储的高级功能，而 2023 年初这一比例为 30%。”

## **了解 CSI，Kubernetes 存储的基础**

[Kubernetes CSI](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/) 是 Kubernetes 中处理持久性的标准机制。该层包含一组 API，应用程序可以使用这些 API 对底层存储系统执行读写操作。

由于 CSI 是一种标准，每个存储供应商都有自己的实现——Nutanix CSI、[戴尔](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention) CSI、[红帽](https://www.openshift.com/try?utm_content=inline+mention) OpenShift CSI、[Portworx](https://portworx.com/?utm_content=inline+mention) CSI 等等——并且每个 CSI 驱动程序都通过内置的 CSI 扩展机制提供供应商特定的属性。

Nutanix CSI 为容器化有状态应用程序提供 [Nutanix 统一存储](https://www.nutanix.com/library/datasheets/nus#) (NUS)。NUS 是一个软件定义的数据服务平台，它将文件、对象和块存储整合到一个单一的、高性能、高密度且成本优化的平台中，并根据客户需求进行打包：

[![Architecture diagram showing disaster recovery setup across two data centers (AZ1 and AZ2). Data center AZ1 contains the primary Nutanix cluster with Prism Central, and a primary Kubernetes cluster running an NDK application, with K8s resources and persistent volumes. Data center AZ2 contains the secondary Nutanix cluster, also with Prism Central, and a primary DR Kubernetes cluster, plus the same NDK application components shown in dashed lines. The synchronous replication arrow connects the persistent volumes between the two data centers, enabling high availability and failover capabilities.](https://cdn.thenewstack.io/media/2025/11/ed0d455e-nutanix-csi.png)](https://cdn.thenewstack.io/media/2025/11/ed0d455e-nutanix-csi.png)

Nutanix CSI 用于使用 Nutanix 统一存储的有状态应用程序。（来源：Nutanix）

## **CSI 对企业工作负载的局限性**

CSI 对于为单个集群提供持久存储来说没有问题，但除此之外，它还有一些[局限性](https://thenewstack.io/kubernetes-isnt-enough-for-a-production-ready-platform)。主要是，它不提供数据保护或业务连续性和灾难恢复 (BCDR) 机制。这在金融服务和医疗保健等受严格监管的行业中尤为重要。在受监管行业中对 BCDR 的需求并非新鲜事，但随着在 Kubernetes 集群中运行的应用程序数量不断增加，它变得越来越重要。

法规还规定了数据必须存储的位置。在 EMEA 等地区，政策可能要求所有数据副本都保留在国界之内，这在已经复杂的技术挑战上增加了一层地理特定合规性。

对于任何应用程序，持久性数据都需要尽可能靠近应用程序运行的位置，这使得数据复制对于 BCDR 和相关用例（如工作负载再平衡和高可用性）成为必需。这在异构部署模型中尤为重要，例如，为了处理临时需求高峰（如“黑色星期五”、大学招生截止日期、在线票务销售或媒体流媒体激增）而从本地到公共云的云爆发。云爆发需要应用程序环境和相关数据快速、一致地往返于云端进行复制。

## **同步与异步数据复制**

数据复制可以是同步的，也可以是异步的，这取决于写入操作如何管理：

*   同步数据复制意味着数据不断地从主服务器同时复制到所有副本服务器。
*   异步数据复制意味着数据首先复制到主服务器，然后根据预先配置的保护策略（规定数据复制频率和数据保留期限）复制到副本服务器。

尽管同步复制确保不会丢失数据，但异步复制需要显著更少的带宽并且成本更低。

## **填补空白**

[Nutanix Kubernetes 数据服务](https://www.nutanix.com/en_gb/products/data-services-for-kubernetes) (NDK) 可以填补 CSI 留下的空白，让您能够从一个统一平台将虚拟机 (VM) 和容器化应用程序的不同世界作为一个单一实体进行管理、控制和操作。

NDK 使用熟悉的 Kubernetes 机制来帮助减少学习曲线。它作为 Helm chart 发布，用户使用 kubectl 从命令行与它交互。数据服务与 Kubernetes 发行版无关。虽然我们更希望客户使用我们的 Kubernetes 发行版，但数据服务将与替代方案（如 Red Hat OpenShift 或 [亚马逊](https://aws.amazon.com/?utm_content=inline+mention) EKS Anywhere）协同工作。NDK 支持同步和异步数据复制。

在 NDK 中，异步复制可以以每小时一次的最大频率执行。策略是在应用程序级别而非集群级别设置的，因此单个集群中的不同应用程序可以运行不同的数据复制策略。

异步复制用于 BCDR。在一个典型示例中，您可能有位于不同国家的两个数据中心——例如，西班牙的主数据中心和德国的备用数据中心——以便在发生重大灾难时可以从一个切换到另一个。

除了 BCDR，Nutanix 还支持使用同步复制实现高可用性。

[![Architecture diagram showing disaster recovery setup across two data centers (AZ1 and AZ2). Data center AZ1 contains the primary Nutanix cluster with Prism Central, and a primary Kubernetes cluster running an NDK application, with K8s resources and persistent volumes. Data center AZ2 contains the secondary Nutanix cluster, also with Prism Central, and a primary DR Kubernetes cluster, plus the same NDK application components shown in dashed lines. The synchronous replication arrow connects the persistent volumes between the two data centers, enabling high availability and failover capabilities.](https://cdn.thenewstack.io/media/2025/11/6dd4a60b-ha-sync-replication.png)](https://cdn.thenewstack.io/media/2025/11/6dd4a60b-ha-sync-replication.png)

使用同步复制实现高可用性。（来源：Nutanix）

同步复制保证在发生故障时数据零丢失，但它要求两个数据中心物理位置非常接近。这意味着它不适合防范地震或飓风等自然灾害，但根据您的业务需求，它可能是一种有价值的方法。

例如，我们的一位客户经营游轮，并有两个独立的数据机房。它们位于不同的位置，但物理距离很近，通过带宽高速网络连接，延迟低于 10 毫秒。这样做的好处是，如果一个数据机房出现故障，可能是由于停电或洪水，游轮可以切换到另一个机房并继续运行。

## **超越 CSI：为什么 AI 对 Kubernetes 存储有更高的要求**

将虚拟机和容器融合到统一平台是企业应对分布式、数据密集型应用程序复杂性的实际需求。随着有状态应用程序在 Kubernetes 环境中持续激增——这一趋势因人工智能的采用而加速——对企业级数据服务的需求变得至关重要。

尽管 CSI 为持久性存储提供了基础，但对于需要企业级容器化工作负载所要求的数据保护、合规性和操作灵活性的组织而言，NDK 等解决方案至关重要。NDK 作为 Nutanix Kubernetes 平台 (NKP) 解决方案的一部分提供，这是一个完整的全栈平台，将基础设施、Kubernetes 编排、存储、数据服务和应用程序生命周期管理整合到单一平台中。