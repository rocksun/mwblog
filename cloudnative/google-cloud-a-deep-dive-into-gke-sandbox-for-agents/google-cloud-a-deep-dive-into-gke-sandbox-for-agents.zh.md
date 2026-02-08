Google Kubernetes Engine (GKE) [Agent Sandbox（代理沙盒）](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox) 是一个新的 [Kubernetes](https://thenewstack.io/kubernetes/) 扩展，旨在在隔离、安全的环境中运行工作负载，例如执行不受信任或专用代码的 AI 代理。本质上，它在 Kubernetes 集群内[提供](https://thenewstack.io/google-debuts-gke-agent-sandbox-inference-gateway-at-kubecon/)了一个轻量级的“类 VM”沙盒，利用 [gVisor](https://gvisor.dev/) 等技术实现强大的[内核级隔离](https://thenewstack.io/interview-google-gvisor-and-the-challenge-of-securing-multitenant-containers/)。

本次深入探讨将阐述 GKE Sandbox for Agents 是什么、它在 GKE 生态系统中的作用，以及 Kubernetes 工程师应了解的架构组件和实现细节。

## 什么是 GKE Sandbox for Agents？

GKE 的 Sandbox for Agents（通常简称为 Agent Sandbox，即代理沙盒）是一种 Kubernetes 原生机制，用于按需创建临时的、隔离的运行时环境。它旨在解决新兴用例，例如生成和执行代码的 AI/ML 代理，或任何需要在集群内运行不受信任代码而又不危及宿主或其他工作负载的场景。

直接在集群节点上运行任意代码或第三方代理可能会带来安全风险。Agent Sandbox 通过为运行的代码提供进程、存储和网络隔离来缓解这些风险，这得益于由 gVisor 支持的沙盒层。实际上，这意味着即使沙盒中运行的代码是恶意或存在漏洞的，它也极不可能逃逸并影响宿主内核或相邻 Pod。

重要的是，Agent Sandbox 不是 GKE 专有功能，而是一个[开源项目](https://github.com/kubernetes-sigs/agent-sandbox)，目前在 [Kubernetes SIG Apps](https://github.com/kubernetes/community/blob/master/sig-apps/charter.md) 组中。它引入了一个新的 Kubernetes 自定义资源定义（CRD）和对应的控制器，名为 Sandbox。此 CRD 充当了一个高级抽象，用于在 Kubernetes 中管理具有类 VM 特性（例如稳定身份和持久状态）的单容器、长时间运行工作负载。

在 GKE 中，Google 集成并支持此 CRD，以便集群运营商可以轻松地在标准和 Autopilot 集群上启用沙盒代理。事实上，在 [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) 集群上，默认在所有节点上启用基于 gVisor 的沙盒，而在标准 GKE 集群上，您需要明确创建支持 gVisor 的节点池才能使用 Agent Sandbox。

[![](https://cdn.thenewstack.io/media/2025/12/2502e33c-k8s-agent-sandbox-1024x394.jpg)](https://cdn.thenewstack.io/media/2025/12/2502e33c-k8s-agent-sandbox-1024x394.jpg)

实现的核心是 Sandbox CRD 及其控制器。此 CRD 定义了隔离沙盒环境的期望状态。当创建 Sandbox 自定义资源时，Agent Sandbox 控制器会启动并管理一个相应的 Pod 来实现沙盒。与普通的 Deployment 或 StatefulSet 不同，Sandbox CRD 表示一个单例 Pod——每个沙盒始终只有一个 Pod——并对其生命周期和身份进行特殊处理。Sandbox CRD 的主要架构特性包括：

**稳定身份：** 每个沙盒都分配有一个稳定的名称（主机名和网络身份），即使底层 Pod 重启，该名称也保持一致。换句话说，沙盒的行为类似于具有固定身份的单个 VM 或节点，而不是 Kubernetes 通常分配的临时 Pod 名称。这对于需要一致主机名或 IP 地址的应用程序非常有用。控制器确保沙盒的 Pod 始终使用相同的名称，并且通常使用无头服务或类似方法进行 DNS 解析。

**持久存储：** 沙盒可以配置 PersistentVolumeClaim（持久卷声明），以便在重启后保留状态。这使得沙盒能够随着时间的推移维护数据和已安装的工具，很像 VM 的磁盘。例如，AI 代理沙盒可以在首次运行时安装库或缓存数据，这些数据会持久保存在卷上以供后续使用。

**生命周期管理：** Agent Sandbox 控制器创建 Pod，监控其健康状况，并支持休眠（暂停）和恢复等操作。如果不再需要沙盒，可以停止它（移除 Pod），同时保留其卷，稍后通过重新创建 Pod 并从卷中恢复状态来恢复。这种休眠/恢复能力是一个独特的功能，因为原生的 Kubernetes 不支持暂停 Pod 的执行。这在代理可能长时间空闲但在需要时应快速恢复的场景中非常有用。

为了实现这些功能，Agent Sandbox 项目还在核心 Sandbox 对象之上定义了一些扩展 CRD：

**SandboxTemplate（沙盒模板）：** 定义沙盒规范（容器镜像、资源等）的可重用模板。当您需要启动许多相似的沙盒时，这很有帮助——您只需定义一次模板，而无需每次重复 Pod 规范。

**SandboxClaim（沙盒声明）：** 一种高级抽象，允许用户（或其他控制器）从模板中“声明”一个沙盒，而无需担心细节。该声明会触发控制器使用指定的模板创建一个 Sandbox 实例。这种模式将请求者与实现解耦，在多租户或按需场景中非常有用（类似于 PersistentVolumeClaim 对卷的工作方式）。

**SandboxWarmPool（沙盒预热池）：** 此扩展维护一个预热的沙盒 Pod 池，以提高性能。当需要新的沙盒时，控制器可以几乎即时地从预热池中分配一个，而不是从头开始创建 Pod（在使用重度隔离时可能会很慢）。然后，该池在后台补充。这种设计对于减少延迟至关重要。

在底层，Sandbox 控制器是用 Go 语言实现的，并作为集群部署运行，与其他的 Kubernetes 控制器非常相似。它监控 Sandbox 和相关的 CRD 事件，并为每个 Sandbox 对象管理一个对应的 Pod 和一个 PersistentVolumeClaim。

控制器确保 Pod 的规范与 Sandbox CRD 中的模板匹配，并将其调度到支持所需运行时的节点上。值得注意的是，Sandbox CRD 的规范包含一个 `podTemplate` 字段，您可以在其中指定容器镜像、命令以及其他 Pod 设置，包括任何所需的沙盒运行时类（例如 gVisor）。实际上，Sandbox 资源是一个围绕 Pod 的“包装器”，具有额外的约束和功能。

## 与 Kubernetes 和 GKE 内部的集成

由于 Agent Sandbox 以 CRD 和控制器的形式交付，它与 Kubernetes API 机制自然集成。您在集群中安装 CRD 和控制器，然后就可以像创建 Deployments 或 Pods 一样创建 Sandbox 资源。作为原生扩展的设计意味着 kubectl 或 Argo CD 等工具可以以声明方式管理沙盒。资源 API (agents.x-k8s.io/v1alpha1) 是标准化和开放的，支持社区贡献和互操作性。事实上，Google 从一开始就与 Kubernetes 社区合作，将其构建为[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)项目，这表明其旨在将其打造为一项标准功能而非专有功能。

在 GKE Standard 集群上，使用 Agent Sandbox 通常需要一些设置：您需要在这些 Pod 将运行的节点上启用 GKE 的沙盒支持。这可以通过创建一个启用“Enable GKE Sandbox (gVisor)”选项的节点池来实现（或者通过 gcloud 或 Terraform 使用 `--sandbox type=gvisor` 标志）。这些节点将安装 gVisor 运行时并与 containerd 配置。然后，调度到该节点上并具有相应 runtimeClass 的任何 Pod（包括 Agent Sandbox 管理的 Pod）都将自动在 gVisor 中隔离运行。

在 GKE Autopilot 集群上，Google 使这变得更加容易。Autopilot 集群默认在所有节点上启用 gVisor。代理沙盒可以在 Autopilot 上部署，无需特殊节点池配置；您只需将沙盒的运行时指定为 gVisor，Autopilot 就会处理沙盒执行。这种自动化集成降低了那些喜欢完全托管的 Autopilot 模式的用户使用沙盒代理的门槛。

GKE 还提供了解决运行许多隔离沙盒的性能和可扩展性挑战的功能。其中一项功能是[Pod 快照](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots)，目前是 GKE 独有的预览功能。Pod 快照允许将运行中的 Pod 的状态（内存、CPU 状态甚至 GPU 内存）检查点到持久存储中，然后恢复到一个新的 Pod 中。当与 Agent Sandbox 结合使用时，这意味着您可以对完全初始化的沙盒环境进行快照，然后通过恢复快照快速启动该沙盒的新实例，而不是从头开始初始化每个实例。

Google 报告称，使用 Pod 快照可以将复杂沙盒工作负载的启动时间从数分钟缩短到数秒。它还能提高经济效益。您可以暂停空闲的沙盒（将其状态保存到存储并移除 Pod）以释放资源，然后通过恢复快照按需恢复它们。这对于 GPU 加速的 AI 代理等昂贵工作负载来说是颠覆性的——您不再需要让它们在不使用时空闲运行并消耗资源。

另一个集成点是网络和身份。GKE 鼓励将 Agent Sandbox 与严格的网络策略和 [GKE 工作负载身份](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)结合使用。每个沙盒 Pod 都可以通过 Kubernetes NetworkPolicy 进行限制（默认情况下，gVisor 提供其自身的网络隔离）。

实际上，人们会对这些沙盒采用“默认拒绝”的网络态势，仅允许出站流量流向代理绝对需要的特定 API 端点或资源。同样，使用工作负载身份，每个沙盒都可以分配一个具有最小权限的隔离 IAM 身份，这样即使被攻破，也无法访问其他云资源。这些不是沙盒本身的内置功能，而是 GKE 支持的推荐操作实践，旨在增强代理工作负载的整体安全性。

## 结论

GKE Sandbox for Agents 代表着在弥合传统虚拟机和 Kubernetes 容器工作负载之间差距方面迈出了重要一步。通过提供一种 Kubernetes 原生的方式来启动安全、隔离的单容器环境，它使集群运营商能够以更低的风险支持新型工作负载。

其架构基于 Sandbox CRD 和控制器，利用 gVisor 新颖的用户空间内核模型，为在共享集群上运行“不受信任”的代码提供了一个优雅的解决方案，同时不牺牲安全性。同时，与 GKE 生态系统（如 Autopilot 自动化、预热池和 Pod 快照）的集成表明，性能和可用性问题正在通过创新得到解决。

对于 Kubernetes 工程师来说，Agent Sandbox 是一种工具，可以对某些 Pod 的运行方式进行细粒度控制。它体现了云原生基础设施的方向：在大规模提供灵活性和安全性。随着项目的成熟，我们预计它将成为 GKE 和其他 Kubernetes 平台中的核心功能，从而推动需要 Kubernetes 编排能力和 VM 级隔离安心感的新一波应用程序的发展。

总之，GKE Sandbox for Agents 为我们的工具箱增加了一个重要的选项——它使我们能够自信、安全地在 Kubernetes 上运行更具实验性或不受信任的工作负载。