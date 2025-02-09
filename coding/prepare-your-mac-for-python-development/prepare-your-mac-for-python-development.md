
<!--
title: 为Python开发准备您的Mac
cover: https://cdn.thenewstack.io/media/2024/09/8a15b6c4-python.png
-->

在你的Macintosh上安装Python可能有些棘手。以下是如何安装Parallels和Homebrew，并搭建最佳开发环境。

> 译自 [Prepare Your Mac for Python Development](https://thenewstack.io/prepare-your-mac-for-python-development/)，作者 Damon M Garn。

我出于乐趣涉猎 [Python](https://thenewstack.io/what-is-python/) 开发领域，最近，我决定使用一个专用环境来更认真地对待它。虽然我考虑过新的 [Raspberry Pi 5](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/)（并且可能仍然会买一个！），但我决定在我的 MacBook Pro 上使用一个专用的 Parallels 虚拟机来保持本地化。Mac VM 镜像可以通过 Parallels 获得，因此安装非常简单。

本文的其余部分介绍了我的后续步骤，应该可以帮助任何对在 macOS 上设置一个有用但简单的 [Python3 开发环境](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) 感兴趣的人。请记住，某些软件选择是基于我自己的偏好。请随意做出自己的选择。我对 [Vim](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/) 的强烈偏好可能是最具争议的选择。

## MacOS 和 Python

我会在力所能及的地方提供具体的命令，并在其他情况下提供建议。诚然，其中一些主题是基本的常识和最佳实践（例如管理软件更新）。

### 设置我的 Mac

花几分钟时间按照你喜欢的方式自定义 macOS。创建一个高效且舒适的用户界面对于设置一个与你合作而不是与你作对的环境至关重要。

以下是一些常见的设置：

- 通过删除 Apple 默认添加的（许多）应用程序来清理 Dock。将 Dock 减少到你经常使用的应用程序。将你稍后在此列表中安装的程序添加进去，以便于访问。
- 设置一些鼓舞人心的壁纸。我使用 Python 图标来激励自己。
- 配置至少两个 [Spaces](https://support.apple.com/guide/mac-help/work-in-multiple-spaces-mh14112/mac)。如果你从未使用过 Spaces，这是最有用的 macOS 效率工具之一。Spaces 是存在于屏幕外的虚拟桌面。你可以在它们之间快速切换，并在每个桌面上打开特定的应用程序。我在我的 Mac 上使用四个 Spaces。
- 调整显示设置、字体大小和其他视觉设置以符合你的偏好。
- 将触控板和键盘设置调整到你的口味。围绕这两个设备有几个效率选项，因此请务必研究这些选项。我使用高分辨率的多个显示器，所以我增加了指针的大小，以便更容易在如此广阔的视觉区域中找到它。

我更喜欢 Chrome 而不是 Safari，所以我也在此时切换浏览器。

我使用云存储来存储我的大部分业务文档，但我也运行定期的 Time Machine 备份。为你的工作设置一个备份例程。

最后，我更新 macOS 和当前安装的任何应用程序，以确保我拥有最新的功能和安全更新。请务必定期执行此操作！

你应该有自己的 macOS 偏好，但也许这些想法会给你带来新的想法。

### 安装 Parallels Tools

我的 macOS/Python 平台是一个虚拟机。我使用 [Parallels](https://www.parallels.com/) 来托管我用于业务的各种 Linux 和 macOS 虚拟机。你可以选择另一个虚拟化平台，在物理 Mac 上管理你的 Python 项目，或者使用非 Apple 平台（如 Linux）。

一旦我创建了我的 macOS/Python VM，我就会添加 Parallels Tools 以确保高效的通信。这不需要是一个非常强大的 VM，因为大多数 Python 应用程序都相当小，尤其是在刚开始时。

### 安装 Homebrew

很少有通用实用程序能像 Homebrew 包管理器那样有用。Linux 用户已经熟悉像 [DNF 和 APT](https://thenewstack.io/how-to-manage-linux-software/) 这样的包管理器，但如果你是这种软件管理方法的新手，请准备好留下深刻的印象。包管理器使你能够快速轻松地安装应用程序。Homebrew 还允许你安装 Apple App Store 上不可用的软件。并非所有开发人员都想屈服于 Apple 的严格要求，也并非所有软件都已准备好进入 App Store。

通过在终端中键入以下命令来安装 [Homebrew](https://thenewstack.io/homebrew-for-macos-developers/)：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 增强终端

在开发程序时，你可能会在命令提示符下花费大量时间。虽然 GUI 工具很棒，但有时 CLI 是更好的选择。Apple 内置的终端应用程序是可以容忍的，但还有其他选择。我最喜欢的是 [iTerm2](https://iterm2.com/)。这个高度可定制的终端替代品提供了许多实用的功能——太多了，无法在此处一一列出。

看看这些突出的选项，让你开始使用 iTerm2：

- 拆分窗格视图。
- 广泛的搜索功能。
- 自动完成选项。
- 各种项目的可定制配置文件。（想象一下一个用于 Python 开发的配置文件，另一个用于文件管理任务。）

为了获得额外的加分，可以考虑使用 [Oh-My-Zsh](https://ohmyz.sh/) 框架增强 iTerm2，以进一步自定义您的 shell 环境。

### 更新 Python3

最新的 macOS (Sequoia) 包含 Python 3.9.6。但是，您真的应该将您的 Python 版本更新到最新版本，以解决旧的 Apple 版本中的错误修复。打开终端并键入 `python3` 以查看当前版本。它可能是 Python3 3.9.6 —— 与我撰写本文时最新的 3.13.1 版本相比，已经过时了。

![](https://cdn.thenewstack.io/media/2025/02/9fdd54fb-python-3-9-6old.png)

*Python 3.9.6 已经严重过时了。*

Homebrew 维护了对 Python3、Python 模块、PIP 包管理器和其他必要组件的广泛包支持，所以我使用它来更新我的 Python。

以下是基本的 Homebrew 命令：

```
brew update
brew install python3
brew link python3
```

这些命令应该会自动将
`/opt/homebrew/bin/` PATH 变量添加到
`.zshrc` 文件中，但是您需要运行
`source` 命令（或注销并重新登录）来更新会话。
如果您现在键入 `python3`，您应该会看到更新后的版本。

![](https://cdn.thenewstack.io/media/2025/02/d7023a84-python-3-13-1new.png)

考虑定期运行 `brew upgrade python3` 以保持最新版本。

### 花时间使用 IDLE

您应该已经可以访问默认的 Python3 编辑器 IDLE。您可以从终端或启动台中访问它。

IDLE 是一个很好的基本编辑器，Python3 包含它很好。但是，我正在寻找更强大的东西。

### 安装 PyCharm Community Edition

我并不反对 IDLE IDE，但我想使用 JetBrains 的 [PyCharm Community Edition](https://www.jetbrains.com/pycharm/) 来处理 Python。[下载 .dmg 文件](https://www.jetbrains.com/pycharm/download/?section=mac)（滚动到页面底部找到 Community Edition），然后将 PyCharm CE 图标拖到 macOS 应用程序文件夹中。就是这样 —— 一个典型的简单的 Mac 程序安装。

根据您的喜好自定义 PyCharm CE 用户界面主题，并添加您喜欢的任何插件。PyCharm 还支持各种其他语言，并包含一个新的 AI 支持功能供您探索。对于 Python 和 PyCharm 的新手，IDE 包含一个 40 节课的教程，可帮助您入门！

![](https://cdn.thenewstack.io/media/2025/02/d7f3000a-pycharmce.png)

*考虑使用 PyCharm CE IDE 来开发你的 Python 项目。*

### 安装和自定义 Vim

它可能看起来很古老，但我非常喜欢 [Vim 文本编辑器](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/)。没有什么比一个基本的文本编辑器更能让你在没有古怪的图标和 10,000 个专门功能干扰的情况下完成工作了。作为一名作者，我经常只需要将文字写在纸上（或者在这种情况下是屏幕上），而 Vim 非常出色地完成了这个任务。

编码就是一个很好的例子。Vim 提供 Python3 语法高亮、自动缩进和代码折叠，以简化您的编码体验。要在 Vim 启动时自动加载这些选项，我编辑 `~/.vimrc` 文件并添加以下内容（使用 `"` 作为注释行）：

```
" Syntax checking
syntax on
" Line numbering
set number 
" Highlight cursor line
set cursorline
" Indention
filetype indent on
" Folding
set foldmethod=indent
set foldlevel=99
```

![](https://cdn.thenewstack.io/media/2025/02/afc63837-vimrc.png)

*我的最初经过略微定制的.vimrc文件*

存在许多其他有用的设置，但这些对我来说是一个好的开始。许多人已将他们高度自定义的 .vimrc 配置文件放在网上供参考。其中一些配置文件是专门为 Python 开发而调整的。

![](https://cdn.thenewstack.io/media/2025/02/e64f6c25-pythonvim.png)

*带有Python语法高亮和行号的Vim*

存在许多特定于 Python 的 Vim 插件，以进一步扩展 Vim 作为 IDE 的功能。如果您决定深入研究，请考虑使用插件管理器。

### 添加 CotEditor

我最近最喜欢的 macOS 应用程序是 [CotEditor](https://coteditor.com/)。我需要一个基本的 GUI 文本编辑器来替换 VS Code。我想要一些简单、图形化且（如果可能）开源的东西。我找到了 CotEditor。到目前为止，这个工具非常棒，而且正是我所需要的。您可能会或可能不会直接将其用于编码，但它非常适合 Markdown 文档或其他基本编辑项目。

![](https://cdn.thenewstack.io/media/2025/02/b610da62-coteditor.png)

*CotEditor是一款出色的文本编辑器。*

### 为 Python3 项目设置 venv

[Python 虚拟环境](https://docs.python.org/3/library/venv.html) 帮助避免依赖地狱。你的各种项目可能需要不同的模块，甚至不同的 Python 版本。在系统范围内管理这些严格的要求将具有挑战性，因此 Python 使用[虚拟环境](https://thenewstack.io/why-every-python-dev-needs-virtual-environments-now/) (venv)。安装在 venv 中的模块和其他组件受其边界限制，不会影响其他 venv。我通常为每个 Python 项目创建一个新的 venv。你将在从一个项目切换到另一个项目时激活和停用虚拟环境。

为名为“new-app”的项目创建和激活 venv 的基本过程是：

```bash
mkdir new-app
cd new-app
python3 -m venv .venv
source venv/bin/activate
```

最佳实践是将虚拟环境命名为“venv”、“env”或“.venv”。

## 总结

你现在可以开始在 Mac 上构建 Python 项目了！正如一开始提到的，其中一些工具和偏好是我自己的选择，因此只需选择你喜欢或感兴趣的工具和偏好，忽略其他的即可。

Mac 是很棒的开发平台，使用虚拟机是试验不同工具和选项的便捷方式。立即开始使用 macOS 和 Python 吧！
