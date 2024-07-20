
<!--
title: Istio从A到Y
cover: https://a-cup-of.coffee/blog/istio/cover.png
-->

Istio 是一款开源服务网格，允许您连接、保护、控制和观察应用程序的服务。我们将了解如何安装 Istio，以及如何使用它来保护和监控我们的服务。

> 译自 [Istio from A to Y](https://a-cup-of.coffee/blog/istio/)，作者 Quentin JOLY。

当你开始使用 Kubernetes 时，你很快就会意识到管理服务之间的通信并不简单。一旦流量通过 Ingress，你唯一能做的事情就是检查 Pod 日志，这既不实用也不高效。

这就是服务网格诞生的原因。它们允许你管理服务之间的通信，安全和监控交换，以及控制流量。本页面的目标是向你介绍 Istio，一个开源服务网格。

让我们一起探索 Istio，如何安装它，以及如何在喝一杯好咖啡的同时使用它。

但在我们开始之前，让我们先解释一下什么是服务网格。

## 什么是服务网格？

服务网格是一个基础设施层，允许你管理应用程序服务之间的通信。

简而言之：服务网格集成到由多个子应用程序（例如微服务）组成的应用程序的基础设施中，以添加功能。

在之前的一篇文章中，我介绍了 [Consul](https://a-cup-of.coffee/blog/consul/)，它可以作为基于 [Envoy](https://www.envoyproxy.io/) 的 sidecar 的服务网格使用。

![](https://a-cup-of.coffee/blog/istio/_resources/ServiceMeshdrawio.drawio.png)

在上面的示例中，每个程序都需要访问另一个程序，UI 访问身份验证和后端，后端访问存储和排队服务，最后：消费者访问排队服务。

有了这种方案，就会出现一些问题：

- 如何允许/拒绝两个服务之间的交换？
- 如何保护服务之间的交换？
- 可观测性如何？

例如，如果我们希望 UI 访问后端但不访问存储，我们该怎么做？或者如果我们希望后端访问存储但不访问 UI？

一种可能性是使用 NetworkPolicies，如果我们的 CNI 支持，但这不允许管理第 7 层交互（HTTP、gRPC 等）*除了 Cilium*。具体来说，我无法限制对特定路由（`/api`、`/endpoint/v3/ping`）或请求类型（GET、POST 等）的访问。

这就是像 Istio（或 Consul）这样的服务网格发挥作用的地方。

> 服务网格如何管理服务之间的交换？

服务网格使用代理来拦截服务之间的请求。它们充当中间人，通过在通信上添加一层控制来实现。

这有点像 Web 应用程序的 WAF（Web 应用程序防火墙）。每个应用程序将拥有自己的“路由器”，它将把传入和传出的请求重定向到目标服务的代理。

因此，以下是带有服务网格的图表：

![](https://a-cup-of.coffee/blog/istio/_resources/ServiceMeshdrawioEnvoy.drawio.png)

每次应用程序尝试与另一个服务通信时，代理都会拦截请求并将其重定向到目标服务的代理。

## 为什么使用服务网格？

当你只有 2-3 个应用程序时，服务网格可能看起来没有必要。但一旦你开始拥有多个服务、多个团队、多个集群，服务网格就会很快变得实用。

你可以通过信任服务的身份而不是 IP 地址或 DNS 名称（它们很容易被欺骗）来允许不同的服务以安全和受控的方式相互通信。

## 那 Istio 呢？

Istio 可用作 Kubernetes 集群中的服务网格。事实上，它满足了上面提到的需求：保护交换、控制流量和监控交换。

它是一个完全开源的项目，于 2022 年 9 月 30 日加入 CNCF（云原生计算基金会），并于 2023 年 7 月 12 日成为孵化项目。

我们将在本文后面有机会更多地讨论 Istio 的架构、组件和功能。

## 我的实验室环境

对于这个实验室，我使用了一个具有 3 个节点（1 个主节点，2 个工作节点）的 Kubernetes 集群，并使用 Talos 和 **Flannel** 作为 CNI（通常，我更喜欢 Cilium，但我与 Istio 的某个功能存在不兼容性，我将在后面讨论）。

以下是使用 [talhelper](https://a-cup-of.coffee/blog/talos/#using-talhelper) 为我的集群配置的配置。请随时查看 [我关于 Talos 的文章](https://a-cup-of.coffee/blog/talos/)，以获取有关其安装的更多信息。

**Talhelper 配置**

```yaml
---
clusterName: istio-cluster
talosVersion: v1.7.4
kubernetesVersion: v1.29.1
endpoint: https://192.168.128.27:6443
allowSchedulingOnMasters: true
cniConfig:
  name: flannel
patches:
  - |-
    - op: add
      path: /cluster/discovery/enabled
      value: false
    - op: replace
      path: /machine/network/kubespan
      value:
        enabled: false
    - op: add
      path: /machine/kubelet/extraArgs
      value:
        rotate-server-certificates: true
    - op: add
      path: /machine/files
      value:
      - content: |
          [metrics]
            address = "0.0.0.0:11234"
        path: /var/cri/conf.d/metrics.toml
        op: create
nodes:
  - hostname: controlplane
    ipAddress: 192.168.128.27
    controlPlane: true
    arch: amd64
    installDisk: /dev/sda
  - hostname: worker-1
    ipAddress: 192.168.128.28
    controlPlane: false
    arch: amd64
    installDisk: /dev/sda
  - hostname: worker-2
    ipAddress: 192.168.128.30
    controlPlane: false
    arch: amd64
    installDisk: /dev/sda
controlPlane:
  schematic:
    customization:
      systemExtensions:
        officialExtensions:
         - siderolabs/qemu-guest-agent
         - siderolabs/iscsi-tools
worker:
  schematic:
    customization:
      systemExtensions:
        officialExtensions:
         - siderolabs/qemu-guest-agent
         - siderolabs/iscsi-tools
```

我们还需要一个指标服务器才能让 Istio 的 HPA（水平 Pod 自动扩缩器）正常工作。对此，我已经部署了以下清单，分别为 kubelet 部署指标服务器和证书批准者。

```
kubectl apply -f https://raw.githubusercontent.com/alex1989hu/kubelet-serving-cert-approver/main/deploy/standalone-install.yaml
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

一如既往，务必小心直接在网上应用的清单，务必在应用之前仔细阅读它们。

## 安装 Istioctl

Istioctl 是管理 Istio 的命令行工具。它允许您部署、验证组件的状态、通过清单注入 Sidecar，以及执行更多操作。

安装 Istioctl 的最简单方法是使用 Istio 提供的脚本（它会下载最新版本），或者直接从 Istio 版本页面中检索二进制文件。

```bash
curl -L https://istio.io/downloadIstio | sh -
```

> 可以使用 ISTIO_VERSION 环境变量和目标架构 TARGET_ARCH 指定要安装的版本。
> 
> curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.22.0 TARGET_ARCH=x86_64 sh -

当然，尽量避免下载脚本并在不阅读的情况下运行它们。另一个解决方案是下载二进制文件本身。

NixOS 包也可用于安装 Istioctl。

```
nix-env -iA nixpkgs.istioctl # via nixpkgs
nix-env -iA nixos.istioctl # via nixos
```

现在，我们已具备在 Kubernetes 集群上安装 Istio 所需的一切内容。

## Istio Profile

配置文件在将Istio安装到我们的集群之前，选择一个配置文件非常重要。配置文件是一个预定义的Istio配置，它将确定要安装的组件、默认配置和已启用的功能。

Istio有几个版本，每个版本都有其自己的特点：

```
$ istioctl profile list
Istio configuration profiles:
    ambient
    default
    demo
    empty
    minimal
    openshift
    openshift-ambient
    preview
    remote
    stable
```

若要查看配置文件，可以使用命令 istioctl profile dump <profile>。

例如，可以使用以下命令查看默认配置文件：

```
istioctl profile dump default
```

以下是它的价值：

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  components:
    base:
      enabled: true
    egressGateways:
    - enabled: false
      name: istio-egressgateway
    ingressGateways:
    - enabled: true
      name: istio-ingressgateway
    pilot:
      enabled: true
  hub: docker.io/istio
  profile: default
  tag: 1.22.1
  values:
    defaultRevision: ""
    gateways:
      istio-egressgateway: {}
      istio-ingressgateway: {}
    global:
      configValidation: true
      istioNamespace: istio-system
```

若要比较两个配置文件，可以使用命令 istioctl profile diff <profile1> <profile2>。

若要比较默认配置文件和 demo 配置文件，可以使用以下命令：

```
istioctl profile diff default demo
```

这将显示两个配置文件之间的差异：

```yaml
apiVersion: install.istio.io/v1alpha1
 kind: IstioOperator
 metadata:
   creationTimestamp: null
   namespace: istio-system
 spec:
   components:
     base:
       enabled: true
     egressGateways:
-    - enabled: false
+    - enabled: true
       name: istio-egressgateway
     ingressGateways:
     - enabled: true
       name: istio-ingressgateway
     pilot:
       enabled: true
   hub: docker.io/istio
   profile: default
   tag: 1.22.1
   values:
     defaultRevision: ""
     gateways:
       istio-egressgateway: {}
       istio-ingressgateway: {}
     global:
       configValidation: true
       istioNamespace: istio-system
+    profile: demo
```

可以自定义一个配置文件，命令为 istioctl profile dump <profile> > myprofile.yaml，修改 myprofile.yaml 文件，添加或移除组件。

在这个练习中，我们主要使用 demo 配置文件，这是一个已启用所有稳定 Istio 功能的完整配置文件。

## 安装 Istio

要在 Kubernetes 集群上安装 Istio，我们将使用 istioctl install 命令，后跟配置文件或一个配置文件。

要使用配置文件：

```bash
istioctl install --set profile=demo
```

用法：使用配置文件：

```bash
istioctl install -f myprofile.yaml
```

所选配置文件将生成安装 Istio 和根据配置文件规范配置 Istio 所需的清单文件（当然也可以使用 Helm，但此方法似乎并非推荐的最佳方法）。

> 就这样吗？

嗯，是的。然后 Istio 将通过创建一个 istio-system 命名空间并部署必要的组件安装在 Kubernetes 集群上。

但是，它还没有生效，并且尚未将代理注入到 Pods 中。为此，我们需要启用所需命名空间中的 Istio 自动注入。我们稍后会讨论这个问题。

## 我们的测试应用程序：Bookinfo

我们将使用 Istio 提供的“Bookinfo”测试应用程序。它是一个由多个微服务组成的应用程序，将成为测试此服务网格的良好示例。

![](https://a-cup-of.coffee/blog/istio/_resources/bookinfo.png)

```
$ kubectl apply -n default -f https://raw.githubusercontent.com/istio/istio/release-1.22/samples/bookinfo/platform/kube/bookinfo.yaml
```

Bookinfo 应用程序现在已部署到我们的 Kubernetes 集群中。我们可以使用命令 `kubectl get-all -n default`
（*krew 插件*）检查已部署的内容。

```
$ kubectl get-all -n default
NAME NAMESPACE AGE
serviceaccount/bookinfo-details default 4m15s
serviceaccount/bookinfo-productpage default 4m9s
serviceaccount/bookinfo-ratings default 4m14s
serviceaccount/bookinfo-reviews default 4m12s
service/details default 4m15s
service/kubernetes default 15h
service/productpage default 4m10s
service/ratings default 4m14s
service/reviews default 4m13s
deployment.apps/details-v1 default 4m14s
deployment.apps/productpage-v1 default 4m8s
deployment.apps/ratings-v1 default 4m13s
deployment.apps/reviews-v1 default 4m11s
deployment.apps/reviews-v2 default 4m11s
deployment.apps/reviews-v3 default 4m11s
```

现在让我们尝试访问 Bookinfo 应用程序。为此，我们将使用端口转发从本地机器访问它。

```
kubectl port-forward svc/productpage 9080:9080 -n default
```

接下来，打开浏览器并访问 URL `http://localhost:9080/productpage`
。

![](https://a-cup-of.coffee/blog/istio/_resources/index_bookinfo.png)

点击“普通用户”按钮，应该会出现类似于此页面的页面：

![](https://a-cup-of.coffee/blog/istio/_resources/55139e6424e5d54bbd7ea49327ae4492.png)

> 但是，具体来说，Bookinfo 应用程序做了什么？在什么情况下使用每个微服务？

Bookinfo 应用程序中有 4 个微服务：

- **productpage**: 应用程序的前端服务。它调用 details 和 reviews 服务来显示页面内容。
- **details**: 包含书籍详细信息的服务。它不调用任何其他服务。
- **reviews**: 包含书籍评论的服务。它调用 ratings 服务来获取评分。
- **ratings**: 包含评论评分的服务。它不调用任何其他服务。

![](https://a-cup-of.coffee/blog/istio/_resources/services-on-bookinfo.png)

通过多次刷新页面，我们可以看到“评论”会根据使用的“reviews”服务版本而改变。实际上，有 3 个版本：

**版本 1**: 没有评分。

![](https://a-cup-of.coffee/blog/istio/_resources/v1.png)

**版本 2**: 带有黑色星星的评分。

![](https://a-cup-of.coffee/blog/istio/_resources/v2.png)

**版本 3**: 带有红色星星的评分。

![](https://a-cup-of.coffee/blog/istio/_resources/v3.png)

那么，如何管理“reviews”版本的分配呢？它是通过 Kubernetes 服务（使用 ClusterIP 类型服务）完成的，该服务将以“轮询”模式将请求重定向到“reviews”服务的 Pod。

现在，我们将启用 Istio 边车的注入。这可以通过 3 种方式完成：

- 通过在部署创建的 Pod 中注入标签：
```
kubectl patch deployment -n default productpage-v1 -p '{"spec": {"template": {"metadata": {"labels": {"sidecar.istio.io/inject": "true"}}}}}'
```

- 通过在部署之前修补清单文件（使用
`istioctl kube-inject`
，它将在清单文件中添加边车）：
```
wget https://raw.githubusercontent.com/istio/istio/release-1.22/samples/bookinfo/platform/kube/bookinfo.yaml
istioctl kube-inject -f bookinfo.yaml | kubectl apply -n default -f -
```

- 通过在命名空间中启用自动注入并重新部署 Pod：
```
kubectl label namespace default istio-injection=enabled
kubectl rollout restart deployment -n default details-v1 productpage-v1 ratings-v1 reviews-v1 reviews-v2 reviews-v3
```

无论选择哪种选项，Istio 边车都将被注入到 Bookinfo 应用程序的 Pod 中。您可以使用命令 `kubectl get pods -n default` 验证边车是否已注入。

```
$ kubectl get pods
NAME READY STATUS RESTARTS AGE
details-v1-64b7b7dd99-ctqd4 2/2 Running 0 118s
productpage-v1-6bc7f5c4c6-tsxdt 2/2 Running 0 114s
ratings-v1-c54575675-cq8bv 2/2 Running 0 118s
reviews-v1-76bf7c9d86-zbvts 2/2 Running 0 117s
reviews-v2-bb7869c75-n7rb5 2/2 Running 0 116s
reviews-v3-5f978f677b-2bqw5 2/2 Running 0 116s
```

每个 Pod 现在都有一个 Istio 边车 âµ，它将拦截传入和传出的请求。

要获取有关此方面的更多信息，可以使用 `istioctl analyze` 和 `istioctl proxy-status` 命令，它们将分别检查 Istio 配置是否正确以及代理是否处于活动状态。

```
$ istioctl analyze
✔ No validation issues found when analyzing namespace: default.
$ istioctl proxy-status
NAME                                                   CLUSTER        CDS        LDS        EDS        RDS          ECDS         ISTIOD                      VERSION
details-v1-7b6fb77db6-bwv5b.default                    Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-8596844f7d-z5rgl     1.21.0
istio-egressgateway-b569895b5-ppk8f.istio-system       Kubernetes     SYNCED     SYNCED     SYNCED     NOT SENT     NOT SENT     istiod-8596844f7d-z5rgl     1.21.0
istio-ingressgateway-694c4b4d85-78f95.istio-system     Kubernetes     SYNCED     SYNCED     SYNCED     NOT SENT     NOT SENT     istiod-8596844f7d-z5rgl     1.21.0
productpage-v1-68dfd95669-qr69h.default                Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-8596844f7d-z5rgl     1.21.0
ratings-v1-6b47557bbb-cr6k9.default                    Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-8596844f7d-z5rgl     1.21.0
reviews-v1-dd46dd5f-dkkkb.default                      Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-8596844f7d-z5rgl     1.21.0
reviews-v2-5b65c4bdb-76pd4.default                     Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-8596844f7d-z5rgl     1.21.0
reviews-v3-685dd59d69-tmzlf.default                    Kubernetes     SYNCED     SYNCED     SYNCED     SYNCED       NOT SENT     istiod-8596844f7d-z5rgl     1.21.0
```

*请不要关注 stio-egressgateway 和 istio-ingressgateway pod，它们与 Bookinfo 应用程序无关。*

但在我们继续之前，让我们配备一些工具来帮助我们使用 Istio。

## 我们的可观测性套件

Istio 对那些拒绝充分装备自己的人来说是相当不宽容的。因此，我们将发现一些工具来帮助我们了解集群中发生了什么。

### Kiali

此工具对于可视化 pod 之间的交换 **至关重要**，它直接与 Istio 交互以检索代理数据。它将是我们验证应用程序正常运行的主要工具。

它能够：

- 可视化服务及其之间的交换。
- 验证/修改我们的 Istio 配置。
- 获取服务指标。

它是一款真正的 Istio 万能工具。

要安装 Kiali，我们可以使用 Istio 存储库中提供的清单。部署后，我们可以使用端口转发访问 Kiali Web 界面。

```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/addons/kiali.yaml
istioctl dashboard kiali
```

*注意：istioctl dashboard kiali 只是对 Kiali 服务进行端口转发，您也可以使用 kubectl port-forward svc/kiali 20001:20001 -n istio-system。*

> 提示：请注意，该清单只部署了 Kiali 的演示版本（没有身份验证），对于生产环境，我建议您参考 [官方文档](https://kiali.io/docs/installation/) 以更可持续的方式配置 Kiali，并根据您的需求进行定制。

让我们生成一些流量来查看 Kiali 可以向我们展示什么。

```
kubectl port-forward -n default svc/productpage 9080:9080 >/dev/null &
watch -n 1 curl -s http://localhost:9080/productpage -I
```

在“流量图（Traffic Graph）”部分，我们可以看到服务之间的交换（“ratings”服务丢失了，但这很正常）。

![](https://a-cup-of.coffee/blog/istio/_resources/kiali-b4-vs.png)

此页面可能是您最常用来调试应用程序的页面。在本文的其余部分，我将广泛引用它。

### Jaeger & Zipkin

Zipkin 和 Jaeger 是跟踪工具，允许您跟踪请求通过各个服务的路径。它们允许您查看每个服务的响应时间、错误和交互延迟。

这类似于 OpenTelemetry（我还没有测试过），对于了解应用程序的性能以及查看哪个服务是瓶颈非常有用。

要安装 Jaeger，我们可以使用 Istio 存储库中提供的清单。部署后，我们可以使用端口转发访问 Jaeger Web 界面。

```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/addons/jaeger.yaml
istioctl dashboard jaeger
```

从 Jaeger，我可以看到我的请求的跟踪，并查看每个服务的响应时间。

![](https://a-cup-of.coffee/blog/istio/_resources/jaeger.png)

让我们获取“productpage”服务的跟踪（Bookinfo 应用程序的入口点），并查看跟踪的详细信息：

![](https://a-cup-of.coffee/blog/istio/_resources/trace-productpage.png)

![](https://a-cup-of.coffee/blog/istio/_resources/details-trace.png)

当然，我可以查看每个服务的详细信息，并查看每个服务的响应时间。

![](https://a-cup-of.coffee/blog/istio/_resources/trace-labels.png)

简而言之，Jaeger 是一个非常有用的工具，可以查看请求的详细信息，并获得有关应用程序性能的更多信息。

Kiali 更侧重于“概述”，而 Jaeger 更侧重于“细节”。

Bookinfo 应用程序的架构图：

![](https://a-cup-of.coffee/blog/istio/_resources/Schema-jaeger.png)

一个典型的用例是查找失败请求的跟踪，以了解原因。因此，我可以查找失败请求的跟踪，并查看哪个服务返回了错误。

![](https://a-cup-of.coffee/blog/istio/_resources/404-jaeger.png)

![](https://a-cup-of.coffee/blog/istio/_resources/404-trace.png)

*在这种情况下，前端只是返回了 404 错误，我们将在后面看到更有趣的案例。*

### Prometheus & Grafana

关于指标的问题，Istio 与 Prometheus（它链接到 Grafana 以进行指标可视化）完美集成。通过使用 Istio 提供的清单文件，可以部署 Prometheus 和预先配置的 Grafana 仪表盘来显示指标。

```
kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/addons/grafana.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/master/samples/addons/prometheus.yaml
istioctl dashboard grafana
```

因此，我们有可视化仪表盘，以便查看：

- Istio 使用的资源。
- 服务之间的响应时间。
- 请求的状态 (200、404 等)。
- 服务使用的带宽。

![](https://a-cup-of.coffee/blog/istio/_resources/grafana-dashboard.png)

现在我们准备好了，我们可以开始使用 Istio 了。

## 公开我们的应用程序

目前，流量只通过 sidecar 传输，Envoy 没有执行任何操作（没有过滤、没有控制、没有安全）。我们将进行设置，以便 Istio 可以执行其工作。

我们将看到的第一个 CRD（自定义资源定义）是 VirtualService。VirtualService 是一个 Istio 对象，允许您为 Kubernetes 服务配置路由规则。

VirtualService 创建的路由将传播到所有 sidecar，然后 sidecar 将根据定义的规则重定向流量。

例如，我将为 Bookinfo 应用程序的“details”服务创建第一个 VirtualService。

```yaml
kind: VirtualService
apiVersion: networking.istio.io/v1beta1
metadata:
  name: details-vs
  namespace: default
spec:
  hosts:
  - details # valid for details and details.default.svc.cluster.local
  http:
  - route:
    - destination:
        host: details
```

从 Kiali 中，我们可以看到“details”有一个新的图标，表示该服务现在由 VirtualService 管理。

![](https://a-cup-of.coffee/blog/istio/_resources/vs-details.png)

此 VirtualService 添加了 2 个被动功能：

- 如果请求失败，Envoy 将自动重试最多 3 次。
- mTLS 在 PERMISSIVE 模式下启用（HTTP 仍然可用）。

*我们将在稍后讨论 mTLS（并解释它是什么）*。

现在，让我们只通过 VirtualService 使“productpage”服务（Bookinfo 应用程序的前端）可访问。我还会借此机会限制对“/”路由（网站根目录）的访问，该路由包含一个用户不应查看的页面。

![](https://a-cup-of.coffee/blog/istio/_resources/index_bookinfo.png)

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: bookinfo
spec:
  hosts:
  - "productpage"
  http:
  - match:
    - uri:
        exact: /productpage
    - uri:
        prefix: /static
    - uri:
        exact: /login
    - uri:
        exact: /logout
    - uri:
        prefix: /api/v1/products
  route:
  - destination:
      host: productpage
```

使用我们的 `kubectl port-forward`，我们无法测试 VirtualService 带来的限制。为此，让我们直接从集群中的 pod 发出请求。

```
$ kubectl exec deployments/ratings-v1 -c ratings -- curl http://productpage:9080/ -I -s
HTTP/1.1 404 Not Found
date: Sat, 22 Jun 2024 09:25:11 GMT
server: envoy
transfer-encoding: chunked

$ kubectl exec deployments/ratings-v1 -c ratings -- curl http://productpage:9080/productpage -I -s
HTTP/1.1 200 OK
server: envoy
date: Sat, 22 Jun 2024 09:25:55 GMT
content-type: text/html; charset=utf-8
content-length: 5293
vary: Cookie
x-envoy-upstream-service-time: 20
```

> 注意：`x-envoy-upstream-service-time` 标头是由 Envoy 添加的标头，指示目标服务的响应时间。
> 
> 您可以通过修改 VirtualService 来删除它，使其不显示它，方法是添加以下代码：

```yaml
options:
  stagedTransformations:
    early:
      responseTransforms:
      - responseTransformation:
          transformationTemplate:
            dynamicMetadataValues:
            - metadataNamespace: body-logging
              key: upstream-service-time
              value:
                text: '{{ header("x-envoy-upstream-service-time") }}'
            headers:
              x-envoy-upstream-service-time:
                text: ''
```

我们可以看到路由“/”返回 404 错误（在 VirtualService 之前不是这种情况），而路由“/productpage”正确地返回 Bookinfo 应用程序的主页。

现在……如果我们能够在不通过端口转发的情况下访问应用程序，那会更好，不是吗？

### 网关

网关等同于 Ingress。区别在于 Ingress 直接指向服务，而网关允许不同的功能以不同的方式或通过更多监控来重定向流量。

网关是传入流量进入集群的入口点。就像 Ingress 与 IngressController 一样，网关需要一个 GatewayController 来运行，该控制器由 `istio-system` 命名空间中的 pod `istio-ingressgateway` 管理。

> 警告：请注意，`istio-ingressgateway` 组件不会与 Istio 系统安装（它与 `demo` 配置文件一起安装）。如果您使用配置文件而不是配置文件，请确保 `istio-ingressgateway` 组件已启用，如下面的示例所示：

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  components:
    base:
      enabled: true
    ingressGateways:             #
    - enabled: true              # This is the GatewayController
      name: istio-ingressgateway #
    pilot:
      enabled: true
  hub: docker.io/istio
  tag: 1.21.0
  values:
    defaultRevision: ""
    gateways:
      istio-egressgateway: {}
      istio-ingressgateway: {}
    global:
      configValidation: true
      istioNamespace: istio-system
    profile: a-cup-of-coffee
```

由于我没有负载均衡器，我将使用 NodePort 来访问网关：

```
kubectl patch service istio-ingressgateway -n istio-system --type='json' -p='[{"op": "replace", "path": "/spec/type", "value":"NodePort"}]'
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
export INGRESS_HOST=$(kubectl get po -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].status.hostIP}')
echo $INGRESS_HOST:$INGRESS_PORT # 192.168.128.30:30492
```

*请记住这些变量，我们将会经常用到它们。*

现在我们有了 Istio 网关控制器（ingress-gateway）的入口点！让我们尝试向网关发送第一个请求。

```
curl -s $INGRESS_HOST:$INGRESS_PORT/productpage -I -v
*   Trying 192.168.128.30:30492...
* connect to 192.168.128.30 port 30492 failed: Connexion refusée
* Failed to connect to 192.168.128.30 port 30492 after 105 ms: Connexion refusée
* Closing connection 0
```

啊！我确信我已经正确地暴露了网关，并且在正确的网络中。为什么连接被拒绝？

原因：如果没有任何网关与我们的网关控制器关联，那么流量将被拒绝。让我们从创建网关对象开始。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: bookinfo-gateway
spec:
  selector:
    istio: ingressgateway # use istio default controller
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*" # It should match a domain-wildcard (ex: '*.istio.a-cup-of.coffee'), but in dev env, we can use a wildcard
```

让我们尝试访问网关：

```
curl -s $INGRESS_HOST:$INGRESS_PORT -I

HTTP/1.1 404 Not Found
date: Sat, 22 Jun 2024 09:20:20 GMT
server: istio-envoy
transfer-encoding: chunked
```

然后让我们尝试通过“/productpage”路由（由“productpage”虚拟服务使用）访问网关：

```
$ curl -s $INGRESS_HOST:$INGRESS_PORT/productpage -I
HTTP/1.1 404 Not Found
date: Sat, 22 Jun 2024 09:52:17 GMT
server: istio-envoy
transfer-encoding: chunked
```

为什么是 404？因为“productpage”虚拟服务尚未与网关关联。我们马上就会处理它。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: bookinfo
spec:
  hosts:
  - "productpage"
  gateways:              # We add the Gateway
  - bookinfo-gateway     #
  http:
  - match:
    - uri:
        exact: /productpage
    - uri:
        prefix: /static
    - uri:
        exact: /login
    - uri:
        exact: /logout
    - uri:
        prefix: /api/v1/products
    route:
    - destination:
        host: productpage
```

让我们再试一次？这次是正确的！

```
$ curl -s $INGRESS_HOST:$INGRESS_PORT/productpage -I
HTTP/1.1 404 Not Found
date: Sat, 22 Jun 2024 10:29:52 GMT
server: istio-envoy
transfer-encoding: chunked
```

仍然是 404？

- 虚拟服务配置正确且正常工作。
- 网关配置正确，并与正确的虚拟服务关联。
- 网关控制器处于活动状态。

你们中的一些人可能已经猜到了导致 404 的原因。事实上，“productpage”服务只能通过“productpage.default.svc.cluster.local”域名访问。

```
$ curl  -H "Host: productpage.default.svc.cluster.local" $INGRESS_HOST:$INGRESS_PORT/productpage -I
HTTP/1.1 200 OK
content-type: text/html; charset=utf-8
content-length: 5290
vary: Cookie
x-envoy-upstream-service-time: 27
```

> 提示：在虚拟服务中，“hosts”字段必须与服务可访问的域名匹配。当主机不是完全限定域名（FQDN）时，Istio 将自动使用命名空间和集群域名对其进行补充。
> 
> 例如，如果我在“hosts”字段中放置“productpage”，Istio 将自动将其补充为 `productpage.default.svc.cluster.local`。
>
> 因此，最好在“hosts”字段中指定完整的域名（`productpage.default.svc.cluster.local`
）以避免任何混淆。

胜利，我们现在可以通过网关访问 Bookinfo 应用程序！

从 Kiali 中，我们可以看到：

![](https://a-cup-of.coffee/blog/istio/_resources/after-ingress-kiali.png)

> 提示：在我们的开发环境中，我们可以对虚拟服务的“hosts”字段使用通配符。这允许将传入流量重定向到服务，而无需指定特定的域名。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: bookinfo
spec:
  hosts:
  - "*"
  gateways:
  - bookinfo-gateway
  http:
  - match:
    - uri:
        exact: /productpage
    - uri:
        prefix: /static
    - uri:
        exact: /login
    - uri:
        exact: /logout
    - uri:
        prefix: /api/v1/products
    route:
    - destination:
        host: productpage
```

现在，让我们解决“reviews”应用程序，它有点特殊。

### 使用 DestinationRules 进行版本管理

“reviews” 服务有 3 个不同的版本。每个版本可以通过不同的标签访问（app=reviews，version=v1，v2，v3）。

该服务（以 Kubernetes 的方式）被配置为将流量重定向到带有标签 `app=reviews` 的应用程序。但是我们如何将流量重定向到特定版本呢？

答案是：DestinationRules，一个 Istio 对象，允许在流量被 VirtualService 路由后应用一组处理。

例如，DestinationRule 可以：

- 修改负载均衡模式。
- 创建断路器。
- 配置 mTLS。

当然，最重要的是：管理应用程序的“子集”以区分同一服务的不同版本。

以下是我们的“reviews”服务的 DestinationRule 的示例：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews
spec:
  host: reviews
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
  - name: v3
    labels:
      version: v3
```

每个子集都根据每个 pod 的 `version` 标签被赋予一个名称。然后，我们可以使用相应的子集将流量重定向到特定版本。

## 使用 Istio 进行流量管理

现在我们有了 Gateway 并配置了 VirtualServices 和 DestinationRules，我们可以使用 Envoy 代理并发现 Istio 的一些功能。

### 流量切换

流量切换是 Istio 的一项功能，允许将流量重定向到服务的特定版本。这允许测试应用程序的新版本，而不会影响用户。

为此，我们将使用 VirtualService 将流量重定向到“reviews”服务的特定子集。

```
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - route:
    - destination:
        host: reviews
        subset: v1
```

通过多次重新加载页面，我们可以看到“Reviews”始终相同（没有评分）。这是正常的，VirtualService 将流量重定向到“reviews”的版本 1。

让我们更进一步，将“reviews”的版本 2 和 3 添加到 VirtualService 中，并使用一个新概念：权重。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    - reviews
  http:
    - route:
        - destination:
            host: reviews
            subset: v1
          weight: 15
        - destination:
            host: reviews
            subset: v2
          weight: 25
        - destination:
            host: reviews
            subset: v3
          weight: 60
```

总的来说，流量将按以下方式分配：

- 15% 的请求将被重定向到版本 1，
- 25% 到版本 2，
- 60% 到版本 3。

为了验证流量是否正确分配，我们可以循环生成请求，并直接从 Kiali 检查结果。

```
while true; do curl $INGRESS_HOST:$INGRESS_PORT/productpage -s -I ; done
```

![](https://a-cup-of.coffee/blog/istio/_resources/traffic-shifting.png)

现在，我们可以看到流量在“reviews”的不同版本之间分配良好：版本 3 使用最多（60% 的请求），而版本 1 使用最少（15% 的请求）。

这可以与金丝雀部署（或“金丝雀部署”）进行比较，在金丝雀部署中，应用程序的新版本被部署并测试在一小部分用户身上，然后再部署到所有人。然后，我们可以逐步将流量重定向到新版本，并根据日志和指标（借助 Kiali、Jaeger 和 Grafana）控制后者的采用率。

在我们的金丝雀部署中，我们将流量随机重定向到“reviews”服务的不同版本，但为什么不根据其他标准重定向呢？

### A/B 测试

A/B 测试是一种技术，它根据某些标准（例如用户的国家、设备类型等）将流量重定向到应用程序的不同版本。它对于在不影响其他用户的情况下，在特定用户组上测试应用程序的新版本非常有用。

例如，我们将为用户“quentin”将流量重定向到“reviews”服务的版本 3，而为其他用户重定向到版本 2。请注意，当我们连接到 bookinfo 应用程序时，它将创建一个包含用户名 的会话 cookie。productpage 应用程序将通过“end-user”标头将此用户名传输到其他应用程序（reviews、details）。我们将使用此标头来重定向流量。

如果您想亲自验证这一点，我建议您查看 Productpage 应用程序的 `getForwardHeaders()` 函数 [此处](https://github.com/istio/istio/blob/master/samples/bookinfo/src/productpage/productpage.py#L133-L134)。

让我们从使用用户名“quentin”进行身份验证开始（密码无关紧要，输入任何内容）：

![](https://a-cup-of.coffee/blog/istio/_resources/login-to-quentin.png)

在页面标题中，我们可以看到我们使用哪个用户名连接：

然后，让我们修改 VirtualService “reviews” 如下：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    - reviews
  http:
  - match:
    - headers:
        end-user:
          exact: quentin
    route:
    - destination:
        host: reviews
        subset: v3
  - route:
    - destination:
        host: reviews
        subset: v2
```

此配置可以翻译如下：

- 如果“end-user”头等于“quentin”，则将流量重定向到“reviews”的版本 3。
- 否则，将流量重定向到版本 2。

在未进行身份验证的情况下，我们可以看到流量被重定向到版本 2：

![](https://a-cup-of.coffee/blog/istio/_resources/review-2.png)

如果我们使用用户名“quentin”进行身份验证，流量将被重定向到版本 3：

![](https://a-cup-of.coffee/blog/istio/_resources/55139e6424e5d54bbd7ea49327ae4492.png)

来自另一个用户（例如“alice”）的流量将被重定向到版本 2。

现在让我们测试 A/B 测试的另一种情况：根据用户是从移动设备还是计算机打开页面来将流量重定向到特定版本。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    - reviews
  http:
  - match:
    - headers:
        user-agent:
          regex: .*Mobile.*
    route:
    - destination:
        host: reviews
        subset: v3
  - route:
    - destination:
        host: reviews
        subset: v2
```

- 如果我没有指定 user-agent，流量将被重定向到版本 2。
```
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage -s | grep reviews-
<u>reviews-v2-5b65c4bdb-76pd4</u>
```
- 如果我指定一个包含“Mobile”的 user-agent，流量将被重定向到版本 3。
```
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage --user-agent "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.110 Mobile Safari/537.36" -s | grep reviews-
<u>reviews-v3-685dd59d69-tmzlf</u>
```

现在让我们看看 Istio 集成应用程序新版本的最后一个功能：“暗启动”。

### 暗启动（镜像）

暗启动是一种技术，它允许在不将新版本的响应发送给用户的情况下，与旧版本并行测试应用程序的新版本。

![](https://a-cup-of.coffee/blog/istio/_resources/Dark-launch.png)

因此，当用户打开页面时，流量将被重定向到应用程序的当前版本，但新版本也会并行调用。新版本的响应不会发送给用户，但管理员可以查看日志以查看应用程序是否在将来的部署中正确集成。

假设我们要从“reviews”服务的版本 2 过渡到版本 3，我们可以配置一个 VirtualService 进入“镜像”模式。这将使我们能够验证版本 3 应用程序是否能与当前请求正确配合。

*当然，“ratings”应用程序的性能会受到“镜像”模式的影响，因为每个请求都会被调用两次（一次针对版本 2，一次针对版本 3）。*
```
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - route:
    - destination:
        host: reviews
        subset: v2
    mirror:
      host: reviews
      subset: v3
```
以下是 Kiali 的架构图：

![](https://a-cup-of.coffee/blog/istio/_resources/mirror.png)

启用“镜像”模式后，我们需要分析日志以查看应用程序的新版本是否正常工作。为此，我们可以使用跟踪工具（Jaeger、Zipkin）和指标（Prometheus、Grafana）。

### 故障注入

现在我们能够使用安全带和吊带部署新版本，是时候看看 Istio 如何帮助我们测试应用程序的弹性了。

有一个功能允许将错误注入请求，以查看应用程序在发生错误时如何反应。这就是“故障注入”。

让我们以 Bookinfo 应用程序的“ratings”服务为目标。我们将对 30% 的请求注入 403（禁止）错误，以查看应用程序如何反应以及用户如何受到影响。

```
kind: VirtualService
apiVersion: networking.istio.io/v1beta1
metadata:
  name: ratings
  namespace: default
spec:
  hosts:
  - ratings
  http:
  - fault:
      abort:
        httpStatus: 403
      percentage:
        value: 30
    route:
    - destination:
        host: ratings
```

> 信息：要指定何时注入 403 错误，我们可以使用 `match`
字段来指定条件。在这里，只有当“end-user”头等于“testing-user”时，才会注入 403 错误。

```yaml
kind: VirtualService
apiVersion: networking.istio.io/v1beta1
metadata:
  name: ratings
  namespace: default
spec:
  hosts:
  - ratings
  http:
  - fault:
      abort:
        httpStatus: 403
        percentage:
          value: 30
    route:
      - destination:
          host: ratings
    match:
      - headers:
          end-user:
            exact: testing-user
  - route:
    - destination:
        host: ratings
```

使用上述配置，30% 的“ratings”服务请求将返回 403 错误：

![](https://a-cup-of.coffee/blog/istio/_resources/c17bb7d4cc0022c40e328bb3e704c959.png)

在 Kiali 中，请求被抛入“黑洞”（黑洞）。

![](https://a-cup-of.coffee/blog/istio/_resources/4db0624f7e92b4e0a251d8027287eb44.png)

### 延迟注入

除了注入错误，我们还可以向请求添加延迟，以查看应用程序在出现延迟时如何反应。

我将保留“ratings”服务，并以“details”服务为目标，在 50% 的请求中注入 7 秒的延迟。

```yaml
kind: VirtualService
apiVersion: networking.istio.io/v1beta1
metadata:
  name: details
  namespace: default
spec:
  hosts:
  - details
  http:
  - route:
    - destination:
        host: details
    fault:
      delay:
        fixedDelay: 7.000s
        percent: 50
```

好了，现在“details”服务的 50% 请求将经历 7 秒的延迟。让我们验证一下：

```
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage -s -w '\n* Response time: %{time_total}s\n' | grep 'Response time'
* Response time: 3.262570s
```

我们没有得到 7 秒的延迟，为什么？因为延迟是在“productpage”和“details”服务之间注入的，而我们的前端应用程序对“details”服务的请求有一个 [3 秒的超时](https://github.com/istio/istio/blob/master/samples/bookinfo/src/productpage/productpage.py#L337)。

然后让我们从 7 秒切换到 2 秒，看看延迟是否被考虑在内。

```
kubectl patch virtualservice details -n default --type='json' -p='[{"op": "replace", "path": "/spec/http/0/fault/delay/fixedDelay", "value": "2.000s"}]'
```

```
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage -s -w '\n* Response time: %{time_total}s\n' | grep 'Response time'
* Response time: 0.282223s
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage -s -w '\n* Response time: %{time_total}s\n' | grep 'Response time'
* Response time: 2.264027s
```

好了，2 秒的延迟被很好地观察到了 ð !

### 断路器

断路器是一种机制，当遇到一定数量的错误时，它允许停止对服务的请求。这有助于保护下游服务免受过载请求的影响，并减少延迟时间（通过避免超时，因为请求在到达下游服务之前就被停止了）。

```yaml
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: productpage
spec:
  host: productpage
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 1 # Maximum number of connections in http 1.1
      http:
        http2MaxRequests: 3 # Maximum number of connections in http 2
        maxRequestsPerConnection: 1 # Maximum number of requests per connection
```

有了这个配置，如果“productpage”服务在 HTTP/2 中收到超过 3 个请求，断路器将停止正在进行的请求并返回 503 错误（服务不可用）。因此，如果服务器收到太多请求，服务将不会崩溃，并将处理它可以处理的请求，而不会影响其他应用程序。

为了测试这一点，我们可以使用像 `fortio` 这样的基准测试工具向“productpage”发送大量请求。*(我们稍后将有机会谈论 fortio。)*

如果我们一次启动一个访问：

```
$ fortio load -c 1 -n 50 http://$INGRESS_HOST:$INGRESS_PORT/productpage
Connection time histogram (s) : count 1 avg 0.13487925 +/- 0 min 0.134879246 max 0.134879246 sum 0.134879246
# range, mid point, percentile, count
>= 0.134879 <= 0.134879 , 0.134879 , 100.00, 1
# target 50% 0.134879
# target 75% 0.134879
# target 90% 0.134879
# target 99% 0.134879
# target 99.9% 0.134879
Sockets used: 1 (for perfect keepalive, would be 1)
Uniform: false, Jitter: false, Catchup allowed: true
IP addresses distribution:
192.168.128.30:30492: 1
Code 200 : 50 (100.0 %)
Response Header Sizes : count 50 avg 188 +/- 0 min 188 max 188 sum 9400
Response Body/Total Sizes : count 50 avg 5399.12 +/- 271 min 4480 max 5481 sum 269956
All done 50 calls (plus 0 warmup) 162.183 ms avg, 6.2 qps
```

100% 的请求都成功了。现在，让我们用 4 个并发请求运行相同的测试：

```
$ fortio load -c 4 -n 50 http://$INGRESS_HOST:$INGRESS_PORT/productpage
Connection time histogram (s) : count 7 avg 0.1462682 +/- 0.02803 min 0.106653371 max 0.176468802 sum 1.02387742
# range, mid point, percentile, count
>= 0.106653 <= 0.12 , 0.113327 , 28.57, 2
> 0.12 <= 0.14 , 0.13 , 42.86, 1
> 0.14 <= 0.16 , 0.15 , 57.14, 1
> 0.16 <= 0.176469 , 0.168234 , 100.00, 3
# target 50% 0.15
# target 75% 0.166862
# target 90% 0.172626
# target 99% 0.176085
# target 99.9% 0.17643
Sockets used: 7 (for perfect keepalive, would be 4)
Uniform: false, Jitter: false, Catchup allowed: true
IP addresses distribution:
192.168.128.30:30492: 7
Code 200 : 46 (92.0 %)
Code 503 : 4 (8.0 %)
Response Header Sizes : count 50 avg 172.96 +/- 51 min 0 max 188 sum 8648
Response Body/Total Sizes : count 50 avg 5000.3 +/- 1421 min 247 max 5481 sum 250015
All done 50 calls (plus 0 warmup) 195.516 ms avg, 7.0 qps
```
我们可以看到，8% 的请求返回了 503 错误，这是断路器停止这些请求以防止“productpage”服务过载。

## Istio 中的安全性

我们已经谈了很多关于流量管理和错误处理，但是安全性呢？Istio 提供了广泛的功能来保护服务之间的交换，从证书管理到服务身份验证。

我建议我们深入研究这方面，看看 Istio 如何帮助我们保护我们的应用程序。

![](https://istio.io/latest/docs/concepts/security/arch-sec.svg)

### mTLS

我在本文开头简要提到了它，Istio 默认支持 mTLS（双向 TLS）来保护服务之间的交换。

![](https://a-cup-of.coffee/blog/istio/_resources/citadel.mtls.drawio_black.png)

每次 Envoy 与新服务通信时，它都会请求 **Istiod** 获取证书以验证交换。因此，由于 mTLS 的性质，发送方和接收方都可以相互验证。

默认情况下，Istio 中的 mTLS 以“宽松”模式启用。这意味着服务可以在 HTTP 或 HTTPS 中通信。

我们可以强制交换以“严格”模式进行，以便服务只能在 HTTPS 中通信。

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default-mtls
  namespace: default
spec:
  mtls:
    mode: STRICT
```

> 提示：与其强制默认命名空间的 mTLS，不如通过指定 `istio-system` 命名空间在整个集群范围内进行。

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default-mtls
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
```

启用“严格”模式后，我们可以重新启动服务以使 mTLS 生效。

```
kubectl rollout restart deployment -n default details-v1 productpage-v1 ratings-v1 reviews-v1 reviews-v2 reviews-v3
```

从 Kiali 中，我们可以看到 mTLS 已通过锁符号正确启用。

![](https://a-cup-of.coffee/blog/istio/_resources/mtls-kiali.png)

为了自己测试这一点，让我们使用 NodePort 将“productpage”服务暴露在集群外部（ClusterIP 服务不足）。

```
kubectl patch svc productpage -n default --type='json' -p='[{"op": "replace", "path": "/spec/type", "value": "NodePort"}]'
PRODUCTPAGE_PORT=$(kubectl get svc productpage -n default -o jsonpath='{.spec.ports[0].nodePort}')
PRODUCTPAGE_HOST=$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[0].address}')
echo $PRODUCTPAGE_HOST:$PRODUCTPAGE_PORT # 192.168.128.27:31447
```

现在，让我们尝试查看“productpage”证书：

```
$ openssl s_client -connect $PRODUCTPAGE_HOST:$PRODUCTPAGE_PORT < /dev/null 2>/dev/null | openssl x509 -noout -text
Certificate:
Data:
Signature Algorithm: sha256WithRSAEncryption
Issuer: O = cluster.local
Validity
Not Before: Jun 22 06:20:33 2024 GMT
Not After : Jun 23 06:22:33 2024 GMT
Subject:
Subject Public Key Info:
Public Key Algorithm: rsaEncryption
Public-Key: (2048 bit)
X509v3 extensions:
X509v3 Key Usage: critical
Digital Signature, Key Encipherment
X509v3 Extended Key Usage:
TLS Web Server Authentication, TLS Web Client Authentication
X509v3 Basic Constraints: critical
CA:FALSE
X509v3 Authority Key Identifier:
E5:BD:7C:B1:C3:CE:56:30:B1:9F:59:BE:97:E5:76:BD:6C:7B:D3:02
X509v3 Subject Alternative Name: critical
URI:spiffe://cluster.local/ns/default/sa/bookinfo-productpage
Signature Algorithm: sha256WithRSAEncryption
```

我们可以看到证书已由本地集群正确签名，并且持续时间有限（1 天）。

如果没有有效的证书，我们就无法与“productpage”服务通信：

```
$ curl $PRODUCTPAGE_HOST:$PRODUCTPAGE_PORT -v
* Recv failure: Connection reset by peer
* Closing connection 0
curl: (56) Recv failure: Connection reset by peer
```

### ACLs

现在让我们继续创建 ACL（访问控制列表）以根据某些条件允许或拒绝访问某些服务。

通常，ACL 可以基于以下几个条件：

- 命名空间（输入、输出）；
- 操作（GET、POST、PUT、DELETE）及其路径；
- 服务的标签。

其目的是允许某个应用程序公开某个路径或 HTTP 操作，并在不满足条件时拒绝访问。

为了实际演示这一点，我们将从拒绝“default”命名空间中的所有交换开始。

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
 name: allow-nothing
 namespace: default
spec: {}
```

现在，如果我们尝试访问“productpage”，我们将收到 403（禁止）错误：

```
curl $INGRESS_HOST:$INGRESS_PORT/productpage -v
* Trying 192.168.128.30:30492...
* Connected to 192.168.128.30 (192.168.128.30) port 30492 (#0)
> GET /productpage HTTP/1.1
< HTTP/1.1 403 Forbidden
< server: istio-envoy
< x-envoy-upstream-service-time: 0
<
* Connection #0 to host 192.168.128.30 left intact
```

Kiali 指示流量确实被阻止：

![](https://a-cup-of.coffee/blog/istio/_resources/kiali-blocked.png)

Jaeger 也是：

![](https://a-cup-of.coffee/blog/istio/_resources/jaeger-blocked.png)

为了重新授权访问“productpage”，我们可以创建一个新的 ACL 规则，允许对“productpage”服务执行不同的操作：

```
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  namespace: default
  name: allow-productpage
spec:
  selector:
    matchLabels:
      app: productpage
  action: ALLOW
  rules:
  - to:
    - operation:
        methods: ["GET"]
        paths:
        - "/logout"
        - "/static/*"
        - "/productpage"
        - "/api/v1/products"
    - operation:
        methods: ["POST"]
        paths: ["/login"]
```

不错，我们现在可以再次访问“productpage”了：

![](https://a-cup-of.coffee/blog/istio/_resources/productpageOK.png)

![](https://a-cup-of.coffee/blog/istio/_resources/a6e19e77fbeae1e5629f47e25c7b2044.png)

另一方面，其他服务仍然被阻止。别无选择，我们必须为每个服务创建 ACL 规则。

因此，让我们借此机会对它们进行身份验证，以防止任何应用程序与它不需要的容器通信。

### 通过 SA 进行身份验证

接下来，我们来谈谈服务认证。目标是允许一个服务使用 ServiceAccount 作为认证密钥与另一个服务通信。这样一来，只有拥有正确 ServiceAccount 的服务才能与授权的服务进行通信。

在本例中，我们将实现以下规则：

- “details” 必须可被 “productpage” 访问；
- “ratings” 必须可被 “reviews” 访问；
- “reviews” 必须可被 “productpage” 访问。

“bookinfo” 应用为每个服务提供了 ServiceAccount。以下是可用的 ServiceAccount：

```
$ kubectl get sa
NAME                   SECRETS   AGE
bookinfo-details       0         3d19h
bookinfo-productpage   0         3d19h
bookinfo-ratings       0         3d19h
bookinfo-reviews       0         3d19h
default                0         4d11h
```

首先，我们允许 “productpage” 访问 “details”。

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  namespace: default
  name: allow-details
spec:
  selector:
    matchLabels:
      app: details
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/default/sa/bookinfo-productpage"]
    to:
    - operation:
        methods: ["GET"]
        paths: ["/details/*"]
```

从 ProductPage，我们可以看到 “details” 信息正常显示：

![](https://a-cup-of.coffee/blog/istio/_resources/allow-details.png)

但是，如果我尝试从 “ratings” 访问 “details”，则会收到 403（禁止）错误：

```
$ kubectl exec deployments/ratings-v1 -c ratings -- curl -s http://details:9080/details/0
RBAC: access denied
```

![](https://a-cup-of.coffee/blog/istio/_resources/kiali-allow-details.png)

现在，我们来处理其他服务。以下是允许 “ratings” 和 “reviews” 的 ACL 规则：

```yaml
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  namespace: default
  name: allow-reviews
spec:
  selector:
    matchLabels:
      app: reviews
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/default/sa/bookinfo-productpage"]
    to:
    - operation:
        methods: ["GET"]
        paths: ["/reviews/*"]
---
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  namespace: default
  name: allow-ratings
spec:
  selector:
    matchLabels:
      app: ratings
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/default/sa/bookinfo-reviews"]
    to:
    - operation:
        methods: ["GET"]
        paths: ["/ratings/*"]
```

应用这些规则后，我们可以看到 “ratings” 和 “reviews” 再次可从 “productpage” 访问：

![](https://a-cup-of.coffee/blog/istio/_resources/allow-all.png)

### JWT 认证

现在我们已经了解了如何使用 ServiceAccount 认证服务，接下来看看如何使用 JWT（JSON Web Token）认证请求。这种方法稍微复杂一些，需要应用程序的请求进行调整以发送 JWT *(Envoy 不会自动完成)*。

> 信息：JWT，即 JSON Web Token，是一种用于创建访问令牌的开放标准，用于保护各方之间信息交换的安全性。JWT 包含有关用户的身份信息（称为“声明”），以 JSON 格式编码。它们通常使用私钥进行数字签名，以确保其真实性。

在本部分，我将 **强烈** 借鉴 [InfraCloud Github 仓库](https://github.com/infracloudio/Python-Key-Generation) 的灵感，如果没有它，我将无法在 Istio 中实现 JWT。感谢他们的工作！

我们将从生成用于签署 JWT 的私钥和公钥开始。为此，我们将使用 OpenSSL 生成 RSA 密钥。需要一个密钥来保护私钥。

```
openssl genrsa -aes256 -out private_encrypted.pem 4096
openssl rsa -pubout -in private_encrypted.pem -out public.pem
openssl rsa -in private_encrypted.pem -out private.pem -outform PEM
```

我们得到三个文件：`private.pem` ，`public.pem`和 `private_encrypted.pem`。

现在，我们将使用 `private.pem` 生成 JWT 密钥：

```python
# generatekey.py
from authlib.jose import jwt
import os
JWT_ISSUER=os.getenv('JWT_ISSUER') # ex: qjoly@a-cup-of.coffee
JWT_EXPIRATION=int(os.getenv('JWT_EXPIRATION')) # ex: 1685505001
header = {'alg': 'RS256'}
payload = {'iss': JWT_ISSUER, 'sub': 'admin', 'exp': JWT_EXPIRATION}
private_key = open('private.pem', 'r').read() #Provide the path to your private key
bytes = jwt.encode(header, payload, private_key)
print(bytes.decode('utf-8'))
```
```bash
export JWT_EXPIRATION=1782191719000
export JWT_ISSUER="qjoly@a-cup-of.coffee"
export JWT_TOKEN=$(python3 generatekey.py)
```

对于 JWT_EXPIRATION 变量，您可以使用 [Epoch 转换器](https://www.epochconverter.com/) 网站将日期转换为时间戳。

现在，我们来验证公钥是否正确验证了 JWT：

```python
# validatekey.py
import os
JWT_TOKEN=os.getenv('JWT_TOKEN')
from authlib.jose import jwt
public_key = open('public.pem', 'r').read() #Provide path to your public key
claims = jwt.decode(JWT_TOKEN, public_key)
claims.validate()
print(claims)
```
```bash
$ python3 validatetoken.py
{'iss': 'qjoly@a-cup-of.coffee', 'sub': 'admin', 'exp': 1782191719000}
```

我们的令牌被正确识别并有效（幸运的是，因为这是 Istio 用于认证请求的相同机制）。

现在，我们从公钥生成 JWK（JSON Web Key）以在 Istio 中配置它。

```python
from authlib.jose import jwk
public_key = open('public.pem', 'r').read() #Provide path to your public key
key = jwk.dumps(public_key, kty='RSA')
print(key)
```

```
$ python3 generatejwk.py
{'n': 'rPbn21rfrOrjq5AZ4W6XMjfpUu0SMIAIY9zj6skWWRMEYJn4Jvj6v3olLgMd0JjJluPXxgBYalIL2Fv9mKnZIyFcaCWDkTKBj1xN9k4PN-g5pPSGtYEYHT-zfdBfH-8inea8c9XoQGwyqm7TEwmI4M43WsBoqsItBcB_rLTo8DLlRf0mzlbTeK-M0iEC8-Osfj2FV9vtHR_FdsWaLK5QN-c8aJZIAZQ_S81EvRzVYguJ2-3l05JNI0GGNdGwawvp4cXmvIlCGEuZ5fdNJTjd3pcEJqMR8Gzyd_kb32SiHDXvTdI48KHPo_EjUf_i1maufxJToqEBOPwjEdpg1D1BPQ', 'e': 'AQAB', 'kty': 'RSA'}
```

我们将 `generatejwk.py` 生成的 JSON 提供给 Istio，以便它可以验证对“productpage”的请求中的 JWT。

```yaml
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: productpage-jwt
  namespace: default
spec:
  selector:
    matchLabels:
      app: productpage
  jwtRules:
  - forwardOriginalToken: true
    issuer: qjoly@a-cup-of.coffee
    jwks: |
      {"keys": [{"n": "rPbn21rfrOrjq5AZ4W6XMjfpUu0SMIAIY9zj6skWWRMEYJn4Jvj6v3olLgMd0JjJluPXxgBYalIL2Fv9mKnZIyFcaCWDkTKBj1xN9k4PN-g5pPSGtYEYHT-zfdBfH-8inea8c9XoQGwyqm7TEwmI4M43WsBoqsItBcB_rLTo8DLlRf0mzlbTeK-M0iEC8-Osfj2FV9vtHR_FdsWaLK5QN-c8aJZIAZQ_S81EvRzVYguJ2-3l05JNI0GGNdGwawvp4cXmvIlCGEuZ5fdNJTjd3pcEJqMR8Gzyd_kb32SiHDXvTdI48KHPo_EjUf_i1maufxJToqEBOPwjEdpg1D1BPQ", "e": "AQAB", "kty": "RSA"}]}
```

现在，我们可以应用一个 ACL 规则，仅当 JWT 由发行者“[qjoly@a-cup-of.coffee](mailto:qjoly@a-cup-of.coffee)”签名时，才允许对“productpage”的流量。

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: productpage-jwt
  namespace: default
spec:
  selector:
    matchLabels:
      app: productpage
  action: ALLOW
  rules:
  - when:
    - key: request.auth.claims[iss]
      values: ["qjoly@a-cup-of.coffee"]
```

现在一切都已到位，让我们删除在之前步骤中创建的 ACL 规则（允许对“productpage”的所有流量的规则）：

```
kubectl delete authorizationpolicies.security.istio.io allow-productpage
```

在此配置中，我仅当 JWT 由发行者“`qjoly@a-cup-of.coffee` ”签名时，才允许对“productpage”的流量。让我们尝试发出一个请求以验证这一点：

```
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage -s -I
HTTP/1.1 403 Forbidden
server: istio-envoy
date: Sun, 23 Jun 2024 06:13:26 GMT
x-envoy-upstream-service-time: 1
```

现在，让我们使用有效的 JWT 进行测试（请记住，我从命令 `export JWT_TOKEN=$(python3 generatekey.py)`
生成了令牌）。

```
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage --header "Authorization: Bearer $JWT_TOKEN" -s -I
HTTP/1.1 200 OK
server: istio-envoy
date: Sun, 23 Jun 2024 06:16:08 GMT
x-envoy-upstream-service-time: 17
```

以及使用无效的 JWT：

```
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage --header "Authorization: Bearer a-cup${JWT_TOKEN}of-coffee" -s -I
HTTP/1.1 401 Unauthorized
www-authenticate: Bearer realm="http://192.168.128.30:30492/productpage", error="invalid_token"
content-length: 42
content-type: text/plain
date: Sun, 23 Jun 2024 06:18:14 GMT
server: istio-envoy
x-envoy-upstream-service-time: 5
```

### 管理外部访问

可以要求 Envoy 管理外部服务（即不在 Istio 网格中的服务）。这对于在利用 Istio 的功能（重试、可观测性、带宽管理等）的同时管理与第三方服务的通信很有用。

为此，您可以使用 **ServiceEntry** 来声明外部服务。以下是一个示例：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: coffee-website
spec:
  hosts:
  - a-cup-of.coffee
  - une-tasse-de.cafe
  location: MESH_EXTERNAL
  ports:
  - number: 443
    name: https
    protocol: TLS
  resolution: DNS
```

为了进行测试，我将声明一个 pod，它将允许我们向外部服务发出请求。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: debug-network
spec:
  containers:
  - name: debug
    image: digitalocean/doks-debug:latest
    command: [ "sleep", "infinity" ]
```

我将通过此 pod 生成一些请求，以查看 Istio 如何处理对已注册服务的请求。

```
while true; do kubectl exec pods/debug-network -c debug exec -- curl https://a-cup-of.coffee ; done
```

![](https://a-cup-of.coffee/blog/istio/_resources/se-blog-coffee.png)

我们可以看到 Istio 很好地识别了 ServiceEntry。

现在，让我们尝试对未在 ServiceEntry 中声明的服务发出请求：

```
kubectl exec pods/debug-network -c debug exec -- curl https://perdu.com
```

![](https://a-cup-of.coffee/blog/istio/_resources/854dc23b91c2fd92f6f75e6ea4bddb48.png)

流量被发送到“PassThroughCluster”
*(这表明请求像经典 pod 一样正常处理（Envoy 不处理请求）)*。

现在，让我们考虑我想限制集群的出站流量的情况。为此，我将修改 Istio 网格的设置，以阻止所有出站流量，除了在 ServiceEntry 中声明的流量。

```
istioctl upgrade --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY
```

然后，如果我重试对 `perdu.com` 的请求，我将收到错误：


```
$ kubectl exec pods/debug-network -c debug exec -- curl https://perdu.com/ -v
* Recv failure: Connection reset by peer
* OpenSSL SSL_connect: Connection reset by peer in connection to perdu.com:443
0 0 0 0 0 0 0 0 --:--:-- --:--:-- --:--:-- 0
* Closing connection 0
curl: (35) Recv failure: Connection reset by peer
command terminated with exit code 35
```

另一方面，如果我向 `a-cup-of.coffee` 发起请求，请求将成功发送：

```
$ kubectl exec pods/debug-network -c debug exec -- curl https://a-cup-of.coffee -I -s
HTTP/2 200
accept-ranges: bytes
content-type: text/html
server: lighttpd/1.4.71
```

>注意：要返回默认模式，只需将 `meshConfig.outboundTrafficPolicy.mode` 变量设置为 `ALLOW_ANY`。

```
istioctl upgrade --set meshConfig.outboundTrafficPolicy.mode=ALLOW_ANY
```

请注意，`REGISTRY_ONLY` 模式允许每个 Pod 中所有在 ServiceEntry 中声明的服务的流量。我还没有找到如何将出站流量限制到单个应用程序。例如，将“productpage”的出站流量限制为“a-cup-of.coffee”，并将“reviews”的出站流量限制为“une-tasse-de.cafe”。

## 厌倦了 Sidecar？

Istio 提供了一个名为“Ambient”的功能，该功能允许不在每个 Pod 中部署 Sidecar。在此模式下，Istio 充当 CNI（容器网络接口）并拦截来自 Pod 的传入和传出网络流量以应用安全规则。

此模式的主要目标是通过避免在每个 Pod 中部署 Sidecar 来减少资源消耗（CPU、内存），以及提高 Istio 网格的性能。我们将在专门的部分中查看这是否确实如此。

那么，您可能会问，“Ambient”模式如何提高 Istio 网格的性能？好吧，通过减少 Sidecar 的数量，从而减少每个请求的 L7 处理步骤数量。

> 相反，最大的罪魁祸首是 Istio 需要实现其复杂功能集的密集 L7 处理。与 Sidecar 不同，Sidecar 为每个连接实现两个 L7 处理步骤（每个 Sidecar 一个），环境网格将这两个步骤合并为一个。在大多数情况下，我们预计这种减少的处理成本将弥补额外的网络跳跃。[来源](https://istio.io/latest/blog/2022/introducing-ambient-mesh/)

要激活“Ambient”模式，我们需要使用 `ambient` 配置文件安装 Istio，并添加 Gateway API（一个官方的 Kubernetes 项目，旨在用新对象替换 Ingress。如果您对该主题感兴趣，可以参考 [此处](https://istio.io/latest/docs/reference/config/networking/gateway/) 的文档）。

```
istioctl install --set profile=ambient --skip-confirmation
kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
{ kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd/experimental?ref=v1.1.0" | kubectl apply -f -; }
```

Ambient 使用命名空间的新标签：`istio.io/dataplane-mode=ambient`。我们可以将其应用于“coffee”命名空间以激活“Ambient”模式，并删除 `istio-injection` 标签以禁用自动 Sidecar 注入。

```
kubectl label namespace coffee istio.io/dataplane-mode=ambient
kubectl label namespace default istio-injection-
kubectl rollout restart deployment -n default details-v1 productpage-v1 ratings-v1 reviews-v1 reviews-v2 reviews-v3
```

现在，无需“istio-ingressgateway”服务来管理传入流量，我们可以直接使用 Gateway 对象。

为此，我们应用以下配置：

```yaml
apiVersion: gateway.networking.k8s.io/v1beta1
kind: Gateway
metadata:
  name: bookinfo-gateway
spec:
  gatewayClassName: istio
  listeners:
  - name: http
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: Same
---
apiVersion: gateway.networking.k8s.io/v1beta1
kind: HTTPRoute
metadata:
  name: bookinfo
spec:
  parentRefs:
  - name: bookinfo-gateway
  rules:
  - matches:
    - path:
        type: Exact
        value: /productpage
    - path:
        type: PathPrefix
        value: /static
    - path:
        type: Exact
        value: /login
    - path:
        type: Exact
        value: /logout
    - path:
        type: PathPrefix
        value: /api/v1/products
  backendRefs:
  - name: productpage
    port: 9080
```

成功部署了“gateway” Pod：

```
$ kubectl get pods
NAME READY STATUS RESTARTS AGE
bookinfo-gateway-istio-7c755f6876-t59dn 1/1 Running 0 14s
details-v1-cf74bb974-ph5dd 1/1 Running 0 50s
productpage-v1-87d54dd59-nwxgd 1/1 Running 0 49s
ratings-v1-7c4bbf97db-sq475 1/1 Running 0 50s
reviews-v1-5fd6d4f8f8-2r4dz 1/1 Running 0 50s
reviews-v2-6f9b55c5db-4fkwb 1/1 Running 0 50s
reviews-v3-7d99fd7978-nbbdr 1/1 Running 0 49s
```

没有 LoadBalancer，我将公开“bookinfo-gateway”服务作为 NodePort 以从外部访问应用程序。

```
$ kubectl annotate gateway bookinfo-gateway networking.istio.io/service-type=NodePort --namespace=default
$ kubectl get svc
NAME                     TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                        AGE
bookinfo-gateway-istio   NodePort    10.98.171.168   <none>        15021:31677/TCP,80:31334/TCP   17s
details                  ClusterIP   10.105.80.56    <none>        9080/TCP                       51s
productpage              ClusterIP   10.109.221.79   <none>        9080/TCP                       51s
ratings                  ClusterIP   10.102.161.80   <none>        9080/TCP                       51s
reviews                  ClusterIP   10.100.182.23   <none>        9080/TCP                       51s
```

以下命令用于查找网关服务的端口：

```
export INGRESS_PORT=$(kubectl get service bookinfo-gateway-istio -o jsonpath='{.spec.ports[?(@.name=="http")].nodePort}')
export INGRESS_HOST=$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}')
```

```
$ curl $INGRESS_HOST:$INGRESS_PORT/productpage -I
HTTP/1.1 200 OK
server: istio-envoy
date: Tue, 25 Jun 2024 20:55:31 GMT
content-type: text/html; charset=utf-8
content-length: 4294
vary: Cookie
x-envoy-upstream-service-time: 28
```

![](https://a-cup-of.coffee/blog/istio/_resources/ambient-kiali.png)

在这种情况下，流量仅在 L4 层进行管理（不再像 sidecar 那样在 L7 层进行管理）。这可以减少 pod 的负载并提高 Istio 网格的性能。但是，一些功能（如 HTTP 流量管理（重试、断路器等））会丢失。可以通过使用网关（或 Istio 术语中的“航路点”）来管理 HTTP 流量来缓解此问题。

我将在以后的文章中继续探讨“环境”模式，以澄清这些不确定性。

## 性能基准测试

最后，我将执行性能基准测试，以查看 Istio 如何影响 Kubernetes 集群的性能。为此，我们将比较三种不同场景下的两种通信方法（HTTP 和 TCP）：

- 无 Istio；
- 有 Istio；
- Istio 在“环境”模式下。

为此，我将使用 [Fortio](https://fortio.org/)，它是由 Istio 开发的用于 HTTP 和 TCP 服务的基准测试工具。

我的集群中使用的 CNI 是 Flannel（我在 Cilium 和 Istio Ambient 之间遇到了问题）。但是，我仍然使用 Cilium 执行了性能测试，以让您了解我的 pod 之间的带宽。

```
🔥 Network Performance Test Summary [cilium-test]:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📋 Scenario        | Node       | Test            | Duration        | Min             | Mean            | Max             | P50             | P90             | P99             | Transaction rate OP/s
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📋 pod-to-pod      | same-node  | TCP_RR          | 10s             | 27µs            | 75.32µs         | 8.115ms         | 69µs            | 108µs           | 211µs           | 13149.99
📋 pod-to-pod      | same-node  | UDP_RR          | 10s             | 29µs            | 81.06µs         | 23.993ms        | 67µs            | 113µs           | 308µs           | 12222.58
📋 pod-to-pod      | same-node  | TCP_CRR         | 10s             | 143µs           | 320.87µs        | 14.373ms        | 284µs           | 411µs           | 1.068ms         | 3106.70
📋 pod-to-pod      | other-node | TCP_RR          | 10s             | 129µs           | 298.52µs        | 14.168ms        | 245µs           | 395µs           | 1.197ms         | 3340.77
📋 pod-to-pod      | other-node | UDP_RR          | 10s             | 147µs           | 382.21µs        | 37.771ms        | 309µs           | 573µs           | 1.534ms         | 2609.31
📋 pod-to-pod      | other-node | TCP_CRR         | 10s             | 440µs           | 1.21346ms       | 17.531ms        | 1.061ms         | 1.797ms         | 4.255ms         | 823.03
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
📋 Scenario        | Node       | Test            | Duration        | Throughput Mb/s
-------------------------------------------------------------------------------------
📋 pod-to-pod      | same-node  | TCP_STREAM      | 10s             | 610.56
📋 pod-to-pod      | same-node  | UDP_STREAM      | 10s             | 272.15
📋 pod-to-pod      | other-node | TCP_STREAM      | 10s             | 1506.68
📋 pod-to-pod      | other-node | UDP_STREAM      | 10s             | 209.39
-------------------------------------------------------------------------------------
```

现在我们已经了解了最大可实现的性能，我们将开始我们的基准测试。

它将包含两个部分：

- 使用 Fortio 的 HTTP 部分来测试延迟；
- 使用 Iperf 的 TCP 部分来测试带宽。

**小免责声明**：我将获得的结果可能与您的结果不同。性能可能会因集群配置、集群负载、应用程序配置等而异。我将获得的结果不一定代表现实情况。它们只是为了让您了解 Istio 在给定用例下在 Kubernetes 集群中的性能。

如果您想阅读更全面的基准测试，我建议您参考 [这个 Github 仓库](https://github.com/livewyer-ops/poc-servicemesh2024/blob/main/docs/test-report.md#network-tests)，它提供了非常完整和有趣的结果。

### HTTP 基准测试

如前所述，我将使用 Fortio 来测试服务的延迟。为此，我将在集群中部署一个 Fortio pod，并向“bookinfo”应用程序的其中一个服务“details”发出请求。

为了安装 Fortio，我首先部署了 [Fortio OPERATOR](https://github.com/verfio/fortio-operator)，然后再选择经典部署（KISS）。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fortio-debug
spec:
  ports:
  - port: 8080
    name: http-debug
  selector:
    app: fortio-debug
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fortio-debug-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fortio-debug
  template:
    metadata:
      labels:
        app: fortio-debug
    spec:
      containers:
      - name: fortio-debug
        image: fortio/fortio:latest_release
        imagePullPolicy: Always
        ports:
        - containerPort: 8080
```

为了启动和配置测试，我只需对 Fortio Pod 进行端口转发：

```bash
kubectl port-forward svc/fortio-debug 8080:8080
```

其余配置直接在 Fortio Web 界面上完成，地址为 `http://localhost:8080/fortio/`。我选择执行延迟测试，每个测试有 10 个并发连接，每秒发出 100 个请求。当然，我确保测试始终在两个不同的节点之间进行。

![](https://a-cup-of.coffee/blog/istio/_resources/fortio-web.png)

以下是三种场景的测试结果：

**无 Istio**

![](https://a-cup-of.coffee/blog/istio/_resources/6f25496656b67355c3149d7b819b8def.png)

**带 Istio Sidecar**

![](https://a-cup-of.coffee/blog/istio/_resources/f1b75ffbb034f1aadbcedad63815c95a.png)


**带 Istio Ambient**

![](https://a-cup-of.coffee/blog/istio/_resources/1141abfb3858c60718eefbe6e3125d98.png)

有趣的是，我们得到了截然不同的结果。在延迟方面，结果如下：

1. Istio Ambient：2.35 毫秒延迟；
2. 无 Istio：2.8 毫秒延迟；
3. Istio Sidecar：39.3 毫秒延迟。

我注意到，在 Istio Ambient 中存在连接错误，即使经过多次测试也无法解释。

令人惊叹的是，与没有 Istio 的集群相比，Istio Ambient 能够降低延迟（我甚至多次检查结果以确保）。这表明“Ambient”模式是一种可行的解决方案，可以潜在地提高 Kubernetes 集群的性能。

### TCP 基准测试

对于此基准测试，我将使用 Iperf 测试服务之间的带宽。然后，我将部署一个 Iperf Pod 作为服务器，并使用一个“tcp-iperf-client”Pod 向 Iperf 服务器发出请求。

**IPerf 清单**.

**客户端 Iperf**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: tcp-iperf-client
spec:
  containers:
  - name: debug
    image: digitalocean/doks-debug:latest
    command: [ "sleep", "infinity" ]
```

**服务器 Iperf**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tcp-iperf
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tcp-iperf
      version: v1
  template:
    metadata:
      labels:
        app: tcp-iperf
        version: v1
    spec:
      containers:
      - args:
        - -s
        - --port
        - "5201"
        image: mlabbe/iperf
        imagePullPolicy: IfNotPresent
        name: tcp-iperf
        ports:
        - containerPort: 5201
          name: tcp-app
          protocol: TCP
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: tcp-iperf
    service: tcp-iperf
  name: tcp-iperf
  namespace: default
spec:
  ports:
  - name: tcp-iperf
    port: 5201
    protocol: TCP
  selector:
    app: tcp-iperf
  type: ClusterIP
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: tcp-iperf
spec:
  hosts:
  - "*"
  gateways:
  - tcp-iperf
  tcp:
  - match:
    - port: 5201
    route:
    - destination:
        host: tcp-iperf
        port:
          number: 5201
```

我还将强制执行 mTLS，以使其更接近实际使用场景。

![MTLS 基准测试](https://a-cup-of.coffee/blog/istio/_resources/5e90e32fe249e74763f9760e8ddcfd81.png)

```bash
# Without Istio (no sidecar, no ambient)
iperf -c tcp-iperf --port 5201
------------------------------------------------------------
Client connecting to tcp-iperf, TCP port 5201
TCP window size: 16.0 KByte (default)
------------------------------------------------------------
[  1] local 10.244.2.4 port 56286 connected with 10.102.184.216 port 5201 (icwnd/mss/irtt=13/1398/585)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-10.0207 sec  4.22 GBytes  3.62 Gbits/sec
```

```bash
# With Istio Sidecar
iperf -c tcp-iperf --port 5201
------------------------------------------------------------
Client connecting to tcp-iperf, TCP port 5201
TCP window size: 2.50 MByte (default)
------------------------------------------------------------
[  1] local 10.244.2.215 port 41158 connected with 10.106.115.53 port 31400 (icwnd/mss/irtt=13/1398/34)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-10.1227 sec  2.22 GBytes  1.88 Gbits/sec
```

```bash
# With Istio Ambient
 iperf -c tcp-iperf --port 5201
------------------------------------------------------------
Client connecting to tcp-iperf, TCP port 5201
TCP window size: 2.50 MByte (default)
------------------------------------------------------------
[  1] local 10.244.1.9 port 54814 connected with 10.110.166.223 port 5201 (icwnd/mss/irtt=13/1398/50)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-10.0806 sec  2.48 GBytes  2.12 Gbits/sec
```

与延迟不同，Istio Ambient 在延迟方面表现最佳，而“无 Istio”模式在带宽方面则优于其他两种模式。

1. 无 Istio：3.62 Gbits/sec；
2. Istio Ambient：2.12 Gbits/sec；
3. Istio Sidecar：1.88 Gbits/sec。

## 结论

Istio 是一款功能强大且完整的产品，但也并非没有缺陷。很容易在 Istio 的配置中迷失方向，最终导致网格无法按预期工作（此外，日志并不总是很明确）。因此，在深入配置网格之前，了解 Istio 的概念非常重要。

尽管我花了很多时间学习 Istio，但我仍然没有足够的信心用于生产环境，还有很多东西需要从这个解决方案中学习。我希望阅读本文对那些想要开始学习 Istio 的人有所帮助。

如果您想鼓励我写这类文章（并资助我失眠的夜晚），请随时在我的 [Kofi 页面](https://ko-fi.com/thebidouilleur) 上进行少量捐赠，您也可以在下面的社交网络上给我一些支持：

- [Twitter](https://twitter.com/thebidouilleur)
- [LinkedIn](https://www.linkedin.com/in/quentin-joly-it/)

在此之前，祝您度过美好的一天，并祝您在 Istio 之旅中好运！