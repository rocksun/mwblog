<!--
title: GitHub 发布全新 Copilot 独立应用，正面硬刚 Claude Code 与 Codex
cover: https://cdn.thenewstack.io/media/2026/05/ebfbc142-roman-synkevych-wx2l8l-fgea-unsplash.jpg
summary: GitHub 推出了全新的独立桌面应用 GitHub Copilot App，旨在统一管理 AI 代理、任务和 PR。该应用标志着 Copilot 从 IDE 插件向自主 Agent 模式的转型，直接竞争 Claude Code。
-->

GitHub 推出了全新的独立桌面应用 GitHub Copilot App，旨在统一管理 AI 代理、任务和 PR。该应用标志着 Copilot 从 IDE 插件向自主 Agent 模式的转型，直接竞争 Claude Code。

> 译自：[GitHub takes aim at Claude Code and Codex with its new Copilot app](https://thenewstack.io/github-copilot-desktop-app/)
> 
> 作者：Paul Sawers

GitHub 动摇其 Copilot 编程助手格局的最新举措是为其提供一个专属的独立应用。

这家微软子公司在周四[宣布](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/)了 [GitHub Copilot 应用](https://github.com/features/preview/github-app)的技术预览版。这是一个独立的桌面应用程序，旨在通过单一界面管理编程代理（Agents）、议题（Issues）、拉取请求（Pull Requests）以及开发会话。

该应用允许开发者直接从 GitHub 议题、提示词或现有的代码会话中启动 Copilot 任务，同时跨仓库跟踪进度和活跃的代理运行情况。

> “一个旨在通过单一界面管理编程代理、议题、拉取请求和开发会话的独立桌面应用程序。”

![Copilot 应用](https://cdn.thenewstack.io/media/2026/05/f4ecd4ca-cl_githubapppreview_header_07-1024x538.png)

*Copilot 应用*

根据 GitHub 的介绍，该应用包含一个用于呈现议题和拉取请求的统一收件箱、并排的代码差异（Diff）审查、会话历史记录、仓库上下文，并支持同时运行多个编程代理。开发者还可以检查提议的更改、留下反馈、恢复暂停的会话，并将完成的工作移入拉取请求中。

在底层，这款新应用构建于 [GitHub Copilot CLI](https://github.com/features/copilot/cli) 之上，后者是 GitHub 基于终端的 AI 编程代理，已于今年 2 月正式发布。桌面客户端将这些代理能力带入了一个专门的图形界面，允许开发者在不频繁切换终端、编辑器和浏览器标签页的情况下，监督编程会话、仓库和任务。

![GitHub Copilot 应用](https://cdn.thenewstack.io/media/2026/05/3ca28875-giffy.gif)

*GitHub Copilot 应用*

Copilot 应用目前支持 macOS、Windows 和 Linux 系统，面向 Copilot Business 和 Enterprise 订阅用户开放公开预览，而 Copilot Pro 和 Pro+ 用户[可以加入候补名单](https://github.com/features/preview/github-app?#form)以获取早期访问权限。

GitHub 尚未正式宣布全面的公开发布日期。然而，公告[随附的产品视频](https://github.com/user-attachments/assets/244c19ef-dfdf-446e-b346-101475799f05)中提到了 6 月 2 日，这表明该公司可能将该日期作为更大规模推广的目标。

## **超越 IDE**

自从 [2021 年发布](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)以来，Copilot 主要存在于 Visual Studio Code、JetBrains IDE 和 Visual Studio 等开发工具中。随后，GitHub 通过 Copilot CLI 将其扩展到了 GitHub.com、移动应用和基于终端的工具。

最初的体验围绕着嵌入在编辑器内部的行内建议和聊天辅助。开发者在本地编写代码，而 Copilot 在其现有工作流旁生成补全、回答问题或建议修改。

> “新的桌面应用将 Copilot 进一步推向了整个 AI 编程市场中正在兴起的模式。”

新的桌面应用将 Copilot 进一步推向了整个 AI 编程市场中正在兴起的模式：即跨仓库、任务和云环境运行的自主编程代理（Autonomous coding agents）。这使得 GitHub 与 Anthropic 的 [Claude Code](https://thenewstack.io/claude-code-desktop-redesign/) 以及 [OpenAI 的 Codex](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/) 等工具展开了更直接的竞争，这些工具都通过允许开发者将更大块的工程工作委托给 AI 系统而获得了关注。

当然，GitHub 的优势在于，大部分周边的开发者基础设施已经存在于其平台上。仓库、议题、拉取请求、CI 流水线和代码审查系统已经内置于 GitHub 中，这为该公司提供了一种将编程代理直接绑定到现有软件开发生命周期的方法。

[Petter Arnesen](https://www.linkedin.com/in/pettertech/) 是一位 Azure MVP 兼云架构师，他已经[提前体验该应用](https://www.youtube.com/watch?v=5Q5mLNYJ6Hw)数周。他将 GitHub 的方法描述为他迄今为止尝试过的 AI 开发者助手中“最有趣的实现方式”。

在 [LinkedIn 帖子](https://www.linkedin.com/feed/update/urn:li:activity:7460725853962829826/)中，Petter Arnesen 表示他一直在使用该应用处理从侧边项目到代理驱动的拉取请求审查循环的所有事务，在这些循环中，Copilot 可以等待反馈、处理评论并自动更新 PR。尽管如此，他表示他目前还“不会在没有监督的情况下将其释放到生产系统中”，并指出预览期间存在一些 Bug，且 AI 代理在没有人工监督的情况下倾向于产生过于复杂的解决方案。

## **Copilot 的商业模式**

此次发布紧随最近几个月 Copilot 的一些重大变化，GitHub 正在调整产品和商业模式。

今年 4 月，GitHub [暂停了某些 Copilot 个人方案的新用户注册](https://thenewstack.io/github-copilot-signups-paused/)，同时对现有订阅者引入了更严格的使用限制，反映出与 AI 编程工具相关的需求增长和基础设施成本上升。

不久之后，[该公司宣布](https://thenewstack.io/github-copilot-usage-billing/)对 Copilot 定价进行全面改革，从很大程度上固定价格的订阅模式转向与不同 AI 模型消耗的 Token 挂钩的按用量计费模式。

在修订后的结构下，定价因素包括输入 Token、生成的输出以及缓存上下文的使用情况，费率根据开发者选择运行的底层模型而有所不同。这些变化使 Copilot 的收费方式更接近基础模型提供商自身的 AI 推理收费方式。

GitHub 最近几个月还一直在扩展 Copilot 周边的底层代理基础设施。周三，该公司[推出了一个 REST API](https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api/)，用于启动基于云的 Copilot 代理任务，同时在 [JetBrains IDE 内部引入了统一的会话视图](https://github.blog/changelog/2026-05-13-introducing-copilot-cli-agent-and-unified-sessions-view-in-github-copilot-for-jetbrains-ides/)。

桌面应用现在将这些零散的功能整合到一个更连贯的产品界面中。

从更广泛的角度来看，这次发布反映了 AI 编程工具进化的速度之快。早期的编程助手专注于帮助开发者更快地编写单个函数或片段。新一代工具则围绕着能够在仓库和项目中独立处理更大任务的系统。

GitHub 的新应用表明，该公司将这一转型视为 Copilot 未来的核心——并且不希望这个市场被其著名的竞争对手所定义。