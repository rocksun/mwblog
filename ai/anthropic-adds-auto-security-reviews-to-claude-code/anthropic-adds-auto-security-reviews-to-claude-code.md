
<!--
title: Claude Code代码新增自动安全评估
cover: https://cdn.thenewstack.io/media/2025/08/476ea983-peter-conrad-ua8pwpht1vw-unsplash-1.jpg
summary: Anthropic 发布 Claude Code 的自动化安全审查功能，包括终端安全扫描和 GitHub pull request 审查，旨在解决 AI 加速开发带来的安全问题，并实现安全专业知识的民主化。新功能已在内部测试中发现多个生产漏洞。
-->

Anthropic 发布 Claude Code 的自动化安全审查功能，包括终端安全扫描和 GitHub pull request 审查，旨在解决 AI 加速开发带来的安全问题，并实现安全专业知识的民主化。新功能已在内部测试中发现多个生产漏洞。

> 译自：[Anthropic Adds Auto Security Reviews to Claude Code](https://thenewstack.io/anthropic-adds-auto-security-reviews-to-claude-code/)
> 
> 作者：Darryl K. Taft

[Anthropic](https://www.anthropic.com/) 今天发布了 [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) 的自动化安全审查功能，这是一款命令行 [AI 代码助手](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/)，旨在解决随着 AI 显著加速软件开发，人们对维护代码安全性日益增长的担忧。

新功能包括一个基于终端的安全扫描命令和自动化的 GitHub pull request 审查，Anthropic 前沿红队负责人 [Logan Graham](https://www.linkedin.com/in/logangraham/) 称之为“帮助开发者在几乎不用努力的情况下，让他们的代码真正、非常安全”的起点。

## **终端速度的安全审查**

本次更新的核心是一个新的 `/security-review` 命令，开发者可以在提交代码之前直接从终端运行该命令。Anthropic 在一篇博文中表示，该功能会扫描常见的漏洞，包括 SQL 注入、[跨站脚本 (XSS)](https://thenewstack.io/xss-vulnerability-discovered-in-backstage-software-catalog/)、身份验证缺陷、不安全的数据处理和依赖项漏洞。

“[使用该命令] 就像敲击 10 次键盘，就好像有一位资深安全工程师在你身边一样，”Graham 告诉 The New Stack。“对于编写代码的人来说，或者对于使用 Claude 编写代码的人来说，让代码非常安全应该是毫不费力的，或者应该自动发生，”他补充道。

在识别出问题后，开发者可以要求 Claude Code 自动实施修复，从而将安全审查保持在 Graham 所谓的“内部开发循环”中，在该循环中，解决问题最容易且成本最低。

## 自动化的 Pull Request 安全

第二个主要功能是一个 [GitHub Action](https://thenewstack.io/how-to-use-github-actions-and-apis-to-surface-important-data/)，它会自动审查每个 pull request 的安全漏洞。一旦由安全团队配置，该系统会自动在新 pull request 上触发，审查代码更改中的安全漏洞，应用可自定义的规则来过滤误报，并在 pull request 上以内联方式发布带有具体问题和建议修复的评论。

“这为您的整个团队创建了一个一致的安全审查流程，确保没有任何代码在没有经过基线安全审查的情况下进入生产环境，”Anthropic 在博文中表示。“该 action 与您现有的 [CI/CD 管道](https://thenewstack.io/how-to-build-scalable-and-reliable-ci-cd-pipelines-with-kubernetes/) 集成，并且可以自定义以匹配您团队的安全策略。”

## 实际结果

Anthropic 已经在内部测试了这些功能。Graham 表示，该公司在这些功能发布之前就发现了几个生产漏洞，包括可以通过本地 HTTP 服务器中的 DNS 重新绑定利用的远程代码执行漏洞，以及内部凭证管理系统中的 SSRF 攻击漏洞。

“自从设置了 GitHub Action 以来，它已经发现了我们自己代码中的安全漏洞，并防止它们被发布并影响我们的用户，”该博文指出。

## 规模挑战

这些安全功能旨在解决 Graham 认为软件安全方面正在出现的一个危机。随着 AI 工具变得越来越普遍，生成的代码量正在爆炸式增长。

“模型现在正在编写极大量的代码，”Graham 说。“我认为在未来一两年内，您最终可能会将世界上存在的代码量增加 10 倍、100 倍或 1,000 倍。跟上这种增长的唯一方法是通过模型。”

Graham 说，代码量的急剧增加使得传统的人工主导的安全审查在规模上变得不切实际。“目前，这需要人工来审查所有内容以确保其安全性，如果我们真的希望模型处理世界上最有价值的事情，我们需要找到一种方法使所有生成的代码同样安全，理想情况下要更加安全，”他告诉 The New Stack。

## 安全民主化

除了解决规模问题之外，这些功能还旨在实现安全专业知识的民主化。Graham 解释说，这些工具可以使缺乏专门的安全工程师或没有预算购买昂贵安全软件的小型开发团队受益。

“我们正在将[安全审查民主化](https://thenewstack.io/coderabbits-ai-code-reviews-now-live-free-in-vs-code-cursor/)，提供给那些正在构建令人兴奋的东西，并且没有 [安全工程师](https://thenewstack.io/aptori-is-building-an-agentic-ai-security-engineer/)，无法支付软件许可费的个体经营者，”他说。“如果他们开始使用这些工具，他们可能会更快、更可靠地发展壮大。”

## 从黑客马拉松到生产环境

这些安全功能起源于 Anthropic 的一个内部黑客马拉松项目，安全团队在那里构建工具来维护 Graham 所描述的这家 AI 公司的“前沿级安全”。当该工具开始在 Anthropic 自己的代码发布之前发现问题时，该团队决定将其提供给所有 Claude Code 用户。

“这始于一个 [黑客马拉松](https://thenewstack.io/hackathon-tips-to-boost-devops-innovation/) 项目。它已经开始在我们自己的代码发布之前发现其中的问题或缺陷，”Graham 解释说。“我们认为，这非常、非常有用。这与我们的使命非常一致。为什么我们不直接将其提供给 Claude Code 中的每个人呢？”

## 企业焦点

此次安全公告延续了 Anthropic 最近推动 Claude Code 更适合企业使用的努力。Graham 说，仅在上个月，该公司就发布了子代理、管理员分析仪表板、原生 Windows 支持、Hooks 和多目录支持。

这种创新步伐表明，Anthropic 的更广泛的目标是将 Claude Code 定位为开发团队必不可少的基础设施，从简单的代码生成转向全面的开发工作流程集成。

该公司能够以如此快的速度交付技术，是因为：“Anthropic 的人才密度非常高，而且我们以这样的规模所做的事情，老实说，今天非常、非常了不起，”Graham 告诉 The New Stack。

## 展望未来

Graham 表示，这些安全功能仅仅是软件开发和安全与 AI 相交的更大转变的开始。

“我们广泛的信念是，随着时间的推移，模型基本上会以一种非常代理的方式完成所有事情，”他说，这表明 AI 代理将越来越多地自主处理复杂的、多步骤的开发任务。

所有 Claude Code 用户都可以立即使用 `/security-review` 命令和 GitHub Action。终端命令需要更新到最新版本的 Claude Code，而 GitHub Action 需要按照 Anthropic 的文档进行手动设置。

对于那些正在努力应对 AI 加速开发带来的安全影响的开发者和组织来说，这些工具代表着一种早期的尝试，旨在确保 AI 代码辅助的好处不会以牺牲应用程序安全为代价，Graham 说。