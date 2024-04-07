
<!--
title: Podman 5 携多平台镜像和虚拟机支持而来
cover: https://cdn.thenewstack.io/media/2024/04/38bf6368-podman-logo.png
-->

Podman 所做的所有更改最终汇聚成一个更灵活、更具响应能力的容器运行时引擎。

> 译自 [Podman 5 Arrives with Multiplatform Images, VM Support](https://thenewstack.io/whats-new-with-podman-5-multiplatform-images-vm-support/)，作者 Jack Wallen。

如果你一直在使用 Podman 进行容器部署或开发，那么你将大饱口福。

[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 最近发布了 [Podman 容器管理系统](https://thenewstack.io/check-out-podman-red-hats-daemon-less-docker-alternative/) 的 5.0 版本，该版本完全重新设计了 Podman 虚拟机管理工具（*podman-machine*）的代码。

[官方发布公告](https://www.redhat.com/en/blog/podman-50-unveiled) 中提到：“Podman machine 包含一组子命令，用于管理 Podman 虚拟机，这是用户在 MacOS 或 Windows 上运行 Podman 所必需的。”

在 [Podman 5.0](https://github.com/containers/podman/releases/tag/v5.0.0) 中，新增了许多功能和改进，包括：

- 新的 *podman machine reset* 选项，它简化了重置 Podman 虚拟机的过程
- Podman 虚拟机的全新订阅管理器和 *qemu-user-static* 功能
- Podman 虚拟机的更快的启动时间
- 用于在远程机器上快速构建多平台镜像的 *podman farm build*
- 增加了对 [开放容器计划](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/) 工件的支持的 podman manifest
- 对无根网络工具的更改，以获得性能更高的网络堆栈

对 Podman 所做的所有更改最终都汇集到一个更灵活、响应更快的容器运行时引擎中。

## 问题

目前使用 Podman 5 的能力相当有限。据我所知，截至本周，获取/测试 Podman 5 的唯一途径是通过 [Fedora Linux](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/)，因为其他发行版的存储库中唯一可用的版本是 4.x。对于 Fedora，安装 Podman 5 的唯一途径是通过开发版本。

## 如何在 Fedora 上安装 Podman 5

首先，我不建议在 [生产](https://thenewstack.io/risk-aware-vs-risk-averse-product-development/) 机器上安装 Podman 的 [开发版本](https://thenewstack.io/risk-aware-vs-risk-averse-product-development/)。仅在测试环境中使用它。我也不会建议在虚拟机上执行此操作，因为 Podman 将难以访问 KVM 系统。

另一个问题是，你无法使用 Fedora 40 beta 1 之前的任何 Fedora 版本。如果你使用的是 39 或更早版本的 Fedora，则此方法将不起作用。因此，你需要做的第一件事是 [下载 Fedora 40 beta 的 ISO](https://fedoraproject.org/workstation/download?beta)。完成后，创建一个可引导闪存驱动器，启动进入 Fedora 40 beta 1，然后安装操作系统。

安装 Fedora 40 beta 1 后，你可以使用以下命令安装 Podman 5.0 的开发版本：

```
sudo dnf update --refresh --enablerepo=updates-testing podman
```

完成后，你可以使用以下命令验证安装：

```
podman --version
```

你应该在输出中看到类似以下内容：

```
podman version 5.0.1
```

## 使用 Podman 5

Podman 5.0 最好的功能之一是能够快速重置机器环境。此命令将停止所有正在运行的机器并删除它们。此外，还将删除 [配置数据文件](https://thenewstack.io/circleci-offers-a-private-option-for-orb-reusable-configuration-files/)（例如机器磁盘映像和先前提取的缓存映像）。该命令只有一个选项，即 –force（或仅 -f），它在未经确认的情况下重置所有内容。

假设你创建了几个机器，如下所示：

- podman machine init dev1
- podman machine init dev2
- podman machine init web1
- podman machine init web2

然后，你使用以下命令启动它们：

```
podman machine start dev1
podman machine start dev2
podman machine start web1
podman machine start web2
```

接下来，你使用以下命令访问每台机器：

```
podman machine ssh NAME
```

其中 NAME 可以是 *dev1*、*dev2*、*web1* 或 *web2*。

访问机器后，你 [开展了开发](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/) 工作，运行了一些测试，或者对机器执行了任何你需要执行的操作。使用完这些机器后，如果你想使用 Podman 4.x 摆脱它们，则必须分别停止它们，然后使用以下命令删除它们：

```
podman machine stop NAME
podman machine rm NAME
```

其中 NAME 可以是 dev1、dev2、web1 或 web2。

使用 Podman 5.0，可以使用以下命令完成所有这些操作：

```
podman machine reset
```

你的所有机器都将被停止并删除（以及关联的文件和数据）。

新版本还包括 `podman farm build` 命令，该命令在 farm 节点上构建镜像，然后将它们捆绑到清单列表中。我还没有测试过此功能，但根据手册页（使用 `man podman-farm` 阅读）：

Podman 通过读写位于 `$XDG_CONFIG_HOME/containers` 下的 `podman-connections.json` 文件来管理 farm，如果未设置 env，则默认为 `$HOME/.config/containers` 。 或者可以将 `PODMAN_CONNECTIONS_CONF` 环境变量设置为 podman 将使用的一个完整文件路径。此文件由 podman 命令管理，用户切勿直接编辑。要手动配置 farm，请使用 `containers.conf` 中的 `[farm]` 部分。

对于那些不使用 Fedora 40 的人，我还没有发现任何迹象表明它何时可用于不同的发行版。如果我猜的话，Podman 5.0 将在今年随 9.4 版本进入 Red Hat Enterprise Linux。如果发生这种情况，它很可能会很快进入 [Rocky Linux](https://thenewstack.io/start-developing-with-rocky-linux-as-a-docker-container/)、[AlmaLinux](https://thenewstack.io/jack-aboutboul-how-almalinux-came-to-be-and-why-it-was-needed/) 和 [Oracle Linux ](https://developer.oracle.com/?utm_content=inline+mention)。

同样重要的是，在更新到 Podman 5.0 之前，用户要了解 Podman 4 机器与 Podman 5.0 不兼容。因此，在升级到 5.0 之前，您应该删除所有 Podman 4 机器。在删除这些机器并升级到 Podman 5.0 之后，还建议在部署任何新机器之前运行 `podman machine reset` 命令。

要详细了解 Podman 5.0，请查看 [Podman 网站上的新功能摘要文章](https://blog.podman.io/2024/03/podman-5-0-has-been-released/)。
