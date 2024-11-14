[< 博客首页](/blog)
# Kubernetes 与菲律宾停电 - 关于在 Tailscale 上设置 k0s
![Kubernetes 停电编排](https://a.storyblok.com/f/153547/1080x608/95e9fc915f/kubernetes-power-outage-orchestration.jpg/m/)
在菲律宾构建可靠的 IT 系统面临着独特的挑战，例如频繁的停电和不可靠的互联网连接。为了有效地解决这些问题，我们的团队实施了一个弹性设置，确保最终用户能够不间断地访问关键服务。

本指南将引导您完成使用 Tailscale 和 [k0s](https://k0sproject.io/) 的类似设置，您可以在您的家庭实验室环境中复制该设置。如果您只对设置感兴趣，请随时跳到第二部分。

## I. 挑战
为了提供一些背景信息，我们的团队为各种客户管理多个项目，将大多数服务托管在他们附近的本地服务器上。然而，我们面临的一个重大问题是，由于当地变电站的维护或紧急情况，经常发生停电。这些中断几乎每周都会发生，有时持续 8-12 小时，有效地使我们的服务在整个工作日内都无法使用。

## *旁注：为什么不托管在云端？
嗯，这有点复杂。一些服务在云端运行良好（所以我们已经将它们放在那里），但其他服务有其独特的需求。例如，让我们仔细看看我们两个主要项目：[Impactville](https://impactville.com/) 和 [Lupain.AI](https://www.lupain.ai/landing/new)。

Impactville 处理来自组织的私人数据，这些组织出于隐私考虑不愿将其存储在云端。同时，Lupain.AI 处理来自地方政府部门的敏感土地数据，需要安全和本地存储。

从成本角度来看，Lupain.AI 涉及对卫星数据的密集处理。使用云资源可能会增加成本，尤其是在美元兑菲律宾比索汇率不断上涨的情况下。对于我们来说，使用自托管的 GPU 节点集群来管理这些任务更具成本效益。

## 回到挑战
总结一下我们的场景：

我们对分布在全国各地的节点拥有完全的控制权和所有权。

我们的目标是实现容错服务，并将停机时间降至最低（理想情况下少于 1 分钟，5-10 分钟是可以接受的）。

数据冗余和高可用性是基本要求。

鉴于这些需求，最可行的解决方案是设置一个编排器，该编排器能够检测停机时间，自动重新安排服务，并将它们分布到节点集群中。

在此设置中，如果一台服务器发生停电，服务将暂时转移到其他服务器，直到正常运行恢复。

因此，采用 Kubernetes 对我们来说是一个显而易见的选择。[Kubernetes](https://kubernetes.io/) 是一个开源系统，专门设计用于自动化容器化应用程序的部署、扩展和管理。

本指南将引导您完成使用 [k0s](https://k0sproject.io/) 和 [Tailscale](https://tailscale.com/) 部署您自己的 Kubernetes 集群的基本设置。

**免责声明：**此处描述的设置是简化的，可能与我们的生产设置不同。我们的生产环境解决了各种复杂性，例如 ISP DNS 问题 [1][2]、速率限制、与 Starlink 连接的节点的与天气相关的挑战、服务器安全加固、冗余数据的加密以及集群入口。这些主题需要详细讨论，要么保留在以后的文章中，要么作为内部知识进行处理。
但是，对于小型家庭实验室设置，本指南应该提供足够的指导。

## II. Kubernetes 设置
在本指南中，我们将使用 k0s 设置一个 Kubernetes 集群，并通过 Tailscale 连接我们的节点。以下是所涉及技术的概述：

### k0s
k0s 是一个开源 Kubernetes 发行版，旨在简化和通用化。它包含构建 Kubernetes 集群所需的所有必要功能，并且足够轻量级，可以在各种环境中运行，例如云、裸机、边缘和物联网设备。它最小的设置和简单的配置使其非常适合我们的需求。

### Tailscale
虽然可以使用任何 VPN，但 Tailscale 凭借其易于设置、全面的文档和可靠的网络功能而脱颖而出。MagicDNS 简化了 DNS 管理，增加了额外的便利层。

### 分布式存储
对于分布式存储，您可以从各种选项中进行选择。最简单的方法是设置 [NFS](https://en.wikipedia.org/wiki/Network_File_System) 或 [NAS](https://en.wikipedia.org/wiki/Network-attached_storage)，尽管可能需要为高可用性 (HA) 配置它。在我们的设置中，我们选择使用 [SeaweedFS](https://github.com/seaweedfs/seaweedfs)，这是一个分布式存储系统，它提供可扩展性和对大量数据的高效管理。请注意，为 HA 配置 [SeaweedFS](https://github.com/seaweedfs/seaweedfs) 超出了本指南的范围。
### 指令
要开始设置 Kubernetes 集群，请按照以下步骤操作：

#### 1. 手动节点设置
首先，确保 SSH 已安全配置以访问您的节点。验证您是否可以 SSH 访问所有节点，并且它们使用基于密钥的身份验证。在集群设置期间暂时禁用密码身份验证；您可以在以后的 SSH 配置中重新启用它。

#### 2. 通过 VPN 连接它们
接下来，使用 Tailscale 在您的节点之间建立安全连接：

注册 Tailscale 并将您的设备添加到网络中。查看

[https://tailscale.com/](https://tailscale.com/)按照 Tailscale 的说明安装并连接 Tailscale 到您的网络。查看

[https://tailscale.com/kb/1017/install](https://tailscale.com/kb/1017/install)检查

`tailscale0`
是否出现在您的网络接口中（例如，通过`ifconfig`
）。确保您的控制机器（您将在其中运行

`kubectl`
）也连接到 Tailscale 网络。
#### 3. 安装 k0s
要设置您的 Kubernetes 集群，请按照以下步骤操作：

**在您的控制机器上安装 k0s**。首先在您的控制机器上安装 k0s。您可以在 [k0s 安装](https://docs.k0sproject.io/stable/install/) 中找到详细说明。使用以下命令：
```
curl -sSLf https://get.k0s.sh | sudo sh
```
**使用 k0sctl 进行自动化部署：**为了简化跨节点的安装，请使用 k0sctl：
根据您的操作系统安装 k0sctl。参考 [k0sctl 安装](https://github.com/k0sproject/k0sctl#installation)：

```
brew install k0sproject/tap/k0sctl
choco install k0sctl
```
**生成 k0sctl 配置文件：**创建一个 k0sctl 配置文件来定义您的集群设置：
```
k0sctl init > k0sctl.yaml
```
根据需要自定义配置。以下是一个示例配置：

```yaml
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
  name: k0s-cluster
spec:
  hosts:
  - role: controller
    ssh:
      address: 10.0.0.1 # 替换为控制器的 IP 地址
      user: root
      keyPath: ~/.ssh/id_rsa
  - role: worker
    ssh:
      address: 10.0.0.2 # 替换为工作节点的 IP 地址
      user: root
      keyPath: ~/.ssh/id_rsa
```
有关进一步的自定义，请参考 [k0sctl 配置文档](https://docs.k0sproject.io/stable/configuration/)。

**引导集群：**要初始化和部署您的 Kubernetes 集群，请执行以下命令：
`k0sctl apply --config k0sctl.yaml`
k0sctl 将自动在您的网络中指定的机器上安装和部署 k0s，配置 Kubernetes 集群以进行操作。部署后，生成 kubeconfig 文件以使用 kubectl 管理集群：

```
k0sctl kubeconfig > kubeconfig
kubectl get pods --kubeconfig kubeconfig -A
```
**卸载或重置集群：**如果您需要重新配置或删除集群，请使用以下命令：
```
k0sctl reset --config k0sctl.yaml
```
此命令将重置集群配置，允许根据需要进行后续部署或修改。

#### 4. 配置
虽然前面的说明提供了标准设置，但还需要额外的配置才能与 Tailscale 集成并有效地管理私有容器注册表。

##### 连接到 Tailscale 的节点
为了确保 k0sctl 为连接到 Tailscale 的机器正确分配 IP，请在配置中指定正确的网络接口。对于 Tailscale，请使用 `tailscale0`
。以下是一个示例配置片段：

```yaml
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
hosts:
- ssh:
    address: machine-1
    privateInterface: tailscale0
    role: controller
- ssh:
    address: node-2
    privateInterface: tailscale0
    role: worker
```
##### 私有容器注册表
如果您的应用程序的镜像需要额外的隐私，您很可能将容器镜像存储在私有注册表中。为了确保 k0s（特别是 containerd）从正确的注册表中拉取镜像，请按照以下说明操作：

在每个工作节点上创建一个 containerd 的自定义配置文件：

```
sudo nano /etc/k0s/containerd.d registry.toml
```
添加以下内容：

```
[plugins."io.containerd.grpc.v1.cri".registry]
config_path = "/etc/containerd/certs.d"
```
这将指示 containerd 在 `/etc/containerd/certs.d`
中查找主机。

创建一个

`hosts.toml`
文件用于您的注册表域名或 IP
```
sudo nano /etc/containerd/certs.d/<registry-domain or ip>:<registry port>/hosts.toml
```
用以下内容填充它：

```
server = "http://<domain or ip>:<port>"
[host."http://<domain or ip>:<port>"]
skip_verify = true # 如果您的注册表未通过 TLS 配置
```
注意：对于生产环境，请确保 TLS 证书已正确配置。有关其他配置详细信息，请参考 [containerd 文档](https://github.com/containerd/containerd/blob/main/docs/hosts.md)。

配置完成后，k0s 将使用这些设置根据需要从您的注册表中拉取私有镜像

##### 网络
网络配置一直是一个挑战，我们在服务器设置中遇到了各种问题，花费了大量时间和精力进行故障排除。经过数天的艰苦工作，我们发现了以下问题。

对于网络，k0s 支持各种提供商来管理 pod 间网络，正式称为容器网络接口 (CNI)。有关 k0s 网络功能的更多详细信息，您可以参考官方文档 [此处](https://docs.k0sproject.io/stable/networking/)。

默认情况下，k0s 使用 kube-router CNI，以其轻量级和高性能而闻名。但是，我们遇到了特定问题，即节点之间的 pod 间通信失败。关键诊断信息（例如 `nslookup` 无法连接到名称服务器和 `traceroute` 显示星号）促使我们进一步调查。

经过对 iptables 的广泛故障排除，我们确定 kube-router 没有使用正确的接口进行通信——在我们的案例中是 Tailscale。此外，kube-router 目前不支持显式设置网络接口，并且可能在不久的将来不会添加此功能（请参阅 [GitHub 问题 #567](https://github.com/cloudnativelabs/kube-router/issues/567)）。因此，我们决定迁移到另一个 CNI。

k0s 的另一个内置 CNI 选项是 Calico，它提供了更灵活的配置选项，包括网络接口设置。如果您遇到 kube-router 问题并且需要切换到 Calico，您可以在集群引导期间使用以下配置：

```
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
  name: k0s-cluster
spec:
  k0s:
    config:
      spec:
        network:
          provider: calico # <-- use Calico
          calico:
            envVars:
              IP_AUTODETECTION_METHOD: "interface=tailscale0" # <-- use tailscale
            hosts:
            - role: controller
              ssh:
                address: 10.0.0.1 # replace with the controller's IP address
                user: root
                keyPath: ~/.ssh/id_rsa
            - role: worker
              ssh:
                address: 10.0.0.2 # replace with the worker's IP address
                user: root
                keyPath: ~/.ssh/id_rsa
```
重要的是要注意将 Calico 与 Tailscale 集成时的潜在边缘情况，如 [此处](https://github.com/tailscale/tailscale/issues/591) 所述。为了避免冲突，我们建议重新映射 Calico 的 netfilter 数据包。这确保了网络设置中的兼容性和平稳运行。

```
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
  name: k0s-cluster
spec:
  k0s:
    config:
      spec:
        network:
          provider: calico
          calico:
            envVars:
              FELIX_IPTABLESMARKMASK: "0xff00ff00" # <- use mask
              IP_AUTODETECTION_METHOD: "interface=tailscale0"
```
重新部署后，pod 现在可以跨不同节点相互通信！

#### 节点本地负载均衡
节点设置完成后，我们的 Kubernetes 集群现在可以有效地处理节点间通信，即使在断电期间也是如此。但是，我们需要解决一个重要的场景：*如果控制节点出现故障会发生什么？* 没有正常运行的控制节点，就没有协调器来管理 pod 事件，这会导致关键服务的停机。

为了确保持续运行，必须规划控制平面的高可用性。这可以通过在集群中设置多个控制平面节点来实现。

幸运的是，k0s 为此提供了一个内置解决方案，即 [节点本地负载均衡](https://docs.k0sproject.io/stable/nllb/)。调整一小部分配置可以增强我们的设置：

```
apiVersion: k0sctl.k0sproject.io/v1beta1
kind: Cluster
metadata:
  name: k0s-cluster
spec:
  k0s:
    config:
      spec:
        network:
          nodeLocalLoadBalancing:
            enabled: true
            type: EnvoyProxy
```
#### 5. 使用您的 Kubernetes 集群
现在您的 Kubernetes 集群已部署并使用上述步骤配置，最后一步是在本地机器上设置 kubectl（Kubernetes 命令行工具）。此工具允许您有效地管理您的集群。

按照以下步骤完成设置：

**安装 kubectl**: 在本地机器上安装 Kubernetes 命令行工具 kubectl。您可以从官方 Kubernetes 文档下载它，也可以使用 `apt` 或 `brew` 等包管理器。
**配置 kubeconfig**: 集群部署后，将生成的 kubeconfig 文件复制到相应的目录，将其设置为默认配置
```
cp kubeconfig ~/.kube/config
```
此步骤确保 kubectl 使用正确的凭据和配置访问您的 Kubernetes 集群。

**验证设置**: 通过检查集群中 pod 的状态来确认 kubectl 是否已正确配置
`kubectl get pods -A`
此命令将列出所有命名空间 (`-A` 标志) 中的所有 pod，表明您的集群正在运行并已准备好部署应用程序。

配置好 kubectl 后，您现在就可以在 Kubernetes 集群上无缝地管理和编排容器化应用程序！

## 最后的想法
感谢您的阅读！感谢您抽出时间阅读到这里 ❤ 。如果您发现任何部分令人困惑或在复制过程中遇到任何问题，我很乐意提供帮助。只需给我发送电子邮件 ([thepiesaresquared@gmail.com](mailto:thepiesaresquared@gmail.com)) 或在 [@justfizzbuzz](https://twitter.com/justfizzbuzz) 上给我发私信/推文。

我非常享受制作本指南的过程！如果您对更多类似的文章感兴趣，我邀请您订阅此博客，或让我们联系并在 [Twitter/X](https://twitter.com/justfizzbuzz) 上分享我们的文章！

脚注

[1] [https://answers.netlify.com/t/every-netlify-site-i-visit-cant-be-reached-from-the-philippines/49205?page=2](https://answers.netlify.com/t/every-netlify-site-i-visit-cant-be-reached-from-the-philippines/49205?page=2)

[2] [https://www.reddit.com/r/PinoyProgrammer/comments/wo7qcl/any_pldt_dev_here_why_pldt_blocks_netlify/](https://www.reddit.com/r/PinoyProgrammer/comments/wo7qcl/any_pldt_dev_here_why_pldt_blocks_netlify/)

*这篇文章最初发表在作者的 [个人博客](https://justrox.me/kubernetes-vs-philippine-power-outages-a-simple-guide-to-k0s-over-tailscale/) 中。经作者许可在此转载。照片由 [natsuki](https://unsplash.com/@myr0326) / Unsplash 提供。*