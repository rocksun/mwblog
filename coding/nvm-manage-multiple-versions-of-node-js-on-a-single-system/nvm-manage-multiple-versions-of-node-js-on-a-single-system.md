<!--
title: NVM: 在单个系统上管理多个Node.js版本
cover: https://cdn.thenewstack.io/media/2023/09/33e2dc43-umbrella-3380192_1280.jpg
summary: 告别Node.js版本混乱！🚀 NVM (Node Version Manager)神器来袭，轻松管理多版本Node.js，让你的项目不再受限！支持Ubuntu、Rocky Linux等主流系统，告别依赖冲突，提升开发效率！一键安装、版本切换，就是这么简单！快来体验NVM的强大吧！
-->

告别Node.js版本混乱！🚀 NVM (Node Version Manager)神器来袭，轻松管理多版本Node.js，让你的项目不再受限！支持Ubuntu、Rocky Linux等主流系统，告别依赖冲突，提升开发效率！一键安装、版本切换，就是这么简单！快来体验NVM的强大吧！

> 译自：[NVM: Manage Multiple Versions of Node.js on a Single System](https://thenewstack.io/nvm-manage-multiple-versions-of-node-js-on-a-single-system/)
> 
> 作者：Jack Wallen

## 概述

本文介绍了 NVM (Node Version Manager)，它是一个使开发人员能够在单个系统上管理多个 Node.js 版本的工具。这对于需要不同 Node.js 版本的项目特别有用，可以根据需要在它们之间轻松切换。

**主要特性和优势：**

- 可安装在各种 Linux 发行版、macOS 和 Windows（通过 Windows Subsystem for Linux）上
- 可以按用户安装
- 从命令行使用符合 POSIX 标准的 shell 调用
- 本文提供了在 Ubuntu Server 22.04.3 和 Rocky Linux 9 上安装 NVM 的分步说明，并指导用户使用 NVM 安装不同版本的 Node.js。

## 主要收获：

- 使用 NVM 在单个系统上管理多个 Node.js 版本
- 可安装在各种操作系统和架构上
- 可用于为单个项目或应用程序安装不同版本的 Node.js

开发人员经常不得不依赖同一语言、框架或库的多个版本。发生这种情况的原因可能是一个项目可能依赖于语言的最新版本，而另一个项目可能需要以前的版本。

某些操作系统和/或语言并没有简化使用同一语言的多个版本的任务。如果您碰巧使用 Linux 作为您的开发平台，并使用 Node.js 作为您使用的众多语言之一，那么您很幸运，因为有一个方便的工具可以使这项任务变得相当简单。

有问题的工具称为 [NVM](https://github.com/nvm-sh/nvm)，它是 Node Version Manager 的缩写。NVM 可以安装在许多不同的 Linux 发行版上，例如 Ubuntu、RHEL、CentOS Stream、[Rocky Linux](https://thenewstack.io/post-centos-rocky-linux-fights-for-community-driven-enterprise-open-source/)、[AlmaLinux](https://thenewstack.io/almalinux-captures-the-soul-of-centos/) 和 Debian，以及 MacOS 和 Windows（通过 Windows Subsystem for Linux）。

从本质上讲，NVM 是一个 Node.js 的版本管理器，它以每个用户为基础安装，并从任何符合 POSIX 标准的 shell（例如 sh、dash、ksh、zsh 和 bash）的命令行调用。

我将向您展示如何在 Ubuntu Server 22.04.3 和 Rocky Linux 9 上安装和使用 NVM。

## 你需要什么

要使用 NVM，您需要以下内容：

- Ubuntu 或 Rocky Linux 的实例（或其他等效实例，例如 AlmaLinux 或 CentOS Stream）。
- 已安装 Node.js。
- 具有 sudo 权限的用户。
- 网络连接。

就这样。让我们开始工作吧。

## 在 Ubuntu Server 上安装 NVM

登录到您的 Ubuntu Server 实例。如果您的服务器包含桌面环境，请打开一个终端窗口。

下一步是安装一些依赖项，可以使用一个命令来完成：

```
sudo apt-get install build-essential libssl-dev -y
```

接下来，使用以下命令下载并运行安装脚本：

```
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
```

命令完成后，注销并重新登录到您的 Ubuntu 服务器实例。

## 在 Rocky Linux（或等效发行版）上安装 NVM

在 Rocky Linux 上安装 NVM 与在 Ubuntu 上安装类似，唯一的区别是依赖项的安装。

要安装依赖项，请登录到您的 Rocky Linux 实例，并在必要时打开一个终端窗口。然后，发出以下命令来安装依赖项：

```
sudo dnf group install "Development Tools" -y
```

在 Rocky Linux 上安装依赖项将比在 Ubuntu 上花费的时间更长。完成后，您可以像在 Ubuntu 上一样在 Rocky Linux 上发出相同的安装命令，即：

```
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
```

命令完成后，注销 Rocky Linux 并重新登录。然后，您可以使用以下命令验证安装：

```
nvm --version
```

输出应如下所示：

```
0.39.5
```

NVM 现在已安装并可以使用。

如果您发现提示返回 NVM 未安装，您可能需要使用以下命令重新加载您的 .bashrc 脚本：

```
source ~/.bashrc
```

## 使用 NVM 安装 Node.js

现在已经安装了 NVM，您可以使用它来安装不同版本的 Node.js。无论您使用哪个发行版，此过程都是相同的。使用 NVM，您会发现可以安装从 v0.1.14 到 v20.7.0 的 Node.js 版本。当然，您可能不想一直回到 beta 版本，并且随着 Node.js 的升级，将添加更新的版本。

要查找 NVM 可用的 Node.js 版本的完整列表，请发出以下命令：

```
nvm list-remote
```

输出将如下所示：

```
        v19.0.1
        v19.1.0
        v19.2.0
        v19.3.0
        v19.4.0
        v19.5.0
        v19.6.0
        v19.6.1
        v19.7.0
        v19.8.0
        v19.8.1
        v19.9.0
        v20.0.0
        v20.1.0
        v20.2.0
        v20.3.0
        v20.3.1
        v20.4.0
        v20.5.0
        v20.5.1
        v20.6.0
        v20.6.1
        v20.7.0
```

假设你当前的项目需要 Node.js 版本 19.0.1。要安装此版本，命令如下：

```bash
nvm install v19.0.1
```

命令完成后，您可以使用以下命令验证安装：

```bash
nvm list
```

您应该看到以下输出：

```
-> v19.0.1
system
default -> v19.0.1
```

如果您已从默认软件包管理器（例如 apt-get）安装了 Node.js，您可能会在输出中看到一个 system 条目。 如果你想使用系统安装的 Node.js 版本，你可以执行以下命令：

```bash
nvm use system
```

如果您安装了多个 Node.js 版本，您可以使用如下命令选择要使用的版本：

```bash
nvm use v20.7.0
```

上述命令的输出将如下所示：

```
Now using node v20.7.0 (npm v10.1.0)
```

使用 NVM，您可以根据需要安装任意数量的 Node.js 版本，并轻松地在版本之间来回切换。 任何时候项目需要不同的版本，使用 `nvm use` 命令切换即可。

## Node.JS 常见问题

**Q: 什么是 Node.js？**

A: Node.js 是一个开源、跨平台的 JavaScript 运行时环境，允许开发人员在服务器端运行 JavaScript。 它提供了一个事件驱动、非阻塞 I/O 模型，用于构建可扩展和高性能的 Web 应用程序。

**Q: Node.js 中的“Node”代表什么？**

A: Node.js 中的“node”部分经常被误解为代表“神经网络优化”，但它来自一家名为“Node Coffee Shop”的咖啡店的名称，Node.js 的创建者之一 Jordan Walke 当时在那里工作。

**Q: 我可以在 Node.js 中使用哪些版本的 JavaScript？**

A: 您可以使用浏览器或其他客户端支持的任何版本的 JavaScript。 但是，为了获得最大的兼容性和性能，建议使用像 ECMAScript 2015 (ES6) 或更高版本这样的最新版本。

**Q: Node.js 仅用于构建 Web 应用程序吗？**

A: 虽然 Node.js 最常与构建 Web 应用程序相关联，但它也可以用于以下用途：

- 使用 Electron 等框架构建桌面和移动应用程序
- 使用 WebSockets 和服务器发送事件创建实时数据处理系统
- 将后端服务与前端应用程序集成

**Q: Node.js 的一些常见用例是什么？**

A: 一些流行的 Node.js 用例包括：

- 实时 Web 应用程序（例如，聊天机器人、实时更新）
- 高性能 Web 服务器（例如，Express.js、Hapi）
- 微服务架构
- 物联网开发
- 机器学习和人工智能

**Q: Node.js 中同步编程和异步编程有什么区别？**

A: 同步编程会阻塞代码的执行，直到任务完成。 异步编程允许您的应用程序在执行需要更长时间的任务（例如 I/O 操作）时继续运行。

**Q: Node.js 安全吗？**

A: Node.js 并非对安全问题免疫，但它确实提供了强大的内置功能，例如：

- 用于高效数据处理的缓冲区和流
- 内置对 HTTPS 和 TLS 加密的支持
- 类似沙盒的环境（例如，某些浏览器中的沙盒）

**Q: 我可以在 Node.js 中使用其他编程语言吗？**

A: 虽然 JavaScript 是 Node.js 中使用的主要语言，但您也可以使用以下语言编写代码：

- 通过 V8 引擎使用 C++
- 通过 v8-rs crate 使用 Rust
- 通过 pyjs 和 node-python 等第三方库使用 Python

**Q: 构建基于 Node.js 的 Web 应用程序有哪些流行的框架和工具？**

A: 构建基于 Node.js 的 Web 应用程序的一些流行选择包括：

- [Express.js](http://expressjs.com/)（Web 框架）
- [Hapi](https://hapi.dev/)（Web 框架）
- [Koa.js](http://koajs.com/)（Web 框架）
- [Socket.io](http://socket.io/)（实时通信库）
- [Redux](https://redux.js.org/) 或 [MobX](https://mobx.js.org/)（状态管理库）

**Q: Node.js 仍然由社区积极维护和支持吗？**

A: Node.js 项目由一个庞大的开发团队积极维护和更新，定期发布和添加新功能。