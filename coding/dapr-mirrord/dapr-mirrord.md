<!--
title: Dapr和Mirrord：为开发赋能
cover: https://metalbear.co/blog/dapr-mirrord/thumbnail.png
summary: Dapr简化云原生应用构建，但本地开发复杂。Mirrord使本地代码在Kubernetes集群上下文中运行，与Dapr Sidecar交互，无需频繁部署。通过流量镜像和窃取，实现快速迭代和调试，提高开发效率。Dapr与Mirrord结合，专注于应用代码，加速交付。
-->

Dapr简化云原生应用构建，但本地开发复杂。Mirrord使本地代码在Kubernetes集群上下文中运行，与Dapr Sidecar交互，无需频繁部署。通过流量镜像和窃取，实现快速迭代和调试，提高开发效率。Dapr与Mirrord结合，专注于应用代码，加速交付。

> 译自：[Supercharging Development With Dapr and mirrord](https://metalbear.co/blog/dapr-mirrord/)
> 
> 作者：Arsh Sharma

[Dapr](https://dapr.io/) (分布式应用运行时) 是一个旨在简化云原生应用构建的框架。通过抽象诸如服务调用、发布/订阅、状态管理和遥测等任务，Dapr 显著加快了开发速度。在本博客中，我们将探讨 Dapr 解决了哪些问题（以及您为什么应该使用它），当您开始将 Dapr 与 Kubernetes 一起使用时，本地开发体验 (DevEx) 是怎样的，然后通过一个演示展示如何使用 [mirrord](https://metalbear.co/mirrord/) 改善 DevEx！

## Dapr 解决的问题

构建现代云原生应用通常需要开发人员解决与实际业务逻辑关系不大的复杂问题。这些任务最终会占用他们大量时间，而这些时间本可以用于开发实际产品本身。

例如，假设您的应用程序有多个微服务，这些微服务需要使用发布/订阅消息传递（pub/sub）进行通信。如果没有 Dapr，您的开发人员将需要直接处理所有细节，例如设置与消息传递系统（如 Kafka 或 RabbitMQ）的连接、管理重试、处理消息格式以及处理故障。在多个服务中执行此操作会导致代码重复且更难维护。

Dapr 通过提供简单的发布/订阅 API 来简化此过程。开发人员只需告诉 Dapr 发布消息或订阅消息，而无需直接处理消息传递系统详细信息。Dapr 在后台处理消息传递、重试和错误处理。

![Dapr 如何使用发布/订阅的概述](https://metalbear.co/blog/dapr-mirrord/pubsub-overview.png)

*Dapr 如何使用发布/订阅的概述（来自 Dapr 文档）*

这种方法不仅使您的开发人员免于一遍又一遍地编写相同的样板代码，而且还具有一个额外的好处：灵活性。如果您的团队稍后决定从一个消息传递系统（如 Kafka）切换到另一个消息传递系统（如 RabbitMQ），则您的开发人员无需重写任何代码。他们只需更新配置文件，Dapr 就会处理剩下的事情。

发布/订阅消息传递只是我们在此讨论的一个示例。Dapr 还为管理状态、可靠地调用其他服务、安全地处理密钥、添加**可观测性**等 [提供 API](https://docs.dapr.io/developing-applications/building-blocks/)。简而言之，Dapr 帮助您避免基础架构难题，保持代码简单，并让您的开发人员专注于构建您的产品。

## 使用 Dapr 和 Kubernetes 进行开发时遇到的问题

因此，您的团队已经认识到 Dapr 提供的价值，并且您决定采用 Dapr 来帮助您的服务与特定的基础架构依赖项解耦。

在生产中使用 Kubernetes 部署时，采用 Dapr 非常简单。Kubernetes 会自动在每个应用程序 Pod 旁边注入一个专用的 Dapr Sidecar。这些 Sidecar 管理与基础架构组件的通信。

![使用 Dapr 和 K8s 时 Sidecar 注入的工作原理概述](https://metalbear.co/blog/dapr-mirrord/dapr-injection.png)

*使用 Dapr 和 K8s 时 Sidecar 注入的工作原理*

但是，一旦您的团队开始在本地进行开发和测试，复杂性就会出现。与 Kubernetes 提供的自动 Sidecar 注入不同，本地设置需要手动操作。开发人员通常使用 Docker Compose 或手动引导 Dapr 运行时（使用其 CLI）来模仿 Kubernetes 环境。这些方法虽然可行，但永远无法完全复制生产设置。网络、配置、安全策略和环境变量的差异通常会在不知不觉中溜进来。

结果是？开发人员最终完全依赖 CI 管道和暂存环境来确保他们编写的代码能够正常工作。管道和到暂存环境的部署需要几分钟到半小时不等。这会中断开发人员流程，降低迭代速度，并最终延迟您的团队交付产品的能力。

mirrord 的构建正是为了解决这种摩擦。

## mirrord 简介

mirrord 允许您在 Kubernetes 集群的上下文中运行本地代码。它通过允许您镜像集群和本地计算机之间的传入和传出流量来实现这一点。它还允许您本地运行的代码访问来自集群的环境变量和其他配置。通过执行所有这些操作，mirrord 使您的本地进程“认为”它正在云中运行，从而允许您在类似生产的条件下对其进行测试。如果您想了解更多关于 mirrord 如何工作的信息，请查看 [我们的文档](https://metalbear.co/mirrord/docs/overview/introduction/#how-it-works)。

使用 mirrord 可以使您在本地编写的代码直接与 Kubernetes 部署的 Dapr Sidecar 和集群中运行的其他服务进行交互。使用 mirrord，您可以：

* 在本地运行您的服务，但与真正的 Dapr Sidecar 和其他集群服务进行交互，而无需每次都部署您的代码。
* 从暂存环境中运行的 Kubernetes Pod 窃取流量，以模拟类似生产的交互。
* 利用实际的 Kubernetes 配置，包括密钥、环境变量和服务网格设置。

这意味着：

* 您可以快速迭代启用了 Dapr 的服务，而无需多次通过 CI 管道和部署。
* 您可以在本地调试和测试，但可以使用实际的集群行为、数据和交互。
* 您不必依赖 Docker Compose 等工具在开发期间在本地运行和管理容器，从而避免了重建镜像、重启容器和等待的需要。

### 为什么这比使用像 Tilt 这样的工具更好？

Tilt 是人们用来简化云应用程序本地开发的另一种工具。Tilt 的工作原理是在您进行代码更改时构建和部署容器镜像。但是，即使 Tilt 自动化了这些步骤，它仍然需要为每次迭代重复构建和部署容器，这会减慢您的反馈循环。

相比之下，mirrord 通过将您的本地环境直接与 Kubernetes 集群集成，完全消除了这种重复开销。使用 mirrord，您的代码的行为就像在集群中运行一样（使用集群服务和配置），从而提供即时反馈，而无需不断重建和重新部署。

## 将 Dapr 与 mirrord 一起使用

### 前提条件

为了按照本分步教程进行操作，请确保您已设置以下内容：

请注意，虽然我将 mirrord 与 VS Code 一起使用，但它也支持其他代码编辑器，如 Cursor、Windsurf 和 JetBrains IDE。您也可以始终使用 [mirrord CLI](https://metalbear.co/mirrord/docs/overview/quick-start/#cli-tool) 而不是代码编辑器扩展。

### 创建 Kubernetes 集群

我们将使用 k3d 创建一个本地 Kubernetes 集群：

```
k3d cluster create dapr-mirrord

```

这将使用 Docker 容器启动一个轻量级的本地 K8s 集群。可以随意使用任何云提供商的集群或其他本地工具，如 minikube、kind 等。mirrord 只需要一个 Kubernetes 集群；它在哪里运行并不重要 :)

请注意，我们仅在本演示中使用本地集群，以便易于理解。理想情况下，您希望将 mirrord 与看起来像您的生产环境的集群一起使用，例如暂存或测试集群。

### 在集群中初始化 Dapr

集群启动后，使用 dev 选项在 Kubernetes 模式下初始化 Dapr：

```
dapr init -k --dev

```

这将在集群中安装 Dapr 控制平面和必要的组件。`--dev` 标志部署 Dapr 在 Kubernetes 集群本身中需要的 Redis 和 Zipkin 组件。您可以在 [此处](https://docs.dapr.io/operations/hosting/kubernetes/cluster/) 了解有关在 Kubernetes 集群中配置 Dapr 的不同方法的更多信息。

### 部署示例服务 

在本指南中，我们将使用 Dapr 社区的 Hello Kubernetes [入门应用程序](https://github.com/dapr/quickstarts/tree/master/tutorials/hello-kubernetes)。克隆我们在此处的示例应用程序版本。该应用程序由两个微服务组成：一个 Node.js 应用程序和一个 Python 应用程序，它们使用 Dapr 协同工作。Python 应用程序生成消息，而 Node 应用程序使用并持久化这些消息。以下架构图说明了构成此应用程序的组件：

应用 Kubernetes 清单：

```
kubectl apply -f ./deploy/node.yaml
kubectl apply -f ./deploy/python.yaml

```

这些 YAML 文件定义了每个服务的部署和 Dapr Sidecar。

### 观察实时集群日志

让我们看一下 `node` 服务当前正在记录的内容。这将帮助您了解在我们将 mirrord 插入情景之前的工作方式。

```
kubectl logs --selector=app=node -c node --tail=-1

```

示例输出：

```
Got a new order! Order ID: 155266
Successfully persisted state for Order ID: 155266
Got a new order! Order ID: 155267
Successfully persisted state for Order ID: 155267
...

```

这些日志表明，该服务正在集群中按预期接收和处理订单。

### 更改代码以向 Node 应用程序添加调试信息

让我们修改 Node 应用程序以记录处理请求的 Pod 名称。这将使我们能够确认请求是在本地（由 mirrord）还是在集群中处理的。

在 `./node/app.js` 中，更改此行：

```
console.log("Got a new order! Order ID: " + orderId);

```

改为：

```
console.log("Got a new order! Order ID: " + orderId + ", pod Name: " + process.env.HOSTNAME ?? "unknown");

```

这将在每个日志条目中打印 Pod 名称。

### 创建 mirrord.json 配置文件

默认情况下，mirrord 将“镜像”进入目标微服务的流量，并且集群中运行的原始微服务将继续回复请求。由于我们也要测试代码的响应（即在日志中查看 Pod 名称），因此我们需要在 mirrord 中启用 [窃取模式](https://metalbear.co/mirrord/docs/using-mirrord/steal/)。我们可以通过创建一个简单的配置文件 `./.mirrord/mirrord.json` 来做到这一点：

```
{
  "feature": {
    "network": {
      "incoming": "steal"
    }
  }
}

```

`incoming: "steal"` 设置告诉 mirrord 拦截（或“窃取”）原本用于远程 Pod 的传入流量，并将其转发到您的本地进程。然后，本地进程将是回复任何原本用于远程 Pod 的请求的进程。这是让您像在集群内部一样测试本地代码的关键。

### 在 VS Code 中激活 mirrord

现在让我们使用 mirrord 在本地运行 Node 应用程序：

* 单击 VS Code 底部菜单中的 mirrord 图标。
* 选择“选择活动配置”，然后选择您的 `mirrord.json` 的位置。
* 转到 VS Code 中的“运行和调试”部分。
* 确保在 node 目录中运行 `npm install`，以便应用程序可以启动。
* 从 VS Code 在调试模式下启动 Node 应用程序。

### 观看流量被窃取

本地应用程序运行后，您将开始看到如下日志：

```
Got a new order! Order ID: 154876, pod Name: nodeapp-569c55fffc-wc7kr
Successfully persisted state for Order ID: 154876
Got a new order! Order ID: 154877, pod Name: nodeapp-569c55fffc-wc7kr
Successfully persisted state for Order ID: 154877
...

```

Pod 名称现在出现在日志中，但您需要注意的真正酷的部分是，用于记录 Pod 名称的代码仅存在于本地运行的应用程序中，而不存在于集群中的实际 Pod 中。这意味着：

* 您正在拦截原本用于远程 Pod 的请求。
* 您的本地进程正在从集群继承配置（如 Pod 名称）。
* 您可以立即测试本地代码更改，而无需任何镜像重建或重新部署。

## 使用 Dapr 和 mirrord 更轻松地进行云开发

总而言之，构建云原生应用程序在很多不同的原因上都很困难，而像 Dapr 这样的工具可以帮助解决其中的一些挫败感。让 Dapr 抽象出与基础架构相关的配置可以让您专注于您的应用程序。但是，当采用像 Dapr 这样的工具时，您的开发环境会慢慢开始偏离生产环境，并且您会发现自己更多地依赖 CI 管道和暂存环境，这会降低开发人员的生产力。mirrord 解决了这个问题。一起使用 Dapr 和 mirrord 可以让您只专注于您的应用程序代码，同时让这两个工具处理基础架构和开发环境设置的复杂性。它们共同创造了一种开发体验，使您的团队能够以比以前快得多的速度交付代码！如果您想了解更多关于 mirrord 的信息，请查看我们的 [文档](https://metalbear.co/mirrord/docs/overview/introduction/)。