
<!--
title: Warp 是 Linux 高级用户的梦想终端
cover: https://cdn.thenewstack.io/media/2024/10/ad5a3912-warpterminal.jpg
-->

Warp 的学习曲线略微陡峭，但一旦你掌握了它的工作原理，你就会发现它简直是终端的终极理想境界。

> 译自 [Warp Is a Power User's Dream Terminal for Linux](https://thenewstack.io/warp-is-a-power-users-dream-terminal-for-linux/)，作者 Jack Wallen。

我从 90 年代后期就开始使用 [Linux](https://thenewstack.io/learning-linux-start-here/)，这意味着很早我就不得不依赖 [终端窗口](https://thenewstack.io/tutorial-your-terminal-og-style-no-libs-or-plugins/)（因为当时的 GUI 远不如现在）。我对命令行非常熟悉，几乎所有 Linux 命令我都能在睡梦中运行。

但并非所有终端应用程序都是一样的。当然，许多 [Linux 终端](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/) 应用程序都提供配置文件和其他简单的功能，但是当您想要真正的强大功能和选项时，您会转向哪里？

在过去一年左右的时间里，我从内置终端应用程序切换到了一个名为 [Warp](https://www.warp.dev) 的新范例。这个应用程序是用 [Rust](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) 构建的，因此它的设计注重速度。然而，速度并不是 Warp 最令人印象深刻的部分，因为这个应用程序的功能远不止于此。

它有代理模式，该模式 heavily into AI，因此您可以使用简单的英语来完成多步骤的工作流程。例如，您可以输入“我想更新 Ubuntu”，Warp 将返回执行此操作的分步说明，甚至自动将初始命令添加到提示符中，因此您只需按键盘上的 Enter 键即可。

您甚至可以将此功能用于您当前的开发项目。您可能想知道哪些拉取请求导致了合并冲突，因此您可以输入“使用 GitHub CLI 找出导致此合并冲突的 PR”。

您甚至可以使用它进行故障排除，例如：“为什么我无法 SSH 到我的服务器？” Warp 将会提供如何开始故障排除的建议。

还有 Warp Drive，它添加了一个安全空间来保存和共享交互式笔记本和可重复使用的工作流程。例如，您可以通过添加带有命令 `sudo apt-get update && sudo apt-get upgrade -y` 的笔记本，来创建一个用于更新和升级 Ubuntu 机器的新工作流程。

创建工作流程后，您只需从 Warp Drive 中选择它，然后按键盘上的 Enter 键即可。工作流程将执行，一切就绪。Warp Drive 还允许您保存笔记本，其中几乎可以包含您想要的任何文本（无论是命令、代码片段、注释还是其他任何内容）。您还可以在 Warp Drive 中设置环境变量，甚至创建文件夹来存放相关内容。

Warp AI 是另一个非常有用的功能。例如，假设您需要运行一个命令，但您不确定该命令的作用。在 Warp 终端 CLI 中键入该命令，突出显示该命令，然后使用 Ctrl+` 键盘命令，Warp 的 AI 将会解释该命令的作用。

- Warp AI 可以轻松理解命令的作用。

除了这些功能之外，您还可以自定义 Warp 的外观，创建自定义提示符，将命令行固定到窗口的顶部或底部，甚至使用透明背景（以增加酷炫感）。Warp 使用类似现代 [IDE](https://thenewstack.io/best-open-source-ides/) 的编辑（因此您可以同时使用鼠标和光标），使用 [Vim 键绑定](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/)，支持 Tab 自动补全，并自动捕获命令中的类型错误或缺少的参数。

换句话说，Warp 是强化版的 Linux 终端。

当然，还有团队驱动器、会话共享和块共享，这些功能在免费版本中没有。

说到这里，Warp Drive 的免费版本（适用于 Linux 和 macOS，Windows 版本即将推出）将每个用户每月的 AI 请求限制为 100 次，只有一个个人 Warp Drive，最多三个笔记本，以及共享驱动器中的 10 个工作流程，所有离线功能以及通过公共论坛提供的免费支持。专业版（每月每用户 15 美元）将每个用户每月的 AI 请求增加到 1,000 次，并提供私人电子邮件支持。团队版（每月每用户 22 美元）增加了无限的 AI 请求、Warp Drive 中无限的共享笔记本和工作流程，以及实时会话共享。企业版（提供定制价格）允许您使用自己的 LLM，并增加了 OpenAI 零数据保留策略、基于 SAML 的 SSO、端到端加密和专属客户经理。

## 在 Linux 上安装 Warp

在 Linux 上安装 Warp 终端很简单。您只需下载 DEB（适用于基于 Ubuntu 的发行版）或 RPM 文件（适用于基于 Fedora 的发行版），打开默认终端窗口，然后运行以下命令之一：

*   Ubuntu – `sudo dpkg -i warp-terminal*.deb`
*   Fedora – `sudo rpm -i warp-terminal*.rpm`
对于 macOS 用户，请下载 .dmg 文件并像安装其他应用程序一样进行安装。对于 Windows 用户，您需要[注册等候名单](https://www.warp.dev/windows-terminal)，以便在 Windows 版本可用时收到通知。

正如我所说，我已经使用 Warp Terminal 大约一年了，我无法想象回到大多数[Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)中那种枯燥、缺乏功能的默认终端应用程序。Warp 的开发者们创造了市场上最好的终端应用程序，任何 Linux（或 macOS）用户如果不尝试一下都会感到遗憾。
