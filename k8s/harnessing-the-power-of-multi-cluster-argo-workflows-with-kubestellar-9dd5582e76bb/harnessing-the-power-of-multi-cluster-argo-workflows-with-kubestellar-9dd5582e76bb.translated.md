利用 KubeStellar 驾驭多集群 Argo 工作流的力量

[Joshua Sortino](https://unsplash.com/@sortino?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/worms-eye-view-photography-of-ceiling-LqKhnDzSF-8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

在这篇文章中，我们将探索一种新颖的方法，将 Argo 工作流分布到多个 Kubernetes 集群中。

**了解基础知识：Argo 工作流**

[Argo 工作流](https://argoproj.github.io/workflows/)，一个开源的、容器原生的工作流引擎，专为 Kubernetes 设计。它是一个强大的工具，可编排多步骤任务、管理数据和资源依赖关系，并促进批处理、基础设施自动化和 ML 工作流。难怪 Argo 工作流已成为 Kubeflow Pipelines 等流行的云原生 AI/ML 项目的组成部分。

## 多集群工作流的必要性

但为什么要在多个集群上运行这些工作流？答案在于组织的独特需求。如今，大多数组织出于各种原因（包括环境隔离、帐户管理、数据主权和资源异构性）运营多个 Kubernetes 集群。

我在组织内探索的一个有趣场景是在多个 Kubernetes 集群中分布工作负载。这是一个常见问题：一些集群利用不足，而另一些集群则接近容量。显而易见的解决方案似乎是向集群添加更多工作节点，但这种方法有实际限制，尤其是在多区域和多地理位置场景中。

那么，当我们意识到需要多集群解决方案时会发生什么？这就是 KubeStellar 发挥作用的地方。

## 介绍 KubeStellar：一个改变游戏规则的人

[KubeStellar](http://kubestellar.io)，一个 CNCF 沙盒项目，是 Kubernetes 领域的游戏规则改变者。它简化了跨多个 Kubernetes 集群部署和配置应用程序，为用户提供类似于使用单个集群的无缝体验。使用 KubeStellar，用户可以定义绑定策略并使用标准 Kubernetes 工具部署工作负载，从而使多集群操作变得轻而易举。KubeStellar 提供了一个通用的平台，可容纳广泛的应用程序，从边缘计算到混合和多云环境中的人工智能和机器学习。

KubeStellar 的核心是两个基本概念：

**工作负载定义空间 (WDS)：**这是一个用户友好的界面，旨在公开 Kubernetes API 服务器界面，允许用户提交和管理其工作负载。此外，它使用户能够设置绑定策略，以控制如何在系统中分配这些工作负载。

**清单和传输空间 (ITS)：**通过此功能，用户可以维护受管集群的清单，以编排在它们之间分配工作负载，确保它们在绑定策略中指定的位置交付和运行。

在讨论 Argo 工作流如何与 KubeStellar 配合工作之前，让我们快速概述一下

*工作流*。

## 详细了解工作流

Argo 工作流通过称为

*工作流*的 Kubernetes 自定义资源进行定义和管理。此关键资源服务于两个主要功能：

**定义工作流执行：**在 Workflow

spec结构中指定要执行的特定工作流步骤，该结构由

templates和

entrypoint的列表组成。

entrypoint指定要首先执行的初始模板或“main”函数。

**存储工作流状态：**随着工作流的执行，其实时状态保存在 Workflow 对象本身中，使其成为一个动态实体，既表示工作流定义又表示其实时状态。

工作流由

*模板定义*（可能包括容器、脚本或资源）和

*模板调用*（用于调用其他模板和控制执行流）组成。它们主要有两种类型：

**步骤：**按一系列顺序步骤或并行组定义任务，支持通过

*when*子句进行条件执行。

**DAG**（有向无环图）：将任务构建为依赖关系图，其中任务可以根据其依赖关系的完成情况并发运行。

与 KubeStellar 集成的标志性功能是

spec.suspend

**架构：KubeStellar 和 Argo 工作流**

让我们探讨 KubeStellar 和 Argo 工作流在启用多集群工作流方面的协同作用。

图 1 说明了多集群 Argo 工作流的设置。主要组件包括：

**Argo 工作流：**安装在控制集群和多个工作流执行集群 (WEC) 上。

**KubeStellar：**安装在控制集群上（并在 WEC 上安装代理），它将 Workflow

spec从控制集群同步到 WEC，并
### Corrected Markdown

**状态从 WEC 到控制集群**

**S3 工件存储：**为所有 Argo 工作流实例提供通用存储。

**KubeStellar**

* **绑定策略**定义工作负载与其目标执行集群之间的关联方式：
    * **工作负载：**使用 objectSelectors 标识。
    * **集群：**通过 clusterSelectors 分配。

在本文档中描述的设置中，工作流和集群由 *标签选择器* 标识。没有指定标签且未设置 *suspend* 标志的工作流在控制集群上执行。配置了 spec.suspend=true 且与绑定策略的标签匹配的工作流在远程集群上执行。

**KubeStellar 控制器**监视与策略标签匹配的对象。当在控制集群（也是 WDS）中创建匹配的对象时，控制器会将其打包到清单中，并通过 ITS 层将其传递到选定的 WEC。

ITS 和 KubeStellar 控制器都确保 Argo 工作流状态从 WEC 到控制集群的持续上同步。为了实现无缝操作，必须排除 spec.suspend 标志和某些 Argo 特定标签传播到远程 Argo 工作流实例。在此， **KubeStellar 的 CustomTransform 功能** 在 WEC 下同步之前过滤工作负载对象中的用户定义字段。

**演示设置**

确保您的环境满足 KubeStellar 的 [先决条件](https://docs.kubestellar.io/release-0.22.0/direct/pre-reqs/#kubestellar-prerequisites)。鉴于您将建立三个 *kind* 集群，因此在执行设置脚本之前，扩展您的 [资源限制](https://kind.sigs.k8s.io/docs/user/known-issues/#pod-errors-due-to-too-many-open-files) 非常重要。为了便于安装和配置与各种项目的集成，包括 Argo 工作流，KubeStellar 社区提供了 [galaxy 存储库](https://github.com/kubestellar/galaxy)。您可以使用以下命令克隆存储库：

```
git clone https://github.com/kubestellar/galaxy
```

然后运行设置脚本。

```
cd galaxy/scripts/argo-wf
./install-all.sh
```

脚本执行以下操作：

- 启动三个 *kind* 集群。
- 在控制集群上安装 KubeStellar。
- 将剩余两个集群注册到控制集群。
- 设置一个 KubeStellar *CustomTransform* 来过滤掉 suspend 标志和 Argo 特定标签。
- 在所有集群中部署 Argo 工作流。
- 配置工作流执行集群以使用托管在控制集群上的共享 S3 (MinIO) 工件存储。

请耐心等待，因为脚本执行可能需要几分钟。完成后，脚本日志应显示 Argo 和 MinIO 的可访问 URL：

```
您可以在 https://argo.localtest.me:9443 访问 argo 控制台
+ echo 'you can access the minio console at http://minio.localtest.me:9080'
您可以在 http://minio.localtest.me:9080 访问 minio 控制台
```

**运行您的第一个多集群场景**

您现在可以运行您的第一个多集群 Argo 工作流。

*samples* 目录包含一些工作流示例（您可以在 [argo 项目](https://github.com/argoproj/argo-workflows/tree/main/examples) 中找到更多示例）。让我们从运行一个“hello world”工作流开始：

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: hello-world-
  namespace: argo
  labels:
    workflows.argoproj.io/archive-strategy: "false"
    kubestellar.io/cluster: cluster1
  annotations:
    workflows.argoproj.io/description: |
      这是一个简单的 hello world 示例。
spec:
  suspend: true
  entrypoint: whalesay
  templates:
  - name: whalesay
    container:
      image: docker/whalesay:latest
      command: [cowsay]
      args: ["hello world"]
```

请注意 spec.suspend 为 true，以及 kubestellar.io/cluster: cluster1。此标签与 samples/wf-binding-policy-cluster1.yaml 中的绑定策略匹配：

```yaml
apiVersion: control.kubestellar.io/v1alpha1
kind: BindingPolicy
metadata:
  name: workflows-cluster1
spec:
  wantSingletonReportedState: true
  clusterSelectors:
  - matchLabels:
      name: cluster1
  downsync:
  - objectSelectors:
    - matchLabels:
        kubestellar.io/cluster: cluster1
```

要启动工作流，只需运行以下命令：

```
kubectl create -f samples/argo-wf1.yaml
```

我们可以运行以下命令来验证工作流正在运行，并且一个用于 hello-world 的 pod 已在 *cluster1:* 上启动：

```
$ kubectl get workflows -n argo
NAME STATUS AGE MESSAGE
hello-world-f9kqn Running 2s
$ kubectl get pods -n argo --context cluster1
NAME READY STATUS RESTARTS AGE
argo-server-788d77f579-8hxsv 1/1 Running 0 30m
hello-world-f9kqn 0/2 PodInitializing 0 11s
```

工作流完成后，我们可以检查已完成状态：

```
$ kubectl get workflows -n argo
NAME STATUS AGE MESSAGE
hello-world-f9kqn Succeeded 4m23s
```

现在让我们尝试一个更复杂的示例：

```
kubectl create -f samples/dag-nested.yaml
```
## 使用 Argo Workflows UI 检查工作流进度

让我们使用 Argo Workflows UI 来检查此工作流的进度。使用浏览器打开 URL [https://argo.localtest.me:9443/](https://argo.localtest.me:9443/)，你应该能够获取有关正在运行的工作流的大量详细信息：

注意 HOST NODE NAME 显示 `cluster1-control-plane`，因为任务在 `cluster1` 中的节点上运行。单击日志按钮，甚至应该提供所选任务的日志：

## 结论

通过将 KubeStellar 与 Argo Workflows 集成，多集群编排变得既简化又透明，可以从单个界面查看。在这里，我们只接触了基本功能；KubeStellar 拥有丰富的用于管理和配置多集群工作负载的高级功能。

截至本文发布之时，我还致力于增强 KubeStellar，以支持 KubeFlow Pipelines，利用前面展示的 Argo Workflow 集成。有关更多详细信息和示例，请考虑浏览 [kubestellar.io](https://kubestellar.io)。如果我们的工作引起了你的共鸣，我们将不胜感激你的支持——请在 [https://github.com/kubestellar/kubestellar](https://github.com/kubestellar/kubestellar) 为我们的 GitHub 存储库加星。

请继续关注有关此项不断发展的工作的后续文章。