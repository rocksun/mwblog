
<!--
title: Harness AI 解决软件开发的核心瓶颈
cover: https://cdn.thenewstack.io/media/2025/08/f2ef1a1b-akash-rai-q3w3c8iskci-unsplash.jpg
summary: Harness AI 旨在通过自动化软件交付流程来解决 AI 代码生成后测试、安全和部署等问题。它构建软件交付知识图谱，利用 AI 代理优化 DevOps、SRE、安全和测试，从而显著缩短测试周期、减少停机时间并降低维护工作量。
-->

Harness AI 旨在通过自动化软件交付流程来解决 AI 代码生成后测试、安全和部署等问题。它构建软件交付知识图谱，利用 AI 代理优化 DevOps、SRE、安全和测试，从而显著缩短测试周期、减少停机时间并降低维护工作量。

> 译自：[Harness AI Tackles Software Development's Real Bottleneck](https://thenewstack.io/harness-ai-tackles-software-developments-real-bottleneck/)
> 
> 作者：Darryl K. Taft

虽然[AI 编码助手](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/)可以在几分钟内生成数千行代码，但编写代码只是简单的部分。真正的痛苦在于之后——测试、保护、部署和保持其运行。

为了解决这个问题，[Harness](https://harness.io/products/continuous-integration?utm_content=inline+mention) 推出了 Harness AI，这是一个可以自动化你在点击 “commit” 之后所有事情的平台。并且根据早期客户的结果，他们可能正在做一些有意义的事情。

## 实际出问题的地方

大多数开发人员只花费一小部分时间实际编写代码。其余时间都被 Harness 首席执行官 [Jyoti Bansal](https://www.linkedin.com/in/jyotibansal/) 称之为 “苦工” 的事情所占据 —— 管理 [CI/CD 流水线](https://thenewstack.io/introduction-to-ci-cd/)、照看 [测试套件](https://thenewstack.io/a-better-developer-experience-requires-better-testing-tools/)、追查 [安全漏洞](https://thenewstack.io/top-9-api-security-vulnerabilities-how-to-defend-against-them/) 以及弄清楚为什么 [云账单持续增长](https://thenewstack.io/your-engineering-organization-is-too-expensive/)。

“你可能每周要花费 35 到 45 个小时仅仅是管理和维护 CI/CD 流水线，”Bansal 在最近的一次采访中告诉我。“你的构建失败了？那又是一个小时。云成本飙升？你的下午就泡汤了。”

这些数字支持了这一点。Harness 发现，近 80% 的软件故障发生在编码之后，其中 CI/CD 流水线是最大的罪魁祸首。根据 [2024 DORA 报告](https://dora.dev/research/2024/dora-report/)，尽管有大量的花哨 AI 工具，但软件交付实际上变得越来越不稳定和缓慢。

现在把 [AI 生成的代码](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/) 混入其中，问题会变得更糟。开发人员可以在 20 分钟内生成 20,000 行代码，但在发布之前没有人会通读所有这些代码。

“下游系统最好足够强大，能够抓住问题，因为它们即将到来，”Bansal 告诉 The New Stack。

在一篇博客文章中，Bansal 说 Harness AI 是“下一代软件交付的基础 —— 这一代软件交付不仅适用于今天的应用程序，也适用于具有相同速度、可靠性和安全性的 AI 驱动的应用程序。”

## 超越点解决方案

大多数试图解决这个问题的公司都投入更多的工具——一个用于测试的 [AI 助手](https://thenewstack.io/ai-coding-assistants-12-dos-and-donts/)，一个 [安全扫描器](https://thenewstack.io/how-to-implement-a-security-scanner-for-docker-images/)，可能还有一些云成本监控。这可能会导致工具蔓延，而没有任何真正的智能来连接这些点。

Bansal 说 Harness 采取了一种不同的、独特的方法。它没有构建另一个点解决方案，而是创建了它所谓的“软件交付知识图谱”——本质上是一个了解你整个开发过程的大脑，从代码仓库到生产基础设施。

[![](https://cdn.thenewstack.io/media/2025/08/53bd7f9c-unnamed-1-1.png)](https://cdn.thenewstack.io/media/2025/08/53bd7f9c-unnamed-1-1.png)

该平台表面上看起来很简单 —— 只是一个聊天界面，你可以在其中要求它“为我们的移动应用程序设置一个流水线”或“为什么我们的部署昨晚失败了？” 但在底层，专业的 [AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 正在处理繁重的工作，每个代理都专注于不同的方面，如 [安全性、测试或成本优化](https://thenewstack.io/ai-is-testing-ai-generated-code-should-you-trust-it)，Bansal 说。

“Harness AI 无缝连接了一套智能代理，例如 [DevOps](https://thenewstack.io/introduction-to-devops/)、[SRE](https://thenewstack.io/ai-reliability-engineering-welcome-to-the-third-age-of-sre/)、发布、AppSec 和测试代理，”Bansal 在文章中写道。“你看不到这些代理，但你可以在每个工作流程中感受到它们的影响：更快、更安全、更智能的交付。”

有趣的是上下文。该系统知道你公司的安全策略，了解你的基础设施设置，并记住你上次尝试在星期五下午部署时发生了什么。它不是生成通用的流水线 —— 它正在构建真正适合你组织的东西。

## 真实世界的成果

早期数据显示，企业客户的测试周期时间缩短了 80%，停机时间减少了一半，测试维护工作量减少了 70%。Bansal 说，一位客户告诉他，仅仅通过拥有一个真正了解其设置的 AI，就将流水线调试时间减少了一半。

“反馈非常棒，”Bansal 说，他回忆起最近在俄亥俄州哥伦布市和芝加哥的用户活动。“人们说没有类似的东西存在。每个人都在与 DevOps 和安全以及所有这些占据 70% 工程时间的事情作斗争，而且没有好的 AI 解决方案。”

## 更大的图景

Harness 已经构建自动化工具七年了，但 AI 层相对较新 —— 大约开发了 30 个月，Bansal 说。他们正在与常见的对象合作 —— Anthropic、OpenAI、Google —— 并且还与 Cursor 和 [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) 等开发人员工具集成，以便在开发人员实际工作的地方与他们会面，他补充说。

随着 AI 使生成代码变得更容易，瓶颈转移到其他所有事情。Bansal 说，那些弄清楚如何自动化软件交付的公司可能会拥有真正的竞争优势。

此外，Bansal 说，在一个每个人都专注于让编码更快的世界里，需要有人确保流水线的其余部分能够跟上。

Harness AI 现已提供给现有的 Harness 客户，并计划在 9 月份的公司 [Unscripted 会议](https://www.unscriptedconf.io/) 上进行更广泛的展示。