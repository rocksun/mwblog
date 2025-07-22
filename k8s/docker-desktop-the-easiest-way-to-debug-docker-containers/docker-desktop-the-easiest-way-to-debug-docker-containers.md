<!--
title: Docker Desktop：调试Docker容器的终极利器
cover: https://cdn.thenewstack.io/media/2025/07/8574ad19-dd-hiroko.jpg
summary: 本文介绍了Docker Desktop的Logs Explorer扩展，它可以更方便地查看和过滤Docker日志，尤其适合初学者。安装方法简单，通过Docker Hub运行Hello World示例，展示了实时日志查看和过滤功能。
-->

本文介绍了Docker Desktop的Logs Explorer扩展，它可以更方便地查看和过滤Docker日志，尤其适合初学者。安装方法简单，通过Docker Hub运行Hello World示例，展示了实时日志查看和过滤功能。

> 译自：[Docker Desktop: The Easiest Way to Debug Docker Containers](https://thenewstack.io/docker-desktop-the-easiest-way-to-debug-docker-containers/)
> 
> 作者：Jack Wallen

如果你是一名 [容器开发者](https://thenewstack.io/containers/) 并且你使用 [Docker](https://www.docker.com/?utm_content=inline+mention)，你可能遇到过这样的情况：当你遇到问题时，找到这些问题的答案可能会有点棘手。当然，Docker 有一些用于此目的的命令行工具，但它们并不总是最容易使用的。我曾从命令行进行过一些调试，但总是觉得它比我希望的要麻烦。

考虑一下这个命令：

```
docker container ls --all --format ‘{{ json . }}’ | python3 -m json.tool --json-lines
```

你真的想依赖这样一个复杂的命令吗？你不仅要理解它，还要记住它？更糟糕的是，输出并不总是能准确地告诉你问题所在（除非你确切地知道你要找什么）。

如果我告诉你有一种更简单的方法呢？

确实有，而且它来自 [Docker Desktop 应用](https://thenewstack.io/create-a-development-environment-in-docker-desktop/)。

没错，要获得查看 Docker 日志最有效和最简单的方法，你需要 [Docker Desktop 应用程序](https://docs.docker.com/desktop/)。但是新的日志查看功能默认情况下没有内置到应用程序中，因此你需要采取额外的步骤才能使其正常工作。

使用 Logs Explorer 扩展，你可以浏览 Docker 日志、过滤结果、使用高级搜索功能，甚至可以实时查看新日志。

它非常棒。

想象一下启动一个容器并在启动时能够对其进行调试。不再需要猜测，也不需要一遍又一遍地运行 `docker ps -a` 命令来查看你的容器是否处于运行状态。

幸运的是，Logs Explorer 扩展可用于 Docker Desktop，因此你无需处理令人困惑的复杂命令。

我知道你在说什么……如果你要学习 Docker 的来龙去脉，你需要知道这些命令。这在很大程度上是正确的，而且那些长期使用 Docker 的人应该知道这些命令。但是，对于那些刚刚开始他们的容器之旅的人呢？

想象一下，对于一个初级容器开发者来说，从 Docker Desktop 中学习调试和排除容器故障的基础知识会容易多少。我的朋友们，这是值得的（该扩展是免费的）。

说了这么多，让我们看看有什么可看的。

## 首先，安装 Docker Desktop

我将在 [macOS](https://thenewstack.io/how-to-set-up-macos-as-a-development-machine/) 上演示这一点，因为目前在 Linux 上安装 Docker Desktop 的状态非常糟糕，令人啼笑皆非。

要安装 Docker Desktop（它也会安装所需的 Docker 运行时引擎），请从官方 [Docker Desktop 下载页面](https://docs.docker.com/desktop/setup/install/mac-install/) 下载适用于 Apple Silicon 或基于 Intel 的系统的二进制安装程序。文件下载完成后，双击它，然后将 Docker Desktop 图标拖到文件夹图标。这应该只需要几秒钟即可完成。

安装完成后，你可以弹出安装程序，一切就绪。

当你第一次打开 Docker Desktop 时，你可以登录、创建帐户或跳过它。如果你只是刚开始接触它，请跳过这部分，因为你随时可以稍后返回并创建一个帐户。

## 安装扩展

Logs Explorer 扩展非常容易安装。你所要做的就是展开侧边栏中的“Extensions（扩展）”菜单项，然后单击“Manage（管理）”。在“Manage（管理）”部分中，单击“Browse（浏览）”选项卡，然后在搜索字段中键入 logs explorer。

一旦官方的 Logs Explorer 扩展出现，单击相关的“Install（安装）”按钮（图 1）。系统会提示你输入 macOS 用户密码，然后才能完成扩展安装。

[![screenshot](https://cdn.thenewstack.io/media/2025/07/1344d1e4-le1.jpg)](https://cdn.thenewstack.io/media/2025/07/1344d1e4-le1.jpg) 

*图 1：安装 Logs Explorer 扩展比你想象的要容易得多。*

安装完扩展后，你会在侧边栏中注意到新的 Logs Explorer 条目。

让我们看看它是如何工作的。

## Hello, World!

是的，我们将使用经过验证的 Hello, World! 应用程序来演示新安装的扩展。

单击侧边栏中的“Docker Hub”条目，然后在搜索字段中键入 hello world。按键盘上的 Enter 键，找到 Hello World 条目，然后单击相关的向下箭头以拉取镜像。

镜像拉取完成后，单击侧边栏中的“Images（镜像）”，选择“Hello World”，然后单击“Run（运行）”（图 2）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/07/ce728a99-le2.jpg)](https://cdn.thenewstack.io/media/2025/07/ce728a99-le2.jpg) 

*图 2：你即将使用 Docker Desktop 运行你的第一个容器。*

单击“Run（运行）”后，立即单击侧边栏中的“Logs Explorer”链接，你将实时看到日志输出（图 3）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/07/59d29da3-le3.jpg)](https://cdn.thenewstack.io/media/2025/07/59d29da3-le3.jpg) 

*图 3：现在，这很有帮助。*

显然，Hello World 应用程序不会产生大量可用的输出，因为它是一个非常小的容器。即便如此，你也可以了解 Logs Explorer 扩展提供的功能。如果这是一个更复杂的容器，你将看到更多的输出（以及更有用的输出）。

你还可以过滤输出。假设你正在调试一个包含 [NGINX](https://thenewstack.io/nginx-one-console-not-for-experts-only/) 的大型容器部署，并且你只想查看与 NGINX 相关的输出。在搜索字段中键入 nginx，你将只会看到包含 NGINX 的条目。

对于那些刚开始使用 Docker 开发容器的人来说，此扩展应该被认为是必备的。一旦你掌握了使用 Logs Explorer 扩展解释日志的方法，你就可以放心地迁移到命令行。