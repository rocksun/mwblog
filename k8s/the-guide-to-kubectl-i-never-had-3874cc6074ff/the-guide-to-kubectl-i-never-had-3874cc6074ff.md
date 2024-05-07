
<!--
title: 从未有过的kubectl指南。
cover: https://miro.medium.com/v2/resize:fit:1200/1*WD8beae38C0PYq-DZw26uw.png
-->

你是哪种工程师？光看外表，有人能猜出来吗？很可能猜不出来。

> 译自 [The guide to kubectl I never had.](https://medium.com/@jake.page91/the-guide-to-kubectl-i-never-had-3874cc6074ff)，作者 Jake Page。

如果有人通过观察你的键盘就能猜出来呢？现在可能稍微容易一点了。

当键盘上的“k”键已经磨损时，你就知道自己正在与一位**Kubernetes工程师**打交道。

在 [Glasskube](https://github.com/glasskube/glasskube) 办公室，你会发现到处都是备用的 “k” 键，以备不时之需。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/0*mOPnyzrL9nFDeMFz.gif)

当然，我是在开玩笑。

我并不确定磨损的键盘能说明其主人的什么情况。但我确实知道，对于任何想要成为一名熟练的[Kubernetes](https://kubernetes.io/)管理员的人来说，kubectl 有多重要。

kubectl 是用于与 Kubernetes API 通信的 CLI 工具，它乍一看似乎很简单，但很快就会变得复杂。

因此，在这篇博文中，我的目标是编写**我刚开始时希望拥有的指南**。首先关注命令语法和有用的命令，然后再转向[插件](https://krew.sigs.k8s.io/plugins/)和工具的充满活力的生态系统，这些插件和工具旨在扩展 kubectl 和 Kubernetes 的功能。

同时分享一些提示和技巧，以及一份有用的 kubectl 速查表。

让我们开始吧。

## 免责声明

这不是一篇关于 Kubernetes 的文章。K8s 是一项极其庞大的技术，涵盖了众多概念，例如各种类型的 Kubernetes 对象及其交互。对于此讨论，我假设你熟悉这些概念。相反，我将专门关注 kubectl、它的用法以及围绕它构建的工具。

## 开始之前

如果你支持让 Kubernetes 软件包管理对每个人都更好的开源项目，那么请考虑支持 [Glasskube](https://github.com/glasskube/glasskube)，在 GitHub 上给我们一颗星。

## 安装

要安装 kubectl，你可以根据你的操作系统选择一些不同的选项。以下是如何在一些常见平台上安装它：

**Linux (Ubuntu/Debian)**

```
sudo apt-get update && sudo apt-get install -y kubectl
```

**使用 Homebrew 的 MacOS**

```
brew install kubectl
```

**使用 Chocolatey 的 Windows**

```
choco install kubernetes-cli
```

安装后，你可以通过运行以下命令来验证 kubectl 是否已正确安装：

```
kubectl version --client
```

## kubectl 命令：

kubectl 是一个命令行界面 (CLI) 工具，用于与 Kubernetes API 通信。命令有很多，多到无法记住。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/0*DTYa51mRBVTnceMO.png)

不过不用担心，它不像有些人让你想象的那么可怕。

我们将探索快速访问命令参考、特定于 k8s 对象的命令、有用的别名和命令补全的方法。但首先，命令字符串是如何构建的？

## 语法

英语和汉语是**主谓宾** (SVO) 语言。

印地语和韩语是**主宾谓** (SOV) 语言。

如果 kubectl 是一种语言，那它将是一种**kubectl + 动词 + 对象/[名称可选] + 标志 (kvof)** 语言 

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*MFaHuHzVFYtrTM5j.png)

也类似于语言，学习和吸收语法的最佳方法是在上下文中使用它，而不是死记硬背冗长的动词和对象列表。

> 如果你遇到困难，并且想要快速引用任何 Kubernetes 版本中的现有 Kubernetes 对象，请运行 kubectl api-resources。

命令是通过选择要应用于所需 Kubernetes 的**操作 [动词]**来构建的**资源 [对象]**，通常后跟资源的名称，此外，你还有大量的**过滤器 [标志]**，可以应用于命令，这些过滤器将确定最终的范围和输出。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*8-46rFQoLFOjEY-t.png)

让我们看一个使用常用的**get 动词**来检索 glasskube-system 命名空间中的所有资源的命令构建示例，并且输出采用 yaml 格式：

```
kubectl get all --namespace glasskube-system -o yaml
```

> 如果你遇到一个你以前从未听说过的 Kubernetes 资源，或者需要复习，请使用 kubectl explain [resource-name] 来获取终端描述和使用说明。

## 命令式工作

在 Kubernetes 环境中工作时，你的任务有很多，从部署新应用、对故障资源进行故障排除、检查使用情况等等。稍后，我们将探讨如何使用声明式工作方式更适合定义和部署工作负载，但对于其他所有内容，我们准备好了有用的命令式 Kubernetes 命令。

让我们开始的简单命令是：

```
# Create a new deployment named "nginx-deployment" with the nginx image
kubectl run nginx-deployment --image=nginx

# Delete a pod named "nginx-deployment" in the default namespace
kubectl delete pod nginx-deployment
```

要将命令式命令提升到下一步，请知道你可以使用[TUI](https://en.wikipedia.org/wiki/Text-based_user_interface#:~:text=In%20computing%2C%20text%2Dbased%20user,before%20the%20advent%20of%20bitmapped)编辑器来修改资源：

通过运行 kubectl edit -n [namespace] [resource-name]，将打开类似于以下内容的文本编辑器。编辑并像 [vim](https://www.vim.org/) 运行 ESC + :q! 这样退出。

```yaml
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
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
```

大多数命令都适用于所有类型的 Kubernetes 对象。在进一步讨论对某些 Kubernetes 资源有用的特定命令之前，了解可以应用于许多不同对象的某些有用标志是值得的。

## 有用标志：

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

`kubectl events -n [resource-namespace] — for=[resource-kind]/[resource-name]` 此命令获取与指定命名空间中特定资源相关的事件。它会持续监视与给定资源相关的新的事件。

```
kubectl events -n my-namespace --for=deployment/my-deployment
```

## 老派与新派监视标志：

**-o wide 与 -w：**

-o wide：这是一个 **“老派”** 标志，提供宽输出格式，显示有关资源的其他详细信息。

-w：这是一个 **“新派”** 标志，启用对资源更改的持续监视，类似于 watch 命令。

## 使用 Pod

Pod 是 Kubernetes 生态系统中最小的抽象，它们是容纳容器的逻辑单元。Pod 消耗资源，可以执行并生成日志。以下是一些可帮助您管理 Pod 的命令。

```
# Show resource usage of a pod
kubectl top pod -n [namespace] [pod-name]

# Run a command inside a new pod in the cluster
kubectl run -it ubuntu --image ubuntu --rm -- bash

# Show resource labels as columns
# e.g. kubectl get pods -n [namespace] -L vault-active -L vault-sealed
kubectl get pods -n [namespace] -L vault-active -L vault-sealed

# Execute a command inside a pod
kubectl exec -it [pod-name] -n [namespace] --

# Port forward to a pod
kubectl port-forward [pod-name] [local-port]:[remote-port] -n [namespace]

# Show container logs
kubectl logs -n [namespace] [pod-name]
kubectl logs -n [namespace] /deployment/[deployment-name]  # Use -f flag for continuous streaming

# Run a command inside an existing container
kubectl exec -it -n [namespace] [pod-name] -- [command...]
```

## 使用节点

节点是提供计算能力和存储的基础实例，Kubernetes 集群在其之上运行。

```
# Show node resource utilization
kubectl top node [node-name]  # Node name is optional; without shows table of all nodes

# Get node information
kubectl get node
```

## 使用 Deployments, DaemonSets 和 StatefulSets

部署、守护程序集和有状态集是 Kubernetes 中的更高级别的抽象，用于管理应用程序工作负载的部署和扩展。


```
# Restart a workload (e.g. deployment, stateful set, daemon set)
kubectl rollout restart -n [namespace] [workload-kind]/[workload-name]  # Triggers a re-creation of all pods for this workload, adhering to the workload configuration

# Check the status of a deployment rollout
kubectl rollout status deployment/[name]

# View rollout history of a deployment
kubectl rollout history deployment/[name]  # View rollout history of a deployment

# Scale a deployment to the specified number of replicas
kubectl scale deployment/ --replicas=[number]  # Scale a deployment to the specified number of replicas

# Watch events related to a deployment
kubectl events -n glasskube-system --for=deployment/glasskube-controller-manager  

#Update Deployment Image
kubectl set image deployment/[deployment-name] [container-name]=new-image:tag

# Delete DaemonSet
kubectl delete daemonset [daemonset-name]
```

## 使用 Job

作业管理 pod 的执行以执行特定任务，并确保在终止之前成功完成该任务。

```
# Run a CronJob manually
kubectl create job [job-name] --image=image/name

# Creates a new job from the job template specified in the cronjob
kubectl create job -n [namespace] --from=cronjob/[cron-job-name] [job-name]
```

## 使用 Secret

Secret 用于在 Kubernetes 中安全地存储敏感信息，如密码、OAuth 令牌和 SSH 密钥。

```
# Create Secret
kubectl create secret generic [secret-name] --from-literal=key1=value1 --from-file=ssh-privatekey=~/.ssh/id_rsa

# Get a value from a secret
kubectl get secrets -n [namespace] [secret-name] --template='{{ .data.[key-name] | base64decode }}'

# Get a value from a secret using jsonpath
kubectl get secrets [secret-name] -o jsonpath="{.data.key1}" | base64 --decode
```

> JSONPath 是一种查询语言，用于从 JSON 文档中提取特定数据。在 Kubernetes 中，JSONPath 表达式通常与 kubectl 命令中的 `-o jsonpath` 标志一起使用，以从这些命令的输出中提取特定信息。

## Shell 补全

您可能已注意到，kubectl 命令很快就会变得很长。可以将一个非常漂亮的 shell 补全脚本添加到您的 bash 或 zshell 文件中以启用轻松的标签补全。无需再死记硬背了。要在所有 shell 会话中实现这一点，请将以下内容添加到您的 ~/.zshrc 文件中：

```
source <(kubectl completion zsh)
```

并重启shell。如果您使用 bash，请按照此处的说明进行操作：

```
# Install bash-completion package
sudo apt-get install -y bash-completion
# Store the output of the completion command in .bashrc
echo "source <(kubectl completion bash)" >> ~/.bashrc
# Activate the completion rules
source ~/.bashrc
```

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*ibkrc8KB9DM31Jcb.gif)

## 声明性工作

Kubernetes 资源的声明性管理涉及使用 YAML 清单文件指定资源的所需状态，并将这些清单应用到集群。

### 创建 YAML 文件

无论 Kubernetes 对象是由您自己编写的还是由其他人编写的，所有对象均定义在 YAML 文件中。Kubernetes API 就是通过 YAML 文件定义来了解集群状态的：

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

若要从头开始创建此部署，请使用 kubectl create 命令：

```
kubectl create -f glasskube-deployment.yaml
```

### 应用 YAML 文件(客户端应用)

运用 YAML 文件是管理 Kubernetes 资源的标准方法。您可以用 YAML 格式定义您资源的所需状态，并将这些 YAML 文件应用于该集群。

```
kubectl apply -f manifest.yaml
```

### 服务器端应用 (SSA)

服务器端应用是将配置更改应用到 Kubernetes 资源的一种较新方法。使用 SSA，变更会直接应用于服务器端，这意味着 Kubernetes API 服务器负责确保实现所需状态。

```
kubectl apply --server-side -f manifest.yaml
```

## 插件和工具

每当我看到一些来回讨论 Kubernetes 的内容时，它到底是什么。它最适合哪些用例以及如何最好地思考它，[Kelsey Hightower](https://twitter.com/kelseyhightower/status/935252923721793536?lang=en) 的同一条推文会浮现在我脑海里。

![](https://miro.medium.com/v2/resize:fit:640/format:webp/0*uHKNAJDe7ywGBXeL.png)

这一观点被广泛认可，Kubernetes 插件和工具的大量生态系统证明了这一点，这些插件和工具旨在帮助处理 Kubernetes 生命周期中的各个阶段。

### Krew Kubernetes 插件管理器

一个强大的插件管理器，用于查找新插件是 [krew](https://krew.sigs.k8s.io/docs/user-guide/setup/install/)，安装方法如下。通过 Krew 安装 kubectl 插件的命令：

```
kubectl krew install <PLUGIN_NAME>
```

让我们探索一些主要的调试和工具类别，重点介绍一些最实用的项目。由于有许多值得关注的地方，因此我将为每个部分添加一个荣誉部分。

### 内容和命名空间切换

在 Kubernetes 环境中，您始终在两个层次结构上下文中操作集群和命名空间。确保准确的命令执行需要指定适当的上下文以获得所需的输出。切换集群上下文或命名空间可能涉及难以记住的长命令，这就是 Kubectl 和 Kubens 等工具的用武之地。

**Kubectx 和 Kubens**

在此轻松查看可用的集群和命名空间，并在它们之间轻松切换。

请在[此处](https://github.com/ahmetb/kubectx)查看安装说明。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*wunuUoxOe-jOrBJB.gif)

**值得称赞的：** 

[kubectl-cf](https://github.com/surfinggo/kubectl-cf)：一种在 kubeconfig 文件（而不是上下文）之间切换的更快方法。

## 可见性

Kubernetes 集群是复杂的系统，包含许多相互依赖的活动部分，以使您的应用得以运行。始终清晰地了解正在发生的事情至关重要。

### k9s

[K9s](https://k9scli.io/) 是一个方便、轻量级的交互式 Kubernetes 仪表盘，运行在终端中。除了可视化你的 k8s 资源外，你还可以轻松的进入 pods 中，编辑清单，并且在一处管理你的工作负载。这或许是我最喜欢的 Kubernetes 管理工具之一。

安装说明在[这里](https://k9scli.io/topics/install/)。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*ATgLknN4UVRSzRFv.gif)

### kubectl tree

一个 kubectl 插件，用于通过对象上的 ownersReferences 探索 Kubernetes 对象之间的所有权关系。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*vhRiVZ8jREVyLXVA.png)

**安装**：

```
kubectl krew install tree
kubectl tree --help
```

### kubecolor

KubeColor 用于为 kubectl 输出添加颜色。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*NcOP0FXIamKjyen-.png)

[此处](https://github.com/kubecolor/kubecolor?tab=readme-ov-file#installation)为安装说明。

## 包管理

使用常规包管理工具进行集群包管理可能会令人抓狂，并且更新包十分繁琐。配置很笨拙，直到现在，以声明方式应用所需的软件包栈仍然超出掌控范围。

**Glasskube：**

有了 Glasskube，传统包管理器（如 helm）中发现的所有痛点均可迎刃而解，确保您有时间管理工作负载，不必担心管理您的 k8s 软件包堆栈。

## 网络

### Kubectl-Cilium:

kubectl-Cilium 是一款与 Cilium 交互的插件，Cilium 是一种基于 eBPF 的云原生解决方案，用于在工作负载之间提供、保护和观察网络连接。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*KP_Qd24dGGNynisa.png)

安装：

```
kubectl krew install cilium
```

### Cert-manager

Cert-manager 将证书和证书颁发者添加为 Kubernetes 集群中的资源类型，简化了获取、更新和使用这些证书。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*fqhNbneZAh3Xx_Bf.png)

安装说明请见此处。

**特别提及**： 

[Ksniff](https://github.com/eldadru/ksniff)：这是一个利用 tcpdump 和 Wireshark 在 Kubernetes 集群中的任何 Pod 上启动远程捕获的 kubectl 插件。

## RBAC

**Kubelogin**

[Kubelogin](https://github.com/int128/kubelogin) 是 Kubernetes OpenID Connect (OIDC) 认证的插件，也称为 kubectl oidc-login。

安装说明在[这里](https://github.com/Azure/kubelogin?tab=readme-ov-file#installation)。

**Kube-policy-advisor**

[Kube-policy-advisor](https://github.com/sysdiglabs/kube-policy-advisor) 更便于从活动 K8s 环境或包含 Pod 规范（部署、守护进程集、Pod 等）的单个 .yaml 文件创建 K8s Pod Security Policies (PSP) 或 OPA Policy。

安装：

```
kubectl krew install advise-policy
```

值得称赞的： 

- [kubectl-who-can](https://github.com/aquasecurity/kubectl-who-can)：显示在 Kubernetes 中 SUBJECTS 对 VERB [TYPE | TYPE/NAME | NONRESOURCEURL] 拥有 RBAC 权限。 
- [rakkess](https://github.com/corneliusweig/rakkess)：评估访问 - kubectl 插件，用于展示服务器资源的访问矩阵 
- [kubectl-rolesum](https://github.com/Ladicle/kubectl-rolesum)：汇总指定主题（ServiceAccount、用户和组）的 RBAC 角色。

## Linting

**Kubectl-neat:**

[Kubectl-neat](https://github.com/itaysk/kubectl-neat)：Kubectl-neat 去除了 Kubernetes 清单中的混乱内容，让清单更具可读性。它主要查找两类内容并予以忽略：由 Kubernetes 对象模型插入的默认值和常见的变异控制器。

安装：

```
kubectl krew install neat
```

**KubeLinter：**

[KubeLinter](https://github.com/stackrox/kube-linter) 分析 Kubernetes YAML 文件和 Helm chart，并将它们与各种最佳实践进行对比，重点关注生产准备和安全性。

安装说明：https://github.com/stackrox/kube-linter?tab=readme-ov-file#installing-kubelinter。

## 集群维护和安全

**KubePug** 

[KubePug](https://github.com/kubepug/kubepug) 会下载包含针对特定 Kubernetes 版本的 API 弃用信息的已生成数据文件 data.json，扫描正在运行的 Kubernetes 集群以确定是否有任何对象会受弃用影响，并向用户显示受影响的对象。

示例：

您可以使用以下命令查看正在运行的集群的状态。

```
$ kubepug --k8s-version=v1.22 # Will verify the current context against v1.22 version
[...]
RESULTS:
Deprecated APIs:
PodSecurityPolicy found in policy/v1beta1
     ├─ Deprecated at: 1.21
     ├─ PodSecurityPolicy governs the ability to make requests that affect the Security Context that will be applied to a pod and container.Deprecated in 1.21.
        -> OBJECT: restrictive namespace: default


Deleted APIs:
     APIs REMOVED FROM THE CURRENT VERSION AND SHOULD BE MIGRATED IMMEDIATELY!!
Ingress found in extensions/v1beta1
     ├─ Deleted at: 1.22
     ├─ Replacement: networking.k8s.io/v1/Ingress
     ├─ Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give servicesexternally-reachable urls, load balance traffic, terminate SSL, offer namebased virtual hosting etc.DEPRECATED - This group version of Ingress is deprecated by networking.k8s.io/v1beta1 Ingress. See the release notes for more information.
        -> OBJECT: bla namespace: blabla
```

**安装：**

```
kubectl krew install deprecations
```

**Kubescape：**

[Kubescape](https://github.com/kubescape/kubescape/) 是一个开源 Kubernetes 安全平台，适用于您的集群、CI/CD 管道和 IDE，可将安全信号从扫描器噪音中分离出来。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*RvXKaSHdoTH__D30.gif)

安装说明 [此处](https://github.com/kubescape/kubescape/blob/master/docs/installation.md)。

**值得一提：** 

[kubectl-watch](https://github.com/imuxin/kubectl-watch)：另一个观察工具，可视化查看 Kubernetes 资源的增量更改。

## 故障排除

**Inspektor-Gadget：**

[Inspektor-gadget](https://github.com/inspektor-gadget/inspektor-gadget) 是用于调试和检查 Kubernetes 资源和应用程序的工具（或小工具）集合。

Inspektor Gadget 工具称为小工具。您可以部署一个、两个或多个小工具。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*YGg7sV2agvaZaazv.png)

**K8s-gpt：**

[k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) 是一个用于扫描您的 Kubernetes 集群、诊断和用简单的英语对问题进行分类的工具。

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*tAAho9i7A-9aTEcA.gif)

安装说明[此处](https://github.com/k8sgpt-ai/k8sgpt?tab=readme-ov-file#cli-installation)。

**值得一提：** 

[kubectl node-shell](https://github.com/kvaps/kubectl-node-shell)：直接在正在运行的节点的主机操作系统中启动根 shell。

## 日志记录

**Stern：**

[Stern](https://github.com/stern/stern) 允许您跟踪 Kubernetes 上的多个 Pod 和 Pod 中的多个容器。每个结果都使用颜色编码，以便更快速地进行调试。

安装：

```
kubectl krew install stern
```

> 使用 kubectl 插件的一些安全影响包括可能的漏洞、权限提升和无意的数据泄露。请确保仅使用积极维护的插件，并且最好在它们周围有一个活跃的社区。

## 别名

有如此多的 kubectl 命令需要记住，通过使用键盘快捷键或别名来简化您的生活。

您将在此处找到一个[存储库](https://github.com/ahmetb/kubectl-aliases)，其中包含一个 [脚本](https://github.com/ahmetb/kubectl-aliases/blob/master/generate_aliases.py)，用于生成数百个方便的 shell 别名 kubectl。问题是许多别名很长，可能难以回忆。不过不用担心，我找到了[Benoit Couetil 撰写的这篇非常实用的博客文章](https://dev.to/zenika/kubernetes-a-pragmatic-kubectl-aliases-collection-17oc)，介绍如何处理上述脚本生成的众多别名。

## Kubectl 速查表

没有速查表，任何指南都是不完整的，对吧？

```
# Basic Commands
# List API Resources
kubectl api-resources

# List Resources
kubectl get [name]

# Explain Resources
kubectl explain

# Working with Pods
# Create a new deployment named "nginx-deployment" with the nginx image
kubectl run nginx-deployment --image=nginx

# Show Resource Usage of a Pod
kubectl top pod -n [namespace] [pod-name]

# Run Command in Pod
kubectl run -it [pod-name] --image [image-name] --rm -- [command]

# Show Resource Labels
kubectl get pods -n [namespace] -L [label1] -L [label2]

# Execute Command in Pod
kubectl exec -it [pod-name] -- [command]

# Port Forwarding
kubectl port-forward [pod-name] [local-port]:[remote-port]

# Filtering Pods by Node Name
kubectl get pods --field-selector spec.nodeName=[node-name]

# Filtering Pods by Phase
kubectl get pods --field-selector status.phase=Running

# Delete a pod named "my-pod" in the default namespace
kubectl delete pod my-pod

# Working with Nodes
# Watch Nodes (Old School)
watch kubectl get nodes -o wide
# Watch Nodes (New School)
kubectl get nodes -w

# Node Resource Utilization
kubectl top node [node-name]

# Get Node Resource
kubectl describe node [node-name]

# Working with Deployments, Daemonsets, and StatefulSets
# Restart Workload
kubectl rollout restart -n [namespace] [kind]/[name]

# Rollout Status
kubectl rollout status [kind]/[name]

# Rollout History
kubectl rollout history [kind]/[name]

# Scale Deployment
kubectl scale deployment/[name] --replicas=[replica-count]

#Update Deployment Image
kubectl set image deployment/[deployment-name] [container-name]=new-image:tag

# Watch events related to a deployment
kubectl events -n glasskube-system --for=deployment/glasskube-controller-manager  

# Delete DaemonSet
kubectl delete daemonset [daemonset-name]

# Working with Jobs
# Run CronJob Manually
kubectl create job -n [namespace] --from=cronjob/[cron-job-name] [job-name]

# Working with Secrets
# Get Value from Secret
kubectl get secret -n [namespace] [secret-name] -o=jsonpath='{.data.[key]}' | base64 --decode

# Create Secret
kubectl create secret generic [secret-name] --from-literal=key1=value1 --from-file=ssh-privatekey=~/.ssh/id_rsa

# Get a value from a secret
kubectl get secrets -n [namespace] [secret-name] --template='{{ .data.[key-name] | base64decode }}'

# Working with Containers
# Show Container Logs
kubectl logs -n [namespace] [pod-name] 
kubectl logs -n [namespace] deployment/[deployment-name]

# Run Command in Container
kubectl exec -it -n [namespace] [pod-name] -- [command]

# Working Imperatively
# Modify Resource
kubectl edit -n [namespace] [resource-kind]/[resource-name]

# Delete Resource
kubectl delete [resource-kind]/[resource-name]

# Create Resource
kubectl create -f [resource-file]

# Working Declaratively
# Use Server-Side Apply (SSA)
kubectl apply --server-side -f [resource-file]

# Events and Logs
# Show Events for Resource
kubectl get events -n [namespace] --field-selector involvedObject.kind=[kind] --field-selector involvedObject.name=[name]

# Filtering Events by Type
kubectl get events --field-selector type=Warning

# Filtering Events by Involved Object Name
kubectl get events --field-selector involvedObject.name=[resource-name]

# Show Resource Usage
kubectl top
```

## 其他资源

- 精选插件列表：  [https://github.com/ishantanu/awesome-kubectl-plugins](https://github.com/ishantanu/awesome-kubectl-plugins)
- 别名列表：  [https://github.com/ahmetb/kubectl-aliases](https://github.com/ahmetb/kubectl-aliases)
- Krew 插件仓库：[https://krew.sigs.k8s.io/plugins/](https://krew.sigs.k8s.io/plugins/)

如果您喜欢此类内容并希望看到更多此类内容，请考虑通过在 GitHub 上给我们一个 [Star](https://github.com/glasskube/glasskube) 来支持我们。