<!--
title: Claude 现可跨 Outlook、Word、Excel 和 PowerPoint 协作
cover: https://cdn.thenewstack.io/media/2026/05/7ce6a399-manaa-graphic-wrlewny994u-unsplash-scaled.jpg
summary: Anthropic 扩展了 Claude 对 Microsoft 365 的集成，新增 Outlook 插件并全面开放 Word、Excel 和 PowerPoint 支持。用户可在单一对话中跨应用保留上下文，实现高效协同办公。
-->

Anthropic 扩展了 Claude 对 Microsoft 365 的集成，新增 Outlook 插件并全面开放 Word、Excel 和 PowerPoint 支持。用户可在单一对话中跨应用保留上下文，实现高效协同办公。

> 译自：[Claude can now follow users across Outlook, Word, Excel, and PowerPoint](https://thenewstack.io/claude-word-excel-powerpoint-outlook-microsoft-office/)
> 
> 作者：Paul Sawers

Anthropic 正在扩展 Claude 在 Microsoft 365 中的触达范围，[新增 Outlook 支持](https://support.claude.com/en/articles/14855664-use-claude-for-outlook)，同时将 Word、Excel 和 PowerPoint 的集成推向全面开放（General Availability）。

此次更新意味着 Claude 现在可以在单个持续对话中跨电子邮件、文档、电子表格和幻灯片跟踪工作，允许上下文在用户切换应用时得以延续。

这一发布基于 Anthropic 在 [2 月份公布](https://thenewstack.io/anthropic-accelerates-its-cowork-enterprise-play/)的 Microsoft 365 推进计划，该计划引入了 Excel 和 PowerPoint 之间的共享上下文，以及针对 [Claude Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/) 更广泛的插件生态系统。此次扩展将 Claude 进一步推向日常办公工作流，特别是微软的生产力套件内部。

> “Claude 现在可以在单个持续对话中跨电子邮件、文档、电子表格和幻灯片跟踪工作，允许上下文在用户切换应用时得以延续。”

## **一个聊天窗口，四个应用**

最大的亮点是 Outlook，它作为 Claude 最新的 Microsoft 365 界面进入公开测试阶段。

Anthropic 表示，Claude 现在可以在同一对话线程中同时参考电子邮件以及电子表格、演示文稿和文档。

![Outlook 中的 Claude](https://cdn.thenewstack.io/media/2026/05/db2ade52-outlook.gif)

*Outlook 中的 Claude*

与此同时，Claude 的 Word 集成在 [4 月悄然进入测试阶段](https://www.linkedin.com/posts/claude_claude-for-word-now-in-beta-activity-7448436011535204352-8sus/)后，现已全面开放。Claude for Word 可以直接在侧边栏起草、编辑和修改文档，同时保留格式并将修改显示为修订追踪。

值得注意的是，这些集成旨在跨应用共享上下文。例如，Claude 可以从 Outlook 切换到 Word，同时保留早前工作流中收集的对话、邮件和待办事项。

![在 Outlook 和 Word 之间使用 Claude](https://cdn.thenewstack.io/media/2026/05/e5b9cce1-outlooktoword.gif)

*在 Outlook 和 Word 之间使用 Claude*

在整个套件中，用户可以先在 Outlook 中处理收件箱，要求 Claude 从 Excel 的附加表格中提取关键数据，在 Word 中生成一份面向客户的摘要，然后使用相同的底层上下文更新 PowerPoint 演示文稿——而无需在应用之间反复重新解释任务。

Claude 还可以同时处理多个打开的文件。Anthropic 表示，电子表格、文档和演示文稿可以并排保持打开状态，而 Claude 会在它们之间传递修改和上下文。对话也会按文件持久化，允许用户稍后返回同一文档或工作流，而无需重新开始对话。

这种连续性也可能引发关于监管和数据泄露的新问题，特别是随着 AI 助手获得更广泛的内部业务背景访问权限。在 [博文](https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) 中，Anthropic 指出，在 Claude 代表用户发送或安排任何内容之前，用户仍负责批准外部操作。

该公司写道：“你在每一条回复和会议邀请发出之前都会进行检查，除非你点击发送，否则什么都不会发出。”

## 一场企业级的博弈

这里蕴含的更广泛机遇不容忽视。尽管过去两年出现了大量独立的 AI 产品，但大部分企业工作仍流向微软的生产力堆栈——Outlook 收件箱、Excel 模型、PowerPoint 幻灯片和 Word 文档，这些在大型组织中仍然根深蒂固。

正如[一位领英评论者](https://www.linkedin.com/feed/update/urn:li:ugcPost:7458211439950983168?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7458211439950983168%2C7458218247184732160%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287458218247184732160%2Curn%3Ali%3AugcPost%3A7458211439950983168%29)在发布后所说：“内置于 Office 的 Claude，是大多数企业 AI 方案错失的切入点（wedge）。”

> “内置于 Office 的 Claude，是大多数企业 AI 方案错失的切入点。”

这一观察揭示了企业级 AI 领域正在发生的更广泛转变。各家公司都在竞争谁能嵌入到工作已经发生的日常软件环境中——而在这个领域，没有比微软更大的玩家了。

Claude for Excel、PowerPoint 和 Word 现已在 Windows 和 macOS 的付费计划中全面开放，而 Claude for Outlook 目前处于公开测试阶段。组织可以通过微软的 AppSource 市场和微软管理中心部署这些集成。

Anthropic 表示，企业客户还可以配置 OpenTelemetry 支持，以监控跨应用的提示词、工具调用和文档引用，而分析工具可以按用户、应用和日期细分使用情况。

组织可以直接通过 Claude 账户访问这些加载项，也可以使用托管在 Amazon Bedrock、Google Vertex AI 或 Microsoft Foundry 上的 Claude 模型，通过现有的企业级 AI 基础设施路由请求。