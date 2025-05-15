# Cycle 扩展到 Kubernetes 之外：新增 VM、裸金属、FaaS

![Featued image for: Cycle Expands Beyond Kubernetes: Adds VMs, Bare Metal, FaaS](https://cdn.thenewstack.io/media/2025/04/21f8663e-firat-sahin-wxqqvh-clq8-unsplash-1024x576.jpg)

[Firat Sahin](https://unsplash.com/@firatsahn?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/the-sky-is-filled-with-white-clouds-and-blue-sky-wXqqvH-cLQ8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)上发布。

*披露：作者代表* *cycle.io 撰写了这篇文章。*

[Cycle.io](https://cycle.io/)，这个低运维的 Kubernetes 替代方案，宣布了两项新功能，使其从云容器编排转变为一个全面的计算平台，用于容器、虚拟机 (VM) 和可以在任何地方运行的函数。

Cycle 结合了两件事：平台编排和基础设施管理。从基础设施的角度来看，该供应商历来专注于容器，支持 OCI 兼容或基于 [Docker](https://www.docker.com/?utm_content=inline+mention) 的容器镜像（使用 Docker Hub、Docker Registry 和 Dockerfile）。

底层的服务器显示为一个分布式资源池，现在可以存在于多个云提供商（[AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Equinix Metal](https://metal.equinix.com/?utm_content=inline+mention)、[GCP](https://cloud.google.com/?utm_content=inline+mention) 和 Vultr）以及通过新的虚拟提供商在裸金属上。

**使用 CycleOS 简化裸金属和 VM 部署**

从本质上讲，对裸金属的支持并不新鲜。Cycle 已经提供了一个 API 一段时间，允许与其他提供商集成。但是，新的虚拟提供商大大简化了该过程。

Cycle 的联合创始人兼首席执行官 [Jake Warner](https://www.linkedin.com/in/jakewarner/) 告诉 The New Stack：“我们为裸金属制作了一个简单的按钮。” “这意味着你可以在任何地方运行 Cycle——在边缘、本地和主机托管中。”

无需像以前那样需要很长时间才能实现 API，只需使用提供的向导即可。Cycle 启动该过程，两分钟后，用户将获得一个 4MB 的可下载 ISO，它是 CycleOS 的 [iPXE](https://ipxe.org) 加载器。这是一个最小的 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 派生的操作系统，为运行在其之上的容器层提供基本的网络、存储协议和插件。该 ISO 可用于使用 iPXE 进行网络启动，也可以从闪存驱动器手动安装在任何服务器上。

除了虚拟提供商之外，Cycle 还增加了对 [Qcow2](https://www.linux-kvm.org/page/Qcow2) 和原始格式的 VM 的新支持。在这里，CycleOS 位于 VM 下方，管理它们的网络、卷挂载等。

在 Cycle 上部署 VM 时，该平台会创建一个隐藏的容器实例，该实例在内部运行带有 [QEMU/KVM](https://www.qemu.org) 的虚拟机管理程序。最终用户无需在任何时候与此隐藏容器进行交互。由于该平台在后台自动管理虚拟机管理程序容器，因此无需手动配置。

Cycle 上的 VM 镜像可以通过三种方式获取：来自 Cycle 的内置基本镜像、远程 URL 或使用 iPXE 脚本。正如你所期望的那样，与容器不同，VM 在部署后无法重新镜像。

**Cycle 通过容器、VM 和 FaaS 支持多云计算**

在 Cycle 平台中，一个计算节点可以并行运行 VM、容器和函数。用户还可以在 AWS EC2、GCP 或 Vultr 实例之上运行 CycleOS，以将该实例转换为 Cycle 计算节点。[Warner](https://www.linkedin.com/in/jakewarner/) 开玩笑说：“这几乎是 VM 盗梦空间。” “只要最低的 VM 支持嵌套虚拟化，我们就可以在 VM 上运行 CycleOS 来托管其他 VM。”

可以使用与迁移容器实例相同的系统在支持虚拟机管理程序的服务器之间迁移 VM，包括跨区域迁移。这意味着附加到 VM 的卷也将迁移到目标实例。但是，在撰写本文时，虽然 VM 迁移有效，但它们不是实时迁移。在重定向流量之前，将在目标服务器上启动 VM 的新副本。

VM 可以访问与同一环境中存在的容器相同的专用网络。在 VM 中运行的应用程序可以使用发现服务连接到其他容器和 VM，而无需额外的配置。

Cycle 提供了一种运行 VM 的替代方法，特别是对于寻求比 Broadcom 成本更低的选项的公司，Cycle 还为需要更多控制其操作系统的客户提供 VM 支持。[Warner](https://www.linkedin.com/in/jakewarner/) 还预见了其他三个用例。第一个是针对 AI 初创公司。
他告诉我们：“我们有些使用 AI 的公司需要特定版本的内核，比如说 Ubuntu。以前，你无法控制这些；你不能将自己的内核引入 Cycle，因为我们只是[容器](https://thenewstack.io/zh/introduction-to-containers/)。现在，你可以将自己的操作系统作为 VM 运行在 Cycle 之上，如果需要，可以与你的容器并行运行。”

第二个用例涉及 Windows 的遗留支持。“我们的一些客户希望运行旧的 Windows 应用程序，并使用 Cycle 运行他们所有的容器，以及遗留的 Windows 应用程序，”Warner 说。“现在他们可以了。”

VM 的第三个用例是在 Cycle 之上运行 [Kubernetes](https://thenewstack.io/zh/kubernetes/)，将 Cycle 仅用作控制平面。“理论上，有人可以在他们所有的裸机上安装 Cycle，并在其上运行 Kubernetes VM；这将为他们提供多云、混合基础设施 Kubernetes，”Warner 告诉我们。

为了完善整个图景，Cycle 还包括函数容器，这些容器可用于原本将部署在无服务器或函数即服务 (FaaS) 架构上的工作负载。这些容器适用于临时任务、批处理或事件驱动的任务，例如转换文件、处理图像或训练大型语言模型。

函数容器配置有预定义数量的热实例，这些实例都经过预定义和配置，因此几乎可以立即启动（启动时间低于 100 毫秒）。更重要的是，由于这些是容器，因此用户不受特定运行时的限制；你可以将任何你想要的东西放入其中。

我承认我是 Cycle 的粉丝。虽然 Kubernetes 继续占据主导地位，但我认为 Cycle 为那些没有锁定在 Kubernetes 方式中或正在寻找出路的公司提供了一个精心设计的替代方案。

诚然，VM 的实现不如现有的容器功能那么全面。“这些新的 VM 功能与 VMware 相比，功能较少，”Warner 承认。“我们的目标是达到大约 80% 的功能完整度，足以在 Cycle 上正确运行 VM。然后，我们将观察我们的客户如何使用它并进行相应的优化。”

总而言之，这三个新功能可能代表了 2024 年 [Gartner Cool Vendor](https://cycle.io/blog/2024/12/gartner-cool-vendor/) 的一个转折点，因为它即将迎来十周年。我发现自己想到了一个零售客户，他们正在寻找一种更简单的方法来管理他们在大型商店中的 ePOS 系统，并且一直在与 Kubernetes 作斗争。同样，对于一些寻求利用新兴的[可持续软件](https://thenewstack.io/zh/ebooks/cloud-infrastructure/developers-guide-to-cloud-infrastructure-efficiency-and-sustainability/)运动的替代云提供商来说，Cycle 可能非常适合。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)