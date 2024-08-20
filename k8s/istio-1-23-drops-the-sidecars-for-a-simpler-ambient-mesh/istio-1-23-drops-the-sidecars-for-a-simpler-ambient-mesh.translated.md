# Istio 1.23 摒弃 Sidecar，采用更简单的“环境网格”

![Istio 1.23 摒弃 Sidecar，采用更简单的“环境网格”的特色图片](https://cdn.thenewstack.io/media/2024/08/0400bf13-istio.png)
![Louis Ryan.](https://cdn.thenewstack.io/media/2024/08/1b2fa23a-louis-ryan-300x225.jpg)
Louis Ryan，Solo.io 首席技术官

[最新发布](https://istio.io/latest/news/releases/1.23.x/announcing-1.23/?ref=dailydev) 的开源 [Istio](https://istio.io/latest/) 服务网格软件，通过引入 [环境网格](https://thenewstack.io/traffic-routing-in-ambient-mesh/) 选项，为处理 [Kubernetes](https://www.thenewstack.io/Kubernetes) 流量提供了一种潜在的重大改变。

虽然这项技术在几个版本中一直作为实验性功能提供，但核心开发团队在收集用户反馈后，这是第一个将该功能作为生产级功能提供的版本。

商业 Istio 提供商 [Solo.io](https://www.solo.io/) 的首席技术官 [Louis Ryan](https://github.com/louiscryan) 也是 [Istio 技术监督委员会和指导委员会](https://github.com/istio/community/blob/master/TECH-OVERSIGHT-COMMITTEE.md) 的成员，他在接受 TNS 采访时解释说，这是一种全新的架构。“它更便宜、更快、更容易部署、更可扩展、更好。”

“环境”服务网格与传统方法不同，它不需要为每个应用程序配备单独的 sidecar。

Istio 是 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) 的一个项目，使其成为许多 Kubernetes 部署的基础。

## 无 Sidecar 的 Istio
Solo.io 的创始人兼首席执行官 [Idit Levine](https://www.linkedin.com/in/iditlevine/) 指出，sidecar 是 [微服务架构](https://thenewstack.io/year-in-review-was-2023-a-turning-point-for-microservices/) 的必要产物。一旦应用程序被分解成独立的服务，这些服务就需要一种通信方式。因此，为每个服务配备一个 sidecar 来处理所有网络流量是有意义的。

sidecar 为每个应用程序提供安全性、可靠性提升和动态网络功能。

Levine 指出，sidecars 解决了一个“真正的问题”。sidecar 提供了功能，但设计者“忽略”了它们会给机器本身带来多少开销。

相比之下，环境方法“正在降低成本，因为没有到处都是 sidecar。但它仍然为你提供你想要的安全性，以及所有功能，”Levine 说。“所以它实际上非常棒。”

Solo.io 的工程师们已经花了数年时间来完善环境方法。

## 环境网格的工作原理
“这种创新方法使 Kubernetes 中的网络变得更加容易。不再需要使用 sidecar 进行额外的步骤。服务现在可以更直接、更简单地进行通信，”AWS 社区构建者 [Seifeddine Rajhi](https://x.com/RajhiSaifeddine) 在一篇 [文章](https://itnext.io/kubernetes-networking-with-ambient-istios-sidecarless-innovation-0ef5fcc267f8) 中写道，解释了这项技术。

环境网格建立在 [零信任架构](https://thenewstack.io/beyondcorp-google-ditched-virtual-private-networking-internal-applications/) 之上。[ztunnel](https://github.com/istio/ztunnel) 零信任隧道是一个用 [Rust](https://thenewstack.io/rust-meets-dart-with-release-of-rust_core-1-0-0/) 编写的 [daemonset](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) pod，安装在每个集群上以处理第 3 层和第 4 层流量。然后，基于 [Envoy](https://thenewstack.io/envoy-gateway-offers-to-standardize-kubernetes-ingress/) 的 [Waypoint 代理](https://istio.io/latest/blog/2023/waypoint-proxy-made-simple/) 用于处理每个 [命名空间](https://thenewstack.io/leveraging-namespaces-for-cost-optimization-with-kubernetes/) 中更复杂的第 7 层流量，Rajhi 解释道。

因此，例如，对于 50 个 pod，每个 pod 每秒只接收 50 个请求，你可以使用单个代理处理所有这些请求。“这节省了大量的资源，”Ryan 指出。

还有其他优点。升级变得容易得多，因为应用程序不需要下线来分配 sidecar。相反，daemonset 的更新可以滚动进行。这就是“环境”这个名字的由来，这意味着要管理的端点要少得多。功能内置在集群本身中。

“用户体验非常简单。它易于安装，易于操作。你没有像 sidecar 模型那样有很多开销，”Levine 兴奋地说。

![环境 Waypoint 的图表](https://cdn.thenewstack.io/media/2024/08/d86b6902-waypoint-architecture.png)
Waypoint 代理独立于应用程序运行，独立于应用程序本身运行。

## Istio 环境可能更快
尽管处于实验阶段，但至少在某些情况下，环境网格与传统的 Istio 设置相比，可以降低延迟。

在为 The New Stack 撰写的一篇[投稿文章](https://thenewstack.io/ambient-mesh-can-sidecar-less-istio-make-applications-faster/)中，Solo.io 开源总监，同时也是 Istio 技术监督委员会和指导委员会成员的[Lin Sun](https://thenewstack.io/author/lin-sun/)，证明了 Istio 实际上可以在某些情况下降低用户应用程序的延迟。

为了进行测试，她使用了[Fortio](https://github.com/fortio/fortio) 负载测试库和 Istio 自身的[Bookinfo](https://istio.io/latest/docs/examples/bookinfo/) 示例应用程序。

“我们一直被教导说服务网格会增加延迟，”Sun 写道。这些结果“表明在某些情况下，工作负载通过服务网格运行时速度更快。”

在此测试中，Sun 重现了[早期测试](https://a-cup-of.coffee/blog/istio/#with-istio-ambient) 的结果，该测试由站点可靠性工程师[Quentin Joly](https://github.com/QJoly) 进行，他发现：

* Istio 环境：2.35 毫秒延迟；
* 无 Istio：2.8 毫秒延迟；
* Istio Sidecar：39.3 毫秒延迟。

“令人惊叹的是，Istio 环境设法降低了与没有 Istio 的集群相比的延迟，”他写道。“这表明‘环境’模式是一种可行的解决方案，可以潜在地提高 Kubernetes 集群的性能。”

## Istio 1.23 的其他新功能
**DNS 自动分配改进**: 地址分配已重新设计，解决了服务路由的许多问题。“在新方法中，分配的 IP 地址会持久化到*ServiceEntry*status 字段中，确保它们永远不会更改，”说明中指出。**重试改进**: 重试策略已重新设计，更改现已处于预览阶段，旨在减少[503 错误](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503)。到目前为止，重试仅对出站流量进行，重试会转到不同的 Pod。已添加一个新的检测例程来确定目标应用程序是否已关闭连接。**Bookinfo 改进**: 用于测试 Istio 部署的示例应用程序已重新设计。
[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)