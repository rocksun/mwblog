<!--
title: “存在诸多已知局限”：开发者眼中的 Cursor SDK，潜力巨大但仍在演进
cover: https://cdn.thenewstack.io/media/2026/05/5cf64b71-getty-images-pxhjzwy8k1m-unsplash-scaled.jpg
summary: Cursor 发布专用 SDK，支持开发者利用其底层能力构建 AI 代理。尽管该工具在简化基础设施管理和自动化工作流方面表现出色，但目前处于测试阶段，其局限性仍受关注。
-->

Cursor 发布专用 SDK，支持开发者利用其底层能力构建 AI 代理。尽管该工具在简化基础设施管理和自动化工作流方面表现出色，但目前处于测试阶段，其局限性仍受关注。

> 译自：[“Several known limitations”: Developers react to Cursor's promising but still-moving SDK](https://thenewstack.io/cursor-sdk-ai-agents/)
> 
> 作者：Adrian Bridgwater

AI 驱动的代码编辑器 Cursor 上周三发布了一个专用 SDK，允许开发者使用驱动 Cursor 自身的相同运行时、测试基座和模型来构建代理——这似乎是其[超越其 IDE 根源](https://thenewstack.io/cursor-sdk-harness/)的更广泛举措的一部分。

在此之前，Cursor 首席执行官 Michael Truell 迎来了他所预告的软件开发“[第三纪元](https://cursor.com/blog/third-era?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)”，这一纪元现在由 AI 辅助的代码工具驱动。

Cursor 将其测试基座（即 [AI 代码生成](https://thenewstack.io/ai-code-generation-trust-and-verify-always/)模型执行预定义测试验证并提供性能基准的能力部分）定位为该领域工具的核心卖点（USP），该组织表示，编程代理现在可以成为开发者“编程化基础设施”层的一部分。

## Cursor SDK 自动化了哪些基础设施？

通过为开发者提供一种规避代理栈开销琐事的方法，Cursor SDK 测试基座提供了额外的自动化服务。

这些服务涵盖了 MCP 服务器连接、代理技能管理（其本身也是自动化的）、用于观察、控制和扩展代理“循环”（即代理经过感知、推理、行动和结果观察的过程）的钩子；以及子代理控制，用于将较小的任务委托给具有自己提示词和模型的命名子代理，这些子代理由主“[代理派生](https://thenewstack.io/hidden-agentic-technical-debt/)”驱动，即指导专门且通常孤立的代理子操作的行为。

## 代理化没有免费的午餐？

这听起来全是好消息。那么开发者对这一进展怎么看？这种新层次的抽象效率有多大吸引力，是否伴随着权衡（毕竟，世界上仍然没有免费的代理午餐）……以及有哪些需要注意的痛点？

零售软件开发公司 Faire 的高级工程经理 George Jacob 在 [Cursor 宣布这些变化的博客文章](https://cursor.com/blog/typescript-sdk)中表示，此举是从编辑器和命令行界面（CLI）并行运行多个代理的关键。

Jacob 表示：“我们对 [Cursor] SDK 感到兴奋，它是在相同的云运行时上运行我们自己的编程代理的一种途径，无需[管理虚拟机](https://thenewstack.io/from-pets-to-cattle-the-new-mindset-for-managing-vms/)或绕过内存限制，从而在不需要开发者持续干预的情况下保持代码库的健康。”

## Python 方面的周旋

Cursor 埃及社区的负责人 Khalid Abdelaty 发表了更为细致的评论。在 5 月 1 日发布的 [Cursor SDK 用户教程](https://www.datacamp.com/tutorial/cursor-sdk)中，Abdelaty 回答了 Cursor SDK 是否支持 Python 或任何其他语言的问题。

“目前官方还不支持。截至公开测试版，该 SDK 仅限 TypeScript；Python 用户应直接调用 [云代理 REST API](https://cursor.com/docs/cloud-agent/api/endpoints)，”Abdelaty 指导道。

此外，关于这项技术的鲁棒性以及它是否适用于生产环境，答案是肯定的，但有前提条件。

“首先将其用于低风险任务。SDK 的表面层仍处于公开测试阶段，”他说道。

Abdelaty 在对他已发布的说明进行扩展时告诉 *The New Stack*，对他而言，Cursor SDK 有趣的地方不仅在于它允许开发者从代码中使用 AI 代理，更在于它让这些代理更接近开发者已经工作的地方，如 CI、内部工具、GitHub 问题、代码审查和小型维护脚本。

“这很有用，但也意味着团队需要谨慎，”Abdelaty 说。“难点不仅在于编写一个好的提示词。还在于决定代理可以更改什么、哪里需要人工审核、如何处理机密信息，以及在信任更改之前需要通过哪些测试。”

Abdelaty 强调了他的想法，他表示不会以此为理由允许代理自由更改生产代码。他会从更安全的任务开始，比如修复分支上的测试、检查旧文档、总结更改或准备待审的拉取请求。他的底线是方向很明确：编程代理正开始从聊天窗口进入正常的开发工作流。

## 预期的 API 变更

Abdelaty 还指出，作用域机密（与定义的环境、项目或用户相关的敏感凭据数据）需要审核，开发者应在正式发布前“预期 API 会发生变化”。

> “考虑将该 SDK 用于生产自动化的团队应将其视为一个极具潜力但仍在变动中的平台……工具调用模式尚不稳定，应进行防御性解析。”
> ——Curtis Pyke，Kingy AI。

广泛认可的深度学习和 AI 专家 Curtis Pyke 也是 [Kingy AI](https://kingy.ai/) 的创始人。Pyke 最初持乐观态度，他表示 Cursor SDK 是试图将运行编程代理的“困难部分”进行“产品化”，即仓库上下文、工作区管理、云端执行、流式事件、模型选择、MCP 集成、子代理、钩子、工件和生命周期管理。

## 已知局限

但他在 [4 月 30 日的一份分析](https://kingy.ai/ai/cursor-sdk-review-cursors-coding-agent-becomes-programmable-infrastructure/)中警告说：“考虑将该 SDK 用于生产自动化的团队应将其视为一个极具潜力但仍在变动中的平台。Cursor 自己的文档列出了几个已知局限，[包括：] SDK 身份验证尚不支持团队管理员 API 密钥；且工具调用模式尚不稳定，应进行防御性解析。这些虽然不是致命缺陷，但它们定义了其成熟度水平。”

在 Hacker News 上发帖的 kage18 则更具前瞻性，他[写道](https://news.ycombinator.com/item?id=47750940)，这种演进“在架构上是合理的”，且 Claude Code SDK 凭借其子代理、钩子和会话管理，“为代理化使用进行了良好设计”，所有这些都能简洁地工作。

> “有趣的问题是 Cursor 在此基础上增加了什么——它的用户体验（UX）和上下文管理决策才是真正的差异化所在。”
> ——kage18.

## 差异化存在于用户体验中

“如果你要在它之上构建一个 IDE，你会想要那个基础，而不是自己重造轮子，”kage18 表示。“有趣的问题是 Cursor 在此基础上增加了什么——它的用户体验（UX）和上下文管理决策才是真正的差异化所在。”

谁将在 AI 编程平台竞赛中获胜是一个很难做出的判断。但正如 *The New Stack* 的 Matt Burns 在他的初始报道中指出的那样，Cursor 的这一进展完全取决于开发者在将其工具包与来自 Anthropic、拥有 Codex 的 OpenAI 及其与微软合作的 GitHub Copilot……以及其他前沿模型先锋的竞争技术进行比较时，如何权衡其价值。

事实上，这些供应商首先是在开发者的工作流中争夺关注度——而不是针对终端用户的最终应用功能——这未必会成为一个问题。毕竟，这是从软件工程师到消费者的自然食物链方向。一切可能最终取决于谁的扩展性最好，以及哪家供应商能最体贴地处理基于 Token 的消费定价。