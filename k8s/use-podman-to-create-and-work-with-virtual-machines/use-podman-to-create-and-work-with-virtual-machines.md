
<!--
title: 使用 Podman 创建和使用虚拟机
cover: https://cdn.thenewstack.io/media/2024/04/38bf6368-podman-logo.png
-->

Red Hat 的 Podman 不仅可以用来管理容器，而且对于构建和维护虚拟机也很方便。

> 译自 [Use Podman to Create and Work with Virtual Machines](https://thenewstack.io/use-podman-to-create-and-work-with-virtual-machines/)，作者 Jack Wallen。

当您想到 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 Podman 时，会想到一件事：[容器](https://thenewstack.io/containers/)。这是因为 [Podman 被创建](https://thenewstack.io/check-out-podman-red-hats-daemon-less-docker-alternative/) 为用于 [创建和管理容器化应用程序](https://thenewstack.io/install-and-use-podman-desktop-gui-to-manage-containers/) 和服务。 

但是 Podman 还有另一个绝招。在 [QEMU 仿真器](https://www.qemu.org/) 的帮助下，Podman 能够创建基本的 Fedora CoreOS 虚拟机，该虚拟机可用于容器、容器化工作负载或此类容器化应用程序的开发（只要它们在 [Fedora CoreOS](https://fedoraproject.org/coreos/download?stream=stable) 领域内工作）。

对于不熟悉 Fedora CoreOS 的人来说，它是专门创建的，以优化运行容器化应用程序。Fedora CoreOS 最初于 2003 年 11 月 6 日发布，此后一直在稳步增长。顾名思义，Fedora CoreOS 在设计上保持在最低限度，因此它只包含您需要的内容。

Podman 使部署 Fedora CoreOS 虚拟机变得轻而易举。通过这样做，您不必担心从 Docker Hub 或任何其他第三方存储库中提取最新版本的 Fedora CoreOS。这意味着 [虚拟机是干净的](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/)。

但是，您如何开始使用这些虚拟机？让我向您展示如何操作。

## 您需要什么

要使用 Podman Machines，您需要一个基于 Ubuntu 的 Linux 发行版。虽然基于 RHEL 的发行版上的 Podman 版本支持 Machines 命令，但目前无法安装必要的 QEMU 软件来使其工作。这就是我将重点演示 Ubuntu 的原因。您还需要一个具有 [sudo 权限](https://thenewstack.io/sudo-update-offers-python-plug-ins-extended-logging-auditing/) 的用户才能进行安装。

就是这样。让我们来点 VM 魔术。

## 安装 Podman 和要求

Ubuntu 没有配备 Podman。好消息是可以从标准存储库中安装它。因此，登录到您的 Ubuntu 系统，打开一个终端窗口，并使用以下命令安装 Podman：

```
sudo apt-get install podman -y
```

系统会提示您输入用户密码以获得管理员权限。安装完成后，您需要安装所需的 QEMU 软件，使用以下命令完成：

```
sudo apt-get install qemu-system -y
```

完成后，您必须执行一个（或两个）步骤。首先，下载 gvproxy 文件并使用以下命令将其保存到正确的位置：

```
wget https://github.com/containers/podman-machine/releases/download/v0.1.0/gvproxy -O /usr/bin/gvproxy
```

最后，您需要确保加载了 KVM 内核模块，这意味着您正在运行的机器必须支持 KVM。可以使用以下方法之一完成此操作：

```
sudo modprobe kvm-intel
sudo modprobe kvm-amd
```

您现在可以继续创建您的第一个 Fedora CoreOS 虚拟机。

## 部署虚拟机

Podman 虚拟机使用 *podman* 机器命令（以及各种选项）进行管理。首先，使用以下命令查看当前机器：

```
podman machine list
```

您不应该看到列出的任何虚拟机，因为我们还没有创建任何虚拟机。要创建您的第一个 VM，请使用以下命令对其进行初始化：

```
podman machine init
```

上述命令将创建一个具有随机生成名称的新 VM。您还可以使用以下方法生成一个具有用户指定名称的 VM：

```
podman machine init NAME
```

其中 NAME 是您要部署的机器的名称。

现在，如果您查看可用的 VM（使用命令 podman machine list），您应该会看到一个列出，名称是随机生成的还是用户创建的。

假设您创建了一个名为 vm1 的新 VM。要启动该机器，请发出以下命令：

```
podman machine start vm1
```

虚拟机将启动，当您收到提示符时，您就可以开始了。

## SSH 到您的虚拟机

虚拟机正在运行，现在是时候访问它了，这是通过 SSH 完成的。在您尝试运行标准 ssh 命令之前，这不是在这种情况下它的工作方式。要 SSH 到您的虚拟机，请运行以下命令：

```
podman machine ssh NAME
```

其中 NAME 是虚拟机的名称。如果您在创建 VM 时没有提供名称，则可以简单地发出以下命令：

```
podman machine ssh
```

此时，您会发现自己处于正在运行的虚拟机中，您可以在其中开始开发您的容器化应用程序。完成后，您可以使用以下命令退出该虚拟机：

```
exit
```

最后，您可以使用以下命令停止虚拟机：

```
podman machine stop
```

当然，如果您为虚拟机指定了自定义名称，则该命令应为：

```
podman machine stop NAME
```

其中 `NAME` 是您希望停止的虚拟机的名称。

您可以根据需要部署任意数量的虚拟机。但是，我建议您始终为虚拟机指定一个唯一的标识名称，以指示您正在构建的容器化应用程序或服务。

您还可以使用以下命令删除虚拟机：

```
podman machine rm NAME
```

其中 `NAME` 是您希望删除的虚拟机的名称。

我的朋友们，这就是使用 Podman 应用程序部署虚拟机的全部内容。
