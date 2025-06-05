<!--
title: GitHub发布其编码助手
cover: https://cdn.thenewstack.io/media/2025/05/e323f54e-img_6682-scaled.jpg
summary: GitHub发布AI编码助手**GitHub Copilot Coding Agent**，集成于GitHub，可处理issue并自主解决。基于Anthropic的Claude Sonnet 3.7，在**GitHub Actions**云端运行，监控代码库，辅助开发。微软推出Azure **SRE Agent**，与**GitHub SWE Agent**联动，实现Agentic DevOps，加速软件交付。VS Code Copilot扩展已开源。
-->

GitHub发布AI编码助手**GitHub Copilot Coding Agent**，集成于GitHub，可处理issue并自主解决。基于Anthropic的Claude Sonnet 3.7，在**GitHub Actions**云端运行，监控代码库，辅助开发。微软推出Azure **SRE Agent**，与**GitHub SWE Agent**联动，实现Agentic DevOps，加速软件交付。VS Code Copilot扩展已开源。

> 译自：[GitHub Launches Its Coding Agent](https://thenewstack.io/github-launches-its-coding-agent/)
> 
> 作者：Frederic Lardinois

今年早些时候，GitHub [预告](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/)了 Project Padawan，它是一款旨在协助软件工程师并代表他们处理日常任务的助手，例如审查代码、重构代码、排除故障等等。今天，在年度 [Microsoft Build](https://build.microsoft.com/en-us/home) 大会上，GitHub 推出了其首个迭代的编码助手，名为 GitHub Copilot Coding Agent。这款新的软件工程 (SWE) 助手将完全集成到 GitHub 体验中，并且能够处理 GitHub 问题并自主解决。它将从今天开始向 Copilot Enterprise 和 Copilot Pro+ 用户推出。

由于编码助手需要大量的计算能力，它将在云中运行，使用 GitHub Actions。一旦开发人员将问题分配给助手，它将在 GitHub Actions 中启动一个可定制的开发环境来处理 pull requests。

然而，未经人工批准，该助手将无法运行任何 CI/CD 工作流程。它也只能推送到它创建的分支，永远不会触及默认分支和开发人员创建的其他分支。开发人员可以限制助手可以访问哪些 MCP 服务器和互联网站点，并且为了在此基础上增加另一层审查，要求助手打开 pull request 的开发人员不能是批准它的人。

![](https://cdn.thenewstack.io/media/2025/05/d3102053-screenshot-2025-05-18-at-2.06.51%E2%80%AFpm.png)

*图片来源：Microsoft。*

GitHub CEO [Thomas Dohmke](https://www.linkedin.com/in/ashtom/) 告诉我：“在当今世界，助手并不像人类开发人员那样受到信任。“这几乎就像你让某人加入你的团队，而没有经过面试和背景调查。因此，我们认为助手需要处于一个比我们对人类施加更多控制的环境中。”

目前，它由 Anthropic 的 Claude Sonnet 3.7 提供支持，因为正如 Dohmke 告诉我的那样，该团队认为该模型目前具有“代码质量和匹配开发人员偏好的最佳组合”。

## 👀

Dohmke 最近[谈到](https://thenewstack.io/github-copilot-wants-to-become-your-peer-programmer/) Copilot 成为开发人员的同行。在很多方面，这就是正在发生的事情。

他在今天宣布之前的一次采访中说：“工作流程是，作为一名开发人员，你仍然将大部分时间花在 VS Code 中，构建你喜欢的软件，做你喜欢做的事情。“当你有一个任务，或者有人给你分配了一个 GitHub 问题，或者收到一个错误报告时，你将其交给编码助手。然后，你在云中运行一些助手会话，而你的本地机器可供你使用，处于流畅状态。希望做一些神奇的事情。”

![](https://cdn.thenewstack.io/media/2025/05/71cfb03a-screenshot-2025-05-18-at-2.07.56%E2%80%AFpm.png)

*图片来源：Microsoft。*

使用 GitHub.com、GitHub Mobile 或 GitHub CLI，开发人员可以将问题分配给助手，就像他们对待任何其他同事一样。然后，助手添加 👀 表情符号并开始工作。开发人员可以通过查看助手的推理步骤和在会话日志中验证代码的努力来监控进度。

GitHub 强调，所有这些对于通常由单个 GitHub 问题涵盖的定义明确的请求效果最佳。Dohmke 说：“该助手擅长于经过良好测试的代码库中复杂度较低到中等的任务，从添加功能和修复错误到扩展测试、重构代码和改进文档。”

## 从代码补全到编码助手

![](https://cdn.thenewstack.io/media/2025/05/7b6cd271-screenshot-2025-05-18-at-2.11.03%E2%80%AFpm-300x199.png)

*图片来源：Microsoft。*

这个新的助手补充了 Copilot 现有的助手模式，该模式在 IDE 中运行。助手模式还可以从头开始编写代码，对现有代码库进行编辑，并根据需要使用工具。顺便说一句，这种助手模式以前仅在 VS Code 中可用，但现在也可在 JetBrains、Eclipse 和 Xcode 中使用。

Dohmke 将当前产品视为一个连续的频谱，从代码补全和助手模式（涵盖编码的内部循环）到编码助手——然后再返回，他强调说。
“如果你想象一下，编码代理创建了一个 pull request，并且它已经创建了五个 commits，”他解释说。“它几乎完成了，现在你必须做出决定，你是想继续提示它，让它达到你想要的状态吗？还是直接使用 GitHub CLI 快速检出该 pull request？打开 VS Code（无论是否使用 Agent 模式），进行更改，然后推送回去？Pull request 提供了一个理想的位置，代理可以让你几乎完成，你可以快速完成剩下的工作，并将另外几个 commits 提交到同一个 pull request 中，以便准备好合并它。”

## 微软的 SRE 代理

除了编码代理之外，微软本周还将为 Azure 推出一个站点可靠性工程（SRE）代理，它实际上可以使用新的 GitHub SWE 代理来自动修复问题。

“[Amanda Silver](https://www.linkedin.com/in/amandaksilver/)告诉我：“这里的关键是它可以 24/7 监控你的系统，并自动排除出现的问题。”她是微软开发者部门的企业副总裁兼产品负责人。“它通过 GitHub 在你的工作流程中工作。因此，一旦它找到问题的根本原因，它实际上可以自动尝试修复它，[…]，但它也可以将这些问题记录到 GitHub 中。因此，我们也有这种非常好的互动，你可以让 SRE 代理监控你的生产系统。它发现一个问题，它将该问题作为 issue 记录到 GitHub 中，然后 SWE 代理——我们正在推出的 GitHub Copilot 编码代理——可以去处理并推进修复项目。”

Silver 指出，这个 SRE 代理是基于微软自己开发并在内部使用的内部代理。它的数据基于该公司向其工程师提供的相同指导，以帮助他们排除 Azure 服务的故障。

微软还与 New Relic 合作，将其应用程序性能监控（APM）服务的数据引入到这个工作流程中。该代理还将能够与 ServiceNow、[PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention) 和其他事件管理系统一起工作。

## DevOps 的乐趣

Silver 说，所有这些都是为了让乐趣回归 [DevOps](https://thenewstack.io/devops/)。

“我们将整个类别真正视为 ‘agentic DevOps’，作为 DevOps 整体的下一个阶段，”Silver 说。“在这个世界中，我们看到 AI 代理嵌入到开发的每个阶段：从计划到生产，从编码到部署。这将真正有助于更快、更高质量、更愉快地交付软件。”

## 奖励：VS Code Copilot 扩展开源

虽然编码代理绝对是今天 GitHub 公告的亮点，但值得注意的是，GitHub 也在开源 VS Code GitHub 扩展。VS Code 已经是开源的，开发者已经开始依赖许多扩展。Copilot 扩展，包括其系统提示，现在将与 VS Code 位于同一个 GitHub 存储库中。

“我认为这里的关键是，这真的会让生态系统与我们一起构建，”Silver 告诉我。“VS Code 一直是开源的，扩展是 VS Code 的魔力所在。我认为，显然，在 AI 辅助编码方面正在发生令人难以置信的创新，因此我们希望确保 VS Code 继续成为所有这些创新发生的中心。”

值得注意的是，适用于 Apple 的 Xcode IDE 的 Copilot 扩展 [已经开源](https://github.com/github/CopilotForXcode)。