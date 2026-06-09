<!--
title: AI工作负载时代下，如何保障Kubernetes集群安全？
cover: https://cdn.thenewstack.io/media/2026/06/911d4dcf-mariola-grobelska-ruyb0h3oq7a-unsplash-scaled.jpg
summary: 随着AI智能体的兴起，Kubernetes面临动态、不可预测的新安全威胁。保障K8s安全需要零信任网络、策略即代码、镜像扫描及运行时异常检测等多控制平面的协同防护。
-->

随着AI智能体的兴起，Kubernetes面临动态、不可预测的新安全威胁。保障K8s安全需要零信任网络、策略即代码、镜像扫描及运行时异常检测等多控制平面的协同防护。

> 译自：[How to secure Kubernetes in the age of AI workloads](https://thenewstack.io/securing-kubernetes-ai-agents/)
> 
> 作者：Mary Branscombe

保障 Kubernetes 的安全一直是一项复杂的系统工程——涵盖了访问控制、镜像漏洞、机密管理和网络安全。而 AI 工作负载让这一切变得更加困难。它们带来了全新的行为模式、流量特征和安全风险，从而扩大了攻击面。

两年前，您的集群运行的是微服务。现在，它运行的是智能体（Agent）。因此，您的集群中不再是 CPU 使用率可预测的持久化应用，而是 GPU 节点上动态、瞬时的进程，它们会产生突发性、不可预测且频繁需要访问外网的流量，而 Kubernetes `NetworkPolicy` 根本不具备处理这些流量的细粒度和可见性。

> 两年前，您的集群运行的是微服务。现在，它运行的是智能体。

智能体会复制或生成不可信的代码，发现并调用您尚未评估的工具（更不用说将其加入来自新注册表的白名单了），启动子智能体、技能和 MCP 客户端，将针对陌生 API 的意外调用串联起来，并通常对您的基础设施和数据源提出不可预测的需求。

此外，现在的底层基础设施还包括稀缺且昂贵的 GPU 资源，而这些资源几乎肯定会与其他用户共享，绝大多数团队对这种共享模式的安全防护还很不习惯。解决这一问题需要的不仅仅是传统的集群加固：您需要一个能够横跨四个关键控制平面（从网络开始）提供安全保障的架构。

## 从引导启动到智能体跃迁的零信任网络

即使是在像 **[Azure Kubernetes 服务](https://azure.microsoft.com/en-us/products/kubernetes-service)** 这样的托管服务上，标准集群默认情况下也具有不受限制的出站网络访问权限。AKS 并没有让用户通过繁琐的防火墙规则来锁定访问，而是正在转向一种更安全的默认设置：[网络隔离集群](https://learn.microsoft.com/en-us/azure/aks/concepts-network-isolated)允许您在引导启动时不对公共互联网产生任何出站依赖，除非您显式启用它们。

负责 AKS 安全体验的 [Shashank Barsin](https://www.linkedin.com/in/shashank-barsin-1898643b/) 接受 *The New Stack* 采访时这样解释道。

“引导启动集群本身不需要任何出站流量：您可以使用私有端点从私有 Azure Container Registry 拉取所有镜像，”Barsin 说道。“这是我们设计该平台时的初衷，旨在避免意外的数据外泄。在 AI 时代，您总是会担心智能体在做什么以及它们可能会窃取哪些数据。”

领导云原生安全和注册表团队的 [Toddy Mladenov](https://www.linkedin.com/in/toddysm/) 告诉 *The New Stack*，如果集群无法看到集群之外的公共注册表和 API，那么在其中运行的智能体产生意外行为或建立非预期连接的机会就会减少。

“您在集群上建立的网络路由控制着智能体可以去哪里获取工具、获取包或获取赖以运行的知识，”Mladenov 说道。

对于完全物理隔离的环境，网络加速技术的提升使得 Private Link 更适用于连接到 Azure Key Vault 或将指标和日志发送到 Azure Monitor，从而使遥测数据和机密信息远离公共网络。

零信任同样适用于集群运维；AKS 正在与 Kubernetes 生态系统的其他部分一起采用 Gateway API，而 [Azure Kubernetes 应用网络](https://learn.microsoft.com/en-us/azure/application-network/)（目前处于预览阶段）通过托管的 Istio 服务简化了[无代理服务网格](https://istio.io/latest/docs/ambient/)，为平台团队提供了一种一致的方式来控制和监控东西向和南北向流量。

## **策略即代码实现护栏与治理**

您无法预测 AI 的每一种行为，但您可以强制执行[声明式策略](https://learn.microsoft.com/en-us/azure/aks/use-azure-policy)来管控智能体与智能体之间、智能体与工具之间以及智能体与大语言模型（LLM）之间的通信。

使用准入策略以及诸如 [OPA](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes) 和 [Kyverno](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/eks-to-aks/governance) 等引擎来建立安全护栏，以处理细粒度的管控：在哪个事务中，使用哪个身份的哪个智能体被允许部署哪个工作负载、调用哪个工具，哪些数据源被视为敏感数据，以及何时需要人工干预。

“我们正在处理这样一些情况：一个智能体调用另一个智能体，后者又调用另一个智能体，再后者又调用一组工具；授权需要在事务上下文中进行，而不是进行一次静态的、一次性的授权，”Barsin 解释道。“能够将智能体、子智能体和工具所做的一切以及它们如何交互的整个事务串联起来，正变得越来越重要。”

> “零信任领域中涌现出的诸如事务令牌和 AAuth 等新项目，涵盖了整个生命周期，不仅包括集群，还包括之上的工作负载及其通信。”

Istio 社区正在探索将该项目作为 [AgentGateway](https://github.com/agentgateway/agentgateway) 的控制平面，以便在智能体生成带有多个请求的、不规则且突发性的流量时，为需要保持开启的连接提供一个路由层，从而维持状态。AKS 将在其成熟后与之一致；同时，该团队正在试验智能体身份识别方法，使从终端用户到智能体和工具的整个路径对该控制平面可见，以便策略可以在整体上下文上发挥作用。

“零信任领域中涌现出的诸如[事务令牌](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/)和 [AAuth](https://datatracker.ietf.org/doc/draft-rosenberg-oauth-aauth/) 等新项目，涵盖了整个生命周期，不仅包括集群，还包括之上的工作负载及其通信。”在业余时间，Barsin 正在合作开发 [kontxt（一个针对 OAuth 和事务令牌的 IETF 智能体授权提案的开源实现）](https://github.com/aramase/kontxt)，以便为具有覆盖整个身份链的声明式授权策略的智能体间通信提供零信任环境。

这些方法有望带来更高层次的控制，例如要求参与被标记为处理受监管数据的事务的智能体和工具必须达到某种程度的策略合规性。

## 镜像扫描与出处验证

策略应该涵盖智能体可以从哪些注册表中拉取镜像、库和工具，新工具如何获得批准使用，以及哪些 API 和数据源被认为是敏感、机密或适合任何智能体使用的。“如果您不限制周边防御，智能体可能会决定从它们认为方便的任何注册表中拉取工具，”Mladenov 警告道。“这就是智能体的本质：它们在寻找解决问题的方法。没有任何限制的话，它们会在互联网上的任何地方寻找解决方案。”

> “这就是智能体的本质：它们在寻找解决问题的方法。没有任何限制的话，它们会在互联网上的任何地方寻找解决方案。”

为了在获得智能体灵活性的同时降低其运行所带来的风险，您可以限制它们只能使用虚拟网络（VNet）中单个经过批准和策划的注册表。这限制了它们可以访问的工具，并允许您应用适当的安全策略，例如[持续扫描](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-containers-introduction?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json)漏洞、缺失补丁、过时依赖项、恶意软件和泄露的机密。这样，从公共注册表拉取的任何镜像在进入生产环境之前，都可以被隔离、扫描、[签名](https://learn.microsoft.com/en-us/azure/container-registry/overview-sign-verify-artifacts)、验证并在必要时[更新](https://opensource.microsoft.com/blog/2024/09/18/project-copacetic-quick-and-efficient-container-image-patching/)。为了简化这一过程，Azure Container Registry 支持基于角色的访问控制（RBAC），并且您现在可以[锁定其制品缓存以使用另一个 ACR 注册表](https://techcommunity.microsoft.com/blog/AzureCompute/use-azure-container-registry-as-an-upstream-source-for-artifact-cache/4517102)。

生命周期元数据可帮助您解决镜像血缘问题：机器可读的出处和漏洞报告可实现自动打补丁和更新，并在准入控制器处审核甚至阻止不合适的镜像。

沙箱提供了额外的一层保护。Cloud Hypervisor 提升了 [Kata 容器](https://katacontainers.io/)的性能，但如果您只是为了运行一个 Python 脚本而启动一个沙箱，这无法扩展到成千上万个智能体。而 [Hyperlight](https://opensource.microsoft.com/blog/2024/11/07/introducing-hyperlight-virtual-machine-based-security-for-functions-at-scale/) 运行时在硬件隔离的虚拟机中执行单一用途的应用程序，其内存占用和启动延迟极小（仅 1-2 毫秒），因此没有任何理由不强制使用沙箱环境，特别是对于智能体。这正是您最需要沙箱保护的地方，这样您就可以默认将智能体想要运行的所有代码视为不可信的。

## **针对智能体行为调整的运行时异常检测**

即使有了这些层层的策略和护栏，智能体仍会以意想不到的方式行事：毕竟，如果您知道所有事情应该如何完成，您一开始就不需要智能体了。

AKS 与 Microsoft Defender for Containers 集成，使用 eBPF 和其他底层探针进行运行时保护，[发出警报](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-containers?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json)来标记[二进制漂移](https://learn.microsoft.com/en-us/azure/defender-for-cloud/binary-drift-detection?toc=%2Fazure%2Faks%2Ftoc.json&bc=%2Fazure%2Faks%2Fbreadcrumb%2Ftoc.json&tabs=edit-rule)（随着智能体尝试运行不在原始容器中的代码，这种情况变得越来越普遍）以及可疑的网络访问或进程行为。

监控网络和文件系统涵盖了长期运行的工作负载的已知流量模式和应用行为，但瞬时智能体工作负载是动态启动 Pod 的。当发生问题的不是行为异常的 Pod，而是智能体反复创建短暂的 Pod，且这些 Pod 立即尝试沙箱逃逸或暴力破解数据库时，异常检测将需要在更高的层面发挥作用。如果另一个 Pod 表现出相同的行为，仅关闭该 Pod 是无济于事的；智能体本身需要被控制起来。

## **生产环境中的防护**

Mladenov 表示，如今大多数客户更担心的是 GPU 容量而不是安全性。但在充分利用这些稀缺且昂贵的资源时，平衡隔离性与利用率是一项复杂的任务。

> “我有一个集群托管着多租户应用：有些是基于智能体的，有些不是，但它们都遵循非常优秀的安全实践，因为平台强制执行了这些实践。”

如果您不知道[如何安全地将 GPU 划分](https://docs.nvidia.com/datacenter/cloud-native/kubernetes/latest/index.html)为多个实例，那么为高速数据传输提供支持的 GPU 节点之间的直接连接，以及它们所需的高效通信模型，可能会降低其他工作负载的性能，甚至导致数据泄露。让您能够将最敏感的数据用于 AI 的[机密 GPU](https://github.com/Azure/az-cgpu-onboarding/blob/main/docs/Confidential-GPU-H100-AKS-Onboarding.md)在 Kata 中仍是一个[预览功能](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-confidential-containers.html)，并且还要求您自行处理密钥管理。

要成功地从概念验证走向生产，您将需要处理可观测性、高性能沙箱、[安全的 GPU 多租户](https://learn.microsoft.com/en-us/azure/aks/gpu-multi-instance?tabs=azure-cli)以及保障智能体通信安全等问题，或者选择像 AKS 这样为您处理好这一切的平台。

“推理和智能体需要全新的技术栈，这也带来了新的安全挑战和对全新安全控制措施的需求，”Barsin 表示赞同。

Mladenov 坚信，在 AKS 中为解决智能体安全而开展的工作也将使更传统的工作负载受益。“我有一个集群托管着多租户应用：有些是基于智能体的，有些不是，但它们都遵循非常优秀的安全实践，因为平台强制执行了这些实践。”