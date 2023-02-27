# 如何为 Kubernetes 构建合适的平台

本文翻译自 [How to Build The Right Platform for Kubernetes](https://thenewstack.io/kubernetes/kubernetes-infrastructure-architecture/) 。

无论您是与云提供商合作还是单独行动，您都需要为您的 Kubernetes 基础架构规划正确的架构。

![](https://cdn.thenewstack.io/media/2023/02/3b7ffe06-shutterstock_538143214-1024x683.jpg)
Image by Shutterstock

[Kubernetes 是一种编排工具](https://thenewstack.io/kubernetes/)。它可以帮助你部署、网络、负载均衡以及缩放容器化应用程序，并且每个工作负载都有它自己的架构，无论是有状态还是无状态，或者是你容器化的巨型服务，还是使用服务网格的微服务，批处理作业或者 serverless 函数。

但您还需要考虑 Kubernetes 基础架构本身的架构：如何构建 Kubernetes 运行的平台。

Kubernetes 既可以部署几乎所有类型的应用程序，又可以在几乎所有类型的硬件上、云端或其他地方运行，具有非常强大的灵活性。为了达到通用性和强大性，它具有非常高的可配置性和可扩展性。这给你的架构选择提供了很多可能性。

这些选项包括你是否自己做出所有的配置选择，是否遵循 [VMware Tanzu](https://tanzu.vmware.com/?utm_content=inline-mention) 或 Azure Arc 等工具中的默认选项，这些工具提供了一种更集成的方法来部署和管理基础设施，或者使用托管云 Kubernetes 服务，它仍然为你提供关于你所部署的资源的选项，但会有[快速启动](https://aws.amazon.com/solutions/implementations/amazon-eks/)、[参考架构](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks/baseline-aks)和为[常见应用工作负载](https://cloud.google.com/architecture/distributed-load-testing-using-gke#architecture)设计的[蓝图](https://learn.microsoft.com/en-us/azure/architecture/framework/services/compute/azure-kubernetes-service/azure-kubernetes-service)。

## 规划 Kubernetes 资源

您的 Kubernetes 基础设施架构是 Kubernetes 用来运行容器化应用程序（及其自己的服务）的一组物理或虚拟资源，以及您在指定和配置它们时所做的选择。

您需要确定控制平面服务器、集群服务、附加组件、集群、数据存储和网络组件所需的虚拟机（或裸机硬件），集群上需要多少节点，以及基于 pod 和服务的工作负载和资源需求确定需要的内存和 vCPU。

[自动缩放](https://thenewstack.io/getting-started-with-kubernetes-autoscaling/)让您可以动态地向上或向下调整容量，但您需要有可用的基础容量。您需要考虑托管 Kubernetes 集群的最佳平台：在您自己的数据中心、边缘、托管提供商或公共、私有或混合云中的基础设施。

其中一些将由您的工作负载的需求决定：如果它们主要是无状态的（或者如果很容易在外部存储该状态），您立刻可以通过使用部署打折但也可能被中断的 spot 实例来降低云成本。您需要了解您计划运行的应用程序的大小、复杂性和可扩展性以及您需要的控制和定制量，以及您将使用的资源的性能、可用​​性和成本因素.

最初，Kubernetes 的构建假设其运行的所有硬件在本质上都是相似的并且可以有效互换，因为它的开发是为了利用云基础设施即服务 (IaaS) 中常见的商用服务器。

但即使在云端，不同的工作负载仍然需要非常不同的资源，而 Kubernetes 已经发展到支持更多异构基础设施：不仅是 Windows 节点和 Linux，还有 GPU 和 CPU、Arm 处理器和 x86。甚至可以选择使用某些类别的 Linux 设备作为节点。

如果您为 Kubernetes 虚拟机使用云 IaaS 或托管云 Kubernetes 服务（如 AKS 或 EKS），则可以为您的虚拟机选择合适的实例。如果您要在边缘构建自己的 Kubernetes 基础设施，您可能会选择 Arm 硬件或消费级英特尔 NUC 来运行要求较低的 Kubernetes 发行版，例如餐厅或零售店中的 k3s，您没有中心级硬件的数据设施。

根据您选择的 Kubernetes 发行版，您可能还需要考虑您想要的主机操作系统以及您将使用的容器运行时。您会运行自己的容器注册表还是只从公共注册表中拉取镜像？你将在哪里存储秘密？使用 [HashiCorp Vault](https://www.hashicorp.com/?utm_content=inline-mention) 或来自您的云提供商的托管密钥存储意味着您不会在可能泄漏的部署管道中拥有凭据。

## 多集群 K8s 基础架构

您还需要考虑可能的故障：您是否需要运行关键控制平面组件的多个副本的高可用性集群，或者您将运行多集群架构？

对于较小的 Kubernetes 基础设施，您可以使用命名空间分隔不同的工作负载：逻辑分区让您可以在一个集群上隔离和管理不同的应用程序、环境和项目。但您也可以使用单个 Kubernetes 控制平面来管理多个节点集群，将工作负载放在不同的集群上以获得更好的安全性和性能。

如果您对可接受的延迟有监管要求或严格限制，需要执行不同的策略和权限，或者想要避免需要零停机时间的应用程序出现单点故障，这使您可以在不同位置编排应用程序 - 包括不同的云提供商——但仍然有一个地方可以访问该基础设施。这简化了将应用程序从一个集群迁移到另一个集群，无论是用于扩展还是灾难恢复，尽管它也引入了显着的复杂性。

## 将您的 Kubernetes 基础设施联网

您还需要规划服务发现选项和网络拓扑，包括防火墙和 VPN 连接，以及集群的网络插件、DNS 设置、负载均衡器和 ingress 控制器。

想想访问管理：您需要部署基于角色的访问控制 (RBAC) 来为您的用户和资源实施细粒度的权限和策略，并确保您保护管理员访问权限。但您还需要为需要访问现有数据存储的工作负载管理机器身份。

本机 Kubernetes 用户身份验证使用证书：如果您需要对用户访问进行集中控制和治理，您可能希望使用现有的身份提供程序进行身份验证。

## 管理 Kubernetes 的架构师

由于 Kubernetes 旨在简化应用程序的扩展，虽然您可以手动更改活动和就绪探针等个别设置，但它实际上是为声明式配置管理而设计的。您在 YAML 中编写配置文件（或使用为您发出这些文件的工具）来告诉 Kubernetes 应用程序应该如何运行，而 Kubernetes 会处理实现这一点。

您不应调整设置，而应专注于使用基础设施即代码实现可重复性的自动化：将配置设置为版本控制的、可审计的代码，并根据需要经常应用它（或在出现问题时重新启动它），每次获得相同的系统。

Kubernetes 的设计目标是可重复、不可变的基础设施，在这种基础设施中，您将集群视为牛（而不是您命名、拥抱和关心的宠物）。为此做好准备的方式便是减少持续管理和实际在生产中操作容器的工作量。

您可以使用带有 Flux 或 Argo CD 的 GitOps 工作流将其扩展到策略管理和治理以及应用程序交付，部署应用程序更新并使集群在从引导到配置更新的整个过程中一直处于所需状态。您需要收集指标并跟踪性能：大多数工作负载都会发出 Prometheus metrics ，但您还需要考虑监控仪表板以及要启用的日志记录。

您需要监控容器基础架构中的威胁和安全风险，并确保您的 VM 主机得到适当强化。同样，在规划 Kubernetes 基础设施架构时，考虑一下您将为此使用的工具和流程，可以更轻松地确保您不会遗漏任何东西。

## 理解 Kubernetes 架构

将所有这些放在一起并非易事，您可以从其他 Kubernetes 用户如何构建其基础设施架构中学到很多东西。

“你试图获得 8 年的 Kubernetes 开发经验，然后才能高效地使用它。这要求太多了。你需要一本年鉴来帮助你导航和避开冰山，”前 Kubernetes 发布负责人和指导委员会成员 Lachlan Evenson 警告说。 Evenson 与 Kubernetes 联合创始人布伦丹·伯恩斯 (Brendan Burns) 合著了《[Kubernetes 最佳实践](https://www.oreilly.com/library/view/kubernetes-best-practices/9781492056461/)》，试图提供一个配套指南来提供其中的一些内容。

但是您仍然应该期望花时间弄清楚哪种基础设施架构最适合您的特定工作负载并获得运行它的专业知识。