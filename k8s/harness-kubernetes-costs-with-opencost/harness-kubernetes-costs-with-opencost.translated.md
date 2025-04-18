# 利用 OpenCost 掌握 Kubernetes 成本

我参加的每次活动中，大家讨论（或者说抱怨）最多的就是如何管理 Kubernetes 的复杂性和成本。最近的一项调查[发现](https://www.infoq.com/news/2024/03/cncf-finops-kubernetes-overspend/)，近一半的公司发现 Kubernetes 增加了云支出。Kubernetes 的普遍性日益明显，并且每天对更好地管理它的需求都在增长。

[为了管理 Kubernetes 的复杂性](https://thenewstack.io/managing-kubernetes-complexity-in-multicloud-environments/)，我们可以选择一个用于抽象它的底层。为此，让我们使用开源 Cloud Foundry [Korifi](https://github.com/cloudfoundry/korifi)，它是一个构建在 Kubernetes 上的抽象层，可以简化应用程序的部署和管理。为了管理成本，让我们采用 [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) 的孵化项目 [OpenCost](https://github.com/opencost/opencost)，它提供全面的成本可见性和优化功能。

## Korifi 和 OpenCost 简介

以下教程的先决条件是需要了解这些工具。Cloud Foundry Korifi 旨在将 Cloud Foundry 的最佳体验带到 Kubernetes。它在 Kubernetes 上提供了一个更高级别的抽象，[简化了开发人员的应用程序部署和管理](https://thenewstack.io/simplifying-cloud-native-application-development-with-ballerina/)。

**以下是其主要功能的细分：**

- 简化应用程序部署：Korifi 允许开发人员使用熟悉的 Cloud Foundry 命令（例如 cf push）将应用程序部署到 Kubernetes。这抽象了[Kubernetes YAML 配置](https://thenewstack.io/tutorial-configure-storage-volumes-for-kubeflow-notebook-servers/)的复杂性，使部署更容易、更快捷。
- 语言和框架无关：开发人员可以使用各种语言和框架构建的应用程序，而无需担心底层的 Kubernetes 配置。
- 自动化网络和安全：Korifi 自动化网络和安全任务，例如服务发现、路由和安全策略，从而增强应用程序的可靠性和安全性。
- 增强的开发人员体验：通过提供精简且用户友好的体验，Korifi 使开发人员能够专注于[构建应用程序，而不是与复杂的 Kubernetes](https://thenewstack.io/build-vs-buy-compare-your-kubernetes-platform-options/) 配置作斗争。

## 什么是 OpenCost？

OpenCost 是一个开源平台，可提供跨整个云基础设施的全面[成本可见性](https://thenewstack.io/it-leaders-brace-for-tariff-fallout-on-infrastructure-and-cloud-costs/)。对于任何[希望控制其云成本的 DevOps 团队](https://thenewstack.io/chaos-under-control-addressing-cloud-infrastructure-drift/)来说，OpenCost 都是一个强大的工具。通过提供精细的可见性、深刻的分析和灵活的平台，OpenCost 使您能够优化云支出并最大程度地提高云投资的回报。

在当今的云原生世界中，了解和优化云支出对于任何组织（无论规模大小）都至关重要。以下是 OpenCost 众多优势的简短列表。

- 开源且可定制：OpenCost 基于开源原则构建，具有灵活性，能够根据您的特定需求进行定制，并能够将其无缝集成到您现有的基础设施中。
- 支持多个云提供商：无论您使用 AWS、Azure、GCP 还是它们的组合，OpenCost 都可以提供跨所有平台的统一云支出视图。
- 数据驱动的决策：OpenCost 提供了大量数据和可视化效果，可帮助您深入了解云成本，并就云战略做出明智的决策。
- 社区驱动的开发：受益于活跃的开发人员和用户社区，他们为平台的持续开发和改进做出贡献。

### 如何安装 Cloud Foundry Korifi 和 OpenCost

本指南将演示如何在本地 Kubernetes 集群 (KiND) 上安装 Cloud Foundry Korifi 和 OpenCost。

**先决条件：**

- 确保您已在系统上安装并配置了 Helm 3。
- 使用官方说明安装 KiND。
- 安装 kubectl 以管理您的集群。

**安装 Korifi：**

- 通过内联应用以下配置，使用 KiND 创建 Kubernetes 集群：

```
12345678910111213141516171819202122232425 |
```
```
```yaml
cat <<EOF | kind create cluster --name korifi --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
containerdConfigPatches:
  - |-
    [plugins."io.containerd.grpc.v1.cri".registry]
      [plugins."io.containerd.grpc.v1.cri".registry.mirrors]
        [plugins."io.containerd.grpc.v1.cri".registry.mirrors."localregistry-docker-registry.default.svc.cluster.local:30050"]
          endpoint = ["http://127.0.0.1:30050"]
      [plugins."io.containerd.grpc.v1.cri".registry.configs]
        [plugins."io.containerd.grpc.v1.cri".registry.configs."127.0.0.1:30050".tls]
          insecure_skip_verify = true
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 32080
        hostPort: 80
        protocol: TCP
      - containerPort: 32443
        hostPort: 443
        protocol: TCP
      - containerPort: 30050
        hostPort: 30050
        protocol: TCP
EOF

```

- 使用以下安装程序安装 Korifi 基础：

```bash
kubectl apply -f https://github.com/cloudfoundry/korifi/releases/latest/download/install-korifi-kind.yaml
```

- 接下来，使用 Helm 安装 OpenCost：

```bash
helm repo add opencost https://charts.opencost.io
```

- 确保更新 Helm：

```bash
helm repo update
```

- 接下来，使用 Helm 安装：

```bash
helm install opencost opencost/opencost
```

- 使用以下命令验证安装：

```bash
kubectl get pods -n opencost
```

- OpenCost 完成安装后，等待所有 OpenCost pod 达到“Ready”状态。然后，使用以下命令建立本地端口转发连接：

```bash
kubectl port-forward --namespace opencost service/opencost 9003 9090
```

- 通过访问 localhost:9090 从浏览器访问 OpenCost UI。
下图显示了 OpenCost 如何提供每个 pod 的有用信息。对于 Korifi，pod 代表一个构建。因此，我们现在可以看到每个构建的成本，否则这些成本将永远无法获得。

检查每个命名空间的成本对于推导责任、推动优化和识别异常非常有用。以下是使用 OpenCost 的可视化效果示例。

## 总结
现在你已经了解了。现在，你可以了解和优化你的成本——最重要的是，通过利用开源软件。

与 Korifi 一起部署的 OpenCost 可以监控“构建”、“部署”以及构成整个集群的其他原语的成本。OpenCost 可以将成本分解为原子组件，这有助于以全新的维度综合理解 Kubernetes 集群。

但为什么要首先这样做呢？为了最大限度地利用云计算，[工程团队必须开始了解](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/)所涉及的基础设施成本。这并不意味着要密切关注 AWS 账单。这也意味着要扩大应用程序部署、CI/CD 成本、可观测性成本等的透明度。有了这些信息，工程团队可以就为其堆栈分配正确的资源做出更具变革性的决策。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)
```