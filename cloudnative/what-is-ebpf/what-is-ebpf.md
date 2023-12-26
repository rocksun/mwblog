
<!--
title: eBPF终极指南
cover: https://cdn.thenewstack.io/media/2023/11/4a21b028-ebpf-copy-1024x532.png
-->

eBPF代表扩展的伯克利数据包过滤器。在这份全面的技术指南中，了解关于Linux eBPF的所有重要信息。

> 译自 [What Is eBPF? The Ultimate Guide](https://thenewstack.io/what-is-ebpf/)，作者 B. Cameron Gain 是 ReveCom Media 的创始人和首席分析师。他对计算机的迷恋始于在上世纪80年代初在当地的游戏机厅里黑客入侵 Space Invaders 游戏机，整天只需花费25美分。然后...

eBPF（扩展伯克利数据包过滤器）是目前备受瞩目的技术之一，已经在云原生环境中证明了其价值和适用性。它能够提高计算效率，增强众多工具和平台的计算能力，尤其在安全性、可观测性和网络方面表现出色。

eBPF 的架构包括程序验证、助手调用、eBPF 映射、预定义的挂钩（hooks）、函数和尾调用等要素。

那么，[eBPF除了是云原生技术外](https://thenewstack.io/ebpf-offers-a-new-way-to-secure-cloud-native-systems/)，它从何处获得超能力呢？eBPF的强大之处主要体现在其与Linux内核的直接关联，这使其具有卓越的计算效率。然而，仅将eBPF标记为[基于Linux内核的工具](https://thenewstack.io/how-io_uring-and-ebpf-will-revolutionize-programming-in-linux/)是误导的，因为其影响扩展到了应用程序层面。

eBPF之美的一个显著方面在于，它已通过开源项目以各种方式被使用和应用。与[WebAssembly](https://thenewstack.io/webassembly/)等技术不同，后者承诺提供计算效率，并能够同时在端点之间启动命令，但由于标准化方面的挑战，WebAssembly在不同端点用例中的适用性受到了限制。

## eBPF与其他技术有何不同？

使用行业术语来说，它在沙盒中运行，并提供各种功能，可扩展到用户进程，涵盖了从可观测性、安全性、网络、跟踪到充当 [Sidecar 和服务网格](https://thenewstack.io/ebpf-or-not-sidecars-are-the-future-of-the-service-mesh/)替代品的各种用例。

不想过度使用术语"沙盒运行"，可以说 [eBPF 是在内核内部运行](https://thenewstack.io/ebpf-put-the-kubernetes-data-plane-in-the-kernel/)的，允许与其配套的运行时在封闭的环境中运行。换句话说，它消除了潜在的攻击矢量，因为[恶意行为者](https://thenewstack.io/how-developers-can-thwart-bad-actors/)无法像在容器、Pod 或其他共享权限的地方运行时那样写入或访问它。

eBPF 被以多种方式利用，并已成为许多成功商业项目的基础。对于安全目的，它一直是推动力。克服曾经阻碍 eBPF 采用的障碍为各种工具和平台铺平了道路，这些工具和平台不仅克服了这些挑战，还提高了在安全性、可观测性、网络和其他应用程序方面的效率。

这主要是因为希望利用 eBPF 的公司或组织可能缺乏内部开发超大规模者或直接利用 eBPF 优势的专业知识。这就是 BPF 工具提供商和平台提供商发挥作用的地方。他们的专业知识填补了这一空白，包括对 Linux（技术上是 Unix）的了解，以创建使用内核代码运行 eBPF 应用程序或设备所需的过程。此外，一些 [Linux 内核不支持 eBPF](https://thenewstack.io/how-ebpf-turns-linux-into-a-programmable-kernel/)，但工具提供商已经克服了这个限制。

## 如何准备使用 eBPF？

然而，由于eBPF代码存放在Linux内核中，一些安全问题可能会引起关注：

“在内核中执行自定义代码，从定义上总是为坏人创建了一个攻击面，以便利用，”[企业管理协会（EMA）](https://www.enterprisemanagement.com/)分析师[Torsten Volk](https://www.linkedin.com/in/torstenvolk)表示。“然而，对策非常类似于确保整个堆栈安全性的对策：更新您的内核，确保对所有eBPF应用进行集中监控，应用一套中央安全策略，并创建集中审计是这一战略的关键支柱之一。”

Gartner提供以下用户建议：

- 对于仍在使用具有有限或无eBPF支持的eBPF Linux发行版的组织，迁移到更现代的平台。
- 在考虑规模、性能、可见性和安全性时，寻找[eBPF Kubernetes](https://thenewstack.io/can-ebpf-agent-in-kubernetes-be-the-key-to-better-observability/)容器网络基础设施（CNI）解决方案。
- 使用提供eBPF支持的eBPF Linux变体，以启用网络性能、可见性和eBPF安全产品。
- 通过支持技术先进的企业，探索eBPF是否能够有意义地解决组织的性能或可见性挑战。
- 投资于eBPF以提高性能和可见性，避免落后于竞争对手，用于网络和网络安全供应商。

Volk表示，eBPF直接监视和与系统调用、线程和进程交互的能力，再加上实时访问延迟和利用率指标，使其成为[安全性和可观测性](https://thenewstack.io/tetragon-1-0-promises-a-new-era-of-kubernetes-security-and-observability/)应用的优秀平台。

简而言之，“eBPF非常适用于快速变化的微服务应用，因为可以跨云监控服务器节点，并且可以在没有手动插装的情况下跟踪函数调用的延迟，只要它们运行的是具有eBPF支持的Linux系统，”Volk说。“利用eBPF的能力是一个毫无疑问的选择，因为这项技术可以逐渐采用，而无需放弃传统的可观测性、网络或安全工具。”

## eBPF是否“基于”Linux内核？

经常有人写和说eBPF是“基于”Linux内核的。这并不完全正确。通常情况下，当使用“基于”来描述一项技术时，首先需要定义或描述Linux内核及其与eBPF的关系。

Linux内核被认为是Linux操作系统的核心代码或核心。例如，内核确定哪些用户进程和驱动程序有限的访问权限，以执行其功能。

但是，eBPF功能并未改变内核；相反，它直接访问CPU和内存。请记住，内核在某种意义上充当中介者，因此eBPF并没有更改内核代码。然而，通过以某种方式绕过内核，它直接运行并与CPU和内存直接连接。

因此，其强大的一个重要来源与[WebAssembly类似](https://thenewstack.io/webassemblys-status-in-computing/)。尽管与WebAssembly存在逆向关系，因为它在WebAssembly模块内的代码分布到的端点处与CPU进行交互。

以这种方式，eBPF运行、添加或甚至扩展了Linux内核作为操作系统的一个特性，更具体地说，是内核本身。再次强调，由于它是内核的一部分，这个Linux基金会项目基本上可以扩展到任何兼容Linux的用户进程和应用程序运行的地方。这种扩展范围涵盖了从数据中心的服务器到云原生应用程序的高度分布式[Kubernetes](https://thenewstack.io/kubernetes/)环境。

[微软是eBPF基金会的创始成员之一](https://thenewstack.io/microsoft-brings-ebpf-to-windows/)，于2021年与Google、Isovalent、Meta和Netflix共同创建，并再次成为Linux基金会的项目。尽管与Linux操作系统相比，微软几乎不是Windows的主要支持者，尽管相对于Linux操作系统存在充分记录的性能、安全性等问题。这解释了eBPF for Windows的存在。

尽管eBPF for Windows尚未像其Linux eBPF对应物那样广泛采用，微软仍然继续展示其使用和多个挂钩的示例。

微软将eBPF描述为不仅仅是Linux内核的一部分，而是操作系统的一部分——具体来说是Windows操作系统。

## eBPF存在哪些安全风险呢？

但eBPF代码直接运行在内核中，难道不会带来安全风险吗？

eBPF如何与Linux内核集成可能会引发一些安全担忧。毕竟，除了攻击者外，没有人希望恶意代码直接访问操作系统和CPU。

为了解决这一eBPF安全问题，[eBPF验证器](https://docs.kernel.org/bpf/verifier.html)检查代码，并仅在验证程序在GPL下授权后才授予eBPF写权限，以帮助确保其安全性和兼容性。当然，没有什么是完全防不胜防的，但直到目前为止，通过eBPF在内核级别策划的重大攻击并未被报告。

## BPF与eBPF之间有什么区别？

首次报告的BPF实例是在2010年，伯克利数据包过滤器与Linux内核编译器合并。其首次报告用于非网络目的的用途归功于Google首席软件工程师Will Drewry，他发现将BPF配置为网络层可作为Linux内核的适当seccomp（安全计算模式）。这一2012年的[报告](https://lwn.net/Articles/475043/)成为安全和其他挂钩的起源，为更令人激动的发展奠定了基础。

如果考虑独立的BPF，它主要用于高效处理数据包，而eBPF则扩展了这些能力。据报道，eBPF的[首次实例](https://lore.kernel.org/netdev/1396029506-16776-1-git-send-email-dborkman@redhat.com/)出现在2014年，然后，如今一样，仍然在不断发展。最初主要专注于网络，后来扩展到包括系统调用和其他功能，偶尔还会合并相似的元素。这种扩展导致了“[完全扩展的伯克利数据包过滤器](https://prototype-kernel.readthedocs.io/en/latest/bpf/)”这一术语的出现。

从BPF到eBPF的命名差异甚至可以归因于营销，ARMO的首席执行官兼联合创始人[Shauli Rozen](https://il.linkedin.com/in/shaulirozen)说道，该公司提供由Kubescape提供支持的企业级[Kubernetes安全](https://thenewstack.io/6-kubernetes-security-best-practices/)平台ARMO Platform。

“这是重新激发对尚未获得巨大关注的强大事物的兴趣的一种方式，”Rozen说。“ARMO使用了大量来自BPF的可观测性数据，以增加安全措施的价值并协助进行优先排序。基于生成的可观测性数据，您了解到正在实施的安全工作，以增强您的环境。”

**eBPF为网络，特别是在云原生环境中，带来了哪些特别之处？**

[eBPF](https://thenewstack.io/performant-and-programmable-telco-networking-with-ebpf/)还被证明在网络生产力方面取得了显著的收益。这主要是因为eBPF位于内核中，因此直接将流量导向CPU。在许多情况下，诸如XDP负载平衡的技术都被这些网络功能所取代。

eBPF具有用于[观测性](https://thenewstack.io/groundcover-simplifying-observability-with-ebpf/)和安全性的内置功能。当然，这也是通过在整个网络中预先实现的挂钩实现的。这要归功于嵌入在内核中的这些挂钩。

## 什么是XDP？

XDP代表Express Data Path（快速数据路径）。当然，这有助于在不同的通信层之间传输数据包和观测性，包括第七层的HTTP、DNS或gRPC，第四层的TCP，IP层，第三层等等，当然还包括第二层的Ethernet和WiFi。

eBPF允许在这些不同层之间进行通信。这样，效率也与内核如何使用BPF作为仲裁者来指导数据包流向相关。在沙盒环境中，减少了数据包丢失等风险。当然，这些数据包的数据可以通过eBPF沙盒化代码直接实时修改。

其中一个重要的项目是[Cilium，这是一个开源项目](https://thenewstack.io/supercharge-service-mesh-with-ebpf-and-cilium/)。Cilium提供网络、可观测性和eBPF安全解决方案。在网络方面，其使用范围涵盖了第三层到第七层的网络层。Cilium还为Kubernetes环境中的Pod和外部服务之间的流量提供了分布式负载平衡的便利和实现。

这包括集成的ingress/egress、网关、带宽管理、[服务网格和深度网络安全](https://thenewstack.io/implementing-a-secure-service-mesh/)。在服务网格方面的公共可见性监视显示出了很多潜力，替代了sidecar组件。在使用服务网格管理Kubernetes集群和Pod时，sidecar似乎会减缓数据流量。

## eBPF在Kubernetes中的使用方式是怎样的？

出现了许多依赖eBPF来检测威胁和执行安全策略的平台和[eBPF工具](https://thenewstack.io/ebpf-tools-an-overview-of-falco-inspektor-gadget-hubble-and-cilium/)。如上所述，将eBPF应用于安全的努力主要始于BPF开始作为Linux内核和访问内核的进程的适当seccomp的时候。

一个正确使用eBPF的平台应该能够让DevOps团队[监控在Kubernetes集群中应该运行的内容](https://thenewstack.io/using-prometheus-to-monitor-kubernetes-clusters-running-cloud-foundry/)，并在违反策略或检测到安全威胁时提供可执行的结果。

以Kubernetes安全提供商ARMO的开源Kubescape为例，这个[Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline-mention)的沙盒项目涵盖了Kubernetes应用程序的生命周期及其更新。

这包括用于风险分析、安全、合规性、错误配置扫描和镜像扫描的IDE、[CI/CD流水线](https://thenewstack.io/the-biggest-security-risks-lurking-in-your-ci-cd-pipeline/)和集群。网络策略和安全策略等加固建议也作为开源贡献的一部分。

Kubescape用于与您的DevOps团队所需的平台工具清单集成，例如软件物料清单（SBOM）、签名扫描和策略控制。它从开发周期的一开始就开始运行扫描，并在整个CI/CD以及部署和集群管理过程中延伸。

ARMO最近提供的eBPF功能之一涉及漏洞相关性和优先级。相关性和优先级允许ARMO平台和Kubescape用户将属于未使用的软件包和组件的漏洞降低优先级。通过首先降低较不重要的漏洞的优先级，用户可以集中精力解决对其运行的集群构成更大威胁的漏洞。

“你无法保护看不见的东西，这就是为什么可观测性至关重要的原因，” Rozen 表示。“事实上，充分利用来自 eBPF 的大量可观测性数据，并将其应用于帮助 DevOps 团队对真正需要关注的安全威胁和漏洞进行优先排序并采取行动是关键。”
