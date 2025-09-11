
<!--
title: Clockwork FleetIQ：打破AI网络瓶颈，降低高昂成本
cover: https://cdn.thenewstack.io/media/2025/09/51079913-donald-wu-mrgtyitjrna-unsplash-scaled.jpg
summary: Clockwork的FleetIQ提供跨栈可观测性，解决GPU集群中网络瓶颈问题，提高基础设施利用率和弹性。它与NVIDIA、AMD等硬件兼容，已被Nebius、Uber等采用，旨在优化AI工作负载，减少训练中断。
-->

Clockwork的FleetIQ提供跨栈可观测性，解决GPU集群中网络瓶颈问题，提高基础设施利用率和弹性。它与NVIDIA、AMD等硬件兼容，已被Nebius、Uber等采用，旨在优化AI工作负载，减少训练中断。

> 译自：[Clockwork's FleetIQ Aims To Fix AI's Costly Network Bottleneck](https://thenewstack.io/clockworks-fleetiq-aims-to-fix-ais-costly-network-bottleneck/)
> 
> 作者：Frederic Lardinois

GPU 的速度正在稳步提升，但随着企业、新云以及根深蒂固的超大规模企业希望从中获得更高的效率，瓶颈往往在于网络——以至于例如 NVIDIA 现在正在[投资](https://www.nvidia.com/en-us/networking/products/silicon-photonics/)硅光子技术，以提高网络速度和弹性。改进现有网络的一个关键是提高对这些 GPU 集群以及连接不同系统的网络的可见性。

[Clockwork](https://www.clockwork.io/) 最初是一个用于同步计算集群中时钟的工具和服务。但事实证明，一旦你知道一个数据包以亚微秒级的精度发送和接收的时间，你就也为监控解决方案奠定了基础，该解决方案可以跟踪大型集群中确切的瓶颈位置，无论你查看的是 CPU 还是 GPU。一旦你掌握了这些信息并添加了额外的监控功能，你也可以开始在机器之间调整这些功能。

与此同时，AI 工作负载——尤其是训练工作负载——对这些集群提出了很高的要求，网络通常成为这些高度分布式工作负载的瓶颈和错误来源，这可能需要从最近的检查点重新启动训练过程。

[![](https://cdn.thenewstack.io/media/2025/09/65196db3-clockwork-fleetiq.png)](https://cdn.thenewstack.io/media/2025/09/65196db3-clockwork-fleetiq.png)

图片来源：Clockwork。

Clockwork 的产品和解决方案副总裁 Dan Zheng 表示，这通常会导致数小时的工作丢失，并使训练运行的时间增加数天。

“如今，发生的情况是，你可能拥有非常好的针对 GPU、网络、存储的孤立信息，但是当一项作业运行缓慢时——这可能是一项训练作业，也可能是一项分布式推理作业——你试图查明问题所在，而且通常需要大量的努力才能弄清楚……我们能够提供跨栈**可观测性**，以便你可以快速识别问题所在，”Zheng 说。

该公司今天推出的 FleetIQ 为运营团队提供了这种**可观测性**，结合了有状态的容错能力（即使在面对基础设施故障时，作业也可以继续进行而不会中断）和自动性能优化，以帮助避免网络拥塞、争用和其他瓶颈。

[![](https://cdn.thenewstack.io/media/2025/09/e0815da9-clockwork-jitter.png)](https://cdn.thenewstack.io/media/2025/09/e0815da9-clockwork-jitter.png)

图片来源：Clockwork。

Zhen 解释说：“如果你查看 GPU 集群的可用性或正常运行时间，那么实际上你看到的最多也只能达到 90% 出头。” 就像网络设备或存储舱一样，单个 GPU 可能会发生故障。“因为我们位于边缘并拥有独特的视角，所以我们可以在软件层中执行有趣的操作。 我们统称其为软件驱动的 fabrics，因为我们认为瓶颈已从原始 GPU 计算转移到通信。”

Clockwork 团队最近聘请了前 Sysdig 和 Nimble Storage 的 CEO [Suresh Vasudevan](https://www.linkedin.com/in/suvasudevan/) 担任公司 CEO，他们认为其系统提供了对整个堆栈的完全**可观测性**，同时在很大程度上与硬件无关，尽管该团队确实必须深入研究不同的硬件组件如何与各种网络 API、传输协议和通信库（例如）进行交互。

[![](https://cdn.thenewstack.io/media/2025/09/a578dccb-clockwork-recover.png)](https://cdn.thenewstack.io/media/2025/09/a578dccb-clockwork-recover.png)

图片来源：Clockwork。

除其他外，该服务可以与 NVIDIA、AMD 等公司的 GPU 和加速器一起使用，并支持 NVIDIA 的 [NCCL](https://developer.nvidia.com/nccl) 和开源 [RCCL](https://github.com/ROCm/rccl) 库以及 InfiniBand 和以太网/[RoCE](https://www.roceinitiative.org/roce-introduction/) 等网络库。（网络工程师比大多数技术学科更喜欢首字母缩略词。）

展望未来，Clockwork 还计划更进一步地向上发展，并将其应用程序级别的监控引入其服务。 目前，像 FleetIQ 这样的工具对实际的应用程序（这些应用程序正在通过网络发送数据）知之甚少。

[Nebius](https://nebius.com/) 刚刚与微软、NScale、Uber 和其他几家大型公共和私有云运营商签署了一项重大 AI 基础设施协议，目前已经在使用 FleetIQ。

“我们正在 Uber 基础设施上推广 Clockwork，并期待在 Uber 的规模上体验他们的全部功能。 Clockwork 的软件驱动 fabric 为混合多云环境提供了基础**可观测性**，帮助我们提供最重要的事情：提高基础设施利用率、增强弹性，并最终为每天依赖我们平台的数百万用户提供更好的体验，”Uber 的首席架构师 [Albert Greenberg](https://www.linkedin.com/in/albert-greenberg-376a39/) 说。