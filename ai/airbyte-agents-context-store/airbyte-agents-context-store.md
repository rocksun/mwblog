<!--
title: AI 面临严峻的数据难题，Airbyte 发布新工具一举破解
cover: https://cdn.thenewstack.io/media/2026/05/1f1fe79b-yura-timoshenko-tdarp6bcu44-unsplash-1-scaled.jpg
summary: Airbyte推出Airbyte Agents服务，通过“上下文存储”预先计算并索引企业数据，解决AI智能体因频繁调用多API导致的延迟高和Token消耗大问题，优化AI生产环境。
-->

Airbyte推出Airbyte Agents服务，通过“上下文存储”预先计算并索引企业数据，解决AI智能体因频繁调用多API导致的延迟高和Token消耗大问题，优化AI生产环境。

> 译自：[AI has a sprawling data problem. Airbyte has just launched a tool to fix it.](https://thenewstack.io/airbyte-agents-context-store/)
> 
> 作者：Frederic Lardinois

[Airbyte](https://airbyte.com) 周二推出了 Airbyte Agents，这是一项新服务，可对公司的业务数据进行预计算和索引，允许 AI 智能体（AI agents）直接查询，而不是在运行时查询多个 API。

这次发布的核心理念是，在生产环境中运行智能体的限制因素不是模型，甚至不是围绕它们的框架，而是底层数据。当智能体被连接起来通过调用半打 SaaS 工具的实时 API 来回答单个问题时，结果就是高延迟和膨胀的 Token 支出。

> 当智能体被连接起来通过调用半打 SaaS 工具的实时 API 来回答单个问题时，结果就是高延迟和膨胀的 Token 支出。

Airbyte Agents 是围绕该公司称为“上下文存储”（Context Store）的功能构建的。上下文存储不再让智能体在运行时跨 Salesforce、Zendesk、Jira 和 Slack 进行查询，而是提前将这些系统整合到一个保留了实体历史记录和当前状态的统一索引中。然后，智能体针对该索引运行查找。据 Airbyte 称，这种方法将典型的智能体任务从五六次 API 调用减少到一两次，并在此过程中削减了 Token 使用量。

Airbyte 首席执行官兼联合创始人 [Michel Tricot](https://www.linkedin.com/in/micheltricot/) 告诉 *The New Stack*：“开发者习惯于从服务和 API 的角度思考。对于智能体，你必须从随时间变化的各种状态和上下文的角度来思考。这需要在技术栈中增加一个不同的层，它位于你的数据源和智能体运行时之间，并确保一致性。”

![](https://cdn.thenewstack.io/media/2026/05/1c77263c-image-22-1024x503.png)

图片来源：Airbyte。

此次发布直接建立在 Airbyte 自 2020 年以来所做的工作基础之上。联合创始人 Tricot 和 John Lafleur 在旧金山创立了这家公司，围绕一个开源数据集成平台和一个用于将数据推送到数据仓库和湖仓的连接器库。Airbyte 现在正将同样的连接器库指向一个新的买家：构建智能体的团队，他们需要一个干净、统一的读取层，而不是另一个分析管道。

> “我们在生产中看到的大多数 AI 智能体失败案例并非模型失败，而是数据失败…… 智能体被迫在断开连接的系统中拼凑多个 API 调用，这引入了延迟、不一致性，并且经常导致相互矛盾的结果。”

Tricot 表示，当前的智能体构建模式在大规模应用时会失效。“我们在生产中看到的大多数 AI 智能体失败案例并非模型失败，而是数据失败，”他说，“智能体被迫在断开连接的系统中拼凑多个 API 调用，这引入了延迟、不一致性，并且经常导致相互矛盾的结果。”

客户可以通过两种方式访问上下文存储。第一种是 Airbyte MCP 服务器，它允许人类和智能体通过 Claude、ChatGPT、Cursor 和其他兼容 MCP 的工具提取数据，而无需编写代码。第二种是面向工程团队的 Agent SDK，他们希望对自定义智能体如何从存储中读取、可以回写什么以及权限范围如何划分进行编程控制。

> “RAG 和 API 是检索模式——它们让你在需要时获取数据…… 缺少的是一个跨系统维护关系和状态的持久化、结构化层。”

正如 Tricot 所指出的，上下文存储是现有检索方法无法提供的一个层。“RAG 和 API 是检索模式——它们让你在需要时获取数据，”他说，“缺少的是一个跨系统维护关系和状态的持久化、结构化层。没有这个层，智能体就会在运行时不断重建上下文，这是效率低下且容易出错的。”

![](https://cdn.thenewstack.io/media/2026/05/675d4dc7-image-21-1024x563.png)

图片来源：Airbyte。

上下文存储在发布时支持 50 个连接器，包括 Salesforce、HubSpot、Zendesk、Jira 和 Slack。Airbyte 目录的其余部分将在未来几个月内上线。

此举将 Airbyte 带入了一个非常拥挤的领域。例如，Composio 的业务围绕连接器目录和专门针对 AI 智能体的 MCP 网关构建，通过 MCP 公开了数百个工具包。Zapier 的 MCP 服务器也将其实际的集成库连接到任何兼容 MCP 的客户端。

Fivetran 是 Airbyte 在 ELT 领域最直接的竞争对手，也一直在将其平台推向 AI 工作负载。与此同时，像拥有 Agentforce 的 Salesforce 和 ServiceNow 这样垂直整合的现有厂商，正将自己的云服务宣传为智能体天然的真理来源。Airbyte 的观点是，对于数据通常已经分布在许多这些系统中的公司来说，一个连接器丰富、厂商中立的数据层更有意义。

Airbyte 还通过 Automations 涉足另一个日益繁忙的领域，这是一个视觉构建器，用于在上下文存储之上无需代码即可组合智能体工作流。它目前处于研究预览阶段。视觉智能体构建器市场已经包括 Langflow 和 Flowise 等开源项目，以及来自 Zapier、微软（Copilot Studio）和一长串初创公司的 SaaS 产品。Airbyte 在此的卖点是，Automations 直接构建在为其平台其他部分提供支持的相同上下文存储和连接器目录之上，而不是重新发明这两者。

## 可用性

现有的 Airbyte 付费客户可以获得三个月的 Airbyte Agents 访问权限（受按量计费限制），计费单位是公司称为“智能体操作”（Agent Operations）的新单位，涵盖读取、搜索、写入操作和推理调用。