ATLANTA — [VCluster Labs](https://www.vcluster.com/)（前身为 Loft Labs）发布了其[同名 Kubernetes 发行版](https://thenewstack.io/vcluster-to-the-rescue/)的增强版本，该版本专为运行 NVIDIA GPU 而定制，后者是运行[大型计算密集型 AI 工作负载](https://thenewstack.io/nvidias-ai-factories-and-agentic-software-development/)的[首选平台](https://thenewstack.io/nvidias-ai-factories-and-agentic-software-development/)。

该公司将于本周在亚特兰大举行的 [KubeCon+CloudNativeCon North America 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event) 大会上，在 #421 展位展示该软件。

该平台官方名称为“用于人工智能的基础设施租户平台，以最大化 NVIDIA Kubernetes 环境中的 GPU 效率”。它结合了高级隔离、动态扩展和混合网络，为组织提供了一个平台，使其能够以类似云的方式为其内部用户运行 GPU 服务。

## 适用于 GPU 的灵活租户

vCluster 首席执行官 [Lukas Gentele](https://github.com/LukasGentele) 在接受 TNS 采访时解释道：“我们的故事是关于灵活的租户。有时你需要为单个租户提供独立的集群。一个租户可以是你的客户之一，也可以是你的开发团队之一。它也可以是针对单个开发者或一个应用程序。”

Gentele 说，两类用户会发现这项技术可能很有价值。一类是拥有许多潜在用户争夺有限 GPU 资源的大型组织。另一类是希望为其客户提供基于 GPU 服务的公共云服务。

Gentele 表示，考虑到 AI 工作的动态性，在两种情况下，灵活性都极其重要。快速动态分配和解除分配 GPU 的能力将是此类环境的一项高级功能。

据该公司称，利用 vCluster 从一个大型集群中划分出多个单独安全的“虚拟集群”的能力，公司可以更快地配置集群，更充分地利用其 GPU，并更有效地管理[第二天运营](https://thenewstack.io/learn-to-love-day-2-operations-with-gitops-driven-api-management/)。

theCUBE Research 实践负责人兼首席分析师 Paul Nashawaty 在一份声明中进一步解释说，该租户平台实现了“动态、多租户 GPU 编排，具有企业从公共云中期望的相同弹性和控制力，但适用于私有 NVIDIA 驱动的 AI 系统。”他指出，[theCUBE Research](https://thecuberesearch.com/analysts/) 发现 71% 的组织报告 GPU 利用率低下是一个主要挑战。

VCluster 还发布了在 [NVIDIA DGX 系列交钥匙 GPU 服务器](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)上运行基础设施租户平台的[参考架构](https://www.vcluster.com/ebooks/reference-architecture-vcluster-on-nvidia-dgx)。

## 基础设施租户平台

该发行版基于多项 Kubernetes 技术构建，其中一些是 vCluster 最近推出的，包括：

它与 NVIDIA [Base Command Manager](https://docs.nvidia.com/base-command-manager/index.html) (BCM) 集群管理软件直接集成。这是 NVIDIA 提供用于启动裸机 GPU 服务器并将其连接到网络的软件。

Gentele 说，VCluster 提供了所有支持软件和易用性体验。虚拟 GPU 可以通过 [Kubernetes Cluster API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)，或通过 Terraform、Helm chart 或 kubectl 进行配置。

新的 vCluster 针对 NVIDIA DGX 系统的参考架构提供了一套在以 GPU 为中心的系统上部署虚拟集群的最佳实践，使企业能够内部提供类似云的 Kubernetes 体验。