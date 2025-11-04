<!--
title: 突破“无共享”瓶颈：NoSQL新范式
cover: https://cdn.thenewstack.io/media/2025/10/3df98bda-lights123.jpeg
summary: NoSQL数据库常采DAS享高性能，但其高成本、低效率、缺数据服务。现代SAN（如NVMe/TCP、软件定义）可提供同等高性能，同时更经济、高效且具完整数据管理功能，推荐大规模NoSQL采用。
-->

NoSQL数据库常采DAS享高性能，但其高成本、低效率、缺数据服务。现代SAN（如NVMe/TCP、软件定义）可提供同等高性能，同时更经济、高效且具完整数据管理功能，推荐大规模NoSQL采用。

> 译自：[Breaking the 'Shared-Nothing' Bottleneck: A NoSQL Paradigm](https://thenewstack.io/breaking-the-shared-nothing-bottleneck-a-nosql-paradigm/)
> 
> 作者：Carol Platz

虽然没有一种单一的存储架构模型适用于所有 NoSQL 数据库，但通常推荐的方法是在每个节点使用本地存储（通常是基于闪存的）的分布式、无共享架构。

在存储硬件层面，直连存储（DAS）就是无共享架构的一个例子。这种模型提供了 Cassandra 和 MongoDB 等业务关键型 NoSQL 数据库所需的高性能、低延迟、容错性和可用性。

虽然 DAS 具有显著优势，但它与当今数据中心削减资本支出（CapEx）、运营支出（OpEx）和可持续发展倡议的气候背道而驰。同时，共享网络存储系统（如存储区域网络（SAN））固有的关键数据服务在 DAS 中缺失。

然而，借助当今的 SAN 解决方案，您可以鱼与熊掌兼得：效率、数据服务、弹性，以及是的，还有高性能和低延迟。通过使用采用分解式、软件定义架构的供应商，将您的数据平台现代化为 SAN 模型，可以在不牺牲效率的情况下，提供您的 NoSQL 数据库所需的性能和容错能力。

## 为什么无共享架构在 NoSQL 中很常见

DAS 是一种用于性能敏感型工作负载（如 [NoSQL 数据库](https://thenewstack.io/nosql-database-growth-has-slowed-but-ai-is-driving-demand/)）的普遍模型，因为从历史上看，本地闪存，尤其是 [非易失性内存高速 (NVMe) 存储](https://www.lightbitslabs.com/nvme-over-tcp/?utm_source=TNS&utm_medium=article&utm_campaign=nov)，比通过网络访问的传统共享存储（如 SAN 或 NAS）提供了显著更低的延迟和更高的 IOPS（更快的读/写操作）。稍后将详细介绍。

大多数 NoSQL 数据库旨在实现横向扩展和无共享架构，其中每个节点都是独立的并管理其数据，这使得横向扩展更加简单高效。

此外，一些 NoSQL 数据库是明确为分布式、无共享系统设计的。例如，在 Cassandra 中，集群中的每个节点负责一部分数据，并使用其本地磁盘进行存储。虽然 MongoDB 有灵活的部署方式，但由于其副本集和分片架构，它与 DAS 高度契合。当数据被分区并在多个节点间实现复制时，弹性会更高。如果一个节点发生故障，只有一部分数据会暂时不可用，系统可以继续使用其他节点上的副本运行。高弹性是业务关键型数据库工作负载的要求。

## 无共享架构的权衡

虽然 DAS 提供了显著优势，但它也带来了与当今数据中心倡议（如减少数据中心蔓延和能源消耗、降低运营开销、以经济高效的方式大规模管理指数级数据增长、支持企业可持续发展准则等）背道而驰的妥协和权衡。

从本质上讲，由于在 DAS 模型中每个节点都有自己的专用存储，这需要更多的硬件。硬件资源通常会被过度配置以适应不可预测的需求，从而导致资源利用率低下和容量闲置。DAS 环境中存储资源的利用不足可能非常显著，可能在 30% 到 70%（甚至在某些情况下更高）之间。

[![](https://cdn.thenewstack.io/media/2025/10/9e7af2bf-image1-1024x276.png)](https://cdn.thenewstack.io/media/2025/10/9e7af2bf-image1-1024x276.png)

*来源: Lightbit Labs*

在大规模部署时，DAS 模型的资本支出和运营支出负担会使 IT 预算膨胀。管理大量潜在独立节点上的存储会增加管理开销。监控、升级和容量规划必须在单个节点上执行。

如果说膨胀的 IT 预算还不够痛苦，那么对于那些实施 DAS 模型的人来说，最大的痛点是牺牲了 SAN 平台常见的数据库管理功能。高级数据管理服务（压缩、精简配置、快照、重复数据删除、分层、克隆、复制）在无共享模型的存储层中并非固有可用。在 DAS 模型中，如果可用，这些功能必须在应用层实现。

## NoSQL 的新存储范式

鉴于资本支出和运营支出预算压力的动态，以及可持续发展倡议和减少当今数据中心普遍存在的蔓延的需求，人们正转向共享存储平台，如 SAN，它可以充分替代高性能 NoSQL 工作负载的无共享架构。现代 SAN 系统可以实现与本地 NVMe 相媲美的性能，并支持高要求的 NoSQL 工作负载。

现代 SAN 能够实现与本地闪存相当的性能，“锦上添花”之处在于高速互连技术。忘掉光纤通道（FC）SAN 和 iSCSI 吧。采用 [NVMe over Fabrics (NVMe-oF)](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) 设计的 SAN 将 NVMe 闪存的性能优势扩展到网络结构，与 iSCSI 等传统块协议相比，显著降低延迟并提高吞吐量。这使得 NoSQL 应用程序能够以更接近本地闪存的性能访问共享存储，从而弥补了 DAS 的一个关键优势。

[NVMe over TCP](https://www.lightbitslabs.com/nvme-over-tcp/?utm_source=tns&utm_medium=article&utm_campaign=nov) (NVMe/TCP) 作为 NVMe-oF 的一个子集，结合了 NVMe 的高性能和使用 TCP 作为传输层的标准以太网网络的普遍性和成本效益。与 FC 不同，NVMe/TCP 在无处不在且经济高效的以太网基础设施上运行。这种架构模型确保了超低延迟和高吞吐量，无需定制硬件或专有驱动程序。

许多组织正在通过将 NVMe/TCP 与分解式和 [软件定义系统](https://thenewstack.io/how-software-defined-storage-empowers-developers/) 相结合，将其现代化举措提升到新的水平。该模型弥合了本地存储性能和资源效率之间的差距。一个采用 NVMe/TCP 作为传输协议的分解式 [软件定义存储](https://www.lightbitslabs.com/product/?utm_source=TNS&utm_medium=article&utm_campaign=nov) 架构满足了大规模支持高性能 NoSQL 工作负载的所有要求：更低的资本支出和运营支出、减少数据中心蔓延和支持可持续发展倡议、弹性、高性能和效率。同时，这些组织通过降低对专有硬件和复杂供应链的依赖，降低了业务风险。

[![](https://cdn.thenewstack.io/media/2025/10/0cd0ccd7-image2-1024x316.png)](https://cdn.thenewstack.io/media/2025/10/0cd0ccd7-image2-1024x316.png)

*来源: Lightbits Labs*

## 总结

尽管由于性能优势，带有 DAS 的分布式、无共享架构一直是高要求 NoSQL 数据库的历史推荐方案，但存储技术已经发展到提供具有更大业务效益的现代解决方案。

对于较小的集群，DAS 可能足够，但大规模部署时，它在操作和经济上都变得沉重。如果您的组织面临优化数据中心成本、增强可持续性和简化操作的压力，那么您应该重新评估您的无共享 DAS 模型。

现代 SAN 解决方案，明确为分解式、软件定义架构和 NVMe/TCP 等高速互连而设计，提供了一个引人注目的替代方案。它们有效地弥合了性能差距，同时提供了 DAS 本身缺乏的关键数据服务和效率。

通过采用这种现代存储范式，组织确实可以鱼与熊掌兼得，实现业务关键型 NoSQL 数据库所需的高性能和低延迟，而无需牺牲共享存储基础设施的经济和运营效益。

从无共享模型转向共享、分解式和软件定义模型，不仅能支持您当前的 NoSQL 工作负载，还能为持续增长、扩展和应用程序需求提供面向未来的数据基础设施。

要了解更多关于使用支持 NVMe-oF 的现代 SAN 支持 NoSQL 工作负载的信息，请阅读我的博客文章“[NVMe 存储：闪电般快速数据访问的初学者指南](https://www.lightbitslabs.com/blog/nvme-storage-a-beginners-guide-to-lightning-fast-data-access/)”。