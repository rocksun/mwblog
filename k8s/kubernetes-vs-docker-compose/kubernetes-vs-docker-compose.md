
<!--
title: Kubernetes vs. Docker Compose：应该选择哪个编排工具？
cover: https://cdn.thenewstack.io/media/2023/11/25b9af59-kubernetes-webassembly-1.jpg
summary: 🚀云原生时代，容器编排选谁？Docker Compose轻量易上手，适合本地开发；Kubernetes专为大规模分布式系统而生，支持高可用、自动伸缩，玩转CI/CD、GitOps。YAML配置是关键，Helm保驾护航，更有Prometheus、OpenTelemetry加持，可观测性Max！😎
-->

🚀云原生时代，容器编排选谁？Docker Compose轻量易上手，适合本地开发；Kubernetes专为大规模分布式系统而生，支持高可用、自动伸缩，玩转CI/CD、GitOps。YAML配置是关键，Helm保驾护航，更有Prometheus、OpenTelemetry加持，可观测性Max！😎

> 译自：[Kubernetes vs. Docker Compose: Which Orchestration Tool Should You Choose?](https://thenewstack.io/kubernetes-vs-docker-compose/)
> 
> 作者：Sunny Yadav

Kubernetes vs. Docker Compose：

- **Docker Compose** 非常适合本地开发和小型应用程序。它易于设置，并在单台机器上运行。
- **Kubernetes** 专为大型分布式系统而构建。它提供高级扩展、自动化和高可用性，但同时也带来了更高的复杂性。

当我们构建容器化应用程序时，我们需要一种方法来管理这些容器的运行方式。这就是编排工具的用武之地。

Docker Compose 和 [Kubernetes](https://thenewstack.io/kubernetes/) 是两个流行的选择。它们都帮助我们定义、部署和管理多容器应用程序，但它们以非常不同的方式来实现。了解每种工具的功能、它们的比较以及何时选择其中一种。了解这些差异将帮助我们为工作选择合适的工具。

## Kubernetes vs. Docker Compose：概述

以下是 Kubernetes 和 Docker Compose 之间主要区别的快速概述：

| 特性           | Docker Compose                 | Kubernetes                       |
| -------------- | ------------------------------ | -------------------------------- |
| 解决的问题     | 单台机器上的简单多容器应用程序 | 跨多台机器的复杂应用程序         |
| 核心概念       | 服务、网络、卷                 | Pod、Deployment、服务             |
| 设置和学习曲线 | 易于设置，快速学习             | 设置和学习更复杂                 |
| 扩展           | 仅限于单个节点                 | 跨多个节点的水平扩展             |
| 网络           | 简单的桥接网络、服务名称       | 集群范围的网络、用于外部访问的 Ingress |
| 存储和状态管理 | 用于本地存储的命名卷           | 用于持久性的 PersistentVolume、StatefulSet |
| CI/CD 和自动化 | 在开发容器、GitHub Actions 中很简单 | Helm、GitOps、高级自动化          |
| 可观测性和调试 | 基本日志和统计信息             | 高级指标、跟踪和调试工具         |
| 成本和资源效率 | 轻量级，本地资源使用           | 更多开销，但自动缩放以提高效率   |

## 每种工具解决什么问题？

在比较 Docker Compose 和 Kubernetes 之前，让我们看看每种工具旨在解决什么问题。两者都帮助我们管理容器化应用程序，但它们是为不同类型的项目和团队需求而构建的。

### Docker Compose 用于单节点工作流程

当我们想要在单台机器上运行和管理多个[容器](https://thenewstack.io/introduction-to-containers/)时，Docker Compose 非常有用。它可以使事情变得简单。我们在一个文件中定义我们的服务，并使用单个命令运行它们。

**它非常适合**：

- 本地开发
- 测试小型应用程序
- 快速启动服务，例如 Web 服务器、[数据库](https://thenewstack.io/introduction-to-databases/)和 API
- 与团队成员共享设置说明

它轻巧且易于学习。但它不适合跨多个服务器进行扩展或运行。

### Kubernetes 用于分布式系统

Kubernetes 帮助我们在多台机器上运行容器。它是为需要高可用性、自动缩放和对部署进行强大控制的团队而构建的。

**当我们这样做时，它会发光**：

- 在生产环境中运行应用程序
- 管理跨多个容器的流量
- 处理故障和重启
- 需要自动缩放

Kubernetes 更强大，但也更复杂。它专为无法仅在一台机器上运行的严肃工作负载而设计。

## 架构和核心概念

现在让我们看看每种工具是如何构建的，以及它们使用哪些关键思想。这有助于我们了解它们如何在幕后管理容器。

### Compose 服务、网络和卷

在 Docker Compose 中，我们将容器分组到服务中。每个服务运行一个容器镜像。例如，我们可能有一个用于 Web 应用程序的服务，一个用于数据库的服务，以及另一个用于缓存的服务。

Compose 还设置网络，以便我们的服务可以轻松地相互通信。无需将端口暴露给外部。卷用于存储需要保留的数据，例如数据库文件。这样，当容器停止或重新启动时，我们不会丢失重要信息。

一切都在一个 docker-compose.yml 文件中定义。它易于阅读且易于更改。

### Kubernetes Pod、Deployment 和服务

Kubernetes 的工作方式略有不同，并且有几个 [Kubernetes 构建块](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/)。基本单位是 pod，而不是容器。一个 pod 可以运行一个或多个共享存储、网络和设置的容器。

我们使用 Deployment 来管理这些 pod。Deployment 告诉 Kubernetes 我们需要多少个 pod 并保持它们的运行。如果一个 pod 崩溃，Kubernetes 会将其恢复。

Kubernetes 中的服务帮助 pod 相互通信。它们还管理流量如何流入和流出集群。
与 Compose 不同，Kubernetes 将这些部分拆分为不同的文件或命令。它需要更多的设置，但也为我们提供了更多的控制权。

## 设置和学习曲线

每种工具的入门感觉都非常不同。一个简单快速，另一个需要更多时间，但提供更强大的功能。

### 本地安装和配置

Docker Compose 很容易设置。如果我们安装了 Docker，基本上就可以开始了。我们只需编写一个 **docker-compose.yml 文件**，运行 **docker-compose up**，我们的应用程序就开始运行了。它非常适合本地开发。无需安装任何其他东西。我们可以快速启动或关闭环境。

Kubernetes 需要更多的设置。对于本地测试，我们可以使用 Minikube、kind 或启用 Kubernetes 的 Docker Desktop 等工具。这些增加了一些额外的步骤。我们还需要了解[集群如何工作](https://thenewstack.io/managing-kubernetes-clusters-for-platform-engineers/)——即使在单台机器上运行。

### 声明式 YAML 的复杂性

这两种工具都使用 [YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)，但 Kubernetes 将其提升到了一个新的水平。在 Docker Compose 中，我们的 YAML 文件简短易懂。通常一个文件就可以完成任务。

**在 Kubernetes 中，我们通常需要多个 YAML 文件才能运行单个应用程序**：

*   一个用于 Pod 或 Deployment
*   一个用于 Service
*   一个用于存储或配置设置

这使得事情更强大，但也更难学习。结构很严格，小的错误可能会导致问题。我们需要花更多的时间来理解各个部分是如何组合在一起的。

## 扩展和高可用性

如果我们的应用程序增长，我们需要它来处理更多的流量，并在出现问题时保持在线。这就是这些工具真正开始有所不同的地方。

### Kubernetes 中的水平扩展

Kubernetes 是为扩展而构建的。它可以跨不同的机器运行同一 Pod 的多个副本（称为 replicas）。我们设置副本的数量，Kubernetes 会处理剩下的事情。

如果我们需要在繁忙时段进行扩展，Kubernetes 可以自动执行此操作。它还可以平衡 Pod 之间的流量，并重新启动任何失败的 Pod。这使得它非常适合高可用性。如果一个 Pod 或机器出现故障，应用程序仍然可以继续运行。

### Docker Compose 中的副本限制

Docker Compose 可以运行服务的多个副本，但它受到限制。所有副本都在同一台机器上运行。没有内置的方法可以将它们分布在集群中。

我们可以使用 **–scale** 标志来运行更多的容器，但没有自动负载平衡或故障转移。如果机器崩溃，一切都会停止运行。Compose 适用于小型应用程序或开发工作，但不适用于高流量或关键系统。

## 网络和服务发现

这两种工具都帮助我们的容器相互通信。但它们以不同的方式做到这一点，这会影响我们构建和连接服务的方式。

### Compose Bridges 和服务名称

Docker Compose 默认创建一个私有桥接网络。同一 Compose 文件中的所有服务都在此网络上，并且可以使用其服务名称相互通信。

例如，如果我们有一个需要数据库的 Web 应用程序，该应用程序可以直接连接到数据库——无需 IP 或特殊设置。这适用于小型项目。它简单而自动。

### Kubernetes 集群网络和 Ingress

Kubernetes 使用集群范围的网络。每个 Pod 都有自己的 IP。集群内部的服务可以通过 Kubernetes Service 相互通信，Kubernetes Service 处理流量和路由。

对于外部访问，我们通常使用 [Ingress](https://thenewstack.io/ingress-kubernetes-example-with-ngrok/)。这就像一个智能路由器，控制哪些请求去哪里。它还有助于处理 HTTPS 和域名等问题。Kubernetes 网络更强大，但需要更多的时间来理解和配置。

## 存储和状态管理

当我们的应用程序需要保存数据时——例如，用户信息或日志——我们需要[数据存储](https://thenewstack.io/storage/)，该存储在容器重新启动时不会消失。这两种工具都提供了处理此问题的方法，但方式不同。

### 命名卷与 PersistentVolumeClaims

在 Docker Compose 中，我们使用命名卷。这些在 Compose 文件中定义，并且可以在服务之间共享。它们易于设置，并且适用于本地开发。例如，我们可以为数据库创建一个卷，以便即使容器停止，其数据也能保持安全。

在 Kubernetes 中，我们使用 PersistentVolumeClaims (PVC)。这些是对存储的请求，连接到 PersistentVolume (PV)。它更灵活，更适合大型设置。我们可以使用 [云存储](https://thenewstack.io/to-store-in-the-cloud-or-on-premises-how-about-door-no-3/)、本地磁盘或网络驱动器。PVC 更复杂，但它们让我们将应用程序与存储分离。

### StatefulSets 和数据持久性

对于需要稳定存储的应用程序（如数据库），Kubernetes 有一种称为 StatefulSet 的东西。它可以确保每个 pod 都有一个唯一的名称和自己的存储。即使 pod 重新启动或移动到另一个节点，它也会保留其数据。

Docker Compose 没有完全匹配的功能。所有服务都被同等对待，如果我们要扩展或移动东西，管理长期数据可能会变得棘手。

## CI/CD 和自动化

自动化可以帮助我们更快地构建、测试和部署应用程序。Docker Compose 和 Kubernetes 都可以用于 [CI/CD pipelines](https://thenewstack.io/ci-cd/)，但工具和工作流程有所不同。

### Dev Containers 和 GitHub Actions 中的 Compose

Docker Compose 在开发管道中运行良好。我们可以将其与 VS Code 中的 Dev Containers 结合使用，以快速启动本地环境。它非常适合测试需要多个服务的应用程序。

在 [GitHub Actions](https://thenewstack.io/8-github-actions-for-setting-up-your-ci-cd-pipelines/) 等 CI 工具中，我们可以运行 `docker-compose up` 来在合并或部署之前测试我们的应用程序。它很简单并且可以完成任务。Compose 非常适合早期自动化、本地测试和小型团队。

### 带有 Helm 和 GitOps 的 Kubernetes

Kubernetes 专为大规模自动化而设计。我们经常使用 [Helm](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/) 等工具来管理复杂的部署。Helm 允许我们将应用程序打包到 charts 中，并在不同环境中重用配置。

为了实现更多的自动化，团队使用 [GitOps](https://thenewstack.io/gitops-for-databases-on-kubernetes/)。这意味着我们将所有 Kubernetes 设置存储在 Git 中。当我们更新存储库时，Argo CD 或 Flux 等工具会将更改同步到集群。它需要更多的设置，但功能强大，尤其适用于管理许多应用程序或集群的团队。

## 可观测性 和调试

为了保持应用程序的健康，我们需要了解应用程序内部发生的事情。日志、指标和调试工具可以帮助我们发现问题并快速修复它们。

### 使用 docker compose 记录日志和统计信息

Docker Compose 为我们提供了检查正在发生的事情的基本工具。我们可以运行 `docker-compose logs` 来查看我们的容器正在做什么。它显示了每个服务的输出。

我们还可以运行 `docker stats` 来查看 CPU 和内存使用情况。它有助于在开发过程中进行快速检查。为了获得更深入的了解，我们需要自己添加 Prometheus 或 Grafana 等工具，因为 Compose 默认不包含它们。

### 指标、追踪和 kubectl Debug

Kubernetes 将可观测性提升到了更高的水平。我们可以运行 `kubectl logs` 来检查日志，就像使用 Compose 一样。但是我们也可以使用 `kubectl describe` 或 `kubectl debug` 来更深入地研究 pod 的行为。

**Kubernetes 可以很好地与以下监控工具配合使用**：

*   Prometheus 用于指标
*   Grafana 用于仪表板
*   Jaeger 或 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 用于追踪

这使得跟踪复杂系统中的问题变得更加容易，但也意味着需要更多的设置和学习。

## 成本和资源效率

让我们来谈谈每种工具如何使用系统资源，以及这对成本和性能意味着什么。

### 本地资源占用

Docker Compose 是轻量级的。它在单台机器上运行所有内容。除了容器本身之外，没有额外的开销。这使得它非常适合本地开发，因为我们不需要太多的 RAM 或 CPU 即可启动小型应用程序。它对于单节点工作来说简单而高效。

### 集群开销和自动缩放

Kubernetes 使用更多资源。即使是小型集群也需要 API 服务器、调度程序和控制器管理器等后台服务。这些服务使系统平稳运行，但会增加开销。

也就是说，[Kubernetes 专为自动缩放而构建](https://thenewstack.io/kubernetes-autoscaling-q-a-with-fairwinds-cto-andy-suderman/)。它可以根据流量向上或向下扩展 pod。如果我们在使用云提供商，它甚至可以扩展整个集群，添加或删除节点。因此，虽然运行成本更高，但它可以在规模上更有效率。我们只为我们需要的付费——当我们需要的时侯。

## 何时选择 Docker Compose

在以下情况下，Docker Compose 是一个不错的选择：

*   **您需要一个简单的设置**：如果您正在处理小型应用程序或本地环境，Compose 快速而简单。无需担心复杂的配置。
*   **您想在本地进行测试**：它非常适合本地开发和测试。我们可以在单台机器上启动多个容器，而无需太多开销。
*   **您正在组建一个小团队或个人项目**：如果您没有管理大型分布式系统，Docker Compose 可以帮助您保持事物井井有条。
*   **您不需要自动缩放**：如果您的应用程序不需要动态缩放，Compose 就可以正常工作。它专为简单性而构建，而不是复杂性。

简而言之，当我们想要在单台机器上简单、快速且易于管理的东西时，Docker Compose 非常棒。

## 何时选择 Kubernetes

在以下情况下，Kubernetes 是最佳选择：

- **你需要管理一个大型系统**： 如果你在多台机器上运行多个服务，Kubernetes 可以帮助你顺利地组织和扩展一切。
- **高可用性至关重要**： Kubernetes 自动处理 Pod 重启、扩展和负载均衡，确保你的应用程序保持在线，即使部分组件发生故障。
- **你需要自动缩放**： Kubernetes 可以根据流量进行向上或向下扩展，使其成为处理需求变化的理想选择。[自动缩放](https://thenewstack.io/getting-the-most-from-kubernetes-autoscaling/)
- **你正在管理复杂的生产级应用程序**： Kubernetes 专为大型分布式系统而构建，并提供强大的工具，用于大规模监控、调试和部署。
- **你希望在混合环境中**： Kubernetes 跨云提供商、本地或混合设置运行良好，从而使我们能够更好地控制基础设施。[混合环境](https://thenewstack.io/how-to-go-about-setting-up-a-hybrid-cloud-environment/)

简而言之，当你的应用程序需要跨多台机器进行扩展、保持可用性并进行管理时，请选择 Kubernetes。

## 从 Docker Compose 迁移到 Kubernetes 的路径

从 Docker Compose 迁移到 Kubernetes 似乎是一个很大的步骤，但如果我们一次完成一个阶段，这是可以管理的。请按照以下步骤操作：

- **了解你当前的设置**： 首先查看你的 Docker Compose 配置。确定需要迁移的服务、网络和卷。这将使你清楚地了解应用程序的架构。
- **将 Compose 文件转换为 Kubernetes 清单**： 使用 Kompose 等工具自动将 Docker Compose 文件转换为 Kubernetes YAML 文件。你需要调整这些文件以适应你的 Kubernetes 集群设置。[Kubernetes 清单](https://thenewstack.io/manifest-first-deploy-with-confidence/)
- **设置 Kubernetes 集群**： 在迁移之前，你需要一个 Kubernetes 集群。你可以使用 [Google Kubernetes Engine (GKE)](https://thenewstack.io/google-kubernetes-engine-customized-for-faster-ai-work/)、Amazon EKS 等服务，或者使用 Minikube 设置本地集群。
- **创建部署、服务和卷**： 在 Kubernetes 中，我们需要为每个服务定义 Deployment，为处理内部和外部访问定义 Service，以及为存储定义 PersistentVolumeClaims。
- **上线前进行本地测试**： 设置 Kubernetes 清单后，使用 kubectl apply 在本地对其进行测试。在扩展到生产环境之前，请确保一切正常。
- **逐步迁移**： 每次迁移一个服务。Kubernetes 允许我们并行运行 Docker Compose 和 Kubernetes 服务，从而简化过渡。
- **监控和优化**： 迁移后，请密切关注资源使用情况、性能和扩展。Kubernetes 为我们提供了强大的工具来监控和根据需要调整配置。

## Kubernetes vs. Docker Compose：结论

选择 Docker Compose 还是 Kubernetes 取决于我们项目的规模和复杂性。

- **Docker Compose** 非常适合较小的项目、本地开发和简单的应用程序。它易于设置、使用快速，并且非常适合单节点环境。
- **Kubernetes** 在我们需要管理具有高可用性和自动缩放功能的大型分布式系统时，它会发光。它非常适合需要强大的编排和监控的复杂生产级应用程序。

如果我们只是刚开始或正在开发一个小型应用程序，那么 Docker Compose 是最佳选择。但是，随着我们扩展并需要更多地控制性能、正常运行时间和可伸缩性，Kubernetes 成为更好的选择。这两种工具都很强大，但了解我们的需求是做出正确决策的关键。