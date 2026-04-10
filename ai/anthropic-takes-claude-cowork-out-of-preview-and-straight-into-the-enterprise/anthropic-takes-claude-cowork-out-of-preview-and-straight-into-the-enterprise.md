<!--
title: Anthropic正式发布Claude Cowork：全面进军企业级AI智能体市场
cover: https://cdn.thenewstack.io/media/2026/04/6e6875bd-cowork-ga-yt-x-thumbnail-1920x1080-1.png
summary: Anthropic 宣布 Claude Cowork 结束预览正式商用。该工具允许非技术人员通过 AI 智能体自动化文档和流程。新版增强了权限管理、可观测性及 Zoom 集成等企业功能，旨在与微软、OpenAI 竞争。
-->

Anthropic 宣布 Claude Cowork 结束预览正式商用。该工具允许非技术人员通过 AI 智能体自动化文档和流程。新版增强了权限管理、可观测性及 Zoom 集成等企业功能，旨在与微软、OpenAI 竞争。

> 译自：[Anthropic takes Claude Cowork out of preview and straight into the enterprise](https://thenewstack.io/anthropic-takes-claude-cowork-out-of-preview-and-straight-into-the-enterprise/)
> 
> 作者：Frederic Lardinois

Anthropic 周四将其 [Claude Cowork](https://thenewstack.io/anthropic-accelerates-its-cowork-enterprise-play/) 工具[结束预览](https://claude.com/blog/cowork-for-enterprise)并正式商用（GA）。该工具允许非开发人员将任务和工作流委托给基于 Claude 的智能体。

这项仅在几个月前推出的服务，现在已在所有 Claude 付费方案（Pro、Team、Enterprise）中全面开放。

当 Claude Code 走红时，许多开发人员意识到它不仅是一个有趣的 CLI 编程工具，对于处理非编程任务，尤其是涉及本地文件系统的任务也大有裨益。Cowork 的核心就是这种能力，但作为 Claude 桌面应用的一部分，它拥有更友好的用户界面。它让 Claude 模型脱离了 Claude.ai 的聊天模式，使其能够端到端地处理任务，包括处理文本文件和电子表格。

Anthropic 在公告中写道：“Claude Cowork 的绝大部分使用来自工程团队之外。重要的是，运营、市场、财务和法律等职能部门并不是将核心工作交给 Claude，而是处理围绕其最关键任务的外围工作——如项目更新、协作幻灯片、调研冲刺等。”

## 打造企业级 Cowork

通过此次发布，Anthropic 强调 Cowork 已经为企业做好了准备。针对这些用户，公司还增加了一系列企业一直要求的额外功能。

“阻碍 Claude Cowork 全面推向企业的不是产品，而是首席信息官（CIO）在规模化批准任何项目之前所需的治理层。今天的发布填补了这一空白，”一位 Anthropic 发言人在邮件中告诉我们。

这些新的企业功能包括对企业来说可能最重要的功能：基于角色的访问控制（RBAC）。通过此次更新，企业管理员现在可以将用户组织成组，可以采用手动方式（这对于大型组织来说并不理想），也可以通过其现有身份提供商的跨域身份管理（SCIM）功能进行操作。

此外，管理员现在可以细粒度地限制每个 MCP 工具可用的操作。例如，这意味着他们可以允许 Gmail 连接器读取电子邮件，但不允许发送邮件。

其他新功能包括为团队设置预算的能力（适用于使用 API 的用户），以及使用情况分析，包括每用户活动、技能使用情况以及常规的日/周/月活跃用户报告。

通过此次更新，Cowork 现在还支持 OpenTelemetry，因此团队可以获取关于正在使用哪些工具、技能和连接器等数据的详细信息，企业随后可以将这些数据拉入其现有的分析管道中（此功能仅适用于 Team 和 Enterprise 方案的用户）。

由于在企业工作遗憾地意味着要参加超负荷（或不必要）的会议，因此很高兴看到 Cowork 现在还配备了 Zoom MCP 连接器。这带来了会议摘要、待办事项以及会议转录。

GA 版的发布正值智能体桌面类别竞争升温之际。微软在 3 月份推出了 Copilot Cowork，它基于与 Anthropic 产品相同的 Claude 引擎和智能体框架构建，但 Copilot Cowork 在客户 M365 租户内的云端运行。这也意味着微软所有内置的治理功能都将覆盖 Copilot Cowork。

谷歌的 Gemini Agent Mode 和 OpenAI 的 Operator 也在争夺同样的非开发人员工作流自动化市场。