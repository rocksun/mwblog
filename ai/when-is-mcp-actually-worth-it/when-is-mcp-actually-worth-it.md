
<!--
title: MCP认证：何时才是最佳投资？
cover: https://cdn.thenewstack.io/media/2025/09/97717475-mcp-logo-2.png
summary: MCP 是连接 AI 代理与外部数据和服务的开放标准，适用于增强代理工作流程、提供工程上下文和公开系统。但它不适用于确定性自动化、静态上下文、绕过 CLI 和安全风险高的场景。
-->

MCP 是连接 AI 代理与外部数据和服务的开放标准，适用于增强代理工作流程、提供工程上下文和公开系统。但它不适用于确定性自动化、静态上下文、绕过 CLI 和安全风险高的场景。

> 译自：[When Is MCP Actually Worth It?](https://thenewstack.io/when-is-mcp-actually-worth-it/)
> 
> 作者：Bill Doerrfeld

[模型上下文协议 (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) 已经成为连接 AI 代理与外部数据和服务的开放标准。自从 Anthropic 在 11 月份推出以来，它已经迅速发展：一个目录列出了超过 16,000 个 MCP 服务器。

“[红帽](https://www.openshift.com/try?utm_content=inline+mention) 的 AI 产品经理 Adel Zaalouk 表示：“MCP 是一个强大的标准，但其价值在复杂、高风险的环境中最为明显。MCP 的一个关键优势是它能够支持可扩展的多租户平台。”

虽然 [MCP 在许多情况下增强了代理的能力](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)，但它并不是每个任务的最佳工具。一种新兴的共识是，MCP 不是确定性或一次性集成的最佳工具。当上下文是静态的或安全性要求严格时，[简单的 API 调用通常更胜一筹](https://thenewstack.io/why-apis-are-essential-and-mcp-is-optional-for-now/)。

[Arcee.ai](http://arcee.ai) 的首席布道师 Julien Simon 在 [Medium](https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b) 上的博文中警告说，MCP 对几十年来的远程过程调用 (RPC) 系统最佳实践的漠视可能会导致“痛苦的生产故障”，因为企业会在碎片化的第三方库群上构建。Arcee.ai 专注于小型语言模型。

那么，什么时候 MCP 才是值得的呢？下面，我们将深入探讨 MCP 表现出色的场景，以及它不是理想解决方案的场景。我们还将探讨一些新兴的案例研究和最佳实践，以便在生产中充分利用它。

## 何时 MCP 有意义

在少数情况下，MCP 服务器会表现出色，使其非常值得采用。

### 增强代理工作流程

MCP 允许自主代理发现和调用工具，而无需进行刚性集成，使其成为开发团队使用 AI 代理与外部数据、工具或其他代理交互的强大助手。

云计算基础设施公司 [Vultr](https://www.vultr.com/) 的首席营销官 Kevin Cochrane 告诉 The New Stack：“MCP 服务器非常适合复杂的代理 AI 应用，例如基础设施自动化、多代理协调以及任何需要在严格的运营治理下快速、安全地访问异构企业资源的场景。”

[Atlassian](https://www.atlassian.com/) 的首席工程师 Kun Chen 表示，对于已经使用多个编码代理的团队来说，MCP 是一个自然的选择。

Kun Chen 告诉 The New Stack：“对于已经使用代理产品的团队（如 Cursor 或 Rovo Dev）来说，MCP 特别值得采用，他们希望将更多的机械性或重复性工作委派给 AI 代理。”他补充说，这可能包括创建待办事项、生成发布说明或更新文档。

对于个人贡献者来说，使用 MCP 可以增强工作流程并提高生产力。[GitHub](https://github.com/) 的首席产品经理 Toby Padilla 告诉 The New Stack：“MCP 是一种强大的力量倍增器。它可以帮助个人扩展规模，因为它允许代理驱动通常为人类构建的现有平台。”

例如，Padilla 说，[GitHub 的官方 MCP 服务器](https://github.com/github/github-mcp-server) 可以让代理在几分钟内审查数百个问题和拉取请求。MCP 服务器还可以连接云服务，例如直接从 Slack 聊天中创建一个 GitHub 问题。

### 提供工程上下文

[WireMock](https://www.wiremock.io/) 的 CTO 兼联合创始人 Tom Akehurst 告诉 The New Stack：“使用 MCP 是一种将上下文引入代理工作流程的好方法，而无需修改代理本身。”WireMock 是一种 API 模拟工具。

例如，[Context7 MCP 服务器](https://github.com/upstash/context7) 可以为 AI 编辑器提取当前的文档或代码库，帮助代理提供更准确的代码建议。一个相关的项目 [git-mcp](https://gitmcp.io/) 公开了公共 GitHub 存储库，以便代理可以按上下文访问最新的文档和代码。

除了文档之外，MCP 还擅长将私人数据与 [大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms/) 同步，从而提供工程上下文。

向量数据库 [Qdrant](https://qdrant.tech/) 的高级开发者倡导者 Kacper Lukawski 告诉 The New Stack：“AI 辅助编码是我们看到大量采用的用例之一，并且通过 MCP 服务器进行检索是有意义的。”他补充说，这有助于参考特定的库版本、编码约定或相关示例。

### 当不存在其他标准接口时

并非所有平台或工作流程都具有命令行界面 (CLI)、API 或流行的集成。这是 MCP 可以提供帮助的一个重要领域。

[Upbound](https://www.upbound.io/) 的开发者倡导者兼 [DevOps Toolkit](https://www.youtube.com/@DevOpsToolkit) YouTube 系列的主持人 Viktor Farcic 告诉 The New Stack：“当 MCP 提供对代理无法访问的工具和服务的访问权限，或者当它反映用户意图而不是镜像现有 CLI 时，MCP 值得采用。”

他分享了一些适用此情况的优秀用例：

*   桥接到 Slack、[Google](https://cloud.google.com/?utm_content=inline+mention) Drive 或电子邮件等服务，这些服务不存在 CLI。
*   创建以意图为中心的工具，例如 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) EKS MCP，将多个 API 组合成有意义的操作。
*   构建混合系统，将确定性代码与代理决策相结合，以用于复杂的工作流程，例如日志分析或 Kubernetes 部署建议。

### 向代理公开系统

平台和软件即服务 (SaaS) 提供商也可以通过创建 MCP 服务器作为外部 AI 的桥梁而受益。Atlassian 的 Chen 说：“从提供商的角度来看，值得考虑将 MCP 作为向其他 AI 代理公开服务的开放标准。”

统一 API 聚合器 [Merge](https://www.merge.dev/) 的 CTO Gil Feig 表示，MCP 可用于支持“动态、实时的工作流程”。“它也非常擅长将数据发布到第三方系统中。”

这可能意味着创建或更新支持单、记录客户关系管理系统交互、在企业资源规划 (ERP) 系统中触发发票或将更新推送到项目管理工具中。

Feig 补充说，MCP 连接对于触发 API 以进行新的查找或将新数据写回源系统特别有用。对于旧数据的查询，他建议维护一个同步副本作为企业搜索的索引，这可以避免昂贵的 [语义搜索](https://thenewstack.io/what-is-semantic-caching/)。

通过使用 MCP，多租户平台可以避免为每个客户端构建自定义集成。Red Hat 的 Zaalouk 说：“该平台可以简单地连接到客户托管的 MCP 服务器，该服务器公开其特定的工具。对于为众多客户提供服务的提供商，每个客户都有独特的工具和数据，MCP 提供了一个可扩展的解决方案。”

## 何时 MCP 不值得

另一方面，在某些情况下，更简单的解决方案使 MCP 变得不必要，甚至过于复杂。

### 替换确定性自动化

当工作流程每次都预期相同的结果时，MCP 就显得过犹不及了。Chen 说：“MCP 并非旨在用于不涉及 AI 代理的确定性工作流程。如果您的用例只是为了提供对服务的编程访问，那么传统的 API 更适合。”

GitHub 的 Padilla 认为，其他人也同意 API 更适合日常自动化。“LLM 和 MCP 非常适合处理‘模糊’请求或自然语言，”他说。“如果您需要重复完成相同的任务，那么传统的编程和 API 调用是更好的选择。”

Feig 指出，在这些情况下，传统的集成通常会胜出：“对于需要下载内容和处理复杂的访问控制列表的企业搜索，MCP 的性能不如同步数据。他补充说，API 通常最适合静态工作流程。

### 当上下文保持静态时

如果您的工程指令（如规则或偏好）保持相对不变，则使用 MCP 可能过犹不及。Qdrant 的 Lukawski 说：“只有当我们有足够频繁变化的知识，并且足够大以至于我们不想将其传递给每个 LLM 调用时，引入 MCP 服务器进行上下文工程才有意义。”

Cochrane 补充说，当需求偏向静态、紧密耦合的集成时，使用 MCP 可能是过度设计的迹象：“在这些设置中，系统通常在高度受控的环境中运行，具有固定的功能、有限的连接，并且不需要动态发现、多代理协调或运行时可组合性。”

### 绕过已建立的 CLI

当代理已经可以直接执行 CLI 工具时，MCP 的相关性较低。Upbound 的 Farcic 说：“95% 的 MCP 都属于这一类——它们是已经可以完美运行的工具的更慢、更复杂的版本，”他指的是镜像 git 命令的 MCP 或复制 kubectl 的 Kubernetes MCP。

Akehurst 也认为 MCP 可能会过度设计基础设施即服务 (IaaS)，在这种情况下，AI 编码代理可以直接生成 Terraform 代码来自动化 CI/CD。

### 当安全不可谈判时

除非 MCP 带来明显的生产力提升，否则将其引入企业工具链可能不值得 [承担风险](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/)。

Akehurst 说：“在企业中，[MCP 存在重大的安全和合规性挑战](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/)。”虽然 MCP 安全架构的工作正在进行中，但其漏洞和缺乏默认控制对于公司治理来说可能太多了。

Feig 说：“许多 MCP 服务器构建和维护得很差。”薄弱的描述或不完整的实现可能会导致糟糕的工具选择。他补充说：“如果您正在处理敏感数据和业务关键型工作流程，您可能需要谨慎行事。”

## MCP 可以提供真正的价值

尽管 MCP 是一种新技术，但一些早期的案例研究表明了切实的商业价值。

在 GitHub，MCP 服务器有助于自动化开源管理职责。在一个元步骤中，GitHub 使用其 GitHub MCP 服务器来管理提交给开源 [GitHub MCP 服务器](https://github.com/github/github-mcp-server) 项目的许多贡献和问题。

Padilla 说：“在内部，我们使用 GitHub MCP 服务器来帮助对这些社区贡献进行分类和分组。它使我们的小团队能够以 MCP 之前不可能的方式进行扩展。”

Atlassian 和 WireMock 也看到了类似的势头。Atlassian 正在试验将代理产品连接到其远程 MCP 服务器，以简化诸如 Jira 自动化之类的任务，而 WireMock 已经通过一个 MCP 服务器吸引了潜在客户，该服务器扩展了 API 模拟以用于编码代理。

Red Hat 的 Zaalouk 说，Red Hat 的客户也在采用 MCP 来扩展安全数据访问。一家欧洲云提供商使用它来让非技术用户通过构建在 OpenShift AI 上的自助式 AI 平台连接私有数据源。

他补充说，Red Hat 的一家大客户，一家大型 IT 公司，将 MCP 应用于一个多代理承保系统，允许专业代理访问不同的数据源，而无需硬编码集成。“这简化了一个传统上复杂且需要大量人工干预的业务流程，从而提高了效率，缩短了承保时间，并使决策更加一致，”他说。

一些项目也在探索使用 MCP 进行基础设施管理。例如，Farcic 说，[dot-ai MCP 服务器](https://github.com/vfarcic/dot-ai) 可以将诸如“我想要一个带有监控的 EKS 集群”之类的简单英语请求转换为正确的 Kubernetes 资源，从而减少 DevOps 的辛劳。

## 运营 MCP 的策略

尽管使用 MCP 取得了积极的成果，但一些模式和最佳实践正在出现，以帮助在生产中充分利用它——对于服务器提供商和消费者而言。

### MCP 服务器创建者的技巧

对于服务器设计者来说，MCP 工具需要周全的规划，而不仅仅是对现有接口进行建模。Chen 说：“仅仅将现有的 REST API 包装到 MCP 工具中通常会导致 AI 代理难以有效地使用它们。”他补充说，更直观的代理界面可以优化令牌使用并提供更好的结果。

其他人也同意：可用的 MCP 工具需要做的不仅仅是包装 API。Farcic 说：“围绕用户意图而不是 API 反射来设计 MCP。”

Akehurst 警告说：“有时您需要减少通过 MCP 提供的能力范围，以提高 AI 正确运行的几率。策划一组稀疏的、非重叠的工具，而不是仅仅为每个可用的 API 调用生成一个一对一的工具。”

清晰的指导有助于代理知道何时调用工具。Padilla 建议，一种解决方案是以自然语言为中心进行设计。“尽可能使您的工具名称和描述与人们说话的方式相匹配。”

即使是简单的命名约定也可以提供帮助。例如，GitHub 的 `get_me` 工具返回经过身份验证的用户的个人信息。Padilla 说：“当他们说诸如‘向我显示我的未解决问题’之类的话时，我们可以获得正确的用户个人信息。如果没有这一点，LLM 会对‘我’、‘我的’和‘我’是谁感到困惑。”

Cochrane 说，清晰的命名和逻辑组织应该有益于代理与 MCP 的交互：“逻辑分组提高了推理性能，减少了误用，并支持大规模的多代理协调。”

### MCP 服务器用户的技巧

对于消费者来说，让人们参与其中非常重要。Chen 说：“应谨慎采用，让人们参与其中以确保安全性和可靠性。”

其中一些指导可以进行编程。例如，GitHub 发现，在系统提示中嵌入自定义指令可以帮助 LLM 调用预期的工具，Padilla 说。他说，这可能是一种提示，例如“对于 GitHub 操作，请使用可供您使用的 GitHub 工具。”

除了平衡人工监督与自主决策之外，可见性也很重要。Lukawski 说，MCP 服务器应部署为共享服务，而不是在本地运行，以便所有团队成员都可以远程访问它们。这简化了维护和监督。

但是，这种共享需要谨慎，需要策略执行、输入验证、访问控制和日志记录，Cochrane 说。实际上，这意味着像对待 API 一样小心地对待 MCP。

Cochrane 还建议在私有的、隔离的云原生环境中部署 MCP 服务器，并使用专用网络连接内部工具。“首先从小处着手，用 [FastMCP](https://gofastmcp.com/getting-started/welcome) 包装现有的 BASH、Python 或 Go 脚本，以将它们作为运行时工具公开，而无需打开公共端点或重写遗留代码。”

## 了解何时使用它

与许多技术趋势一样，归根结底是了解何时（以及如何）使用 MCP。

我们已经看到了一些强大的案例出现，可以提高软件开发的生产力，尤其是在新颖情况下进行不确定的推理，这些情况侧重于意图（而不是包装功能齐全的 API）并使 AI 编码代理能够即时获得更多上下文。

但是，对于预测标准化结果的编程自动化，MCP 可能会导致不必要的混乱并引入安全风险。要实现投资回报，还需要指导，无论是作为 MCP 服务器的创建者还是消费者。

总而言之，这些策略正变得越来越重要，因为许多人将 MCP 视为代理 AI 架构未来的核心。

Vultr 的 Cochrane 说：“MCP 对于代理 AI 来说就像 HTTP 对于网络一样，能够实现自主代理与实时企业系统之间的实时交互。除非开发人员正在开发小众服务，否则他们不能忽视 MCP。”