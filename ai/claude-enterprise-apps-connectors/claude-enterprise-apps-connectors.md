<!--
title: 完整应用现在可以直接在Claude内部打开
cover: https://cdn.thenewstack.io/media/2026/03/21bf8ca8-screenshot-2026-03-27-at-12.21.10-1024x670.png
summary: Anthropic推出新功能，允许Claude直接在对话中打开并操作完整的企业应用界面。基于MCP Apps架构，该更新支持Adobe、Atlassian等工具，并引入了会议、白板和数据查询等企业级功能，进一步推动AI在企业中的深度应用。
-->

Anthropic推出新功能，允许Claude直接在对话中打开并操作完整的企业应用界面。基于MCP Apps架构，该更新支持Adobe、Atlassian等工具，并引入了会议、白板和数据查询等企业级功能，进一步推动AI在企业中的深度应用。

> 译自：[Full apps open inside Claude](https://thenewstack.io/claude-enterprise-apps-connectors/)
> 
> 作者：Amanda Caswell

**Anthropic 正在扩大 Claude 直接在** 企业应用程序中工作的能力；它现在可以打开完整的软件界面、检索信息并进行更改，而无需用户在应用程序之间切换。

周二在旧金山举行的 [The Briefing: Work at the Frontier](https://www.anthropic.com/events/the-briefing-work-at-the-frontier-ls) 上，该公司宣布了扩展的交互式连接器，以及用于会议、电子表格、共享工作空间和业务数据的新工具。

“多年来，我们一直在学会围绕软件工作。现在，Claude 围绕着你工作，”Anthropic 首席产品官 [Ami Vora](https://www.linkedin.com/in/amvora/) 在为该活动准备的演讲中说道。

> “多年来，我们一直在学会围绕软件工作。现在，Claude 围绕着你工作，”

## 完整应用现在可以直接在 Claude 内部打开

Anthropic 的[交互式连接器](https://claude.com/resources/articles/interactive-connectors-full-tool)以前允许用户在 Claude 中查看已连接应用的小预览。现在，他们可以在对话中打开并操作完整的应用程序，首批支持 Adobe、Atlassian 和 HubSpot。

例如，Claude 可以直接编辑 Confluence 页面，或者使用公司品牌套件中的素材更新 Adobe 设计。用户仍然需要在 Claude 执行这些更改之前对其进行批准。

## 基于 MCP Apps 构建

扩展的连接器构建在 [MCP Apps](https://modelcontextprotocol.io/docs/extensions/apps) 之上，它允许 MCP 服务器提供交互式界面，而不仅仅依赖 Token 调用。开发人员可以使用应用工具和嵌入式网站将现有的应用程序界面引入 Claude，而无需为助手重新构建它们。这些新功能处于公开预览阶段，并且不限于 Claude，因为其他支持 MCP Apps 的 AI 客户端也可以使用它们。

> 这些新功能处于公开预览阶段，并且不限于 Claude，因为其他支持 MCP Apps 的 AI 客户端也可以使用它们。

Anthropic 表示，Claude 市场现在包含 9,000 多个连接器和插件，延续了[将 AI 系统与企业基础设施连接起来](https://thenewstack.io/mcp-sql-the-secret-weapon-to-connect-ai-to-enterprise-systems/)的努力。对于没有受支持连接器的应用程序，Claude 可以使用其内置浏览器与其进行交互。

## 现有权限依然适用

该公司表示，连接器遵循员工在底层应用程序中已有的权限。例如，无法访问特定 Google Drive 文档的用户无法通过 Claude 检索它。

管理员还可以限制单个连接器的功能，包括允许 Claude 读取 Slack 消息但没有发送消息的权限。

此外，Anthropic 正在推出测试版的 Claude 自动连接功能，这是一种十分钟的设置，允许管理员在整个组织中启用连接器，而无需员工单独配置。同时，智能报告让管理员能够深入了解团队的使用情况、完成的工作和支出。

## Claude 数据获得认证查询

在 10 月推出 [Claude 仪表板](https://thenewstack.io/claude-dashboards-data-motion/)之后，Anthropic 还正式推出了 Claude 数据服务。

> 该更新引入了认证查询，允许数据团队批准 Claude 用于报告的查询，以便不同团队从相同的数据中获得一致的数字。

该 update 引入了认证查询，允许数据团队批准 Claude 用于报告的查询，以便不同团队从相同的数据中获得一致的数字。第二项功能是实时共享，允许员工访问更新后的仪表板，而无需直接访问底层数据源。

这两项功能仍处于测试阶段。Anthropic 尚未详细说明其如何处理认证查询的版本控制或对源数据架构的更改。

## 任务委派超越工程领域

Anthropic 表示即将推出的 Claude Meetings 将加入视频通话，以创建项目计划、回答问题并从连接的应用程序中检索信息。该功能计划面向团队和企业客户推出，但不会对使用零数据保留、符合 HIPAA 的配置或客户管理加密密钥的组织开放。

另一项功能 Claude Whiteboards 为团队提供了一个与 Claude 共同开发项目的共享空间，而 Claude Sheets 则让他们能够共同构建和编辑电子表格。两者都在付费计划中提供测试版。

## 企业采用超越工程领域

在 Datadog，产品经理正在使用 Claude 开发产品需求文档和可测试的原型。该公司技术合作伙伴负责人 [Uday Tennety](https://www.linkedin.com/in/udaytennety/) 表示，这种方法缩短了从最初想法到可用原型之间的时间。

Anthropic 还报告称，Mercado Libre 已将 Claude 部署到 26,000 多名员工，其中 78% 的人每周都在使用它。这些数字尚未经过独立验证。

这篇文章最初发布在 [The New Stack](https://thenewstack.io) 上：[Anthropic 想要让 Claude 成为你整个企业应用栈的前端](https://thenewstack.io/claude-enterprise-apps-connectors/)