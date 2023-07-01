# 在边缘设备上安装 Korifi 以管理 K3s 


通过安装 Cloud Foundry Korifi 抽象层，可以更轻松地在边缘设备和物联网设备上启用 Kubernetes 。

翻译自 [Install Korifi to Manage K3s at the Edge](https://thenewstack.io/install-korifi-to-manage-k3s-at-the-edge/) 。

![](https://cdn.thenewstack.io/media/2023/04/259d121e-korifi-1024x683.jpg)

[Cloud Foundry Korifi](https://www.cloudfoundry.org/technology/korifi/) 是将 Cloud Foundry 抽象层移植到 Kubernetes 集群中的熟悉工具。它为 Kubernetes 带来了多租户体验，并帮助应用开发人员轻松使用集群。它提供了一个回答社区中许多人提出的问题的解决方案：“ Cloud Foundry 用户迁移到 Kubernetes 的最佳方式是什么？”

Korifi 通过在 Kubernetes 集群中安装来实现功能。尽管纯粹的 Kubernetes 是理想的选择，但每个托管云提供商在 Kubernetes 上有一些细微的变化。因此，我们正在创建针对每个云提供商的特定教程。尽管这可能意味着又一个开源项目的分散，但每个云提供商都有其特定用途的优势，例如用于生产环境或内部团队使用等。因此，编写指南以在每个提供商上安装和使用 Korifi 是有意义的。

因此，现在我们介绍第一个关于在流行的轻量级 K3s 上部署 Korifi 的教程。

[K3s](https://k3s.io/) 是一个轻量级的 Kubernetes 发行版，专为资源受限的环境（如边缘计算或物联网设备）而设计。最初， K3s 由 Rancher Labs 开发， Rancher Labs 是一家专门提供 Kubernetes 管理解决方案的公司。在 2020 年， SUSE 收购了 Rancher Labs ，而 K3s 的开发和维护现在由开源社区推动。 K3s 取得了显著的进展，并且拥有不断增长的贡献者社区。它已经发展成为一个成熟且稳定的项目，定期发布新版本，最新版本是 [25.10-rc1+k3s1](https://github.com/k3s-io/k3s/releases) 。

K3s 的小型占用空间使其能够在计算能力较低的设备上运行，非常适用于物联网部署。K3s 还非常适用于资源有限且连接可能不稳定的边缘计算场景。它使开发人员能够将 Kubernetes 集群部署在靠近边缘设备的位置，减少延迟并增强数据处理能力。

在本教程中，我们将介绍如何在 K3s 集群上安装 Cloud Foundry Korifi 。我们将首先安装 Kubernetes （以K3s的形式），然后将 Korifi CRD 安装到集群中。教程的最后一步将是部署一个应用程序到集群中的示例。

但首先，对 [Cloud Foundry](https://www.cloudfoundry.org/?utm_content=inline-mention) Korifi 进行更多介绍。 [Korifi](https://github.com/cloudfoundry/korifi/tree/main) 是由 Cloud Foundry 社区构建的开源软件。它是基于对在 Kubernetes 上构建内部开发平台的需求而诞生的。Korifi 的目的是在 Kubernetes 上提供一个更高级的抽象层，最终使开发人员能够专注于构建应用程序。它是一个[完全开源的工具](https://github.com/cloudfoundry/korifi)，旨在用于在 Kubernetes 上部署应用程序，并提供自动化的网络、安全、可用性等功能。现在，让我们开始吧。

先决条件：请安装以下工具以开始。

* [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
* [cf](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html) CLI v8.5或更高版本
* [Helm](https://helm.sh/docs/intro/install/)

## 第 1 步：安装 K3s 。

```shell
curl -sfL https://get.k3s.io | sh -s - --disable traefik --write-kubeconfig-mode 644
```

这些指令在快速入门指南中已经很清楚了。然而，我们需要配置一些额外的参数来适应我们的安装。`--disable traefik` 参数被传递给安装脚本，以禁用 Traefik Ingress Controller 的安装。这是因为我们将在稍后的步骤中安装 Contour 进行 Ingress 控制，而两者会产生冲突。

脚本传递的第二个参数是 `--write-kubeconfig-mode 644` 。这将设置生成的 kubeconfig 文件的文件权限模式为 644 ，这意味着所有者具有读写权限，而其他用户只有读取权限。K3s 安装过程中默认不执行此操作。如果跳过此步骤，我们将无法使用 kubectl 与集群连接，而这是后续操作所需的。

## Step 2: 设置环境变量

```shell
export ROOT_NAMESPACE="cf"
export KORIFI_NAMESPACE="korifi"
export ADMIN_USERNAME="system:admin"
export BASE_DOMAIN="localhost"
```

这只是为了方便起见的一步。我们可以在后续步骤中使用环境变量。

## Step 3: 安装 Cert Manager

```shell
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.yaml
```
[Cert Manager](https://cert-manager.io/docs/) 通过一个 kubectl apply 命令进行安装，路径中引用了最新版本的 yaml 定义文件。

Cert Manager 是一个专为 Kubernetes 集群设计的开源证书管理解决方案。它帮助自动化管理和颁发 X.509 证书，用于保护 Kubernetes 环境中各个组件和服务之间的通信。

Cert Manager 项目通过自定义资源定义（CRD）扩展了 Kubernetes ，用于定义与证书相关的对象，如 Certificate、CertificateRequest 和 ClusterIssuer 。使用 Cert Manager，Kubernetes 用户可以简化集群中 TLS 证书的管理。它确保所有必要的组件，如入口控制器、Pod和服务，都具有有效和最新的证书，从而增强 Kubernetes 环境的安全性和可靠性。

## Step 4: 安装 kpack

kpack 是一个与 Kubernetes 集成的开源项目，用于提供容器本地构建过程。它使用 Cloud Native Buildpacks 来导出 OCI 兼容的容器。通过使用 kpack ，开发人员可以采用云原生的方式构建和打包应用程序，以便在 Kubernetes 集群上部署。

kpack 通过一个 kubectl apply 命令进行安装，路径中引用了最新版本的 yaml 定义文件。

```shell
kubectl apply -f https://github.com/pivotal/kpack/releases/download/v0.11.0/release-0.11.0.yaml
```

## Step 5: 创建 Root Namespaces

```shell
cat <<EOF | kubectl apply -f -

apiVersion: v1
kind: Namespace
metadata:
  name: $ROOT_NAMESPACE
  labels:
     pod-security.kubernetes.io/audit: restricted
     pod-security.kubernetes.io/enforce: restricted

EOF
```

```shell
cat <<EOF | kubectl apply -f -

apiVersion: v1
kind: Namespace
metadata:
  name: $KORIFI_NAMESPACE
  labels:
     pod-security.kubernetes.io/audit: restricted
     pod-security.kubernetes.io/enforce: restricted
EOF
```

在这一步中，我们创建了 cf 和 korifi 命名空间。

## Step 6: 安装 Contour

```shell
kubectl apply -f https://projectcontour.io/quickstart/contour.yaml
```

Contour 是一个基于 Envoy 代理构建的用于 Kubernetes 的开源 Ingress 控制器。 Ingress 控制器是 Kubernetes 中管理集群内服务的入站网络流量的资源。它充当网关，为集群内运行的服务提供外部访问。 Contour 专注于提供用于管理 Kubernetes 中的 Ingress 的高级功能和能力。

## Step 7: 创建一个用于访问容器注册表的密钥

```shell
kubectl --namespace "cf" create secret docker-registry image-registry-credentials --docker-server="us-central1-docker.pkg.dev" --docker-username="_json_key" --docker-password "$(awk -v RS= '{$1=$1}1' ~/Downloads/summit-labs-8ff7123608fe.json)"
```

容器注册表用于管理在集群上部署的所有容器。在构建工作流程结束时，将包上传到容器注册表，并在运行工作流程开始时从注册表中拉取容器。在这种情况下，我们使用 [Google Artifact Registry](https://cloud.google.com/artifact-registry) 来推送和拉取镜像。

也可以使用其他容器注册表（如 Docker Hub、Github 容器注册表等）。请参阅安装文档获取具体信息。

## Step 8: 安装 Korifi

```shell
helm install korifi https://github.com/cloudfoundry/korifi/releases/download/v0.7.1/korifi-0.7.1.tgz --namespace="korifi" --set=global.generateIngressCertificates=true --set=global.rootNamespace="cf" --set=global.containerRegistrySecret="image-registry-credentials" --set=adminUserName="system:admin" --set=api.apiServer.url="api.localhost" --set=global.defaultAppDomainName="apps.localhost" --set=global.containerRepositoryPrefix="us-central1-docker.pkg.dev/summit-labs/korifi/korifi-" --set=kpackImageBuilder.builderRepository="us-central1-docker.pkg.dev/summit-labs/korifi/kpack-builder" --wait
```

使用官方 Helm chart 安装 Korifi 。每个版本都有对应的 Helm chart ，由社区进行更新。在[此处](https://github.com/cloudfoundry/korifi/blob/main/README.helm.md)可以找到所有可用于自定义 Helm chart 的选项。

## Step 9: 通过 Cloud Foundry API 进行身份验证

```shell
cf api https://api.localhost --skip-ssl-validation
cf login
```

身份验证 Cloud Foundry API 需要两个步骤。第一步是设置 API 的 URL 。第二步是登录命令。登录命令会提示您选择要使用的不同用户身份。选择默认身份以继续。

## Step 10: 创建 Org 和 Space

```shell
cf create-org acme-corp
cf target -o acme-corp
cf create-space -o acme-corp foo-bu && cf target -o acme-corp -s foo-bu
```

在 Cloud Foundry 中：

- target 是设置 Cloud Foundry 实例中的活动组织和空间。
- 组织（org）是用户、应用程序和服务的逻辑分组，提供管理和协作控制。
- 空间（space）是组织内的一个子分区，为不同团队或项目提供隔离和独立性，用于开发和管理其应用程序和服务。

## Step 11: 部署应用程序

```shell
cf push mighty-monkey -p ~/sandbox/korifi/tests/smoke/assets/test-node-app/
```
使用单个 `cf push` 命令将应用程序部署到安装了 Korifi 的 K3s 实例上。

## 结论

Cloud Foundry 社区的目标是使 Korifi 成为处理大量应用程序开发人员并希望使用工具来帮助他们大规模管理 Kubernetes 集群的运营商的首选工具。 Korifi 是基于 Cloud Foundry 数十年的生产卓越经验构建的。在运行 Korifi 的 K3s 实例上，部署到边缘和运行 Kubernetes 的物联网设备将变得更简单。