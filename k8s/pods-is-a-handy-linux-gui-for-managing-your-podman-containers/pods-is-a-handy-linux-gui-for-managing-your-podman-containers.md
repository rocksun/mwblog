
<!--
title: Pods 是一个方便的 Linux GUI，用于管理 Podman 容器
cover: https://cdn.thenewstack.io/media/2025/09/a2c0fdb3-kateryna-hliznitsova-3wl6rumol4s-unsplash.jpg
summary: 本文介绍了 Podman 的 GUI 工具 Pods 的安装、配置和使用方法。Pods 简化了 Podman 容器的管理，提供了本地和远程实例管理、镜像/容器/Pod 查看与控制等功能。安装只需使用 Flatpak，配置 Podman Socket 后即可连接使用。
-->

本文介绍了 Podman 的 GUI 工具 Pods 的安装、配置和使用方法。Pods 简化了 Podman 容器的管理，提供了本地和远程实例管理、镜像/容器/Pod 查看与控制等功能。安装只需使用 Flatpak，配置 Podman Socket 后即可连接使用。

> 译自：[Pods Is a Handy Linux GUI for Managing Your Podman Containers](https://thenewstack.io/pods-is-a-handy-linux-gui-for-managing-your-podman-containers/)
> 
> 作者：Jack Wallen

如果你一直使用 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 作为你的 [container](https://thenewstack.io/introduction-to-containers/) 开发环境，并且你选择的发行版是基于 [Fedora](https://thenewstack.io/ultramarine-linux-fedora-made-easy-and-beautiful-for-everyone/)，那么你可能已经接触过 [Podman](https://thenewstack.io/whats-new-with-podman-5-multiplatform-images-vm-support/)。

Podman 是 Docker 的替代品，在过去几年中获得了相当大的欢迎。如果你使用过 Podman，你可能想知道是否有用户友好的 GUI 可用于容器服务。

确实有。

实际上，有几个，其中一个叫做 Pods。Pods 是一个 Linux GUI，可以免费安装和使用在任何支持 Podman 和 [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) 的发行版上。这个方便的应用程序包括以下功能：

*   本地和远程 Podman 实例。
*   查看镜像、容器和 Pod。
*   查看关于镜像、容器和 Pod 的信息。
*   检查镜像、容器和 Pod。
*   查看/搜索容器日志。
*   监控容器和 Pod 进程。
*   下载镜像并使用 [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/ "Dockerfiles") 构建它们。
*   创建池和容器。
*   控制容器生命周期（启动、停止、暂停等）
*   删除镜像、容器和 Pod。
*   修剪镜像。
*   重命名容器。

这是一个相当完整的功能列表，这意味着对于那些刚开始学习 Podman 和容器的来龙去脉的人，或者甚至是那些了解这项技术并正在寻找一个简单的 GUI 的人来说，Pods 可能是一个出色的选择。

我想向你展示如何安装、配置和使用 Pods 来简化你的 Podman 管理。

## 你需要什么

你唯一需要的是一个支持 Podman 和 Flatpak 的 Linux 发行版。如果你正在使用 Fedora Desktop，那么这两个应用程序都应该预先安装好，所以无需担心依赖关系。

让我们开始安装。

## 安装 Pods

由于有了通用包管理器 Flatpak，Pods 非常容易安装。在你的桌面上打开一个终端窗口并执行以下命令：

```
flatpak install flathub com.github.marhkb.Pods
```

一旦该命令完成，有一些配置需要处理。

## 配置 Podman

接下来，我们必须配置 Podman，以便它允许 Pods 通过 Podman 套接字进行连接。为此，请执行以下命令：

```
systemctl --user enable --now podman.socket
```

此时，Podman 正在你的系统上运行。稍等片刻，Pods 应该能够成功连接。

## 将 Pods 连接到你的本地 Podman 服务

在你的桌面菜单中找到 Pods 并启动它。在出现的窗口（**图 1**）中，给连接命名，然后点击 Connect。

**图 1**

[![](https://cdn.thenewstack.io/media/2025/09/9136740c-pods1.jpg)](https://cdn.thenewstack.io/media/2025/09/9136740c-pods1.jpg)

创建本地连接不应该花费几秒钟的时间。

连接建立后，你应该进入 Pods 主窗口（**图 2**），你可以在那里创建你的第一个容器。

**图 2**

[![](https://cdn.thenewstack.io/media/2025/09/f55c8423-pods2.jpg)](https://cdn.thenewstack.io/media/2025/09/f55c8423-pods2.jpg)

Pods GUI 非常用户友好。

## 使用 Pods 创建你的第一个容器

在左侧边栏中选择 Containers，然后点击 Create Container。然后你可以接受随机生成的名称，或者手动输入一个（**图 3**）。

**图 3**

[![](https://cdn.thenewstack.io/media/2025/09/01e18463-pods3.jpg)](https://cdn.thenewstack.io/media/2025/09/01e18463-pods3.jpg)

使用 Pods 创建你的第一个容器。

让我们将 Ubuntu 部署为一个容器。点击 Remote Image 按钮（在 Select Image 旁边）。在搜索字段中输入 "ubuntu"，然后找到 Ubuntu 的官方镜像（**图 4**）。

**图 4**

[![](https://cdn.thenewstack.io/media/2025/09/711971d9-pods4.jpg)](https://cdn.thenewstack.io/media/2025/09/711971d9-pods4.jpg)

确保使用官方的 Ubuntu 镜像。

点击 Next 拉取最新版本的镜像。

现在你已经准备好了镜像，你可以根据需要配置容器。例如，你可以点击 Integrations 选项卡（拼图图标），然后添加端口映射、卷（**图 5**）、环境变量和标签。

**图 5**

[![](https://cdn.thenewstack.io/media/2025/09/d0762d08-pods5.jpg)](https://cdn.thenewstack.io/media/2025/09/d0762d08-pods5.jpg)

为容器添加一个卷。

完成配置后，点击 Run 部署容器。如果容器没有自动运行，你可以点击侧边栏中的 Container 链接，查看你的新容器。点击运行按钮启动它。

假设你已经部署了你的 Ubuntu 容器，并且想要通过 shell 访问它。在容器页面上，找到 Utilities 下的 Terminal（**图 7**）。

**图 6**

[![](https://cdn.thenewstack.io/media/2025/09/1704b7b6-pods7.jpg)](https://cdn.thenewstack.io/media/2025/09/1704b7b6-pods7.jpg)

所有可用于你的容器的实用程序。

点击 Terminal，你将立即获得对你正在运行的容器的 shell 的访问权限（**图 8**）。

**图 8**

[![](https://cdn.thenewstack.io/media/2025/09/33e046a1-pods8.jpg)](https://cdn.thenewstack.io/media/2025/09/33e046a1-pods8.jpg)

我们的 Ubuntu 容器的 CLI 已经可以使用了。

你现在可以做任何你需要做的事情来开发你新的基于 Ubuntu 的容器。你可以使用以下命令更新所有软件：

```
apt-get update && apt-get upgrade -y
```

然后你可以使用以下命令安装 Node.js：

```
apt-get install node.js -y
```

你已准备就绪。

Pods 是开始学习 Podman 的好方法。如果你是这项容器技术的新手，要知道在你掌握它之前你会失败几次。确保始终检查你的容器的日志，看看抛出了什么错误，这样你就可以进行故障排除并弄清楚发生了什么。

一旦你开始掌握了，你就可以冒险进入命令行，并尝试从 CLI 部署和管理你的容器、Pod 和卷。

享受 Pods 的新鲜 GUI 体验吧。