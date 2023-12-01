<!--
title: Cilium双向认证可能带来安全隐患
cover: https://cdn.thenewstack.io/media/2023/11/de3dd6d2-mutual-authentication-1024x683.jpg
-->

Kubernetes工作负载采用的新双向认证机制存在最终一致性问题，这可能带来安全隐患。

> 译自 [How Cilium’s Mutual Authentication Can Compromise Security](https://thenewstack.io/how-ciliums-mutual-authentication-can-compromise-security/)，作者 Christian Posta 是 Solo.io 的全球首席技术官，支持客户和最终用户采用云原生技术。他是 Manning 和 O'Reilly 出版社的作者，开源贡献者，博客和 Envoy Proxy 极富盛名的演讲者，以及......

最近，Cilium 项目宣布了对[一种新的互认机制的支持](https://docs.cilium.io/en/latest/network/servicemesh/mutual-authentication/mutual-authentication/)，这种机制可以通过一个简单的配置标志透明地部署到应用程序中。乍一看，这似乎是一种简单的方法，可以为使用 Cilium 的 [Kubernetes](https://thenewstack.io/kubernetes/) 工作负载提供服务间的双向认证。然而，该设计存在一个不应被忽略的严重缺陷:

Cilium 中的整个双向认证基础最终是一致的。

安全实现的数据路径中的最终一致性可能会导致安全属性的故障，并在应被禁止的情况下导致流量在服务之间继续。

## Cilium 双向认证的工作方式

Cilium 的自定义双向认证机制透明地对服务之间的流量进行认证，并基于 Cilium 现有的扩展伯克利数据包过滤器([eBPF](https://thenewstack.io/ebpf-offers-a-new-way-to-secure-cloud-native-systems/))数据平面。Cilium 使用 eBPF 来实现服务网络、网络策略和连接处理等功能。

Cilium 使用“无 TLS 的互认”(或 mTLess)来认证一个服务。我称之为“较少”，因为它没有使用 TLS 来完成 TLS 设计的目的：对两个对等体之间的传输进行认证、加密和完整性检查。Cilium 的双向认证实现与 mTLS 不同，正如我将在下面解释的那样。

当服务(或 Pod)A 想要与服务(或 Pod)B 通信时，Cilium 会尝试对这两个对等体进行认证，然后在一个特殊的节点本地“认证缓存”中标记该特定流量是否被允许。

![](https://cdn.thenewstack.io/media/2023/11/62c230c4-initial-connection-dropped_1.png)

*图 1:初始连接将被丢弃，因为它未经认证。*

当 Pod A 想要与 Pod B 通信时，它会通过正常的 Cilium eBPF 数据平面，但是 eBPF 代码将检查此连接是否已经通过检查节点本地认证缓存来进行了认证。在第一次尝试时，调用将不会被认证，所以 Cilium 将丢弃数据包。但这将触发后台机制，试图认证 Pod A 和 Pod B 之间的流量。如果成功，它将更新节点本地认证缓存。

期望的是，足够快的后台认证 Pod A 调用 Pod B 的机制，最初被丢弃的数据包将被重试，而不会造成太大的延迟。后台使用的机制是运行在不同节点上代表两个特定服务身份的 cilium-agent 之间的“无 TLS”连接(用 Go 编写)。所有这些都不会发生在 eBPF 数据平面上，而是在用户空间 Cilium 代理中。

![](https://cdn.thenewstack.io/media/2023/11/62c230c4-initial-connection-dropped_1.png)

*图 2:如果 cilium-agent 之间成功建立了表示两个特定服务身份的 mTLS 连接，则流量被认为是经过认证的。*

我将这个连接称为“无 TLS”，因为它用于测试认证并立即关闭，协商的所有会话密钥用于加密和完整性也被丢弃。也就是说，Cilium 不会在连接的整个生命周期内保留 mTLS 的安全属性；它只使用握手的认证部分。

![](https://cdn.thenewstack.io/media/2023/11/991c4115-lacky-connection-ends_3.png)

*图 3:握手之后，Cilium 结束无 TLS 连接。*

如果这个无 TLS 连接成功(即握手成功)，Cilium 将认为从 Pod A 到 Pod B 的流量是“经过认证的”。此时，节点本地认证缓存中的条目将被更新，以指示应允许从 Pod A 到 Pod B 的流量。

![](https://cdn.thenewstack.io/media/2023/11/792b9e31-auth-cache-updated_4.png)

*图 4:Cilium 更新认证缓存以指示 Pod A 经过认证可以调用 Pod B。*

现在，当它重试连接数据包时，认证缓存将指示流量已认证，应允许连接并继续剩余的 eBPF 数据平面(实施网络和其他策略)。这个节点本地认证缓存确实展示了最终一致性的迹象，可能会失步，但这不是最令人担忧的最终一致性属性。

![](https://cdn.thenewstack.io/media/2023/11/cbc146ff-connection-flows_5.png)

*图 5:一旦缓存已更新并重试数据包，连接将流动。*

## Cilium 方法的大问题

使用真正的 mTLS 连接，在成功握手后，您希望剩余的数据使用参与方之间协商的密钥(仅为参与方所知)进行加密。Cilium 中的一个流量的成功认证并不意味着它是加密的(它将是纯文本)，也不保证流量将以只对相关方可见的方式加密。如果您想要加密，可以使用基于 WireGuard 的 Cilium 加密选项(或 IPSec)，但这仅仅是两个 Kubernetes 节点之间的加密，而不是特定的经过认证的工作负载。在“无 TLS”连接检查和实际将敏感数据投入线路之间可能会发生很多事情。

如果这个无 TLS 连接成功(即握手成功)，Cilium 将认为从 Pod A 到 Pod B 的流量是“经过认证的”。此时，节点本地认证缓存中的条目将被更新，以指示应允许从 Pod A 到 Pod B 的流量。

![](https://cdn.thenewstack.io/media/2023/11/8aacad10-different-session-keys_6.png)

*图6:流量使用在 A/B 和 B/C 之间不同的会话密钥进行加密。*

![](https://cdn.thenewstack.io/media/2023/11/ea61c30c-wireguard-encrypted_7.png)

*图7:基于 WireGuard 的加密使用相同的密钥。*

Cilium 最终一致的双向认证实现中的实际问题出现在 Cilium 的核心身份模型周围。在上述 TLS 握手中，我略过了细节，但是如果您阅读 Cilium 文档，您会看到用于“mTLess”的 X509 证书有一个可选的基于“面向所有人的安全生产身份框架([SPIFFE](https://thenewstack.io/the-rise-of-workload-identity-in-cloud-native-with-spiffe-spire/))”的身份模型。事实上，在部署实现 Cilium 双向认证所必需的组件时，您可以选择部署 SPIFFE 运行时环境(SPIRE)，这是 Cilium 用来生成代表工作负载及其身份的证书的 SPIFFE 实现。

这个 SPIFFE 身份用于握手中使用的证书，但 SPIFFE 不是 Cilium 中用于构建的通用工作负载身份。SPIFFE 被用作一个独立的身份层，映射到 Cilium 现有的身份实现。Cilium 基于其 CiliumIdentity 概念构建所有网络策略。CiliumIdentity 实现将一个整数映射到一组 IP 地址(与一组 Pod 相关联的 Pod IP)。这个“整数”及其映射到 Pod IP 地址表示 Cilium 中的核心身份基元。

![](https://cdn.thenewstack.io/media/2023/11/ae733df8-core-identity-integers_8.png)

*图8:Cilium 的核心身份基元基于整数，这些整数在每个节点上的本地缓存中映射到 IP 地址。*

我们在我们的博客文章“[基于网络缓存的身份可能会被误解](https://www.solo.io/blog/could-network-cache-based-identity-be-mistaken/)？”中详细讨论了这个话题。由于这个问题，我们建议在考虑使用容器网络接口(CNI)和服务网格的网络安全时采用深度防御的姿态。

下面是问题的关键:

给定身份的所有 IP 的映射，对于集群中存在的每个身份，都存在于集群中每个节点上的本地缓存中。

![](https://cdn.thenewstack.io/media/2023/11/e57a167b-ips-in-separate-cache_9.png)

*图9:集群中每个身份的所有 IP，对于集群中的每个身份，都存在于每个节点上的单独缓存中。*

![](https://cdn.thenewstack.io/media/2023/11/8c87d70a-eventual-consistency_10.png)

*图10:最终一致性可能会导致错误或过时的 IP 映射。*

为了 Cilium 的双向认证和策略执行能够工作，这些缓存必须使用正确的 IP 到身份映射进行更新。然而，更新集群中所有节点上的单独缓存是一个最终一致的操作。当 Cilium 的 eBPF 数据平面尝试推断连接的策略时，它将参考其节点本地缓存中的 IP 到身份映射。如果该缓存过时或延迟，它将导致不正确的网络策略(这可能不合规，允许恶意活动，危及数据等)。无论您是否使用 WireGuard 或 IPSec 在节点之间加密流量，对于这个身份混淆场景来说都没有区别。

这个演示展示了在使用 Cilium 的双向认证时可能发生的违反网络策略的流量身份混淆: [视频](https://youtu.be/RpvkxfiwYFI)。

## 总结

所以总结一下:

- Cilium 项目为 Kubernetes 工作负载引入了一种新的双向认证机制。
- Cilium 中的双向认证建立在最终一致性之上，这可能会危及安全性。
- Cilium 使用“mTLess”进行认证，但并没有对整个连接进行加密。
- Cilium 的身份模型包括 SPIFFE，但其核心身份是基于整数的独立身份层。
- 核心问题是 IP 到身份映射存储在每个节点上的本地缓存中，这可能导致最终一致的更新。
- Cilium 的双向认证中的最终一致性可能会导致不正确的网络策略和安全漏洞。

要正确使用依赖于 IP 地址映射的身份的 CNI，请考虑在顶部分层服务网格(如 Istio Ambient)的深度防御姿态。Istio Ambient 实现了一个无 sidecar 的服务网格，在服务之间的数据路径上使用 mTLS(无论其 IP 地址如何)。在[像 Istio 这样的服务网格](https://thenewstack.io/solo-io-istio-is-winning-the-service-mesh-war/)中，身份模型使用 SPIFFE 定义，并植根于负责签署用于认证流量的证书的证书颁发机构。

