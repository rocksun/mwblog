<!--
title: Kubernetes最简安装方式对比
cover: ./cover.jpg
-->

释放Kubernetes的力量：明智地选择你的发行版！

> 译自 [The Easiest Kubernetes Installations Ever: Unveiling Distros Side by Side](https://rebelion.la/the-easiest-kubernetes-installations-ever)。作者 La Rebelion Labs 。

踏上穿越 Kubernetes 宇宙的征程？准备好探索 `K0s`、`K3s`、`microk8s` 和 `minikube` 的多样风景吧 - 每个都有其独特的魅力和能力。

没有特定的顺序或偏好，只是按照 "大小" 的名义排列，至少在发行版的名称中是这样，从最小到最大：

- K0s，“零摩擦 Kubernetes” - [首次发布](https://github.com/k0sproject/k0s#status)于2020年11月。
- K3s，“轻量级 Kubernetes” - [官方发布](https://www.suse.com/c/rancher_blog/introducing-k3s-the-lightweight-kubernetes-distribution-built-for-the-edge/)日期为2019年2月26日。
- microk8s，“极简生产 Kubernetes” - Canonical 在2012018年12月[发布了 MicroK8s](https://ubuntu.com/blog/microk8s-in-the-wild)。
- Minikube，“单节点 Kubernetes” - [首次发布](https://github.com/kubernetes/minikube/releases/tag/v0.7.0)于2016年7月26日，未被标记为预发布版本的是 v0.7.0。

从上面可以看出哪个是最古老的，哪个是最新的。但是一个令人燃烧的问题仍然存在 - 哪个才是王者？

让我们解读每一个背后的智慧：

- `Minikube` 先发制人，长时间以来在本地环境和 PoC 中赢得开发者的青睐。
- `K3s` 和 `microk8s` 加入了这场战斗，为争夺最佳的 "物联网或边缘计算发行版" 的称号而激烈竞争。它们轻巧的特性和简单的安装使它们成为领跑者。
- 还有一位新来者 - `K0s` 。一个改变游戏规则的人，具有其独特的功能：一个控制平面，能够在不同的现有服务器或新的虚拟机上仅通过 SSH 密钥添加工作节点！这就是未来吗？
    - 在这个播客的第29分钟查看：[与Mirantis的Jussi Nummelin一起探索K0s](https://www.heavybit.com/library/podcasts/the-kubelist-podcast/ep-38-exploring-k0s-with-jussi-nummelin-of-mirantis)

## 介绍

有多种安装这些发行版的方法，我将使用 `multipass` ，因为这是开始并在我的笔记本上运行多个虚拟机的最简单方法。我将使用相同的虚拟机配置来安装所有发行版，这样我就可以将它们并排进行比较。

### 我是怎么到这里的？

将近4年前（2019年第四季度），当我开始学习 Kubernetes 时，我不得不在一个[无网络访问的环境](https://en.wikipedia.org/wiki/Air_gap_(networking))（RHEL 7.9）上安装了几个 Vanilla Kubernetes 集群。在这种环境中，您无法访问互联网，因此必须从具有互联网访问权限的机器上下载所有二进制文件和镜像，然后将它们复制到无网络访问的环境中，这是繁琐且容易出错的过程。一些同事和其他供应商的顾问尝试过安装 Kubernetes，但他们失败了，我不得不多次向他们解释如何操作，甚至我创建了一个内部Wiki页面提供指导，但他们仍然失败了。因此，将近2年后，我不得不创建一些脚本来自动化这个过程，并决定分享这些知识，创建一个指南和一个视频，展示如何[在Ubuntu上安装（Vanilla）Kubernetes 集群](https://go.rebelion.la/install-kubernetes)。

现在，这些流行的发行版都宣传易于安装和简单，我将指导您完成每个发行版的安装过程，并与您分享我用于自动化此过程的脚本，我将对所有发行版使用相同的虚拟机配置，以便可以并排比较它们。准备好了吗？我们开始吧！

### 布景设定：Multipass 和实验环境

在我们深入安装之前，让我们用 [Multipass](https://multipass.run/) 来设置布景 - 这是一个轻量级的 Linux、Windows 和 macOS 虚拟机管理器。通过 Multipass，我们将以一个命令释放 Ubuntu 环境的力量。准备好了比较这些发行版了吗？让我们开始吧！

查看官方参考文档以了解如何[安装 Multipass](https://microk8s.io/docs/install-multipass)；支持 Linux、macOS 和 Windows。

**对于 `multipass` 而不是 `ssh` 的调整**

因为我使用默认的 `cloud-init` 文件，实例是用默认用户 ubuntu 创建的，但是此用户不允许通过 SSH 连接，因为没有定义密码，您必须手动执行此步骤，而我更喜欢不过于复杂化这个过程，所以要么：

我需要使用 `multipass shell` 命令连接到实例并从实例终端执行命令；或者我可以并且我更喜欢使用 `multipass exec` 命令从本地执行实例中的命令，这类似于 `docker exec` 和 `kubectl exec` 命令，但适用于虚拟机，我将使用它而不是 `ssh $ssh_user@$host 'bash -s <SCRIPT_HERE>'` 来执行我的脚本。

> 如果不使用 multipass，您可以使用上面的 ssh 命令。

鼓励您检查下面每个发行版的步骤，了解后您可以查看并下载[安装 Kubernetes 发行版](https://rebelion.la/the-easiest-kubernetes-installations-ever#references-and-resources)的脚本。

**Multipass 参考：**

- [为默认 ubuntu 用户设置密码](https://multipass.run/docs/set-up-a-graphical-interface)。
- [构建 Multipass 镜像](https://multipass.run/docs/building-multipass-images-with-packer)。
- [cloudinit](https://cloudinit.readthedocs.io/en/latest/)

## 实验环境

### 系统要求

下表是根据官方文档为每个发行版的最低要求的表格。

| 发行版 | CPU | RAM | 硬盘 |
| --- | --- | --- | --- |
| K0s | 1 | 控制平面 1 GB，工作节点 0.5 GB | 控制平面 ~0.5 GB，工作节点 ~1.3 GB |
| K3s | 1 | 512 MB | 5 |
| microk8s | 1 | 540MB | 20G |
| minikube | 2 | 2G | 20G |

毫无疑问，minikube 是最占资源的发行版，但它是最古老的，因此可以理解，也许它从未被设计用于物联网或边缘环境，但对于开发者在他们的个人电脑、笔记本电脑和 PoCs 中来说，这是一个很好的选择。

有 Canonical 公司的朋友们做的这份[要求比较](https://microk8s.io/compare)，但它与官方文档不匹配，因此我将质疑其中的一些要求，并将使用相同的虚拟机配置，只有 **1 个 CPU**、**1GB 的 RAM** 和 **5GB 的硬盘空间**；挑战接受！ 🤓

请记住，选择最佳工具取决于您特定的需求和实验环境中的资源。

## K0s

[K0s](https://k0sproject.io/) 是一种"零摩擦 Kubernetes"发行版，旨在在任何基础设施上运行：公有云、私有云和无网络访问的环境。它是一个单一的二进制文件，旨在尽可能简单易安装和升级。

### 安装

#### 控制平面

```bash
# download the K0s binary
curl -sSLf https://get.k0s.sh | sudo sh
# install K0s
k0s install controller --enable-worker
systemctl daemon-reload
k0s start
# check the status
k0s status
k0s kubectl get nodes
watch 'k0s kubectl get pod --all-namespaces'
k0s kubectl get nodes
# create a token to join workers to the cluster
k0s token create --role=worker > token-file

```

#### 工作节点

在每个工作节点上运行以下命令：

```bash
# download the K0s binary
curl -sSLf https://get.k0s.sh | sudo sh
# install K0s
k0s install worker --token-file token-file
systemctl daemon-reload
k0s start
# check the status
k0s status

```

### K0s 额外参考

- [需求](https://docs.k0sproject.io/v1.28.4+k0s.0/system-requirements/)
- [使用 Ansible Playbook 创建 K0s 集群](https://docs.k0sproject.io/v1.28.4+k0s.0/examples/ansible-playbook/?h=control+plane#create-the-cluster) - 作者表示，基于 K3s Ansible Playbook。

## K3s

[K3s](https://k3s.io/) 是一种轻量级的 Kubernetes 发行版，旨在在任何基础设施上运行：公有云、私有云和无网络访问的环境。它是一个单一的二进制文件，旨在尽可能简单易安装和升级。它是一个与上游 Kubernetes 没有破坏性更改的完全兼容的 Kubernetes 发行版。

### 安装

#### 控制平面

```bash
curl -sfL https://get.k3s.io | sh -
# Check for Ready node, takes ~30 seconds
k3s kubectl get nodes
# Check for Ready pod, takes ~60 seconds
watch 'k3s kubectl get pod --all-namespaces'
# get the token to join workers to the cluster
cat /var/lib/rancher/k3s/server/node-token

```

在 [K3s 架构](https://docs.k3s.io/architecture)中，`主节点`被称为`服务器节点`，`工作节点`被称为`代理节点`。服务器和代理被合并为一个单一的二进制文件，称为 k3s。服务器使用 --server 参数启动，代理使用 --agent 参数启动。服务器和代理可以合并为单一节点，也可以在单独的节点上运行。

加入节点：`NODE_TOKEN` 来自服务器上的 `/var/lib/rancher/k3s/server/node-token`。

#### 工作节点

要安装代理节点，请在每个节点上运行以下命令：

```bash
curl -sfL https://get.k3s.io | K3S_URL=https://k3s1-rebelion:6443 K3S_TOKEN=mynodetoken INSTALL_K3S_EXEC="agent" sh -
```

注（来自官方文档）：

- 将生成一个 kubeconfig 文件到 `/etc/rancher/k3s/k3s.yaml`，并且由 K3s 安装的 `kubectl` 将自动使用它。

### 故障排除

**代理节点无法加入集群**

似乎默认情况下，代理节点试图连接到负载均衡器，生成一个超时错误，并且无法连接到端口 `6444`，但如果您正在使用单个服务器节点，则不需要负载均衡器，因此您需要使用 `agent` 和 `--disable-apiserver-lb` 标志启动代理节点，如下所示：

```bash
sudo k3s agent --server https://k3s1-rebelion:6443 -t $token --disable-apiserver-lb > /dev/null 2>&1 &
```

**服务器节点卡住**

我遇到的另一个问题是代理节点无法连接到服务器节点，因此我不得不增加服务器节点的资源，然后代理节点才能连接到服务器节点。（仅增加内存，不包括 CPU 或磁盘空间）

```bash
multipass stop k3s1-rebelion
multipass set local.k3s1-rebelion.memory=2G
#multipass set local.k3s1-rebelion.cpus=2
#multipass set local.k3s1-rebelion.disk=10G
multipass start k3s1-rebelion
```

参考：

- 增加资源 [multipass.run/docs/modify-an-instance](https://multipass.run/docs/modify-an-instance)
- [github.com/k3s-io/k3s/issues/4839](https://github.com/k3s-io/k3s/issues/4839) - 这不是我的情况，但似乎对一些人有帮助，所以我在这里包含了它，以防万一。

### K3s 额外参考

- [要求](https://docs.k3s.io/installation/requirements?os=debian)
- [使用 Ansible 通过 K3s 构建 Kubernetes 集群](https://github.com/k3s-io/k3s-ansible)

## microk8s

多种[安装 microk8s](https://microk8s.io/docs/install-alternatives) 的方法。

[MicroK8s](https://microk8s.io/docs/getting-started) 安装默认使用 Calico 作为 CNI，使用 dqlite 作为数据存储，并使用 Kubernetes 服务的默认一套具有观点的默认参数。MicroK8s 是一个符合上游 Kubernetes 部署的简化设计，专为开发人员体验而优化。

"MicroK8s 在至少 540MB 的内存中运行，但为了适应工作负载，我们建议系统至少具有 20G 的磁盘空间和 4G 的内存。"

### 安装

#### 控制平面

```bash
#install snapd
apt update
apt install snapd
#install microk8s
snap install microk8s --classic
# one step further, getting the token to join the cluster

# Run the command and store the output
output=$(microk8s add-node) 
# Extract the second line
join_command=$(echo "$output" | sed -n '2p')
echo $join_command --worker
```

#### 工作节点

```bash
#install snapd
apt update
apt install snapd
#install microk8s
snap install microk8s --classic
#join the cluster
microk8s join <BASED_ON_OUTPUT_IN_CONTROL_PLANE_SERVER> --worker

microk8s kubectl get nodes
```

要将新节点添加到集群，您需要在控制平面服务器上运行 `microk8s add-node` 命令，然后在工作节点上运行该命令的输出，并且必须对要添加到集群的每个工作节点执行此操作，因为 `microk8s add-node` 命令的输出对于每个工作节点都是不同的。

在 microk8s 文档中我注意到的一件事，而在其他发行版中没有看到的是，您可以轻松地从集群中删除节点，这对于测试目的非常有用，当然，在其他发行版中也可以做到，但您必须手动执行，在 microk8s 中，您可以使用单个命令完成：

```bash
microk8s leave
```

#### MicroK8s 额外参考

- [删除节点](https://microk8s.io/docs/clustering#removing-a-node-2)
- [RBAC](https://microk8s.io/docs/multi-user)
- [MicroK8s 实战](https://ubuntu.com/blog/microk8s-in-the-wild)

## minikube

[minikube](https://minikube.sigs.k8s.io/docs/start/) 是一个使在本地运行 Kubernetes 变得容易的工具。Minikube 在您的笔记本电脑上的虚拟机中运行单节点 Kubernetes 集群，供想要尝试 Kubernetes 或在日常开发中使用的用户使用。

### 安装

#### 控制平面

```bash
# install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
# start minikube
minikube start
# check the status
minikube status
alias kubectl="minikube kubectl --"
kubectl cluster-info

# check the nodes
kubectl get nodes
# check the pods
watch 'kubectl get pod --all-namespaces'
```

您需要安装一个驱动程序，docker 是首选的驱动程序，因此您需要首先安装 docker，然后 `minikube` 将使用它作为驱动程序。

如果您考虑使用干净的虚拟机，那么 `minikube` 的安装过程是所有发行版中最复杂的，但仍然很容易安装，而且它是最古老的一个，因此可以理解。

非常棒的一点是，我正在使用 `multipass`，因此拥有 `minikube` 实例的最简单方式是创建预先安装了 `minikube` 的 `multipass` 虚拟机，仅此而已！

非常糟糕的一部分是，`minikube` 虚拟机映像至少需要 2 个 CPU、4GB RAM 和 40GB 磁盘空间，与其他发行版相比巨大！

```bash
# create the VM with minikube pre-installed
multipass launch --name minikube-rebelion -c 2 -m 4G -d 40G minikube
# check the status
multipass info minikube-rebelion
```

Minikube 必须使用至少 2 个 CPU 创建，否则将出现此错误：

`launch failed: Requested Number of CPUs is less than Blueprint minimum of 2`

至少 4GB RAM，否则将出现此错误：

`launch failed: Requested Memory size is less than Blueprint minimum of 4G`

并且至少 40GB 的磁盘空间，否则将出现此错误：

`launch failed: Requested Disk space is less than Blueprint minimum of 40G`

#### Worker Nodes

⚠️ 尽管 Minikube 确实有一个 `--nodes` 标志，允许您指定节点的数量，但这些节点仍然都在同一台服务器/虚拟机内运行，而不是在单独的虚拟机中，这与我们在此实验中要测试的不同。

如果您在实验室中需要一个多节点的 Kubernetes 集群，那么其他发行版绝对是更好的选择，或者使用 Vanilla 安装了完整功能的 Kubernetes，具有多个虚拟机。

#### Minikube 额外参考

- [Requirements](https://minikube.sigs.k8s.io/docs/start/#what-youll-need)
- [Minikube 在实际应用中](https://minikube.sigs.k8s.io/docs/tutorials/kubernetes_101/)
- [docs.docker.com/engine/install/ubuntu](docs.docker.com/engine/install/ubuntu)
- [minikube.sigs.k8s.io/docs/drivers/docker](minikube.sigs.k8s.io/docs/drivers/docker)
- [minikube.sigs.k8s.io/docs/drivers](minikube.sigs.k8s.io/docs/drivers)

## 休息一下：比较各发行版的安装

基于之前的经验，我原本期望在安装这些发行版时会遇到一些问题，但令我惊讶的是它们都在不到 5 分钟的时间内顺利安装，而且都没有出现任何问题。我的结论是它们都很容易安装，但我会把桂冠颁给 K3s，因为它的过程最简单，需要遵循的步骤更少，第二名是 microk8s，因为它也很容易安装，但需要遵循更多步骤，第三名是 K0s，因为它需要遵循更多步骤，相对于其他两个来说不太容易安装。

从我的角度来看，这些发行版的安装并不是问题，问题在于 Kubernetes 生态系统的复杂性，以及缺乏良好的开发者体验，但这是另一篇文章的话题。

## 离线安装

正如我在介绍中所解释的，我开始产生内容不仅仅是因为 Kubernetes 本身的复杂性，还因为在无网络环境中安装的额外复杂性；在那些日子里，没有工具可以帮助你完成这种类型的安装，所以我不得不创建脚本来自动化离线安装过程，如今，所有这些发行版都有一种在无网络环境中安装它们的方式：

- [K0s 的离线安装](https://docs.k0sproject.io/v1.28.4+k0s.0/airgap-install/)
- [K3s 的离线安装](https://docs.k3s.io/installation/airgap)
- [MicroK8s 的离线安装](https://microk8s.io/docs/install-offline)
- [Minikube 的离线安装](https://minikube.sigs.k8s.io/docs/handbook/offline/)

## K1s 和 K1sT

[K1s](http://k1ss.me/k1s)，一个无服务器 Kubernetes（**不是发行版**本身，但是是我的心血之作，所以我包括在内。你也会喜欢它的！）。这个 Kubernetes 集群是一个完全兼容的 Kubernetes API，允许你运行任何 Kubernetes API 调用，以体验 kubectl 命令行工具或客户端 API 调用，它是新手学习 Kubernetes 的模拟器，也是经验丰富的用户测试其脚本和工具的工具，与上游 Kubernetes 没有破坏性更改。

[K1sT](http://k1ss.me/k1st)，面向开发者的 Kubernetes CLI，适用于所有人。这是一个使与 Kubernetes 集群交互并更高效、更有生产力地管理工作负载变得容易的工具。

试一试它们，告诉我你的想法！这还是一个正在进行中的项目（为早期采用者提供的 alpha 版本），但已经可以使用，并且是免费的！

我正在准备一个视频，向你展示如何使用它们，以及如何连接到所有的 Kubernetes 集群而无需麻烦，以之前的发行版为例，所以[请关注](https://go.rebelion.la/subscribe)！

## 比较各发行版的资源使用

```bash
multipass info --all | grep -E "Name|Load|CPU|Mem|Disk"
# or formatted as a table (markdown)
echo -e "| Name | CPU | Load | Disk | Memory |\n| --- | --- | --- | --- | --- |"
multipass info --all | grep -E "Name|Load|CPU|Mem|Disk" | awk -F: '{split($0,a,":"); printf("|%-10s ", a[2])} END {print "|\n"}' | column -t
# just one VM as an example
multipass info primary | grep -E "Name|Load|CPU|Mem|Disk" | awk -F: '{split($0,a,":"); printf("|%-10s ", a[2])} END {print "|\n"}' | column -t
# comma separated format for easy copy/paste in a spreadsheet
multipass info primary | grep -E "Name|Load|CPU|Mem|Disk" | awk -F: '{split($0,a,":"); printf("%-10s, ", a[2])} END {print "\n"}' | column -t

```

multipass info 命令[文档在此](https://multipass.run/docs/info-command)。

### 逐项对比

| Name                 | CPU | Load               | Disk                  | Memory                         |
|----------------------|-----|--------------------|-----------------------|--------------------------------|
| primary              | 1   | 0.00 0.00 0.00     | 1.8GiB out of 4.7GiB  | 185.3MiB out of 892.2MiB      |
| k0s1-rebelion        | 1   | 0.58 0.83 1.27     | 3.3GiB out of 4.7GiB  | 744.7MiB out of 892.2MiB      |
| k0s2-rebelion        | 1   | 0.00 0.00 0.00     | 2.6GiB out of 4.7GiB  | 321.9MiB out of 892.2MiB      |
| k0s3-rebelion        | 1   | 0.01 0.04 0.01     | 2.6GiB out of 4.7GiB  | 324.8MiB out of 892.2MiB      |
| k3s1-rebelion        | 1   | 0.02 0.06 0.02     | 2.2GiB out of 4.7GiB  | 739.4MiB out of 1.9GiB        |
| k3s2-rebelion        | 1   | 0.00 0.00 0.00     | 2.2GiB out of 4.7GiB  | 275.6MiB out of 892.2MiB      |
| k3s3-rebelion        | 1   | 0.01 0.00 0.00     | 2.1GiB out of 4.7GiB  | 300.5MiB out of 892.2MiB      |
| microk8s1-rebelion   | 1   | 0.39 0.22 0.20     | 3.5GiB out of 4.7GiB  | 809.1MiB out of 1.9GiB        |
| microk8s2-rebelion   | 1   | 0.00 0.02 0.03     | 3.3GiB out of 4.7GiB  | 326.7MiB out of 892.2MiB      |
| microk8s3-rebelion   | 1   | 0.00 0.00 0.00     | 3.3GiB out of 4.7GiB  | 324.3MiB out of 892.2MiB      |
| minikube-rebelion    | 2   | 0.32 0.39 0.38     | 8.8GiB out of 38.6GiB | 1.5GiB out of 3.8GiB          |


*Kubernetes distros resource usage.*

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705958749097/fbefc750-57b2-48fb-9b48-e1fb938501d6.png?auto=compress,format&format=webp)

*Kubernetes distros memory usage.*

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1705958789529/c43a366a-fdaa-491d-bce7-a53bbad95615.png?auto=compress,format&format=webp)

## 观测

- Minikube 是资源消耗最大的发行版，但它是最古老的，所以可以理解，也许它从未打算用于**物联网或边缘环境**，但对于开发者在其个人计算机、笔记本电脑和 PoCs 中，它是一个很好的选择。
- 关于所需的资源，其他发行版只需 1 个 CPU、1GB 的 RAM 和 5GB 的磁盘空间即可顺利运行。
- 对于 K3s 和 microk8s，我不得不增加主节点的内存，因为代理节点无法连接到服务器节点，但那是我唯一遇到的问题，而且是间歇性的，所以我不确定它是一个真正的问题还是只是我的笔记本由于可用资源和后台运行的其他进程（打开了许多浏览器和标签，以及其他正在运行的应用程序）而出现的小问题。
- 基于这个实验，K0s 是最容易安装的；K3s 是最难安装的，我不确定我在代理/工作节点上做的最终安装是否正确，但它确实有效，如果你想更深入地了解，你可能需要更深入地调查并调整我上面展示给你的安装过程。
- 我会让你自己去比较这些发行版的性能，我不会去做，但我相信你能做并与我和社区分享你的结果。

## Bonus - 自动化安装

你可以使用官方的 [K3s](https://github.com/k3s-io/k3s-ansible) 和 [K0s](https://docs.k0sproject.io/v1.28.4+k0s.0/examples/ansible-playbook) Ansible Playbook，也可以使用我为你创建的以下脚本来安装这些发行版，我将使用这些脚本来消除安装 Ansible、[外部依赖项](https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.3/html/red_hat_ansible_automation_platform_planning_guide/platform-system-requirements)（Ansible、Python 和外部库）以及可能需要安装这些发行版所需的额外资源（CPU、RAM 和磁盘空间）中的任何额外复杂性。

### 启动 Multipass 虚拟机，以防需要

```bash
# bash shell (Linux, macOS, WSL)
# A single command line to launch 3 VMs, with the names of the VMs for our lab (k0s1, k0s2, k0s3, k3s1, k3s2, k3s3, microk8s1, microk8s2, microk8s3, minikube)
for i in {1..3}; do multipass launch --name k0s${i}-rebelion -c 1 -m 1G -d 5G; multipass launch --name k3s${i}-rebelion -c 1 -m 1G -d 5G; multipass launch --name microk8s${i}-rebelion -c 1 -m 1G -d 5G; done
# minikube doesn't support multiple VMs, so we are going to launch only one VM
multipass launch --name minikube-rebelion -c 1 -m 1G -d 5G

# PowerShell (Windows), same as above 3 VMs per distro
for ($i=1; $i -le 3; $i++) { multipass launch --name k0s$i-rebelion -c 1 -m 1G -d 5G; multipass launch --name k3s$i-rebelion -c 1 -m 1G -d 5G; multipass launch --name microk8s$i-rebelion -c 1 -m 1G -d 5G; }
# minikube doesn't support multiple VMs, so we are going to launch only one VM
multipass launch --name minikube-rebelion -c 1 -m 1G -d 5G
# command prompt (Windows)
for /L %i in (1,1,3) do multipass launch --name k0s%i-rebelion -c 1 -m 1G -d 5G & multipass launch --name k3s%i-rebelion -c 1 -m 1G -d 5G & multipass launch --name microk8s%i-rebelion -c 1 -m 1G -d 5G
# minikube doesn't support multiple VMs, so we are going to launch only one VM
multipass launch --name minikube-rebelion -c 1 -m 1G -d 5G
```

愉快编码，享受生活，加油 Rebels！

## 参考和资源

- 用于[自动化 Kubernetes 发行版安装](https://go.rebelion.la/kubernetes-distros-installation)的脚本。
- La Rebelion [博客](https://rebelion.la/)。
- [完整视频](https://go.rebelion.la/kubernetes-distros-installation-video)
- [订阅 "La Rebelion" 社区](https://go.rebelion.la/subscribe)，获取更多技术见解、教程和突破。
- [K1s 终端](https://go.rebelion.la/k1st)简化 Kubernetes 和云原生操作。

## 让我们一起创新！