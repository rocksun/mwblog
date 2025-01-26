
<!--
title: 强大的负载均衡策略：Kubernetes Gateway API
cover: ./cover.png
-->

第41集：从ClusterIP到Ingress和Gateway API。探索Kubernetes中最常见的服务负载均衡策略。

> 译自 [Powerful Load Balancing Strategies: Kubernetes Gateway API](https://cloudnativeengineer.substack.com/p/powerful-load-balancing-strategies-kubernetes)，作者 Giuseppe Santoro。

在Kubernetes中有很多方法可以暴露运行的HTTP应用程序。

典型的设置包括创建一个部署和一个关联的服务。

服务的类型决定了应用程序的可见性。

最常见的[Kubernetes服务](https://kubernetes.io/docs/concepts/services-networking/service/)类型是：

- `ClusterIP`: 默认值（如果未提供类型），仅在同一个Kubernetes集群内部向其他服务暴露应用程序。
- `NodePort`: 主要用于测试，在每个集群节点的选定端口上外部暴露服务。
- `LoadBalancer`: 用于云中的生产用例，以在集群外部暴露服务。

就是这样吗？

两年前参加认证Kubernetes管理员（又名CKA）考试时，我学到的就是这些，我也这么认为了一段时间。

在本文中，我们将简要介绍ClusterIP和LoadBalancer服务类型，并讨论[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)和[Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)的替代方案。

我们将简要讨论每个选项及其优缺点，并提供一些代码示例帮助您入门。

本文包含以下部分：

- 一个小小的警告
- ClusterIP：在内部暴露服务
- LoadBalancer：在云中暴露服务
- Ingress：所有服务的单一网关
- Gateway API：Ingress的现代替代方案

## 一个小小的警告

本文中的代码示例是有效的示例，即使只是一个玩具应用程序。

为了尽可能简单，因为内容很多，我们只想关注负载均衡策略。

我们将使用名为[traefik/whoami](https://github.com/traefik/whoami)的容器镜像，它将HTTP请求的内容及其所有标头和参数作为输出返回。

此容器镜像由反向代理[Traefik](https://traefik.io/traefik/)在其官方文档中使用。由于Traefik是我选择的反向代理（因为它在[K3d](https://k3d.io/)中作为默认值提供），所以我们将在本文中使用它。

即使这些代码示例已在K3d和Traefik上进行了测试，它们也应该适用于任何Kubernetes发行版或任何反向代理。

本文不包含有关设置这些代码示例的更多信息。我将来会写这方面的内容。

本文并非旨在成为Kubernetes中负载均衡器的详尽教程。内容太多了。

我想向您介绍这些概念，以便您知道这些东西的存在。

我将提供一些外部资源来继续学习。

## ClusterIP：在内部暴露服务

创建和暴露HTTP应用程序的最低要求是创建一个Kubernetes部署和一个关联的服务。

在整篇文章中，我们将使用相同的Kubernetes部署，代码如下所示。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08902b49-c877-41ff-8b01-073c24f65665_634x944.png)

*一个包含3个副本的Kubernetes部署，用于`traefik/whoami`镜像*

如上所述，这只是一个用于调试HTTP网络路由的玩具应用程序。

我们将在Ingress部分看到此应用程序的输出是什么样的。

除了部署的样板代码外，您应该注意：

- 我们正在创建三个相同pod的副本。这样，当运行客户端时，您将获得每个响应pod的不同内部IP。
- 应用程序使用的容器端口由环境变量`PORT`配置，然后由`containerPort: 80`引用。
- 我们将使用Kubernetes标签`label: my-app`用于部署、服务和pod。

拥有部署后，您可以创建一个没有类型的关联服务。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feaa921c9-4ce3-4b33-82bd-0b0828b58e0c_457x621.png)

默认情况下，服务的类型为`ClusterIP`，并且该服务只能从同一Kubernetes集群内的其他服务和pod访问。

除了在80端口暴露HTTP应用程序之外，此服务没有什么值得注意的。

根据上述部署，上述服务将在后续章节中使用（大部分按原样）。

## LoadBalancer：在云中暴露服务

如开头所述，如果要将服务外部暴露给互联网以用于生产用例，则需要创建一个类型为`LoadBalancer`的服务。

您运行Kubernetes集群的云提供商将为此服务提供一个负载均衡器。

您要暴露的每个服务都将创建一个不同的负载均衡器。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8be39df3-283f-4522-a2fd-c3edc2fbf8b2_449x655.png)

正如你所看到的，与上一节中的服务唯一的区别在于`spec.type = LoadBalancer`中的服务类型。

## 优缺点

虽然此方案简单直接，但是当您拥有许多微服务并且不想为每个外部服务创建单个负载均衡器时，它就开始成为问题。

虽然此方案在云端运行时非常完美，但在本地机器上运行 Kubernetes 集群（例如使用 K3d）时则无法工作。

假设您像我一样坚信本地 Kubernetes 集群应该能够让您复制生产用例。在这种情况下，您将无法实现。

或者，您可以使用服务网格提供商，例如[Istio](https://istio.io/)。但是，对于简单的用例，有一个更简单的替代方案。

## Ingress：所有服务的单一网关

一段时间前，Kubernetes 决定为每个服务使用单个负载均衡器的良好替代方案是创建一个名为[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)的资源，该资源允许像 Traefik 或 Nginx 这样的反向代理创建复杂的路由规则。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd13d022d-810c-4c52-9836-b967dc07cf73_553x733.png)

*一个类型为 Ingress 的 Kubernetes 资源*

此 Ingress 资源指向我们在`ClusterIP：内部公开服务`部分中定义的服务定义和相关的部署。为简洁起见，此处不重复代码。

要从您的笔记本电脑访问服务，您必须运行以下 curl 命令：

```bash
curl -H "Host: my-app.example" http://localhost:8080
```

您可能已经注意到，`my-app.example`是在 Ingress 资源的`spec.rules.host`中定义的主机名。

作为参考，curl 命令的输出如下。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3b93428-ccf0-411c-9895-f7c7dfe7d420_676x737.png)

本节中提供的示例正式称为`基于主机的路由（虚拟主机）`，它只是 Ingress 的众多用例之一：

* 基于路径的路由
* SSL/TLS 终止
* 负载均衡和流量管理
* 身份验证和访问控制

## 使用 Ingress API 的优缺点

使用 Ingress 的优点：

* 完善的 API，所有主要的反向代理（例如 Traefik、Nginx）都支持
* 在本地 Kubernetes 集群（使用 K3d）和云端都能工作

缺点：

* 仅支持 L7 负载均衡。不支持 L4 协议，例如 TCP 和 UDP
* 从 L7 网络堆栈来看，它只支持 HTTP/S。它不支持 GRPC。如果您想支持微服务，这可能会带来不便。
* Ingress 不是所有反向代理之间的标准 API。规范和实现某些路由策略的方法可能存在一些差异。

## Gateway API：Ingress 的现代替代方案

`Ingress`的问题在于大多数反向代理都有自己实现这些路由规则的方法。

每个反向代理都需要用户提供自定义 Kubernetes 注解、自定义中间件扩展或一些自定义 Kubernetes 自定义资源 (CRD)。

这种情况一直持续到引入名为[Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/)的新 Kubernetes API。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0789b02a-b9e1-417b-ae88-f9d04c9fb3e4_627x709.png)

*来自网关API的HTTPRoute类型的Kubernetes资源*

从上面可以看出，您可以使用`HTTPRoute`复制与 Ingress 相同的结果。

在这种情况下，您可以使用以下命令访问后端服务：

```bash
curl -H "Host: load-balance.example" http://localhost:8080
```

## Gateway API 的优缺点

优点：

* 与 Ingress 概念相似。所有服务的单个网络端点，而不是每个服务一个负载均衡器。
* 支持 L4 和 L7 网络协议（例如 UDP、TCP、HTTP/S 和 GRPC）。
* 跨多个反向代理（例如 Traefik、Nginx 等）的标准 API。

缺点：

* 这是一个更新的 API，因此并非所有功能都由所有反向代理实现。例如，有关 Traefik v3.2.2 最新版本支持的功能的完整列表，请访问[gateway-api/conformance/reports/v1.2.1/traefik-traefik/experimental-v3.2.2-default-report.yaml at main · kubernetes-sigs/gateway-api](https://github.com/kubernetes-sigs/gateway-api/blob/main/conformance/reports/v1.2.1/traefik-traefik/experimental-v3.2.2-default-report.yaml)。

