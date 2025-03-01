# 使用 Kro 和 Kubernetes 编排云原生工作负载

![使用 Kro 和 Kubernetes 编排云原生工作负载的特色图片](https://cdn.thenewstack.io/media/2025/02/2667bd7f-planet-volumes-th2ottz_roq-unsplash-1024x643.jpg)

在[本系列的第一部分](https://thenewstack.io/kubernetes-gets-a-new-resource-orchestrator-in-the-form-of-kro/)中，我介绍了 Kube 资源编排器（[Kro](https://kro.run/docs/overview/)）的背景。在本期中，我们将为 WordPress 定义一个资源图定义，并通过将其创建为 Kro 应用程序来部署多个实例。

为了理解和欣赏 Kro 的强大功能，想象一下一家托管公司，专门为各种客户部署和管理 WordPress 网站——每个客户都有独特的品牌、自定义域名和特定的性能要求。该公司需要一个一致的 WordPress 部署定义，同时只需更改每个客户的几个参数。Kro 完全适合此用例。

通过利用 RGD 作为 WordPress 部署的集中蓝图，该公司可以确保每个网站都符合一致且优化的配置，同时允许进行个性化定制。这种分离意味着核心设置（涵盖数据库配置、持久性存储和入口规则等组件）在一个强大且可重复使用的定义中维护，简化了所有网站的更新和安全补丁。

同时，可以使用特定于客户的设置（例如唯一凭据和自定义域名）定制各个应用程序实例，从而实现快速入职并降低手动错误的风险。这种方法不仅简化了操作，还增强了可扩展性和可靠性，使托管提供商更容易有效地管理不断增长的 WordPress 网站组合。

本教程将把 WordPress 工作负载定义为一个 RGD，该 RGD 封装了所有必需的 Kubernetes 资源，例如密钥、卷、部署、服务和入口。然后，我们将定义两个实例，分别代表该托管公司的不同客户或租户。

为完整起见，本教程包含从头到尾的所有步骤，以探索 Kro。

## 步骤 1 — 安装和配置 Minikube

```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-darwin-arm64 && sudo install minikube-darwin-arm64 /usr/local/bin/minikube
```

让我们启动 Minikube 并配置存储和入口。我们将使用 Rancher 本地路径作为存储提供程序。

```bash
minikube start
minikube addons enable ingress
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.31/deploy/local-path-storage.yaml
```

最后，安装 Helm。

```bash
brew install helm
```

## 步骤 2 — 在 Minikube 上安装 Kro

首先，获取 Kro 的最新发行版本，然后将其作为 Helm chart 安装到其自己的[命名空间](https://thenewstack.io/what-are-linux-namespaces-and-how-are-they-used/)中：

```bash
export KRO_VERSION=$(curl -sL "https://api.github.com/repos/kro-run/kro/releases/latest" | jq -r '.tag_name | ltrimstr("v")')
helm install kro oci://ghcr.io/kro-run/kro/kro --namespace kro --create-namespace --version=${KRO_VERSION}
```

这将在我们的 Kubernetes 集群中创建一个 CRD。

## 步骤 3 — 使用 Kro 部署 WordPress 应用程序

创建一个包含资源图定义的[YAML 文件](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)。此文件聚合了 WordPress 部署所需的所有 Kubernetes 对象，包括 MySQL 组件、PersistentVolumeClaims、部署、服务和可选的入口资源：

在上面的 WordPress RGD 中，定义结构分为两个主要部分：模式和资源模板。

模式指定 WordPress 部署的关键参数，例如应用程序名称、MySQL 密码（Base64 编码）、存储类以及是否应启用入口。操作员可以自定义这些值，而无需直接编辑多个 Kubernetes 对象。

然后，资源模板使用这些模式值动态生成所有必要的 Kubernetes 资源，包括用于存储 MySQL 凭据的密钥、用于 MySQL 和 WordPress 数据的 PersistentVolumeClaims、用于运行 MySQL 和 WordPress Pod 的部署和服务，以及可选的用于外部访问的入口。

这种统一的方法通过将多个相互依赖的组件聚合到单个逻辑单元中来简化部署过程。它还确保在资源创建期间的一致性和正确的顺序。因此，管理像 WordPress 这样的复杂应用程序变得更高效、更可预测且更不容易出错，因为任何对配置参数的更改都会自动传播到所有相关的资源。

上述步骤将产生一个名为 wp-app 的新 RGD。

## 步骤 4 — 部署两个应用程序实例
创建另一个 YAML 文件（例如，`wordpress-apps.yaml`），以实例化您的 ResourceGraphDefinition。这里定义了两个 WordPress 应用程序，它们具有自定义名称、MySQL 密码、存储设置和启用的 Ingress：

将 RGD 与单个应用程序实例分开具有显著优势，特别是对于为多个客户部署 WordPress 站点的托管公司而言，可以使用自定义域名。

基于 RGD 的单个应用程序实例允许进行特定于客户的自定义，例如唯一的 MySQL 凭据、存储配置和自定义域名设置，而无需修改底层蓝图。这种分离简化了维护，加快了新客户的入职流程，并最大限度地降低了错误风险，因为核心配置只需定义一次，然后即可根据实例进行参数化。

请注意我们只更改了必需的参数。如果要扩展此功能，请将 Ingress 主机名更改为参数。

部署应用程序后，它们应该变为活动状态并同步。

这些应用程序由 Kro 控制器转换为各种 Kubernetes 资源。

添加 HOST DNS 条目并通过 Chrome 的 Mod Header 等扩展程序修改 Header 后，我们可以访问 WordPress 站点。访问站点之前，请不要忘记启动 Minikube Tunnel。

我希望本教程为您提供了对 Kro 及其使用流程的全面概述。

[YouTube 频道](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收听我们所有的播客、访谈、演示等等。