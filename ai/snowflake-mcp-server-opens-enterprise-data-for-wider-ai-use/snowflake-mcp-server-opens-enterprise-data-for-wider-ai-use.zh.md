[![Snowflake 标志](https://cdn.thenewstack.io/media/2025/10/9918c534-snowflake-300x225.png)](https://cdn.thenewstack.io/media/2025/10/9918c534-snowflake-300x225.png)

Snowflake 标志

数据云 [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) 为其 Snowflake Cortex AI 服务配备了新的 [MCP 服务器](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)，以及一套第三方集成，旨在帮助金融服务公司更好地利用其在 Snowflake 云中的数据。

“我们正在简化构建可信 AI 的过程，并将其扩展到用户所在的地方，” Snowflake AI 副总裁 Baris Gultekin 在接受 TNS 采访时表示。

客户服务、投资分析和理赔管理都可以通过使用这些服务得到简化。

## Snowflake 的 MCP 服务器

Snowflake MCP 服务器是一项目前处于预览阶段的托管服务，它允许 Snowflake 用户不仅可以连接到他们自己的数据，还可以连接到来自 Nasdaq 和美联社等合作伙伴的第三方数据，例如市场分析、专家研究、商业内容和新闻。然后，Snowflake 用户可以将这些数据输入到 AI 应用程序和代理平台中，例如 [Anthropic](https://thenewstack.io/anthropic-launches-claude-sonnet-4-5/)、[Cursor](https://thenewstack.io/install-cursor-and-learn-programming-with-ai-help/) 和 Salesforce 的 Agentforce，以实现此前未实现的益处。

MCP 基于服务器-客户端架构。客户端嵌入在 AI 应用程序中。服务器公开了一组工具，或者说可执行函数（例如查询数据库），供客户端使用。

基于 [MCP 规范](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/)，Snowflake 的 MCP 服务器是一项由 Snowflake 管理的服务，允许用户创建自己的 MCP 服务器对象，在服务器配置中指定工具和元数据。标准的 Snowflake [基于角色的访问控制](https://thenewstack.io/three-realistic-approaches-to-kubernetes-rbac/)（RBAC）保护服务器对象。Snowflake 管理 MCP 服务器本身，确保操作符合客户的安全和隐私限制。

[![MCP 原语](https://cdn.thenewstack.io/media/2025/10/b2ded806-mcp-primitives.png)](https://cdn.thenewstack.io/media/2025/10/b2ded806-mcp-primitives.png) MCP 原语 (Snowflake)

MCP 客户端在通过 [OAuth 2.0](https://docs.snowflake.com/en/user-guide/oauth-snowflake-overview) 进行必要的身份验证后，可以连接到服务器，并通过标准 MCP 程序发现和调用工具：

[![Snowflake MCP 工具发现。](https://cdn.thenewstack.io/media/2025/10/43ca2f96-snowflake-mcp-discovery.png)](https://cdn.thenewstack.io/media/2025/10/43ca2f96-snowflake-mcp-discovery.png) MCP 工具发现。

## 面向金融服务的 Cortex AI

面向金融服务的 Cortex AI 是为 Snowflake 的 MCP 服务器而创建的一套 AI 工具，旨在让金融用户更容易在基于代理的应用程序中使用自己的数据，这些应用程序既可用于他们自己的客户，也可由他们的员工构建。

除了 MCP 服务器访问客户数据外，它还可以利用第三方数据，包括结构化和非结构化数据。

结构化数据提供商 CB Insights、Cotality、德意志交易所、MSCI 和 Nasdaq eVestment 将通过[语义视图共享](https://docs.snowflake.com/en/user-guide/views-semantic/semantic-view-sharing)进行访问，该功能很快将作为 Snowflake AI 平台 [Cortex](https://thenewstack.io/stack-overflow-on-snowflake-cortex-answers-without-attitude/) 的一部分普遍可用。

Snowflake 认为，将公司自己的数据与第三方数据源结合，并通过大型语言模型（LLM）处理，可以为公司提供独一无二的有价值信息。

[![Snowflake 合作伙伴](https://cdn.thenewstack.io/media/2025/10/604af955-snowflake-partners.png)](https://cdn.thenewstack.io/media/2025/10/604af955-snowflake-partners.png)

CB Insights、FactSet、Investopedia、美联社和《华盛顿邮报》等非结构化数据发布商将通过 [Cortex 知识扩展](https://www.snowflake.com/en/blog/easy-button-context-rich-ai-agents/)提供。

## 利用 Cortex

用户还可以引入其他 Cortex 服务：[Snowflake 数据科学代理](https://www.snowflake.com/en/news/press-releases/snowflake-intelligence-and-data-science-agent-deliver-the-next-frontier-of-data-agents-for-enterprise-ai-and-ml/)为业务分析师提供了编写自己公式的便捷途径。[Snowflake Cortex AISQL](https://www.snowflake.com/en/blog/ai-sql-query-language/) 可以理解大量非结构化文档，例如音频和图像。[Snowflake Intelligence](https://www.youtube.com/watch?v=va-l7sYp3OA)（现已公测）可以提供一个自然语言接口来检查 Snowflake 数据。

MCP 服务器连接到 [Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst) 和 [Cortex Search](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview)，其他 Cortex 知识扩展可通过 [Snowflake Marketplace](https://www.snowflake.com/en/product/features/marketplace/) 获得。

由于所有数据都位于 Snowflake 内部，因此在整个代理过程中，所有惯常的安全实践都保持不变。

这种设置使得组织能够轻松地通过第三方服务处理和增强其数据：Claude 的推理可以通过 Cortex Analyst 和 Cortex Search 应用于结构化和非结构化文档。

在软件开发中，Snowflake 的 MCP 服务器可以为 Cursor 提供更多上下文数据，帮助组织中的程序员创建更好的代码。同样，FactSet 也可以用于更有效地管理风险。

最初的这套第三方工具专注于金融领域，这是 Snowflake 最受欢迎的市场之一。Gultekin 表示，面向其他垂直行业的工具也将陆续推出。