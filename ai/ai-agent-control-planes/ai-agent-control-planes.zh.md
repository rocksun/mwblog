OpenAI 于 7 月 9 日发布了 [ChatGPT Work](https://thenewstack.io/openai-codex-work-atlas/)，并开始向 Pro、Enterprise 和 Edu 用户推出。它运行在新的 GPT-5.6 之上，可以打开用户的本地文件，编辑 Google Workspace 和 Microsoft 365 文档，并将多步骤任务执行至最终交付物。

路透社将其直接与 Anthropic 的 [Claude Cowork](https://thenewstack.io/claude-cowork-cloud-mobile/) 对标，两者的目标受众都是同一个人——那些想要编码代理的强大功能，却不需要使用终端的非编程人员。算上 Anthropic、微软、Perplexity 和亚马逊，目前已有五家领先的实验室发布了此类代理。这批产品表明，最新一代的代理更多是按预期用户而非功能来组织的。

基于目标用户画像，出现了四种原型：知识工作者、自行托管的超级用户、开发者和企业。由于一个人可以同时扮演这三种角色，这些画像往往会重叠。此外，像 [Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/) 这样的产品同时面向独立开发者和平台团队。

因此，请考虑这些按主要购买者分类的部署原型，而不是严格的界限。原型仅代表营销推广的内容。在幕后，每个实验室几乎都一致决定了谁拥有运行时、保留内存、管理凭据以及执行策略。

## 基于用户画像的四种原型

让我们分别分析这四种原型，因为每种原型在用户可获得的控制水平上都有所不同。

第一种原型服务于知识工作者。供应商运营运行时，并将代理作为一种委托手段出售给那些生活在文档而非代码中用户。

ChatGPT Work 是最新的产品，与 Claude Cowork 并列，后者现在在网页和移动端运行云会话，同时在桌面端保持对本地文件的访问；微软的 Copilot Cowork 是一种云托管代理，在 Microsoft 365 信任边界内执行长期任务；[Perplexity Computer](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/)，它可以在本地文件和 Microsoft 应用之间工作；以及 Amazon Quick，它是 Q Business 的继任者，因为该产品已于 7 月底停止接受新客户。用户授予访问权限并监督结果。在大多数情况下，供应商管理运行时和持久状态，Perplexity 的本地选项除外。

第二种原型属于自行托管的超级用户。提供商控制持久代理进程，并选择存储状态和凭据的位置，通常是在 [Mac mini 上，它本身已成为一种个人基础设施](https://thenewstack.io/mac-mini-agent-infrastructure/)。

[OpenClaw](https://thenewstack.io/openclaw-foundation-nonprofit-status/) 和 [Hermes](https://thenewstack.io/persistent-ai-agents-compared/) 是参考示例，它们是开源的，并在操作员自己的机器上运行。由于这两种选择仍然允许访问托管模型和存储外部服务的凭据，因此自行托管涉及的是管理控制平面，而不是完全的本地托管。

**相关阅读：**

“微软已证明它能在科技浪潮的重大变革中生存下来……如今，它面临着核心现金奶牛之一的又一次演变，因为后期独角兽公司和 AI 实验室都在向 Office 领域深入推进。”

[→ *在 Cautious Optimism 中阅读更多内容*](https://www.cautiousoptimism.news/the-ai-agents-are-coming-for-microsoft-office/?utm_source=The+New+Stack&utm_medium=referral&utm_campaign=Article+Quote+Box)

开发者属于第三种原型，其运行时跨越了 IDE、终端、存储库和云沙箱。Claude Code、[OpenAI Codex](https://openai.com/codex/)、处于代理模式的 [GitHub Copilot](https://github.com/features/copilot) 以及开源的 [OpenCode](https://opencode.ai/) 都属于此类，而亚马逊的开发者代理正在并入其 Kiro 工具中。编码代理的执行正从本地 IDE 扩展到供应商管理的沙箱和异步云工作者，这使其成为最难明确分类的原型。

第四种原型专为企业工作流和业务流程集成而构建。它们在托管、受管的运行时上运行开放代理框架，如 LangGraph 或 CrewAI。Gemini Enterprise Agent Platform 上的 ADK、[Bedrock AgentCore](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) 上的 Strands、Foundry Agent Service 上的 Microsoft Agent Framework 以及 Claude Managed Agents 都属于这一类别。[OpenAI 的 Agents SDK](https://thenewstack.io/openai-agents-sdk-sandboxes/) 可以托管在其中一些运行时上，包括 AgentCore，AWS 将其列为支持的框架之一。供应商运营基础设施，客户在此基础上配置身份、策略和保留规则。

| 用户画像 | 代表产品 | 运行时所有权 | 状态和凭据 | 平台类型 |
| --- | --- | --- | --- | --- |
| 知识工作者 | [ChatGPT Work](https://chatgpt.com//), [Claude Cowork](https://www.anthropic.com/product/claude-cowork), [Copilot Cowork](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/), [Perplexity Computer](https://www.perplexity.ai/hub/blog/everything-is-computer), [Amazon Quick](https://aws.amazon.com/quick/) | 大多数为供应商云，部分支持按文件夹进行本地访问 | 供应商保留会话状态，用户授予作用域凭据 | 封装体验 |
| 超级用户，自行托管 | [OpenClaw](https://github.com/openclaw/openclaw), [Hermes](https://github.com/NousResearch/hermes-agent) | 操作员自己的机器 | 操作员选择状态和令牌的存储位置，尽管推理通常是外部的 | 封装体验，自行操作 |
| 开发者 | [Claude Code](https://www.anthropic.com/claude-code), [OpenAI Codex](https://github.com/openai/codex), [GitHub Copilot](https://github.com/features/copilot), [OpenCode](https://opencode.ai/) | 跨越 IDE、笔记本电脑和云沙箱 | 目前主要在存储库和本地，正在向托管沙箱转移 | 摇摆，向平台发展 |
| 企业，工作流驱动 | [ADK](https://adk.dev/) on [Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform), [Strands](https://strandsagents.com/) on [AgentCore](https://aws.amazon.com/bedrock/agentcore/), [MAF](https://learn.microsoft.com/en-us/agent-framework/) on [Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/overview), [Claude Managed Agents](https://www.anthropic.com/engineering/managed-agents) | 托管供应商运行时，客户可配置 | 客户定义身份、策略和保留规则；平台进行代理 | 可编程平台 |

## 用户画像之下的底线

基于用户画像的方法抽象了四件事：执行在哪里运行，状态在哪里持久化，权威如何委托，以及策略在哪里执行。

Anthropic 将其设计描述为将大脑与双手解耦。调用 Claude 的工具与执行代码的沙箱分开运行，而会话（每次模型调用、工具调用和结果的仅追加日志）连接了两者。由于沙箱与大脑保持分离，代理可以在任何容器存在之前就开始推理，并且它运行的代码与开发者的凭据保持距离。

同样的四个平面出现在其他供应商那里。AgentCore Runtime 为每个会话提供了一个专用的微型虚拟机，具有隔离的 CPU、内存和文件系统，并计量计算使用情况。[谷歌可以通过其 Agent Gateway 路由受管流量](https://thenewstack.io/google-debuts-gke-agent-sandbox-inference-gateway-at-kubecon/)，模型防护策略检查配置的入站和出站流量，而 Agent Identity 和 Agent Registry 则跟踪机队。微软为每个托管代理分配一个专用的 Entra Agent ID，并在一个文件系统在空闲期间仍然存在的每会话沙箱中运行它。

> 在受管运行时上部署代理更像是租赁工作室，而不是购买工具……长期租户安装自己的锁，维护自己的记录，并在租约结束时带走自己的工具。

在受管运行时上部署代理更像是租赁工作室，而不是购买工具。房东管理建筑物并提供电力，但长期租户安装自己的锁，维护自己的记录，并在租约结束时带走自己的工具。用户画像往往掩盖了这种差异。目前，供应商通常运营运行时，因此关键问题是客户在四个平面上还能行使多少控制权，以及他们能带走什么。

## 界限在哪里

区分每种产品供给的不是计算操作员，因为供应商处理了几乎所有这些。而是产品留给客户配置和导出的四个平面有多少。封装体验将这四个平面几乎全部交给供应商，并返回监督和一个最终结果。可编程平台运营基础设施，但让客户定义身份、策略和保留规则，并将代码移动到其他地方。

Copilot Cowork 表明这两个轴是独立的。它是一种封装的知识工作者体验，但它运行在一个受管的企业平台上，并继承了微软的身份、合规性和审计控制。

> 用户画像销售产品，但四个平面决定了锁定。

产品表面上可以是封装的，底层可以是可编程的，这就是为什么必须将用户画像和控制平面作为不同的问题来阅读。ChatGPT Work 从开发者端指出了同样的点，因为 [OpenAI 的新桌面应用](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/) 将 Chat、Work 和 Codex 折叠成一个单一的界面，尽管 OpenAI 尚未详细说明其底层共享运行时或凭据存储的程度。用户画像销售产品，但四个平面决定了锁定。

| 用例 | 代理类型 | 权衡 |
| --- | --- | --- |
| 将知识任务委托给您监督的代理 | 知识工作者代理，如 ChatGPT Work、Copilot Cowork 或 Amazon Quick | 供应商通常运营运行时并保留状态，您在表面之下几乎无法配置除访问和批准之外的内容 |
| 将状态和凭据保留在您控制的硬件上 | 自托管代理，如 OpenClaw 或 Hermes，采用本地配置 | 您控制持久进程，尽管模型推理和某些工具可能仍然是远程的 |
| 在 IDE、存储库和 CI 中发布代码更改 | 开发人员编码代理，如 Claude Code、Codex 或 Copilot | 执行跨越您的工具和云沙箱，因此所有权是分散的，在提交之前值得映射 |
| 运行许多带有审计和身份的受管代理 | 企业运行时平台，如 AgentCore、Agent Platform、Foundry 或 Managed Agents | 供应商运营基础设施，同时您定义身份、策略和保留规则，以换取将工作流逻辑耦合到一个云 |

实际部署结合了这些行，而不是选择其中一行。Foundry Agent Service 上的团队通常运行开源编排（如 LangGraph）来实现代理逻辑，同时依赖平台进行受管执行，而微软自己的托管运行时现在支持像 OpenClaw 和 Hermes 这样具有持久状态的长期运行个人代理。体验与平台之间的边界不是一条清晰界定的厚界线，而是一条单一系统可以跨越的细线，连接着相互竞争的阵营。

> 代理市场不是由开放与封闭决定的。像 Strands、ADK 和 [Microsoft Agent Framework 这样的开放框架恰恰是受管运行时](https://thenewstack.io/microsoft-scout-openclaw-runtime/) 所构建的目的地。

代理市场不是由开放与封闭决定的。像 Strands、ADK 和 Microsoft Agent Framework 这样的开放框架恰恰是受管运行时所构建的目的地。供应商现在管理着几乎所有原型的运行时，将竞争转移到谁能最有效地配置和导出状态、身份和基础策略。

如果编码代理与知识工作者代理一起进入受管沙箱，开发者原型将在平台侧建立。地图随后将转化为供应商已经勾勒出的内容。当企业团队评估代理时，他们最重要的问题应该是他们能从产品中配置和提取多少执行、状态、身份和策略。他们不应该关注它呈现出什么画像或者其框架是否开放，因为框架不再决定产品的价值或锁定能力。