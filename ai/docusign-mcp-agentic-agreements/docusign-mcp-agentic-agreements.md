<!--
title: 构建代理式协议企业：开发者如何利用 Docusign MCP 服务器开启智能体体验
cover: https://cdn.thenewstack.io/media/2026/05/05ec8bf7-getty-images-ff7vuuen6vk-unsplash-scaled-e1779371130112.jpg
summary: Docusign发布MCP服务器、协议管理器API及工具包，利用代理式AI加速协议管理。开发者可借此将协议能力集成至主流大模型，实现高效自动化的智能合约工作流。
-->

Docusign发布MCP服务器、协议管理器API及工具包，利用代理式AI加速协议管理。开发者可借此将协议能力集成至主流大模型，实现高效自动化的智能合约工作流。

> 译自：[Building the agentic agreement enterprise: How developers are unlocking agentic experiences with Docusign's MCP server and platform](https://thenewstack.io/docusign-mcp-agentic-agreements/)
> 
> 作者：Doug Sillars

在整个企业中管理协议传统上是一个缓慢、手动的过程。[Docusign 开发者中心](https://developers.docusign.com/)通过繁琐步骤的自动化加速了这一过程，但代理式 AI 的注入有望进一步加快协议管理，将其转变为敏捷、无缝且高速的工作流。

在 Docusign 的年度客户大会 [Momentum 2026](https://momentum.docusign.com/) 上，Docusign 正在通过面向开发者的关键发布来突破这一界限：Docusign MCP 服务器、协议管理器 API（Agreement Manager API）、IAM 工具包以及全新改版的开发者控制台（Developer Console）。

## MCP 服务器：让协议具备智能体就绪能力

![](https://cdn.thenewstack.io/media/2026/05/4089920a-unnamed.png)

企业内 AI 智能体面临的一个主要挑战是 LLM 平台的通用性。虽然它们能力非凡，但往往缺乏驱动关键任务业务影响所需的专业化、特定领域的机构记忆。例如，像 Claude 这样的智能体可能拥有 Docusign 协议平台的理论知识，但仍然无法实际与之交互或调用其技术能力。

Docusign [模型上下文协议 (MCP) 服务器](https://developers.docusign.com/platform/mcp-server/)使 [Docusign 智能协议管理 (IAM)](https://www.docusign.com/intelligent-agreement-management) 平台具备智能体就绪能力，允许 Docusign 的功能呈现在第三方 AI 工具中，如 [Anthropic Claude](https://claude.com/connectors/docusign)、[Google Gemini](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/docusign/set-up-data-store)、[Microsoft Copilot](https://learn.microsoft.com/en-us/connectors/docusignmcpdemo/) 和 [OpenAI ChatGPT](https://chatgpt.com/apps/docusign/asdk_app_69fcc3b7582c81918df4ffae40cb7204)，从而实现从对话到行动的跨越，无需切换标签页。

通过连接 Docusign，MCP 服务器提供了协议智能体可以据此采取行动的业务上下文和机构记忆，并作为客户和独立软件供应商（ISV）开发自定义代理式工作流的基石。

具体而言，这意味着您团队中的非技术成员只需向智能体询问他们需要的：

* “使用我们的标准 NDA 模板创建一份 NDA，并发送给 ACME 的 John Smith。”
* “找出所有包含调价条款且在未来 90 天内到期的客户合同。”

> “传统上，在 CRM、审批系统和协议平台之间自动执行续约可能需要数小时或数天的自定义集成工作。有了 MCP 服务器，终端用户只需使用自然语言，即可直接从他们已有的工作系统中生成并发送续约协议。”
>
> — Aman Dhembla，Docusign 开发者平台高级产品经理

新的实施不再需要等待开发团队。非技术团队从第一天起就可以使用自然语言处理协议。用户需要一个经过认证的 Docusign 账户才能在第三方工具中使用该连接器。

## 协议管理器 API：大规模解锁协议数据

企业拥有成百上千份协议，通常存储在多个位置。这些协议包含关键任务信息，但总的来说，它们是“暗数据”——无法大规模读取、提取或利用。Docusign 的 [协议管理器 API](https://developers.docusign.com/docs/navigator-api/)（前身为 Navigator API）提供了**大规模集中协议并从中提取洞察**的能力，将零散的合同转化为可信的、可编程的数据源。

协议管理器 API 可以通过编程方式将大量协议从不同的环境（如 SharePoint、Salesforce、遗留 CLM）上传到单一的记录系统中。一旦摄入，只需几分钟即可部署可搜索系统。协议可以整理成单一的可搜索数据源，使企业能够轻松发现影响其业务的洞察。

> “协议管理器 API 创建的集中式存储库允许组织以编程方式搜索、检索和审计其整个合同库，同时确保其主要 CRM 和 ERP 系统与其实际合同义务保持完美一致。”
>
> — Steven Baxter，Docusign API 策略高级产品经理

繁琐的手动协议搜索已成为过去。借助协议管理器 API，团队可以构建业务逻辑，从单一事实来源的所有协议中提取关键信息。绝不会错过协议续约或发票日期。报告变得自动化，协议数据从需要手动搜索的暗数据转变为安全的、可编程的接口。数小时的手动工作被压缩到几秒钟内。

![](https://cdn.thenewstack.io/media/2026/05/a31ee91d-unnamed-1-1024x735.png)

为企业客户实施 [协议管理器](https://www.docusign.com/products/platform/navigator) 通常涉及多个步骤，例如创建 20-50 多个自定义协议字段和类型、训练 AI 模型、使用额外字段扩展标准类型、测试提取准确性以及摄入大量协议。

[IAM 工具包](https://developers.docusign.com/iam-toolkit/) 使系统集成商和企业开发者能够以编程方式实施协议管理器——用可复用的基于代码的方法取代了过去减慢客户实现价值速度的手动、UI 驱动设置。

团队现在可以将协议管理配置定义为一次性的 JSON 代码，在演示账户中进行测试和完善，将验证后的配置推送到生产环境，然后通过客户系统批量摄入协议——所有这些都通过易于使用的 CLI 界面完成，从而实现更快、更可靠且可扩展的协议管理器实施。

IAM 工具包的关键功能包括自定义字段和 AI 提取逻辑的程序化**批量配置**，以及只需一条命令即可跨环境部署配置的**账户移植性**。此外，该工具包通过针对多达 400 份协议的**准确性测试**来支持可靠性，并促进直接从客户系统大规模**批量摄入**协议。

**结果：** 团队发现实施速度提高了 40%，为客户提供了极高的价值实现时间。

## 开发者控制台：在一处管理您的集成

![](https://cdn.thenewstack.io/media/2026/05/9533345c-dev-console-1.gif)

以前，开发者必须在两个断开连接的账户中管理相同的集成：用于测试的 Demo 账户和用于上线的 Production（生产）账户。这种碎片化导致上线、监控和故障排除始终依赖管理员，减慢了开发速度并使支持实时集成变得困难。为了避免管理员和开发者之间的反复沟通，许多客户授予了开发者完整的生产管理员访问权限，这带来了严重的治理和安全风险。

新的 [开发者控制台](https://developers.docusign.com/platform/create-ik-developer-console/) 通过将演示和生产体验整合到一个中心位置，并引入新的开发者角色，解决了这些问题，使管理员能够以适当的访问级别将开发者引导至生产账户。

有了这个控制台，开发者现在可以直接从生产账户内访问开发者控制台，创建集成应用以获取用于开发和测试的 Demo 客户端 ID/密钥，只需点击一下即可使集成上线，并从一个统一的仪表板监控演示和生产使用情况，从而为 Docusign 上的开发者创造更快的价值实现时间。

## Momentum 2026

[MCP 服务器](https://developers.docusign.com/platform/mcp-server/)、[协议管理器 API](https://developers.docusign.com/docs/navigator-api/)、[IAM 工具包](https://developers.docusign.com/iam-toolkit/) 以及全新的集成 [开发者控制台](https://developers.docusign.com/platform/create-ik-developer-console/) 现已可用。无论您是在 Momentum 2026 现场还是远程关注，现在都是开始构建的最佳时机。

探索 [Docusign 开发者中心](https://developers.docusign.com/)，开启一个 [免费开发账户](https://www.docusign.com/developers/sandbox)，并加入 [开发者社区](https://community.docusign.com/developer-59) 与其他构建者联系，走在未来的前沿。