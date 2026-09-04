# MCP未能解决的智能体工具难题，ARD有望补全这一环

将 AI 智能体连接到工具相对简单。然而，一旦组织在不同的云和平台中拥有成百上千种资源，事情就会变得复杂起来。代理资源发现（Agentic Resource Discovery，简称 ARD）旨在帮助智能体在这些复杂环境中找到所需资源。

AWS 在 8 月 31 日的 [Weekly Roundup](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-welcome-ducklabs-to-the-team-agentic-resource-discovery-ard-and-more-august-31-2026/) 中重点介绍了这一开放规范。在一周前深入研究其技术细节后，AWS 将其描述为“智能体的 DNS”。ARD 不需要提前告知智能体去哪里寻找资源，而是让它在不同的注册中心搜索所需的内容。

尽管 AWS 重点推荐了该项目，但 ARD 并非 AWS 的技术。它由来自 Google 的 Junjie Bu、来自 Microsoft 的 R.V. Guha 以及来自 Hugging Face 的 Shaun Smith 共同撰写，并基于 Apache 2.0 许可证发布。来自 Cisco、Databricks、GitHub、GoDaddy、[Nvidia](https://thenewstack.io/nvidia-hugging-face-acquisition-neutrality/)、Salesforce、ServiceNow 和 Snowflake 等其他多家公司的工程师也参与了该项目的制定。

AWS 的作用（至少目前为止）是提供关于该规范的反馈，并探索如何将其与自家的 Agent Registry 集成。其目标是让现有的注册中心能够协同工作。

> ARD 不需要提前告知智能体去哪里寻找资源，而是让它在不同的注册中心搜索所需的内容。

## MCP 跳过了发现步骤

[Model Context Protocol](https://thenewstack.io/mistral-mcp-connector-migration/) 已成为 AI 应用连接外部工具和数据的常用方式，但它假设客户端已经知道自己想要使用哪个服务器。随着公司将基础设施分散在不同的云、SaaS 平台和内部系统中，这成了一个问题。

ARD 在智能体尝试使用资源之前，帮助它找到该资源。该规范使用“代理资源”（agentic resource）一词来涵盖 AI 客户端可以连接的任何内容，从 MCP 服务器到其他外部功能。兼容 ARD 的服务会跟踪可用资源，而不是要求开发人员预先设置每一个连接。

> Model Context Protocol 已成为 AI 应用连接外部工具和数据的常用方式，但它假设客户端已经知道自己想要使用哪个服务器。

## 无需强制迁移的联邦制

公司可以保留自己的目录和策略，同时将搜索路由到其他兼容 ARD 的服务。例如，企业可以在需要时搜索经批准的外部目录，同时保持内部资源私有。AWS 将其称为“描述一次，随处发现”（describe once, discover everywhere）。

当前的 v0.91 提案（日期为 8 月 26 日）使用 JSON-LD 和 REST 接口。其必需的 `POST /search` 端点用于按任务进行搜索，而可选端点允许客户端浏览可用资源。

每个发现服务都可以设置自己的规则，决定返回什么内容以及信任哪些来源。这也是 AWS 将其比作 DNS 的局限所在——域名指向特定位置，而 ARD 搜索可能会出现多个看起来都能完成任务的选项。

## Route 53 工程师塑造了 ARD

这种 DNS 类比是有历史渊源的。AWS 8 月 24 日关于 ARD 的文章的三位作者中，有两位与 Route 53 密切相关。首席软件工程师 Jeffrey Damick 专注于 DNS 和网络技术，而 Bhargav Talluri 则负责管理 Route 53 的产品，以及 AWS Agent Registry 中的智能体身份与发现功能。

Agent Registry 已经为 AWS 客户提供了资源的中央视图。添加 ARD 可以将运行在其他地方的资源纳入该视图，而无需公司将所有内容都在 AWS 进行注册。

> 添加 ARD 可以将运行在其他地方的资源纳入该视图，而无需公司将所有内容都在 AWS 进行注册。

ARD 的治理工作仍在进行中，董事会条款和成员资格等细节尚未敲定。该小组还讨论了最终将该项目移交给 W3C 或 AI 基金会等中立组织的可能性。

AWS 已经在探索如何将其与 Agent Registry 连接，并[寻找其自身目录之外的资源](https://thenewstack.io/cloudflare-ai-web-economics/)。

达成统一方法的时间可能不多了，因为一旦各公司建立起自己的发现系统，连接所有这些目录将变得更加困难。