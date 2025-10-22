Kubernetes 已成为现代容器化应用的核心支柱，然而，企业 IT 中越来越多的讨论集中在它是否也应成为虚拟机（VM）的归宿。这不仅仅是关于平台整合，它触及了更广泛的技能、预期和迁移问题，这些问题正在塑造董事会和行业会议上的战略决策。

在单一控制平面下同时运行虚拟机和容器的能力具有明显的吸引力。它承诺操作一致性、潜在的成本节约以及为平台团队提供简化的基础设施视图。然而，这种融合并非没有重大挑战。这种转变需要新的技能，它对 [Kubernetes](https://thenewstack.io/kubernetes/) 本身提出了新的要求，并引入了一个复杂的迁移问题。

## 虚拟机运维人员的技能鸿沟

围绕 [VMware](https://tanzu.vmware.com?utm_content=inline+mention)、Hyper-V 或 [Nutanix](https://www.nutanix.com/solutions/cloud-native?utm_medium=redirect&utm_content=inline-mention) 建立职业生涯的运维人员本能地理解数据存储、端口组和快照等概念。这些构造与物理服务器和传统 IT 实践紧密相关。相比之下，Kubernetes 需要一种新的思维模式。

Pod 是短暂的。部署和服务定义了期望状态。网络是策略驱动的，存储是抽象的。管理通常通过 YAML 文件和 API 而不是图形控制台进行。作为一名前 VMware 管理员，我习惯于在 vCenter 中拖放虚拟机；这不是平台工程师会考虑对其 Pod 进行的操作。对于习惯于稳定状态虚拟机的团队来说，这可能感觉像是一种令人迷失方向的转变。

开源 [KubeVirt](https://thenewstack.io/open-source-kubevirt-vm-management-with-kubernetes-is-a-work-in-progress/) 项目走在解决这一鸿沟的最前沿。它扩展了 Kubernetes 以管理虚拟机，其方式与管理容器大致相同，通过 Kubernetes API 暴露熟悉的构造。[红帽](https://www.openshift.com/try?utm_content=inline+mention)通过 [OpenShift Virtualization](https://thenewstack.io/virtualization-and-containers-better-together/) 的独立许可进一步推进了这一点，该许可旨在帮助那些仍希望将 Kubernetes 作为其控制平面但需要专注于托管虚拟机的组织。

对此话题的兴趣显而易见。我自己的深度指南“[KubeVirt for vSphere 管理员](https://veducate.co.uk/kubevirt-for-vsphere-admins-deep-dive-guide/)”已成为我阅读量最高的帖子之一，这表明虚拟机运维人员正在积极寻找将其技能融入 Kubernetes 环境的方法。

## 对 Kubernetes 平台的不同期望

在 Kubernetes 上运行虚拟机也改变了企业对平台本身的期望。容器被设计为无状态和瞬态的，而虚拟机通常是有状态的、长期存在的并与持久存储绑定。弥合这两种模型需要在调度、存储处理和生命周期管理方面具有灵活性。

网络最清楚地说明了这一挑战。虚拟机工作负载经常依赖静态 IP、VLAN 和防火墙构造。Kubernetes 假定一个具有动态寻址和网络策略的扁平网络。协调这些世界并非易事。

这就是 [Cilium](https://thenewstack.io/breaking-the-chains-of-kube-proxy-with-cilium/) 等项目进入讨论的地方。Cilium 带来了由 [eBPF](https://thenewstack.io/what-is-ebpf/) 驱动的网络模型，这让使用过 NSX 等解决方案的虚拟机运维人员感到熟悉。它提供了微隔离、可观测性和安全控制，这些功能与传统虚拟机 SDN 平台的功能相呼应，但一致地应用于虚拟机和容器。对于探索这种融合的企业来说，它展示了 Kubernetes 网络如何演进以满足以虚拟机为中心的期望，而不会碎片化操作模型。

## 迁移困境

即使 Kubernetes 能够满足虚拟机的操作需求，迁移问题仍然存在。将工作负载迁移到基于 Kubernetes 的平台所涉及的远不止复制一个磁盘文件。

虚拟机绑定到特定于管理程序的设置。它们的磁盘通常驻留在专有存储系统上。它们的网络依赖于 Kubernetes 环境中可能不存在的构造。将所有这些映射到一组新的抽象是一个相当大的任务。

同样重要的是要认识到，我们不太可能看到 VMware 资产的全面迁移。大多数企业最近才完成其虚拟化计划。将所有工作负载迁移到容器可能需要数十年，就像大型机和物理服务器工作负载今天仍在运行一样。更现实的是选择性迁移。组织可以从较容易的工作负载开始：CI 和构建系统、批处理作业、Web 前端或某些数据库，在这些情况下，迁移工作是值得的。

供应商正在这一领域开始创新。红帽的虚拟机迁移工具包（MTV）提供了一个将虚拟机迁移到 Kubernetes 环境的框架，处理了许多原本需要手动完成的转换任务。类似地，思科 Live 2025 上推出的 Isovalent Network Bridge 等项目专注于简化网络转换。它允许迁移后的虚拟机保持与现有数据中心环境的通信，从而减少了平台转移造成的中断。

这些创新凸显了人们日益认识到迁移不仅是一项技术任务，而且是采用的战略障碍。在工作负载迁移过程变得风险更小、更可预测之前，企业不会完全接受 Kubernetes 作为虚拟机的归宿。

## 这对企业意味着什么

虚拟机和容器在 Kubernetes 上的融合并非抽象概念。它是一个正在塑造当今企业战略的实时对话。平台负责人正在权衡维护独立基础设施的成本与统一它们的复杂性。CIO 们正在评估 Kubernetes 是否真正可以作为工作负载的通用基础，或者它是否面临承担过多责任的风险。

这一话题将在即将举行的 KubeCon North America 2025 等会议上成为主导讨论。预计会听到更多关于 KubeVirt 等项目、Kubernetes 网络进展以及不断发展的迁移工具生态系统的信息。在这些技术辩论的背后，有一个更深层次的问题：企业如何将其基础设施选择与数字化转型、效率和韧性的更广泛目标相一致？

对于有兴趣进一步关注此话题的读者，[KubeVirt 社区](https://kubevirt.io/community/)维护着一个活跃的特别兴趣小组（SIG）和定期的社区电话会议。红帽发布关于 OpenShift Virtualization 和 MTV 的更新，而 [Cilium 社区](https://cilium.io/get-involved/)定期发布关于网络进展的深度文章。这些都是获取最佳实践和经验教训的宝贵资源。

## 结论

Kubernetes 已经改变了组织交付软件的方式。它的下一个考验可能在于它是否也能承担管理虚拟机的角色，在单一平台上 объеди老旧和新的工作负载。挑战很明确：对运维人员进行再培训，使平台适应不同的工作负载期望，以及应对复杂配置、存储和网络的迁移。

这些并非小障碍，但它们正吸引着开源社区和企业供应商日益增长的关注。结果将决定 Kubernetes 是仍然是容器平台，还是演变为企业计算的通用基础。

*KubeCon + CloudNativeCon North America 2025 将于 11 月 10 日至 13 日在佐治亚州亚特兰大举行。* [*立即注册*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*。*