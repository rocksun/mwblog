<!--
title: 我在真实 Python 代码库中测试了 OpenAI Codex 新功能：Claude Code 目前最强对手
cover: https://cdn.thenewstack.io/media/2026/05/d32adedb-beatriz-camaleao-d0qgevtqb0w-unsplash-scaled.jpg
summary: 本文通过对 Python 代码库 HTTPie 的实测，评估了 OpenAI Codex 的应用内浏览器、计算机使用及 PR 审查等新功能。结果显示其具备极强的代码理解与修复能力，已成为 Claude Code 的有力竞争者。
-->

本文通过对 Python 代码库 HTTPie 的实测，评估了 OpenAI Codex 的应用内浏览器、计算机使用及 PR 审查等新功能。结果显示其具备极强的代码理解与修复能力，已成为 Claude Code 的有力竞争者。

> 译自：[I tested the new OpenAI Codex features on a real Python codebase, and it's the strongest Claude Code rival yet](https://thenewstack.io/openai-codex-claude-code/)
> 
> 作者：Jessica Wachtel

上个月底，[OpenAI 发布了一款新产品](https://thenewstack.io/openai-workspace-agents-gpt-5-5/)，他们称之为“（几乎）适用于一切的 Codex”。其目标是将 [Codex](https://thenewstack.io/openais-codex-is-now-on-windows/) 从一款代码编辑产品转变为通用工具。

“（几乎）适用于一切的 Codex” 发布的功能包括计算机使用、应用内浏览器、PR 审查、连接远程开发机的 SSH 以及 90 多个新插件。每周有超过 300 万开发者使用 Codex，其中许多人可能在第二天早上打开应用时并未察觉到任何变化。

我注意到了。现在我有一些看法。

## 设置

我花了一天时间，针对我在[这篇文章中测试 Cursor 3 和 Claude Code](https://thenewstack.io/cursors-agents-window-vs-claude-code/) 时使用的同一个真实代码库测试了三个重要的新功能（但测试的是不同的 Bug）。测试代码库是 HTTPie，一个用于发起 HTTP 请求的热门开源 [Python](https://thenewstack.io/python/) [命令行界面 (CLI)](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) 工具。

我在 [Codex 桌面应用](https://openai.com/codex/)上运行了测试。通过我的 OpenAI 账号，我可以访问其所有新功能。我使用的是免费版本。计算机使用功能需要 Mac 以及特定的系统权限（稍后详细介绍）。

## Codex 应用内浏览器

这是我最期待测试的功能，因为它彻底改变了提示词工作流。我没有将 Bug 描述复制粘贴到聊天框中，而是直接在 Codex 内部打开了 GitHub Issue，并让智能体指向它。浏览器是一个插件，因此在文本框的初始弹出菜单中没有浏览器选项。你需要在选择插件选项后找到它。是的，这让我困惑了一下。不，我不想谈论这件事。

我在应用内浏览器中打开了 [GitHub issue #1665](https://github.com/httpie/cli/issues/1665) 并输入：

*“我在浏览器中打开了 GitHub issue。请阅读它并修复其中描述的 Bug。”*

我对接下来发生的一切非常满意。页面以分屏布局打开，就在聊天界面旁边。

> Codex 不仅理解当前的任务，还理解代码库本身。

Codex 在 3 分钟内修复了它。它阅读了 Issue，将 Bug 追踪到代码库中的三个文件，编写了修复程序，添加了回归测试，并运行了相关的测试。它还注意到 `downloads.py` 中有我之前测试时留下的无关更改，并明确保持其未动。这让我意识到 Codex 不仅理解当前的任务，还理解代码库本身。

## Codex 计算机使用功能测试

计算机使用是一项重大功能。Codex 现在可以查看你的屏幕、移动自己的光标、点击以及在你 Mac 上的应用中输入内容。对于授予 Codex 这么多权限，我心情复杂，但为了这篇文章，我愿意尝试一下。

> 拥有不受限终端访问权限的编程智能体是一个安全风险。

我授予了屏幕录制和辅助功能权限，并要求 Codex 打开终端，导航到 HTTPie 仓库，并免操作修复同一个 Bug。Codex 立即标记出 Terminal.app 在此会话中被禁止使用计算机功能，理由是安全原因。它改为使用其内置的 shell 完成了任务。我认为这种限制是最好的。[拥有不受限终端访问权限的编程智能体是一个安全风险](https://thenewstack.io/securing-ai-agent-systems/)。

我转向了一个风险较低的任务。我要求 Codex 打开访达 (Finder)，导航到项目文件夹并截屏。它正确地导航了文件夹，但截屏失败了。它生成了一个文件夹内容的文本渲染，并承认了局限性。不过，文本渲染是很准确的。

计算机使用是真实存在的，它适用于 GUI 任务，例如运行桌面应用、执行基于浏览器的流程以及视觉 UI 测试。对于重度依赖终端的开发者工作流，我不推荐它。对于前端开发者测试 UI 流程或操作桌面应用，它可能被证明更有益。

## Codex 拉取请求 (PR) 审查测试

为了这个测试，我将一个修复了 Bug 的分支推送到我的 GitHub fork 中，并要求 Codex 审查该 PR。Codex 阅读了拉取请求，确认修复在概念上是正确的，并引用了相关的 urllib3 和 Requests 文档来支持其评估。然后它运行了特定的回归测试，并指出测试覆盖率中存在一个真正的缺口。它说，模拟测试没有端到端地运行真实的 gzip 流，并建议进行后续的集成测试。

由于端口绑定限制，沙箱再次阻止了完整测试套件的运行。这在我测试过的所有工具中都会出现，这也是沙箱化智能体环境的一个真实局限。

它并不完美，但起作用了。PR 审查阅读了真实的 GitHub PR，引用了文档，执行了测试，并给出了可操作的反馈。

Codex 现在不仅仅是我们过去一年中所了解和喜爱的标准编程智能体。尽管仍有改进空间（说的就是你，计算机使用功能），但它是目前 [Claude Code 最完整的替代方案](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/)。