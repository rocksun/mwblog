<!--
title: 简化通配符目标地址的出站路由
cover: https://raw.githubusercontent.com/istio/istio.io/master/static/img/istio-social.png
summary: 本文介绍了 Istio 如何通过支持 DYNAMIC_DNS 解析的通配符 ServiceEntry 简化出站路由。相比传统的出口网关方案，新方法降低了延迟与配置复杂度，并支持 Ambient 模式。
-->

本文介绍了 Istio 如何通过支持 DYNAMIC_DNS 解析的通配符 ServiceEntry 简化出站路由。相比传统的出口网关方案，新方法降低了延迟与配置复杂度，并支持 Ambient 模式。

> 译自：[Simplifying Egress Routing to Wildcard Destinations](https://istio.io/latest/blog/2026/egress-dynamic-dns/)
> 
> 作者：Rudrakh Panigrahi (Salesforce)

## 概览

在服务网格部署中，控制出站（egress）流量是一个常见需求。许多组织通过设置以下配置，将网格配置为仅允许显式注册的外部服务：

```
meshConfig.outboundTrafficPolicy.mode = REGISTRY_ONLY
```

在此配置下，任何外部目的地都必须使用 `ServiceEntry` 等资源在网格中注册，并指定全限定域名和 DNS 解析类型。

```
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: external-wikipedia-https
  namespace: istio-system
spec:
  hosts:
  - "www.wikipedia.org"
  ports:
  - name: tls
    number: 443
    protocol: TLS
  location: MESH_EXTERNAL
  resolution: DNS
  exportTo:
  - "*"
```

然而，一些外部服务暴露了许多动态子域名，应用程序可能需要访问如下端点：

```
https://en.wikipedia.org
https://de.wikipedia.org
https://upload.wikipedia.org
```

随着主机名列表的增加，逐个注册每个主机名很快就会变得难以管理且难以扩展。为了解决这个问题，Istio 需要支持通配符主机名注册。

## 为什么通配符 HTTPS 出站如此困难

当工作负载发起 HTTPS 连接时，目标主机名通过 **服务器名称指示 (SNI)** 字段在 TLS 握手中传输。

例如，调用 `https://en.wikipedia.org` 的客户端在 TLS 握手期间会在 ClientHello SNI 字段中发送主机名 `en.wikipedia.org`。Istio sidecar 会拦截出站连接，并确定目标是否已注册以及应如何路由。

然而，Istio 的路由模型通常要求提前知道上游目的地。即使在路由规则中使用了通配符匹配，最终的上游集群仍必须对应一个静态配置的服务。由于不同的子域名可能解析到不同的端点，因此历史上直接路由到通配符主机并不简单。

## 通过 Egress Gateway 进行 SNI 路由

这个问题此前在 Istio 博客文章 [将出站流量路由到通配符目的地](https://istio.io/latest/blog/2023/egress-sni/) 中得到过解决。该架构包含一个充当 SNI 前向代理的专用出口网关设置。

[![带有任意域名的 Egress SNI 路由](https://istio.io/latest/blog/2026/egress-dynamic-dns/egress-sni-flow.svg)](https://istio.io/latest/blog/2026/egress-dynamic-dns/egress-sni-flow.svg "带有任意域名的 Egress SNI 路由")

应用程序 → sidecar → 出口网关 → SNI 检测 → 外部目的地

上图最初发布于 [将出站流量路由到通配符目的地](https://istio.io/latest/blog/2023/egress-sni/)。

如上所示：

1. 应用程序发起 HTTPS 连接。
2. Sidecar 代理拦截此连接并向出口网关发起内部 mTLS 连接。
3. 网关终止此内部 mTLS 连接。
4. 内部监听器检查原始 TLS 握手中的 SNI 值。
5. 流量动态转发到从 SNI 中提取的主机名。

实现这一点需要多个自定义资源：

* `ServiceEntry` 和 `VirtualService` 用于将通配符域名流量转发到出口网关。
* `DestinationRule` 用于 sidecar 与网关之间的 mTLS。
* `EnvoyFilter` 配置使出口网关能够执行动态 SNI 转发，这是迄今为止该方案中最复杂的部分。该过滤器通过引入三个组件利用底层 Envoy 功能扩展了网关：**对网关 TCP 代理的补丁**（将流量路由到内部监听器）、**监听器中的 SNI 检测器**（从 TLS ClientHello 中提取 SNI）以及一个**动态前向代理集群**（用于对 SNI 进行动态 DNS 解析）。

虽然这种方法有效，但它引入了额外的网络跳数以及该跳数的额外内部 mTLS 层。由于需要大量的自定义配置，它还增加了操作复杂度，这些配置可能难以管理且容易出错。但最近的改进使得通过更简单的配置实现相同的结果成为可能。

## 带有 `DYNAMIC_DNS` 解析的通配符 `ServiceEntry`

Istio 现在支持在 `ServiceEntry` 中使用带有 `DYNAMIC_DNS` 解析的通配符主机名，使 sidecar 代理能够直接路由通配符出站 TLS 流量，而无需出口网关。

例如，以下配置允许访问所有 `*.wikipedia.org` 端点：

```
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: external-wildcard-https
  namespace: istio-system
spec:
  hosts:
  - "*.wikipedia.org"
  ports:
  - name: tls
    number: 443
    protocol: TLS
  location: MESH_EXTERNAL
  resolution: DYNAMIC_DNS
  exportTo:
  - "*"
```

应用此资源后，网格中的工作负载可以通过此 ServiceEntry 连接到任何匹配的子域名。

```
$ kubectl exec $POD_NAME -n default -c ratings -- curl -sS -o /dev/null -w "HTTP %{http_code}\n" https://de.wikipedia.org && echo "Checking stats after request..." && kubectl exec $POD_NAME -c istio-proxy -- curl -s localhost:15000/clusters | grep "outbound|443||\*\.wikipedia\.org" | grep -E "rq|cx"

HTTP 200
Checking stats after request...
outbound|443||*.wikipedia.org::142.251.223.228:443::cx_active::0
outbound|443||*.wikipedia.org::142.251.223.228:443::cx_connect_fail::0
outbound|443||*.wikipedia.org::142.251.223.228:443::cx_total::3
outbound|443||*.wikipedia.org::142.251.223.228:443::rq_active::0
outbound|443||*.wikipedia.org::142.251.223.228:443::rq_error::0
outbound|443||*.wikipedia.org::142.251.223.228:443::rq_success::0
outbound|443||*.wikipedia.org::142.251.223.228:443::rq_timeout::0
outbound|443||*.wikipedia.org::142.251.223.228:443::rq_total::3
```

### 配置如何工作

[![带有 DYNAMIC_DNS 解析的通配符 ServiceEntry](https://istio.io/latest/blog/2026/egress-dynamic-dns/egress-dynamic-dns.svg)](https://istio.io/latest/blog/2026/egress-dynamic-dns/egress-dynamic-dns.svg "带有 DYNAMIC_DNS 解析的通配符 ServiceEntry")

应用程序 → sidecar → 外部目的地

带有 `resolution: DYNAMIC_DNS` 的通配符 `ServiceEntry` 会导致 Istio 创建一个[动态前向代理 (DFP)](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/clusters/dynamic_forward_proxy/v3/cluster.proto#envoy-v3-api-msg-extensions-clusters-dynamic-forward-proxy-v3-clusterconfig) 集群，该集群根据 SNI 字段中的主机名转发 TLS 连接。通配符主机（例如 `*.wikipedia.org`）首先在网格服务注册表中注册，允许 sidecar 路由主机名匹配该模式的出站请求。当工作负载发起 TLS 连接时，监听器中的 SNI 检测器被配置为从握手中读取 SNI 值。然后，DFP 集群将其用作上游主机名来转发连接。通过允许代理动态解析并转发连接到匹配的子域名，而无需静态端点配置，这有效地实现了通配符 HTTPS 出站。与此同时，它保留了客户端发起的 TLS 会话，原封不动地转发加密流量。

## 其他用例

这种方法适用于应用程序需要连接到通配符域名，同时仍需获得网格可观测性和弹性功能的用例。

### Ambient 模式下的出站流量

在 [Ambient 网格](https://istio.io/latest/docs/ambient/overview/)中，节点级 ztunnel 处理 L4 流量，而可选的 [waypoint 代理](https://istio.io/latest/docs/ambient/usage/waypoint/)可以在显式附加时应用 L7 策略和遥测。为了通过 waypoint 处理出站流量（例如，为了给调用许多 AWS 服务端点的请求保持一致的策略路径），可以为 `ServiceEntry` 标记 `istio.io/use-waypoint` 标签，以便控制平面通过名为 `waypoint` 的 `Gateway` 引导匹配的流量。

下面的示例将 `*.amazonaws.com` 注册为外部 TLS (`443`) ServiceEntry，并将其固定到名为 `waypoint` 的 waypoint 网关：

```
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: amazonaws-wildcard
  namespace: istio-system
  labels:
    istio.io/use-waypoint: waypoint # 附加到 waypoint 网关
spec:
  exportTo:
  - .
  hosts:
  - '*.amazonaws.com'
  location: MESH_EXTERNAL
  ports:
  - name: tls
    number: 443
    protocol: TLS
  resolution: DYNAMIC_DNS
```

### 发往未知内部目的地的流量

调用者可能在其配置中只有有限数量的服务，但仍需要与其他内部服务建立 mTLS 连接。设置如下：

* 一个 `Sidecar` 资源，限制 ratings 服务的出站主机仅限于 `istio-system` 命名空间，即它不能直接调用 details 服务：

```
apiVersion: networking.istio.io/v1
kind: Sidecar
metadata:
  name: restrict-default
  namespace: default
spec:
  workloadSelector:
    labels:
      app: ratings
  egress:
  - hosts:
    - "istio-system/*"
```

* 定义其他内部服务通配符服务的 `ServiceEntry`：

```
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: internal-wildcard-http
  namespace: istio-system
spec:
  hosts:
  - "*.svc.cluster.local"
  ports:
  - name: http
    number: 9080
    protocol: HTTP
  location: MESH_INTERNAL
  resolution: DYNAMIC_DNS
  exportTo:
  - "*"
```

* 为此 `ServiceEntry` 定义 mTLS 配置的 `DestinationRule`：

```
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: internal-wildcard-dr
  namespace: istio-system
spec:
  host: "*.svc.cluster.local"
  trafficPolicy:
    tls:
      mode: MUTUAL_TLS # 需要证书中的 DNS SAN
  exportTo:
  - "*"
```

Ratings 服务现在可以调用网格中的其他服务，即使它的配置中没有这些服务，方法是使用 DNS 动态解析主机名：

```
$ kubectl exec $POD_NAME -n default -c ratings -- curl -sS -o /dev/null -w "HTTP %{http_code}\n" details.default.svc.cluster.local:9080/details/0 && echo "Checking stats after request..." && kubectl exec $POD_NAME -c istio-proxy -- curl -s localhost:15000/clusters | grep "outbound|9080||\*\.svc\.cluster\.local" | grep -E "rq_total|rq_success"

Making test request...
HTTP 200
Checking stats after request...
outbound|9080||*.svc.cluster.local::10.96.35.238:9080::rq_success::1
outbound|9080||*.svc.cluster.local::10.96.35.238:9080::rq_total::1
```

注意：此用例中的 mTLS 需要证书具有 DNS SAN，因为 Envoy 的动态前向代理利用主机名执行自动 SAN 验证。

## 结论

随着通配符 `ServiceEntry` 支持和 `DYNAMIC_DNS` 解析的引入，Istio sidecar 代理现在可以直接处理发往通配符域名的 HTTP 和 TLS 出站流量。这实现了更简单的配置和更直接的请求路径，通过消除中间出口网关跳转降低了延迟，同时仍保留了现有的安全和策略控制。