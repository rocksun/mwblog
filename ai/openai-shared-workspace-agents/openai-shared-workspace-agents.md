<!--
title: OpenAI发布全天候智能体，彻底消除团队手动交接摩擦
cover: https://cdn.thenewstack.io/media/2026/04/e5f4eba3-tri-wiranto-zm8g3xrrrd4-unsplash-scaled.jpg
summary: OpenAI推出“工作区智能体”（workspace agents），支持跨工具自主运行，旨在消除团队手动交接。该工具基于GPT-5.5，可集成至Slack等平台，处理多步复杂任务，助力企业实现自动化协作。
-->

OpenAI推出“工作区智能体”（workspace agents），支持跨工具自主运行，旨在消除团队手动交接。该工具基于GPT-5.5，可集成至Slack等平台，处理多步复杂任务，助力企业实现自动化协作。

> 译自：[OpenAI debuts always-on agents to end the friction of manual team handoffs](https://thenewstack.io/openai-shared-workspace-agents/)
> 
> 作者：Paul Sawers

OpenAI 正在将 ChatGPT 进一步推向公司的日常运营，本周[推出](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)了共享的“[工作区智能体](https://openai.com/academy/workspace-agents/)”（workspace agents），它们可以跨工具执行任务，并在无需持续输入的情况下持续运行。此举正值该公司[推出最新的 GPT-5.5 模型](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/)之际，这是其推动系统处理更复杂、现实世界工作的一部分。

该新功能由 [OpenAI 的编程智能体](https://thenewstack.io/openais-codex-gets-plugins/) Codex 驱动，允许团队构建处理多步工作的智能体，如起草报告、分拣请求或回复消息，并使用组织内部可用的数据和工具。与依赖来回提示模式的早期 ChatGPT 版本不同，这些智能体旨在接收任务并将其完成。

***另请参阅：[OpenAI 发布 GPT-5.5，称其为“新一类智能”。](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/)***

OpenAI 表示，这些智能体在云端运行，可以在团队中共享，允许多人随着时间的推移使用和完善同一个系统。它们还可以部署在 Slack 等工具中，在那里它们可以根据工作的到来响应请求或触发操作。

![共享工作区智能体](https://cdn.thenewstack.io/media/2026/04/54e3933d-oai_blog_agents_library_image5_workspace_agents-1024x631.png)

***共享工作区智能体***

## 团队协作

OpenAI 一段时间以来一直在 ChatGPT 中[构建](https://openai.com/index/introducing-chatgpt-team/)以团队为中心的功能。ChatGPT Enterprise 和 ChatGPT Business 等产品引入了共享环境，而[自定义 GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts) 则允许团队为特定任务创建量身定制的助手。

> “工作区智能体是 GPTs 的进化版。” —— OpenAI

工作区智能体建立在这一概念之上。它们不再只是响应提示，而是被设置为遵循定义的流程：从连接的系统中收集信息并返回结果。在某些情况下，这可能涉及汇总周报、筛选销售线索或根据公司政策审查内部请求。

OpenAI 表示，团队可以通过在 ChatGPT 内部描述工作流来构建这些智能体，然后系统会引导用户连接工具、定义步骤并测试系统。智能体还可以计划在特定时间运行，或自动响应传入的请求。

根据 OpenAI 的说法，自定义 GPTs 将保持可用，并计划随着时间的推移允许团队将它们转换为智能体。

## 共享上下文，共享系统

向共享智能体的转变反映了将 AI 从个人使用转向团队流程的更广泛努力。例如，Notion 正在[通过自定义智能体探索类似的想法](https://www.notion.com/en-gb/blog/introducing-custom-agents)，构建跨内部文档、工具和通信渠道运行的系统。

在 OpenAI 的案例中，智能体利用包含文件、代码、连接的应用程序和记忆的工作区。这允许它们跨不同系统工作，同时跟踪之前的步骤，而不是每次都从头开始。

> “AI 已经帮助人们独自工作得更快，但组织内部许多最重要的工作流程依赖于团队之间的共享上下文、交接和决策。工作区智能体正是为这种工作而设计的。” —— OpenAI

OpenAI 表示，团队可以使用自己的工具、数据源和内部流程来自定义智能体。该公司还强调了内部的早期用例，包括编制销售笔记、生成报告以及在 Slack 频道中回复员工查询的智能体。

![Slack 中运行的工作区智能体](https://cdn.thenewstack.io/media/2026/04/2e571e11-slack-1024x580.png)

***Slack 中运行的工作区智能体***

## 控制与监督

随着这些系统承担更多责任，OpenAI 也在增加对智能体可以访问和执行的操作的控制。

团队可以设置围绕工具和数据的权限，并要求对某些操作（如发送电子邮件或修改文件）进行审批。管理员可以监控智能体的使用情况，包括它们的运行频率以及与之交互的系统。合规 API 提供了对智能体配置和活动的可见性。

这种对监督的关注源于 AI 系统正被用于处理更敏感的内部数据。OpenAI 还在开展相关的隐私保护工作，包括其[开源的 OpenAI 隐私过滤器](https://openai.com/index/introducing-openai-privacy-filter/)，旨在过滤或限制 AI 系统处理数据的方式。

工作区智能体正在面向 ChatGPT Business、Enterprise 和教育版计划发布研究预览版，定价定于 5 月转向基于额度的模式。