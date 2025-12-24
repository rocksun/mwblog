<!--
title: Fedora Silverblue：开发神器，化繁为简
cover: https://cdn.thenewstack.io/media/2025/12/e6296a88-round-icons-lfmqv_kq51i-unsplash.png
summary: Fedora Silverblue的Toolbox提供容器化开发环境。保持宿主系统整洁，隔离依赖，支持多发行版，主要用于命令行。用`create/enter/run`管理，注意安全。
-->

Fedora Silverblue的Toolbox提供容器化开发环境。保持宿主系统整洁，隔离依赖，支持多发行版，主要用于命令行。用`create/enter/run`管理，注意安全。

> 译自：[Fedora Silverblue Has a Handy Tool To Help Simplify Development](https://thenewstack.io/fedora-silverblue-has-a-handy-tool-to-help-simplify-development/)
> 
> 作者：Jack Wallen

如果你正在寻找一个用于开发目的的新 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)，你应该考虑 [Fedora Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/)。为什么？简单来说，Toolbox。

Toolbox 是 Fedora Silverblue 附带的一个工具，允许你创建 [容器化环境](https://thenewstack.io/containers/)，用于日常软件开发和调试。得益于 Fedora Silverblue 的不可变特性（操作系统核心以只读方式挂载），Toolbox 提供了一个熟悉的基于软件包的环境，你可以在其中安装和使用工具和库。

## Toolbox 的优势

使用 Toolbox 的优势包括：

*   保持宿主操作系统干净稳定。
*   避免安装开发工具和软件包后可能出现的混乱。
*   访问不同的发行版。
*   更好地隔离和组织不同项目所需的依赖项。
*   安全的实验方式，因为你可以随意创建和销毁容器。

尽管 Toolbox 容器是隔离的，但它们仍然可以访问宿主系统，所以不要认为开发或运行你平时不会在宿主上运行的软件是安全的。你仍然需要谨慎使用。

请记住，Toolbox 只创建命令行环境，所以如果你正在开发 GUI 应用，这并非你所需的工具。如果你想构建 Web 应用、服务或其他命令行友好的工具，这个应用会是一个真正的便利。

而且由于它预装在 Fedora Silverblue 上，一旦你安装了操作系统，就可以立即开始使用。

## 容器化环境

请记住，Toolbox 环境可以无缝访问用户的主目录、Wayland 和 X11 套接字、网络、可移动设备、[systemd 日志](https://thenewstack.io/systemds-lennart-poettering-wants-to-bring-linux-home-directories-into-the-21st-century/)、[SSH 代理](https://thenewstack.io/ssh-made-easy-with-ssh-agent-and-ssh-config/)、D-Bus、ulimits、/dev、udev 数据库等等。

由于 Fedora Silverblue（以及其他基于 OStree 的发行版）不鼓励在宿主上安装软件，而是将软件作为（或在）容器中安装，因此通过标准方法设置开发环境或故障排除可能会很困难。

因此，便有了 Toolbox。

但是如何使用 Toolbox 呢？

很高兴你问了。

让我们深入了解。

## 使用 Toolbox 的第一步

当你创建一个新的 Toolbox 环境时，每个实例都包含：

*   你的用户名和权限。
*   访问你的主目录、系统和会话 D-Bus、系统日志和 Kerberos。
*   常用命令行工具，例如你的包管理器。

Toolbox（也称为 Toolbx）创建可变容器，你可以在其中安装所有你喜欢的开发/故障排除工具、编辑器、SDK 等。

请记住，Toolbox 不做任何安全承诺，所以请谨慎使用。

你必须做的第一件事是下载一个 OCI 镜像并创建一个 toolbx 容器，这可以通过以下命令完成：

```
toolbox create
```

系统会要求你确认此过程，输入 Y 继续。这将从 Fedoraproject 注册表拉取。根据你的网络连接情况，这可能需要几分钟。

注册表拉取完成后，你就可以使用以下命令进入新的 Toolbox 容器：

```
toolbox enter
```

你可以使用以下命令离开容器：

```
exit
```

默认情况下，create 命令会拉取并创建一个 Fedora 容器。如果你想拉取不同的发行版（例如 Ubuntu 24.04），可以使用：

```
toolbox create --distro utuntu --release 24.04
```

当拉取非默认发行版时，你必须告诉 Toolbox 你想使用哪个版本；否则，它会报错。

同样，如果你创建了不同的容器（非默认容器），你必须告知 Toolbox 你想进入哪个容器，像这样：

```
toolbox enter ubuntu-toolbox-24.04
```

此时，你已可以访问所有必要的工具来安装你开始开发所需的任何东西。例如，如果你在 Ubuntu 容器中需要 [Node.js](https://nodejs.org/)，可以输入以下命令：

```
sudo apt-get update
sudo apt-get install nodejs -y
```

你可以在容器中安装任何你需要的工具。

再次强调，使用 exit 命令离开容器。

你可以使用以下命令列出所有 Toolbox 容器：

```
toolbox list
```

你应该看到所有容器当前都在运行。

## 将应用程序安装到 Toolbox 容器中

你也可以在不进入 Toolbox 容器的情况下，将应用程序安装到其中。假设你想在不先进入容器的情况下升级当前的 Fedora 容器。为此，你可以运行以下命令：

```
toolbox run sudo dnf update
```

或者你可以安装 NGINX：

```
toolbox run sudo dnf install nginx -y
```

如果你想在不同的容器（例如 ubuntu-toolbox-24.04）上执行此操作，命令将是：

```
toolbox run -c ubuntu-toolbox-24.04 sudo apt-get install nginx
```

如果你想移除一个 Toolbox 容器，命令是：

```
toolbox rm NAME
```

其中 NAME 是容器的名称。例如，你可以使用以下命令移除 ubuntu-toolbox-24.04 容器：

```
toolbox rm ubuntu-toolbox-24.04
```

如果你想移除所有容器，你必须首先停止它们。奇怪的是，Toolbox 没有 stop 命令，所以你必须使用 [Podman](https://thenewstack.io/pods-is-a-handy-linux-gui-for-managing-your-podman-containers/) 来停止它们，如下所示：

```
podman stop fedora-toolbox-43
```

一旦你停止了容器，你就可以用以下命令移除它：

```
toolbox rm fedora-toolbox-43
```

我的朋友们，这就是你如何使用 Toolbox 创建用于开发目的的容器化环境。这个工具非常方便。试一试，看看它是否会成为你的首选工具。