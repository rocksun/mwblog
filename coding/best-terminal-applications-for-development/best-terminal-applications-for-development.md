
<!--
title: 告别低效！程序员必备的终端神器，你用过几个？
cover: https://cdn.thenewstack.io/media/2025/02/eb39c4b7-douglas-lopes-ehyv_xoz4ia-unsplash-1.jpg
-->

对于许多老派开发者来说，终端才是他们的最爱——你得把它从他们冰冷的手指中撬出来才行。

> 译自 [Best Terminal Applications for Development](https://thenewstack.io/best-terminal-applications-for-development/)，作者 Jack Wallen。

虽然大多数开发人员喜欢在[集成开发环境 (IDE)](https://thenewstack.io/best-open-source-ides/)中工作，但也有一些人更喜欢在终端窗口中工作的效率、简洁性和速度。使用终端窗口，您可以访问 nano、vi 和 Emacs 等编辑器，以及 [Python](https://thenewstack.io/my-ai-python-coding-test-surprising-results/)、GCC、Make 等标准开发工具。

对于许多老派开发人员来说，终端就是一切——你必须从他们冰冷、僵硬的手中夺走它。

是的，终端用户可能对他们选择的工具非常认真。

终端应用程序重要的另一个原因是，它们允许您远程连接到另一台机器，并像在本地一样工作。借助 SSH，您可以进入，并可以访问该远程机器上的所有命令行工具。

所以终端非常棒——但是有很多终端应用程序。从如此众多的应用程序中，哪些更适合开发人员？

让我们深入挖掘并找出答案。

## 1. Warp

我将从市场上两个更花哨的终端应用程序开始讨论，第一个是 [Warp](https://www.warp.dev)。实际上，我已经将 Warp 设置为我在 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 和 macOS 上的默认终端窗口，因为它太令人印象深刻了。Warp 不仅具有通常的 UI 功能（例如选项卡、拆分窗格和对大多数 shell 的支持），而且还具有一些非常重要的现代功能，例如内置 AI（包括 Agent Mode，使您可以用自然语言输入您想做的事情——Warp 将返回所需的命令）和 Warp Drive，它允许您创建可以重用的代码片段集合，甚至添加工作流程（可以保存和共享的模板化命令）。对我来说，Warp 最好的部分是内置 AI。如果我正在尝试弄清楚如何在 Python 中做某事，但解决方案让我难以捉摸，我可以使用 Warp AI 来帮助我弄清楚。

Warp 可以在 Linux、macOS 和 Windows 上免费安装和使用。您还可以购买以下三种许可证之一：

- Pro（15 美元/用户/月），每月最多可获得 1,000 个 AI 请求、无限接受的“下一步命令”建议、高令牌限制和私人电子邮件支持。
- 团队（22 美元/用户/月），增加了无限的 AI 请求、最高的令牌限制、无限的共享笔记本和工作流程，以及无限的实时会话共享。
- 企业（自定义定价），允许您使用自己的 [LLM](https://thenewstack.io/llm/)，并增加了 OpenAI 零数据保留策略、基于 SAML 的 SSO 以及通过 Slack 提供入职支持的专门客户经理。

## 2. Windsurf

我最近为 [The New Stack](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) 介绍了 [Windsurf](https://windsurfai.org/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)，发现它是一个非常出色的工具。这个终端应用程序的最大特点是它是第一个“代理 IDE”。为了实现这一点，Windsurf 利用 Codeium 自动完成工具，并为 70 多种 [编程语言](https://thenewstack.io/programming-languages/) 提供代码建议和完成。Windsurf 真正让我印象深刻的是它在帮助我编写 Python 脚本方面的出色表现，甚至可以从同一个 AI 聊天中构建脚本。这令人印象深刻……*真的*令人印象深刻。

Windsurf 还包括工作区、流程、多文件编辑、显式操作的自动推理、自然语言集成和强大的上下文引擎等功能。Windsurf 甚至包括用于测试您的应用程序的“运行”和“调试”操作。

Windsurf 可以在 Linux、macOS 和 Windows 上免费安装和使用。

## 3. Terminator

现在，我们进入了更传统的终端应用程序领域。[Terminator](https://gnome-terminator.org) 是一个非常流行的开源 Linux 终端，它基于 [GNOME](https://thenewstack.io/voyager-linux-offers-a-user-friendly-customized-gnome/) 终端应用程序。但是，是什么让 Terminator 比一般的终端更好呢？首先，它允许您创建多窗格窗口，因此您可以有效地使用所需的任意数量的终端应用程序，同时一次查看所有这些应用程序。当然，屏幕的大小将决定您可以一次打开多少个窗格（并且仍然能够有效地使用它）。使用此功能，您可以打开一个终端用于编写和编辑代码，一个用于编译，一个用于运行脚本，一个用于远程工作。（可能性是无限的。）其他功能包括选项卡、自定义布局、高级命令历史记录、脚本支持、其他终端的模拟、增强的键盘支持、系统托盘集成、主题、插件支持、对各种文件类型的支持、语法突出显示、命令自动完成、彩色输出格式和跨平台兼容性。另一个非常酷的功能是，它允许您对终端进行分组并同时在所有终端中键入。

Terminator 可以在 Linux、macOS 和 Windows 上免费安装和使用。

## 4. Guake

[Guake](https://github.com/Guake/guake) 是一种特殊的终端，因为它保持隐藏状态，直到您使用键盘快捷键将其调出。当您召唤此终端时，它会从显示器的顶部滚下来，以便您可以根据需要使用它。将其发送回上方并从视线中移开，然后进行其他工作。当您需要返回代码时，请点击相同的快捷方式，Guake 就会重新出现，因此您可以执行所需的操作。我将 Guake 添加到此列表的原因是它非常方便，而且它允许进行大量自定义。例如，您可以更改其主题、高度、宽度、外壳、自定义键盘快捷键、创建钩子等等。至于内置的编程功能，您不会找到任何功能，因为这是一个直接的终端应用程序。但是鉴于 Guake 的便利性，我认为它必须在列表中。

您可以在大多数 Linux 发行版上免费安装 Guake。

## 5. Contour

[Contour](https://github.com/contour-terminal/contour) 是对标准终端应用程序的现代改进，旨在用于日常使用，但主要面向高级用户。Contour 具有许多功能，例如 GPU 加速渲染、字体连字支持、Unicode 表情符号支持、选项卡、粗体和斜体字体、高 DPI 支持、垂直线标记、类似 vi 的输入模式、Windows 10 和 KDE Plasma 和 GNOME 桌面环境的模糊背景支持、运行时配置重新加载、真彩色支持、按键绑定自定义、语法突出显示、主题等等。使用 Contour，您甚至可以模拟其他终端，例如 GNOME Terminal 和 Xterm。

但是，为什么需要一个相当简单的终端窗口呢？一个原因是它如何处理终端仿真。如果您需要从不同类型的终端中测试应用程序，Contour 可以轻松实现。而且由于 Contour 可以与其他应用程序（例如文件管理器甚至 IDE）集成，因此它成为程序员的可行选择。

Contour 可以在 Linux、macOS 和 Windows 上免费安装和使用。
