
<!--
title: 揭秘Kubernetes网络：顶级工程师实用指南
cover: https://cdn.sanity.io/images/rhzn5s2f/production/09c5cf6ab47ed35e6bb811568057d8bd1f2e2b94-1200x628.jpg?w=1230&fit=max&auto=format
-->

在现代[云原生](/kubernetes-glossary/cloud-native)生态系统中，Kubernetes 是容器编排的首选，它能够轻松管理和扩展容器化应用程序。从本质上讲，Kubernetes 可以看作是一个分布式系统，其中独立的[节点](/kubernetes-glossary/node)容器）组合在一起，为用户呈现一个统一、有凝聚力的环境。

> 译自 [Mastering Kubernetes Networking: The Ultimate Guide for Advanced Engineers](https://www.getambassador.io/blog/kubernetes-networking-guide-top-engineers)，作者 Prince Onyeanuna 是一位技术作家和 DevOps 工程师，他相信展示的力量。他热衷于通过写作和编码帮助他人学习和成长。。

然而，此类架构中出现的一个主要问题是网络。如何分配端口？容器如何相互通信？外部世界如何与容器通信？这些都是理解 Kubernetes 网络所必须要回答的问题。

让我们分解[Kubernetes 网络](/blog/emerging-trends-microservices-kubernetes)模型，并全面了解 Kubernetes 中的网络工作原理。您将了解 Kubernetes 中网络相关的四个主要问题领域，以及解决这些问题的常见策略。在本文的最后，您将具备像专业人士一样对 Kubernetes 中的网络问题进行故障排除所需的技能。

## 了解 Kubernetes 网络基础知识

前面强调的分布式系统中的端口分配问题，可以通过 [Kubernetes](/blog/kubernetes-tutorial-beginners-guide) 中的 Pod 概念来解决。

Pod 是 Kubernetes 中最小的可部署单元，表示应用程序的一个实例。每个 Pod 都有其唯一的 IP 地址，并且可以在同一集群中的其他 Pod 进行通信，而无需[网络地址转换 (NAT)](https://www.comptia.org/content/guides/what-is-network-address-translation)。这意味着每个 Pod 都可以在同一端口上侦听，而不会发生冲突。

Kubernetes 中通信的这种便利性归功于集群中的每个组件都连接到一个扁平网络。在扁平网络中，所有组件都可以相互通信，而无需任何硬件，例如路由器或交换机。这是通过 Kubernetes 网络模型实现的。

## Kubernetes 网络模型

在 Kubernetes 中，每个应用程序或服务都在[容器](/docs/telepresence/latest/reference/inside-container/)中运行。这些容器被分组到称为 Pod 的单元中，其中可以包含一个或多个容器作为单个实体协同工作。

Pod 能够相互交互，因为它们具有唯一的 IP 地址。这就是它们可以通过网络相互通信的原因。

但是，[Kubernetes](/blog/kubernetes-best-practices) 在多个节点（机器）上运行，并且 Pod 可以部署在其中任何一个节点上。这意味着 Pod 可能会在不同的节点上运行，并且它们需要一种方法来进行通信，而不管它们的位置如何。

为了促进这种通信，Kubernetes 采用了一种网络模型，确保 Pod 可以相互通信，无论它们在何处运行。这涉及在 Kubernetes 中使用[容器网络接口 (CNI)](https://www.tigera.io/learn/guides/kubernetes-networking/kubernetes-cni/)，它负责处理 Pod 之间的路由流量、负载平衡，并确保整个集群的无缝通信。

在每个节点上，Kubernetes 网络模型通过容器运行时和 CNI 插件的组合来实现。容器运行时为每个容器设置网络命名空间，而 CNI 插件配置网络规则和策略，以实现集群中 Pod 之间的通信。

## 容器网络接口 (CNI)

CNI 作为容器编排系统（例如 Kubernetes）中网络插件的标准接口规范。它概述了 Docker 或 containerd 等容器运行时如何与网络插件协作，为容器和 Pod 配置网络。

从本质上讲，[CNI](/blog/kubernetes-security-tools-risks-best-practices) 提供了一种标准化方法，用于容器运行时将网络责任移交给外部插件。这些插件处理诸如向容器分配 IP 地址、设置网络接口、定义路由和执行网络策略之类的任务。

在 Kubernetes 中，CNI 插件在促进 Pod 之间的通信和管理集群中的网络设置方面发挥着至关重要的作用。它们与底层网络基础设施无缝集成，以提供诸如覆盖网络、网络隔离、负载均衡和网络安全之类的功能。

在 Kubernetes 集群设置期间，通常会配置 CNI 插件，并自动与容器运行时和 Kubernetes 网络组件集成。Kubernetes 支持广泛的 CNI 插件，允许用户选择最符合其需求的网络解决方案。您可以在 [CNI GitHub 存储库](https://github.com/containernetworking/cni) 上浏览可用的 CNI 插件。

## Kubernetes 网络中的常见挑战

在 Kubernetes 中，主要有四个 (4) 个领域会出现与网络相关的问题。它们是：

### 1. Pod 到 Pod 的通信

此类通信涉及 Pod 在同一集群内相互通信的方式，无论是在同一节点还是在不同节点上。当一个 Pod 需要与另一个 Pod 通信时，就像它们在集群中来回发送消息一样。

有时，Pod 可能无法相互访问，这可能是由于各种原因造成的。例如，可能存在网络拥塞、网络策略配置错误，甚至托管集群的底层基础设施出现问题。

### 2. 容器到容器的通信

在 [Kubernetes](/resources/kubernetes-ingress) 中，Pod 中的一个容器需要与同一 Pod 中的另一个容器通信。与 Pod 到 Pod 的通信（其中 Pod 是独立实体）不同，容器到容器的通信发生在同一 Pod 中，因此它们就像共享空间中的邻居一样。

现在，为什么同一 Pod 中的容器需要通信？好吧，它们可能是同一应用程序的一部分，每个容器处理不同的方面，例如 Web 服务器容器与数据库容器通信以获取数据。

但是，就像 Pod 到 Pod 的通信一样，这里也可能出现问题。一个容器可能无法访问另一个容器，或者通信存在延迟。这可能是由于网络设置配置错误、防火墙规则阻止通信，甚至应用程序本身存在问题。容器之间可以通信，因为它们共享相同的网络命名空间，这意味着它们可以通过本地主机接口进行通信。

### 3. Pod 到服务的通信

在 Kubernetes 中，[服务](https://cloud.google.com/kubernetes-engine/docs/concepts/service#:~:text=applications%20using%20services.-,What%20is%20a%20Kubernetes%20Service%3F,contact%20Pods%20in%20the%20Service) 作为一种一致且抽象的方式来访问一组 Pod。可以将其视为一个稳定的端点，它代表一个或多个 Pod，为客户端提供了一种连接到这些 Pod 中运行的应用程序的方法。

当 Pod 需要与服务通信时，就像向中央集线器发送消息一样，然后该集线器将消息路由到适当的目标。这是可能的，因为服务有其唯一的 IP 地址和 DNS 名称，这使它们可以轻松地被发现和通信。

在幕后，Kubernetes 使用网络路由和负载均衡将流量从 Pod 路由到与服务关联的适当后端 Pod。这确保了发送到服务中的请求在 Pod 中均匀分布，从而提供了高可用性和可扩展性。

但是，Pod 到服务的通信中仍然可能出现问题。例如，服务定义、网络策略或防火墙规则配置错误可能会阻止 Pod 访问服务。

对此类问题的故障排除可能涉及检查服务配置、检查网络策略或检查防火墙规则，以确保 Pod 和服务之间的通信顺畅。

### 4. 外部到服务的通信

当我们在 Kubernetes 中讨论外部到服务的通信时，我们指的是集群内运行的服务与集群外部的客户端或应用程序之间的交互。这些外部实体可能是访问 Web 应用程序的用户、其他集群中的其他服务，甚至是在 Kubernetes 环境之外运行的应用程序。

有几种方法可以促进与 Kubernetes 集群的外部通信。它们包括：

- **NodePort**：此方法在集群中每个节点上的静态端口上公开服务。外部客户端可以通过访问任何节点的 IP 地址和分配的静态端口来访问服务。[NodePort](/blog/kubernetes-ingress-controllers-nodeport-load-balancers)简单易行，但由于安全问题和端口范围限制，可能不适合生产环境。
- **负载均衡器**：Kubernetes 与云提供商集成，以配置[负载均衡器](/docs/edge-stack/latest/topics/running/load-balancer/)，该负载均衡器在运行服务的多个节点之间分配流量。此方法适用于生产环境，并提供可扩展性、高可用性和自动故障转移。但是，它具有云特定性，并且可能产生额外费用。
- **Ingress**：Ingress 是一个 API 对象，用于管理集群内服务的外部访问。它充当流量控制器，根据已定义的规则将传入请求路由到适当的服务。Ingress 提供比 NodePort 或 LoadBalancer 更高级的功能，例如基于路径的路由、SSL 终止和基于名称的虚拟主机。它是管理 Kubernetes 中外部流量的热门选择。
- **ExternalDNS**： [ExternalDNS](/docs/edge-stack/latest/howtos/external-dns/)根据指定的注释自动配置 Kubernetes 资源（例如服务）的 DNS 记录。它使外部客户端能够使用自定义域名而不是 IP 地址访问服务，从而简化了服务发现和管理。
- **服务网格**： [服务网格](/blog/service-mesh)技术（例如 Istio）促进了 Kubernetes 集群内[微服务](/blog/service-discovery-microservices)以及跨集群服务之间的通信。它们提供流量管理、负载均衡、加密和可观察性等功能，从而增强了复杂微服务架构中的安全性、可靠性和性能。
- **ClusterIP**：这是 Kubernetes 中的默认服务类型，它在集群内的内部 IP 地址上公开服务。虽然无法从集群外部直接访问它，但外部客户端仍可以通过代理访问该服务。

尽管有这些选项，外部到服务通信中仍然会出现问题。例如，配置错误的负载均衡器、DNS 解析问题或网络路由问题可能会中断对服务的外部访问。对这些问题进行故障排除可能涉及检查负载均衡器配置、验证 DNS 记录或分析网络流量以识别和解决连接问题。

## 故障排除 Kubernetes 网络问题

在 Kubernetes 中对网络问题进行故障排除时，可以使用多种工具和技术来诊断和解决问题。以下是用于调试 Kubernetes 中网络问题的实用故障排除技术：

**1. kubectl exec**：此命令允许你在正在运行的容器内执行命令。你可以使用它来检查网络配置、检查网络接口并在容器内验证网络连接。

例如，你可以运行 kubectl exec 在容器中打开一个 shell，然后使用像 ping 或 netstat 这样标准的网络故障排除工具诊断网络问题。

`kubectl exec` 的典型用法如下：

```
kubectl exec -it <pod-name> -- /bin/bash
```

**2. kubectl logs**：此命令允许你检索在 Pod 内运行的容器的日志。你可以使用它来检查与网络相关的日志，例如连接错误、DNS 解析问题或网络超时。

例如，您可以运行 kubectl 日志以检索容器中的日志，然后搜索与网络相关的消息以识别潜在问题。

kubectl logs 的典型用法如下：

```
kubectl logs <pod-name> -c <container-name>
```

**3. 第三方工具**：一些第三方工具可用于对 Kubernetes 中的网络问题进行故障排除。一个名为 [Ksniff](https://github.com/eldadru/ksniff) 的流行工具是一个网络数据包捕获工具，它允许你捕获和分析 Kubernetes 集群中 Pod 之间的网络流量。

它提供了对网络通信、延迟和数据包丢失的见解，帮助你识别和解决网络问题。尽管不适用于生产环境，但 Ksniff 是用于调试和故障排除 Kubernetes 中网络问题的宝贵工具。

## 结论

Kubernetes 网络有时会令人费解，尤其是在你处理复杂的微服务架构和分布式系统时。但是，通过深入了解 Kubernetes 网络基础知识、常见挑战和实用的故障排除技术，你可以像专业人士一样驾驭 Kubernetes 中网络的复杂性。

当您遇到与网络相关的问题时，您应该记住从 Pod 到容器的通信是如何工作的，以及外部通信是如何实现的。有了这些知识，您可以利用 kubectl exec、kubectl logs 和第三方调试工具，来有效诊断和解决网络问题。