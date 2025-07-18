<!--
title: Q&A：Warp 2.0对比Claude Code和Gemini CLI
cover: https://cdn.thenewstack.io/media/2025/07/3b61d180-allison-saeng-dn2xkz36ciw-unsplashb.jpg
summary: Warp CEO Zach Lloyd 讨论了 Warp 2.0 的“代理式开发环境”，包括代码编辑器、AI 功能、平台无关性、Rust 的选择以及 MCP 集成。Warp 致力于为专业开发人员提供管理和审查代理编写代码的工具。
-->

Warp CEO Zach Lloyd 讨论了 Warp 2.0 的“代理式开发环境”，包括代码编辑器、AI 功能、平台无关性、Rust 的选择以及 MCP 集成。Warp 致力于为专业开发人员提供管理和审查代理编写代码的工具。

> 译自：[Q&A: How Warp 2.0 Compares to Claude Code and Gemini CLI](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/)
> 
> 作者：David Eastman

几周前，[AI 终端应用 Warp](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/)发布了其 [2.0 版本产品](https://www.warp.dev/blog/reimagining-coding-agentic-development-environment)，并称之为“代理式开发环境”。我将在短期内评测这款产品，但与此同时，我对 Warp 的 CEO [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/) 进行了一次邮件采访。我一直是 Warp 的忠实粉丝（和用户），主要是因为它是一个适用于所有操作系统的优秀终端。

虽然终端中的 AI 辅助功能很有用，但似乎随着所有主要的 LLM 都在争相进入代码编辑器，AI 最终将从命令行中抽离——直到 [代理式时代](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/) 来临。Warp 似乎很适合利用代理式 AI，因为 [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) 驻留在你陈旧的终端应用程序中。所以我有很多问题想问 Zach。

**David：我注意到 Warp 2.0 的第一件事是它现在有了自己的代码编辑器。我知道它只是为了快速而粗糙的 hacking，但是团队内部创建 Warp 代码编辑器的愿望有多强烈？**

**Zach:** 我们的理念是，手动编写代码的情况会越来越少，并且随着时间的推移会完全消失，但现在，肯定仍然有你需要跳进去进行手动更改的时候。

Warp 中的代码编辑器不是为从头开始编写代码而设计的。我们关注的主要用例是人工审查代理编写的代码。虽然大多数时候人们根本不需要在 Warp 中使用代码编辑器，但当他们需要时，我们认为人类有两种主要的干预方式：一种是重新提示代理，另一种是直接编辑代码。

> “我们的理念是，手动编写代码的情况会越来越少，并且随着时间的推移会完全消失。”
> 
> **– Zach Lloyd, Warp CEO**

因此，编辑器的目标是确保你不必为了进行小的更改而切换出 Warp。我们希望将编辑功能做得足够好，使其在该工作流程中可用且方便，而无需跳转到单独的 IDE。

**David：它非常简洁，这很好。你打算给它多少功能？**

**Zach:** 你说得对，我们的编辑器是有意设计的简洁。这是出于设计考虑。我们不是要重新创建一个功能齐全的 IDE。但我们确实计划添加我们认为基本编辑所需的表级功能：例如保存时格式化、linting、简单的 LSP 支持——只需足以使体验在你需要时顺畅即可。

也就是说，与其他工具（如 [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)、[Codex CLI](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/) 或 [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/)）相比，我们在 UI 方面具有真正的优势。这些产品根本无法构建 WYSWYG 编辑器——更不用说出色的代码审查体验了。

**David：你已经让脾气暴躁的开发人员接触 LLM 有一段时间了，但即使现在人们仍然会问“我为什么需要在终端中使用 AI？” 你是否想发布一个 Warp Classic 版本，删除 LLM 方面，从而留下一个更干净的终端？**

**Zach:** 我们最终确定的解决方案非常简单：在 Warp 的设置中有一个简单的切换开关，你可以直接关闭 AI。它会从 Warp 中删除所有 AI 功能。我们认为我们不需要制作一个完全独立的应用程序，它只是一个没有 AI 的终端，因为如果用户愿意，可以轻松禁用它。

但就我个人而言，我真的相信 Warp 是一个令人难以置信的 AI 工具；如果你不使用 AI 功能，你就是在限制自己作为开发人员的能力。我们知道并非每个人都能立即看到这一点，因此我们面临的真正挑战是帮助用户达到顿悟时刻。一旦他们做到了，他们通常就不想回去了。

> “……如果你不使用 AI 功能，你就是在限制自己作为开发人员的能力。”

最常见的情况是，当有人在终端中遇到错误时，Warp 会为他们修复错误——例如你的 Python 依赖项搞砸了，或者你陷入了调试 Docker 问题的困境，而 Warp 会介入并解决它。我想继续让即使是 AI 怀疑论者也有机会遇到这些时刻；因为当他们这样做时，它真的可以改变他们的工作方式。

**David：在 LLM 创建者将操作移回云端之前，你将如何最大限度地利用这个 ADE [代理式开发环境] 时刻？**

**Zach:** 是的，这真的感觉像是我们的时刻。时代思潮正在转向基于终端的编码代理——这是与传统 IDE 的重大转变。这是因为人们开始意识到终端界面的价值。无论是 Warp 的 ADE、Claude Code、Codex、Gemini CLI 还是其他工具，拥有基于时间的日志和命令式界面的想法——你只需告诉代理你想要什么，它就会执行——正在成为使用 AI 的最佳方式。

这比尝试在 VS Code 克隆中的侧面板或聊天窗口中使用更流畅的体验。相比之下，这些设置感觉很笨拙，并且针对与代理交互而优化的整个屏幕效果更好。

自从推出 ADE 以来，我们看到每日付费注册量增长了约 5 倍——即使考虑到折扣——因此这种吸引力是真实存在的。

> “……拥有基于时间的日志和命令式界面的想法——你只需告诉代理你想要什么，它就会执行——正在成为使用 AI 的最佳方式。”

最疯狂的是，大多数专业开发人员仍然没有改变他们的工作流程——今天尝试代理工具的人主要是业余爱好者、氛围编码者或 AI 早期采用者。我们的重点是为专业人士构建——开发人员在真实的代码库上工作——并为他们提供管理、编辑和审查代理编写的代码的正确工具。这需要比典型的终端应用程序更深入的界面。

这就是为什么成为外部平台——完全控制 UI——是如此优势的原因。我们现在真的是独一无二的，因为我们是唯一不是 VS Code 克隆或 CLI 包装器的专用代理平台。

至于操作是否会移回云端——如果问题是我们是否会支持像 Devin 或 Factory 这样的基于云的代理，我想我们可能会支持。但前提是我们能够使本地和远程之间的转换感觉无缝。这是我们追求的目标。

**David：随着代理线程变得疯狂，可能会越来越需要令牌使用监控和过程监控。你打算如何保持 Warp 的 UI 优势？**

**Zach:** 是的，我们在这里绝对有优势，因为我们有一个非常好的 UX 来管理代理多线程。

随着人们开始一次运行更多代理，成本可能会迅速攀升。我们听到的一个主要反馈是 Warp 感觉“对令牌需求很高”，因此我们正在进行一项重大的工程工作，以使其更有效率，同时又不牺牲质量。这包括优化我们用于不同任务的模型，并可能提高限制，以便用户不会很快达到这些限制。

> “随着人们开始一次运行更多代理，成本可能会迅速攀升。”

在 UI 方面，我们拥有比 CLI 应用程序更大的优势，它具有完全原生的代理管理层——包括系统通知、标签内更新和用于跟踪所有代理的统一视图。我们将继续推动这一点，并使代理管理成为应用程序中更中心、更重要的一部分。虽然今天的 UI 仍然相当简洁，但它已经提供了一种更好的方式来查看、控制和干预——这是只有 Warp 才能做到的，因为它在堆栈中的位置。

**David：现在 Warp 可以在 Linux、Mac 和 Windows 中运行，你是否正在缓慢（或快速）失去你最初的 Mac 优先创业心态？**

**Zach:** 是的，我们肯定会尽量做到平台无关。我们大多数人都是在 Mac 上开始的，并且仍然每天在 Mac 上工作，但我们也有团队成员每天在 Windows 和 Linux 上使用 Warp。

我实际上认为我们在 Windows 上有很大的优势。据我所知，像 Claude Code、Codex 和其他基于 CLI 的设置在 PowerShell 中实际上不起作用——你几乎需要 WSL。因此，如果你是一名 Windows 开发人员，并且想要在没有 WSL 的情况下进行代理式开发，那么 Warp 确实是唯一不错的选择。我们绝对希望继续努力使 Warp 在所有平台上都很棒。

**David：Rust 是否在帮助你保持你想要的任何地方的速度？我注意到新的 [Ladybird 浏览器](https://thenewstack.io/ladybird-that-rare-breed-of-browser-based-on-web-standards/) 选择了 Swift 而不是 Rust。**

**Zach:** Rust 一直是一个相当不错的选择。我们早期研究了带有 Electron 的 Web 技术，我认为跨平台桌面开发基本上有两个不错的选择：Rust 或 Electron。

毫无疑问，Electron 的最大优势是更快的开发时间。有更多的库和更大的生态系统，因此你必须重建的更少。但我们最终选择了 Rust，因为我们想要更高的性能和更多的控制。在 Web 沙箱中进行开发可能很痛苦——使用 Rust，我们可以获得真正的线程、直接内存访问和更深入的系统集成。你可能可以使用 Electron 来完成其中的一些工作，但这会麻烦得多。我也认为 Rust 总体上更快。

> “我们最终选择了 Rust […] 因为我们想要更高的性能和更多的控制。”

我对 Ladybird 或他们为什么选择 Swift 而不是 Rust 知之甚少，但我的理解是，使用 Swift 进行跨平台仍然是一种研究项目，而不是真正可以用于生产的东西。我认为其他团队已经尝试过，但它还没有真正起飞。因此，对我们来说，选择像 Rust 这样真正为跨平台而构建的东西更有意义。

**David：MCP 似乎是 Warp 的一个自然出路，但到目前为止，它在大多数平台上仍然感觉是实验性的——而且有点尴尬。在控制和 UI 方面，Warp 是在加入 MCP 还是在等待看看它是如何流行的？**

**Zach:** 我已经将我们的崩溃报告工具 Sentry 连接到 Notion，它可以让我做一些事情，比如告诉 Warp，“嘿，修复这个 Linear 问题”，然后粘贴一个 Linear 链接，或者“帮助我调试这个服务器崩溃”，然后粘贴一个 Sentry 链接。

我们完全倾向于 MCP。它真正为 Warp 发光的地方是当 CLI 集成不存在时。位于终端层的一个强大之处在于，我们的首选始终是：是否有可以收集上下文的 CLI 工具？如果有，我们将调用它，因为它更快、更原生。

例如，当我们可以运行 Git 命令时，我们不会使用 Git MCP 服务器，并且我们将始终首选 GitHub CLI 而不是使用 GitHub MCP 服务器。基本上，如果有一个好的 CLI，我们将使用它。

但是对于许多工具来说，没有可靠的 CLI——像 Notion 或 Linear 这样的工具就是很好的例子。对于这些工具，拥有一个超级简单的 MCP 集成确实打开了很多上下文。

我们绝对在加入 MCP。我们正在大力投资，使其更易于安装、更易于共享和更易于调试。

## David 的结语

无论你是否支持 LLM 辅助开发（正如 Zach 所说，许多专业开发人员绝对没有改变他们的工作流程），Zach 的见解都应该帮助你了解为什么代理式开发人员在未来会受到专业工具社区的喜爱。