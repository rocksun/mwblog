
<!--
title: Code Anywhere：安卓平板化身开发机
cover: https://cdn.thenewstack.io/media/2025/07/7b8865ca-luis-andres-villalon-vega-xjd9jwfqddk-unsplash-1.jpg
summary: 数字游民可在Android平板上进行开发。需物理键盘。部分平板支持Linux环境，或用Termux模拟。可安装数据库、代码编辑器/IDE，如Code Studio。通过SSH访问远程电脑，用GitHub应用管理项目。选择性能好的平板。
-->

数字游民可在Android平板上进行开发。需物理键盘。部分平板支持Linux环境，或用Termux模拟。可安装数据库、代码编辑器/IDE，如Code Studio。通过SSH访问远程电脑，用GitHub应用管理项目。选择性能好的平板。

> 译自：[Code Anywhere: Turn Your Android Tablet Into a Dev Machine](https://thenewstack.io/code-anywhere-turn-your-android-tablet-into-a-dev-machine/)
> 
> 作者：Jack Wallen

你是一位经常在路上奔波，但仍然需要完成工作的数字游民吗？这里说的“工作”是指开发。如果听起来像你，那么你很可能随身携带一台笔记本电脑。为什么不呢？笔记本电脑拥有完整的[操作系统](https://thenewstack.io/introduction-to-linux-operating-system/)，可以安装和使用你最喜欢的 [IDE](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) 以及处理任何项目的必要工具。

但是，如果你可以稍微减轻负担，并使用 [Android](https://thenewstack.io/how-we-engineered-capturing-android-anrs-in-otel/) 平板电脑来完成其中的一些项目呢？毕竟，平板电脑比笔记本电脑（即使带键盘套）更容易携带。

在我深入探讨之前，要知道你无法重现你在笔记本电脑或台式机上拥有的相同类型的开发环境。即便如此，你仍然可以使用平板电脑，并且做得相当不错。

话虽如此，你如何开始在 [Android 平板电脑](https://thenewstack.io/generative-ai-thread-runs-through-googles-new-products/) 上进行开发？让我看看我是否能帮助你。

## 首先要做的事情

我不在乎你在手机或平板电脑的虚拟键盘上打字有多快；你肯定需要一个物理键盘，否则，你正在做的任何事情都会花费大量时间。

Android 有大量可用的蓝牙键盘，例如 [亚马逊上这个 15 美元的选项](https://www.amazon.com/Bluetooth-Keyboard-Protable-Rechargeable-Illuminated/dp/B098QJT63W)。你不需要任何花哨的东西，只需要一个键盘，这样你就不会用食指和拇指戳你的平板电脑了。

## Linux 支持

在某些 Android 平板电脑（运行 Android 15 或更高版本）上，你可以启用 Linux 开发环境。这样做会为你提供一个在沙盒 [Linux](https://thenewstack.io/choosing-a-linux-distribution/) 环境中运行的完整终端。启用此功能后，你可以访问所有需要的命令行工具，甚至可以使用 *apt* 包管理器安装更多工具。

要启用 Linux 开发环境，你必须首先启用开发者工具，方法是转到“设置”>“关于平板电脑”，然后点击内部版本号 7 次。完成此操作后，你将在应用程序抽屉中找到一个 Linux 终端应用程序。在尝试安装任何命令行工具之前，请务必运行 *apt-get update* 命令（否则会失败）。

如果你的平板电脑不包含 Linux 环境支持，你可以随时安装 [Termux](https://play.google.com/store/apps/details?id=com.termux)，它是一个终端模拟器和 Linux 环境。

## 安装数据库

如果你的开发需要数据库，你应该能够使用以下命令从 Linux 环境（无论是原生的还是通过 Termux）中执行此操作（我将演示使用 MongoDB 和 Termux）：

```shell
pkg update
pkg upgrade
pkg i tur-repo -y
pkg i mongod -y
```

安装完成后，你可以使用以下命令访问 MongoDB 控制台：

```shell
mongod
```

你可以使用以下命令添加 Apache Web 服务器和 PHP：

```shell
pkg i apache2 php -y
```

## 安装代码编辑器/IDE

事实是，适用于 Android 的优秀 IDE 并不多。但这并不意味着没有。你可以尝试以下方法，看看其中一种是否适合你的需求：

* [Code Studio](https://play.google.com/store/apps/details?id=com.alif.ide) – 用于开发 Android 应用程序、Java 控制台程序和网站。
* [PyCoder](https://play.google.com/store/apps/details?id=com.ikou.pycoding) – 带有内置 AI 的 Python3 IDE。
* [CodeSnack IDE](https://play.google.com/store/apps/details?id=com.cloudcompilerapp) – 允许你使用多种不同的语言进行开发，并提供易于使用的工具，例如按示例编写代码。
* [Code Editor](https://play.google.com/store/apps/details?id=com.rhmsoft.code) – 支持 C、C++、[PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/)、[Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/)、[JavaScript](https://thenewstack.io/introduction-to-javascript/)、HTML、CSS 等语言。

## 访问远程计算机和 GitHub

我所做的大部分工作都是通过 Linux 计算机完成的。在这些计算机上，我保持 SSH 服务器运行，因此我可以随时登录它们。你可以在 Android 平板电脑上安装 SSH 客户端，通过 SSH 连接到你的 Linux 计算机，并使用所有可用的工具。我最喜欢的 Android SSH 客户端之一是 [Termius](https://play.google.com/store/apps/details?id=com.server.auditor.ssh.client)，它可以轻松保存主机，并包含简化访问远程计算机所需的所有功能。

你还可以在平板电脑上安装 [GitHub](https://play.google.com/store/apps/details?id=com.github.android) 应用程序，以便你可以对通知进行分类、审查、评论和合并。请记住，你无法使用此应用程序进行推送和拉取。但是，你可以使用 Termux 或通过内置的 Linux 环境安装 [Git](https://thenewstack.io/linus-torvalds-reflects-on-20-years-of-git/)（命令行工具）。相应的命令是：

* Linux 环境 – *apt install git -y*
* Termux – *pkg i git -y*

## 添加项目管理应用程序

你还可以添加项目管理应用程序。我更喜欢看板，但 Android 上有很多不错的管理应用程序，例如：

## 获取合适的平板电脑

最后的考虑因素是合适的平板电脑。你不想使用显示效果差的低功耗设备。如果你想购买一款能够提供充足动力、可靠显示效果和充足存储空间的平板电脑，请考虑以下之一：

使用 Android 平板电脑进行开发并非不可能。只需发挥一点创造力，你就可以拥有一个轻量级的工具随身携带，无论旅途将你带到何处，它都能让你始终掌控你的项目。