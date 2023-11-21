<!--
title: 探索Kubernetes的多租户解决方案
cover: http://example.com/cover.png
-->

## 简介

Kubernetes中的多租户会带来各种复杂的挑战，例如安全性、公平性和资源分配。本博客讨论了与多租户相关的挑战，以及为名为[Labs4grabs.io](http://labs4grabs.io/)的基于Kubernetes的学习平台所做的技术选择。我将探讨两个关键技术vCluster和Kubevirt的需求、优势和劣势。这些技术在开发[Labs4grabs.io](http://labs4grabs.io/)的后端时进行了试验。尽管vCluster非常出色，但我还是决定完全放弃它。


> 译自 [Exploring Multi-Tenancy Solutions for my Kubernetes Learning Platform](https://medium.com/berops-blog/exploring-multi-tenancy-solutions-for-my-kubernetes-learning-platform-4eae52ff4887) 。

## 关于Labs4grabs.io

我的平台是一个Kubernetes学习平台，旨在通过实验环境模拟现实中的问题。但是，除了每个实验的简要描述和几条提示之外，人们需要自行研究和解决问题，指导很少。

实验内容基于我在Berops公司担任Kubernetes工程师时遇到的真实问题，以及我以前在该领域的经验。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/0*kXRnevIEpeTUkoHh.png)

*挑战是直接从Slack开始的。*

## 什么是多租户？

Kubernetes的多租户类似于管理公寓大楼，不同租户共享空间。每个租户都需要自己的空间，如浴室、厨房和卧室，以及水、煤气、电等公共设施。但最重要的是，公寓的租户不能进入其他人的区域或使用其他人的设施。此外，如果其他租户进入他们的私人区域，每个租户都会深感不快。这意味着其他租户的生活质量降低。

Kubernetes中的租户情况也是如此，他们不能访问其他租户的资源、网络带宽等。这会降低想在我的平台上提高Kubernetes技能的人的体验质量。此外，与公寓租户不同的另一个最重要的组成部分是主机系统。

如果租户能逃出自己的环境进入主机系统，影响其他租户，使用全部计算能力进行挖矿或其他活动，那将是最大的灾难。在为Labs4grabs.io租户环境选择正确的多租户技术时，这是我最担心的。

> **主机平台的注意事项**：我选择了Kubernetes作为托管租户环境的平台。Kubernetes具有调度、网络、存储管理、安全等功能，最重要的是背后有强大的社区支持可以解答我可能遇到的任何问题。*

![](https://miro.medium.com/v2/resize:fit:786/format:webp/0*S2t9r5v20xONBS8E.png)

*租户部署在工作节点上的宿主Kubernetes集群。*

## 多租户的挑战

在选择和测试正确的解决方案时，有几个因素需要考虑：

* **安全性**: 提供计算能力和root访问权限时，必须考虑安全影响。
* **学习内容**: 使用某些租户解决方案时，可用的学习内容可能受到限制。
* **资源消耗**: 某些解决方案的资源消耗更大，这会降低主机集群上的租户密度。
* **置备时间**: 与其他解决方案相比，某些解决方案启动实验室需要更长时间。

## 纯 Kubernetes

最简单的多租户形式是为每个学生配置一个新的 Kubernetes 用户，提供证书和密钥以访问主机集群命名空间。这种解决方案简单但风险较大，需要学生通过主机集群的 API 服务器访问实验环境。但是，这种方法可能导致问题，例如学生创建过多 NodePort 服务，降低其他学生的体验，或者向 API 服务器发送数百万请求，影响合法用户的性能。

虽然使用 Kyverno、Gatekeeper 等策略引擎有助于防止用户违反某些规则，但需要通过大量试错为每个实验正确配置策略。此外，这些策略可能会限制学生创建自己的命名空间、访问根文件系统或部署特权容器等，这些都是 Kubernetes 学习的重要方面。

![](https://miro.medium.com/v2/resize:fit:786/format:webp/0*Xd0yru2N-_VjGX0v.png)

*主机Kubernetes集群中，学生无法直接访问主机集群的控制平面，但可以自由访问他们声明的环境。*

## vCluster

vCluster 是在主机 Kubernetes 集群之上运行的 Kubernetes 集群。vCluster 不具备自己的节点池或网络，它会在主机集群内调度工作负载，同时维护自己的控制平面。

vCluster 是我的多租户问题的绝佳解决方案。它提供了速度、更好的安全性和易用性。最出色的是 syncer 功能，它可以复制租户环境中的学生创建的资源到主机集群上。您可以指定要复制的资源类型和数量。这个功能改变了我可以为学生提供的内容。

> 比如在第一个中级实验“**调试 Python Flask 应用程序**”中使用了 syncer，允许学生创建 ingress 资源并使他们的应用程序在主机集群上可公开访问。

![](https://miro.medium.com/v2/resize:fit:828/format:webp/0*WVI-pv2rLU3k21rL.png)

*vCluster在租户上创建了一个指向主机集群上调度的pod的假服务和pod。*


好的，请允许我继续第二次翻译:

### 演示

在这个演示中，我们将在 `student` 名字空间中创建一个基本的 vCluster 租户环境。然后我们将在这个租户环境中创建一个 NGINX pod，并通过 NodePort 服务将其暴露出来。这个服务将被同步到主集群中，允许从外界通过主机的公网 IP 访问 NGINX pod。

1. 使用特权 pod 安全准入创建 `student` 名字空间:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: student
  labels:
    pod-security.kubernetes.io/enforce: privileged
```

2. 创建 vCluster 租户环境:

```bash
vcluster create tenant -n student --connect=false
```

3. 查看 vCluster 租户环境中运行的所有 pod:

```bash
$ vcluster connect tenant --namespace student -- kubectl get pods -A
NAMESPACE     NAME                       READY   STATUS    RESTARTS   AGE
kube-system   coredns-5c96599dbd-fsmwj   1/1     Running   0          116s  
```

4. 在租户环境内创建一个 NGINX pod，然后通过 NodePort 服务暴露，并通过主机的公网 IP 访问:

```bash
$ vcluster connect tenant --namespace student -- kubectl run pod nginx --image nginx
service/nginx exposed

$ vcluster connect tenant --namespace student -- kubectl expose pod nginx --type=NodePort --port 80
service/nginx exposed

$ kubectl get service -n student
NAME                                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                  AGE
....
nginx-x-default-x-tenant            NodePort    10.43.229.163   <none>        80:31871/TCP             2m36s

$ curl $HOST_PUBLIC_IP:31871
<!DOCTYPE html>
GENERIC NGINX OUTPUT
</html>
```

> 💡 您可以不通过 `vcluster` 命令连接到 vCluster，而是通过公共 kubeconfig，这是我的实验要求，因为不能要求学生安装 vCluster 命令行并期望获得“真正的 Kubernetes 体验”。

### 优点

* Syncer syncer syncer！其他解决方案无法通过与主集群同步来提供公网访问，我不得不自己编写解决方案。

```yaml
sync:
  services:
    enabled: true
  ingresses:
    enabled: true
  persistentvolumeclaims:
    enabled: true
```

* vCluster 相比虚拟机更轻量，所以我可以在硬件上获得更好的实验密度。
* 启动快，因为 vCluster 只是几个容器，只需要几秒钟的时间即可完成设置。
* 我不必使用物理机来托管我的实验环境，我可以使用虚拟机来托管 vCluster 租户，并利用虚拟机的所有可扩展性优势。

### 缺点

* 它不提供核心组件的可见性。如果连接到 vCluster，您将看不到 API 服务器、调度程序或控制器管理器。这限制了核心 Kubernetes 组件的学习内容。
* vCluster 不允许拥有比主集群更多的节点。这限制了高级调度的学习内容。
* 我设想该平台可以包括模拟诸如操作系统组件损坏、kubelet 损坏、网络桥接配置错误、DNS 损坏或控制平面损坏等场景的内容。然而，所有这些场景都需要 SSH 访问租户环境，而 vCluster 和容器通常不支持这种访问。

总而言之，vCluster 的限制会严重限制我想为学生提供的学习平台中的某些内容和场景。虽然 syncer 确实启用了其他解决方案无法实现的某些内容访问，但它也会阻止比它允许的更多的内容，这与我对该平台的目标不符。此外，我仍可以探索开发自定义 syncer 以在更小规模上复制 vCluster 同步器的功能的可能性。然而，我放弃了 vCluster，决定采用虚拟化。

## Firecracker 和 Kata 容器

这是关于 Firecracker 和 Kata 容器这两项技术的概述，它们在 Kubernetes 中启用了 Firecracker 运行时。我调查并实验了这些技术，但决定不使用 Kata 容器，因为它需要为 Firecracker 运行时进行额外的配置，特别是与设备映射器相关的配置，这让我感到不太舒服。配置 Firecracker 容器的 SSH 连接也需要额外的步骤，这可能会导致一个非常大的容器，可能无法实现我想要的结果：一个基本的 Kubernetes 集群，具有完整的操作系统，我可以随意破坏。

## Kubevirt

考虑到 vCluster 在可能缺少的学习内容选项方面的限制，研究指向了虚拟化。这种方法在安全性和与宿主系统的完全隔离方面提供了保证，允许使用完整的操作系统和无限的学习内容。

幸运的是，Kubernetes 中有两种可用的虚拟化技术：Kubevirt 和 Virtlet。

- Virtlet 似乎已经被放弃了，在调研时，最后一次提交是 4 年前。
- 而 Kubevirt 具有良好的文档和定期更新，在调研时，最后一次提交就在几个小时前。所以，选择很明显！

### 演示

在查看演示之前，您需要根据[此指南](https://kubevirt.io/user-guide/operations/installation/)安装 Kubevirt 和 QEMU 虚拟化程序。

与 vCluster 相比，实际实验环境的安装更加复杂，因为需要考虑用户数据脚本和存储等因素。但是我将省略这些细节，重点关注最重要的方面。在这个演示中，我将使用通用的容器磁盘镜像。

下面的 YAML 是每个实验环境中的三个虚拟机之一的定义，有一个控制平面节点，两个工作节点，用户数据略有不同。

1. 包含向 ubuntu 用户添加自定义 SSH 密钥的用户数据的 Kubevirt 虚拟机定义:

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    kubevirt.io/vm: myvm
  name: controlplane
  namespace: student
spec:
  running: true
  template:
    metadata:
      labels:
        kubevirt.io/vm: myvm
    spec:
      # 详细配置
      volumes:
      - name: datavolumedisk1
        containerDisk:
          image: "quay.io/containerdisks/ubuntu:22.04"
      - name: cloudinitdisk
        cloudInitNoCloud:
          userData: | 
            #!/bin/bash
            echo "ssh-rsa public key" >> /home/ubuntu/.ssh/authorized_keys
```

2. 创建提供对虚拟机的 SSH 访问的服务。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ssh
  namespace: student
spec:
  type: NodePort
  ports:
  - port: 27017
    targetPort: 22
  selector:
    kubevirt.io/vm: myvm
```

3. 使用自定义 SSH 密钥直接 SSH 访问:

```
$ ssh -i ~/.ssh/student ubuntu@$HOST_PUBLIC_IP -p <NODE_PORT> 
...
ubuntu@controlplane:~$ ls /
# 列出根目录
```

### 工作原理

KubeVirt 虚拟机是一种允许在 Kubernetes 生态系统中运行虚拟化实例的工具。从本质上讲，KubeVirt 虚拟机是一个 Pod，与 QEMU 虚拟机实例紧密耦合。

Kubevirt 有几个组件，但我将重点介绍与我的用例相关的两个重要组件:VirtualMachine 和 VirtualMachineInstance。这两个组件都作为自定义资源定义(CRD)部署到主机 Kubernetes 集群中。

* `VirtualMachineInstance`：由 `VirtualMachine` 组件创建，直接负责 QEMU 虚拟机实例。它是 Kubevirt 的临时部分，当虚拟机被删除时也会被删除。通常通过 `VirtualMachine` CRD 或 `VirtualMachineInstanceReplicaSet` CRD 创建，一般不会单独创建。
* `VirtualMachine`：通过提供停止、启动以及存储虚拟机数据和状态的功能，扩展了 VirtualMachineInstance 的功能。

当新的 `VirtualMachine` 定义被添加到 Kubernetes API 时，Kubevirt 执行以下步骤：

1. `virt-handler` DaemonSet Pod 生成一个 `virt-launcher` Pod。
2. `virt-launcher` 创建一个 `VirtualMachineInstance` 对象。
3. `virt-launcher` 使用来自 `VirtualMachine` 定义的转换定义查询 libvirtd API。
4. libvirtd 启动 QEMU 虚拟机。
5. `VirtualMachine` 组件的任何更新都反映在 QEMU 虚拟机实例上

更多详细信息请访问 [Kubevirt 官网](https://github.com/kubevirt/kubevirt/blob/main/docs/components.md)。

### 容器磁盘与持久存储卷(PVC)

您可以在 PVC 或容器镜像磁盘上运行 Kubevirt 实例，这些镜像是作为容器安装的整个操作系统的快照。

最初，我尝试使用 PVC，但操作很复杂。我必须创建一个包含所有 Kubernetes 组件的通用 “金” PVC，跨命名空间克隆它需要约 3 分钟。其他平台的克隆可以实现瞬时完成！

因此我尝试使用容器磁盘镜像。一旦这些镜像被拉取到我的 Kubernetes集群上，初始化新环境的速度会更快，大概需要 90 秒左右。

尽管有所改进，时间仍然较长。为进一步优化，我创建了一组预置就绪的租户环境缓存。这将初始化环境的时间缩短到不到30秒，达到可接受的程度。但我仍计划在未来进一步加快速度。

> 缓存由运行在主机集群的预置就绪环境数据库组成。学生启动实验时，相应的就绪环境会从数据库中删除并分配给学生。缓存使用定时任务定期进行补充。

### Kubevirt 的资源消耗

为优化实验节点的资源管理，我将每个节点的 CPU 上限从100m 提高到1000m。这一调优带来更快的启动和响应。

内存方面，控制平面分配 1.5G，每个节点分配 1G，每个 Kubevirt 虚拟机实例会额外消耗 100MB 内部容器。每个实验环境消耗约 3.5-4G 的内存和 3 个 CPU 核。在 64G 机器上，可以同时运行约 12 个并行实验环境，同时考虑其他组件和虚拟机上没有挖矿程序。

### 网络

网络安全主要通过限制性的网络策略来管理。这些策略可以有效防止访问其他学生环境和其他 Kubernetes 组件。仅允许三个 Kubernetes 组件间相互通信，学生可以通过 SSH 或 kubeconfig 直接与控制平面通信。然后，再从控制平面节点跳转至 node1 或 node2。

![网络拓扑示意图](https://miro.medium.com/v2/resize:fit:720/format:webp/0*OYDYd2QzkBmCcBAx.png)

*学生视角的网络拓扑*

### 优势

- 在多租户场景下，虚拟化是安全方面最佳的解决方案。
- 内容就是一切！通过操作系统级访问和使用 Kubeadm 安装 Kubernetes，我可以做任何事。这是平台最关键的方面。

### 劣势

- 与 Kubevirt 一起运行完整的操作系统和 Kubernetes 组件，租户密度较低。
- 作为完整的操作系统，启动时间较慢。
- 没有同步工具，我得自己编写!
- 我不得不使用裸机服务器托管实验环境，因为许多公有云不允许嵌套虚拟化，即使允许也很昂贵！

## 租户 Kubernetes 版本

操作系统为 Ubuntu 22.04。而 Kubernetes 版本，我选择在租户环境上使用 Kubeadm 安装 Kubernetes。最初，我计划使用 k3s 或其变体，但我意识到，如果故意造成 k3s 故障，k3s 二进制文件就直接无法启动。因此，调试 k3s 可能需要找到正确的命令，这与我想要创建的内容的重点不符。

我的意图是通过故意损坏各种层级，从操作系统到 Kubernetes 的各个组件，来教授 Kubernetes 的工作原理。Kubeadm 版本是我能想到的唯一一个可以实现我的愿景的选择。

## 总结

总的来说，我的决定是基于我可以为学生提供的内容，而不考虑所使用技术的缺点。尽管 Kubevirt 在资源消耗等方面可能不够完美，但我可以通过每月分配略高一些的预算来缓解。我可以在 Hetzner 拍卖中轻松租用大型裸机服务器，每个月不到 50 欧，提供足够的内存和计算能力。我最终认为，Kubevirt 可能有一些劣势，但它可以提供更加灵活的学习内容，同时通过虚拟化提供更高的安全性。

## 挑战

我最大的挑战一直是，现在也是，平时对各种技术有所了解，但在有效集成应用方面艰难前行。我尝试了解熟悉的技术，遇到障碍，然后转向其他技术，浪费了大量时间。虽然目前一切都运行良好，但我相信仍有很大的改进空间。

> 例如，在放弃 vCluster 后， 我尝试使用 Packer 为 Kubevirt 构建实验环境的金镜像。然而，我后来也放弃了 Packer，因为我已经使用了 Ansible 初始化，不需要再添加新的工具。

当前，我正在根据学生反馈和待办事项的 Backlog，持续改进基础架构。然而，进度缓慢，因为我同时需处理内容、用户体验、Slack机器人、营销、安全等各种不同任务，时常在它们之间切换。我的任务队列中积压了近 70 项任务，这已经成为一个大型的业余项目，我还要兼顾全职工作。

我现在意识到，Slack 可能不是构建社区的理想工具。它更适合团队协作，并且免费账户在 API 调用上有限制。此外，Slack 的价格是基于用户人数，考虑到我 Slack 工作区中不断增长的学生群体，如果我想访问只在付费账户可用的 API，成本会很高。

## 未来计划

* 当实验环境创建时会创建 NodePort，这会在所有待分配的租户主机集群上打开多个 NodePort，这引发了安全风险，因为攻击者可能利用租户环境，这会对真正想学习的用户产生负面影响。
* 可以为每个租户设置网络带宽限制，作为额外的防护措施。[这里](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#support-traffic-shaping)介绍了可用于此目的的机制。
* 根据我的使用案例创建自定义 syncer。这可以是一个在每个租户命名空间内部署的应用，用于监控租户环境中的新服务或入口对象，并复制到主机集群上。
* 例如，学生创建 NodePort 服务，通过我的 syncer 复制到主机集群。这可能无法完全按我设想的方式工作，但我会试一试。
* 学生创建 NodePort 服务，通过我的 syncer 复制到主机集群。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*jFlQCQJaGR2fvdFX.png)

*通过我的 syncer 同步学生创建的 NodePort 服务到宿主集群*

* 许多实验环境并不需要三个节点，大多数只需要一个节点。因此，拥有动态环境会更好。一种方法是维护一个待加入控制平面节点的缓存池，根据请求进行分配。我之前试过这种方法，但由于平台还不够成熟而失败。当资源变得紧缺时我会重新评估这一想法。

目前，缓存的实验环境只支持一个 Kubernetes 版本，不能用于其他版本。这意味着提供所有学习内容需要20到30秒，而沙箱是 1.5 分钟。我将会缓存更多的版本，加速沙箱的初始化速度。
