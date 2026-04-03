<!--
title: OpenClaw vs. Hermes Agent：永不遗忘AI助手的竞速
cover: https://cdn.thenewstack.io/media/2026/04/66127345-getty-images-mhz5eewnoms-unsplash-scaled.jpg
summary: 文章探讨AI编码助手从会话式转向持久化代理的趋势。OpenClaw以广泛生态整合著称但面临安全挑战；Hermes Agent则侧重深度学习和安全架构。核心问题是代理学习到的知识所有权归属，这将在未来深刻影响开发者工具。
-->

文章探讨AI编码助手从会话式转向持久化代理的趋势。OpenClaw以广泛生态整合著称但面临安全挑战；Hermes Agent则侧重深度学习和安全架构。核心问题是代理学习到的知识所有权归属，这将在未来深刻影响开发者工具。

> 译自：[OpenClaw vs. Hermes Agent: The race to build AI assistants that never forget](https://thenewstack.io/persistent-ai-agents-compared/)
> 
> 作者：Janakiram MSV

每个使用过AI编码助手的开发者都经历过同样的挫败感：你花了一个下午的时间教Claude Code或Codex你的代码库的怪癖、命名约定、部署管道以及无人记录的遗留数据库模式。然后你关闭会话。当你打开一个新的会话时，大部分上下文都消失了。

所以，你不得不重新开始。这种上下文丢失和重新解释的循环已成为AI辅助开发中最普遍的痛点之一。现在有两个开源项目正从根本不同的方向解决这个问题。

这里的模式对于任何管理过基础设施的人来说都会感到熟悉。把基于会话的AI工具想象成无状态容器，每次重启都会被清除。它们快速、可一次性使用且无上下文。现在，想想当你添加持久卷、长时间运行的进程以及一个随着时间推移不断改进系统的学习循环时会发生什么。这就是[OpenClaw](https://github.com/openclaw/openclaw)和[Hermes Agent](https://github.com/NousResearch/hermes-agent)所代表的早期转变。它们正在将AI助手从一个会话绑定的工具推向一个持久化的代理运行时。

## 永远在线的代理是一个新的软件类别

我认为AI代理领域正在分裂成两个物种，大多数开发者还没有注意到。一个物种存在于你的终端、你的IDE或你的浏览器标签页中。你打开它，使用它，然后关闭它。像Claude Code、Codex和Cursor这样的工具在一个会话内功能强大，但它们在会话之间携带的上下文有限。解决方法是手动的。你编写CLAUDE.md文件，维护内存目录，并构建精细的基于markdown的“大脑”系统。一位开发者[记录了](https://github.com/anthropics/claude-code/issues/34556)在26天的日常Claude Code使用中进行了59次上下文压缩，之后才从零开始构建了自己的持久化层。

> 像Claude Code、Codex和Cursor这样的工具在一个会话内功能强大，但它们在会话之间携带的上下文有限。

另一个物种则永久存在于你的基础设施上。它在你睡觉时运行。它在你通勤时通过Telegram联系你。它记得上个月学到的东西。它会随着时间变得更好。OpenClaw和Hermes Agent是这第二个物种的两个最突出的例子，它们代表了关于永久代理应该如何运作的非常不同的理念。

尽管如此，这不是一个干净的二分法。会话原生工具已经在增加持久性。Claude Code现在有自动记忆功能，可以将笔记跨会话写入磁盘。Cursor维护工作区级别的上下文。但OpenClaw和Hermes Agent的架构野心超越了附加到基于会话工具的增量内存功能。它们从一开始就被设计为持续运行、随时间学习，并通过消息平台触达用户。

## OpenClaw与生态系统之争

OpenClaw始于2025年末奥地利开发者Peter Steinberger的一个周末项目。最初名为Clawdbot，它成为GitHub上增长最快的开源项目之一，截至2026年4月初已超过345,000颗星。2026年2月，Steinberger[宣布](https://steipete.me/posts/2026/openclaw)他将加入OpenAI，并且OpenClaw将转移到一个独立的基金会。

这种增长并非偶然。OpenClaw解决了一个开发者一直等待解决的问题。它为他们提供了一个自托管的AI代理，可以连接到他们已经使用的消息应用程序。WhatsApp、Telegram、Slack、Discord、Signal以及50多个其他集成。它与每个主要的模型提供商兼容。Anthropic、OpenAI、Google以及通过Ollama的本地模型。该生态系统不断发展，包括[ClawHub](https://clawhub.ai/)，一个拥有数千个社区构建技能的公共技能注册中心，多个托管服务提供商，以及适用于macOS和iOS的配套应用程序。

> OpenClaw解决了一个开发者一直等待解决的问题。

将OpenClaw想象成AI代理的Android。它具有这种比较所暗示的规模、第三方生态系统和碎片化。而且，就像早期的Android一样，其安全状况也很糟糕。

在其爆炸性增长的几周内，一场协调的供应链攻击浮出水面。[Koi Security](https://www.esecurityplanet.com/threats/hundreds-of-malicious-skills-found-in-openclaws-clawhub/)审计了当时ClawHub上的所有2,857个技能，发现了341个恶意条目，其中335个可追溯到一个名为ClawHavoc的单一行动。 [SecurityScorecard](https://conscia.com/blog/the-openclaw-security-crisis/)报告了互联网上数万个公开暴露的OpenClaw实例。CVE-2026-25253（CVSS 8.8）涉及不安全的自动WebSocket连接行为，可能暴露认证令牌，导致多位安全研究人员描述的一键式妥协场景。

[Microsoft](https://www.microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely-identity-isolation-runtime-risk/)建议将运行时视为可能受不可信输入影响，并建议不要在标准个人或企业工作站上运行。 [Cisco](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare)称OpenClaw等个人AI代理为“一场安全噩梦”。

ClawHub市场像早期npm一样运作。发布一个技能只需要一个一周大的GitHub账户。没有自动化静态分析，没有代码审查，没有签名要求。

OpenClaw此后与VirusTotal[合作](https://openclaw.ai/blog/virustotal-partnership)扫描上传的技能，并为运营商添加了安全指南。信任模型正在改进，但仍处于完善阶段。

### 模型无关的灵活性

OpenClaw支持在任何主要的LLM提供商之间切换，无需更改配置。模型无关性是其最强大的功能之一，适用于希望避免供应商锁定或需要根据成本和能力将不同任务路由到不同模型的开发者。

### 跨渠道的持续在线

代理作为后台服务运行，并同时在所有连接的消息平台上保持在线。开发者可以在工作站上开始一项任务，在晚餐时通过Telegram收到完成通知，然后从手机发送后续指令。这种跨渠道的持久性是促使OpenClaw病毒式传播的最主要功能。

> 跨渠道的持久性是促使OpenClaw病毒式传播的最主要功能。

OpenClaw证明了开发者需要超越浏览器标签页的代理。安全事件证明，这些代理的基础设施远未达到生产就绪水平。

## Hermes Agent与研究策略

[Hermes Agent](https://hermes-agent.nousresearch.com/)于2026年2月由Nous Research推出，该实验室是Hermes、Nomos和Psyche模型系列的幕后推手。截至2026年4月初，其GitHub星标约为22,000颗，仅为OpenClaw规模的一小部分。社区技能库较小。品牌知名度较低。Hermes Agent值得关注的不是其目前的规模。而是其底层的架构。

OpenClaw专注于集成的广度，而Hermes Agent则专注于学习的深度。该项目的标语“随你成长的代理”描述了一种围绕闭环学习构建的架构。三个组件使这个循环得以运作。

首先是持久内存。Hermes使用FTS5对存储在SQLite中的所有历史会话进行全文搜索，并结合LLM驱动的摘要功能。代理可以回忆几周前的对话，搜索自己的历史记录，并更深入地了解你是谁以及你如何工作。这不是你自己维护的CLAUDE.md文件。代理会通过定期提示来管理自己的记忆。

其次是自主技能创建。在完成复杂任务后，代理可以编写结构化的技能文档，记录其发现的程序、陷阱和验证步骤。

下一次出现类似任务时，它会加载该技能，而不是从头开始解决问题。技能遵循开放的[agentskills.io](https://agentskills.io)标准，使其可以在兼容平台之间移植。

第三是自训练循环。Hermes与Nous Research的强化学习框架[Atropos](https://github.com/nousresearch/atropos)集成，用于生成批处理轨迹和训练代理行为。

> 开发者可以并行生成数千个工具调用轨迹，导出它们，并用它们来微调更小、更便宜的模型。

这种研究级的设施反映了Nous Research作为模型训练实验室而非产品公司的身份。

### 团队工作流的多实例配置文件

v0.6.0版本（2026年3月30日）引入了配置文件，允许开发者从单个安装运行多个隔离的Hermes实例。每个配置文件都有自己的配置、内存、会话、技能和网关服务。这使得Hermes从“个人助手”走向可重用的代理操作系统。

### 用于IDE集成的MCP服务器模式

Hermes现在可以通过`hermes mcp serve`将其对话和会话暴露给MCP兼容客户端，如v0.6.0发布说明中所述。使用Claude Desktop、Cursor或VS Code的开发者可以通过模型上下文协议（Model Context Protocol）浏览和搜索跨会话内容。这弥合了永远在线的代理与开发者已经使用的IDE原生工具之间的差距。

### 通过架构约束实现安全

Hermes对其技能生态系统采取了更为保守的方法。其文档描述了使用只读根文件系统、删除权限和命名空间隔离的容器强化。文件系统检查点在执行破坏性操作前自动创建快照，并提供回滚命令以恢复状态。

[Tirith](https://hermes-agent.nousresearch.com/docs/user-guide/security/)预执行扫描器在终端命令运行前进行分析。到目前为止，Hermes的生态系统中尚未出现类似知名的公共供应链事件，尽管较小的攻击面和较年轻的生态系统使得直接比较变得困难。一个拥有22,000颗星的项目自然会比一个拥有345,000颗星的项目吸引更少的攻击者。

OpenClaw优化了覆盖范围和生态系统广度，而Hermes则优化了学习深度。它规模较小，更具主见，由一个训练底层模型的团队构建。

## 两种方法之间的选择

OpenClaw和Hermes Agent之间的选择不是功能比较。它映射了一个更深层次的问题：你希望你的代理随着时间演变成什么。

| 要求                   | 推荐选项  | 理由                                       |
| --- | --- | --- |
| 最大消息平台覆盖范围   | OpenClaw  | 50+个集成 vs. Hermes的7个                   |
| 跨会话持久内存         | Hermes Agent | 内置FTS5搜索 + LLM摘要功能                 |
| 大型预构建技能生态系统 | OpenClaw  | 数千个ClawHub技能（需仔细审查）            |
| 随时间自我改进的代理   | Hermes Agent | 具有自主技能创建的闭环学习                 |
| 强化学习训练和轨迹导出 | Hermes Agent | Atropos集成，适用于研究工作流              |
| 经过记录的内置防护措施 | Hermes Agent | 保守架构；实际安全强化成熟度仍在发展中     |
| 社区规模和第三方支持   | OpenClaw  | 34.5万+星，基金会治理，托管服务             |
| 在最小基础设施上运行   | Hermes Agent | 5美元VPS或无服务器，几乎零闲置成本         |

生产系统可能会结合两者的元素。Hermes已经支持从ClawHub安装社区技能，并且存在一个官方迁移工具，供开发者将其配置从OpenClaw迁移到Hermes。Hermes采用的agentskills.io标准旨在使技能在代理平台之间可移植，这表明是趋同而非赢家通吃式的竞争。

## 接下来

OpenClaw和Hermes Agent最好被理解为持久代理基础设施的两个早期且有影响力的原型。一个是生态系统优先。另一个是学习循环优先。两者都不是成品，但它们都指向一个未来，即AI代理作为长期服务运行，而不是会话绑定的助手。

> 随着代理成为长时间运行的进程，积累关于你的代码库、工作流和决策模式的知识，谁拥有这些学到的知识？

对于管理过Kubernetes工作负载的开发者来说，这种发展方向是可识别的。无状态函数让位于有状态服务。短暂容器让位于持久卷。AI领域正在开始类似的转变。

从这一转变中出现的更大问题是，这两个项目都尚未完全回答的问题。随着代理成为长时间运行的进程，积累关于你的代码库、工作流和决策模式的知识，谁拥有这些学到的知识？用户？平台？模型提供商？

OpenClaw向基金会的转移以及Hermes Agent的本地优先架构都指向用户所有权，但这个答案将以远远超出任何单个项目的方式塑造下一代开发者工具。敬请关注。