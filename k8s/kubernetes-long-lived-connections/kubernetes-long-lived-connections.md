
<!--
title: 在Kubernetes中负载均衡和扩展长连接
cover: https://static.learnk8s.io/4f9741344d5b7e302652468bc6be6b59.png
-->

Kubernetes 不会对长期连接进行负载均衡，并且一些 Pod 可能会比其他 Pod 接收更多请求。如果您正在使用 HTTP/2、gRPC、RSockets、AMQP 或任何其他长期连接（例如数据库连接），您可能需要考虑客户端负载均衡。

> 译自 [Load balancing and scaling long-lived connections in Kubernetes](https://learnk8s.io/kubernetes-long-lived-connections)，作者 Daniele Polencic。

*要点：Kubernetes 不会对长连接进行负载均衡，某些 Pod 可能接收的请求比其他 Pod 多。如果您使用 HTTP/2、gRPC、RSockets、AMQP 或任何其他长连接数据库连接，请考虑使用客户端负载均衡或代理。*

Kubernetes 提供了两个便捷的抽象概念，用于部署应用：服务和部署。

**部署描述了一个配方，说明您的应用在任何给定时间应该运行什么类型以及运行多少个副本。**

每个应用都作为 Pod 部署，并分配一个 IP 地址。

**另一方面，服务类似于负载均衡器。**

它们旨在将流量分配给一组 Pod。

![- 1/4](https://learnk8s.io/a/c62b844725054a789045193c5af5d245.svg)

*在此图表中，您有三个单个应用实例和一个负载均衡器。*

![- 2/4](https://learnk8s.io/a/d8e9a17e0af2f745fe071aec6c918d82.svg)

*负载均衡器称为服务，并具有 IP 地址。任何传入请求都会分配给其中一个 Pod。*

![- 3/4](https://learnk8s.io/a/7e3505096792cf045dae1c86602f3a67.svg)

*部署定义了一个配方，用于创建同一 Pod 的更多实例。您很少单独部署 Pod。*

[- 4/4](https://learnk8s.io/a/591660df28a878ec937d8ee49a7a2a49.svg)

*Pod 已分配了一个 IP 地址。*

**通常将服务视为 IP 地址的集合非常有用。**

每当您请求服务时，都会选择该列表中的一个 IP 地址并用作目标。

![- 1/3](https://learnk8s.io/a/bfad9f818be47768e09e7e87aa9eafbe.svg)

*想象一下向服务发出请求，例如 curl 10.96.45.152。*

![- 2/3](https://learnk8s.io/a/93fbaddc90cd2738173c042c72cdb7b4.svg)

*服务将三个 Pod 中的一个选为目标。*

![- 3/3](https://learnk8s.io/a/45dbb5efacb3efe756d93d95e7dceb1a.svg)

*流量被转发到该实例。*

如果您有两个应用（前端和后端），则可以为每个应用使用部署和服务，并在集群中部署它们。

**当前端应用发出请求时，它不需要知道有多少个 Pod 连接到后端服务。**

它可以是一个 Pod，也可以是几十个或几百个。前端应用也不了解后端应用的各个 IP 地址。当它想要发出请求时，该请求将发送到具有不会更改的 IP 地址的后端服务。

![- 1/4](https://learnk8s.io/a/5a7c9a225135ac88cfa88fbb24b8745b.svg)

*红色 Pod 向内部（米色）组件发出请求。红色 Pod 没有将其中一个 Pod 选为目标，而是向服务发出请求。*

![- 2/4](https://learnk8s.io/a/1e09f00bdeada445a87e01f1394b1401.svg)

*服务将其中一个就绪 Pod 选为目标。*

![- 3/4](https://learnk8s.io/a/843057629257694277a07b38d01c36e9.svg)

*流量从红色 Pod 流向浅棕色 Pod。*

![- 4/4](https://learnk8s.io/a/44b5a1479a5f5f5d8b2eb4cc5ed77669.svg)

*请注意，红色 Pod 不知道服务后面隐藏了多少个 Pod。*

*但是服务的负载均衡策略是什么？* *是轮询，对吧？*

差不多。

## Kubernetes 服务中的负载均衡

**Kubernetes 服务不存在。**

没有进程监听服务的 IP 地址和端口。

> 您可以通过访问 Kubernetes 集群中的任何节点并执行 netstat -ntlp 来检查情况是否如此。

甚至在任何地方都找不到 IP 地址。

服务的 IP 地址由控制器管理器中的控制平面分配，并存储在数据库 etcd 中。

然后，另一个组件 kube-proxy 使用相同的 IP 地址。

Kube-proxy 读取所有服务的 IP 地址列表，并在每个节点中写入规则。

这些规则的意思是，“如果您看到此服务 IP 地址，请重写请求并选择其中一个 Pod 作为目标。”

服务 IP 地址仅用作占位符，因此没有进程监听 IP 地址或端口。

![- 1/8](https://learnk8s.io/a/a3e195d7ee05e50797e7444aacabc31d.svg)

*考虑一个有三个节点的集群。每个节点都部署了一个 Pod。*

![- 2/8](https://learnk8s.io/a/28e1cbd79bc0b40cb6a21a6465ee7971.svg)

*米色 Pod 是服务的一部分。服务不存在，因此图表将组件灰显。*

![- 3/8](https://learnk8s.io/a/d8b049c0f076938e7a806d29bec83f00.svg)

*红色 Pod 想要向服务发出请求，并最终到达其中一个米色 Pod。*

![- 4/8](https://learnk8s.io/a/7ad64c57cf4c15c89846b6f7759474bf.svg)

*但服务不存在。没有进程监听服务的 IP 地址。它是如何工作的？*

![- 5/8](https://learnk8s.io/a/f7114f63e281868ac2a5f1c9e3083e19.svg)

*在从节点分派请求之前，它会被 iptables 规则拦截。*

![- 6/8](https://learnk8s.io/a/6ed09629d942890a5b965334414ba3fd.svg)

*iptables 规则知道服务不存在，因此用连接到该服务的 Pod 的 IP 地址之一替换其 IP 地址。*

![- 7/8](https://learnk8s.io/a/3789c862f73c4b36e3849af0ed095387.svg)

*请求具有实际 IP 地址作为目标，并且可以正常进行。*

![- 8/8](https://learnk8s.io/a/d720b7535c378ae7ab0d741ffdd7438d.svg)

*根据您的网络实现，请求最终到达 Pod。*

默认情况下，Kubernetes 使用 iptables 来实现服务。

*iptables 是否使用轮询进行负载均衡？*

不，iptables 主要用于防火墙，不适用于负载均衡。

但是，您可以[制作一套智能规则，使 iptables 表现得像负载均衡器](https://scalingo.com/blog/iptables#load-balancing)。

这正是 Kubernetes 中发生的情况。

如果您有三个 Pod，kube-proxy 会写入以下规则：

1. 以 33% 的可能性选择 Pod 1 作为目标。否则，继续执行以下规则。
2. 以 50% 的概率选择 Pod 2 作为目标。否则，继续执行以下规则。
3. 选择 Pod 3 作为目标（无概率）。

复合概率是 Pod 1、Pod 2 和 Pod 3 被选中的机会均为三分之一 (33%)。

![](https://learnk8s.io/a/fbbcbf56da96099c15314b9af4a0dd77.svg)

此外，无法保证 Pod 2 在 Pod 1 之后被选为目标。

> Iptables 使用 [统计模块](https://www.netfilter.org/projects/iptables/index.html#modules)，其中包含 randommode。因此，负载均衡算法是随机的。

您可能听说过 iptables 的替代方案，例如 ipvs 和 eBPF。虽然技术不同，但核心思想是相似的：如何将流量重定向到正确的 Pod？

在 eBPF 的情况下，[网络数据包在 eBPF 虚拟机中的内核中处理，并且由 eBPF 程序定义负载均衡算法。](https://github.com/lizrice/lb-from-scratch)

现在您已经了解了服务的工作原理，让我们来看看更激动人心的场景。

## 长连接无法在 Kubernetes 中开箱即用地扩展

**从前端到后端启动的每个 HTTP 请求都会打开并关闭一个新的 TCP 连接。**

如果前端每秒向后端发出 100 个 HTTP 请求，那么在这一秒内将打开并关闭 100 个不同的 TCP 连接。

如果您打开一个 TCP 连接并将其重复用于后续 HTTP 请求，则可以改善延迟并节省资源。

HTTP 协议有一个称为 HTTP keep-alive 或 HTTP 连接重用的功能，它使用单个 TCP 连接来发送和接收多个 HTTP 请求和响应。

它无法开箱即用；您的服务器和客户端应配置为使用它。

![](https://learnk8s.io/a/83f9bebffbbbee8d6a25315b8679f9df.svg)

更改本身很简单，并且在大多数语言和框架中都可用。

以下是如何在不同语言中实现保持活动的一些示例：

- [Keep-alive in Node.js.](https://medium.com/@onufrienkos/keep-alive-connection-on-inter-service-http-requests-3f2de73ffa1)
- [Keep-alive in Spring Boot.](https://www.baeldung.com/httpclient-connection-management)
- [Keep-alive in Python.](https://blog.insightdatascience.com/learning-about-the-http-connection-keep-alive-header-7ebe0efa209d)
- [Keep-alive in .NET.](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest.keepalive?view=netframework-4.8)

*当您对 Kubernetes Service 使用 keep-alive 时，将发生什么？*

让我们想象一下前端和后端支持保持活动。

您有一个前端实例和三个后端副本。

前端向后端发出第一个请求并打开 TCP 连接。

请求到达服务，其中一个 Pod 被选为目标。

后端 Pod 答复，前端收到响应。

但它不会关闭 TCP 连接，而是将其保持打开状态以供后续 HTTP 请求使用。

当前端发出更多请求时会发生什么？

它们被发送到同一个 Pod。

iptables 不应该分配流量吗？

是的。

打开了一个 TCP 连接，并且第一次调用了 iptables 规则。

三个 Pod 中的一个被选为目标。

由于所有后续请求都通过同一个 TCP 连接进行，[不再调用 iptables。](https://scalingo.com/blog/iptables#load-balancing)

![- 1/5](https://learnk8s.io/a/3d9434491906a7f16962b3ca12cf896e.svg)

*红色 Pod 向服务发出请求。*

![- 2/5](https://learnk8s.io/a/f7114f63e281868ac2a5f1c9e3083e19.svg)

*您已经知道接下来会发生什么。服务不存在，但 iptables 规则会拦截请求。*

![- 3/5](https://learnk8s.io/a/6ed09629d942890a5b965334414ba3fd.svg)

*属于该服务的一个 Pod 被选为目标。*

![- 4/5](https://learnk8s.io/a/0f85a87d2a76302ca5ba580180d5fdc5.svg)

*最后，请求到达 Pod。此时，在两个 Pod 之间建立了持久连接。*

![- 5/5](https://learnk8s.io/a/46ec0878e28fc5e8995415774883a3bc.svg)

*红色 Pod 的任何后续请求都会重复使用现有的打开连接。*

**因此，您现在获得了更好的延迟和吞吐量，但失去了扩展后端的能力。**

即使您有两个可以接收来自前端 Pod 的请求的后端 Pod，但只有一个处于活动状态。

可以修复吗？

您可以自己修复它，因为 Kubernetes 不知道如何对持久连接进行负载均衡。

**服务是称为端点的 IP 地址和端口的集合。**

您的应用可以从服务中检索端点列表，并决定如何分配请求。

作为第一次尝试，您可以对每个 Pod 打开一个持久连接，并对它们进行循环请求。

或者您可以 [实现更复杂的负载均衡算法](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2019/daperture-load-balancer.html)。

执行负载均衡的客户端代码应遵循以下逻辑：

1. 从服务中检索端点列表。
2. 对每个端点，打开一个连接并保持打开状态。
3. 在需要发出请求时选择一个打开的连接。
4. 定期刷新端点列表，并删除或添加新连接。

![- 1/4](https://learnk8s.io/a/bd7b0d3f4b3d509a113719b1f5d12e48.svg)

*您可以对客户端进行负载均衡，而不是让红色 Pod 向您的服务发出请求。*

![- 2/4](https://learnk8s.io/a/c02175878ab236821df0a61215932760.svg)

*您可以编写一些代码来询问哪些 Pod 是服务的一部分。*

![- 3/4](https://learnk8s.io/a/3d99a9065b0701778cec366802bf21d6.svg)

*获得该列表后，您可以将其存储在本地并使用它连接到 Pod。*

![- 4/4](https://learnk8s.io/a/062514bf827342a12474c032d7b9a4d4.svg)

*您负责负载均衡算法。*

此问题仅适用于 HTTP keep-alive 吗？

## 长数据库连接

**HTTP 并不是唯一可以从长 TCP 连接中受益的协议。**

如果您的应用使用数据库，则无论何时要检索记录或文档，都不会打开和关闭连接。

相反，TCP 连接一旦建立就会保持打开状态。

如果您的数据库使用服务部署在 Kubernetes 中，您可能会遇到与上一个示例相同的问题。

**数据库中的一个副本比其他副本利用得更多。**

Kube-proxy 和 Kubernetes 无法帮助平衡持久连接。

![](https://learnk8s.io/a/cb2c01610ebc62e9ab34797eb8627838.svg)

相反，您应该负责对数据库请求进行负载均衡。此时，您有两个选择：

1. 更改您的应用以支持连接到多个后端。
2. 引入一个*真正的*负载均衡器来分配负载。

在第一个选项中，您将负载均衡决策移至应用。

在伪代码中，如果您想连接到具有多个副本的数据库，则应该执行以下操作：

```
Before issuing an SQL query:
- Retrieve all replica IPs from the Services.
- Pick a different replica from the previous one.
- Dispatch the SQL query
```

此逻辑可能已经存在，具体取决于您用于连接到数据库的库。

在[JDBC](https://jdbc.postgresql.org/documentation/use/#connection-fail-over) 的情况下，以下行允许将查询负载均衡到三个 Postgres 副本：

```
jdbc:postgresql://node1,node2,node3/database?loadBalanceHosts=true
```

[SQLAlchemy 支持提供多个 IP 地址](https://github.com/sqlalchemy/sqlalchemy/issues/4392)，但不提供负载均衡（按顺序尝试 IP 地址，直到其中一个起作用。此时，连接保持稳定）。*在这种情况下，您可以做什么？*

您可以打开几个不同的 SQL 连接并在它们之间循环。或者，您可以使用外部负载均衡器，如 [pgpool](https://www.pgpool.net/mediawiki/index.php/Main_Page)。

在此场景中，您的应用连接到一个端点：pgpool。

[然后，pgpool 将查询负载均衡到所有可用的 Postgres 副本。](https://www.pgpool.net/docs/latest/en/html/runtime-config-load-balancing.html) 

![](https://learnk8s.io/a/c8064d5fe89ad7ac42017414019bdbfe.svg)

**因此，即使应用与 pgpool 之间的连接是持久的（即长期存在的），查询仍会利用所有可用的副本。**

我们在 Postgres 中解决了长期连接，但其他几个协议通过长期 TCP 连接工作。您可以在此处阅读一些示例：

- Websocket 和安全 Websocket
- HTTP/2
- gRPC
- RSocket
- AMQP

*您应该如何处理这些？*

归结为两个选项：

- 您在客户端处理负载均衡，或者
- 您使用外部工具为您执行此操作。

我们来看另外两个常见的示例：gRPC 和 Websocket。

[您可以在应用中对 gRPC 请求进行负载均衡](https://itnext.io/grpc-name-resolution-load-balancing-everything-you-need-to-know-and-probably-a-bit-more-77fc0ae9cd6c)，或者您可以使用 [类似 Envoy 的代理来对 gRPC 请求进行负载均衡。](https://svkrclg.medium.com/grpc-load-balancing-using-envoy-e8972214da2c)

对于 Websocket，情况更复杂。只有在打开多个隧道并在它们之间循环时，您才能在客户端平衡连接。您只能使用[负载均衡器，如 HAProxy。](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/load-balancing/websocket/) 

**请注意，在服务器端解决持久连接主要在于找到一个合适的代理来平衡连接，而在客户端进行负载均衡则需要更多思考。**

但有办法解决这个问题。

## 在 Kubernetes 中对长期连接进行负载均衡

Kubernetes 有四种不同的服务：

- ClusterIP
- NodePort
- LoadBalancer
- External

它们都有一个虚拟 IP 地址，kube-proxy 使用该地址创建 iptables 规则。

**但所有类型服务的根本构建块都是无头服务。**

无头服务没有分配的 IP 地址，它只是一种收集 Pod IP 地址和端口（也称为端点）的机制。所有其他服务都建立在无头服务之上。

ClusterIP 服务是一个具有某些额外功能的无头服务：

- 控制平面为其分配一个 IP 地址。
- kube-proxy 遍历所有 IP 地址并创建 iptables 规则。

您可以忽略 kube-proxy，并始终使用无头服务收集的端点列表，以便从客户端对请求进行负载均衡。

*但您能想象将该逻辑添加到群集中部署的所有应用中吗？*

如果您有现有的应用，这听起来可能是一项不可能完成的任务。但有一个替代方案。

## 服务网格来救援

您可能已经注意到，客户端负载均衡策略相对标准化。当应用启动时，它应该

1. 从服务中检索 IP 地址列表。
2. 打开并维护连接池。
3. 通过添加和删除端点定期刷新池。

一旦它希望发出请求，它应该：

- 使用预定义的逻辑（例如循环）选择一个可用连接。
- 发出请求。

这类似于 pgpool 在上一个示例中的工作方式。上述步骤适用于 Websocket 连接、gRPC 和 AMQP。

您可以在单独的库中提取该逻辑，并与所有应用共享。您可以使用服务网格，例如 [Istio](https://istio.io/) 或 [Linkerd](https://linkerd.io/)。

服务网格通过一个新进程增强你的应用，该进程：

- 自动从服务中发现 IP 地址。
- 检查 WebSocket 和 gRPC 等连接。
- 使用正确的协议进行负载均衡请求。

**服务网格可以帮助你管理集群内的流量，但它们并不轻量级。** 

*如果你忽略它会怎样？*

你可以忽略负载均衡，但仍然不会注意到任何变化。

有几个场景你应该考虑。

**如果你有比服务器更多的客户端，应该会有有限的问题。**

想象一下，你有五个客户端打开到两个服务器的持久连接。

即使没有负载均衡，两个服务器也可能被利用。

![](https://learnk8s.io/a/317efc5e7a260b1f477a95e3b1f101f9.svg)

连接可能会分布不均（可能四个最终连接到同一个服务器），但总体而言，两个服务器都有可能被利用。

更成问题的是相反的场景。

**如果你有更少的客户端和更多的服务器，你可能有一些未充分利用的资源和潜在的瓶颈。**

想象一下有两个客户端和五个服务器。在最好的情况下，会打开到两个服务器的两个持久连接。其余的服务器根本没有被使用。

![](https://learnk8s.io/a/cada9a6e57b5440f779aef1f6c758494.svg)

**如果两个服务器无法处理客户端流量，水平扩展将无济于事。**

## 总结

Kubernetes 服务旨在涵盖 Web 应用程序最常见的用途。

但是，一旦你开始使用使用持久 TCP 连接的应用程序协议（例如数据库、gRPC 或 WebSocket），它们就会崩溃。

Kubernetes 不提供任何内置机制来负载均衡长寿命的 TCP 连接。

相反，你应该编写你的应用程序来检索和负载均衡客户端端的 upstream。或者你应该考虑一个可以负载均衡连接的代理。

非常感谢 [Daniel Weibel](https://medium.com/@weibeld)、[Gergely Risko](https://github.com/errge) 和 [Salman Iqbal](https://twitter.com/soulmaniqbal) 提供了一些宝贵的建议。

以及 [Chris Hanson](https://twitter.com/CloudNativChris)，他建议包括一个详细的解释（和流程图）来说明 iptables 规则在实践中的工作原理。