
<!--
title: 裸机 Kubernetes：性能优势几近消失
cover: https://cdn.thenewstack.io/media/2025/07/e30640aa-balls-8442426_1280.jpg
summary: 文章讨论了在 Kubernetes 和容器基础设施中使用裸机与虚拟机的性能和运维优势。虽然过去裸机有性能优势，但现在虚拟机上的容器性能已接近裸机。大型云供应商如 AWS、GCP 和 Azure 都在虚拟机上运行 Kubernetes 容器基础设施。虚拟机在隔离、安全和运维控制方面具有优势，因此基于虚拟机的容器架构是更佳实践，除非有特定技术或业务原因需要裸机。
-->

文章讨论了在 Kubernetes 和容器基础设施中使用裸机与虚拟机的性能和运维优势。虽然过去裸机有性能优势，但现在虚拟机上的容器性能已接近裸机。大型云供应商如 AWS、GCP 和 Azure 都在虚拟机上运行 Kubernetes 容器基础设施。虚拟机在隔离、安全和运维控制方面具有优势，因此基于虚拟机的容器架构是更佳实践，除非有特定技术或业务原因需要裸机。

> 译自：[Bare-Metal Kubernetes: The Performance Advantage Is Almost Gone](https://thenewstack.io/bare-metal-kubernetes-the-performance-advantage-is-almost-gone/)
> 
> 作者：B. Cameron Gain

与虚拟机抽象层上的容器相比，在过去十年中，裸机在运行 [Kubernetes](https://thenewstack.io/kubernetes/) 和容器基础设施方面提供了性能优势。 但这种情况可能不会持续太久了。

一些结果表明，VM 上的 [容器](https://thenewstack.io/containers/) 在性能方面正在赶上裸机，netperf 基准测试表明，VM 实例保留了相对于裸机 99% 的性能。 与此同时，长期以来人们普遍认为，与裸机相比，VM 提供更直接的运维控制、隔离、安全性和其他优势。

对于那些以大型云供应商为例的人来说，Azure、GCP 和 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 都运行在 VM 上的 Kubernetes 容器基础设施，而不是依赖裸机。

在裸机上运行的概念大约在十年前出现。 部分原因是，在裸机上运行所有内容会更简单。 但最大的动机是性能——人们认为裸机的开销更少。

当时，技术案例听起来很合理。 但自那时以来，IT 复杂性增加了，技术团队需要支持多个工作负载、实施更严格的安全性、满足更严格的 SLA 以及采用云运营模式。 现在很明显，性能差距正在缩小。 因此，如今的 CIO、平台团队和架构师必须认真考虑裸机是否仍然是正确的方法。

## 虚拟化与裸机

[![](https://cdn.thenewstack.io/media/2025/07/102cbb65-screenshot-2025-07-07-at-7.36.04%E2%80%AFpm-1024x565.png)](https://cdn.thenewstack.io/media/2025/07/102cbb65-screenshot-2025-07-07-at-7.36.04%E2%80%AFpm-1024x565.png)
裸机节点是一台没有任何虚拟化层的机器，这与虚拟机 (VM) 或容器不同。 物理服务器直接在物理基础设施上运行操作系统或应用程序，而不是通过虚拟机监控程序或容器引擎。 这两种环境对[大规模部署容器](https://thenewstack.io/kubernetes-gets-back-to-scaling-with-virtual-clusters/)、隔离和其他考虑因素具有重大影响。

在裸机配置中，命名空间仅强制执行“软”资源限制。 软资源限制是由操作系统未严格执行的分配。 通过命名空间，如果其他工作负载需要这些资源，则可以超出这些限制。 这意味着，虽然资源（例如 CPU 和内存）已分配给容器或进程，但不能保证它们可用。 其他进程可能会占用它们，从而可能影响性能。

相反，基于 VM 的部署在虚拟机监控程序级别强制执行“硬”资源限制——例如 CPU、内存和磁盘。 硬资源限制是严格执行的，这意味着分配的资源被保留，并且不能被系统上其他地方的需求使用。 这种严格的执行提供了租户之间的强大隔离。

VM 隔离与硬资源限制之间的关系是直接的。 由于 VM 隔离是通过虚拟机监控程序强制执行硬资源限制来实现的，因此公共云提供商可以更精确地保证服务级别协议 (SLA)。

与此同时，如果没有通过硬资源限制实现的 VM 隔离，“嘈杂邻居”问题变得更加普遍。 在多租户环境中，来自 CPU 或内存密集型工作负载的性能干扰可能会降低其他租户的体验，因为仅靠软资源限制无法阻止一个工作负载影响另一个工作负载。 例如，当分析来自望远镜馈送的大量天体物理数据时，单个行为不当的容器可能会垄断资源并影响整体集群稳定性。

以前在裸机和 VM 上运行的 Kubernetes 之间存在显着的性能差距，但最近的基准测试表明，这种差距正变得越来越小。 因此，这些结果进一步怀疑了依赖裸机而不是容器化基础设施的主要好处。 但是，性能基准表明，这些好处已经减少。

根据基准测试（ReveCom 尚未验证这些结果，但很快会验证），在 VM 层上运行的容器表明，性能已在很大程度上赶上了裸机服务器。 Broadcom 的 [VMware](https://www.vmware.com/?utm_content=inline+mention) 基准测试 [报告的结果](https://www.vmware.com/docs/vsphere8-virtual-topology-perf) 比较了 vSphere 8 与裸机硬件，显示出可忽略不计的差异，甚至更低的延迟，具体取决于 CPU 配置。

对于使用 vGPU 的 AI/ML 工作负载，[MLperf](https://www.nvidia.com/fr-fr/data-center/resources/mlperf-benchmarks/) 基准测试显示了 Broadcom 的 VMware Cloud Foundation VM 平台实例如何 [保留相对于裸机 99% 的性能](https://blogs.vmware.com/cloud-foundation/2025/04/17/broadcom-delivers-near-bare-metal-performance-for-virtualized-ai-ml/)，例如。 具体而言，结果基于使用 MLCommons 虚拟化的 MLPerf Inference v5.0 工作负载，并在 SuperMicro SuperServer SYS-821GE-TNRT 和 Dell PowerEdge XE9680 上使用 VMware vSphere 8.0 U3。 这些结果意味着与在 GPU 环境中运行的虚拟化 AI/ML 工作负载相关的显着成本降低。

TechTarget 的 Enterprise Strategy Group 的分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 表示，节点实例的一个关键性能因素是它们是在 ESX 虚拟机监控程序上本机运行，还是使用第三方 Kubernetes 发行版的来宾集群的一部分。“如果 pod 直接在虚拟机监控程序上运行，则性能损失保持在最低水平。 同时，ESX 为 Kubernetes 应用程序提供了一个轻量级的 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 内核来共享，”Volk 说。“即使在虚拟化环境中有一点开销，集中式策略驱动的管理能力也更为关键，因为声明式管理是可扩展性的基础。”

Gartner 在“[使用 Kubernetes 的云原生基础设施解决方案路径](https://www.gartner.com/en/documents/4022711)”中指出，转向裸机通常需要 DevOps 团队放弃他们“久经考验的虚拟基础设施和相关的专业知识”。 在管理新的裸机环境时，他们必须在许多方面重新开始。

## 大型公共云

[![](https://cdn.thenewstack.io/media/2025/07/aeec5753-screenshot-2025-07-07-at-9.01.png)](https://cdn.thenewstack.io/media/2025/07/aeec5753-screenshot-2025-07-07-at-9.01.png)

IT 组织经常向公共云提供商寻求了解他们如何管理其基础设施，而三大云供应商对这些说法进行了超大规模测试。 通过依赖在其上运行容器的 VM 抽象，来自 AWS、GCP、Azure 或其他云提供商的 Kubernetes 服务几乎完全不是直接在裸机上运行其公共 Kubernetes 产品。 这些云供应商在其官方文档和演示文稿中声明，对于大多数工作负载，由于现代超大规模和硬件虚拟化改进，VM 上的容器与裸机之间的性能差异在很大程度上可以忽略不计。

继续强调使用 VM 进行超大规模扩展并不新鲜，这支持了这样一种说法，即即使 VM 和裸机之间存在缩小的性能差距，虚拟化的显着安全性和运营优势也远远超过了边际性能影响。 同样，延迟、CPU 和内存性能以及其他相关基准的损失仍然可以忽略不计。

早在 2020 年，re:Invent 上的官方 [AWS 演示文稿](https://aws.amazon.com/blogs/aws/reinvent-2020-liveblog-infrastructure-keynote/) 就指出，对于许多实例类型，“对于大多数工作负载，EC2 实例和裸机之间的性能差异可以忽略不计。” AWS 还表示，其 Nitro 虚拟机监控程序为大多数工作负载提供接近裸机的性能。

Microsoft 在其文档中指出，由于虚拟化技术的进步，对于大多数工作负载，VM 和裸机之间的性能差异可以忽略不计。[Microsoft 还声称](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/compute-benchmark-scores)“Azure VM 为大多数工作负载提供接近裸机的性能，尤其是在最新一代硬件和虚拟机监控程序改进的情况下。”

同样，Google 表示，由于虚拟化技术的进步，对于在 Google Cloud 上运行的大多数工作负载，[性能差异](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance)可以忽略不计。

## 结论

对于绝大多数工作负载来说，通过在裸机上运行 Kubernetes 和容器可以实现的性能优势微乎其微。 当然，这并不意味着它们永远不会有益——当权衡裸机部署中固有的风险以及虚拟化带来的好处时，它们不适合大多数用例。

如上所述，裸机始终存在 [安全](https://thenewstack.io/security/) 问题。 工作负载在同一个内核上运行，因此一旦攻击者访问服务器操作系统，就意味着可以访问整个工作负载——所有工作负载。

相反，当容器在 VM 上运行时，由于 VM 的隔离配置，单个受损的容器、集群或应用程序仍然是隔离的。

十年前，裸机提供了切实的性能优势。 如今，借助现代 CPU 和基础设施创新，基于 VM 的容器性能在大多数情况下可以与裸机相媲美或超过裸机。[测试始终表明，基于 VM 的 Kubernetes](https://thenewstack.io/kubernetes-troubleshooting-primer/) 平台相对于裸机实现了 90-110% 的性能。

以数十亿美元规模运营容器服务的主要公共云提供商选择基于 VM 的 Kubernetes。 由于该架构的严格隔离、强制资源限制和运营一致性，这些决策为企业 IT 领导者重新考虑裸机部署提供了令人信服的验证。

任何考虑裸机策略的组织都必须阐明这样做的明确、具体的技术或业务原因。 如果没有充分的理由，基于 VM 的容器架构仍然是默认的最佳实践。

在评估平台策略时，IT 决策者应检查每个物理主机部署的微服务数量以及单个裸机部署中存在的故障域。 还必须注意 [主动支持的 Kubernetes 版本数量以及如何在多个应用程序中管理自定义资源](https://thenewstack.io/flexibility-matters-when-setting-kubernetes-resource-limits/)定义 (CRD)。 应考虑典型 Kubernetes 升级所需的时间以及如何减少 Kubernetes 的表面积。

这些问题挑战了现有的假设。 通常，IT 领导者采用继承的实践，而不重新评估它们是否合适。 重新评估裸机策略可能会发现，曾经相关的优势现在已被现代需求所掩盖。

当每一毫秒延迟都很重要时，某些非常小众的用例仍然可能需要裸机。 这些实例可能包括高频交易应用程序，或者当合规性要求要求某些合同使用裸机服务器时。 但是，由于性能差距已在很大程度上缩小，因此对于绝大多数用例而言，投资于 [支持容器](https://thenewstack.io/terraform-beta-supports-multicloud-complex-environments/) 和 Kubernetes 的 VM 基础设施是目前最佳的资源分配方式。