**KubeVirt** 由 Red Hat 于 2016 年创立，其核心理念是让 Kubernetes 能够在[容器旁边运行虚拟机](https://thenewstack.io/kubevirts-architecture-crds-controllers-and-daemons/)。我们希望允许用户在与现代化应用程序相同的平台上运行传统工作负载。这依然是我们的工作，但自 v1.0 以来，其他项目已经证明它们可以基于其构建，并在更广泛的生态系统中集成 KubeVirt。让我们探讨一下 KubeVirt 的未来十年将带来什么。

诸如开放主权 AI 云（Open Sovereign AI Cloud, OSAC）等其他项目将其用于虚拟机、集群和裸金属服务。集群 API 提供商 KubeVirt（CAPK）将 KubeVirt 虚拟机用作 Kubernetes 节点。Flight Control 在边缘运行 virt-launcher，而无需完整的 KubeVirt 控制平面。

如今，KubeVirt 是一个 CNCF 孵化项目，贡献者来自 Nvidia、Microsoft、AMD、Intel、SUSE 等公司。社区正致力于推动 KubeVirt 成为 CNCF 毕业项目。v1.8、v1.9 和 v1.10 的增强功能追踪器展示了“下一个”在实践中的意义。从 v1.6 到 v1.10，队列从一小批项目增加到了一百多个。v1.9 包含了数十个新提案。KubeVirt 增强提案（VEP）流程是我们保持核心稳定的同时让队列不断增长的方法：代码先行之前的设计、单一追踪器，以及由特别兴趣小组（SIG）进行所有权管理。

在本文中，我将分享一些将塑造后续版本的工作：设备和新硬件、在不扩大核心的情况下扩展 KubeVirt、机密虚拟机、作为沙盒的虚拟机，以及可插拔的虚拟化栈。我的 KubeVirt 贡献者同事 Fan Zhang 和 Harshit Gupta 帮助解释了他们正在开发的功能。

## 设备、DRA 与新硬件

虚拟机上的 GPU 已经可以通过 Kubernetes [动态资源分配（DRA）](https://thenewstack.io/kubernetes-dra-gpu-scheduling/)来申请，而无需使用设备插件。此功能在 v1.9 中处于 Beta 阶段。相同的申请模型正在扩展到通用主机设备、网络设备（如 SR-IOV）以及 CPU。在不久的将来，虚拟机将能够请求 GPU、NIC 和 CPU，并让 Kubernetes 将它们作为一个协调的集分配。还有一项工作允许 KubeVirt 从虚拟机规范和来自供应商策略的输入中构建这些申请，而不是要求每个用户手写 ResourceClaim 对象。

> “这遵循了指导该项目自始至终的设计原则：倾向于使用 Kubernetes 原生的解决方案和机制，而不是构建孤立的虚拟化变通方案。”

这遵循了指导该项目自始至终的设计原则：倾向于使用 Kubernetes 原生的解决方案和机制，而不是构建孤立的虚拟化变通方案。DRA 允许我们提高设备和 CPU 分配的粒度。但还有许多其他例子，例如 Kubernetes 中的 Swap、ImageVolumes、卷填充器（volume populators）等，它们允许我们删除 KubeVirt 专有的路径，并使用集群已有的功能。

KubeVirt 贡献者（包括 Nvidia 工程师）一直在努力使 KubeVirt 能够在更新的 Nvidia 硬件上运行，例如 Grace Hopper、Grace Blackwell 和 Vera Rubin 系统。此功能首先在加速基础设施启用工作组中开发，目前正向主流推进。

## 机密虚拟机与可信执行

用户越来越希望在共享基础设施上运行敏感应用程序和 AI 工作负载，同时在执行过程中[保护其数据](https://thenewstack.io/confidential-ai-sensitive-enterprise-data/)和模型。机密计算利用硬件支持的可信执行环境提供隔离，包括在平台威胁模型中抵御特权主机软件。远程证明允许工作负载所有者在向其委托机密之前，评估有关该环境的证据。KubeVirt 正在扩大对机密虚拟机的支持，并探索与证明和机密发布服务的集成，包括来自机密容器（Confidential Containers）项目的 Trustee。

Kubevirt 的 AIE 和机密计算工作组联合负责人 Fan Zhang 解释说：“对于 AI 来说，信任边界应该延伸到整个执行路径——CPU、加速器以及它们之间的互连。工作负载所有者在释放敏感数据或模型密钥之前，需要通过证明来验证该环境。KubeVirt 提供了一个机会，通过熟悉的 Kubernetes 工作流将机密虚拟机、受保护的加速器和证明结合在一起。与机密容器和 Trustee 等项目的合作可以使这些保护措施更容易获得，同时帮助工作负载所有者控制对其数据和模型的访问。”

这项工作涵盖了英特尔信任域扩展（TDX）、AMD 安全加密虚拟化（包括 SEV-SNP）、IBM 安全执行，以及新兴的 Arm 机密计算架构（CCA）支持。在 KubeVirt v1.9 中，涵盖 AMD SEV 和 SEV-SNP 的功能开关（feature gate）升级到了 Beta 阶段，英特尔 TDX 支持保持 Alpha 阶段，IBM 安全执行支持达到了通用可用性（GA）。Arm CCA 的启用仍在开发中。

> “能力发现有助于确定虚拟机可以在哪里运行；证明有助于工作负载所有者决定是否信任其运行的环境。”

展望未来，贡献者正在探索跨集群节点更一致地发现 TEE 能力，帮助 Kubernetes 将机密虚拟机放置在合适的基础设施上。其他提案涉及证明初始化数据、证据处理，以及与外部验证和机密发布服务（如 Trustee）的集成。能力发现有助于确定虚拟机可以在哪里运行；证明有助于工作负载所有者决定是否信任其运行的环境。

对于加速工作负载，其雄心延伸至机密设备分配以及 CPU 与加速器之间的受保护通信。这些功能需要在硬件、固件、虚拟化栈、客体软件和证明服务之间进行协调支持。

这些工作处于不同的讨论和实现阶段。它们是否会包含在未来的版本中，将取决于社区的审查、集成和测试。

## 在不扩大核心的情况下扩展 KubeVirt

KubeVirt 是一个成熟的项目。其核心是有意受到保护的。一项功能不会进入 kubevirt/kubevirt，除非我们愿意长期为所有人支持它，而不会破坏已经运行的集群。这需要时间。有时社区并不确信功能 A 是否真正属于核心。这不应该阻止任何人去构建它。

> “一项功能不会进入 kubevirt/kubevirt，除非我们愿意长期为所有人支持它，而不会破坏已经运行的集群。”

我们正在遵循 Kubernetes 的可扩展性理念。用户应该能够在核心之外编写完整的功能，并且仍然获得 KubeVirt API 保证。

结构化插件就是这条路径。插件是一个集群范围内的对象：域钩子（domain hooks）、节点钩子（node hooks）、准入控制（admission）。域更改可以是 CEL 表达式，或者在钩子需要外部状态时使用边车（sidecar）。管理员可以查看并控制它。这在 v1.9 中是 Alpha 阶段。

## 可插拔的虚拟化栈

另一半是虚拟化栈本身。libvirt、QEMU 和 KVM 是 KubeVirt 的核心。这依然是默认选项，而且它是正确的默认选项。在 v1.8 中，我们将树内虚拟机监视器抽象层（Hypervisor Abstraction Layer）和微软的 MSHV 后端添加为 Alpha 阶段。然而，我们的目标是使虚拟化栈可插拔，以便用户能够扩展 KubeVirt，让 Cloud Hypervisor、OpenVMM 或 Firecracker 在树外（out-of-tree）运行，而无需分叉（fork）KubeVirt。这项工作仍在进行中。

微软高级软件工程师 Harshit Gupta 表示：“KubeVirt 通过将 Kubernetes 编排、存储和网络引入虚拟机，使客户能够使虚拟机工作流现代化。将这些优势扩展到建立在替代栈上的虚拟化解决方案增加了用户的灵活性。我们的提案建立在支持替代虚拟机监视器的基础工作之上，旨在通过可插拔的虚拟化框架将 KubeVirt 与其底层虚拟化栈完全解耦。它顺应了 KubeVirt 走向更大定制化和灵活性的趋势。我很高兴能参与这项工作，因为它有可能扩大 KubeVirt 在各组织中的采用率。”

可插拔性将需要重新架构 KubeVirt，以使用插件框架来选择特定的虚拟机监视器和 hypervisor，并且已经开始了实现这一目标的初始工作。[KubeVirt 增强提案 #82](https://github.com/kubevirt/enhancements/pull/311) 概述了主要的可插拔性工作。除了启用其他虚拟化平台外，将后端维护为插件还可以支持更好的测试和更简单的维护。

## 下一个十年

该项目始于十年前，其核心重点很简单：协助组织将传统虚拟机工作负载转移到 Kubernetes 上。如今，其使命已经演变为赋能团队部署现代的、下一代的平台。从 AI 推理和边缘部署到强化的多租户环境和新兴架构，社区仍然致力于推进虚拟机在平台上原生能够做到的事情。

最初作为一个通过 Kubernetes 编排虚拟机的雄心勃勃的实验，现在已经扩展成为整个生态系统。下一个十年将取决于贡献者如何将这些提案转化为稳定的功能。

**KubeCon + CloudNativeCon 将于 11 月 9 日至 12 日在盐湖城举行。**[**立即注册**](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)**！**