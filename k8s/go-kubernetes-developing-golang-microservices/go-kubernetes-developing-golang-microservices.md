
<!--
title: 使用Go和Kubernetes快速开发微服务
cover: https://cdn.sanity.io/images/rhzn5s2f/production/af7c417ea93bd3a822c5f4f4325cb66a204cd7b9-1200x627.jpg?w=1230&fit=max&auto=format
-->

[Kubernetes](/blog/kubernetes-tutorial-beginners-guide) 是一个容器编排平台，使用户能够以任意规模（从一项服务到数千项服务）部署和扩展其微服务应用程序。但是，释放 Kubernetes 的强大功能通常比最初看起来要复杂得多；应用程序开发人员的学习曲线尤其陡峭。了解该怎么做只是成功的一半；接下来，你必须为这项工作选择最佳工具。那么，[Go](/docs/telepresence-oss/latest/quick-start/go/) 开发人员如何在 Kubernetes 上创建快速而有效的开发工作流？

> 译自 [Rapid Golang Microservices Development with Go & Kubernetes](https://www.getambassador.io/blog/go-kubernetes-developing-golang-microservices)，作者 Jake Beck。

## 使用 Golang 和 Telepresence 构建云开发环境

应用程序开发人员在尝试在 Kubernetes 上创建[高效的开发工作流](/use-case/productive-local-dev-environment)时面临两项独特的挑战：

1. 大多数开发工作流针对本地开发进行了优化，而 Kubernetes 应用程序被设计为云原生的。
2. 随着 Kubernetes 应用程序演变为复杂的[微服务](/kubernetes-glossary/microservices)架构，开发环境也变得更加复杂。每项微服务都会增加额外的依赖项，并且这些服务很快就会开始需要比[本地开发环境](/blog/kubernetes-dev-environments-local-remote)中通常可用的更多资源。

在本教程中，我们将为 Kubernetes 设置一个开发环境，并对 [Golang](/blog/debug-go-microservices-kubernetes-vscode) 微服务进行更改。通常，要在本地进行开发，我们必须等待容器构建，将其推送到注册表，并将其部署才能看到代码更改的效果。相反，我们将使用 Telepresence 立即查看更改的结果。

## 步骤 1：部署示例微服务应用程序

对于我们的示例，我们将对在资源密集型 Java 服务和大型数据存储之间运行的 Go 服务进行代码更改。我们将首先部署一个由 3 项服务组成的示例微服务应用程序：

- **VeryLargeJavaService**：用 Java 编写的内存密集型服务，负责为我们的应用程序生成前端图形和网页。
- **DataProcessingService**：在 VeryLargeJavaService 和 VeryLargeDataStore 之间管理信息请求的 Golang 服务。
- **VeryLargeDataStore**：包含 Edgey Corp 商店示例数据的大型数据存储服务。

**注意**：“VeryLarge”描述符用于强调你的本地环境可能没有足够的 CPU 和 RAM 来处理这些服务，或者你可能不想为每个开发人员承担额外的开销成本。

![Go 和 Kubernetes](https://cdn.sanity.io/images/rhzn5s2f/production/47ee441979ac21d300f15159776bab3e411c2179-1400x1040.jpg?w=1920&fit=max&auto=format)

在此架构图中，你将注意到来自用户的请求通过 ingress controller 路由到我们的服务。为简单起见，在本教程中，我们将跳过[部署 ingress controller](/docs/edge-stack/latest/tutorials/getting-started#kubernetes-yaml/)。如果你已准备好在你自己的设置中使用 Telepresence，并且正在寻找一种设置 ingress controller 的简单方法，我们建议查看 [Edge Stack API 网关](/products/edge-stack/api-gateway)。

**让我们将示例应用程序部署到你的 Kubernetes 集群：**

```
kubectl apply -f
```

## 步骤 2：设置本地 Go 开发环境

我们需要一个本地开发环境，以便我们可以编辑 `DataProcessingService` 服务。如上所示的架构图中所示，`DataProcessingService` 依赖于 `VeryLargeJavaService` 和 `VeryLargeDataStore`，因此为了对该服务进行更改，我们还必须与这些其他服务进行交互。让我们开始吧！

**1. 从 GitHub 克隆此应用程序的存储库。**

```
git clone https://github.com/datawire/edgey-corp-go.git
```