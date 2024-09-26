
<!--
title: Istio服务网格：为忙碌人士而生
cover: https://www.lucavall.in/images/blog/the-istio-service-mesh-for-people-who-have-stuff-to-do/cover.webp
-->

我最近为 **Istio** 做出了一个小贡献，Istio 是一个开源服务网格项目。我的贡献包括为 Istio CLI 的一个命令添加了一些测试。如果你想查看详细信息，可以在 [此处](https://github.com/istio/istio/pull/51635) 找到 pull 请求。这不是一个巨大的改变，但它是一个很棒的学习体验。在 Istio 上工作帮助我更深入地理解了服务网格。我很高兴能做出更多贡献。在这篇文章中，我将解释什么是 Istio，它为什么有用以及它是如何工作的。

> 译自 [The Istio Service Mesh for People Who Have Stuff to Do | Blog](https://www.lucavall.in/blog/the-istio-service-mesh-for-people-who-have-stuff-to-do)，作者 Luca Cavallin。

## 什么是 Istio？

从本质上讲，Istio 是一个 **服务网格**。服务网格管理微服务之间的通信，负责处理诸如路由流量、保护通信和提供可观测性等事项。随着微服务数量的增长，管理这些交互会变得很复杂。Istio 自动执行许多这些任务，因此你可以专注于构建应用程序，而不是管理服务之间的通信。

## 为什么要使用 Istio？

随着架构变得越来越复杂，你将面临新的挑战。服务需要以可靠、安全和高效的方式进行通信。Istio 帮助你在三个关键领域做到这一点：

1. **管理流量**: Istio 使你能够控制流量在服务之间如何流动。你可以将流量拆分到服务的不同版本之间，在部署期间重新路由请求，或者设置重试和超时策略。**保护通信**: Istio 使启用 
2. **双向 TLS (mTLS)** 变得容易。这确保了服务之间所有通信都是加密和经过身份验证的，从而阻止未经授权的服务。
3. **可观测性**: Istio 自动收集指标、日志和跟踪，使你能够实时了解你的服务。这有助于监控、故障排除和性能调整。

这三个领域——流量管理、安全性和可观测性——是运行健康微服务架构的关键，Istio 可以轻松地处理它们。

## 使用 Istio 管理流量

Istio 的主要功能之一是管理服务之间的流量。在微服务设置中，你可能有多个版本的同一个服务同时运行。例如，你可能正在测试支付服务的最新版本，并希望将大部分流量发送到版本 1，但将一些流量路由到版本 2。

以下是如何使用 Istio 将流量拆分到服务的两个版本之间的示例：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: payments
spec:
  hosts:
  - payments.myapp.com
  http:
  - route:
    - destination:
        host: payments
        subset: v1
        weight: 90
    - destination:
        host: payments
        subset: v2
        weight: 10
```

在这个例子中：

- **90% 的流量** 被发送到`payments` 服务的版本 1，而 **10%** 被发送到版本 2。
- `hosts` 字段指定虚拟服务适用的域——在本例中为`payments.myapp.com`。
- `route` 块定义了流量如何在服务的两个子集中进行拆分：`v1`（版本 1）和`v2`（版本 2）。`weight` 字段控制流量分配。

这对于 **金丝雀部署** 非常有用，在金丝雀部署中，你可以使用一小部分用户测试新功能，然后再完全推出。

## Envoy 代理和 Sidecar 容器

Istio 的 **数据平面** 依赖于 **Envoy 代理**，Envoy 代理是一个第 7 层代理，它管理服务之间所有流量。网格中的每个服务都有自己的 **Sidecar 代理**，它位于服务旁边，并管理其所有入站和出站流量。

Envoy 允许你应用流量策略，例如重试、超时和断路器，所有这些都无需更改应用程序代码。它还收集有关流量流的详细指标，有助于监控和调试。

由于 Envoy 作为 **Sidecar 容器** 运行，因此它可以在不干扰应用程序逻辑的情况下执行这些规则并收集数据。简而言之，Envoy 充当服务网格中所有通信的“交通警察”。

## 可观测性：了解系统中发生的事情

运行一个包含许多微服务的系统可能会让你难以了解正在发生的事情。Istio 的内置 **可观测性** 功能可以帮助你跟踪服务之间所有通信的指标、日志和跟踪。这对于监控系统的运行状况、发现性能问题和修复错误至关重要。

Istio 的可观测性工具可以让你清楚地了解系统的工作方式。你可以及早发现问题，并使你的服务运行得更加顺畅。

## 安全：启用 mTLS 和访问控制

安全是管理微服务时的一大问题。Istio 使实施 **双向 TLS (mTLS)** 变得容易，双向 TLS (mTLS) 会加密服务之间的所有通信，并确保服务在交换数据之前相互验证身份。

Istio 还允许您设置**访问控制策略**，以指定哪些服务可以进行通信。这有助于限制哪些服务可以交互，从而减少系统的攻击面。

以下是一个 Istio 策略示例，该策略仅允许 `billing` 服务与 `payments` 服务通信：

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: payments-to-billing
spec:
  selector:
    matchLabels:
      app: payments
  rules:
  - from:
    - source:
        principals: ["billing.myapp.com"]
```

在此策略中：

- `selector` 指定此规则适用于 `payments` 服务，使用标签 `app: payments`。
- `rules` 块仅允许 `billing` 服务（由主体 `"billing.myapp.com"` 标识）与 `payments` 服务通信。任何其他服务都不允许向 `payments` 服务发送流量。

此策略限制除 `billing` 服务之外的所有服务访问 `payments` 服务，从而加强了微服务的安全性。

## 什么是 SPIFFE？

Istio 使用**SPIFFE**（安全生产身份框架，面向所有人）来管理服务身份。SPIFFE 提供了一种为服务分配安全、可验证身份的方法。网格中的每个服务都会获得一个**SPIFFE 可验证身份文档 (SVID)**，该文档与 mTLS 一起使用以确保安全通信。此身份系统是 Istio 安全模型的基础。

## Istio 中的网络

微服务中的网络可能很困难，尤其是在控制网格内部和外部的流量时。Istio 提供了几种管理网络流量的工具：

1. **服务条目**: 允许外部服务与网格内部的服务进行通信，反之亦然。
2. **虚拟服务**: 定义流量如何在网格内部路由。
3. **目标规则**: 将流量策略（如负载均衡或 mTLS）应用于服务。
4. **网关**: 管理进出网格的流量。


## 配置示例：网关、服务条目、虚拟服务和目标规则

假设您在网格中有一个 API 服务器，它通过负载均衡器接收来自互联网的流量。以下是如何配置**网关**、**服务条目**、**虚拟服务**和**目标规则**来处理此流量。

**网关配置**

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: api-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "api.myapp.com"
```

这里发生了什么？**网关**在**端口 80** 上监听来自域 `api.myapp.com` 的 HTTP 流量。`selector` 字段将此网关连接到**Istio 入口网关**，该网关处理进入网格的流量。

**服务条目配置**

假设您的 API 服务器需要调用外部身份验证服务。以下是如何配置**服务条目**：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: auth-service-entry
spec:
  hosts:
  - "auth.external-service.com"
  location: MESH_EXTERNAL
  ports:
  - number: 443
    name: https
    protocol: HTTPS
  resolution: DNS
  endpoints:
  - address: 203.0.113.1
```

这里发生了什么？**服务条目**告诉 Istio 如何将流量路由到外部服务 (`auth.external-service.com`)，该服务在**端口 443**（HTTPS）上运行。`location: MESH_EXTERNAL` 指示此服务存在于 Istio 服务网格之外。`endpoints` 字段包含外部服务的 IP 地址，允许网格内的 API 服务器发送请求。

**虚拟服务配置**

以下是如何在网格内路由流量：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: api-virtualservice
spec:
  hosts:
  - "api.myapp.com"
  gateways:
  - api-gateway
  http:
  - match:
    - uri:
        prefix: "/v1"
    route:
    - destination:
        host: api-service
        subset: stable
```

这里发生了什么？**虚拟服务**定义了流量路由规则。在这种情况下，通过 `api-gateway` 到达 `api.myapp.com/v1` 的流量将路由到网格中的 `api-service`。`subset: stable` 指的是 `api-service` 的特定版本（您可以拥有同一服务的多个版本）。

**目标规则配置**

最后，以下是一个**目标规则**，用于应用负载均衡和 mTLS：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: api-destination-rule
spec:
  host: api-service
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN
    tls:
      mode: ISTIO_MUTUAL
```

这里发生了什么？**目标规则**将策略应用于路由到 `api-service` 的流量。它使用**轮询**负载均衡将请求均匀地分布到实例中。**mTLS** 通过 `tls.mode: ISTIO_MUTUAL` 启用，确保服务之间加密通信。

## 弹性：使用重试、超时和断路器处理故障

在分布式系统中，故障是不可避免的。服务可能会宕机，网络可能会变慢，或者用户可能会遇到延迟。Istio 可以帮助您使用**重试**、**超时**和**断路器**来处理这些问题。

- **重试**: 自动重试失败的请求，以处理临时故障，而不会影响用户体验。
- **超时**: 定义服务在放弃并继续执行之前应等待响应的时间。
- **断路器**: 如果服务出现故障，Istio 可以停止向其发送流量，从而防止可能导致系统其他部分崩溃的级联故障。

以下是如何在 Istio 中配置重试和超时的示例：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: my-service
spec:
  hosts:
  - my-service
  http:
  - route:
    - destination:
        host: my-service
      retries:
        attempts: 3
        perTryTimeout: 2s
      timeout: 5s
```

这里发生了什么？如果对 `my-service` 的请求失败，Istio 将最多重试该请求 **3 次**。每次重试尝试都有 **2 秒的限制**。请求的总允许时间为 **5 秒**。在此之后，Istio 将停止等待响应。

对于断路，您可以使用类似这样的**目标规则**：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: my-service
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        http1MaxPendingRequests: 50
    outlierDetection:
      consecutive5xxErrors: 2
      interval: 10s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
```

这里发生了什么？如果 `my-service` 在 **10 秒内**返回 **两个连续的 5xx 错误**，Istio 将停止向其发送流量。该服务将从负载均衡池中剔除 **30 秒**，然后重新考虑。

## 总结

Istio 是一个强大的工具，它简化了微服务的流量管理、安全性和可观测性。为 Istio 做贡献让我了解了它如何帮助解决运行分布式系统时遇到的一些复杂挑战。

如果您正在运行微服务架构或计划进行扩展，Istio 可以帮助您使系统更具弹性和更易于管理。如果您有任何问题或想了解更多关于 Istio 的信息，请随时联系我，我很乐意分享我的经验。