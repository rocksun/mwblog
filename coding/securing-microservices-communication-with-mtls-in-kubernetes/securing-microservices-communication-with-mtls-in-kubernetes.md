<!--
title: Kubernetes中使用mTLS保护微服务通信
cover: https://cdn.thenewstack.io/media/2023/11/065a613f-microservices-communication-1-1024x576.jpg
-->

微服务架构中，各服务间常有通信交互，以完成复杂业务流程，这给安全性和可扩展性带来挑战。启用双向 TLS(mTLS)可提高安全性，本文将详述 mTLS 的使用入门方法。

> 译自 [Securing Microservices Communication with mTLS in Kubernetes](https://thenewstack.io/securing-microservices-communication-with-mtls-in-kubernetes/)，作者 Robert Kimani。

[Kubernetes](https://thenewstack.io/kubernetes/)，作为容器化应用程序的事实标准编排平台，为部署和管理[微服务](https://thenewstack.io/microservices/)提供了强大的环境。但是，随着相互连接的服务数量的增长，一个稳固的[安全](https://thenewstack.io/security/)机制的需求变得越来越关键。

微服务通常相互通信以完成复杂的业务操作。这种通信涉及敏感数据的交换，如用户凭证、支付信息和个人标识符。

如果没有适当的安全措施，这些数据可能会被拦截或篡改，从而导致隐私泄露和完整性受损。此外，微服务的动态特性及其持续缩放的需求需要一个敏捷和自动化的安全解决方案。

双向传输层安全性(mTLS)已成为解决这些安全性挑战的有力解决方案。

[mTLS](https://thenewstack.io/mutual-tls-microservices-encryption-for-service-mesh/) 建立在传输层安全性(TLS)协议的基础之上，这是通过加密来保护互联网通信安全的常用方式。但是，mTLS 通过实施通信双方的相互认证将安全性提高了一个台阶。

换句话说，客户端和服务器都需要提供有效的数字证书，以确保不仅加密而且经过身份验证的通信。

## mTLS 和 Kubernetes

Kubernetes 提供了实现 mTLS 的理想平台，因为它具备动态服务发现和管理功能。随着服务频繁地在 Kubernetes 集群中被添加、删除或缩放，mTLS 确保在每个新实例可以与其他服务通信之前对其进行[认证](https://thenewstack.io/how-do-authentication-and-authorization-differ/)。

这为开发人员奠定了一个健壮的安全基础，使他们可以专注于构建功能而不会损害微服务之间的数据流的完整性和隐私。

在本文中，我们将深入探讨在 Kubernetes 集群中实际实施 mTLS。我们将利用 [Istio](https://thenewstack.io/what-is-istio-and-why-does-kubernetes-need-it/)，这是一个为微服务提供高级网络和安全功能的开源[服务网格](https://thenewstack.io/service-mesh/)。

## 在 Kubernetes 中实现 mTLS 的先决条件

在 Kubernetes 集群中开始实施 mTLS 之前，请确保具备以下先决条件。

- **Kubernetes 集群**。您应该有一个[正在运行的 Kubernetes 集群](https://thenewstack.io/best-practices-for-securely-setting-up-a-kubernetes-cluster/)。这可以是一个使用 Minikube 等工具设置的本地集群，也可以是一个像 GKE、EKS 或 AKS 这样的云托管 Kubernetes 环境。
- **Kubectl**。确保您已经安装了 [kubectl](https://thenewstack.io/kubecost-monitor-kubernetes-costs-with-kubectl/) 命令行工具，并且它已经被正确配置为与您的 Kubernetes 集群交互。此工具将用于管理和交互集群资源。
- **基本的 Kubernetes 知识**。[对 Pod、Service、Deployment 和 Namespace 等 Kubernetes 概念的基本理解是必不可少的](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/)。您应该能够使用 kubectl 命令轻松地创建、管理和删除这些资源。
- **容器化微服务**。为您打算在教程中部署的微服务准备容器镜像。这些镜像应该托管在 Kubernetes 集群可以访问的[容器仓库](https://thenewstack.io/how-a-container-registry-can-both-save-and-harm/)中。
- **Istio 安装**。由于我们将使用 Istio 来实现 mTLS，所以您需要在 Kubernetes 集群中安装 Istio。按照与您的环境相关的 [Istio 安装文档](https://istio.io/latest/docs/setup/getting-started/)操作。
- **Helm(可选但推荐)**。[Helm 是 Kubernetes 的包管理器](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/)，可以简化应用程序和服务的部署。虽然严格意义上并非必需，但[使用 Helm](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/) 可以简化像 Istio 这样的复杂应用程序的安装。如果您使用 Helm，请确保它已安装并配置好。
- **有效的域名**。Istio 的 mTLS 功能通常依赖于有效的域名来生成证书。如果您正在为类似生产的环境设置 mTLS，拥有有效的域名(或使用通配符证书)将有助于确保更顺利的实施。
- **访问 Istio 文档**。随手准备 [Istio 官方文档](https://istio.io/latest/docs/)。它将是您配置 Istio 功能(包括 mTLS)的主要参考资源。

注意：本教程假设您在受控环境中学习和实验。在生产环境中实施 mTLS 等安全措施需要仔细的规划、协调和额外的安全措施。请务必参考与您的具体用例相关的最佳实践和安全指南。

如果您已经准备好了所有这些先决条件，那么让我们开始吧。

## 第 1 步：安装 Istio

Istio 充当服务网格，为 Kubernetes 集群中的服务增加控制和可观测性。它通过提供流量管理、负载均衡等功能，简化了像 mTLS 这样的安全功能的实现。

要安装 Istio，可以使用其官方安装工具 [istioctl](https://istio.io/latest/docs/reference/commands/istioctl/)。

下载 Istio:

```bash
curl -L https://istio.io/downloadIstio | sh -
```

移动到 Istio 包目录:


```bash
cd istio-*
```

将 Istio 添加到你的 PATH:


```
export PATH=$PWD/bin:$PATH
```

安装 Istio 到你的 Kubernetes 集群:

```bash
istioctl install
```

## 第 2 步：部署示例服务

我们首先设置样本服务。我们将模拟两个微服务，即服务 A 和服务 B，以展示安全通信。这些服务稍后将被配置为使用 mTLS 进行通信。

### 使用 Kubernetes Deployment 部署

在 Kubernetes 中，Deployment 资源很适合管理应用程序的生命周期。使用部署 YAML 文件部署服务 A 和服务 B，这些文件定义要运行的实例数量以及应该如何管理它们。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
 name: service-a
 labels:
  app: service-a
 spec:
  replicas: 1
  selector:
   matchLabels:
    app: service-a
  template:
   metadata:
    labels:
     app: service-a
   spec:
    containers:
     - name: service-a
     image: your-service-a-image:tag
```

服务 B 的类似 YAML。

### 启用 Sidecar 注入

Istio 利用 [sidecar 容器](https://thenewstack.io/operators-and-sidecars-are-the-new-model-for-software-delivery/)将 mTLS 等功能注入到应用程序 Pod 中。使用 `sidecar.istio.io/inject: "true"` 注解部署

```yaml
metadata:
 annotations:
  sidecar.istio.io/inject: "true"
```

## 第 3 步：配置 mTLS

Istio 的 `DestinationRule` 资源对于配置 mTLS 至关重要。它允许您定义流量策略，包括像 TLS 模式这样的安全设置。以下是如何创建 DestinationRule 来实施 mTLS:

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
 name: enable-mtls
spec:
 host: service-a.default.svc.cluster.local  # Update with actual service name
 trafficPolicy:
  tls:
   mode: ISTIO_MUTUAL
```

## 第 4 步：生成证书

自动化证书生成过程是 Istio Citadel 组件的关键功能，特别是在通过 mTLS 建立安全连接的上下文中。这些数字证书在促进 Istio 服务网格内服务之间的安全通信中发挥着基础性作用。

Citadel 确保网格内的每个服务都拥有有效的证书，这是 mTLS 的相互认证机制的关键要求。此认证要求客户端和服务器都提供有效的证书，从而加强了它们连接的安全性。

这种自动化不仅带来了便利性，还大大减少了与创建、分发和续订证书相关的手动工作量。通过自动化证书管理，可以减轻潜在的人为错误，并简化整个过程。

Citadel 在消除手动干预方面的作用不仅提高了运营效率，还有助于安全基础设施的可靠性。

此外，自动化方法可以确保整个集群的一致性。集成到 Istio 服务网格的所有服务都会收到最新证书，培育统一和安全的通信环境。这种一致性对于维护健壮的安全体系至关重要，特别是在动态和分布式架构中。

## 第 5 步：使用端口转发验证安全通信

### 使用端口转发

要验证安全通信，请使用 Kubernetes 端口转发在本地访问部署的服务:

```bash
kubectl port-forward service/service-a 8080:80
```

### 通过可观测工具监视

Istio 提供了像 [Kiali](https://kiali.io/) 和 [Grafana](https://thenewstack.io/will-grafana-become-easier-to-use-in-2022/) 这样的[可观测性](https://thenewstack.io/observability/)工具来监控 mTLS 流量。这些工具可以洞察流量流、安全策略和通信趋势。

## 第 6 步：清理

### 资源清理

在测试 mTLS 之后，清理资源以防止不必要的资源消耗是必不可少的。删除服务、部署、Istio 配置并禁用 Istio 的 sidecar 注入。

```bash
kubectl delete -f service-a.yaml
kubectl delete -f service-b.yaml
kubectl label namespace <namespace> istio-injection-
istioctl x uninstall --purge
```

通过遵循这些步骤，您将成功地实现了 mTLS 以增强 Kubernetes 集群中微服务之间的通信安全性。

请记住，虽然本教程提供了全面指南，但实际过程可能会因您的具体环境和需求而有所不同。请始终参考 Istio 最新官方文档。

## 接下来呢？

随着您深入了解 mTLS，请探索 Istio 等服务网格提供的更广泛利益。Istio 不仅提供 mTLS，还提供全套安全和可观测性工具。它赋予流量的细粒度控制，促进强大的访问控制策略并对应用程序网格的行为提供实时见解。

探索这些方面不仅巩固了微服务的通信，还让您获得了强大的工具包来增强整体系统的安全性和监控能力。

在测试 mTLS 之后，清理资源以防止不必要的资源消耗是必不可少的。删除服务、部署、Istio 配置并禁用 Istio 的 sidecar 注入。

通过加密 Kubernetes 环境中的通信，利用 mTLS 的强大功能，并查看 Istio 的更广泛的特性，你不仅加强了微服务架构的基础，还采用了一种整体的方法来进行安全、高效和弹性的应用程序开发。
