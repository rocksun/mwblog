
<!--
title: 如何将VS Code用于Python？
cover: https://cdn.thenewstack.io/media/2024/05/d5db76ac-getty-images-glhpcnwhrmm-unsplash-1.jpg
-->

为什么您应该使用 VS Code 进行 Python 开发？当然，所有功能。

> 译自 [How To Use VS Code for Python (and Why You Should)](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/)，作者 Jack Wallen。

自从我开始使用 [Python](https://thenewstack.io/guido-van-rossums-ambitious-plans-for-improving-python-performance/) 以来，我一直在使用 [Linux 操作系统](https://thenewstack.io/a-guide-to-linux-operating-systems-for-kubernetes/) 和 [终端窗口](https://thenewstack.io/off-the-shelf-hacker-embrace-the-linux-command-line/)。Nano 一直是我选择的编辑器，而且使用起来相当简单。但总有一些事情困扰着我：我认识的几乎每个开发人员都使用集成开发环境 (IDE) 来编写代码。这总是让我感到惊讶，因为当我在学校学习 [C++](https://thenewstack.io/c-on-the-move/) 时，我使用了相同的工具组合，部分原因是我买不起指导员建议的软件。最重要的是，我没有运行 Windows 的机器，而 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 没有为 Linux 提供其 IDE 的版本。

那是很久以前的事了，现在情况已经发生了很大变化。我不再受限于终端窗口，因为 Linux 有很多可用的 GUI 工具，其中一些是由 Microsoft 创建和分发的。

其中一个工具是 [Visual Studio Code](https://thenewstack.io/how-to-use-vs-code-as-your-python-ide/)，它也恰好是市场上最流行的 IDE 之一。事实上，VS Code 在 [PYPL 的顶级 IDE 索引](https://pypl.github.io/IDE.html) 中排名第二，仅次于 Visual Studio，市场份额为 13.51%。

所以我决定尝试使用 VS Code 和 Python，并很快发现这是一个绝妙的举动。

但为什么？当一个终端窗口和 nano 让我应付自如时，我为什么要费心使用更复杂的 GUI？让我先谈谈原因，然后我们再讨论方法。

## 你应该将 VS Code 用于 Python 的原因

从本质上讲，这一切都归结为功能。在 Linux 终端窗口（使用 nano）中编写 Python 并没有提供太多功能。当然，你可以获得语法高亮（这样你就可以知道何时遗漏了 ” a ‘ 或 a ），但这只是其中的一部分。你无法获得 IDE 中提供的自动缩进和其他有用的功能。

使用 VS Code 的另一个一大好处是为 Python 提供了丰富的扩展。你会发现用于调试、缩进、环境、预览、 [Django](https://thenewstack.io/what-is-pythons-django/)、 [Intellicode](https://thenewstack.io/top-5-code-completion-services/)（AI 辅助）、文档字符串生成、 [Jupyter Notebook](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) 支持等的扩展。要从命令行访问所有这些功能需要大量的工作。

事实上，在你超越 Python 学习的基础知识之前，你真的不需要任何这些功能。起初，我强烈建议坚持使用基于文本的编辑器和 Python 解释器。因为你正在处理基本代码，所以不需要 VS Code 提供的所有花里胡哨的功能。

但是，随着你获得更多 Python 经验，你可能需要迁移到像 VS Code 这样的 IDE。

考虑到这一点，让我向你展示如何开始使用 VS Code 和 Python。

## 你需要什么

我将在 Pop!_OS Linux 上演示此操作，但你也可以在 macOS 或 Windows 上安装 VS Code。对于这两个操作系统，安装就像下载安装程序文件、双击它并完成安装向导一样简单。

对于 Linux，这个过程有点困难。虽然你可以下载适用于 APT 和 DNF 包管理器的安装程序文件，但除非在发布最新版本时下载并重新安装，否则你不会收到自动更新。

考虑到这一点，让我们在 [Ubuntu](https://thenewstack.io/enable-automatic-updates-for-ubuntu-server/) 和基于 Fedora 的发行版上安装 VS Code。

## 在基于 Ubuntu 的发行版上安装 VS Code

首先要确保你的机器上安装了 wget 和 gpg。为此，发出命令：

```
sudo apt-get install wget gpg -y
```

接下来，我们下载官方 Microsoft GPG 密钥：

```
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
```

现在我们可以使用此命令安装密钥：

```bash
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
```

创建新的 apt 存储库条目：

```bash
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
```

使用此命令安装必要的依赖项：

```bash
sudo apt install apt-transport-https -y
```

更新 apt:

```bash
sudo apt update
```

最后，用此命令安装 VS Code：

```bash
sudo apt install code -y
```

## 在基于 Fedora 的机器上安装 VS Code

安装所需的密钥：

```
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
```

创建 dnf 存储库条目：

```bash
echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null
```

更新 dnf：

```bash
dnf check-update
```

安装 VS Code：

```
sudo dnf install code -y
```

安装好 VS Code 后，从桌面菜单中打开它，然后逐步完成用户友好型入门向导。

## 启用 Python 支持

下一步是启用 Python 支持。为此，请单击侧边栏中的扩展图标（看起来像一个小 Tetris 图标，位于栏的中间附近）。在结果菜单中，键入 python 并等待结果。单击与官方 Python 扩展关联的安装按钮。它应该是顶部结果（请参阅下图）。

![](https://cdn.thenewstack.io/media/2024/05/4323e724-vscode1.jpg)

扩展安装好后，你可以滚动浏览剩余的结果并安装其他任何你可能需要的 Python 相关扩展。完成这些操作后，你可以在计算机上打开一个包含现有 Python 代码的文件夹（选择 File > Open Folder）。你的文件会列在左侧边栏中。打开其中一个文件并继续使用该文件。例如，我将打开我类型转换教程中的一个文件。代码将出现在编辑器中。我之后可以单击“运行”按钮（指向右边的箭头，位于窗口的右上方）。在编辑器下方会打开一个窗格，并且代码将运行。

未在前面提到的另一个额外好处是 VS Code 可快速访问选定文件夹中找到的所有文件。你不必记住自己创建的内容的名称并手动将其打开。这是一个微小的附加功能，但可以显著提高效率。

如果你已经开始熟悉 Python，我强烈建议你在其中添加一个类似于 VS Code 的 IDE。你将享受到它带来的附加功能和效率。