<!--
title: k0smotron Anywhere: 成为完整的ClusterAPI基础设施Provider
cover: ./cover.png
-->

管理多个 Kubernetes 集群，甚至可能跨越多个基础设施，绝对不容易。Cluster API 可以通过引入一种声明性的方式来管理基础设施和集群设置。但是，如果您想在本地、裸金属或其他类似环境中使用，而现有的 Cluster API provider 并没有真正涵盖，也不用担心，我们有您的后盾。现在，有了 [k0smotron](https://k0smotron.io/) Anywhere，您可以在任何基础设施上使用 Cluster API，甚至是裸金属，而无需给您的基础设施添加任何复杂性。

> 译自 [k0smotron Anywhere: Now a complete ClusterAPI infrastructure provider](https://medium.com/k0sproject/k0smotron-anywhere-now-a-complete-clusterapi-infrastructure-provider-7da7b633331f)。作者 Jussi Nummelin 。

今天，我们很高兴宣布 [k0smotron v0.8.0](https://github.com/k0sproject/k0smotron/releases/tag/v0.8.0) 的可用性以及 k0smotron Anywhere（又名[远程机器基础设施provider](https://docs.k0smotron.io/stable/capi-remote/)）的完成。完成意味着 k0smotron Anywhere 现在可以作为符合 [Cluster API](https://cluster-api.sigs.k8s.io/) 的基础设施provider运行。这为在您的 Kubernetes 集群中无缝管理远程机器打开了新的可能性。

如果你忘记了 k0smotron 是什么，它本质上是一组 Kubernetes 控制器，允许你在单个 Kubernetes 集群中以 pods 的形式运行和管理多个 Kubernetes 集群控制平面。这样可以实现更精细的控制，并且由于减小了任何控制平面故障的“爆炸半径”，具有更强大的容错性。随着 Kubernetes 部署到更分布式的应用中，这种更精细的方法对于可靠性和弹性变得至关重要。自从大约 6 个月前的[初始发布](https://medium.com/k0sproject/introducing-k0smotron-c2ed6535ddc8)以来，它已经发展成为不仅仅是控制平面，还充当 ClusterAPI 的通用 [k0s](https://k0sproject.io/) provider。

对于那些使用或关注我们的 k0s 项目的人，你们知道我们非常认真地对待我们的“零故事”。对于 k0smotron Anywhere 来说，这意味着零依赖。最新版本证明了我们对此是多么认真，实际上允许你以无provider的模式使用 ClusterAPI。我们是什么意思呢？跟着阅读，我们将向你展示它是什么以及它是如何工作的。

## 什么是 k0smotron Anywhere？

k0smotron Anywhere 扩展了 k0smotron 作为 ClusterAPI provider 的功能，通过 SSH 连接无缝管理远程机器。这意味着你现在可以在任何基础设施中 provisioning 机器，不仅限于支持 ClusterAPI 并由 API 驱动的环境。你可以将其看作是 Cluster API 的无 provider 提供程序。

## 关键优势

- **灵活性**：在云中、本地或混合设置中的任何位置运行 Kubernetes 工作负载。
- **基础设施中立性**：k0smotron Anywhere 支持任何基础设施，通过 Cluster API 提供一种一致的方法来管理您的 Kubernetes 集群。
- **使用现有机器**：轻松将现有机器整合到您的 Kubernetes 集群中，充分发挥其作用。

## 它是如何工作的？

有了 k0smotron Anywhere 功能，可能性是无穷的。创建定义远程基础设施的 RemoteMachines，指定其详细信息，如地址、端口、用户和 SSH 密钥。然后，这些远程机器可以作为您的 Kubernetes 集群的一部分使用。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*sHhY7KPojPJex_t3vwcRpw.png)

实质上，`RemoteMachine` 控制器会等待直到看到引导提供程序创建的 cloud-init 密钥。一旦 cloud-init 就绪，它将使用 SSH 连接到 `RemoteMachine` 并执行 cloud init 命令。

比如说，假设您有一台裸金属机器，运行在您的私有数据中心。以下是如何将其定义为 RemoteMachine 的示例：

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: RemoteMachine
metadata:
 name: my-remote-machine
spec:
 address: 192.168.1.100
 port: 22
 user: remoteuser # Needs to have sudo capabilities
 sshKeyRef:
   name: ssh-key-secret
```

正如你所见，您只需要提供 SSH 连接详细信息，如地址、用户和 SSH 密钥，通过一个密钥，然后您就可以开始了。k0smotron RemoteMachine 控制器然后使用这些详细信息，连接到机器并执行由引导提供程序创建的 cloud-init 配置。而且，由于 k0s 的“零依赖”，基本上您只需要安装基础 Linux 操作系统，无需其他。您可以自由选择您喜欢的任何 Linux 发行版，绝对不需要向您的基础设施添加任何配置或其他复杂性。

然后，您可以将 RemoteMachine 用作集群的一部分，就像使用任何其他基础设施提供程序一样。例如，您可以通过 `Machine` 对象将其用作工作节点：

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: Machine
metadata:
  name:  remote-test-0
  namespace: default
spec:
  clusterName: remote-test
  bootstrap:
    configRef:
      apiVersion: bootstrap.cluster.x-k8s.io/v1beta1
      kind: K0sWorkerConfig
      name: remote-test-0
  infrastructureRef:
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: RemoteMachine
    name: remote-test-0
---
apiVersion: bootstrap.cluster.x-k8s.io/v1beta1
kind: K0sWorkerConfig
metadata:
  name: remote-test-0
  namespace: default
spec:
  version: v1.27.2+k0s.0
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: RemoteMachine
metadata:
  name: remote-test-0
  namespace: default
spec:
  address: 1.2.3.4
  port: 22
  user: root
  sshKeyRef:
    # This defines which SSH key to use for connecting to the machine. The Secret needs to have key 'value' with the SSH private key in it.
    name: footloose-key
```

## 使用 RemoteMachine 与 MachineDeployments 和 ControlPlanes

显然，`RemoteMachine` 是一个准备作为 Kubernetes 节点运行的单个机器，可以作为工作节点或控制平面节点。然而，在某些情况下，我们需要能够将它们与 ClusterAPI 的更高级别结构一起使用，例如 `MachineDeployment` 和 `ControlPlanes`。这些需要使用 `MachineTemplates`。那么，如何弥合单个 `RemoteMachine` 和 `MachineTemplate` 之间的差距呢？

这就是 `RemoteMachine` 池化概念发挥作用的地方。实质上，您可以创建多个 [PooledRemoteMachine](https://docs.k0smotron.io/stable/capi-remote/#using-remotemachines-in-machinetemplates-of-higher-level-objects) 对象，标记那些可以使用的机器。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/1*5zTLqWui4KSktdbfexrS2g.png)

以下是如何通过 RemoteMachineTemplate 对象利用 PooledRemoteMachines 的示例：

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: RemoteMachineTemplate
metadata:
  name: remote-test-template
  namespace: default
spec:
  template:
    spec:
      pool: default
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: PooledRemoteMachine
metadata:
  name: remote-test-0
  namespace: default
spec:
  pool: default
  machine:
    address: 1.2.3.4
    port: 22
    user: root
    sshKeyRef:
      name: footloose-key-0
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: PooledRemoteMachine
metadata:
  name: remote-test-1
  namespace: default
spec:
  pool: default
  machine:
    address: 2.3.4.5
    port: 22
    user: root
    sshKeyRef:
      name: footloose-key-1
```

当 k0smotron 看到相应的 `RemoteMachineTemplate` 时，它将从池中选择一个空闲的机器并创建相应的 `RemoteMachine` 对象。当然，k0smotron `RemoteMachine` 控制器会跟踪正在使用的 `PooledRemoteMachine` 以及用于哪个 `RemoteMachine`。

一旦您有了一些池化的机器，您可以通过 `RemoteMachineTemplate` 对象将它们与其他 ClusterAPI 结构一起使用：

```yaml
apiVersion: controlplane.cluster.x-k8s.io/v1beta1
kind: K0sControlPlane
metadata:
 name: remote-test
spec:
 replicas: 1
 k0sVersion: v1.27.1+k0s.0
 k0sConfigSpec:
   k0s:
     apiVersion: k0s.k0sproject.io/v1beta1
     kind: ClusterConfig
     metadata:
       name: k0s
     spec:
       api:
         extraArgs:
           anonymous-auth: "true"
 machineTemplate:
   infrastructureRef:
     apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
     kind: RemoteMachineTemplate
     name: remote-test-template
     namespace: default
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: RemoteMachineTemplate
metadata:
 name: remote-test-template
 namespace: default
spec:
 template:
   spec:
     pool: default
```

等等，这是什么意思？这是否意味着我可以利用裸金属基础设施进行自动扩展等操作？嗯，有点像。当然，自动扩展程序无法为您带来新的机器到数据中心，但所有这些将允许您以一种方式使用自动扩展程序和其他类似功能，在集群中收到需要另一台机器的信号时。然后通过将新机器添加到池中，自动扩展程序和 Cluster API 将自动捕捉到并将其加入集群。

## 对生态系统的好处

k0smotron Anywhere 的引入符合使 Kubernetes 集群更具适应性并适应各种基础设施需求的更广泛目标。通过对 RemoteMachines 和池化的支持，k0smotron 本质上将 Kubernetes ClusterAPI 打开，以支持任何基础设施，而不仅仅是那些已经有 CAPI provider 的情况。更不用说像裸金属这样的基础设施，很难进行自动化。

## 接下来是什么？

我们即将关注的重点包括在 k0smotron 上集成 [ClusterClass](https://cluster-api.sigs.k8s.io/reference/glossary.html#clusterclass) 支持。这一重要的增强与我们致力于提供全面的 Kubernetes 管理解决方案的承诺一致。此外，我们正在积极努力将 [clusterctl](https://cluster-api.sigs.k8s.io/clusterctl/provider-contract.html#clusterctl-provider-contract) 的内置支持纳入其中。这一进展旨在简化在管理集群中初始化 k0smotron 的过程。

一旦这些功能得到无缝集成，k0smotron 将接近功能完备。对我们来说，功能完备标志着迈向通用可用性（GA）的重要一步。这一过渡涉及到对文档的大量精炼工作，以确保用户能够清晰简单地理解。此外，我们的奉献还体现在建立一流的维护和支持流程上，使 k0smotron 成为强大可靠的解决方案。

哦，还有那些使用 [Lens](https://k8slens.dev/) 管理集群的人，我们已经开始开发一个 Lens 扩展，将完整的 Cluster API 可见性带到 Lens 中。

## 立即开始！

准备好发挥 k0smotron Anywhere 的威力了吗？升级到[最新版本](https://github.com/k0sproject/k0smotron/releases/latest)，开始探索在 Kubernetes 集群中管理远程机器的灵活性和便利性。

敬请关注来自 k0smotron 团队和生态系统的更多更新和令人兴奋的功能。愉快集群！哦，别忘了给我们的 [GitHub 仓库](https://github.com/k0sproject/k0smotron/)加个星星。
