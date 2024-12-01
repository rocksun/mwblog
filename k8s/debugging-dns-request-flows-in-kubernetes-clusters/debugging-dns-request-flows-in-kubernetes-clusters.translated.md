这篇博客将介绍用于调试 Kubernetes 集群中 DNS 请求流的工具。我们还将介绍不同的调试场景以及如何修复每个场景。

这篇博客基于 Qasim Sarfraz 在 ContainerDays 2024 上的演讲。您可以在 Youtube 上观看完整版：[Demystifying DNS: A Guide to Understanding and Debugging Request Flows in Kubernetes Clusters](https://www.youtube.com/watch?v=KQpZg_NqbZw)。

以下主题将涵盖：

- 理解 DNS 组件和请求流
- DNS 调试的挑战
- DNS 调试工具
- CoreDNS 日志插件
- Hubble
- Inspektor Gadget
- 调试场景

## 理解 DNS 组件和请求流

为了有效地调试 Kubernetes 集群中的 DNS 问题，了解 DNS 架构和请求流至关重要。集群中 DNS 请求涉及的典型组件包括：

- 应用 Pod
- 节点本地 DNS（可选）
- CoreDNS 服务和 Pod
- 上游 DNS 服务器

DNS 请求过程从应用 Pod 开始。从那里，请求可能会通过像 NodeLocal DNS 这样的缓存层，然后再到达 Kubernetes 中的 CoreDNS。如果请求的域名是外部域名，则 CoreDNS 将请求转发到上游 DNS 服务器。

## DNS 调试的挑战

由于隐藏的系统和整个集群的可见性有限，Kubernetes 中的 DNS 调试可能很复杂。像 [tcpdump](https://www.tcpdump.org/) 这样的传统工具可以提供对请求流的洞察，但它们缺乏集群范围的聚合和 Kubernetes 特定的上下文，因此难以跨多个节点跟踪 DNS 请求。

## 深入研究请求流的工具

有几种工具可用于有效地跟踪 Kubernetes 中的 DNS 请求流。

## CoreDNS 日志插件

[CoreDNS 日志插件](https://coredns.io/plugins/log/) 是内置的，需要最少的设置，并直接从 CoreDNS 记录 DNS 事务。它允许按域名和响应类别进行过滤，提供有关客户端 IP、查询 ID、响应代码和响应持续时间的信息。

这是一个示例输出：

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-1.png)

## Hubble

[Hubble](https://github.com/cilium/hubble) 为 Kubernetes 提供网络、服务和安全可观察性。它构建在 Cilium 和 eBPF 之上，并通过其 CLI 提供流检查功能，允许用户跨集群跟踪 DNS 请求。

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-2.png)

#### 如何使用 Hubble CLI 进行流检查：

在使用 Hubble 跟踪 DNS 请求流之前，您需要准备您的设置：

**步骤 1**: 安装具有第 7 层 (L7) 代理支持的 Cilium。按照 [Cilium 的官方文档](https://docs.cilium.io/en/stable/network/servicemesh/l7-traffic-management/) 在安装过程中启用 L7 代理支持。

**步骤 2**: 创建 Cilium 网络策略以启用 `mypod` 和 CoreDNS 的 DNS 流量。定义和应用允许 DNS 解析的流量的策略，并确保策略具有正确的标签以针对特定 Pod。请记住，网络策略默认情况下会阻止流量，因此请确认策略已配置为允许必要的流量。

**步骤 3**: 验证设置。确保所有必需的流量路径都已打开以进行可观察性目的。

**步骤 4**: 验证设置后，部署 Hubble CLI 以跟踪 DNS 请求流。您可以应用过滤器以专门关注 DNS 协议流量，CLI 将开始显示 DNS 请求、响应和相关元数据，从而提供对流量流的宝贵见解。

这是一个示例输出：

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-3.png)

了解如何使用 **jq** 过滤特定的错误，这使得 Hubble 成为 DNS 故障排除的有力工具。

## Inspektor Gadget

[Inspektor Gadget](https://github.com/inspektor-gadget/inspektor-gadget) 是我们将介绍的用于检查 Kubernetes 和 Linux 系统的最终工具集。Inspektor Gadget 的 DNS gadget 使用 eBPF（扩展 Berkeley 数据包过滤器）跟踪 DNS 请求和响应，允许丰富的操作系统级上下文和 Kubernetes 增强功能。您可以将其作为 DaemonSet 部署在 Kubernetes 中，并通过 `kubectl gadget` 插件与之交互，或者使用 `kubectl` 节点调试进行测试，无需安装。

更多信息，请访问 [指南](https://www.inspektor-gadget.io/docs/latest/gadgets/trace_dns) 和 [源代码](https://github.com/inspektor-gadget/inspektor-gadget/tree/main/gadgets/trace_dns) 获取 DNS gadget 的信息。

**如何使用 Inspektor Gadget 调试应用程序 Pod**:

**步骤 1**: 在您的 Kubernetes 集群上运行 DNS Gadget
要开始使用 Inspektor Gadget 调试应用程序 pod，请确保您拥有适用于您的 gadget 的相应 OCI 镜像，可以通过 Inspektor Gadget GitHub 容器注册表访问。您可以在[artifacthub.io](https://artifacthub.io/packages/search?kind=22&verified_publisher=true&official=true&cncf=true&sort=relevance&page=1)找到官方和社区发布的 gadget。

使用`kubectl gadget`命令来追踪应用程序 pod 的 DNS 请求。此命令针对您感兴趣的特定命名空间和 pod，允许您查看正在进行的 DNS 查询。

**步骤 2**: 分析初始输出

输出应如下所示：

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-4.png)

输出将显示诸如 DNS 查询和响应之类的事件，以及完整的 Kubernetes 丰富数据，例如：

- 源：使用 Kubernetes 资源信息丰富的源 (mypod pod)。
- 目标：带有 Kubernetes 资源信息的目的地 (kube-dns 服务)。
- 查询信息和响应代码：DNS 查询的详细信息及其响应状态。

此简洁的视图提供了一种直接检查特定 pod 的 DNS 请求的方法。

**步骤 3**: 拓宽跟踪范围

如果您想观察单个 pod 之外的 DNS 活动，并包含不同命名空间中的 DNS 请求，请调整命令中的过滤器。您可以按 pod 名称或命名空间进行过滤，这有助于隔离与特定组件或服务相关的问题。这种方法可以查看从 pod 发出并到达 CoreDNS (kube-dns) 组件的 DNS 查询。此外，因为它是一个外部名称 (example.com)，CoreDNS 通过创建一个新的请求 (ID=2c39) 将其转发到上游服务器 (192.168.49.1)，如下所示：

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-5.png)

**步骤 4**: 扩展跟踪范围，超越 Pod 过滤器

通过删除特定的 pod 过滤器，您可以更广泛地查看集群内的网络交互，尤其是在节点上发生的情况。当诊断整个集群中发生的问题时，此更广泛的范围特别有用。

以下是预期输出的示例：

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-6.png)

在此输出中，您可以看到所有没有增强的行，这些行反映了节点级别上请求的处理情况。

这些行显示了如何在主机上处理请求。您可以使用网络命名空间 ID (**4026532220**) 来确认操作正在主机级别发生，从而清晰地了解节点级别的处理过程。

此外，**IP 转译** 在这里至关重要：您可以观察 IP 表如何将 kube-dns 服务 IP 转换为特定的 CoreDNS pod。这确保了正确的路由，并有助于诊断节点基础设施中请求处理的潜在问题。

## 工具总结

在下表中，您可以找到我们介绍的每个工具的主要功能：

| CoreDNS 日志插件 | Hubble | Inspektor Gadget |
|---|---|---|
| 非常适合初步检查，但其范围仅限于 CoreDNS。 | 提供带有增强功能和回顾性分析的请求流的简洁概述。 | 提供具有操作系统上下文和 Kubernetes 增强/过滤功能的丰富的 DNS 跟踪。 |
| 需要配置更改才能使用。 | 需要 Cilium CNI/特定的策略才能实现 L7 流可见性。 | 通过自定义 gadget 镜像进行扩展；不支持 TCP。 |

## 结束您的 Kubernetes DNS 调试之旅

现在您已经熟悉了各种可用于 DNS 调试的工具，让我们探索一些实际的调试场景。如需亲身体验，您还可以[观看带有详细步骤的实时演示](https://www.youtube.com/watch?v=KQpZg_NqbZw?t=1049)。

## 场景 1：验证上游 DNS 服务器的运行状况

在此场景中，我们将确保从 CoreDNS 到上游 DNS 服务器的请求按预期执行。您可以检查[此文件中](https://github.com/mqasimsarfraz/talks/tree/main/ContainerDays-2024/debug-scenario1)使用的脚本。

**步骤 1**: 确保 pod 正在生成 DNS 请求。

禁用 CoreDNS 中的任何缓存插件，以防止请求被缓存，这可能会掩盖对上游服务器查询的跟踪。编辑 CoreDNS `Corefile` 以删除或注释掉 `cache` 行。

重新启动 CoreDNS pod 以快速应用更改。

**步骤 2**: 部署一个测试 pod，该 pod 将 DNS 请求发送到诸如 `example.com` 和 `unknown.example.com` 之类的域名，以生成成功和错误请求的混合。

**步骤 3**: 运行 Inspektor Gadget。

使用 DNS gadget 过滤和观察来自上游服务器的响应。关注 `kube-system` 命名空间和 CoreDNS pod，并注意响应代码。

**步骤 4**: 解读结果。

`example.com` 的成功响应表示正常运行，而 `unknown.example.com` 的 `name error` 响应表示错误。
指示未解析域的预期行为。

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-7.png)

## 场景 2：识别失败的 DNS 响应

在本场景中，我们将确定网络中 DNS 请求失败的位置。作为参考，您可以使用[此文件](https://github.com/mqasimsarfraz/talks/tree/main/ContainerDays-2024/debug-scenario2)中使用的脚本。

**步骤 1**：故意创建故障。

为了模拟故障，请使用`erratic`插件修改 CoreDNS 配置以故意丢弃对`example.com`的请求。

编辑后，保存必要的更改并让它们生效，因为 CoreDNS Pod 会重启。

**步骤 2**：生成 DNS 请求。

使用测试 Pod 对`example.com`发起 DNS 查询，并使用 Inspektor Gadget 监控故障。

**步骤 3**：分析跟踪输出

跟踪应该显示请求过程，在 CoreDNS 处结束，而没有转发到上游服务器，从而确认丢弃。这表明 CoreDNS 处存在故意故障。

![](/static/debugging-dns-request-flows-in-kubernetes-clusters-8.png)

## 结论

Kubernetes 中的 DNS 调试需要了解内部请求流程以及用于可观察性和跟踪的正确工具。在本博客中，我们介绍了三个关键工具——CoreDNS 日志插件、Hubble 和 Inspektor Gadget——它们可以帮助您更深入地了解请求的发生情况。我们还使用这些工具探讨了两个实际的调试场景。

有关更详细的指南，请观看 ContainerDays 的完整演讲：[揭秘 DNS：Kubernetes 集群中请求流的理解和调试指南](https://www.youtube.com/watch?v=KQpZg_NqbZw&t=308s)。

查看[演示文稿的幻灯片](https://github.com/mqasimsarfraz/talks/blob/main/ContainerDays-2024/Demystifying%20DNS_%20A%20Guide%20to%20Understanding%20and%20Debugging%20Request%20Flows%20in%20Kubernetes%20Clusters.pdf)。