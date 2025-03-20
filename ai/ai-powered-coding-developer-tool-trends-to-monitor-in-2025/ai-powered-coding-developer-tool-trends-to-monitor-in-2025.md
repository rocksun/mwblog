<!--
title: 2025年值得关注的AI编码趋势：开发者工具
cover: https://cdn.thenewstack.io/media/2025/03/fa87b365-james-harrison-vyhd0plbu9s-unsplashb.jpg
summary: AI编码工具井喷！开发者面临选择：增强现有IDE（VS Code + GitHub Copilot），拥抱“智能IDE”（Cursor, Warp），或转向云原生IDE（Replit, Amazon CodeCatalyst）。云原生工具如Cog, Modal简化AI开发。关注AI与IDE深度融合，原型设计工具Bolt或成新宠。
-->

AI编码工具井喷！开发者面临选择：增强现有IDE（VS Code + GitHub Copilot），拥抱“智能IDE”（Cursor, Warp），或转向云原生IDE（Replit, Amazon CodeCatalyst）。云原生工具如Cog, Modal简化AI开发。关注AI与IDE深度融合，原型设计工具Bolt或成新宠。

> 译自：[AI Coding Trends: Developer Tools To Watch in 2025](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/)
> 
> 作者：Richard MacManus

现在几乎每个编码工具都融入了 AI，开发人员越来越多地问自己：现在哪种类型的编码工具应该成为我的默认选择？我需要那些新式的“智能 IDE”之一，还是 Visual Studio Code 就足够了？云在 AI 工具中扮演什么角色？

为了回答这些问题，我调查了开发工具领域，并挑选出了一些值得开发人员关注的趋势。首先，让我们评估一下开发人员在适应 AI 时的主要选择：

1. **你常用的 IDE，通过 AI 助手插件增强**：最常见的选择似乎是坚持使用你现有的 IDE（如 VS Code、JetBrains 或 Neovim），同时集成 AI 助手，如 [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/)、Google 的 [Gemini Code Assistant](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/) 或 [JetBrains AI](https://thenewstack.io/jetbrains-agentic-ai-assistant-helps-automate-coding-tasks/)。（不过，如果你是 Visual Studio Code 用户，问题就变成了：你如何阻止不同的 AI 插件 [互相干扰](https://thenewstack.io/gemini-code-assist-review-code-completions-need-improvement/)？）
2. **将 AI 与你的编辑器分开**：如果你喜欢干净、无干扰的代码编辑器，你可能会选择在外部使用聊天机器人，如 [ChatGPT](https://thenewstack.io/how-to-learn-unfamiliar-software-tools-with-chatgpt/) 或 Anthropic 的 [Claude 3.7 Sonnet](https://thenewstack.io/making-the-fediverse-more-accessible-with-claude-3-7-sonnet/) 作为编码助手，而不是将 AI 直接嵌入到你的工作流程中。
3. **切换到“智能 IDE”**：像 [Bolt](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/), [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) 和 [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) 这样的工具承诺为你完成大部分编码工作，更像是 AI 驱动的合作开发者，而不是简单的自动完成助手。这些环境旨在通过接受高级指令并生成完整的应用程序来减少手动编码。（另见：[vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)）
4. **依赖于 AI 原生的云 IDE**：一些开发人员没有选择传统的桌面 IDE，而是选择了像 Replit ([Ghostwriter](https://thenewstack.io/ghost-in-the-ide-testing-replits-ai-helper-ghostwriter/))、[Amazon CodeCatalyst](https://thenewstack.io/aws-code-catalyst-a-low-code-approach-for-the-dev-lifecycle/) 或 [Google Cloud Workstations](https://cloud.google.com/workstations?hl=en) 这样的选项，这些选项将 AI 深度集成到基于云的开发环境中。
5. **使用 AI 驱动的终端**：如果你经常使用命令行，你可能更喜欢像 [Warp](https://thenewstack.io/warp-is-a-power-users-dream-terminal-for-linux/) 或 [Ghostty](https://thenewstack.io/warp-vs-ghostty-which-terminal-app-meets-your-dev-needs/) 这样的 AI 增强终端，甚至像 ShellGPT 或 Copilot CLI 这样的 AI 驱动的 CLI 工具，它们可以即时生成命令和脚本。
6. **完全不使用 AI**：一小部分但充满热情的开发人员选择完全避免 AI 辅助编码，更喜欢以传统方式编写代码（公平地说，对于知识渊博的开发人员来说，这种方式在几十年里一直运行良好）。

## 一款开发工具，统治一切

这些选项的共同之处在于，它们的代表都认为它们将是开发人员 *唯一* 需要的 AI 辅助编码工具。

我最近与 Warp 的创始人兼 CEO Zach Lloyd 谈论了该公司新的 [Windows 版本的终端应用程序](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/)。我们还讨论了 Warp 如何在最近涌入市场的众多 AI 编码工具中定位自己。他的回答清楚地表明，他认为像 Warp 这样的终端应用程序现在能够做的事情远不止命令行交互。

![](https://cdn.thenewstack.io/media/2025/02/e500d52f-bolt-screenshot-feb25.jpg)

“Warp 是一种高度差异化、有主见的下一代 AI 工具方法，”他告诉我。“你知道，今天我们是一个终端——今天这就是我们的定位。但我们拥有的愿景是 [...] 我们相信命令行是开发人员使用 AI 做任何事情的好地方。它就像一个非常底层的接口，拥有大量可用的工具。这些工具在很大程度上已经编写完成，可以供人和机器使用，比如 CLIs [Command Line Interface] 既可以供人使用，也可以供机器使用。因此，我们觉得这是一种很棒的、与众不同的、非‘VS Code 克隆’的未来 AI 方法。”
可能是 VS Code 最著名的分支——或者用 Lloyd 的话说“克隆”——是 Cursor。与 VS Code 本身依赖 GitHub Copilot 或 Gemma Code Assistant 等插件来实现 AI 功能不同，[Cursor 将 AI 功能直接嵌入到开发环境中](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)。与 Warp 想要实现的目标类似，使用 Cursor，你几乎可以在应用程序内部完成所有开发者任务。

正如 The New Stack 的 Janakiram MSV [去年 9 月解释的那样](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/)：

> 我最喜欢 Cursor 的一点是，它能够在无需离开开发环境的情况下处理端到端的应用程序生命周期。虽然像 Composer 和 Tab 这样的功能可以处理代码生成，但终端中的聊天窗口是一个真正的游戏规则改变者。它可以生成和运行 shell 脚本、Docker 和 Kubernetes 命令以及任何其他与 CLI 相关的工具。

这种“一个应用程序统治一切”的方法——Warp、Cursor 和其他几个编码应用程序都在追求这一愿景——只有在最新的大型语言模型不断增强的[推理能力](https://thenewstack.io/how-to-add-reasoning-to-ai-agents-via-prompt-engineering/)的支持下才有可能实现。

![](https://cdn.thenewstack.io/media/2025/02/89ac4ce8-gemini-code-assist-feb25.jpg)

*Gemini Code Assist ;图片来自谷歌。*

## 理想的原型设计工具

并非所有应用程序都试图成为所有（AI）开发者的所有工具。

Bolt 是一款基于浏览器的应用程序，它利用了 StackBlitz 的专有 WebContainers 技术。但是，当 [我与它的 CEO Eric Simons 交流时](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)，他承认许多开发者仍然希望使用像 VS Code 这样的 IDE 或任何 JetBrains 的选项。

首先，值得注意的是，Bolt 的大多数用户不是专业开发者——Simons 估计 60-70% 的 Bolt 用户是“非技术人员”。但是对于确实使用该产品的专业开发者来说，Bolt “不是一个完全的替代品 [...] 这也不是我们的目标”，他说。相反，专业开发者倾向于将 Bolt 用作一种原型设计辅助工具。

“我们现在正在销售给的许多公司，他们正在将此用作 Figma 的一种替代品，几乎是，”Simons 告诉我。“在哪里，而不是像在 Figma 中那样将所有原型和东西都作为设计来做，比如，让我们在 Figma 中制作组件，然后将它们放入 Bolt [...] 作为代码，然后提示它为我们制作应用程序。让 AI 去构建这些东西要快得多，然后你得到的是真正的代码。”

值得一提的是 Google 和 Microsoft 在“原型设计”类别中，因为这两家公司都致力于将开发者市场扩展到专业开发者之外。更不用说两者都有能力大规模扩展他们的 AI 编码工具。正如 Google 的 Ryan J. Salva 在 [最近的一次采访](https://thenewstack.io/google-ai-coding-tool-now-free-with-90x-copilots-output/) 中告诉我的那样：

> 我们正在为如何将基本工具和 IDE 提供给尽可能多的人奠定基础，具有非常慷慨的使用限制，并且实际上除了电子邮件地址之外没有其他要求。

## 用于 AI 的云原生工具

我们在 AI 开发中看到的另一个趋势是，由于缺乏更好的短语，AI 工具的云原生化。例如，Docker Compose 的创建者 Ben Firshman 创建了一种 [将 AI 模型包装到容器中](https://thenewstack.io/simplify-ai-development-with-machine-learning-containers/) 的技术——它被称为 Cog，Fishman 将其描述为“机器学习的 Docker”。在此基础上，他与人共同创立了一家名为 Replicate 的公司，该公司提供了一个云平台来共享这些模型。

我们还看到了各种专门从事 AI 的无服务器平台涌现。[最近，我介绍了 Modal](https://thenewstack.io/serverless-for-ai-devs-modals-python-and-rust-based-platform/)，它专门提供为计算密集型和长时间运行的 AI、ML 和数据工作流程量身定制的无服务器基础设施。它的目标是那些不想处理 LLM 和其他 AI 基础设施的大量计算需求的开发者。

![](https://cdn.thenewstack.io/media/2025/01/6aa787b8-modal-playground.png)

*Modal playground.
*
## 结论

感觉我们正处于 AI 编码工具的转折点。虽然我预计大多数经验丰富的开发者会坚持使用他们最喜欢的成熟 IDE（如果你可以简单地添加一个 AI 插件来获得该功能，为什么不呢），但我们应该关注的是初级开发者和下一波开发者。

许多最近或新进入开发者就业市场的人可能会选择像 Cursor 或 Warp 这样的工具作为他们的默认应用程序，并使用它。他们也更可能选择像 Bolt 和 Windsurf 这样的工具来原型化他们的应用程序。在 2025 年的剩余时间里，我们将继续在 The New Stack 上跟踪这些 AI 开发工具的趋势。