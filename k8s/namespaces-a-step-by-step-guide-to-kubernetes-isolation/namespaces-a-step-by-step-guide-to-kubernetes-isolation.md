<!--
title: 命名空间：Kubernetes 隔离核心实践
cover: https://cdn.thenewstack.io/media/2025/09/e4e5b71b-kubernetes.png
summary: Kubernetes命名空间帮助您整理应用、隔离环境、控制资源，通过命令或YAML文件创建管理。它是保持集群整洁和安全的关键工具。
-->

Kubernetes命名空间帮助您整理应用、隔离环境、控制资源，通过命令或YAML文件创建管理。它是保持集群整洁和安全的关键工具。

> 译自：[Namespaces: A Step-By-Step Guide to Kubernetes Isolation](https://thenewstack.io/namespaces-a-step-by-step-guide-to-kubernetes-isolation/)
> 
> 作者：Sunny Yadav

在 [Kubernetes](https://thenewstack.io/kubernetes/) 中管理应用程序会很快变得混乱。当所有东西都堆在一起运行时，很难保持井然有序。删除错误的 Pod 或混淆开发和生产环境等错误都太容易发生了。

这就是命名空间 (namespaces) 可以提供帮助的地方。它们就像集群的文件夹，帮助你将系统的不同部分整齐地分开。无论你是管理多个团队、环境还是应用程序，命名空间都能确保它们互不干扰。

了解如何使用 kubectl 命令创建命名空间，并探索一些技巧，以保持集群的整洁和受控。

## **接下来的内容**

* 为什么要在 Kubernetes 中使用命名空间
* 先决条件和背景
* `kubectl create namespace` 的基本语法
* 验证和检查新命名空间
* 附加资源配额和限制
* 为新命名空间设置 RBAC
* 将命名空间集成到 CI/CD 流水线中
* 常见错误和故障排除
* 命名空间组织最佳实践
* 安全地删除和清理命名空间
* 总结：保持组织，保持掌控

## **为什么要在 Kubernetes 中使用命名空间**

可以将命名空间想象成电脑上的一个文件夹。它将事物分组，这样你就不会混淆文件——或者在这个例子中，是应用程序和服务。

**命名空间有助于：**

* 组织大型项目
* 分离环境，例如开发、测试和生产
* 控制谁可以访问什么
* 避免命名冲突
* 更轻松地清理资源

## **先决条件和背景**

在创建命名空间之前，你需要准备好一些东西。这些是基础知识，你可能已经具备了。

请确保你已具备：

* 一个正常运行的 [Kubernetes 集群](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/)（即使是像 [Minikube](https://thenewstack.io/how-to-enable-and-use-the-minikube-dashboard/) 这样的本地集群也可以）。
* *kubectl* 已安装并连接到你的集群。
* 了解如何在终端中运行命令的基本知识。

小型设置不需要命名空间，但如果你要管理多个应用程序——或者有不同的团队在同一个集群上工作——它们是必不可少的。

## `kubectl create namespace` 的基本语法

让我们进入正题：如何创建命名空间。最直接的方法是使用一个简单的命令：

```
kubectl create namespace your-namespace-name
```

只需替换为你想要使用的名称即可！现在让我们看看你可以添加的一些选项。

### **默认标志和可选标签**

你可以在创建命名空间时为其添加标签。标签可以帮助你用有用的信息标记命名空间，例如它属于哪个团队。

**以下是带有标签的示例：**

```
kubectl create namespace your-namespace-name --dry-run=client -o yaml | kubectl label -f - team=frontend
```

此命令为你的命名空间添加一个名为 team=frontend 的标签。

**你可能会使用的标志：**

* ***–dry-run=client*****:** 显示命令将执行的操作，但不进行更改。
* ***-o yaml*****:** 以 [YAML 格式](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/) 输出命令——非常适合保存为文件。

### **从 YAML 清单创建命名空间**

你也可以在 [YAML](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) 文件中定义命名空间。如果你想跟踪你的设置或与团队共享，这会很有用。

**这是一个基本的 YAML 示例：**

```
apiVersion: v1
kind: Namespace
metadata:
name: your-namespace-name
```

要从该文件创建命名空间，请运行：`kubectl apply -f namespace.yaml`

使用 YAML 在团队协作、自动化或使用 GitOps 工具时特别有用。

## **验证和检查新命名空间**

创建命名空间后，你会想确保它确实存在——也许会查看内部，看看发生了什么。Kubernetes 提供了几种使用 kubectl 轻松完成此操作的方法。

### 使用 `kubectl get ns` 列出命名空间

要查看集群中的所有命名空间，只需运行：*kubectl get ns*。

你将获得如下列表：

```
NAME              STATUS   AGE
default           Active   10d
kube-system       Active   10d
your-namespace    Active   2m
```

这证实你的命名空间已启动并正在运行。

### **描述命名空间详情**

如果你想了解特定命名空间的更多详细信息，请使用：*kubectl describe namespace your-namespace-name*。

这会显示标签、状态和任何已应用的策略等信息。这是仔细检查所有设置是否符合预期要求的好方法。

## **附加资源配额和限制**

命名空间不仅用于组织事物，还可以帮助你控制每个团队或应用程序可以使用多少 CPU、内存和其他资源。这可以防止一个应用程序独占所有资源并导致其他应用程序崩溃。

### **CPU 和内存配额**

你可以设置命名空间可以使用的 CPU 和内存限制。首先，创建如下 YAML 文件：

```
apiVersion: v1
kind: ResourceQuota
metadata:
   name: basic-quota
   namespace: your-namespace-name
spec:
   hard:
     requests.cpu: "1"
     requests.memory: 500Mi
     limits.cpu: "2"
     limits.memory: 1Gi
```

然后用：*kubectl apply -f quota.yaml* 应用它。

这会告诉 Kubernetes：“嘿，这个命名空间不能使用超过这个数量的 CPU 或内存。”

### **对象计数限制**

你还可以限制命名空间可以拥有的 Pod、服务或 Secret 的数量。这是一个示例：

```
spec:
   hard:
      pods: "10"
      services: "5"
      secrets: "20"
```

将此添加到你的配额 YAML 中，以确保命名空间不会过于拥挤。

## **为新命名空间设置 RBAC**

[基于角色的访问控制 (RBAC)](https://thenewstack.io/kubernetes-rbac-permissions-you-might-not-know-about-but-should/) 可帮助你管理谁可以在命名空间内做什么。例如，你可能希望授予开发团队访问一个命名空间的权限，但不能访问另一个。

### **角色和角色绑定基础知识**

首先，创建描述允许哪些操作的角色 (Role)：

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
   namespace: your-namespace-name
   name: pod-reader
rules:
 - apiGroups: [""]
   resources: ["pods"]
   verbs: ["get", "watch", "list"]
```

然后，将该角色绑定到用户或组：

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
   name: read-pods
   namespace: your-namespace-name
subjects:
-  kind: User
   name: dev-user
   apiGroup: rbac.authorization.k8s.io
roleRef:
   kind: Role
   name: pod-reader
   apiGroup: rbac.authorization.k8s.io
```

这赋予了 dev-user 在该命名空间中读取 Pod 信息的权限——仅此而已。

### **服务账号作用域**

你可以将角色分配给应用程序使用的服务账号，而不是分配给用户。这样，你的应用程序只获得它实际需要的资源的访问权限。

**示例：**

```
subjects:
- kind: ServiceAccount
name: my-app
namespace: your-namespace-name
```

这可以确保安全，并避免授予应用程序不必要的权限。

## **将命名空间集成到 CI/CD 流水线中**

命名空间不仅适用于组织应用程序；它们也非常适合自动化你的工作流程。在 [CI/CD 流水线](https://thenewstack.io/why-ci-and-cd-need-to-go-their-separate-ways/)中，你可以使用命名空间来保持测试运行的干净和彼此分离。

### **用于测试环境的动态命名空间创建**

每次你的流水线运行时，你都可以为该测试启动一个全新的命名空间。这可以使测试相互隔离，因此它们不会干扰你的主应用程序或彼此。

**示例命令：** *kubectl create namespace test-run-123*。

你可以使用脚本生成唯一的名称，例如 *test-run-001*、*test-run-002* 等。这在测试拉取请求或新构建时特别方便。

### **自动清理策略**

测试完成后，清理该命名空间以节省资源。

以下是删除它的方法：*kubectl delete namespace test-run-123*。

有些团队还会添加基于时间的[清理](https://thenewstack.io/how-to-detect-and-clean-up-data-contamination-in-llms/)，例如删除任何超过一小时的测试命名空间。你可以通过脚本实现这一点，或使用 Kubernetes Jobs 或 TTL 控制器等工具。

## **常见错误和故障排除**

即使是简单的命令也可能遇到障碍。以下是一些常见的与命名空间相关的错误以及如何解决它们。

### **“AlreadyExists”冲突**

如果你尝试创建一个已存在的命名空间，你将看到如下错误：

```
Error from server (AlreadyExists): namespaces "your-namespace-name" already exists
```

**解决方案：**

* 仔细检查你的命名空间名称。
* 你也可以使用 *kubectl get ns* 列出现有命名空间。
* 或者，如果你打算更新某些内容，请使用 *apply* 而不是 *create*。

### **无效的元数据或标签**

如果你的命名空间 YAML 文件在名称或标签中包含错误格式或不支持的字符，Kubernetes 将抛出错误。

**常见错误：**

* 使用大写字母或空格
* 缺少必需字段，例如名称

始终仔细检查你的 YAML 文件。你可以在应用之前通过运行以下命令来验证它：

```
kubectl apply --dry-run=client -f your-file.yaml
```

这会显示是否有任何错误，而不会实际进行更改。

## **命名空间组织最佳实践**

命名空间可以帮助你保持组织性，但前提是你以正确的方式使用它们。如果没有一个清晰的系统，事情很快就会变得混乱，尤其是有更多人员和应用程序加入时。

以下是如何保持你的命名空间设置干净、逻辑清晰且易于管理的方法。

### **命名约定**

一个好的命名系统可以让你通过查看名称就知道命名空间的作用。坚持使用简短、清晰且一致的名称。

**命名技巧：**

* 仅使用小写字母和连字符（Kubernetes 对此很挑剔！）。
* 在名称中包含用途或所有者。
* 避免模糊的名称，例如 *project1* 或 *testtemp*。

**示例：**

* *frontend-prod*
* *backend-dev*
* *team-alpha-staging*

如果你在 [CI/CD 流水线](https://thenewstack.io/ci-is-not-cd/)中使用命名空间，请使用唯一但可追溯的名称，例如：

* *test-pr-204*
* *ci-run-2025-07-17*

这有助于你以后查找和清理它们。

### **按团队、环境或应用程序划分**

命名空间是灵活的——你可以根据需要对事物进行分组。但以下是一些最常见和最有效的方法：

**按团队：** 每个团队都有自己的命名空间。这使他们的资源相互隔离，并为他们提供了试验空间，而不会相互干扰。

**示例：**

* *team-marketing*
* *team-infra*

**按环境：** 分离开发、测试、预发布和生产环境。这可以避免事故，例如将未完成的代码部署到你的实时应用程序。

**示例：**

**按应用程序：** 如果你的集群运行许多小型应用程序，请为每个应用程序分配自己的命名空间。这可以防止服务冲突，并使管理权限和配额变得更容易。

**示例：**

* *billing-service*
* *user-auth*

你甚至可以组合这些方法。例如：

* *frontend-dev*
* *backend-prod*
* *team-ops-staging*

只需确保每个人都遵循相同的模式，这样你的集群就不会变成一个命名混乱的局面。

## **安全地删除和清理命名空间**

创建命名空间很容易。忘记删除它们？更容易。但是，残留的命名空间会浪费资源、使你的集群混乱，如果它们仍然可以访问敏感数据，甚至会造成安全风险。

以下是如何像专业人士一样进行清理，而不会意外删除重要内容。

### **如何删除命名空间**

要删除命名空间，请运行：*kubectl delete namespace your-namespace-name*。

就是这样。Kubernetes 将清除其中的所有内容——Pod、服务、Secret、配置——所有一切。但一旦删除，就无法挽回。在按 Enter 键之前，请务必仔细检查名称。

### **删除前检查内部内容**

如果你不确定命名空间包含什么，请首先列出其资源：*kubectl get all -n your-namespace-name*。

这将显示正在运行的内容——Pod、部署、服务等。你还可以检查 Secret 和 ConfigMap：

```
kubectl get secrets -n your-namespace-name
```

```
kubectl get configmaps -n your-namespace-name
```

这就像在扔掉冰箱之前先看看里面一样——你可能会发现一些值得保存的东西！

### **卡在“Terminating”状态？**

有时命名空间会卡在 Terminating 状态。这通常意味着内部有东西挂起并且没有释放。

**故障排除步骤：**

1. 运行 *kubectl get namespace your-namespace-name -o json*。在底部查找 finalizers。
2. 手动删除 finalizers（高级——但在极少数情况下有用）。

请谨慎使用：

```
kubectl patch namespace your-namespace-name -p '{"metadata":{"finalizers":[]}}' --type=merge
```

这会强制删除命名空间，但前提是您确定这样做是安全的。

### **自动化清理（额外内容）**

如果你将命名空间用于短期用途，例如测试运行或 CI/CD，请设置自动化以定期删除旧的命名空间。

**以下是一些想法：**

* 添加 TTL (time-to-live) 标签，例如 *ttl=1h*。
* 编写一个清理脚本，检查命名空间年龄并删除旧的命名空间。
* 如果你的集群支持 Kubernetes TTL 控制器，请使用它们。

这可以使你的集群保持整洁，而无需持续的照看。

## **总结：保持组织，保持掌控**

命名空间是 Kubernetes 中最简单但功能最强大的工具之一。它们可以帮助你组织应用程序、保护环境、控制资源并在没有混乱的情况下进行扩展。

从用一行命令创建命名空间到设置配额、RBAC 和自动化清理，你现在知道如何构建一个干净、安全且对团队友好的 Kubernetes 设置。

无论你是管理单个应用程序还是整个集群，正确使用命名空间都能为你提供自信成长所需的控制和清晰度。

查看我们的分步指南《[如何在 Kubernetes 中移除部署](https://thenewstack.io/remove-deployment-in-kubernetes/)》，并保持你的集群整洁。

**主要来源：**

- https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_namespace/
- https://kubernetes.io/docs/concepts/security/multi-tenancy/
- https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
- https://lumigo.io/kubernetes-troubleshooting/kubernetes-node-not-ready-error-and-how-to-fix-it/
- https://www.kubernet.dev/resolving-kubernetes-failedscheduling-errors-a-comprehensive-guide/