**你是哪种工程师**？🤔

有人能仅通过观察就猜出来吗？

很可能猜不出来。

如果有人通过观察你的键盘就能猜出来呢？

现在可能稍微容易一点了。⌨️

当键盘上的“k”键已经磨损时，你就知道自己正在与一位**Kubernetes工程师**打交道。

在[Glasskube](https://github.com/glasskube/glasskube)办公室，你会发现到处都是备用的**“k”**键，以备不时之需 😄

当然，我是在开玩笑。

我并不确定磨损的键盘能说明其主人的什么情况。但我确实知道，对于任何想要成为一名熟练的[Kubernetes](https://kubernetes.io/)管理员的人来说，kubectl 有多重要。

kubectl 是用于与 Kubernetes API 通信的 CLI 工具，它乍一看似乎很简单，但很快就会变得复杂。

因此，在这篇博文中，我的目标是编写**我刚开始时希望拥有的指南**。首先关注命令语法和有用的命令，然后再转向[插件](https://krew.sigs.k8s.io/plugins/)和工具的充满活力的生态系统，这些插件和工具旨在扩展 kubectl 和 Kubernetes 的功能。

同时分享一些提示和技巧，以及一份有用的 kubectl 速查表。📋

让我们开始吧。☸️

# 免责声明 🛑

这不是一篇关于 Kubernetes 的文章。K8s 是一项极其庞大的技术，涵盖了众多概念，例如各种类型的 Kubernetes 对象及其交互。对于此讨论，我假设你熟悉这些概念。相反，我将专门关注 kubectl、它的用法以及围绕它构建的工具。

# 开始之前

如果你支持让 Kubernetes 软件包管理对每个人都更好的开源项目，那么请考虑支持[Glasskube](https://github.com/glasskube/glasskube)，在 GitHub 上给我们一颗星 🙏

# 安装

要安装 kubectl，你可以根据你的操作系统选择一些不同的选项。以下是如何在一些常见平台上安装它：

# Linux (Ubuntu/Debian)

```
sudo apt-get update && sudo apt-get install -y kubectl
```

# 使用 Homebrew 的 MacOS

```
brew install kubectl
```

# 使用 Chocolatey 的 Windows

```
choco install kubernetes-cli
```

安装后，你可以通过运行以下命令来验证 kubectl 是否已正确安装：

```
kubectl version --client
```

# kubectl 命令：

kubectl 是一个命令行界面 (CLI) 工具，用于与 Kubernetes API 通信。命令有很多，多到无法记住。

不过不用担心，它不像有些人让你想象的那么可怕。

我们将探索快速访问命令参考、特定于 k8s 对象的命令、有用的别名和命令补全的方法。但首先，命令字符串是如何构建的？

# 语法

英语和汉语是**主谓宾** (SVO) 语言。

印地语和韩语是**主宾谓** (SOV) 语言。

如果 kubectl 是一种语言，那它将是一种**kubectl + 动词 + 对象/[名称可选] + 标志 (kvof)** 语言 😄

也类似于语言，学习和吸收语法的最佳方法是在上下文中使用它，而不是死记硬背冗长的动词和对象列表。

ℹ️ 如果你遇到困难，并且想要快速引用任何 Kubernetes 版本中的现有 Kubernetes 对象，请运行 kubectl api-resources。

命令是通过选择要应用于所需 Kubernetes 的**操作 [动词]**来构建的**资源 [对象]**，通常后跟资源的名称，此外，你还有大量的**过滤器 [标志]**，可以应用于命令，这些过滤器将确定最终的范围和输出。

让我们看一个使用常用的**get 动词**来检索 glasskube-system 命名空间中的所有资源的命令构建示例，并且输出采用 yaml 格式：

```
kubectl get all --namespace glasskube-system -o yaml
```

ℹ️ 如果你遇到一个你以前从未听说过的 Kubernetes 资源，或者需要复习，请使用 kubectl explain [resource-name] 来获取终端描述和使用说明。

# 命令式工作

在 Kubernetes 环境中工作时，你的任务有很多，从部署新应用、对故障资源进行故障排除、检查使用情况等等。稍后，我们将探讨如何使用声明式工作方式更适合定义和部署工作负载，但对于其他所有内容，我们准备好了有用的命令式 Kubernetes 命令。

让我们开始的简单命令是：

# 使用 nginx 镜像创建一个名为“nginx-deployment”的新部署

```
kubectl run nginx-deployment --image=nginx
```

# 删除默认命名空间中名为“nginx-deployment”的 pod

```
kubectl delete pod nginx-deployment
```

要将命令式命令提升到下一步，请知道你可以使用[TUI](https://en.wikipedia.org/wiki/Text-based_user_interface#:~:text=In%20computing%2C%20text%2Dbased%20user,before%20the%20advent%20of%20bitmapped)编辑器来修改资源：

通过运行 kubectl edit -n [namespace] [resource-name]，将打开类似于以下内容的文本编辑器。像在
通过运行

ESC + :q!

来 [vim](https://www.vim.org/)。

# 请编辑下面的对象。以“#”开头的行将被忽略，
# 并且空文件将中止编辑。如果在保存此文件时发生错误，将
# 使用相关故障重新打开此文件。

#
apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubectl.kubernetes.io/default-container: manager
  creationTimestamp: "2024-04-22T17:07:39Z"
  generateName: glasskube-controller-manager-556ff6fccf-
  labels:
    control-plane: controller-manager
    pod-template-hash: 556ff6fccf
  name: glasskube-controller-manager-556ff6fccf-4qlxz
  namespace: glasskube-system
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: glasskube-controller-manager-556ff6fccf
    uid: 430e90e9-32f3-45f6-92dc-4bae26ae1654
"/var/folders/2q/wjmbwg1n5vn8v7vlw17nsz0h0000gn/T/kubectl-edit-1306753911.yaml" 209L, 5898B

大多数命令都适用于所有类型的 Kubernetes 对象。在进一步讨论对某些 Kubernetes 资源有用的特定命令之前，了解可以应用于许多不同对象的某些有用标志是值得的。

# 有用标志：

**— env：**

--env 标志允许您为正在创建的容器指定环境变量。

```
kubectl run nginx-deployment --image=nginx --env="ENV_VARIABLE=value"
```

**— template：**

此标志允许您为 kubectl 命令的输出格式指定一个 Go 模板。当您想要自定义输出结构、过滤或表示时，它非常方便。

```
kubectl get pods --template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}'
```

**— field-selector：**

使用此标志，您可以根据特定字段过滤资源。例如，您可以根据 Pod 的状态或标签过滤 Pod。

```
kubectl get pods --field-selector=status.phase=Running
```

**— field-selector type=[Normal/Warning]：**

这是 — field-selector 标志的一个特定用法，您可以在其中根据类型（Normal 或 Warning）过滤事件。

```
*kubectl events -n [resource-namespace] — for=[resource-kind]/[resource-name]: *
```

此命令获取与指定命名空间中特定资源相关的事件。它会持续监视与给定资源相关的新的事件。

```
kubectl events -n my-namespace --for=deployment/my-deployment
```

# 老派与新派监视标志：

**-o wide 与 -w：**

-o wide：这是一个
**“老派”** 标志，提供宽输出格式，显示有关资源的其他详细信息。
-w：这是一个
**“新派”** 标志，启用对资源更改的持续监视，类似于 watch 命令。

# 使用 Pod

Pod 是 Kubernetes 生态系统中最小的抽象，它们是容纳容器的逻辑单元。Pod 消耗资源，可以执行并生成日志。以下是一些可帮助您管理 Pod 的命令。

# 显示 Pod 的资源使用情况

```
kubectl top pod -n [namespace] [pod-name]
```

# 在集群中的新 Pod 中运行命令

```
kubectl run -it ubuntu --image ubuntu --rm -- bash# 将资源标签显示为列
# 例如 kubectl get pods -n [namespace] -L vault-active -L vault-sealed
```

```
kubectl get pods -n [namespace] -L vault-active -L vault-sealed# 在 Pod 中执行命令
```

```
kubectl exec -it [pod-name] -n [namespace] --# 将端口转发到 Pod
```

```
kubectl port-forward [pod-name] [local-port]:[remote-port] -n [namespace]# 显示容器日志
```

```
kubectl logs -n [namespace] [pod-name]
kubectl logs -n [namespace] /deployment/[deployment-name] # 使用 -f 标志进行连续流式传输# 在现有容器中运行命令
```

```
kubectl exec -it -n [namespace] [pod-name] -- [command...]
```

# 使用节点

节点是提供计算能力和存储的基础实例，Kubernetes 集群在其之上运行。

# 显示节点资源利用率

```
kubectl top node [node-name] # 节点名称是可选的；如果不显示，则显示所有节点的表格
```

# 获取节点信息

```
kubectl get node
```

# 使用部署、守护程序集和有状态集

部署、守护程序集和有状态集是 Kubernetes 中的更高级别的抽象，用于管理应用程序工作负载的部署和扩展。

# 重新启动工作负载（例如部署、有状态集、守护程序集）

```
kubectl rollout restart -n [namespace] [workload-kind]/[workload-name] # 触发重新创建此工作负载的所有 Pod，并遵守工作负载配置
```

# 检查部署推出状态

```
kubectl rollout status deployment/[name]# 查看部署的推出历史记录
```

```
kubectl rollout history deployment/[name] # 查看部署的推出历史记录# 将部署扩展到指定副本数
```

```
kubectl scale deployment/ --replicas=[number] # 将部署扩展到指定副本数# 监视与部署相关的事件
```

```
kubectl events -n glasskube-system --for=deployment/glasskube-controller-manager # 更新部署映像
```
## 部署管理

### 删除 Deployment

```
kubectl set image deployment/[部署名称] [容器名称]=new-image:tag# 删除 DaemonSet
kubectl delete daemonset [daemonset 名称]
```

### 作业

作业管理 pod 的执行以执行特定任务，并确保在终止之前成功完成任务。

### 手动运行 CronJob

```
kubectl create job [作业名称] --image=image/name
```

### 从 CronJob 创建作业

```
kubectl create job -n [命名空间] --from=cronjob/[cron 作业名称] [作业名称]
```

### Secret 管理

Secret 用于在 Kubernetes 中安全地存储敏感信息，如密码、OAuth 令牌和 SSH 密钥。

### 创建 Secret

```
kubectl create secret generic [secret 名称] --from-literal=key1=value1 --from-file=ssh-privatekey=~/.ssh/id_rsa
```

### 获取 Secret 值

```
kubectl get secrets -n [命名空间] [secret 名称] --template='{{ .data.[key-name] | base64decode }}'
kubectl get secrets [secret 名称] -o jsonpath="{.data.key1}" | base64 --decode
```

### JSONPath

JSONPath 是一种查询语言，用于从 JSON 文档中提取特定数据。在 Kubernetes 中，JSONPath 表达式通常与 kubectl 命令中的 `-o jsonpath` 标志一起使用，以从这些命令的输出中提取特定信息。

### Shell 补全

kubectl 命令很快就会变得很长。可以将一个非常漂亮的 shell 补全脚本添加到你的 bash 或 zshell 文件中，以启用简单的 tab 补全。

**Bash**

```
source <(kubectl completion zsh)
```

**Zsh**

```
echo "source <(kubectl completion bash)" >> ~/.bashrc
source ~/.bashrc
```

### 声明性工作

Kubernetes 资源的声明性管理涉及使用 YAML 清单文件指定资源的所需状态，并将这些清单应用到集群。

### 创建 YAML 文件

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: glasskube-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: glasskube
      env: prod
  template:
    metadata:
      labels:
        app: glasskube
        env: prod
    spec:
      containers:
      - name: glasskube-container
        image: your-glasskube-image:latest
```

### 应用 YAML 文件

**客户端应用**

```
kubectl create -f glasskube-deployment.yaml
```

**服务器端应用 (SSA)**

```
kubectl apply --server-side -f manifest.yaml
```

### 插件和工具

Kubernetes 插件和工具的广泛生态系统旨在帮助完成 Kubernetes 生命周期中的各个阶段。

### Krew Kubernetes 插件管理器

```
kubectl krew install <PLUGIN_NAME>
```

### 内容和命名空间切换

**Kubectx 和 Kubens**

安装说明：[此处](https://github.com/ahmetb/kubectx)。

**值得称赞的：** [kubectl-cf](https://github.com/surfinggo/kubectl-cf)：一种在 kubeconfig 文件（而不是上下文）之间切换的更快方法。

### 可见性

[此处](https://github.com/ahmetb/kubectx)
## Kubernetes 工具

### 可视化和管理

- **k9s:** 交互式 Kubernetes 仪表板，可视化资源并执行操作。
  - 安装说明：[此处](https://k9scli.io/topics/install/)

- **kubectl tree:** 探索 Kubernetes 对象之间的所有权关系。
  - 安装：`kubectl krew install tree`

- **kubecolor:** 为 kubectl 输出添加颜色。
  - 安装说明：[此处](https://github.com/kubecolor/kubecolor?tab=readme-ov-file#installation)

### 包管理

- **Glasskube:** 声明式集群包管理，简化包堆栈管理。
  - [Glasskube](https://github.com/glasskube/glasskube)

### 网络

- **kubectl-Cilium:** 与 Cilium 交互的插件，用于管理网络连接。
  - 安装：`kubectl krew install cilium`

- **Cert-manager:** 管理 Kubernetes 集群中的证书和证书颁发者。
  - 安装说明：[此处](https://cert-manager.io/docs/installation/)

- **Ksniff:** 在 Kubernetes 集群中启动远程捕获。
  - [Ksniff](https://github.com/eldadru/ksniff)

### RBAC

- **Kubelogin:** Kubernetes OpenID Connect (OIDC) 身份验证插件。
  - 安装说明：[此处](https://github.com/Azure/kubelogin?tab=readme-ov-file#installation)

- **Kube-policy-advisor:** 从实时 K8s 环境或 YAML 文件创建 K8s Pod 安全策略 (PSP) 或 OPA 策略。
  - 安装：`kubectl krew install advise-policy`

- **kubectl-who-can:** 显示对 Kubernetes 资源的 RBAC 权限。
  - [kubectl-who-can](https://github.com/aquasecurity/kubectl-who-can)

- **rakkess:** 显示服务器资源的访问矩阵。
  - [rakkess](https://github.com/corneliusweig/rakkess)

- **kubectl-rolesum:** 汇总指定主体的 RBAC 角色。
  - [kubectl-rolesum](https://github.com/Ladicle/kubectl-rolesum)

### Linting

- **Kubectl-neat:** 从 Kubernetes 清单中删除混乱内容。
  - 安装：`kubectl krew install neat`

- **KubeLinter:** 分析 Kubernetes YAML 文件和 Helm 图表，检查最佳实践。
  - 安装说明：[此处](https://github.com/stackrox/kube-linter?tab=readme-ov-file#installing-kubelinter)

### 集群维护和安全

- **KubePug:** 扫描 Kubernetes 集群以查找弃用或已删除的 API。
  - 示例：`kubepug --k8s-version=v1.22`
## 从当前版本中移除的 API，应立即迁移！

### Ingress

- 在 extensions/v1beta1 中找到
  - 已删除：1.22
  - 替换：networking.k8s.io/v1/Ingress
  - Ingress 是允许入站连接到达后端定义的端点的规则集合。Ingress 可以配置为向服务提供外部可访问的 URL、负载均衡流量、终止 SSL、提供基于名称的虚拟主机等。已弃用 - 此 Ingress 的组版本已弃用，请使用 networking.k8s.io/v1beta1 Ingress。有关更多信息，请参阅发行说明。
  - OBJECT：bla 名称空间：blabla

**安装：**

```
kubectl krew install deprecations
```

## Kubescape：

[Kubescape](https://github.com/kubescape/kubescape/) 是一个开源 Kubernetes 安全平台，适用于您的集群、CI/CD 管道和 IDE，可将安全信号从扫描器噪音中分离出来。

安装说明 [此处](https://github.com/kubescape/kubescape/blob/master/docs/installation.md)。

**值得一提：** [kubectl-watch](https://github.com/imuxin/kubectl-watch)：另一个观察工具，可视化查看 Kubernetes 资源的增量更改。

# 故障排除 🧑🔧

## Inspektor-Gadget：

[Inspektor-gadget](https://github.com/inspektor-gadget/inspektor-gadget) 是用于调试和检查 Kubernetes 资源和应用程序的工具（或小工具）集合。

Inspektor Gadget 工具称为小工具。您可以部署一个、两个或多个小工具。

## K8s-gpt：

[k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) 是一个用于扫描您的 Kubernetes 集群、诊断和用简单的英语对问题进行分类的工具。

安装说明 [此处](https://github.com/k8sgpt-ai/k8sgpt?tab=readme-ov-file#cli-installation)。

**值得一提：** [kubectl node-shell](https://github.com/kvaps/kubectl-node-shell)：直接在正在运行的节点的主机操作系统中启动根 shell。

# 日志记录 🪵

## Stern：

[Stern](https://github.com/stern/stern) 允许您：

- 跟踪 Kubernetes 上的多个 Pod 和 Pod 中的多个容器。
- 每个结果都使用颜色编码，以便更快速地进行调试。

安装：

```
kubectl krew install stern
```

ℹ️ 使用 kubectl 插件的一些安全影响包括可能的漏洞、权限提升和无意的数据泄露。请确保仅使用积极维护的插件，并且最好在它们周围有一个活跃的社区。

# 别名 📇

有如此多的 kubectl 命令需要记住，通过使用键盘快捷键或别名来简化您的生活。

您将在此处找到一个 [存储库](https://github.com/ahmetb/kubectl-aliases)，其中包含一个 [脚本](https://github.com/ahmetb/kubectl-aliases/blob/master/generate_aliases.py)，用于生成数百个方便的 shell 别名 kubectl。问题是许多别名很长，可能难以回忆。不过不用担心，我找到了 [Benoit Couetil 撰写的这篇非常实用的博客文章](https://dev.to/zenika/kubernetes-a-pragmatic-kubectl-aliases-collection-17oc)，介绍如何处理上述脚本生成的众多别名。

# Kubectl 速查表

没有速查表，任何指南都是不完整的，对吧？

# 基本命令

## 列出 API 资源

```
kubectl api-resources
```

## 列出资源

```
kubectl get [名称]
```

## 解释资源

```
kubectl explain
```

## 使用 Pod

### 使用 nginx 映像创建一个名为“nginx-deployment”的新部署

```
kubectl run nginx-deployment --image=nginx
```

### 显示 Pod 的资源使用情况

```
kubectl top pod -n [名称空间] [pod 名称]
```

### 在 Pod 中运行命令

```
kubectl run -it [pod 名称] --image [映像名称] --rm -- [命令]
```

### 显示资源标签

```
kubectl get pods -n [名称空间] -L [标签 1] -L [标签 2]
```

### 在 Pod 中执行命令

```
kubectl exec -it [pod 名称] -- [命令]
```

### 端口转发

```
kubectl port-forward [pod 名称] [本地端口]:[远程端口]
```

### 按节点名称过滤 Pod

```
kubectl get pods --field-selector spec.nodeName=[节点名称]
```

### 按阶段过滤 Pod

```
kubectl get pods --field-selector status.phase=Running
```

### 删除默认名称空间中名为“my-pod”的 Pod

```
kubectl delete pod my-pod
```

## 使用节点

### 观察节点（旧版）

```
watch kubectl get nodes -o wide
```

### 观察节点（新版）

```
kubectl get nodes -w
```

### 节点资源利用率

```
kubectl top node [节点名称]
```

### 获取节点资源

```
kubectl describe node [节点名称]
```

## 使用部署、守护程序集和有状态集

### 重启工作负载

```
kubectl rollout restart -n [名称空间] [类型]/[名称]
```

### 部署状态

```
kubectl rollout status [类型]/[名称]
```

### 部署历史记录

```
kubectl rollout history [类型]/[名称]
```

### 扩展部署

```
kubectl scale deployment/[名称] --replicas=[副本数]
```

### 更新部署映像

```
kubectl set image deployment/[部署名称] [容器名称]=new-image:tag
```

### 观察与部署相关的事件

```
kubectl events -n glasskube-system --for=deployment/glasskube-controller-manager
```

### 删除守护程序集

```
kubectl delete daemonset [守护程序集名称]
```

## 使用作业

### 手动运行 CronJob

```
kubectl create job -n [名称空间] --from=cronjob/[cron-job-名称] [作业名称]
```

## 使用机密

### 从机密获取值
## kubectl 命令速查表

### 创建 Secret

```
kubectl create secret generic [secret-name] --from-literal=key1=value1 --from-file=ssh-privatekey=~/.ssh/id_rsa
```

### 从 Secret 中获取值

```
kubectl get secret -n [namespace] [secret-name] -o=jsonpath='{.data.[key]}' | base64 --decode
```

### 使用容器

#### 显示容器日志

```
kubectl logs -n [namespace] [pod-name]
```

#### 显示部署日志

```
kubectl logs -n [namespace] deployment/[deployment-name]
```

#### 在容器中运行命令

```
kubectl exec -it -n [namespace] [pod-name] -- [command]
```

### 命令式操作

#### 修改资源

```
kubectl edit -n [namespace] [resource-kind]/[resource-name]
```

#### 删除资源

```
kubectl delete [resource-kind]/[resource-name]
```

### 声明式操作

#### 创建资源

```
kubectl create -f [resource-file]
```

#### 使用服务器端应用 (SSA)

```
kubectl apply --server-side -f [resource-file]
```

### 事件和日志

#### 显示资源事件

```
kubectl get events -n [namespace] --field-selector involvedObject.kind=[kind] --field-selector involvedObject.name=[name]
```

#### 按类型过滤事件

```
kubectl get events --field-selector type=Warning
```

#### 按涉及对象名称过滤事件

```
kubectl get events --field-selector involvedObject.name=[resource-name]
```

#### 显示资源使用情况

```
kubectl top
```

### 其他资源

- 精选插件列表：
  [https://github.com/ishantanu/awesome-kubectl-plugins](https://github.com/ishantanu/awesome-kubectl-plugins)
- 别名列表：
  [https://github.com/ahmetb/kubectl-aliases](https://github.com/ahmetb/kubectl-aliases)
- Krew 插件仓库：
  [https://krew.sigs.k8s.io/plugins/](https://krew.sigs.k8s.io/plugins/)

如果您喜欢此类内容并希望看到更多此类内容，请考虑通过在 GitHub 上给我们一个
[Star](https://github.com/glasskube/glasskube) 来支持我们 🙏