[Warp](https://www.warp.dev/) 是一个代理开发环境，一个由 AI 驱动、终端优先的 DevOps 工程师和站点可靠性工程师 (SRE) 环境。

尽管 [Cursor](https://cursor.com/)、[Windsurf](https://windsurf.com/) 和 [Kiro](https://kiro.dev/) 等工具可用于部署应用程序和执行 DevOps 任务，但它们是代码优先的 IDE，内置终端。而 Warp 则采取了不同的方法，将代理引入终端并在其中嵌入编辑器，这使其成为执行管理和 DevOps 任务的理想选择。

为了证明其在管理任务方面的强大能力，我将向您展示如何在不运行任何命令的情况下，在一组虚拟机 (VM) 上安装 Kubernetes 1.33 集群。我们将利用 Warp 的代理，通过一个全面而详细的提示来设置集群。它不仅安装 Kubernetes，还为网络配置 Calico，并为存储配置一个本地路径供应器。由于我们正在使用与[氛围编程](https://en.wikipedia.org/wiki/Vibe_coding)相同的工作流程，但应用于 DevOps，我将这种方法称为 VibeOps。

由于 AI 代理是非确定性的，您的结果可能会有所不同。但在我的实验中，我发现在大多数情况下都能获得一致的结果。

继[上周的文章](https://thenewstack.io/multipass-fast-scriptable-ubuntu-vms-for-modern-devops/)之后，本教程假设您的系统上已安装 [Multipass](https://canonical.com/multipass)。有关背景和上下文，请参阅我在 The New Stack 上发表的文章。

让我们首先在配备 Apple Silicon 芯片的 Mac 上配置 Multipass 虚拟机。环境准备好后，我们将启动 Warp 并运行提示来设置 Kubernetes 集群。

## 步骤 1：在 macOS 上启动 Multipass 虚拟机

我们将首先启动作为控制平面的第一个节点。该节点必须满足至少四个 CPU 核心和 8GB 内存的先决条件才能运行控制平面。所有节点都将运行 Ubuntu 22.4，又名 [Jammy Jellyfish](https://releases.ubuntu.com/jammy/)。

```
multipass launch -c 4 -m 8G -n node-1 jammy
```

现在让我们启动集群的其余两个节点：

```
multipass launch -c 2 -n node-2 jammy
multipass launch -c 2 -n node-3 jammy
```

使用以下命令验证虚拟机：

```
multipass list
```

[![](https://cdn.thenewstack.io/media/2025/10/27cb05f0-warp-0-1024x259.png)](https://cdn.thenewstack.io/media/2025/10/27cb05f0-warp-0-1024x259.png)

下一步是将 Multipass 的内部 SSH 密钥加载到您的 SSH 代理中，以便代理可以轻松连接到其虚拟机，而无需输入密码或手动指定密钥。

```
sudo ssh-add "/var/root/Library/Application Support/multipassd/ssh-keys/id_rsa"
```

在继续之前，请验证您是否可以成功通过 SSH 连接到节点：

```
ssh ubuntu@192.168.2.2
```

## 步骤 2：提示 Warp 设置 Kubernetes 集群

现在虚拟机已准备就绪，我们可以通过向 Warp 代理发送提示来启动安装任务。我在安装过程中没有更改模型并接受了默认设置。

我使用以下提示来设置集群。

`You have access to the following ARM64 Ubuntu servers: 192.168.2.2, 192.168.2.3, 192.168.2.4. The username is ubuntu. Install a Kubernetes v1.33 cluster by using the correct package location. Install the control plane on 192.168.2.2 and make all nodes as worker nodes. Use kubeadm to install and configure the cluster. Use Calico (with standard manifests) for networking and Rancher local-path-provisoner for storage. On the control plane, configure ~/.kube/config file and verify the installation of the cluster. Finally, configure local kubectl to talk to the cluster. Write fast, compact and efficient scripts for this task and execute them.`

这是一个全面的提示，包含了安装和配置一个活跃 Kubernetes 集群所需的一切。我们提供了足够的提示，例如 ARM64 架构、Kubernetes 版本、kubeadm 工具、IP 地址、网络和存储选择，最后要求代理配置本地 kubectl 命令。这些步骤本质上与经验丰富的 Kubernetes 工程师安装集群时所遵循的步骤相同。

粘贴提示并按 Enter 键开始引导式安装过程。Warp 将提示您接受运行操作集群或配置的命令。切换到您希望存储代理生成的中间脚本的目录。在我的例子中，它是 `~/Downloads` 文件夹。

[![](https://cdn.thenewstack.io/media/2025/10/a71368a6-warp-1-1024x768.png)](https://cdn.thenewstack.io/media/2025/10/a71368a6-warp-1-1024x768.png)

几秒钟内，Warp 代理就会创建一个行动计划，并请求您的许可来创建和执行脚本。

[![](https://cdn.thenewstack.io/media/2025/10/31b817f6-warp-2-1024x222.png)](https://cdn.thenewstack.io/media/2025/10/31b817f6-warp-2-1024x222.png)

脚本创建后，它将开始执行。

[![](https://cdn.thenewstack.io/media/2025/10/7c58f835-warp-3-1024x768.png)](https://cdn.thenewstack.io/media/2025/10/7c58f835-warp-3-1024x768.png)

同时，我的 `Downloads` 文件夹中充满了 Warp 代理生成的脚本。

[![](https://cdn.thenewstack.io/media/2025/10/bb6eeaf5-warp-4-1024x337.png)](https://cdn.thenewstack.io/media/2025/10/bb6eeaf5-warp-4-1024x337.png)

在代理忙于执行脚本时，您可以随意探索这些脚本。密切关注 Warp 终端，查看一切是否按预期运行。

在接受并运行脚本后，Warp 能够设置集群，配置网络和存储，甚至将 kube 配置文件复制到本地 Mac 以配置 `kubectl` CLI。

代理通过启动一个 NGINX Pod 和一个存储卷来验证集群，然后确认安装。它还移除了控制平面节点的污点，使其可调度。最后，它通过展示所遵循的步骤来确认设置，这令人安心。整个过程大约花了 8 分钟，这比手动安装快得多。

[![](https://cdn.thenewstack.io/media/2025/10/8fbaccc3-warp-5-1024x768.png)](https://cdn.thenewstack.io/media/2025/10/8fbaccc3-warp-5-1024x768.png)

我尝试了相同的提示，在一组裸机上也能使集群正常工作。我甚至可以通过扩展提示来配置 MetalLB。我还能够通过模拟删除 kubelet 和停止节点上的服务等错误来调试集群。

[![](https://cdn.thenewstack.io/media/2025/10/ff26c597-warp-6-1024x416.png)](https://cdn.thenewstack.io/media/2025/10/ff26c597-warp-6-1024x416.png)

我的下一步是尝试基于 NVIDIA GPU operator 设置一个 GPU 集群。敬请期待后续文章中这次实验的发现和结果！