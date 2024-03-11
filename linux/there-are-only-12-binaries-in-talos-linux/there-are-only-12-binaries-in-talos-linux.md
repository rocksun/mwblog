
<!--
title: Talos Linux 中只有 12 个二进制文件 - Sidero Labs
cover: https://www.siderolabs.com/wp-content/uploads/2024/03/12-binaries-banner-1.png
-->

Talos 是一个专用于 Kubernetes 的 Linux 发行版。我们只包含您需要的二进制文件。以下是所有二进制文件及其作用的列表。

> 译自 [There are only 12 binaries in Talos Linux - Sidero Labs](https://www.siderolabs.com/blog/there-are-only-12-binaries-in-talos-linux/)，作者 Justin Garrison。


## Linux 发行版对 Kubernetes 集群的影响

Linux 是 Kubernetes 集群的核心组件。您选择的 Linux 发行版将对创建集群的速度、工作负载的稳定性以及您需要执行的维护工作量产生重大影响。

在为容器或 Kubernetes 创建 Linux 版本时，许多公司和发行版的惯例是从通用 Linux 开始，然后删除您不需要的内容。这将导致主发行版占用更小的空间，例如 [Ubuntu minimal](https://wiki.ubuntu.com/Minimal)，但它始终从一个庞大、通用的 Linux 开始，并尝试使其更小。

Talos Linux 采取了相反的方法。如果发行版只需要运行 Kubernetes 呢？需要哪些最少的工具和可执行文件？

在 Talos 1.7.0 中的 `/bin` 和 `/sbin` 中有 **12 个唯一二进制文件**。这极大地减少了安装大小、操作系统所需的维护以及系统的可能安全漏洞。

作为参考，这里列出了一些其他流行的发行版以及它们默认包含的二进制文件数量。这也计算了符号链接或硬链接到另一个文件的可执行文件（例如，`lvm` 通常被符号链接多次以用于 `lvs` 和 `vgs`）。

| 发行版 | 二进制文件数量 |
|---|---|
| Talos Linux | 29 |
| Ubuntu Server 22.04 | 2780 |
| Amazon Linux 2 | 1382 |
| Flatcar Container Linux | 2391 |

所有发行版都使用默认安装选项进行设置。未安装任何其他软件包，并使用以下命令计算二进制文件：

```
ls -1 $(echo $PATH | tr ':' '\n') | wc -l
```

Talos 不提供 shell、`ls`、`tr` 或 `wc`。文件是通过 API 计算的，我们没有计算目录：

```
talosctl list -n $NODE_IP /sbin | wc -l
talosctl list -n $NODE_IP /bin | wc -l
```

系统上只有 12 个唯一文件，我们可以告诉您每个文件的作用。

### `/sbin/init`

`init` 二进制文件是 Talos Linux 的最大优势之一。Talos 不附带通用 init 系统，如 systemd。Talos 的 init 系统专门用于运行 Kubelet 和容器运行时。init 系统公开了一个声明性 API，这是配置和维护系统的方式。

`init` 二进制文件 [称为 machined](https://github.com/siderolabs/talos/blob/main/internal/app/machined/main.go)，并用 Go 编写。它的代码少于 400 行，Go 开发人员可以在一天内理解它。与超过 3000 行 C 代码的 [systemd](https://github.com/systemd/systemd/blob/main/src/core/main.c) 相比，我永远无法理解它。

`/sbin/init` 二进制文件硬链接到 `/sbin/dashboard`、`/sbin/poweroff`、`/sbin/shutdown` 和 `/sbin/wrapperd`。虽然从技术上讲这是 5 个文件，但它是一个文件硬链接 4 次以提供方便的命令。

仪表板用于提供有关节点的本地和远程信息。您可以在 YouTube 上看到它如何工作的概述。

二进制文件 `poweroff` 和 `shutdown` 是用于干净关闭节点的命令。它们由内核和外部工具使用，但 Talos 使用系统 API 来关闭。

[wrapperd](https://github.com/siderolabs/talos/blob/main/internal/app/wrapperd/main.go) 二进制文件在 init 期间用于派生具有较少权限的进程。因为子进程将从父进程继承很多内容，所以 wrapperd 用于删除内核功能，如 `CAP_SYSADMIN`。

系统上的所有其他二进制文件都包含在我们从源代码构建的其他软件包中。您可以看到它们是如何从 [GitHub](https://github.com/siderolabs/pkgs) 构建的，我们将在下面查看每个二进制文件。

### `/bin/containerd*`

这是随 Talos 一起提供的容器运行时。它通常与 Kubernetes 集群一起使用，并且是大多数提供商的默认容器运行时选项。

这也包括 `/bin/containerd-shim-runc-v2` 和 `/bin/containerd-shim`。这两个 shim 提供相同的功能（在 runc 下执行容器），但 containerd-shim 最初与 docker 一起使用，而 containerd-shim-runc-v2 从 containerd 使用。

### `/bin/runc`

这是容器的真正 [父进程](https://github.com/opencontainers/runc)。它是无守护进程的，因此如果需要，containerd 服务可以在不停止所有容器的情况下重新启动。

### `/sbin/modprobe`

[modprobe](https://linux.die.net/man/8/modprobe) 命令用于管理内核模块，以向内核添加或删除功能。这通常用于添加对特殊硬件（例如 GPU）的支持，但也用于其他内核工具。

Talos 不直接使用 modprob，但某些模块需要二进制文件来加载其他模块。您可以通过 [系统扩展](https://www.talos.dev/latest/talos-guides/configuration/system-extensions/) 向 Talos 添加内核模块，并使用 [Image Factory](https://www.talos.dev/latest/learn-more/image-factory/) 中的预构建扩展。

### `/sbin/lvm`
## LVM 二进制文件

LVM 二进制文件用于管理 Linux 中的逻辑卷。这是为在 Kubernetes 中运行的服务提供的，这些服务可能需要或期望主机上存在逻辑卷（例如 [rook](https://rook.io/docs/rook/latest-release/Getting-Started/Prerequisites/prerequisites/#lvm-package)）。

### /sbin/dmsetup

这用于管理使用设备映射驱动程序的逻辑卷。它类似于 `lvs` 命令，但对于更复杂的磁盘配置来说是一个单独的二进制文件。

### /sbin/udevd

`udevd` 守护程序获取内核消息并将消息传递给其他系统以读取消息。它可以作为 [Talos 机器配置](https://www.talos.dev/latest/reference/configuration/v1alpha1/config/#Config.machine.udev) 的一部分进行配置。

### /sbin/mkfs.xfs

这将在磁盘或逻辑卷上创建一个 [XFS 文件系统](https://en.wikipedia.org/wiki/XFS)。

### /sbin/xfs_repair

如果 XFS 文件系统损坏，则用于修复它。

### /sbin/xtables-legacy-multi

此二进制文件由 `iptables*` 和 `ip6tables*` 符号链接，用于配置主机上的 IP 表。容器网络接口 (CNI) 提供程序通常从主机挂载目录，并期望这些命令存在，因为它们无法轻松地在容器内运行。

这些符号链接占系统中的 12 个总文件，但它们都执行常见的 `iptables` 命令。

### 结论

这看起来似乎不可能，但这就是整个系统。每个二进制文件都是引导 Kubernetes 集群或作为集群一部分运行节点所必需的。这就是我们称 Talos Linux 为 [Kubernetes 操作系统](https://www.siderolabs.com/platform/talos-os-for-kubernetes/) 的原因。

`/lib` 和 `/usr` 中还有更多可执行文件，但那些是共享对象（`.so`）文件和内核模块（`.ko`）。这些对于为驱动程序和各种程序运行系统是必需的，但不会直接调用它们。

如果您想在您选择的系统上下载并安装 Talos，您可以在 [https://talos.dev](https://talos.dev) 开始。

要获得一个更简单的界面来管理本地或云提供商中的 Kubernetes 集群，请在 [https://www.siderolabs.com/platform/saas-for-kubernetes/](https://www.siderolabs.com/platform/saas-for-kubernetes/) 查看 Omni。

如果您有疑问或想入门，请加入 [Talos 社区 Slack](https://slack.dev.talos-systems.io/)。