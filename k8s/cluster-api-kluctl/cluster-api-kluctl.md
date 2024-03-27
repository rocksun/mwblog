
<!--
title: 使用Kluctl管理Cluster API
cover: https://kluctl.io/images/blog/2024-03-13-cluster-api-kluctl.png
-->

Kubernetes 最初是一个非常有前途的容器编排器，在我看来，很明显它会在第一天就确立自己的地位并占领市场。对我来说不太明显的是，Kubernetes 还会演变成某种“API 平台”。

> 译自 [Managing Cluster API with Kluctl](https://kluctl.io/blog/2024/03/13/cluster-api-kluctl/)，作者 Alexander Block。

随着 [自定义资源定义](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) 的引入，Kubernetes 现在可以管理各种资源。[控制器和 operator](https://book.kubebuilder.io/cronjob-tutorial/controller-overview.html#whats-in-a-controller) 采用这些自定义资源并使用协调模式来持续协调所需状态与现实世界。

事后看来，下一步很明显，但对我个人来说仍然是一个惊喜：为什么不从 Kubernetes 集群内部管理 Kubernetes 集群本身。[集群 API](https://cluster-api.sigs.k8s.io/) 诞生了。

## 自定义资源的影响

以自定义资源的形式存在也意味着它成为常规 Kubernetes 资源，可以使用 Kubernetes 生态系统中的所有可用工具进行管理。它可以用纯 Kubectl 管理，也可以用更高级的工具管理，如 [Helm](https://helm.sh/), [Flux](https://fluxcd.io/), [ArgoCD](https://argo-cd.readthedocs.io/en/stable/) 或 [Kluctl](https://kluctl.io)。

## 那么，为什么是 Kluctl？

Kluctl 是 Kubernetes 的通用部署工具。它允许你定义任何复杂程度的 Kubernetes 部署，并通过 [统一的 CLI](https://kluctl.io/docs/kluctl/commands/) 和/或可选的 [GitOps 控制器](https://kluctl.io/docs/gitops/) 管理它们。以下是使 Kluctl 对基于集群 API 的集群管理变得有趣的一些特性。

- [Targets](https://kluctl.io/docs/kluctl/kluctl-project/targets/) 允许你使用相同的 Kluctl 部署项目管理多个工作负载集群。
- [Templating](https://kluctl.io/docs/kluctl/templating/) 允许你遵循自然的项目结构，而无需使用覆盖和修补来满足简单要求。
- [部署项目](https://kluctl.io/docs/kluctl/deployments/deployment-yml/) 允许你重复使用参数化和模板化的子组件，而无需复制粘贴。
- [变量源](https://kluctl.io/docs/kluctl/templating/variable-sources/) 为工作负载集群提供了易于理解且结构化的配置。
- [Kluctl diff](https://kluctl.io/docs/kluctl/commands/diff/) 命令在更改内容时始终会告诉你是否正确（因为它基于服务器端空运行）。
- [GitOps](https://kluctl.io/docs/gitops/) 得到完全支持，但也是可选的。它甚至可以与经典的推送式 CLI [混合](https://kluctl.io/docs/kluctl/commands/gitops-deploy/)。

## 安装 Kluctl

对于本教程，你需要安装 Kluctl CLI。请按照 [此处](https://kluctl.io/docs/kluctl/installation/#installing-the-cli) 的说明进行操作。无需安装 GitOps 控制器或 Webui，但教程结束后，你可以随意试用它们。

### 让我们设置集群 API

在本教程中，我们将完全在本地工作，不涉及任何云资源。这意味着，我们正在使用 [Kind](https://kind.sigs.k8s.io/) 和 CAPD（集群 API Docker）基础设施提供程序。在现实世界中，你需要将此处学到的原则调整为适当的集群 API 基础设施提供程序。

首先，让我们设置一个本地 Kind 集群。如果你尚未安装 Kind，请阅读 [安装说明](https://kind.sigs.k8s.io/#installation-and-usage)。

CAPD 提供程序需要从 Kind 集群内部访问主机 Docker 守护进程。要授予访问权限，你需要通过 Docker unix 套接字进行传递。这可以通过使用自定义 Kind 配置来完成：

```yaml
# contents of kind-config.yaml

kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  ipFamily: dual
nodes:
- role: control-plane
  extraMounts:
  - hostPath: /var/run/docker.sock
    containerPath: /var/run/docker.sock
```

现在使用上述配置创建集群：

```
$ kind create cluster --config kind-config.yaml
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.29.2) 🖼
 ✓ Preparing nodes 📦
 ✓ Writing configuration 📜
 ✓ Starting control-plane 🕹️
 ✓ Installing CNI 🔌
 ✓ Installing StorageClass 💾
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Have a nice day! 👋
```

将 kubectl 上下文设置为“kind-kind”，从现在开始，我们将使用它来安装集群 API。让我们这么做：

```
$ clusterctl init --infrastructure docker
Fetching providers
Installing cert-manager Version="v1.13.2"
Waiting for cert-manager to be available...
Installing Provider="cluster-api" Version="v1.6.1" TargetNamespace="capi-system"
Installing Provider="bootstrap-kubeadm" Version="v1.6.1" TargetNamespace="capi-kubeadm-bootstrap-system"
Installing Provider="control-plane-kubeadm" Version="v1.6.1" TargetNamespace="capi-kubeadm-control-plane-system"
Installing Provider="infrastructure-docker" Version="v1.6.1" TargetNamespace="capd-system"

Your management cluster has been initialized successfully!

You can now create your first workload cluster by running the following:

  clusterctl generate cluster [name] --kubernetes-version [version] | kubectl apply -f -
```

我们现在拥有一个功能齐全的 Cluster API 安装，它能够以 Docker 容器的形式配置和管理工作负载集群。

## 基本项目结构

让我们讨论一下我们将为本教程遵循的基本 Kluctl 项目结构。您可以在 [https://github.com/kluctl/cluster-api-demo](https://github.com/kluctl/cluster-api-demo) 找到完整的项目。此存储库包含多个子目录，其中包含不同版本的项目。第一个版本（如本节和下一节中所述）位于 `1-initial` 中。

根目录将包含 2 个文件。

第一个是 [.kluctl.yaml](https://kluctl.io/docs/kluctl/kluctl-project/) 文件，它指定存在哪些 [targets](https://kluctl.io/docs/kluctl/kluctl-project/targets/)。目标定义使用 Kluctl 项目在何处/部署什么，可以是您想要的任何内容。在经典的应用程序部署中，它将是目标环境。在这种情况下，目标表示部署到 Cluster API 管理集群（我们的 Kind 集群）的 Cluster API 工作负载集群。它充当配置管理的入口点，稍后将允许我们加载特定于集群的配置。

```yaml
# content of .kluctl.yaml

targets:
  - name: demo-1
    context: kind-kind
  - name: demo-2
    context: kind-kind

discriminator: capi-{{ target.name }}
```

您还可以看到此处在 `discriminator` 中首次使用模板。`discriminator` 稍后用于区分之前已应用于集群的资源。这对于清理任务（如修剪或删除）很有用。

第二个文件是 [deployment.yaml](https://kluctl.io/docs/kluctl/deployments/deployment-yml/)，它定义了实际的部署项目。它包括 Kustomize 部署、Helm 图表和其他子部署项目。

```yaml
# content of deployment.yaml
deployments:
  - include: clusters

commonAnnotations:
  kluctl.io/force-managed: "true"
```

这将在 “clusters” 目录中包含一个子部署。在此目录中，必须有另一个 `deployment.yaml`。在 [commonAnnotations](https://kluctl.io/docs/kluctl/deployments/deployment-yml/#commonannotations)`中找到的注释将导致 Kluctl [始终将](https://kluctl.io/docs/kluctl/deployments/annotations/all-resources/#kluctlioforce-managed) 资源视为由 Kluctl 管理。这是必需的，因为 Cluster API [声明对资源的所有权](https://github.com/kubernetes-sigs/cluster-api/issues/5487#issuecomment-950824947)，即使它无法控制这些资源。

```yaml
# content of clusters/deployment.yaml

deployments:
  - path: {{ target.name }}
```

这将包含一个 [Kustomize](https://kluctl.io/docs/kluctl/deployments/deployment-yml/#kustomize-deployments) 部署，该部署来自通过模板 `{{ target.name }}` 解析的目录。“target” 是始终存在的全局变量，它允许您访问当前目标中使用的属性，该属性在上面的 `.kluctl.yaml` 中定义。这意味着，如果您稍后部署目标 “demo-1”，Kluctl 将加载在 “clusters/demo-1” 文件夹中找到的 Kustomize 部署。

## 创建工作负载集群

现在，在 `clusters/demo-1` 目录中创建以下文件：


```yaml
# contents of clusters/demo-1/kustomization.yaml

resources:
  - namespace.yaml
  - cluster.yaml
  - control-plane.yaml
  - workers.yaml
```

上述文件是一个常规的 `kustomization.yaml`，其中包含实际资源。Kluctl 完全支持 [Kustomize](https://kluctl.io/docs/kluctl/deployments/kustomize/) 及其所有功能。在大多数情况下，您也可以省略 `kustomization.yaml`，导致 Kluctl [自动生成](https://kluctl.io/docs/kluctl/deployments/deployment-yml/#simple-deployments) `kustomization.yaml`。然而，在这种情况下，不建议这样做，因为这里的顺序很重要：必须在其他任何内容之前部署命名空间。

```yaml
# contents clusters/demo-1/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: cluster-demo-1
```

我们为此集群创建了一个专用命名空间。稍后，我们还将为每个其他集群创建更多命名空间。

```yaml
# contents of clusters/demo-1/cluster.yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  name: "demo-1"
  namespace: "cluster-demo-1"
spec:
  clusterNetwork:
    services:
      cidrBlocks: ["10.128.0.0/12"]
    pods:
      cidrBlocks: ["192.168.0.0/16"]
    serviceDomain: "cluster.local"
  infrastructureRef:
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: DockerCluster
    name: "demo-1"
    namespace: "cluster-demo-1"
  controlPlaneRef:
    kind: KubeadmControlPlane
    apiVersion: controlplane.cluster.x-k8s.io/v1beta1
    name: "demo-1-control-plane"
    namespace: "cluster-demo-1"
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: DockerCluster
metadata:
  name: "demo-1"
  namespace: "cluster-demo-1"
```


上述文件描述了一个 [集群](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/cluster.x-k8s.io/Cluster/v1beta1@v1.6.2) 和一个 [Docker 集群](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/infrastructure.cluster.x-k8s.io/DockerCluster/v1beta1@v1.6.2)。请注意，我们没有使用集群拓扑（[ClusterClass](https://cluster-api.sigs.k8s.io/tasks/experimental-features/cluster-class/)）功能。我稍后会解释原因。


```yaml
# contents of clusters/demo-1/control-plane.yaml
kind: KubeadmControlPlane
apiVersion: controlplane.cluster.x-k8s.io/v1beta1
metadata:
  name: "demo-1-control-plane"
  namespace: "cluster-demo-1"
spec:
  replicas: 1
  machineTemplate:
    infrastructureRef:
      kind: DockerMachineTemplate
      apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
      name: "demo-1-control-plane"
      namespace: "cluster-demo-1"
  kubeadmConfigSpec:
    clusterConfiguration:
      controllerManager:
        extraArgs:
          enable-hostpath-provisioner: 'true'
      apiServer:
        certSANs: [localhost, 127.0.0.1, 0.0.0.0]
    initConfiguration:
      nodeRegistration:
        criSocket: /var/run/containerd/containerd.sock
        kubeletExtraArgs:
          cgroup-driver: systemd
          eviction-hard: 'nodefs.available<0%,nodefs.inodesFree<0%,imagefs.available<0%'
    joinConfiguration:
      nodeRegistration:
        criSocket: /var/run/containerd/containerd.sock
        kubeletExtraArgs:
          cgroup-driver: systemd
          eviction-hard: 'nodefs.available<0%,nodefs.inodesFree<0%,imagefs.available<0%'
  version: "1.29.0"
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: DockerMachineTemplate
metadata:
  name: "demo-1-control-plane"
  namespace: "cluster-demo-1"
spec:
  template:
    spec:
      extraMounts:
        - containerPath: "/var/run/docker.sock"
          hostPath: "/var/run/docker.sock"
```

上述文件描述了一个 [KubeadmControlPlane](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/controlplane.cluster.x-k8s.io/KubeadmControlPlane/v1beta1@v1.6.2) 和一个 [DockerMachineTemplate](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/infrastructure.cluster.x-k8s.io/DockerMachineTemplate/v1beta1@v1.6.2) 用于控制平面节点。

```yaml
# contents of clusters/demo-1/workers.yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: DockerMachineTemplate
metadata:
  name: "demo-1-md-0"
  namespace: "cluster-demo-1"
spec:
  template:
    spec: {}
---
apiVersion: bootstrap.cluster.x-k8s.io/v1beta1
kind: KubeadmConfigTemplate
metadata:
  name: "demo-1-md-0"
  namespace: "cluster-demo-1"
spec:
  template:
    spec:
      joinConfiguration:
        nodeRegistration:
          kubeletExtraArgs:
            cgroup-driver: systemd
            eviction-hard: 'nodefs.available<0%,nodefs.inodesFree<0%,imagefs.available<0%'
---
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineDeployment
metadata:
  name: "demo-1-md-0"
spec:
  clusterName: "demo-1"
  replicas: 1
  selector:
    matchLabels:
  template:
    spec:
      clusterName: "demo-1"
      version:  "1.29.0"
      bootstrap:
        configRef:
          name: "demo-1-md-0"
          namespace: "cluster-demo-1"
          apiVersion: bootstrap.cluster.x-k8s.io/v1beta1
          kind: KubeadmConfigTemplate
      infrastructureRef:
        name: "demo-1-md-0"
        namespace: "cluster-demo-1"
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: DockerMachineTemplate
```

上述文件描述了创建节点池所需的一切。这包括一个 [DockerMachineTemplate](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/infrastructure.cluster.x-k8s.io/DockerMachineTemplate/v1beta1@v1.6.2)、一个 [KubeadmConfigTemplate](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/bootstrap.cluster.x-k8s.io/KubeadmConfigTemplate/v1beta1@v1.6.2) 和一个 [MachineDeployment](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/cluster.x-k8s.io/MachineDeployment/v1beta1@v1.6.2)。

## 部署工作负载集群

我们现在有一个可通过 [Kluctl CLI](https://kluctl.io/docs/kluctl/commands/)（稍后我们还将探索 GitOps）部署的 Kluctl 部署项目。执行以下命令：

```
$ kluctl deploy -t demo-1
```

这将执行一次空运行，显示差异，然后在确认后执行实际部署。空运行将产生一些错误，因为底层的服务器端空运行与集群 API 结合使用并不完美，你可以忽略这些错误并简单确认。

几分钟后，工作负载集群应该准备就绪，其中包含一个控制平面节点和一个工作节点，所有这些节点都作为 Docker 容器运行。我们现在需要获取此集群的 kubeconfig。

```
$ kind get kubeconfig --name demo-1 > demo-1.kubeconfig
```

你现在可以测试对工作负载集群的访问：

```bash
$ kubectl --kubeconfig=demo-1.kubeconfig get node
NAME                         STATUS     ROLES           AGE   VERSION
demo-1-control-plane-bjfvn   NotReady   control-plane   47m   v1.29.0
demo-1-md-0-mtcpn-wnb8v      NotReady   <none>          21m   v1.29.0
```

这将显示集群当前未完全运行，仅仅是因为缺少一个可用的 [CNI](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)。要安装 CNI，请运行：

```bash
$ kubectl --kubeconfig=./demo-1.kubeconfig \
apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml
```

几秒钟后，重新运行上述 `get node` 命令将显示节点已就绪。

## 修改工作负载集群

您现在可以尝试修改工作负载集群清单中的某些内容。

让我们将 workers 的 `MachineDeployment` 副本增加到 2。您可以通过使用您喜欢的编辑器编辑
`clusters/demo-1/workers.yaml`，搜索 `MashineDeployment` 资源并用 `replicas: 2` 替换
`replicas: 1` 来执行此操作。

现在，让我们[部署](https://kluctl.io/docs/kluctl/commands/deploy/)此更改。我们现在将开始看到 Kluctl 的第一个好处，具体来说，在我们部署某些内容之前发生的空运行和差异。您需要通过按 `y` 确认部署。

```bash
$ kluctl deploy -t demo-1
✓ Loading kluctl project-api-demo/1-initial
✓ Initializing k8s client
✓ Rendering templates
✓ Rendering Helm Charts
✓ Building kustomize objects
✓ Postprocessing objects
✓ Writing rendered objects
✓ Getting remote objects by discriminator
✓ Getting namespaces
✓ demo-1: Applied 8 objects.

Changed objects:
  cluster-demo-1/MachineDeployment/demo-1-md-0


Diff for object cluster-demo-1/MachineDeployment/demo-1-md-0
+---------------+----------------------------------------------------------------------------------+
| Path          | Diff                                                                             |
+---------------+----------------------------------------------------------------------------------+
| spec.replicas | -1                                                                               |
|               | +2                                                                               |
+---------------+----------------------------------------------------------------------------------+
✓ The diff succeeded, do you want to proceed? (y/N) y
✓ demo-1: Applied 8 objects.
✓ Writing command result

Changed objects:
  cluster-demo-1/MachineDeployment/demo-1-md-0


Diff for object cluster-demo-1/MachineDeployment/demo-1-md-0
+---------------+----------------------------------------------------------------------------------+
| Path          | Diff                                                                             |
+---------------+----------------------------------------------------------------------------------+
| spec.replicas | -1                                                                               |
|               | +2                                                                               |
+---------------+----------------------------------------------------------------------------------+
```

## 添加和删除节点池

您还可以尝试更多类型的修改。当您开始添加或删除资源时，它会变得特别有趣，例如，如果您通过将
`workers.yaml` 复制到 `workers-2.yaml`（别忘了也更新`kustomization.yaml`）并用 `md-1` 替换所有出现的 `md-0` 来添加另一个节点池。当您部署此内容时，Kluctl 将向您显示将创建新资源，并在确认后实际创建这些资源。

如果您尝试了此操作，也请尝试再次删除 `workers-2.yaml`，然后查看 `kluctl deploy -t demo-1` 将执行什么操作。它会通知您孤立的资源，然后您可以通过 `kluctl prune -t demo-1` [清理](https://kluctl.io/docs/kluctl/commands/prune/)这些资源。清理也可以通过 `kluctl deploy -t demo-1 --prune` 与部署相结合。我们不会在此处详细介绍，因为当我们在下一部分中将此与模板化相结合时，这将变得更加清晰和强大。

## 引入模板化（templating）

到目前为止，我们只使用了非常静态的清单。要引入新集群，甚至节点池，我们必须在到处替换名称时进行大量复制粘贴。当然，这不被认为是最佳实践，我们应该寻求更好的方法。Cluster API 有一项名为[集群类（cluster classes）](https://cluster-api.sigs.k8s.io/tasks/experimental-features/cluster-class/) 的实验性功能，它试图解决此问题。然而，我们不会在本教程中使用这些功能，而是依靠 Kluctl 的模板化功能来满足相同的要求。后面的部分还将解释为什么模板化是 ClusterClass 的可行替代方案。

对项目结构和文件的以下更改也可以在前面提到的同一个[存储库](https://github.com/kluctl/cluster-api-demo) 中找到，但位于 `2-templating` 目录中。

## 准备一些模板化部署

我们现在将为集群本身及其工作节点引入两个可重用且模板化的 Kustomize 部署。每个集群包含一次集群部署。工作节点部署可以是多次，具体取决于您需要的不同工作节点池的数量。

让我们首先将 `kustomization.yaml`、`namespace.yaml`、`cluster.yaml` 和`control-plane.yaml` 移动到 `templates/cluster/`。还要从 `kustomization.yaml` 中的资源列表中删除 `workers.yaml`。这将成为集群部署。

现在，用 `{{ cluster.name }}` 替换在 `templates/cluster` 目录中找到的所有清单中的所有 `demo-1` 出现。此外，在 `control-plane.yaml` 中的 `KubeadmControlPlane` 内，用 `{{ cluster.replicas }}` 替换 `replicas: 1`。这引入了一些简单的 [Jinja2 模板](https://kluctl.io/docs/kluctl/templating/) 来注入集群名称。此处看到的全局 `cluster` 变量将在稍后介绍。

接下来，将 `workers.yaml` 清单移至 `templates/workers`。这次，不需要 `kustomization.yaml`，因为我们不在乎这里的部署顺序（这里不涉及命名空间），这意味着我们可以允许 Kluctl [自动生成](https://kluctl.io/docs/kluctl/deployments/deployment-yml/#simple-deployments) 它。然后，用 `{{ cluster.name }}` 替换所有的 `demo-1` ，用 `{{ workers.name }}` 替换所有的 `md-0` 。最后，找到 `replicas: 1`（或之前设置的任何值），并用 `replicas: {{ workers.replicas }}` 替换它。

请注意，本教程将这些部署中可能的配置量保持在最低限度。您可能想象，可以通过这里的模板实现很多功能。例如，可以通过 `{{ workers.instanceType }}` 配置 AWS 或 Azure 实例类型。

此外，一个实际示例可能会考虑将集群/工作器模板放入单独的 git 存储库，并通过 [git](https://kluctl.io/docs/kluctl/deployments/deployment-yml/#git-includes) 或 [oci](https://kluctl.io/docs/kluctl/deployments/deployment-yml/#oci-includes) 包含项包含它们。两者都允许您为模板实现版本控制和其他最佳实践。

## 使用模板化部署

现在可以根据需要包含之前准备的模板化部署，并使用不同的配置。

为此，我们必须将 `clusters/demo-1` Kustomize 部署更改为 [包含的子部署](https://kluctl.io/docs/kluctl/deployments/deployment-yml/#includes)。在 `clusters/deployment.yaml` 内用 `include` 替换 `path` ：

```yaml
# content of clusters/deployment.yaml
deployments:
  - include: {{ target.name }}
```

现在，在 `clusers/demo-1` 内创建一个 `deployment.yaml`：

```yaml
# content of clusters/demo-1/deployment.yaml
vars:
  - values:
      cluster:
        name: demo-1
        replicas: 1

deployments:
  - path: ../../templates/cluster
  - barrier: true
  - path: ../../templates/workers
    vars:
      - values:
          workers:
            name: md-0
            replicas: 1
  - path: ../../templates/workers
    vars:
      - values:
          workers:
            name: md-1
            replicas: 2
```

上述子部署定义了一些全局配置（例如 `cluster.name`），并包含之前准备的两个 Kustomize 部署。集群级别配置在子部署级别加载，以便 `deployments` 中的所有项都可以访问那里找到的配置。工作器特定配置作为部署项本身的一部分内联指定。通过这种方式，每个工作器项都可以有自己的配置（例如自己的名称和副本），这里还通过引入一个新的节点池演示了这一点。

您还将在部署项列表中找到一个[障碍](https://kluctl.io/docs/kluctl/deployments/deployment-yml/#barriers)。此障碍确保 Kluctl 在集群资源已应用之前不会继续部署工作器资源。

## 部署重构的工作负载集群

只需重新运行部署命令：

```bash
$ kluctl deploy -t demo-1
✓ Loading kluctl project
✓ Initializing k8s client
✓ Rendering templates
✓ Rendering Helm Charts
✓ Building kustomize objects
✓ Postprocessing objects
✓ Writing rendered objects
✓ Getting remote objects by discriminator
✓ Getting namespaces
✓ ../../templates/workers: Applied 3 objects.
✓ ../../templates/cluster: Applied 5 objects.

Changed objects:
  Namespace/cluster-demo-1
  cluster-demo-1/KubeadmConfigTemplate/demo-1-md-0
  cluster-demo-1/Cluster/demo-1
  cluster-demo-1/MachineDeployment/demo-1-md-0
  cluster-demo-1/KubeadmControlPlane/demo-1-control-plane
  cluster-demo-1/DockerCluster/demo-1
  cluster-demo-1/DockerMachineTemplate/demo-1-control-plane
  cluster-demo-1/DockerMachineTemplate/demo-1-md-0

Diff for object Namespace/cluster-demo-1
+-------------------------------------------------------+------------------------------------------+
| Path                                                  | Diff                                     |
+-------------------------------------------------------+------------------------------------------+
| metadata.annotations["kluctl.io/deployment-item-dir"] | -1-initial/clusters/demo-1               |
|                                                       | +2-templating/templates/cluster          |
+-------------------------------------------------------+------------------------------------------+
| metadata.labels["kluctl.io/tag-0"]                    | -clusters                                |
|                                                       | +demo-1                                  |
+-------------------------------------------------------+------------------------------------------+
...
```

您将看到很多关于 [tags](https://kluctl.io/docs/kluctl/deployments/tags/) 和 kluctl.io/deployment-item-dir 注释。这些注释是由于清单的移动而发生的，对于本教程可以忽略。只需确认并让它部署即可。

您还应该看到正在创建新工作节点。您现在可以通过添加更多工作节点或删除旧工作节点来尝试进行一些实验。Kluctl 将始终通过显示新增内容和已孤立的内容来为您提供支持，允许您通过 `kluctl prune -t demo-1` 或 `kluctl deploy -t demo-1 --prune` 命令修剪内容。

## 添加更多集群

希望在这一点上添加更多集群是不言自明的。它基本上只是复制 `demo-1` 目录，更改 `deployment.yaml` 中的集群名称，并在 `.kluctl.yaml` 中添加一个新目标。如果您希望通过 GitOps 管理您的工作负载集群，则可以通过指向您的 Git 存储库的简单 [KluctlDeployment](https://kluctl.io/docs/gitops/spec/v1beta1/kluctldeployment/) 来重复使用同一个 Kluctl 项目。我们不会在此详细介绍 GitOps，但您可以随时阅读文档并自行尝试。迁移到 GitOps 并不意味着您必须完全参与，因为您始终可以将非 GitOp 相关工作流与 GitOps 工作流混合使用。例如，`kluctl diff / kluctl gitops diff` 始终可以使用，即使同一个部署已通过 GitOps 进行管理也是如此。

## Kluctl 与 ClusterClass

您可能会问为什么不简单地依赖 [ClusterClass](https://cluster-api.sigs.k8s.io/tasks/experimental-features/cluster-class/) 这个 cluster-api 的原生实现可重用性的方法，而要使用 Kluctl。我相信 Kluctl 是 ClusterClass 的一个很好的替代品，原因有很多，让我们来了解其中一些原因。

### 通用解决方案

Kluctl 是一个用于模板化部署的非常通用的解决方案。这意味着您可以实现许多不同的方式和场景来满足不同的需求。如果您已经在其他地方使用 Kluctl，或考虑在其他地方使用它，那么您将很容易习惯通过 Kluctl 管理 Cluster API。使用 ClusterClass，您必须学习一种新的、非常特定于 Cluster API 的模板化方法。

我还认为，您很可能会最终在 Cluster API 清单之上使用至少一些其他工具，仅仅是因为普通的 `kubectl apply -f ...` 不是最好的方法。传统上，这将是 Kustomize 或 Helm。如果需要 GitOps，您最终还可能会使用 Flux 或 ArgoCD。因此，如果已经需要这种额外的工具层，为什么不尝试一下 Kluctl，同时完全避免与它一起使用 ClusterClass。

### 不仅限于 Cluster API 资源

使用 ClusterClass，您只能粘合在一起 Cluster API 相关资源。然而，一个集群可能需要更多，例如 [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) 的一个实例。使用 ClusterClass，您唯一的选择是使用 [ClusterResourceSet](https://cluster-api.sigs.k8s.io/tasks/experimental-features/cluster-resource-set)，它将普通清单部署到工作负载集群。然而，这些 CRS 不是模板化的，这将在很大程度上限制您所能实现的目标。此外，您必须使用普通清单，而不能使用 Helm Chart，这意味着保持清单最新的负担落在您身上。此外，CRS 仅允许将其他资源部署到工作负载集群，而不允许部署到管理集群本身。

使用 Kluctl，您可以为集群和/或工作节点模板使用任何您想要的资源。添加 Cluster Autoscaler 与添加 [Helm Chart](https://kluctl.io/docs/kluctl/deployments/helm/) 和适当的 Helm 值（也可以通过模板化使用集群配置）一样容易。

### 迁移/修改集群模板

[更改 ClusterClass](https://cluster-api.sigs.k8s.io/tasks/experimental-features/cluster-class/change-clusterclass) 是一件有风险的事情，在我看来，拥有适当的干运行和 diff 功能至关重要。使用 ClusterClass，这在某种程度上是 [受支持的](https://cluster-api.sigs.k8s.io/clusterctl/commands/alpha-topology-plan#clusterctl-alpha-topology-plan)，但难以使用且 [并非 100% 可靠](https://cluster-api.sigs.k8s.io/clusterctl/commands/alpha-topology-plan#limitations-server-side-apply)。使用 Kluctl，测试更改变得像更改一些内容然后运行 `kluctl diff -t demo-1` 一样容易。

## 总结

如果您想尝试本教程的结果，而无需复制粘贴所有 YAML，只需克隆 [https://github.com/kluctl/cluster-api-demo](https://github.com/kluctl/cluster-api-demo) 并按照 README.md 中的说明进行操作。

有关 Kluctl 可以做什么的更通用的解释，请观看在 [Rawkode Academy](https://www.youtube.com/@RawkodeAcademy) YouTube 频道上的[现场演示](https://www.youtube.com/watch?v=fJgLOyEHmN8) 。https://kluctl.io/docs/ 上的文档也值得一读。

