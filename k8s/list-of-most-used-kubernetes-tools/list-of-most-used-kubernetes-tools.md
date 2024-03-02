<!--
title: 云原生之旅的最佳 Kubernetes 工具
cover: https://teckbootcamps.com/wp-content/uploads/2023/10/Copy-of-kube-1024x441.png
-->

嗨，在当今动态的环境中，在 450 多家经过 Kubernetes 认证的服务提供商和众多经过 Kubernetes 认证的发行版中进行导航可能是一项艰巨的挑战。本博客旨在通过展示精心整理的**2023 年最常用和最流行的 Kubernetes** 工具列表来简化此过程。

> 译自 [The Best Kubernetes Tools for Your Cloud Native Journey](https://teckbootcamps.com/list-of-most-used-kubernetes-tools/)，作者 Mohamed BEN HASSINE。

## 什么是 Kubernetes？

**Kubernetes**，也称为“kube”或“k8s”，**是一种软件，可自动管理、扩展和维护所需状态的多容器工作负载**。

现代软件越来越多地作为容器组运行，有时称为微服务。一个完整的应用程序可能包含许多容器，所有容器都需要以特定方式协同工作。Kubernetes 是一种软件，它将物理或虚拟主机（服务器）集合转换为一个平台，该平台：

- 承载**容器化工作负载**，为其提供计算、存储和网络资源，以及
- 自动管理大量容器化应用程序——通过适应变化和挑战来保持其健康和可用性

## 为什么要使用 Kubernetes？

Kubernetes 的好处之一是它使构建和运行复杂应用程序变得更加简单。以下是 Kubernetes 的众多功能中的一部分：

- 大多数应用程序需要的标准服务，如本地 DNS 和基本负载平衡，并且易于使用。
- 易于调用的标准行为（例如，如果容器死亡则重新启动该容器），并且可以完成保持应用程序运行、可用和高效的大部分工作。
- 一组标准的抽象“对象”（称为“pod”、“replicasets”和“deployments”），它们围绕容器进行包装，并使围绕容器集合构建配置变得容易。
- 应用程序可以调用的标准 API，以轻松启用更复杂的行为，从而更容易创建管理其他应用程序的应用程序。

对“Kubernetes 用于什么”的简单回答是，它为开发人员和运维人员节省了大量时间和精力，让他们可以专注于为其应用程序构建功能，而不是想办法并实施方法来保持其应用程序在规模上运行良好。

通过在面对挑战（例如，服务器故障、容器崩溃、流量激增等）时保持应用程序运行，Kubernetes 还可以减少业务影响，减少将中断的应用程序重新联机的消防演习的需要，并防止其他责任，例如不遵守服务级别协议 (SLA) 的成本。    

## Kubernetes 容器注册表

在讨论容器注册表之前，我们需要了解三个相关概念：

- **容器**：容器是在沙盒环境中运行程序的一种方式。这意味着该程序与系统其余部分隔离，因此它不会影响其他程序或操作系统本身。 
- **镜像**：镜像是创建容器的模板。它包含容器运行所需的一切，例如程序代码、库和系统设置。 
- **存储库**：存储库是存储镜像的地方。它可以是您计算机上的本地目录，也可以是服务器上的远程存储库。 
- **注册表**：注册表是镜像的中央存储库。它可用于存储单个项目或组织中所有项目的镜像。
 
所以**容器注册表就像容器的库**。它们存储并提供开发人员运行其应用程序所需的容器镜像。

| 工具名称  | 描述    |
|----|------------------|
| JFrog     | JFrog 正在通过持续更新实践彻底改变软件世界，其速度和连续性永远改变了组织管理和发布软件的方式。  |
| Google Container Registry (GCR) | Google Container Registry (GCR) 是 Google Cloud Platform (GCP) 上的安全、私有 Docker 存储库。它是一个高度可扩展且可靠的注册表，可用于存储和管理云原生应用程序的容器镜像。<br/> GCR 与其他 GCP 服务（例如 Kubernetes Engine 和 Cloud Build）集成，从而可以轻松部署和管理您的容器化应用程序。         |
| Harbor    | 一个开放源代码的受信任的云原生注册表项目，用于存储、签署和扫描内容。 |

## Kubernetes 容器运行时

容器就像小盒子，可以容纳应用程序运行所需的一切，包括其代码、库和运行时环境。它们类似于虚拟机，但它们更轻量级且更有效率，因为它们与同一主机上的其他容器共享操作系统。

容器运行时是启动和运行容器的软件。它提供了容器运行所需的资源，例如内存、CPU 和存储。如果没有容器运行时，您将无法运行容器。

| 工具名称     | 描述             |
|--------------|---------------------|
| containerd   | containerd 是一个容器运行时，用于管理物理或虚拟机器（主机）上容器的生命周期。它创建、启动、停止和销毁容器。它还可以从容器注册表中拉取容器镜像，挂载存储，并为容器启用网络。               |
| CRI-O        | CRI-O 是 Kubernetes 的基于 Open Container Initiative 的实现。                      |
| gVisor       | gVisor 是一个沙盒化的容器运行时，为运行容器化应用程序提供安全和隔离的环境。它由 Google 创建，并于 2018 年作为开源软件发布。                     |
## Kubernetes 集群管理

Kubernetes 的集群管理是管理一组 Kubernetes 集群的过程。这包括以下任务：

- **配置和取消配置集群**：根据需要创建和销毁集群。 
- **升级集群**：使集群保持最新版本的 Kubernetes 和其他软件。 
- **监控集群**：收集和分析来自集群的指标和日志，以识别和解决问题。 
- **扩展集群**：根据不断变化的需求向集群添加或删除节点。 
- **保护集群**：配置和管理集群的安全设置。

| 工具名称   | 描述       |
|------------|---|
| kubeadm    | Kubeadm 是用于引导 Kubernetes 集群的工具。  |
| KOPS       | kops 是一个在 AWS、GCP 和 Azure 上管理 Kubernetes 集群的工具（Alpha 版）。  |
| Rancher    | Rancher 是一个完整的容器管理平台。         |
| kubespray  | KubeSpray 用于部署生产就绪的 Kubernetes 集群。        |

## Kubernetes 托管服务

托管 Kubernetes 服务是提供完全托管的 Kubernetes 环境的基于云的服务。这意味着云提供商负责设置、管理和维护 Kubernetes 集群的所有任务，因此您可以专注于开发和运行您的应用程序。

| 工具名称            | 描述        |
|---------------------|-|
| GKE Kubernetes      | Google Kubernetes Engine（GKE）是 Google Cloud 提供的托管 Kubernetes 服务。 Kubernetes 是底层技术，是一个开源的容器编排平台，自动化容器化应用程序的部署、扩展和管理。GKE 利用这一强大技术并对其进行简化，使其适用于各种规模的企业。    |
| EKS Kubernetes      | Amazon Elastic Kubernetes Service（EKS）是一个托管的 Kubernetes 服务，可轻松在 AWS 上运行 Kubernetes。它消除了安装、操作和维护自己的 Kubernetes 控制平面的需求。EKS 提供了一个高可用性、可扩展和安全的 Kubernetes 环境。 |
| AKS Kubernetes      | Azure Kubernetes Service（AKS）通过将运营负担转移到 Azure，简化了在 Azure 中部署托管的 Kubernetes 集群。作为托管的 Kubernetes 服务，Azure 处理关键任务，如健康监控和维护。创建 AKS 集群时，将自动创建和配置一个控制平面。此控制平面作为托管的 Azure 资源免费提供，用户无需关心其细节。您只需支付和管理附加到 AKS 集群的节点。|


查看我的博客文章[比较三大托管 Kubernetes 服务：GKE、EKS、AKS](https://teckbootcamps.com/comparing-the-top-three-managed-kubernetes-providers-gke-eks-aks/)

## Kubernetes 自动化和配置

自动化和配置工具可以更快地创建和设置计算机资源，例如虚拟机、网络、防火墙规则和负载均衡器。这些工具可以处理配置过程的不同部分，也可以从头到尾控制整个过程。其中大多数工具还可以与云原生空间中的其他项目和产品集成。

| 工具名称             | 描述     |
|----------------------|--------------------|
| Terraform Kubernetes | Terraform 作为基础设施即代码 (IaC) 工具，使您能够安全、可预测地创建、更改和改进基础设施。它是一种源可用工具，将 API 编码为声明性配置文件，可以在团队成员之间共享，视为代码，进行编辑、审查和版本控制。      |
| Ansible Kubernetes   | Ansible 是一个根本上简化的 IT 自动化平台，使您的应用程序和系统更容易部署和维护。使用接近普通英语的语言，通过 SSH 自动化从代码部署到网络配置到云管理的所有内容，无需在远程系统上安装代理。       |

## Kubernetes 机密管理

Kubernetes 机密管理工具可帮助您以安全的方式存储和管理敏感信息，例如密码、API 密钥和证书。它们可以帮助您保护机密免遭未经授权的访问，并确保您的应用程序安全运行。

| 工具名称                     | 描述            |
|--|-----------------|
| Vault Kubernetes            | HashiCorp Vault 是一个商业密钥管理工具，提供统一平台来管理所有的秘密，包括密码、API 密钥和证书。Vault 可以与 Kubernetes 集成，为您的 Kubernetes 集群和应用程序提供安全的秘密管理。 |
| Google Secret Manager       | Google Cloud Secret Manager 是一个托管服务，为您的 Google Cloud Platform (GCP) 应用程序提供安全的秘密管理。Secret Manager 可以与 Kubernetes 集成，在 GCP 上运行的 Kubernetes 集群和应用程序提供安全的秘密管理。    |


## Kubernetes 包管理 & Operator

Kubernetes 的包管理是安装、部署和管理 Kubernetes 应用程序的过程，这种方式一致且可重复。Kubernetes 包管理器提供了许多功能，使此过程变得更加容易，例如：

- **版本控制**：包管理器允许您跟踪和管理应用程序的不同版本。如果需要，这对于回滚到以前的版本非常重要。 
- **可重用性**：包管理器允许您为应用程序创建可重用的包。在部署新应用程序或更新现有应用程序时，这可以节省您的时 
- 间和精力。 
- **社区支持**：包管理器通常拥有庞大且活跃的社区，可以提供支持并帮助解决问题。

| 工具名称     | 描述         |
|--------------|-----------------|
| HELM         | Helm 帮助您管理 Kubernetes 应用程序 — Helm Charts 帮助您定义、安装和升级甚至最复杂的 Kubernetes 应用程序。          |
| Kustomize    | Kustomize 是一个原生 Kubernetes 工具，允许您从可重用组件组合 Kubernetes 清单。这对需要管理复杂 Kubernetes 部署的团队来说是一个很好的选择。         |
| GlassKube    | 打开自动驾驶模式，完全自动化在 Kubernetes 上部署和管理开源工具。我们的开源 Glasskube Operator 是管理所有您最喜欢的开源工具及其相关基础设施组件（如数据库、缓存）的最简单、最快速的方式，而无需手动麻烦。|
## 警报和监控

Kubernetes 的警报和监控工具是一个工具，可帮助您跟踪 Kubernetes 集群和应用程序的性能和运行状况。它可以收集指标，例如 CPU 使用率、内存使用率和网络流量，并在出现任何问题时生成警报。这可以帮助您快速识别和解决问题，在它们导致中断或其他中断之前。

警报和监控工具对于 Kubernetes 尤其重要，因为它是一个具有许多活动部件的复杂平台。手动跟踪所有内容可能很困难，尤其是如果您运行多个集群或应用程序时。警报和监控工具可以帮助您自动化此过程，并使 Kubernetes 环境管理更轻松。

| 工具名称               | 描述         |
|------------------------|-------------------|
| prometheus kubernetes  | Prometheus 是一个开源监控系统，为 Kubernetes 集群提供实时监控和警报功能。       |
| Grafana kubernetes     | Grafana 是一个可用于显示 Prometheus 或其他监控系统收集的指标的可视化工具。   |
| Datadog Kubernetes     | Datadog 是一个商业监控平台，为监控 Kubernetes 集群提供了全面的功能集。       |
| dynatrace Kubernetes   | Dynatrace 是另一个商业监控平台，为监控 Kubernetes 集群提供了许多功能，包括全栈可观测性和基于人工智能的洞察。   

## Kubernetes 日志记录和追踪

应用程序创建日志消息来告诉我们它们正在做什么以及发生了什么。日志记录工具收集和存储这些消息，以便我们可以查看正在发生的事情，并在出现问题时进行故障排除。日志记录是监控和管理应用程序的最重要工具之一。

微服务应用程序由许多小型、独立的服务组成，它们通过网络相互通信。追踪允许您查看应用程序中每个服务如何处理请求，以及请求完成所需的时间。

| 工具名称    | 描述                     |
|------|----------|
| Fluentd Kubernetes                | Fluentd 是 Kubernetes 的开源数据收集器。它是一个强大的工具，可用于从 Kubernetes 集群中的所有节点以及运行在 Kubernetes Pod 中的应用程序收集日志。然后，Fluentd 可用于处理和转发这些日志到各种目的地，如 Elasticsearch、Splunk 或 Amazon S3。       |
| jaeger Tracing kubernetes         | Jaeger 是一个设计用于与 Kubernetes 配合使用的开源跟踪工具。Jaeger 可以帮助您跟踪应用程序的性能，并识别性能瓶颈。            |
| open-telemetry Tracing Kubernetes | OpenTelemetry（OTel）是一个用于仪表化、生成、收集和导出跟踪、度量和日志等遥测数据的开源可观察性框架。它是一个供应商中立和语言不可知的项目，得到了广泛范围内公司和组织的支持。   |

## 故障排除与调试

用于 Kubernetes 的故障排除和调试工具是可以帮助您识别和解决 Kubernetes 集群和应用程序问题的工具。Kubernetes 是一个具有许多移动部件的复杂平台，因此手动排查问题可能会很困难。

故障排除和调试工具可以帮助您自动化此过程，并使管理 Kubernetes 环境变得更加容易。

| 工具名称             | 描述     |
|----------------------|-----------------------------|
| Kubernetes kubectl   | kubectl 是官方的 Kubernetes 命令行工具。kubectl 可以用于管理和排除故障 Kubernetes 集群和应用程序。|
| K9s Kubernetes      | K9s 是一个提供用于管理 Kubernetes 集群和应用程序的 TUI (Text-based User Interface) 的 CLI 工具。k9s 可以帮助排除 Kubernetes 问题，因为它允许您可视化您的集群和应用程序。                  |
| lens Kubernetes     | Lens 是一个用于管理 Kubernetes 集群和应用程序的图形用户界面 (GUI) 工具。Lens 也可以帮助排除 Kubernetes 问题，因为它提供了许多功能，可以帮助您诊断问题，如日志查看、性能监控和事件分析。 |

## 持续集成与交付工具

CI/CD 工具帮助开发人员快速高效地构建、测试和部署代码，并具有内置的质量保证。

**持续集成**（CI）自动化了每次更改时构建和测试代码的过程。这有助于确保代码始终处于工作状态，并且可以尽早发现任何错误。

**持续交付**（CD）将 CI 推进一步，通过自动化将代码部署到生产环境的过程。这有助于缩短发布新功能的时间，并减少人为错误的风险。

**成熟的 CI/CD 系统**可以监视源代码的更改，自动构建和测试代码，然后将其部署到生产环境。这些系统通常包括各种测试和验证步骤，以确保代码在部署到生产环境之前能够正常工作。

| 工具名称 | 描述 |
|--|--|
| jenkins kubernetes CICD        | Jenkins 是一个开源的持续集成 (CI) 和持续交付 (CD) 工具。Jenkins 可用于自动构建、测试和部署 Kubernetes 应用程序。        |
| JenkinsX| Jenkins X 提供了基于 Kubernetes 的自动化 CI+CD，使用 Cloud Native pipelines from Tekton 在拉取请求上提供预览环境。    |
| Argo Gitops Kubernetes         | Argo 是 Kubernetes 原生工具，用于运行工作流、管理集群，并正确实施 GitOps。  |
| Flux kubernetes GitOps         | Flux 是 Kubernetes 的开放且可扩展的持续交付解决方案。由 GitOps Toolkit 提供支持。                   |
| tekton Kubernetes CICD         | Tekton 是构建在 Kubernetes 上的云原生 CI/CD 平台。Tekton 提供了一组构建模块，可用于为 Kubernetes 应用程序创建自定义的 CI/CD 流水线。         |
| Gitlab CI Kubernetes           | GitLab CI 是一个持续集成 (CI) 和持续交付 (CD) 工具，可用于自动构建、测试和部署软件。它与 GitLab 代码托管平台集成，使其易于使用和管理 CI/CD 流水线。                     |
| github CICd Kubernetes         | GitHub Actions 让您轻松自动化所有软件工作流程，现在支持世界级的 CI/CD。直接从 GitHub 构建、测试和部署您的代码。让代码审查、分支管理和问题分析按照您的方式工作。            |
| Azure   | Azure Pipelines 是微软提供的支持 Kubernetes 的 CI/CD 平台。Azure Pipelines 可用于自动构建、测试和部署 Kubernetes 应用程序到 Azure Kubernetes Service (AKS)。         |
| Google Cloud Build GCP Kubernetes | Google Cloud Build 是来自 Google Cloud Platform (GCP) 的云原生 CI/CD 平台。Cloud Build 可用于自动构建、测试和部署 Kubernetes 应用程序到 GCP。      |
## Kubernetes 安全工具

**安全和合规性工具有助于使您的平台和应用程序更安全和符合规定**。它们可用于监视容器和 Kubernetes 环境中的漏洞和配置错误，并执行安全策略。换句话说，这些工具可以帮助您：

- 识别并修复容器和 Kubernetes 环境中的安全漏洞。
- 防止可能导致安全漏洞的配置错误。
- 确保您的容器和 Kubernetes 环境符合相关的法规和标准。


| 工具名称    | 描述                   |
|-----|--------------------------|
| kyverno     | Kyverno 是 Kubernetes 原生的策略管理工具，用于管理策略。https://kyverno.io                |
| trivy Kubernetes 安全              | Trivy 是一个用于在 Kubernetes 中查找漏洞、配置错误、秘密和 SBOM 的安全工具。            |
| Falco Kubernetes                   | Falco 是一款云原生的运行时安全工具，用于检测和警报可疑行为和潜在的安全威胁。它是一个由云原生计算基金会（CNCF）孵化的开源项目。<br/><br/> Falco 通过监视 Linux 内核的系统调用和事件来工作。然后，它使用一组规则来识别可疑行为，例如对文件的未经授权访问、意外的网络连接以及尝试提升特权。 <br/><br/> Falco 可用于保护 Kubernetes 集群、容器和主机。它也可以用于监视运行在其他平台上的云原生应用程序，例如 Amazon Web Services (AWS) 和 Google Cloud Platform (GCP)。 |
| open-policy-agent Kubernetes      | Open Policy Agent（OPA）可用于强制执行各种策略，包括： <br/><br/>  授权：OPA 可用于授权用户访问资源。例如，您可以使用 OPA 授权用户访问特定的 Kubernetes API 或在 Kubernetes 上部署特定的工作负载。 <br/><br/> 审计：OPA 可用于审计您的应用程序的活动。例如，您可以使用 OPA 记录所有 Kubernetes API 请求或记录对配置文件的所有更改。<br/><br/> 合规性：OPA 可用于确保您的应用程序符合特定的法规或标准。例如，您可以使用 OPA 强制执行 PCI DSS 合规性或 HIPAA 合规性。              |

查看我的关于 Trivy 的博客：[Kubernetes 安全：如何使用 Trivy 扫描您的 Docker 镜像](https://teckbootcamps.com/kubernetes-notes-trivy/)。

## Kubernetes 服务网格

**服务网格是一种控制和管理微服务之间通信的方式**。它们使平台团队能够在不更改任何代码的情况下，为集群中的所有微服务添加可靠性、可观察性和安全性等功能变得更加容易。

**服务网格现在是云原生基础设施的最重要部分之一，与 Kubernetes 一样。**

以下是使用 Kubernetes 服务网格的一些好处：

- **提高可靠性**：服务网格可以帮助提高分布式应用程序的可靠性，快速检测和解决问题。
- **增强安全性**：服务网格可以通过提供加密和身份验证等功能来增强分布式应用程序的安全性。
- **降低成本**：服务网格可以通过优化流量流向和减少资源使用来降低运行分布式应用程序的成本。
- **增加可见性**：服务网格可以为您提供对分布式应用程序的全面视图，以便您了解所有内容的性能并识别任何潜在问题。

如果您正在 Kubernetes 上运行分布式应用程序，我强烈建议您使用服务网格。它可以帮助您提高应用程序的可靠性、安全性、成本效益和可见性。

| 工具名称           | 描述         |
|--------------------|---------------------------|
| istio Service Mesh | Istio 是最成熟和广泛使用的服务网格。它提供了广泛的功能，包括流量管理、可观察性、安全性和弹性。然而，设置和管理 Istio 可能会比较复杂。    |
| linkerd Service mesh | Linkerd 是一个轻量级且快速的服务网格，易于设置和管理。它提供了一组核心功能，包括流量管理、服务发现和负载均衡。              |
| Anthos Mesh GCP   | Google Anthos Service Mesh 是来自 Google Cloud Platform (GCP) 的服务网格，为分布式应用程序提供流量管理、可观察性、安全性和弹性。它与其他 GCP 服务紧密集成。      |
| Consul Service Mesh | Consul Connect 是来自 HashiCorp 的服务网格，为微服务提供服务发现、负载均衡和加密。它与其他 HashiCorp 产品（如 Consul 和 Vault）良好集成。    |

查看我关于 Kubernetes 服务网格的入门指南：[Kubernetes 服务网格：入门指南](https://teckbootcamps.com/kubernetes-service-mesh/)

## Kubernetes 成本优化

Kubernetes 成本优化工具就像是您 Kubernetes 集群的财务顾问。它可以帮助您做出关于如何在 Kubernetes 上花费资金的明智决策，以便您可以最大限度地发挥投资的价值。

以下是使用 Kubernetes 成本优化工具的一些好处：

- **降低成本**：Kubernetes 成本优化工具可以帮助您将运行 Kubernetes 集群和应用程序的成本降低多达 50%。
- **提高效率**：Kubernetes 成本优化工具可以帮助您通过消除资源浪费和优化 Pod 调度来提高 Kubernetes 集群的效率。
- **增加可见性**：Kubernetes 成本优化工具可以为您提供对 Kubernetes 成本的全面视图，以便您了解资金的流向并确定改进的方向。
- **安心**：Kubernetes 成本优化工具可以让您安心，知道您的 Kubernetes 集群正在被高效地管理，而且您没有过度花费资金。

如果您正在运行 Kubernetes 集群，我强烈建议您使用成本优化工具。它可以帮助您节省资金、提高效率，并增加对 Kubernetes 成本的可见性。

| 工具名称         | 描述             |
|------------------|--|
| kubecost         | Kubecost 是一个免费的开源工具，为 Kubernetes 集群提供详细的成本分析和建议。它可以帮助您识别和消除资源浪费，优化您的 Pod 调度，并为您的需求选择合适的定价模型。                           |
| cast ai kubernetes | CAST AI 是一个商业工具，为 Kubernetes 集群提供基于人工智能的成本优化。它可以帮助您识别和消除资源浪费，优化您的 Pod 调度，并为您的需求选择合适的定价模型。|

## 结论

总之，这个精选列表为任何人在复杂的 Kubernetes 生态系统中导航提供了宝贵的资源。随着这个领域的不断发展，及时了解最新的工具和最佳实践至关重要。

**随时欢迎您定期查看此列表的更新，因为我们将不断完善它，以确保它仍然是一个可靠的参考点。**

此外，我们欢迎您对您在日常 Kubernetes 旅程中发现的其他不可或缺的工具提出评论和建议。让我们共同为每个人改进 Kubernetes 的体验！