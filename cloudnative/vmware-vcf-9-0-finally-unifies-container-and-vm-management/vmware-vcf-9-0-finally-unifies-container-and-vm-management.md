
<!--
title: VMware VCF 9.0 最终统一容器与虚拟机管理
cover: https://cdn.thenewstack.io/media/2025/06/d7414dc6-getty-images-tmca62kseh4-unsplash-1.jpg
summary: VMware VCF 9.0 通过集成 Kubernetes 和虚拟机，实现了统一管理，支持多种环境部署和现代 AI 工作负载。它在多云和私有云上运行虚拟机和容器，并通过 vSphere Supervisor 加速发布和升级。博通的收购推动了 VCF 的集成，提供了一个用于运行虚拟机和容器的许可证，以及一致的策略驱动管理。
-->

VMware VCF 9.0 通过集成 Kubernetes 和虚拟机，实现了统一管理，支持多种环境部署和现代 AI 工作负载。它在多云和私有云上运行虚拟机和容器，并通过 vSphere Supervisor 加速发布和升级。博通的收购推动了 VCF 的集成，提供了一个用于运行虚拟机和容器的许可证，以及一致的策略驱动管理。

> 译自：[VMware VCF 9.0 Finally Unifies Container and VM Management](https://thenewstack.io/vmware-vcf-9-0-finally-unifies-container-and-vm-management/)
> 
> 作者：B. Cameron Gain

未来数月和数周的使用情况和客户反馈将决定 [VMware](https://www.vmware.com/?utm_content=inline+mention) 是否成功完成了一项卓越的研发壮举：随着博通的 VMware Cloud Foundation (VCF) 9.0 正式发布，VMware 表面上已经实现了多年来 [DevOps](https://thenewstack.io/devops/) 中一直缺失的关键点。

也就是说，一个平台可以允许容器在 [Kubernetes](https://thenewstack.io/kubernetes/) 基础设施上和虚拟机 (VM) 并行运行，而无需一方受益于双方所能提供的全部功能。通过这种方式，容器和虚拟机可以受益于以前在单个 VMware 平台上无法获得的增强管理功能。

在发布之前，VMware 在很大程度上引领了多年来的虚拟机开发。其 Kubernetes 平台也与其他 Kubernetes 平台提供商不相上下，同时仍然是 Kubernetes 的最大贡献者之一。但此前，最好的工具和流程无法同时使用。借助 VCF 9.0，VMware 成功地更完整地整合了这两种基础设施，以实现统一管理。

根据 [博通](https://thenewstack.io/vmware-alternatives-a-strategic-guide-to-modern-virtualization/) 的说法，通过 9.0 版本，它通过添加更多服务、增强对多个 [K8s](https://thenewstack.io/kubernetes/) 版本的支持以及独立于 vSphere 升级 vSphere Kubernetes Service (VKS) 和 Supervisor 的能力来加速发布和升级，同时引入多集群管理等，从而增强了整体功能集。

私有云是 VCF 9.0 的重要组成部分。VMware 表示，虽然公有云在很多方面都存在不足，但 VCF 9.0 现在使基础设施能够在单个平台上为各种环境部署。这些环境通常包括不同数据中心的本地部署、托管和 [边缘环境](https://thenewstack.io/edge-computing/)，或者通过超大规模企业或云服务提供商提供的托管服务。

VMware 表示，这样的平台应该能够运行虚拟机和容器工作负载，以及现代 AI 工作负载——VCF 9.0 正是如此。VMware 表示，生命周期和策略通过平台在所有这些环境中进行管理。

## 并行

同样，VCF 被吹捧为在多云和私有云上运行虚拟机和容器的单一平台。VCF 对 Kubernetes 支持的关键组件是 VMware vSphere Supervisor，对于 VCF 9.0 而言，它是 vSphere Supervisor。

Supervisor 现在将其功能扩展为一个平台和一个控制平面，可以在其上配置一组基础设施和云服务，包括 Kubernetes 集群服务。这些服务包括 VKS（Kubernetes 运行时）、多集群管理、VM 服务、vSphere Pod、网络服务、存储和备份服务、身份和访问控制服务、镜像注册表以及作为 VKS 附带的软件包一部分提供的许多其他功能。此外，由于 VMware 提供经过 [云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention) 认证的 Kubernetes 发行版，因此该平台是开放的，并且可以扩展到符合 CNCF 标准的第三方服务。

TechTarget 旗下 Enterprise Strategy Group 的分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 告诉我，VCF 9.0 中的 vSphere Supervisor 是“最终使 [容器化应用程序](https://thenewstack.io/containers/) 能够与虚拟机并行原生运行的秘诀”。“事实上，它可以与不同的 Kubernetes 发行版和不同版本的上游 Kubernetes 配合使用，这一点至关重要，因为 Supervisor 允许当前的 VMware 客户通过 vSphere 控制台管理他们当前的大部分 Kubernetes 环境。”

自从容器“成为现实”以来，VMware 一直是领先的 Kubernetes 管理和基础设施服务提供商之一，也是过去十年中 Kubernetes 项目的三大贡献者之一。但这还不够。

在其 2023 年被 [博通收购](https://thenewstack.io/vmware-to-be-acquired-by-broadcom-in-a-61-billion-deal/) 之前，VMware 的大部分 Kubernetes 知识产权 (IP) 并未被客户充分利用。VMware 当然有很多东西可以提供，但它没有一个通用平台，使处于 Kubernetes 发展不同阶段的公司能够满足他们对虚拟机和 Kubernetes 容器的所有需求。

通过 VCF 转向 Kubernetes 主要涉及 Kubernetes 运行时（VKS，以前称为 Tanzu Kubernetes Grid Service）及其著名的虚拟机和支持基础设施的更深入集成。

博通的收购是 VMware 将其整个私有云堆栈和服务集成到 VCF 中的催化剂。虽然 VMware 以前在 VCF 堆栈中拥有许多基础设施和管理组件，但博通帮助带来了急需的重点——以及支持组织满足其 Kubernetes 运行时和统一管理全部需求的能力。Kubernetes 运行时许可证已经包含在 VCF 许可证中，因此无需额外的许可证。

Volk 表示：“拥有一个用于运行虚拟机和容器的许可证，并在同一 vCenter 的管理下，这非常有意义，因为这对于跨工作负载和位置进行一致的策略驱动管理至关重要。”

## 裸机失宠

在展示 VCF 9.0 时，VMware 提出了一个强有力的论点，支持选择虚拟机上的容器结构，而不是裸机基础设施。

虽然裸机基础设施以前是实现比在虚拟机层上运行容器所提供的抽象更高的运行时效率的优化方法，但证据表明虚拟机上的容器在性能方面已在很大程度上赶上了裸机服务器。除了 VMware 之外，主要的公有云提供商也采用了在虚拟机上部署容器的结构。这包括 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 以及它目前默认情况下如何在 [EC2 虚拟机上运行 EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)，以及 [Google](https://cloud.google.com/?utm_content=inline+mention) 平台使用 [Compute Engine 虚拟机](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) 作为底层节点。[Azure 也在基础设施上使用虚拟机](https://learn.microsoft.com/en-us/azure/aks/core-aks-concepts)。

此外，与在裸机上运行的容器相比，虚拟机层在隔离和其他安全方面具有优势。这是因为在裸机上运行的容器直接依赖于内核，并且与在虚拟机抽象上运行以及此类部署提供的隔离相比，可能缺乏隔离。

VMware 表示，在虚拟机层上运行的容器的基准测试表明，性能已在很大程度上赶上了裸机服务器。博通 VMware 产品营销副总裁 [Prashanth Shenoy](https://www.linkedin.com/in/prashanthshenoy/) 在与记者和分析师的电话会议中表示，根据 [MLPerf 基准](https://github.com/mlcommons/inference) 测试，与裸机相比，VCF 保留了 99% 的性能。“好的，因此性能开销可以忽略不计，同时它提供了客户在过去 25 年中一直依赖的所有关键虚拟化优势。”

然而，性能取决于 vSphere Pod 是否在本机上在 ESX 虚拟机监控程序上运行，或者访客集群是否基于第三方 Kubernetes 发行版，Volk 说。“由于 vSphere Pod 直接在虚拟机监控程序上运行，因此性能损失保持在最低水平。同时，ESX 为 Kubernetes 应用程序提供了一个轻量级的 Linux 内核来共享，”Volk 说。“由于应用程序堆栈的两个组件之间存在无数的相互依赖关系，因此将 Linux 内核和 Kubernetes Pod 紧密结合在一起至关重要。”

Volk 说，当 VCF 管理基于第三方 Kubernetes 发行版的访客集群时，结果会有所不同。“这些集群在基于自己的标准 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 发行版的虚拟机中运行，从而在一定程度上产生了性能和 Linux 管理开销，同时以 vSphere Supervisor 的形式提供了一个统一的管理平面，”Volk 说。“总的来说，我发现无缝和统一的多集群管理能力比裸机辩论重要得多。即使在虚拟化环境中存在一点开销，集中式策略驱动的管理能力也重要得多，因为声明式管理是可扩展性的基础。”

## AI 处理

VMware 表示，VCF 不仅仅提供敷衍的 AI 和代理支持。在与分析师和记者举行的电话会议上，总部位于阿拉斯加的电信公司 [GCI Communications](http://GCI%20Communications) 的首席技术战略顾问 Roger Joyce 表示，GCI 一直依靠 VCF 9.0 作为客户 Beta 测试人员。

他强调了使用 VCF 9.0 支持异构硬件平台的重要性，并表示 GCI 计划利用 VCF 9 的高级服务，包括私有 AI 和数据服务。Joyce 说，VCF 9.0 数据服务为 [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/)、[MySQL](https://thenewstack.io/linux-back-up-a-mysql-database-from-the-command-line/) 和其他数据库提供企业支持，私有 AI 更新包括气隙支持、GPU 即服务和 GPU 监控。

Joyce 强调了构建安全、高性能的私有云基础设施以满足 GCI 的运营和监管需求的重要性。“作为阿拉斯加最大的电信提供商，由于其距离主要超大规模企业较远，GCI 面临着独特的延迟和连接挑战。这种地理现实使得首先采用公有云策略变得不切实际，”Joyce 说。

相反，Joyce 和他的团队选择了采用 VCF 的私有云方法，这为他们提供了必要的技术能力，以便在“本地安全环境中”提供类似云的自助服务和自动化，Joyce 说。

虽然 Joyce 没有明确强调 GPU，但他对 GCI 不断发展的私有云功能的描述与 VMware 在 VCF 9.0 中的增强功能相符，尤其是在对私有 AI 的支持方面。这些功能包括 GPU 即服务、增强的 GPU 监控以及对气隙环境的支持——所有这些对于在电信等受监管行业中安全高效地运行现代 AI 工作负载至关重要。

正如他所描述的那样，目标是使内部开发团队能够快速安全地进行创新，而无需默认使用公有云选项。VCF 使 GCI 能够提供与公有云平台相同的速度和灵活性，同时保持严格的数据治理并利用资本投资——这是涉及敏感数据和高性能计算的 AI 工作负载的关键要求。

博通对 VCF 9.0 高级服务的其他改进包括：

* 通过 VMware Live Recovery 增强的灾难恢复和勒索软件保护。这包括支持恢复到隔离的本地或辅助数据中心。
* 增强的 vSAN 存储集群，允许从计算集群独立扩展存储。
* VMware vDefend，用于 VMware 所谓的“自助服务微细分”和横向安全。
* VMware Avi 负载均衡器，它将消费体验与 VCF 9.0 集成，以及 Avi 控制器的生命周期管理、单点登录和密码轮换。