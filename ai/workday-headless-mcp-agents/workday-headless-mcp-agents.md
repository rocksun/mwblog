<!--
title: Workday走向无头架构，向外部AI智能体开放HR与财务数据
cover: https://cdn.thenewstack.io/media/2026/10/84b59105-workday_work-scaled.jpg
summary: Workday在拉斯维加斯会议上宣布其可信智能体平台实现无头化，允许开发者通过Claude Code和Cursor等工具直接访问HR与财务数据。该平台依托MCP服务器和实时数据查询，确保所有外部智能体严格遵循用户的权限与审计追踪，保障企业数据安全。
-->

Workday在拉斯维加斯会议上宣布其可信智能体平台实现无头化，允许开发者通过Claude Code和Cursor等工具直接访问HR与财务数据。该平台依托MCP服务器和实时数据查询，确保所有外部智能体严格遵循用户的权限与审计追踪，保障企业数据安全。

> 译自：[Workday goes headless, opening its HR and finance data to outside AI agents](https://thenewstack.io/workday-headless-mcp-agents/)
> 
> 作者：Frederic Lardinois

Workday正在开放其平台，允许开发者在 Claude Code、Cursor 和其他工具中构建他们自己的 HR 和财务智能体，只要这些智能体遵循与使用它们的人相同的规则。

周二，在拉斯维加斯举行的 Workday Rising 大会上，该公司将其可信智能体平台（Trusted Agent Platform）变为“无头（headless）”架构。

随着这一举措的推出，其[模型上下文协议](https://modelcontextprotocol.io)（MCP）服务器、对实时 Workday 数据的 SQL 访问权限以及智能体共享运行时现在已全面上市（Generally Available），客户可以在 Anthropic、Google、Meta、Mistral、Nvidia 和 OpenAI 的模型上运行他们自己的智能体。

正如 Workday 首席技术官 Gabe Monroy 在活动前的新闻发布会上所指出的那样：“无论谁构建了智能体，它都在 Workday 的权限、审批和审计追踪下运行——没有任何智能体能走捷径（后门）。”

Workday 指出，许多公司目前通过数据湖中的副本或服务账户将智能体连接到 HR 和财务数据，但该公司认为，这些方法绕过了访问控制（尽管像 [SAP](https://thenewstack.io/sap-acquires-techwolf-skills/)、微软和其他公司肯定也会辩称他们同样实施了访问控制）。

对于 AI 开发者来说，Workday 生态系统的主要入口是 Agent-Ready Tools。这是该公司的 MCP 服务器，作为 Workday Extend AI 的一部分提供。用户使用自己的 Workday 凭证登录，Workday 表示，代表他们行动的智能体无法访问其自身账户无法访问的内容。这是一个关键功能，它将智能体直接绑定到用户的账户。

Monroy 表示，该服务器目前提供 275 个读取工具和 54 个写入或删除数据的工具。

实时数据查询（Live Data Query）是 Workday Data Cloud 的一部分，它允许 BI 工具和智能体直接针对 Workday 的对象图运行 SQL 查询。Monroy 将其描述为对 Workday 对象图的 JDBC 访问，该公司表示，每个查询只返回请求用户被授权看到的内容。

今天还有三个组件全面上市。Agent Harness 是一个共享运行时，Workday 自己的智能体以及由客户和合作伙伴构建的智能体都在其上运行。它向每个智能体传递用户的身份、组织职位和访问权限，限制智能体可以做的事情，并根据成本和性能选择哪个模型处理每个任务。Developer Agent 从 Claude Code、Codex、Cursor 或 Workday 开发者网站中的自然语言提示生成 Workday 智能体和应用程序。Custom Agents 允许团队将他们用 LangChain 或谷歌智能体开发套件（ADK）构建的智能体部署到 Agent Harness 上，不过 ADK 支持目前仅限于设计合作伙伴。

路线图上还有另外两个组件预计在 2027 年初进行抢先体验。Agent Context Service 将仅预加载任务调用的 Workday data，Workday 称这可以加速智能体并限制其接触敏感记录。Grounded Reasoning 将在智能体执行计划操作之前，根据客户的政策、流程规则和 Workday 记录对其进行检查。

Workday 表示，在过去的四个月里，客户已经使用 Developer Agent 和 Agent-Ready Tools 构建了 500 多个智能体和 6000 多个应用程序。

## “无头，无法无天的方式”

在发布会上，Monroy 演示了他所谓的“无头，无法无天的方式”。一个连接到自定义 MCP 服务器的智能体——他称这是 Workday 目前在客户中常见的一种设置——返回了其用户无权查看的职位空缺申请，然后在未经批准的情况下将错误的员工在团队之间调动。当指向 Snowflake 中的 Workday 数据副本时，同一个智能体在被问及合规问题时泄露了首席技术官的薪水。

Monroy 说：“当它失败时，不仅仅是一个错误的答案，而是一个没有人批准的错误行动。”

相反，当智能体通过 Workday 自己的 MCP 服务器和 Data Cloud 进行查询且用户已登录时，毫无意外地，相同的查询仅返回该用户被允许看到的申请（当然，否则就无法很好地演示这些访问控制了）。

## “一小部分用例”

当被问及无头架构对 Workday 的重要性是否与对 Salesforce 一样大时，Workday 产品与技术总裁 Gerrit Kazmaier 表示，Workday 正在给客户提供选择：“如果他们使用我们的用户界面，我总是更倾向于此，但无头架构同样出色。”

Kazmaier 指出，直接在 Workday 的工具和 API 上构建智能体“只适用于不需要 HR 或财务领域逻辑的一小部分用例”。对于其他所有情况，他提到了 AI 到 AI 的集成，其中 Claude 将请求交给 Workday 的智能体协调器 Sana，然后由 Sana 调用 Workday 自己的领域智能体。

## 用于分析的数据湖，而非智能体

值得注意的是，Snowflake 的示例对 Workday 来说有点尴尬。当该公司在 2025 年 9 月[宣布推出 Data Cloud](https://newsroom.workday.com/2025-09-16-Workday-Introduces-Workday-Data-Cloud-to-Unlock-the-Power-of-People-and-Money-Data-and-Accelerate-AI-Powered-Innovation) 时，其宣传点包括与 Databricks、Salesforce 和 Snowflake 进行 Workday 数据的零复制共享。Snowflake 于 10 月 7 日使其 Workday Data Cloud 集成[全面上市](https://docs.snowflake.com/en/release-notes/2026/other/2026-10-07-workday-data-cloud-zerocopy-ga)，而 Databricks 在一天后将其[用于 Unity Catalog 的 Workday 连接器](https://www.databricks.com/blog/announcing-workday-data-connect-federation-unity-catalog)投入公开测试版。

据 Databricks 称，Workday 管理员通过注册集成系统用户（ISU）来设置连接器，这是 Workday 客户用于传统集成的系统账户，具有对共享表的读取权限。之后，目录、架构和表级别的 Unity Catalog 权限决定了谁可以查询数据。

Monroy 表示，数据湖对于分析以及将 Workday 数据与公司其余数据结合仍然有意义，但外部数据湖是“构建需要 Workday 受控访问的智能体的错误地方”。

他说：“你可以导出数据，但无法导出管理数据的规则，”并补充说在数据湖中重建这些规则意味着“维护 Workday 安全模型的第二个副本”，“一旦它发生漂移，一切就都错了。”

## 大家都“失去理智（Headless）”了

看起来，无头架构是目前的潮流。例如，Salesforce、ServiceNow 和微软已经允许外部智能体进入其记录系统。Salesforce 在 4 月的 TDX 开发者大会上[推出了 Headless 360](https://www.theregister.com/saas/2026/05/28/salesforce-waves-bye-bye-to-ui-in-headless-embrace/5247587)，因此 Claude、ChatGPT、Cursor 或终端中的智能体可以与 Salesforce 数据协同工作。ServiceNow 在 5 月份将其[Action Fabric MCP 服务器](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx)全面上市，Anthropic 作为启动合作伙伴，微软则提供了[用于 Dynamics 365 ERP 的 MCP 服务器](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/copilot-mcp)。

所有四家供应商都表示，外部智能体仍然保留在其现有的[权限模型](https://thenewstack.io/mcp-ai-agents-api/)之内。

## 智能体使用的是谁的身份？

当谈到[智能体身份](https://thenewstack.io/mcp-security-permissions-overhaul/)时，不同的供应商目前采取了截然不同的方法。

例如，[据 Salesforce Ben 报道](https://www.salesforceben.com/salesforce-will-charge-flex-credits-for-agentic-mcp-and-api-calls/)，Salesforce 正在准备让通过 MCP 或其 API 连接的智能体使用自己的凭证和权限进行注册，而不是在用户的身份下运行。MCP 客户端最终将需要切换到绑定到这些智能体身份的 OAuth 凭证。

Workday 的[文档](https://doc.workday.com/admin-guide/en-us/workday-ai/agents/agent-system-of-record/agent-security-and-compliance/faq--agent-security.html)称，其智能体已经可以获得最多两个自己的系统账户，称为智能体系统用户（ASU），一个用于代表用户行事，另一个用于“环境（ambient）”工作，每个账户都有自己的 [OAuth 2.0 客户端](https://thenewstack.io/descope-brings-oauth-to-ai-agents-and-mcp-servers/)。当客户开启环境技能时，Workday 会自动创建环境账户。

销售 Workday MCP 集成的 Unified.to 表示，每个 Workday MCP 路径，“无论官方与否”，[都从创建 ISU 开始](https://unified.to/blog/how_to_get_started_with_a_workday_mcp_server)。Cequence 的 Workday MCP 集成[设置指南](https://docs.aigateway.cequence.ai/docs/applications/hr-operations/workday-hcm/)要求客户创建一个“具有适当安全组”的账户。通过 ISU 工作的智能体可以看到这些安全组允许的任何内容，无论是谁在提示它。

更有说明意义的信号可能是 Kazmaier 的警告。如果直接在 MCP 服务器上构建仅适用于一小部分用例，那么 Workday 期望大多数客户使用的无头版本是：Claude 与 Sana 对话，Sana 再与 Workday 自己的智能体对话，而 Workday 的运行时位于每次调用的中间。