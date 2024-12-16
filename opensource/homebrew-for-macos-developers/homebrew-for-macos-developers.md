
<!--
title: macOS开发者必备Homebrew
cover: https://cdn.thenewstack.io/media/2024/12/9be3eb5f-homebrew.png
-->

本文从开发者的角度解释了包管理器的使用，并演示了Homebrew的安装和基本用法。

> 译自 [Homebrew for MacOS Developers](https://thenewstack.io/homebrew-for-macos-developers/)，作者 Damon M Garn。

使用 GUI 安装新的 Mac 应用程序非常简单。但是，并非所有软件都打包精美或依赖于图形环境。此外，某些用户可能希望自定义特定软件的安装。macOS 的 Homebrew 包管理器很好地满足了这一需求。

本文将从开发者的角度解释包管理器的使用，演示 Homebrew 的安装和基本用法，并讨论其功能。

## 什么是包管理器？

包管理器帮助用户和管理员[维护软件](https://thenewstack.io/an-introduction-to-the-snap-universal-package-manager/)。它们安装、删除、更新和报告系统上的软件包。大多数包管理器都从命令行使用，尽管有些也有图形界面。

Homebrew 是 macOS 事实上的标准包管理器。Linux 用户熟悉 DNF 或[APT](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/)，Windows 用户使用 MSI 或 Chocolately，而 macOS 用户则依赖于[Homebrew](https://docs.brew.sh/)。

包管理器具有不同的功能，但它们通常会跟踪已安装的软件，并提供一个用于管理该软件及其依赖项的界面。使用包管理器维护软件有很多优点，其中一些我将在下面列出：

- 易于添加、删除和更新应用程序。
- 易于分发您编写的应用程序。
- 可编写脚本以实现自动化。
- 可以处理软件依赖项，使安装更容易。
- 简化系统管理。
- 提供对非标准或未发布工具的访问。

Homebrew 是在 Mac 上进行编码的开发人员的关键工具。

## 在您的 Mac 上安装 Homebrew

Homebrew 本身易于安装。主页提供了必要的 curl 命令，可以将 Homebrew 拉取到您的 Mac Intel 或 Silicon 系统。您也可以从[GitHub](https://github.com/Homebrew/brew)安装 Homebrew。

将以下 curl 命令粘贴到您的 shell 中以安装 Homebrew：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

安装脚本清楚地解释了该过程，因此您可以确认安装。安装完成后，键入 `brew -v` 以查看版本信息。

![](https://cdn.thenewstack.io/media/2024/12/364d65e8-brewversion.png)

*图1：brew -v 显示包管理器版本。*

如果您一段时间前安装了 Homebrew，并且只是现在开始探索它，请键入 `brew update` 将其更新到最新版本。

就是这样！您刚刚为您的 Mac 添加了一个强大的新应用程序。现在是开始使用它的时间了。

### Homebrew 术语

Homebrew 使用它自己的术语，包括一些您应该熟悉的几个基本概念。这些包括：

- Cask：安装 GUI macOS 原生应用程序的包定义。
- Formula：从源代码安装 CLI 应用程序的包定义。
- Keg：目标安装目录。
- Tap：公式或 cask 的目录或 Git 仓库。

在您使用 Homebrew 的过程中，您会很快熟悉这些术语。

## 管理软件

管理 Mac 上的开发工具和其他软件意味着安装、更新和删除应用程序——这正是 Homebrew 擅长做的。Homebrew 的语法将主要的 `brew` 命令与次要子命令和选项结合起来，以对指定的参数（通常是软件包）进行操作。

语法：`brew subcommand -options argument`

语法示例：`brew info iterm2`

我在下面介绍几个实际示例。

### 基本包管理

显然，关键任务是部署软件。`install` 子命令处理此问题。

如果您是 Vim 文本编辑器的粉丝，可以考虑通过安装[NeoVim](https://neovim.io/) 开始您的 Homebrew 之旅。安装此公式的命令是：

```bash
brew install neovim
```

[iTerm2](https://iterm2.com/) 终端程序是另一个不错的起点。它比标准 macOS 终端强大得多，并且可配置性更强。使用以下命令安装此 cask（GUI 应用程序）：

```bash
brew install --cask iterm2
```

![](https://cdn.thenewstack.io/media/2024/12/aa0b1f1f-install-iterm2.png)

*图2：安装iTerm2程序是开始使用Homebrew的好地方。*

另一个例子是[PyCharm Python IDE](https://www.jetbrains.com/pycharm/)。运行此命令以安装它：

```bash
brew install --cask pycharm
```

在这种情况下，[PyCharm](https://formulae.brew.sh/cask/pycharm#default) 是一个 macOS 原生应用程序，因此使用了 `--cask` 标志。通常，只有在程序同时具有公式和 cask 版本时才需要此标志。

使用 `info` 子命令显示 PyCharm 的信息，如下所示：

```bash
brew info pycharm
```

使用 `uninstall` 子命令删除 IDE：

```bash
brew uninstall pycharm
```
查看系统上 Homebrew 管理的软件包完整清单可能很有用。为此，请使用 `list` 子命令。如果您知道要查找的内容，可以将结果重定向到 `grep` 搜索。

```bash
brew list
```

![brew list](https://cdn.thenewstack.io/media/2024/12/44c69063-brewlist.png)

*图3：使用brew list命令显示已安装的软件。*

### 避免依赖地狱

在早期，管理软件最具挑战性的方面之一是[依赖项](https://thenewstack.io/a-guide-to-software-dependencies/)。如今的许多开源（甚至专有）软件都依赖于与其他应用程序和代码库的互连关系。换句话说，安装应用程序并不总是像简单地将该程序添加到系统中那样简单。您可能还需要添加它依赖的其他程序，以及这些程序可能依赖的其他程序。这种情况非常频繁，以至于产生了一个常用术语：[依赖地狱](https://en.wikipedia.org/wiki/Dependency_hell)。

现代包管理器——包括 Homebrew——会为您识别和处理这些依赖项。这是一个好消息，因为它简化了系统上软件的管理。

结果是，您可能输入命令来安装一个应用程序，但会发现该过程实际上也部署了许多其他软件。Homebrew 甚至会跟踪和维护每个应用程序的依赖项版本，以避免兼容性问题。

### 保持应用程序更新

您需要使软件保持最新，以降低安全风险，访问新功能并确保性能和稳定性。

如上所述，使用 `brew update` 命令获取包管理器本身的最新版本。但是您已经安装的应用程序呢？`upgrade` 子命令负责处理这些。

使用 `upgrade` 子命令而不带参数，即可将所有已安装的软件包更新到最新版本。请注意，如果您有很多应用程序并且最近没有升级它们，这可能需要一些时间。Homebrew 也会更新依赖项。

```bash
brew upgrade
```

您可能只想更新特定应用程序。如果是这样，只需将其指定为 `upgrade` 子命令的参数即可。例如，要仅更新 mtr [网络诊断软件](https://formulae.brew.sh/formula/mtr#default)，请键入：

```bash
brew upgrade mtr
```

## 查找软件

Mac 用户有各种获取软件的选项。在某些情况下，您可以访问供应商的网站直接下载 `.dmg` 或 `.pkg` 文件。其他时候，您可能会被引导克隆 Git 存储库并从源文件构建应用程序。第三种选择是在 Apple App Store 中浏览您想要的应用程序。

App Store 为开发者和其他高级用户带来了一个特殊的挑战。应用程序会经过严格的测试过程，以确保其质量和一致性。并非所有应用程序都已准备好进行此过程，而且并非所有开发者都需要或希望 Apple 决定其软件的可用性。

Homebrew 提供了 App Store 中可能无法提供的应用程序。也许该软件处于测试阶段，尚未准备好用于主流生产，或者它处理的是 Apple 不批准的领域。无论情况如何，软件供应商都可以通过 Homebrew 提供其应用程序，从而提供 App Store 的替代方案。

![neovim](https://cdn.thenewstack.io/media/2024/12/c0720b3b-neovim-brew-not-appstore.png)

### 助您开始使用 Homebrew 的开发工具

Homebrew 提供了维护功能性开发平台所需的 IDE、库和其他应用程序。

使用 `brew search {application-name}` 命令搜索应用程序，或浏览庞大的[公式列表](https://formulae.brew.sh/formula/)。以下是一些入门示例：

* [neovim](https://formulae.brew.sh/formula/neovim#default)：Vim 文本编辑器分支，通常用于 Mac。
* [pycharm](https://formulae.brew.sh/cask/pycharm#default)：功能强大的 Python IDE。
* [python3](https://formulae.brew.sh/formula/python@3.13#default)：常用的编程语言。
* [iterm2](https://formulae.brew.sh/cask/iterm2#default)：Apple 终端应用程序的强大替代品。
* [mariadb](https://formulae.brew.sh/formula/mariadb#default)：MySQL 数据库的替代品。
* [masscan](v)：功能强大且快速的端口扫描器。
* [nmap](https://formulae.brew.sh/formula/nmap#default)：权威的端口扫描器。

![brew search](https://cdn.thenewstack.io/media/2024/12/6ac15cf6-brew-search-apps.png)

### 创建公式

到目前为止，我已经从开发人员设置工作站的角度讨论了 Homebrew。但是，下一个逻辑点是已经完成项目并准备通过 Homebrew 分发项目的开发人员。
这个过程涉及许多步骤和几个Homebrew命令，但大致流程是从将Homebrew指向你的源文件开始。接下来，你将编辑配方文件，包括描述、许可证、依赖项等。为你的配方创建一个Tap（分发库），然后创建实际的配方并将其推送到你的Tap。

## Homebrew与Linux和Windows包管理器相比如何？

如果你已经熟悉Linux包管理器，那么Homebrew对你来说不会构成挑战。它提供了与大多数Linux包管理器相同的直观语法和类似的子命令，因此它很可能是一个轻松的过渡。Windows用户往往不像其他人那样经常使用命令行包管理器，所以可能需要一些时间来适应。但是，你很快就会沉迷于使用简单的`brew`命令查找和管理应用程序的便捷性。

从最常见的任务开始：安装、更新和清点应用程序。养成使用`list`和`info`子命令的习惯。在许多情况下，一个简单的`brew upgrade`命令就能使Homebrew管理的所有已安装应用程序保持最新。

请注意，如果你更喜欢它而不是DNF或APT之类的包管理器，Homebrew也可以在Linux上运行。你也可以在Windows子系统Linux平台下将其添加到Windows系统。如果你同时使用这三个主要平台（就像我一样），拥有一个单一的包管理器当然很方便。

## 总结

Mac系统是非常可行的开发平台，并且有许多IDE和其他支持软件包可供使用。在Homebrew出现之前，管理这些包是一个挑战。现在，查找和维护所需的软件变得简单而可预测。

在你为编码项目或系统/网络管理任务设置系统时，将Homebrew添加到你的Mac应该是第一步。即使是普通的家庭用户也能从轻松添加他们想要的应用程序并独立于App Store监督的能力中受益。

今天就使用简单的脚本安装Homebrew，并开始探索你需要的可用开发工具。你很快就会发现，使用这个强大的包管理器更容易找到这些工具并保持它们的最新状态。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。