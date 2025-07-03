为了跟上当今高性能工作负载的步伐，数据中心现代化势在必行，尤其是在金融服务和电子商务领域，这些工作负载的增长尤其迅速。

[软件定义存储（SDS）](https://thenewstack.io/modernization-storage-strategies-for-the-cloud-era/) 承诺提供更高的敏捷性、可扩展性和更低的成本，使其成为平台架构师精简、软件驱动基础设施愿景中引人注目的一部分。

现代化的一个常见优先事项是淘汰传统的 Fibre Channel (FC) SAN，它们被认为是过时且复杂的。虽然对于许多应用程序工作负载来说仍然足够，但 SDS 块存储解决方案在性能上存在差距，这些解决方案被设计到传统的 FC SAN 中，无法支持组织的关键任务应用程序工作负载。

[块存储](https://www.lightbitslabs.com/blog/4-reasons-why-block-storage-is-gaining-momentum-in-the-enterprise/utm_source=TNS&utm_medium=article&utm_campaign=july)曾经是传统工作负载的主要存储层，现在正演变为高性能、加速数据管道的关键组件，推动业务发展。最具创新精神、发展最快的组织的平台架构师正在寻求弥合其关键工作负载的“最后一英里”差距，并消除 FC SAN 的块存储瓶颈，最终实现向完全软件定义数据中心的转型。

## SDS 的承诺与现实

虽然 FC SAN 管理的某些方面可能涉及软件工具，但其基本架构和对专用硬件的依赖使其与真正的 SDS 存在显着差异。SDS 是关于将存储服务与底层物理硬件分离，而 FC SAN 不符合这一核心原则。

真正的 SDS 为 FC SAN 提供了一个引人注目的替代方案。它具有诸多优势，包括硬件独立性和更大的灵活性，通过软件控制简化管理和自动化，以及提高可扩展性和弹性。SDS 承诺通过利用通用硬件和减少供应商锁定来提高成本效益。

开源 [Ceph Storage](https://www.lightbitslabs.com/blog/ceph-storage/utm_source=TNS&utm_medium=article&utm_campaign=july) 在数据中心中得到广泛使用，证明了 SDS 解决方案对于企业工作负载的很大一部分是可行的。 事实上，它已被证明对许多应用程序都是成功的，可以处理组织高达三分之二的应用程序工作负载存储需求。 然而，剩下的三分之一——那些具有大规模高性能要求的应用程序——通常会带来巨大的挑战，并且是平台架构师实现完全软件定义现代化愿景的最后一英里的障碍。

## 识别性能瓶颈

传统的块存储系统无法支持金融服务和电子商务中常见的各种类型的关键任务应用程序。

这些包括高交易、低延迟的应用程序，例如支持金融交易平台的数据库； I/O 密集型工作负载，例如大规模数据分析和实时处理系统； 以及需要一致且可预测性能的在线交易应用程序，即使是短暂的延迟峰值也会产生重大后果。

[Ceph Storage](https://www.lightbitslabs.com/blog/ceph-storage/?utm_source=TNS&utm_medium=article&utm_campaign=july) 是一个提供文件、块和对象存储的 SDS 系统，可以替代传统的 FC SAN。 然而，许多组织采用 Ceph 主要是为了其对象存储功能，并为其块存储需求选择其他选项。

块存储架构限制了其支持大规模高性能关键任务工作负载的能力。 原因如下：Ceph 最初用于旋转硬盘驱动器 (HDD)，在过去十年中逐步发展其架构，以利用闪存存储的进步。 最新版本的软件使用固态硬盘 (SSD) 进行元数据操作，从而提高了性能。 然而，许多优化 HDD 行为的核心设计元素仍然没有改变。

Ceph 最近集成了 [NVMe (Non-Volatile Memory Express) over TCP](https://www.lightbitslabs.com/nvme-over-tcp/utm_source=TNS&utm_medium=article&utm_campaign=july) 连接。 该实现涉及集成 Ceph 的 NVMe-oF (NVMe-over Fabric) 网关。 图 1 说明了网关如何通过 NVMe/TCP 将 RADOS 块设备 (RBD) 导出到客户端。 这种实现可能会增加由额外跳和协议转换引起的存储网络延迟。 这种模式可以提高 Ceph 的互操作性，但它偏离了 NVMe/TCP 结构架构最初的设计意图。

[![来源：IBM Storage Ceph 产品文档](https://cdn.thenewstack.io/media/2025/07/484e9ed8-image1.png)](https://cdn.thenewstack.io/media/2025/07/484e9ed8-image1.png)

来源：IBM Storage Ceph 产品文档

对于真正极端的 I/O 密集型工作负载，与传统的基于以太网的 SDS 相比，[NVMe-oF 解决方案](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) 可提供显着更低的延迟和更高的 IOPS。 虽然

Ceph 可以利用 NVMe 驱动器，但它不提供与专用 NVMe-oF 解决方案相同级别的直接 NVMe 结构优化。

FC SAN 架构中固有的软件开销，包括数据虚拟化和分布式存储管理，会引入延迟。 在网络上通过分布式存储实现一致的低延迟本质上更加复杂。

底层硬件的潜在限制，例如网络带宽和 SSD 性能，也可能成为瓶颈，尤其是在重负载下。 虽然通常是最小的，但当处理极高的 IOPS 和大规模低延迟要求时，这种开销可能成为重要的性能因素。

这种性能差异为寻求完全过渡到 SDS 的组织制造了一个巨大的障碍。

## 最后一英里的挣扎——真实世界的场景

为了更清楚地说明这一点，让我带您了解两个真实世界的场景。

一家金融服务组织旨在用 SDS 替换其 FC SAN，以实现更好的敏捷性和成本效率。 它已成功地将许多应用程序迁移到新的 SDS 系统。

然而，其高频交易平台（一种关键的创收应用程序）无法迁移。 它需要一种能够提供亚毫秒级延迟和数百万 IOPS 的块存储解决方案，而新的 SDS 解决方案无法始终如一地保证这种性能水平。 该组织的解决方法是专门为此应用程序维护一部分 FC SAN 基础设施，从而否定了完全软件定义数据中心的目标。

在这种情况下，性能差距代表了成功交易执行和潜在财务损失之间的差异。 为了实现最终愿景，它用原生设计的 [基于 TCP 的 NVMe 块存储](https://www.lightbitslabs.com/utm_source=TNS&utm_medium=article&utm_campaign=july) 替换了传统的 FC SAN，并成功清除了软件定义现代化的最后一个障碍。

一个快速增长的电子商务平台将其大部分存储需求（包括网站托管和产品目录）都使用流行的块 SDS。

然而，其实时库存管理系统对于准确的订单履行和防止超卖至关重要，这带来了巨大的性能挑战。 SDS 解决方案难以提供所需的读/写延迟和吞吐量。 这种存储瓶颈导致库存更新偶尔出现延迟，从而导致订单履行问题和客户不满。

为了清除障碍，该组织增强了其 Ceph 存储（它继续将其用于不太关键的数据），并为库存数据库添加了高性能的基于 NVMe 的块存储层。 这种增强模型优化了其 SDS 配置，以提高性能，同时保持对软件定义策略的遵守。

## 清除障碍：策略和解决方案

一些策略和解决方案可以帮助弥合 SDS 中的性能差距。 在 SDS 集群内部以及作为单独的层使用 NVMe 和其他高性能存储技术可以解决 I/O 瓶颈。 调查专为更高性能而设计的新兴的基于 NVMe 的 SDS 架构和技术（例如分解存储和计算存储）也至关重要。

对于真正极端的 I/O 密集型工作负载，与传统的基于以太网的 SDS 相比，[NVMe-oF 解决方案](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) 可提供显着更低的延迟和更高的 IOPS。 虽然 Ceph 可以利用 NVMe 驱动器，但它不提供与专用 NVMe-oF 解决方案相同级别的直接 NVMe 结构优化。 它的实现偏离了 NVMe/TCP 结构架构最初的设计意图，因此，它的块存储组件不适用于大规模的关键任务应用程序工作负载。

整体方法至关重要，要考虑应用程序需求、基础设施功能和成本影响。 没有一刀切的解决方案。 您必须仔细评估您的特定需求，并选择最能平衡性能、成本和可管理性的方法。

由于传统系统和 FC SAN 中固有的块存储功能的挑战，完全软件定义数据中心的实现常常被削弱。 正如您在此处所看到的，有大量的应用程序工作负载非常适合传统解决方案，但未能满足某些 I/O 密集型应用程序的性能需求。

这种“最后一英里”的性能差距可以通过现代基于 TCP 的 NVMe 块存储解决方案来克服。 这是一种有希望完全弥合性能差距的技术，使组织能够充分实现软件定义数据中心的愿景。

如果您想了解更多关于软件定义的基于 NVMe/TCP 的存储及其对数据中心现代化的变革性优势的信息，请下载这份 IDC 白皮书：“[NVMe Over TCP Enables the Democratization of Disaggregated, NVMe Storage](https://www.lightbitslabs.com/idc-research-nvme-over-tcp-democratizes-nvme-storage/?utm_source=TNS&utm_medium=article&utm_campaign=julyutm_source=TNS&utm_medium=article&utm_campaign=july)。”