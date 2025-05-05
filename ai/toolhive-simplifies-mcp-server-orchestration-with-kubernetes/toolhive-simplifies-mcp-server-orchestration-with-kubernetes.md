<!--
title: ToolHive通过Kubernetes简化MCP服务器编排
cover: https://cdn.thenewstack.io/media/2025/04/53bedadb-toolhive.jpg
summary: StackLok开源ToolHive，用Kubernetes简化MCP服务器编排！解决LLM应用访问数据难题。利用K8s的StatefulSets、RBAC和网络策略，安全管理MCP实例，实现隔离。Anthropic力推MCP，集成Jira、Confluence等服务，Agentic AI社区狂喜！
-->

StackLok开源ToolHive，用Kubernetes简化MCP服务器编排！解决LLM应用访问数据难题。利用K8s的StatefulSets、RBAC和网络策略，安全管理MCP实例，实现隔离。Anthropic力推MCP，集成Jira、Confluence等服务，Agentic AI社区狂喜！

> 译自：[ToolHive Simplifies MCP Server Orchestration with Kubernetes](https://thenewstack.io/toolhive-simplifies-mcp-server-orchestration-with-kubernetes/)
> 
> 作者：Joab Jackson

[StackLok](https://stacklok.com/about) 的工作人员开发了一个名为 [ToolHive](https://github.com/StacklokLabs/toolhive) 的命令行实用程序，通过使用 [Kubernetes](https://www.thenewstack.io/Kubernetes) 和 [容器](https://thenewstack.io/introduction-to-containers/)，来[安全地](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/)管理您可能在内部运行的 [多上下文协议 (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) 服务器。

现在，每个人都在[构建 MCP](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/)，这允许基于大型语言模型 (LLM) 的应用程序[从应用程序访问数据和服务](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/)。

然而，设置多个 MCP 服务器可能会导致管理多个软件副本时常遇到的常见问题。

“[设置和维护 MCP 服务器涉及在一个快速变化的领域中导航，该领域具有非常有限的工具、文档和支持，”[Craig McLuckie](https://www.linkedin.com/in/craigmcluckie) 写道，他是 [Kubernetes](https://thenewstack.io/beda-burns-and-mcluckie-the-creators-of-kubernetes-look-back/) 的共同创建者之一，也是 [StackLok](https://stacklok.com/?utm_content=inline+mention) 的首席执行官兼联合创始人，[StackLok](https://thenewstack.io/stacklok-builds-on-sigstore-to-identify-safe-open-source-libraries/) 是一家[以开发者为中心的软件供应链服务提供商](https://thenewstack.io/stacklok-builds-on-sigstore-to-identify-safe-open-source-libraries/)，在一篇[介绍 ToolHive 的博文中](https://www.linkedin.com/pulse/introducing-toolhive-stacklok-labs-project-simplify-craig-mcluckie-zob8c)写道。

ToolHive 是一个开源项目，采用 [Apache 2.0 许可证](https://www.apache.org/licenses/LICENSE-2.0)。

## MCP 部署

“[开发人员在安装和配置这些服务器时可能会遇到复杂性，以及管理更新和确保不同版本之间的兼容性，”McLuckie 继续说道。

每个 MCP 服务器都依赖于外部软件包，例如来自 [Python](https://thenewstack.io/what-is-python/) 或 Node.js 生态系统的软件包，这些软件包必须在推出新的服务器实例时进行维护和存在。

如果您希望用户登录，那么还必须进行密钥管理。对于跨多个服务器的强大隔离来说，这也是一个好的安全想法（如果不是组织强制要求的话）。必须限制用户只能访问他们应该有权访问的服务器。

简而言之，如果 MCP 服务器没有统一部署，那么由此产生的多样性将成为管理的难题。

## 进入 Kubernetes

幸运的是，McLuckie 指出，我们已经拥有一整套用于大规模部署和管理应用程序的工具。Kubernetes 及其[相关的支持技术集合](https://thenewstack.io/cloud-native/)，使其成为管理 [MCP 服务器](https://thenewstack.io/six-reasons-youll-want-to-use-mcp-for-ai-integration/)的自然选择。

[Chris Burns](https://www.linkedin.com/in/chris-j-burns/?originalSubdomain=uk) 是 [Stacklok](https://thenewstack.io/stacklok-donates-minder-security-project-to-openssf/) 的站点可靠性工程师，他在另一篇[介绍 ToolHive 的博文中](https://dev.to/stacklok/toolhive-secure-mcp-in-a-kubernetes-native-world-3o65)写道：“容器化和编排功能为隔离和管理 MCP 实例提供了强大的基础。”

他写道：“Kubernetes 的内置功能，例如基于角色的访问控制 (RBAC)、网络策略和密钥管理，解决了阻止企业的安全问题。”

“此外，Kubernetes 生态系统，包括用于监控、日志记录和自动化部署的工具，为 MCP 服务器提供了一个全面且安全的操作环境。”

ToolHive 可以成为 Kubernetes 和 AI 代理世界之间的连接组织。

ToolHive 用 [Go](https://thenewstack.io/introduction-to-go-programming-language/) 编写，打包为单个二进制文件，可以从命令行运行。从事该项目工作的团队已经在 GitHub 上提交了 26 个版本，该项目已获得 192 颗星。

为了运行 MCP 服务器集合，ToolHive 使用 Kubernetes 的 [StatefulSets](https://thenewstack.io/how-to-better-manage-stateful-applications-in-kubernetes/)，这是一种用于管理有状态应用程序的工作负载 API 对象。应用程序在 [YAML 清单](https://github.com/StacklokLabs/toolhive/tree/main/deploy/k8s)中定义，并为了统一性而保存在 [开放容器计划](https://thenewstack.io/open-container-initiative-launches-container-image-format-spec/)格式的容器中。一旦 StatefulSet 和 pod 启动并运行，它们就可以轻松配置。

## MCP 的受欢迎程度
AI服务提供商Anthropic去年11月[推出了MCP](https://www.anthropic.com/news/model-context-protocol)作为一个开放标准，旨在将[AI助手](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/)连接到外部内容源。

虽然最初的版本旨在与基于LLM的服务[Claude](https://thenewstack.io/making-the-fediverse-more-accessible-with-claude-3-7-sonnet/)对接，但Anthropic标榜MCP是一个开放标准，新兴的Agentic AI社区迅速[接受了这个想法](https://www.google.com/search?q=MCP+site%3Athenewstack.io&rlz=1C1PNKB_enUS1122US1122&oq=MCP+site%3Athenewstack.io&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRiPAtIBCDYzOTdqMGoxqAIAsAIA&)。

本周早些时候，Anthropic演示了MCP如何在更大的环境中使用。该公司为其自身用户推出了一项名为Integration的新功能，该功能使用MCP将[第三方服务融合](https://www.anthropic.com/news/integrations)到其自身的[Claude Desktop](https://claude.ai/download)中。

最初，有10个商业服务被集成到桌面中：[Atlassian的Jira](https://www.atlassian.com/platform/remote-mcp-server)和[Confluence](https://www.atlassian.com/platform/remote-mcp-server)，[Zapier](https://zapier.com/mcp)，[Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare/tree/main)，[Intercom](https://www.intercom.com/blog/introducing-model-context-protocol-fin)，[Asana](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server)，[Square](https://developer.squareup.com/docs/mcp)，[Sentry](https://docs.sentry.io/product/sentry-mcp/)，[PayPal](https://www.paypal.ai/)，[Linear](https://linear.app/changelog/2025-05-01-mcp)和[Plaid](https://api.dashboard.plaid.com/mcp/sse)。