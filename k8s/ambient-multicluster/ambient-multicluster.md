
<!--
title: Ambient模式多集群支持（Alpha版）
cover: https://raw.githubusercontent.com/istio/istio.io/master/static/img/istio-social.png
summary: Ambient 多集群功能已进入 Alpha 状态，旨在简化多集群架构的复杂性。关键组件包括东西向网关、双重 HBONE 和 ServiceScope API。当前实现存在一些限制，例如服务配置一致性、L7 故障转移等问题。
-->

Ambient 多集群功能已进入 Alpha 状态，旨在简化多集群架构的复杂性。关键组件包括东西向网关、双重 HBONE 和 ServiceScope API。当前实现存在一些限制，例如服务配置一致性、L7 故障转移等问题。

> 译自：[Introducing multicluster support for ambient mode (alpha)](https://istio.io/latest/blog/2025/ambient-multicluster/)
> 
> 作者：Jackie Maertens (Microsoft), Keith Mattix (Microsoft), Mikhail Krinkin (Microsoft), Steven Jin (Microsoft)

多集群一直是 Ambient 最受期待的功能之一——并且从 Istio 1.27 开始，它已进入 Alpha 状态！
我们力求在利用 Ambient 用户喜爱的相同模块化设计的同时，捕捉多集群架构的优势并避免其复杂性。
此版本带来了多集群网格的核心功能，并为即将发布的版本中更丰富的功能集奠定了基础。

## 多集群的强大功能与复杂性

多集群架构可提高中断恢复能力、缩小故障半径，并跨数据中心进行扩展。
也就是说，集成多个集群会带来连接性、安全性和运营方面的挑战。

在单个 Kubernetes 集群中，每个 Pod 都可以通过唯一的 Pod IP 或服务 VIP 直接连接到另一个 Pod。
这些保证在多集群架构中会失效；
不同集群的 IP 地址空间可能会重叠，
即使没有重叠，底层基础设施也需要配置才能路由跨集群流量。

跨集群连接也带来了安全挑战。
Pod 到 Pod 的流量将离开集群边界，并且 Pod 将接受来自其集群外部的连接。
如果没有在集群边缘进行身份验证和强大的加密，
外部攻击者可能会利用易受攻击的 Pod 或拦截未加密的流量。

多集群解决方案必须安全地连接集群，并且通过简单、声明式的 API 来实现，以适应集群频繁添加和删除的动态环境。

## 关键组件

Ambient 多集群使用新的组件和最少的 API 扩展了 Ambient，以
使用 Ambient 轻量级的模块化架构安全地连接集群。
它建立在命名空间一致性模型之上，
因此服务在集群之间保持其现有的 DNS 名称，允许您在不更改应用程序代码的情况下控制跨集群通信。

命名空间一致性

在多集群网格中，[命名空间一致性](https://github.com/kubernetes/community/blob/master/sig-multicluster/namespace-sameness-position-statement.md)
适用，并且具有给定名称的所有命名空间都被认为是相同的命名空间。 如果多个集群包含一个具有相同命名空间名称的
`Service`，它们将被识别为单个组合服务。 默认情况下，流量会
在网格中所有集群的给定服务之间进行负载均衡。

在*数量*上匹配的端口也必须具有相同的端口*名称*才能被视为组合的“服务端口”。

### 东西向网关

每个集群都有一个东西向网关，它具有全局可路由的 IP，充当跨集群通信的入口点。
ztunnel 连接到远程集群的东西向网关，通过其命名空间名称识别目标服务。
然后，东西向网关将连接负载均衡到本地 Pod。
使用东西向网关的可路由 IP 无需集群间路由配置，
并且通过命名空间名称而不是 IP 来寻址 Pod 可以消除 IP 空间重叠的问题。
总之，这些设计选择可以在不更改集群网络或重启工作负载的情况下实现跨集群连接，
即使在添加或删除集群时也是如此。

### 双重 HBONE

Ambient 多集群使用嵌套的 [HBONE](https://istio.io/latest/docs/ambient/architecture/hbone/) 连接来有效地保护跨集群边界传输的流量。
外部 HBONE 连接加密到东西向网关的流量，并允许源 ztunnel 和东西向网关验证彼此的身份。
内部 HBONE 连接对流量进行端到端加密，这允许源 ztunnel 和目标 ztunnel 验证彼此的身份。
同时，HBONE 层允许 ztunnel 有效地重用跨集群连接，从而最大限度地减少 TLS 握手。

[![Istio ambient multicluster traffic flow](https://istio.io/latest/blog/2025/ambient-multicluster/mc-ambient-traffic-flow.png)](https://istio.io/latest/blog/2025/ambient-multicluster/mc-ambient-traffic-flow.png "Istio ambient multicluster traffic flow")

Istio ambient 多集群流量

### 服务发现和范围

将服务标记为全局服务可以启用跨集群通信。
Istiod 配置东西向网关以接受全局服务流量并将其路由到本地 Pod，并
对 ztunnel 进行编程，以将全局服务流量负载均衡到远程集群。

网格管理员通过 `ServiceScope` API 定义全局服务的基于标签的标准，
应用程序开发人员相应地标记他们的服务。
默认的 `ServiceScope` 是

这意味着任何带有 `istio.io/global=true` 标签的服务都是全局的。
尽管默认值很简单，但 `ServiceScope` API 可以使用 AND 和 OR 的组合来表达复杂的条件。

默认情况下，ztunnel 在所有端点（甚至是远程端点）上均匀地对流量进行负载均衡——
但可以通过服务的 `trafficDistribution` 字段进行配置，以便仅在没有本地端点时才跨越集群边界。
因此，用户可以控制流量是否以及何时跨越集群边界，而无需更改应用程序代码。

## 限制和路线图

尽管当前 Ambient 多集群的实现具有多集群解决方案的基本功能，
但仍有许多工作要做。
我们希望改进以下领域

* 服务和航路点配置必须在所有集群中保持一致。
* 没有跨集群 L7 故障转移（L7 策略在目标集群中应用）。
* 不支持直接 Pod 寻址或无头服务。
* 仅支持多主部署模型。
* 每个集群部署模型仅支持一个网络。

我们还希望改进我们的参考文档、指南、测试和性能。

如果您想尝试使用 Ambient 多集群，请按照[本指南](https://istio.io/latest/docs/ambient/install/multicluster/)进行操作。
请记住，此功能处于 Alpha 状态，尚未准备好用于生产环境。
我们欢迎您提供错误报告、想法、评论和用例——您可以在 [GitHub](https://github.com/istio/istio) 或 [Slack](https://istio.slack.com/) 上与我们联系。
