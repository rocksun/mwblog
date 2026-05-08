<!--
title: GitHub 为运行在 MCP 上的 AI 编程智能体构建“免疫系统”
cover: https://cdn.thenewstack.io/media/2026/05/e83940f7-zulfahmi-al-ridhawi-307yir2wgko-unsplash-scaled.jpg
summary: GitHub 为 MCP 服务器推出依赖项和密钥扫描功能，旨在构建 AI 编程“免疫系统”。该功能将安全检测左移至代码编写阶段，实时拦截漏洞与凭证泄露，降低 AI 自动化编程的风险。
-->

GitHub 为 MCP 服务器推出依赖项和密钥扫描功能，旨在构建 AI 编程“免疫系统”。该功能将安全检测左移至代码编写阶段，实时拦截漏洞与凭证泄露，降低 AI 自动化编程的风险。

> 译自：[GitHub builds an immune system for AI coding agents running on MCP](https://thenewstack.io/github-mcp-security-scanning/)
> 
> 作者：Paul Sawers

安全已成为 AI 编程领域的核心障碍之一：各家公司正竞相将模型连接到外部工具、内部系统和代码仓库。与此同时，研究人员和安全公司在过去一年中一直在[警告提示词注入攻击](https://thenewstack.io/red-teaming-enterprise-ai-agents/)和权限过大的智能体，并对可能让 AI 系统广泛访问文件、API 和开发环境的[恶意第三方“技能”及工具集成表示担忧](https://thenewstack.io/ai-agent-skills-security/)。

当 AI 系统不再局限于聊天界面，转而开始在开发工具中采取行动时，问题变得更加复杂。随着公司构建 [AI 智能体系统的安全模型](https://thenewstack.io/securing-ai-agent-systems/)，MCP 服务器——旨在将[模型连接到服务](https://thenewstack.io/build-mcp-server-tutorial/)（如 GitHub、数据库和云平台）——正成为暴露密钥、漏洞依赖和不安全代码在团队发现之前进行传播的又一隐患。

这种飞速演变的环境正是 GitHub 开始将更多安全检查直接推向工具层本身，而不是等到代码提交或部署的原因。

> “MCP 服务器正成为暴露密钥、漏洞依赖和不安全代码在团队发现之前进行传播的又一隐患。”

## 日益增长的依赖项

GitHub 周二[发布了](https://github.blog/changelog/2026-05-05-dependency-scanning-with-github-mcp-server-is-in-public-preview/)其 GitHub MCP 服务器的依赖项扫描公开预览版，同时还宣布该工具的密钥扫描功能已[正式商用](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available/)。

[MCP](https://modelcontextprotocol.io/docs/getting-started/intro) 是模型上下文协议（Model Context Protocol）的缩写，最初由 Anthropic 开发，允许 AI 模型连接到外部工具和数据源。随着行业推动模型与服务及软件系统交互的标准化，该协议[已成为](https://thenewstack.io/why-the-model-context-protocol-won/)日益增长的 AI 智能体生态系统的核心组成部分，Anthropic [最近将其捐赠给了](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/)智能体 AI 基金会（Agentic AI Foundation）。

GitHub 最初在 2025 年 4 月[推出了自己的 MCP 服务器](https://github.blog/changelog/2025-04-04-github-mcp-server-public-preview/)，允许 AI 工具和编程助手通过 MCP 连接与 GitHub 仓库、议题（Issues）、拉取请求（Pull Requests）及其他平台功能进行交互。

这一新功能为启用了 [Dependabot](https://docs.github.com/code-security/dependabot) 警报的仓库提供了 MCP 连接开发环境下的依赖项扫描。Dependabot 是 GitHub 的安全工具，用于识别项目内已知的漏洞或过时的软件依赖项。

例如，使用 [Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/) 或 Cursor 等 MCP 连接编程智能体的开发者，可以用简单的英语提示系统在代码提交前检查新添加的包是否存在已知安全问题。随后，智能体可以通过 MCP 服务器查询 GitHub 的咨询数据库，并返回包含受影响依赖项、严重程度评级和建议升级版本的结构化结果。

最终目标是在编写或修改代码时发现安全问题，而不是在开发周期的后期。

> “最终目标是在编写或修改代码时发现安全问题，而不是在开发周期的后期。”

此次更新是对[开发者社区请求](https://github.com/github/github-mcp-server/issues/1921)的回应，开发者要求 GitHub 通过 MCP 服务器开放更多安全工具，包括 Dependabot 和密钥扫描。

## 守护秘密

虽然依赖项扫描侧重于易受攻击的软件包，但在 AI 辅助的开发环境中，暴露的凭证仍然是另一个主要问题。就在本周，*The New Stack* 报道了一个 Cursor AI 编程智能体在自主发现并使用了一个权限过大的凭证后，如何在不到 10 秒的时间内[抹掉了 PocketOS 的生产数据库](https://thenewstack.io/ai-agents-credential-crisis/)。

这些密钥——包括 API 密钥、密码和身份验证令牌——在开发过程中经常被临时硬编码到项目中，结果随后被提交到仓库、日志或共享代码库中。

随着开发者越来越依赖 AI 编程工具来快速生成和修改代码（通常较少进行人工审查），这个问题虽然不是全新的，但已变得更加尖锐。今年 3 月，Gitleaks 的创作者 [Zach Rice](https://www.linkedin.com/in/zricethezav/) 发布了 [Betterleaks](https://thenewstack.io/betterleaks-open-source-secret-scanner/)，这是一款专为他所谓的“AI 智能体时代”设计的开源密钥扫描工具。

Rice 告诉 *The New Stack*，AI 辅助编程会创建一个反馈循环，开发者追求速度，忽略警告，并忘记妥善移除生成代码中的凭证：“我向你保证，大多数人都在这么做，而不是花时间去妥善管理他们的密钥，”Rice 说道。

> “开发者可以直接在 MCP 连接的编程工具和智能体内部发现泄漏或暴露的凭证。”

因此，GitHub 正在寻求从开发环境内部解决这一问题。随着[密钥扫描](https://thenewstack.io/github-now-enables-you-to-find-and-fix-code-for-free/)现已在 GitHub MCP 服务器上正式商用，开发者可以直接在 MCP 连接的编程工具和智能体内部发现泄漏或暴露的凭证。

![运行密钥扫描](https://cdn.thenewstack.io/media/2026/05/634e6331-a-1024x596.png)

***运行密钥扫描***

## 安全左移

这两项更新都是“安全左移”更广泛推动力的一部分——在开发阶段捕获问题，而不是在代码提交或部署之后。

GitHub 一直在更广泛地朝着这个方向迈进：其 Copilot 编程智能体在拉取请求到达人工审阅者之前，[已经运行了强制性的安全扫描](https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-automatically-validates-code-security-and-quality/)，包括 CodeQL 分析、密钥扫描和依赖项审查。MCP 服务器的更新将同样的逻辑扩展到了 AI 辅助编程环境本身。

随着智能体编写和修改代码的速度超过了开发者人工审阅的速度，代码编写到进入生产环境之间的窗口期正在缩短。GitHub 押注，关闭这个窗口的最佳位置是在工具内部，在那里，智能体在工作时会持续接受风险行为检查。