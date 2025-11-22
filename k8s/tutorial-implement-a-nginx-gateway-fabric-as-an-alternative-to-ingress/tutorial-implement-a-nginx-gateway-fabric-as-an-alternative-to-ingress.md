
<!--
title: Nginx Gateway Fabric实战：Ingress的替代者？
cover: https://cdn.thenewstack.io/media/2025/11/9466f8ec-alexey-taktarov-_a6erb7nlfg-unsplash-1.jpg
summary: Kubernetes Ingress Nginx 退役，转向 Gateway API。Gateway API 提供标准化、可扩展的流量管理。Nginx Gateway Fabric 是其实现，本教程演示了如何用它路由HTTP流量。
-->

Kubernetes Ingress Nginx 退役，转向 Gateway API。Gateway API 提供标准化、可扩展的流量管理。Nginx Gateway Fabric 是其实现，本教程演示了如何用它路由HTTP流量。

> 译自：[Tutorial: Implement a Nginx Gateway Fabric as an Alternative to Ingress](https://thenewstack.io/tutorial-implement-a-nginx-gateway-fabric-as-an-alternative-to-ingress/)
> 
> 作者：Janakiram MSV

Kubernetes 生态系统正在经历一场关于其如何管理外部流量的根本性转变。2025 年 11 月 12 日，Kubernetes [宣布](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/) Ingress Nginx 退役，它是云原生基础设施中最广泛部署的组件之一。尽力维护将[持续到 2026 年 3 月](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/)，之后该仓库将进入只读状态，不再提供安全补丁、错误修复或功能发布。

这标志着运行 Kubernetes 集群的组织面临一个关键拐点。传统的 Ingress API 虽然久经考验并为几代工程师所熟悉，但其设计已达到极限。它缺乏对高级流量管理模式的支持，迫使团队与供应商特定的注解搏斗，并且无法表达现代应用程序所需的复杂路由规则。

[Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) 应运而生，它是一个标准化、可扩展的框架，解决了这些根本性限制。Gateway API 不再依赖于碎片化实现和专有注解，而是引入了一个统一模型，支持多协议路由（L4 和 L7）、细粒度流量控制、基于 Header 的模式匹配、请求镜像和原生流量指标。

Gateway API 于 2023 年实现正式发布 (GA)，代表了 Kubernetes 社区对 Ingress 问题的解答。有关 Ingress 控制器和 Gateway 的详细比较，请参阅我之前发表在 The New Stack 上的文章。

[Nginx Gateway Fabric](https://github.com/nginx/nginx-gateway-fabric) 是 Gateway API 的早期实现之一，它是一个开源的、符合规范的 Kubernetes Gateway API 实现，使用 Nginx 作为其高性能数据平面。它分离了控制平面和数据平面关注点，为每个 Gateway 资源动态配置 Nginx 实例，同时将 Gateway API 资源转换为 Nginx 配置。与传统的 [Ingress 控制器](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes/)不同，Nginx Gateway Fabric 开箱即用地提供了高级功能，包括蓝绿部署和金丝雀部署、A/B 测试、请求/响应操作以及多租户基于角色的治理。

本教程将指导您实现基于 Nginx Gateway Fabric 的 [Gateway API](https://thenewstack.io/kubernetes-gateway-api-nixes-future-beta-releases/)，帮助您为后 Ingress 时代做好基础设施准备。我们将从一个熟悉的 Kubernetes 部署开始，包含两个服务：一个用于 web，一个用于 API。我们将使用 Gateway API 将 HTTP 流量路由到这两个内部 ClusterIP 服务。

在本教程中，我使用在 [Multipass 虚拟机](https://thenewstack.io/multipass-fast-scriptable-ubuntu-vms-for-modern-devops/)中运行的 [K3s](https://k3s.io/) 集群。但您可以使用任何 Kubernetes 环境来完成本指南中解释的步骤。

## 步骤 1：定义和部署示例应用程序

我们将定义两个部署和服务，以在 demo 命名空间中将 web 和 api 端点作为 ClusterIP 服务暴露。

应用 YAML 文件并检查 Pod 和服务是否正常运行。

```

kubectl get pods,svc -n demo
```

![](https://cdn.thenewstack.io/media/2025/11/b4d4c445-gw-api-0-1024x441.png)

我们的目标是通过 Gateway API 将流量路由到 demo-api 和 demo-app 端点。

## 步骤 2：部署 Nginx Gateway Fabric

我们将首先安装 Gateway 所需的 CRD。

```

kubectl kustomize "https://github.com/nginx/nginx-gateway-fabric/config/crd/gateway-api/standard?ref=v2.2.1" \
  | kubectl apply -f -
```

```

kubectl get crd | grep gateway.networking.k8s.io
```

![](https://cdn.thenewstack.io/media/2025/11/00d54d12-gw-api-1-1024x337.png)

然后，我们将通过 Helm Chart 部署 Nginx Gateway Fabric。

```

helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
  --create-namespace \
  -n nginx-gateway \
  --set nginx.service.type=NodePort
```

请注意，我们将服务类型暴露为 NodePort。如果您使用的是托管 Kubernetes 环境，请将其更改为 `LoadBalancer`。

通过检查 `nginx-gateway` 命名空间验证安装。

```

kubectl get pods,svc -n nginx-gateway
```

![](https://cdn.thenewstack.io/media/2025/11/184c369f-gw-api-2-1024x254.png)

下一步是部署 Gateway，应用程序开发人员将使用它来定义其命名空间内运行服务的路由。

应用 YAML 文件并验证 Gateway 是否已正确创建。

```

kubectl apply -f gateway.yaml
```

```

kubectl get pods,svc -n nginx-gateway
```

![](https://cdn.thenewstack.io/media/2025/11/ed62af7d-gw-api-3-1024x303.png)

我们可以看到 Gateway 已经创建并通过 `NodePort` 31678 暴露。

## 步骤 3：定义到示例应用程序的路由

Gateway 部署完成后，是时候创建路由了。这通常由在 Kubernetes 中部署应用程序的开发人员完成。路由与应用程序运行在同一个命名空间中。

定义路由并部署它。

```

kubectl apply -f route.yaml
```

这为示例应用程序暴露的端点创建了一个 `HTTPRoute`。

## 4：访问 Gateway 暴露的 HTTP 端点

我们已准备好测试 Gateway 定义的路由。

鉴于我的虚拟机 IP 地址是 `192.168.2.5` 且 `NodePort` 是 31678，我可以发出 cURL 请求来测试这些端点。

![](https://cdn.thenewstack.io/media/2025/11/d1e836d7-gw-api-4.png)

我们已成功实现了 Gateway API，将内部端点暴露给外部用户。在即将发布的教程中，我将逐步讲解实现基于 TLS 路由的步骤。敬请期待！