<!-- 
title: Kubernetes 网络模型综合指南
cover: https://kubeops.net/images/Blog%20pictures/Networking%20Models_ic-high-level_ingress%20egress.png
 -->

这篇详细的博文探讨了 Kubernetes 网络的复杂性，提供了关于如何在容器化环境中确保高效和安全通信的见解。

译自 [Navigating the Network: A Comprehensive Guide to Kubernetes Networking Models](https://kubeops.net/blog/navigating-the-network-a-comprehensive-guide-to-kubernetes-networking-models) 。

## 介绍

在 Kubernetes 的世界中，网络是一个基本方面，它编排着集群内外各种组件之间的通信。理解 Kubernetes 网络模型对于任何使用这个编排工具的人来说都是至关重要的。

这篇详细的博文探讨了 Kubernetes 网络的复杂性，提供了关于如何在容器化环境中确保高效和安全通信的见解。

## 理解 Kubernetes 网络

Kubernetes 网络被设计来满足四个关键要求，每个要求在 Kubernetes 集群的功能和操作中都扮演着至关重要的角色。

**容器与容器之间的通信**：这是 Kubernetes 网络的基本层。它实现了同一个 Pod 内容器之间的直接通信。这些容器共享相同的网络命名空间，意味着它们可以使用 localhost 互相通信。对于涉及多容器 Pod 的应用程序而言，这种设置对于需要密切高效地交互的容器至关重要。

**Pod-to-Pod 通讯**: 在 Kubernetes 中，每个 Pod 都被分配了一个唯一的 IP 地址。这种设计选择简化了启用 Pod 之间通信的过程，无论它们位于哪个节点上。Pod 之间可以直接通信，无需进行网络地址转换（NAT），确保了直接且简单的连接。这种模型是创建分布式系统的基础，其中每个 Pod 都可以作为独立的微服务运行。

**Pod-to-Service 通讯**: Kubernetes 服务是一个关键的抽象，为 Pod 访问其他 Pod 提供了一种一致可靠的方式。服务本质上是一组变化的 Pod 的稳定地址。它确保任何发送到服务的请求都会自动智能地路由到正确的 Pod，即使 Pod 被创建、销毁或更新。这种抽象层对于维护一个具有弹性和可扩展性的系统至关重要。

**External-to-Internal 通讯**: Kubernetes 网络的这一方面涉及管理来自集群外部到集群内部服务的入站流量。通过 Ingress 控制器和负载均衡器等机制来处理。这些工具允许外部用户和应用程序安全高效地访问运行在集群内部的服务。它们在将应用程序暴露给最终用户和其他外部系统方面发挥着至关重要的作用。

## 服务和负载均衡

Kubernetes 中的服务对于为一组可能随时间动态变化的 Pod 提供稳定的地址至关重要。它们在管理访问运行在 Pod 上的应用程序方面起着至关重要的作用。让我们深入了解不同类型的服务及其在负载均衡中的作用：

**ClusterIP**：这是 Kubernetes 的默认服务。ClusterIP 服务分配一个唯一的内部 IP 地址，用于与服务进行通信。这些服务只能在集群内部访问，对于集群中的 Pod 之间的内部通信非常有用。这在不需要外部访问服务的场景中非常理想。

**NodePort**：NodePort 服务扩展了 ClusterIP 的功能。除了内部 IP 外，NodePort 服务还在所有集群节点上提供了一个特定的端口。外部流量可以访问这些暴露的端口上的服务，然后将流量路由到相应的内部 IP。当您需要外部流量跨所有节点访问特定端口时，这尤其有用。

**LoadBalancer**：在 NodePort 的基础上，LoadBalancer 服务与云服务提供商的负载均衡器集成。这种类型会自动创建一个外部负载均衡器，将外部流量引导到整个集群节点上的 NodePort，然后再路由到正确的 Pod 上。它简化了将服务暴露到互联网的过程，特别适用于分发传入的网络流量，从而提高了应用程序的可扩展性和可靠性。

**ExternalName**: 与其他类型不同，ExternalName 服务不会将流量路由到 Pod。相反，它们充当别名，通过返回一个 CNAME 记录到一个外部服务。当您想要使用 DNS 将 Kubernetes 集群中的服务与外部服务集成时，这是非常有用的。

## 网络安全的网络策略

Kubernetes 中的网络策略提供了一个重要的安全层，规定了 Pod 之间以及与其他网络端点之间的通信方式。它们充当了 Pod 的防火墙，允许用户根据标签选择器和 CIDR 块指定入站和出站规则。

例如，考虑这样一个情景：您有一个前端和一个后端服务。后端服务不应该从集群外部访问，但应该允许来自前端服务的流量。您可以使用类似以下内容的网络策略来实现：

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: kubeops-frontend
    ports:
    - protocol: TCP
      port: 80
```

这个策略确保只有带有标签 app: kubeops-frontend 的 Pod 可以访问 TCP 端口 80 上的后端 Pod。这种细粒度的控制有助于在 Kubernetes 中维护一个安全且受控的网络环境。

考虑默认行为也是至关重要的。默认情况下，Kubernetes 集群中的所有 Pod 都可以彼此通信。应用网络策略可以改变这种默认行为。例如，应用允许特定流量的策略意味着所有不符合该策略的其他流量都将被拒绝。

## Ingress 和 Egress 控制器

![](https://kubeops.net/images/Blog%20pictures/Networking%20Models_ic-high-level_ingress%20egress.png)

Kubernetes 中的入口和出口控制器管理集群内部服务的外部访问，通常是 HTTP。入口控制器促进将外部流量路由到正确的内部资源，而出口控制器则管理集群的出站流量。

入口控制器负责读取入口资源信息并适当地处理它。例如，当用户请求 URL 时，入口控制器根据入口资源中定义的路由规则将请求路由到适当的服务。这对于管理对微服务的访问和实现 SSL/TLS 终止特别有用。

另一方面，出口控制器处理出站流量。它们确保来自集群内部到外部世界的请求被正确管理和路由。出口控制器可以强制执行限制 Pod 可以建立连接的目的地的策略，增强了集群的整体安全性。

实现这些控制器需要对网络架构和应用程序的流量模式有清晰的理解。例如，一个配置良好的入口控制器可以高效地处理流量突增，根据 URL 路径进行路由，并提供基于名称的虚拟主机。

## 核心网络解决方案：重要性与作用

**Calico 用于网络策略执行**：以其强大的网络策略执行而闻名，Calico 在维护应用程序安全方面发挥着关键作用。它对 Pod 通信提供了精细的控制，仅允许授权的流量，从而执行安全策略并分段网络流量以防止未经授权的访问。其重要性在于增强了应用程序内部网络交互的整体安全性和完整性。

**Flannel 用于简单的覆盖网络**：Flannel 以其在设置覆盖网络方面的简单性和效率而至关重要，连接跨节点的 Pod。它的作用是通过自动管理子网分配来简化 Kubernetes 部署中的网络配置。这减少了与网络管理相关的复杂性和运营开销，使其成为直接但有效的网络连接的有价值工具。

**Cilium 用于 API 感知网络**：Cilium 对于将 API 感知的网络安全过滤引入 Kubernetes 至关重要。利用 BPF，在内核级别过滤网络流量，理解 Kubernetes 标签和元数据。它的作用在于增强安全性，并为网络流量提供改进的可见性，特别是对于微服务，从而促进更安全、更透明的网络环境。

**Canal 作为 Flannel 和 Calico 的组合**：Canal 合并了 Flannel 和 Calico 的优点，为 Kubernetes 提供了全面的网络解决方案。它的作用是提供易用性（来自 Flannel）和强大的安全功能（来自 Calico）。这种组合使得 Canal 成为一个多功能的选择，满足了对高效网络覆盖和灵活网络策略的需求。

**Kube-router 作为轻量级解决方案**：Kube-router 是标准网络解决方案的简化、更高效的替代方案。它的作用是通过单个守护程序处理路由、网络策略和服务代理功能。这使其成为较小或资源受限环境的理想选择，提供了轻量级但有效的网络解决方案。

![](https://kubeops.net/images/Blog%20pictures/Networking%20Models_Core%20Solutions.png)

## Kubernetes 网络的最佳实践

1. **利用网络策略控制流量流向**：网络策略对于保护 Kubernetes 环境至关重要。它们充当 Pod 的防火墙，允许您定义哪些 Pod 可以彼此通信。例如，您可以限制数据库 Pod，使其只能被特定应用程序 Pod 访问，增强数据的安全性和完整性。

2. **实现服务网格以处理复杂通信**：在微服务架构中，像 Istio 或 Linkerd 这样的服务网格提供了额外的通信控制、可观察性和可靠性层。例如，您可以通过服务网格管理负载均衡、服务间身份验证，并监控服务间通信，从而更容易调试和优化您的应用程序。

3. **优化负载均衡策略**：负载均衡对于平均分配流量到各个 Pod 至关重要。您可以使用轮询策略，其中请求按顺序分配，或者更高级的方法，如 IP 哈希，确保用户的会话始终由相同的 Pod 服务。这确保了资源的有效利用和用户体验的改进。

4. **启用 DNS 进行服务发现**：Kubernetes DNS 服务在服务发现中起着关键作用。它允许 Pod 通过名称定位其他 Pod 和服务，而不是依赖于可能变化的 IP 地址。例如，一个应用程序可以通过其 DNS 名称轻松定位到数据库服务，简化配置和服务间通信。

5. **利用 Ingress 控制器进行外部访问**：当将您的服务暴露给外部世界时，Ingress 控制器是比 NodePort 或 LoadBalancer 服务更高级和灵活的选项。它们提供 HTTP/HTTPS 路由、SSL 终止和基于名称的虚拟主机。这意味着您可以通过精细的控制高效管理对服务的外部访问。

6. **监控和记录网络活动**：持续监控和记录网络流量对于诊断问题和确保安全至关重要。像 Prometheus 监控和 Fluentd 记录这样的工具提供了对您的网络性能和安全性的洞察。它们帮助您发现异常、了解流量模式，并就扩展和优化做出明智决策。

7. **采用 IPv6 网络以实现可扩展性**：随着 Kubernetes 集群规模的增长，IPv6 网络变得越来越重要。它提供了更大的地址空间，消除了复杂的 NAT 设置的需要。过渡到 IPv6 可以未雨绸缪，确保您有足够的 IP 地址用于所有的 Pod 和服务。

## 结论

Kubernetes 网络是支持容器化应用动态和分布式特性的关键因素。通过理解其模型，并有效地实施网络策略和服务，您可以确保为 Kubernetes 集群建立一个稳健、安全和高效的环境。
