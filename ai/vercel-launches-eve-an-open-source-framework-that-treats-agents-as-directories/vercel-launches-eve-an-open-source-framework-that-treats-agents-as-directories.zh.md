Vercel 于周三发布了 [eve](https://vercel.com/eve)，这是一个用于构建 AI 智能体的全新开源框架。它将每个智能体视为一个文件目录，并集成了在生产环境中运行该智能体所需的基础设施。

Vercel 将 eve 描述为“智能体领域的 Next.js”，意指该公司创建并维护的流行 [web 框架](https://nextjs.org/)。

Eve 在 Vercel 于伦敦举行的 Ship 大会上发布，同时发布的一系列相关产品被统称为 [Agent Stack](https://vercel.com/blog/agent-stack)。

![](https://cdn.thenewstack.io/media/2026/06/330044ef-hello-eve-more-padding.gif)

图片来源：Vercel。

## 智能体就是一个目录

Vercel 强调的 eve 与 Next.js 的相似之处在于：eve 定义智能体的方式与 Next.js 定义 Web 应用的方式类似。

一个单一的目录包含了定义智能体行为的所有独立文件。其中一个文件用于设置智能体运行的模型，并由 Vercel 的 [AI Gateway](https://vercel.com/ai-gateway) 处理提供商回退。另一个文件包含以 Markdown 编写的系统提示词。与此同时，智能体的工具是独立的 TypeScript 文件，文件名即为工具名称，无需单独注册。与其他智能体框架一样，eve 使用 skill.md 文件以及 [MCP 服务器](https://modelcontextprotocol.io/) 来连接其他工具。

![](https://cdn.thenewstack.io/media/2026/06/64b07ddc-screenshot-2026-06-17-at-09.42.32-1024x484.png)

图片来源：Vercel。

随后，Eve 会将此目录编译为一个运行中的智能体。

每一次对话都作为一种持久化工作流运行，该工作流构建于 Vercel 的开源 [Workflow SDK](https://workflow-sdk.dev/) 之上，并对每一步进行检查点记录，以便会话可以暂停、在崩溃后存续并在中断处恢复。

在安全性方面，每个智能体都有自己的沙箱来运行其编写的代码，以确保与应用程序保持隔离。值得注意的是，每个工具都可以被设置为在运行前需要人工审批。

在适当的情况下，智能体可以将工作移交给子智能体，通过 MCP 服务器或 [OpenAPI](https://www.openapis.org/) 文档连接外部服务，并通过内置的 Slack、Discord、Microsoft Teams、Telegram、Twilio、GitHub 和 Linear 渠道触达用户。

为了让开发者和 IT 团队能够监控运行状况，每次运行都会产生一个 [OpenTelemetry](https://opentelemetry.io/) 追踪数据，显示在 Vercel [可观测性仪表盘](https://vercel.com/products/observability) 的新“智能体运行”视图中，并支持将数据导出到 [Datadog](https://www.datadoghq.com/) 和 [Honeycomb](https://www.honeycomb.io/) 等专业服务中。

## 运行与部署智能体

开发者只需一个命令即可在本地启动智能体，并通过终端界面与之交互。部署过程与任何其他项目一样，使用 `vercel deploy` 命令。当新版本发布时，正在执行任务的会话会在其启动时的版本上完成任务。

Eve 目前处于 [公开预览](https://vercel.com/eve) 阶段，并在 [GitHub](https://github.com/vercel/eve) 上以 Apache 2.0 许可证开源。

![](https://cdn.thenewstack.io/media/2026/06/ef2cebba-screenshot-2026-06-17-at-09.42.44-1024x484.png)

图片来源：Vercel。

## Vercel 如何使用它

Vercel 表示，其内部在 eve 上运行了超过 100 个智能体，包括员工每月在 Slack 中查询数万次的数据分析智能体，以及将问题导向能够解答的智能体的路由智能体。

智能体已经成为 Vercel 自身流量的主要来源。该公司称，目前其平台上约 [29% 的部署](https://vercel.com/blog/introducing-eve) 是由智能体触发的，高于一年前的不到 3%，并预计这一比例将达到一半。

## 竞争格局

Eve 进入了一个在过去一年中迅速饱和的市场。它最接近的 TypeScript 原生竞争对手是 [Mastra](https://mastra.ai/)，这是一个获得 Y Combinator 支持的框架，于 1 月份达到 1.0 版本，旨在支持在任何平台上运行，这与 eve 默认绑定 Vercel 的特性形成对比。LangChain 的 [LangGraph](https://github.com/langchain-ai/langgraph) 是目前最成熟的智能体框架，它以 Python 为先，并同样专注于 eve 所提供的持久化执行能力。Inngest 的 [AgentKit](https://agentkit.inngest.com/) 是另一个内置持久化功能的 TypeScript 选择。

大型云服务提供商正从基础设施端应对相同的工作负载。Cloudflare 在其 [Workers 平台](https://workers.cloudflare.com/product/agents) 和 [Durable Objects](https://developers.cloudflare.com/durable-objects/) 上构建智能体，而亚马逊的 [Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)、谷歌的 [Vertex AI Agent Engine](https://cloud.google.com/products/agent-builder) 以及微软的 [Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/) 则提供可以运行来自任何框架的智能体的托管运行时。OpenAI 于去年发布的 [AgentKit](https://openai.com/index/introducing-agentkit/) 则将其工具与 OpenAI 自身的模型绑定。

Vercel 表示，对其他平台的支持即将到来。不过目前，eve 仅能在 Vercel 上运行。