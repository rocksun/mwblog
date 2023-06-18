# Kubernetes 开发者门户的“运行服务”蓝图

翻译自 [‘Running Service’ Blueprint for a Kubernetes Developer Portal](https://thenewstack.io/running-service-blueprint-for-a-kubernetes-developer-portal/) 。

运行服务提供运行时数据，以便我们可以在环境、部署和状态的背景下理解一个服务。

![](https://cdn.thenewstack.io/media/2023/06/a93a3de6-shutterstock_1-1024x599.jpg)

内部开发者门户存在的目的是为开发者提供类似产品的体验，减少认知负荷，让开发者能够保持工作状态并提高生产力。这些门户由平台工程团队创建，旨在帮助开发者在内部规范和质量标准的框架内进行自助服务。

通过门户，开发者可以简单轻松地设置临时环境、重新启动 Kubernetes 集群、重新部署镜像标签或创建微服务框架。平台工程团队将使这些操作在平台上可重用，而内部开发者门户将充当与平台的接口，并在软件目录中反映这些变化。

然而，内部开发者门户不仅仅是松散耦合的类产品用户界面，使开发者的工作更加轻松。内部开发者门户还具有宝贵的软件目录，其中包括您的工程中与应用程序相关的一切，从 CI/CD 元数据到云资源、Kubernetes、服务等等。

软件目录的价值远远超出了它所包含的元数据（这也非常有用），它远不止于显示谁拥有一个服务或其日志位于何处。除了作为唯一的真相来源外，它的价值还在于它提供的上下文，特别是在运行时数据的情况下。它可以快速回答诸如“在环境 y 中，服务 x 的当前运行版本是什么？”这样的问题，即使在包含功能标志、金丝雀或蓝/绿部署的情况下也可以如此。

本文将重点介绍上下文和运行时数据。我们将提供一个关于 Kubernetes 对象的内部开发者门户的详细示例。然后，我们将展示软件目录的威力，以及它如何支持工作流自动化——从时间到终止（TTL），到服务锁定，以及在服务降级时触发自动化操作等等——这是由于它的元数据和运行时数据的结合所带来的结果。

## Spotify 内部开发者门户 Backstage 的 C4 模型

软件目录需要一个数据模型，在开始之前，您需要定义它。这并不复杂，但您需要一个标识软件目录内部内容的模式。软件目录需要无倾向性且完全灵活，所以最好的选择是让您自己定义数据模型。

在 Port 中，某种实体（比如一个K8s集群）的模式被称为 [Blueprint](https://docs.getport.io/build-your-software-catalog/define-your-data-model/) 。实际的实体（在这种情况下就是实际的集群）被称为 entity 。在 Spotify 的 backstage 中， Blueprint 被称为 “kind” 。

Backstage 是一款领先的开源内部开发者门户，也是第三受欢迎的云原生计算基金会（CNCF）项目。他们建议使用一种包含六个 Blueprint（或 kind） 的特定数据模型。

* 组件（Component）
* API
* 资源（Resource）
* 系统（System）
* 领域（Domain）
* 组（Group）

正如 Spotify 的高级工程师 Renato Kalman 和技术工程师 Johan Wallin 在[这里](https://engineering.atspotify.com/2022/07/software-visualization-challenge-accepted/)解释的那样，在设计 Backstage 时，他们面临着一个软件可视化的挑战：他们需要一个“标准化的软件元数据模型，以创建一个用于沟通软件架构的共同语言”。他们提出的是 C4 模型。您可以在[这里](https://www.getport.io/blog/using-backstages-c4-model-adaptation-to-visualize-software-creating-a-software-catalog-in-port)看到 Backstage C4 模型的一个示例。

但是这个数据模型忽略了一个重点：即“running service” Blueprint（运行服务模型）。

## 什么是运行服务？

您的代码并不是您的应用程序。存在于您的代码库或容器镜像中的代码并不是应用程序本身。在现实生活中，您的应用程序存在于某个环境中，并在一系列工具和依赖项的生态系统中提供某种服务（API/其他服务/用户）。它的行为取决于它所处的环境。

"[running service" Blueprint](https://www.getport.io/blog/why-running-service-should-be-part-of-the-data-model-in-your-internal-developer-portal)，或者有时也称为“在环境中的服务”，反映了一个事实：单个“服务”通常部署在许多不同的环境中。服务可以存在于各种环境中，包括临时环境、开发环境和生产环境。特别是在单租户架构的情况下，服务还可以存在于许多不同的客户环境中。

服务存在于许多不同环境中这个简单事实在 Port 的“running service” Blueprint 中得到了体现。"running service" 实体使我们能够看到服务在“野外”中的情况——在实际存在的特定环境中。只有这样，我们才能获得正确和可操作的上下文，理解正在发生的事情。

坚持使用静态的软件目录和仅包含元数据而不包含运行时数据的静态数据模型并不能提供我们所需的上下文。只有查看运行中的微服务的真实实例时，才能获得洞察力。

## 一个 Kubernetes 内部开发者门户：运行服务 Blueprint

有人认为，Kubernetes 的增长是推动平台工程的核心因素之一。Kubernetes 的复杂性、其从业者所需的专业知识以及许多开发人员转向云原生开发的最近趋势，都增加了开发人员和 DevOps 之间的负担和摩擦。

[内部开发者门户为开发人员提供了对 Kubernetes 的抽象](https://thenewstack.io/developer-portals-can-abstract-away-kubernetes-complexity/)。它们通过显示相关数据来帮助开发人员理解 Kubernetes ，并支持开发人员自助操作。确保这些 Kubernetes 内部开发者平台包括以下内容非常重要：

* 在软件目录中包含所有的 Kubernetes 对象，而不仅仅是微服务
* 支持多集群
* 支持CRD（自定义资源定义）

让我们看看如何为 Kubernetes 内部开发者门户设置 blueprints（数据模型），以及何时以及如何将运行服务 Blueprint 包含在其中。

以下是 Kubernetes 的基本 blueprints（数据模型）：

![](https://cdn.thenewstack.io/media/2023/06/a09ba344-image3c.jpg)

![](https://cdn.thenewstack.io/media/2023/06/6874e3e8-image1c.jpg)

![](https://cdn.thenewstack.io/media/2023/06/e87c5fbb-image2c.jpg)

工作负载是 Kubernetes 中的“运行服务”。它是指在集群中运行的 stateful sets, deployments, daemon sets 和任何其他工作负载的通用名称。

集群代表基础设施中的一个 Kubernetes 集群，提供了 Kubernetes 集群中不同对象之间的高级连接。

* 节点是托管和提供 Kubernetes 集群中不同应用程序和微服务运行时的服务器。
* 命名空间旨在将同一个 Kubernetes 集群中的许多资源分组在一起，让您可以查看托管在同一个 Kubernetes 集群中的完整环境的连接方式。
* 工作负载旨在成为为开发人员提供关于其应用程序状态最相关上下文的焦点。工作负载实体向开发人员提供了关于其不同工作负载的抽象视图。开发人员可以查看工作负载的当前状态，例如实例数量和健康状况。通过向上追溯依赖树，开发人员可以查看与其自身工作负载并行运行的其他应用程序和微服务，从而了解是否存在连接或功能问题。
* Pod 是工作负载的一个实例，它使我们能够了解构成完整工作负载的部分的健康状况，并理解在工作负载提供的服务可用性方面是否存在特定问题。

## 您应该开始使用运行服务或工作负载 Blueprint。

我们已经看到，无论我们将其称为“运行服务”、“工作负载”或者字面上的“环境中的服务”，运行时 Blueprint都非常有用。它反映了一个单一服务通常同时存在于多个环境（如开发、暂存等）的现实情况。它还可以部署在许多不同的客户环境中。运行服务提供了运行时数据，使我们能够在环境和部署的上下文中理解服务，以及从正常运行时间到状态的实时信息。

您可以免费在 [getport.io](https://getport.io/) 上使用Port，或者在[此处](https://demo.getport.io/)查看一个完全填充的Port演示。