<!--
title: OpenClaw 与 Hermes：对代理定义达成共识，但控制权归属各执一词
cover: https://cdn.thenewstack.io/media/2026/06/9228c0d6-logan-voss-v0sixwyivly-unsplash-scaled.jpg
summary: 本文探讨了 AI 代理架构的两大主流项目 OpenClaw 与 Hermes。OpenClaw 以网关连接为核心，侧重广泛的渠道覆盖与平台集成；Hermes 则以持久化记忆为核心，侧重自主学习与深度上下文。两者代表了 AI 代理在运行、治理与可观测性层面的不同发展路径。
-->

本文探讨了 AI 代理架构的两大主流项目 OpenClaw 与 Hermes。OpenClaw 以网关连接为核心，侧重广泛的渠道覆盖与平台集成；Hermes 则以持久化记忆为核心，侧重自主学习与深度上下文。两者代表了 AI 代理在运行、治理与可观测性层面的不同发展路径。

> 译自：[OpenClaw and Hermes agree on what an agent is. They disagree on what controls it.](https://thenewstack.io/openclaw-hermes-agent-harness/)
> 
> 作者：Janakiram MSV

在微软本月的 Build 大会上，CEO Satya Nadella 描述了一个平台层面的转型：从操作系统和应用程序转向无需用户打开的代理型 AI。随后，他展示了实现这一转变的层级：[OpenClaw](https://github.com/openclaw/openclaw)，这是一个几个月前发布的开源工具链及独立项目，能够直接在微软新执行容器内的 Windows 上原生运行。在此基础上构建的是 [Scout，微软的常驻企业级代理](https://thenewstack.io/microsoft-scout-openclaw-runtime/)。一个诞生仅一年的工具链，如今已成为受监管的基础设施。

Nvidia 在 3 月的 [GTC 大会](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/)上更为直白地表达了这一观点，Jensen Huang 将 OpenClaw 称为“个人 AI 的操作系统”。这个类比很贴切：工具链之于语言模型，就像操作系统之于处理器。模型可以独立回答问题，而工具链使模型能够持续运行、记住所学内容，并调用工具进行操作。

今年，两个开源项目从不同的起点构建了这一层级。**OpenClaw** 围绕网关构建，这是将代理连接到人们已有使用习惯的渠道的部分。Nous Research 推出的 **Hermes Agent** 则围绕记忆构建，这是让代理学习开发者工作方式并不断进步的部分。两者之间的竞争在于控制层，而非各自调用的模型。

## 用通俗语言解释代理工具链

本质上，代理工具链（Agent Harness）是一种软件，它能将模型转变为能够自主运行的系统。它汇集了运行时（在任务间维持代理存活）、网关（负责消息的出入）以及跨会话持久化的记忆。在此之上，还有代理调用以采取行动的工具、代理运行的身份标识、可扩展的技能，以及决定其可以触及什么、必须记录什么的策略和可观测性控制。像 [Claude Code](https://docs.claude.com/en/en/docs/claude-code) 或 [Codex](https://openai.com/index/introducing-codex/) 这样的代码辅助工具仅涵盖了这其中的一部分。它们在交互式会话中运行，一旦会话结束就会丢失大部分工作上下文。而工具链则保留了运行时、记忆和治理机制，以便代理可以无人值守地运行。

> 工具链保留了运行时、记忆和治理机制，以便代理可以无人值守地运行。

Nous Research 和 OpenClaw 在这种解剖结构上达成了共识。但它们在将哪一部分视为主要控制点上存在分歧。OpenClaw 从网关开始，因此一个代理可以在 WhatsApp、Discord、Slack 等渠道上从一个中心位置进行回复。Hermes 从记忆开始，因此一个代理可以在数周内携带开发者的上下文并不断改进自身的技能。

## OpenClaw 的网关优先设计

OpenClaw 最初是 Peter Steinberger 的一个独立开源项目，他因早年在 PDF 工具方面的工作而闻名。他在 2025 年底发布了早期版本，并两次更名，最终在 1 月确定为 OpenClaw。它是为广泛性而构建的，中心是一个连接代理到数十个消息渠道的中央网关。[ClawHub](https://github.com/openclaw/clawhub) 是其公共技能市场，包含数千个社区贡献的技能，扩展了代理的能力。开源动力非常强劲，到 6 月下旬，该仓库在 GitHub 上的星标数接近 380,000，尽管星标衡量的是知名度而非生产使用。

更重要的发展是网关的采用者。Steinberger 于 2 月[加入](https://techcrunch.com/2026/03/16/nvidias-version-of-openclaw-could-solve-its-biggest-problem-security/) OpenAI，项目转交给一个独立的基金会，OpenAI 成为赞助商而非所有者。

在 3 月的 GTC 上，[Nvidia 将 OpenClaw 包装在 NemoClaw 中](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/)，这是一个 OpenShell 运行时，可以对每个代理进行沙箱隔离，并在代理触及范围之外强制执行策略。

在 6 月的 Build 大会上，微软使 OpenClaw 成为 Windows 执行容器的原生组件，并发布了 Scout，这是一个基于 OpenClaw 网关的代理，具有自己的 Entra 身份标识，并与 Teams、Outlook 和 SharePoint 进行了连接。在每种情况下，平台供应商都保留了 OpenClaw 的广泛性，并增加了原始项目所缺乏的治理和身份验证能力。

> 安全团队现在可以限制代理读取哪些文件夹以及哪些文件夹保持隐藏，而不是授予早期 OpenClaw 部署中那种高风险的广泛访问权限。

对于企业而言，这改变了计算方式。安全团队现在可以限制代理读取哪些文件夹以及哪些文件夹保持隐藏，而不是授予早期 OpenClaw 部署中那种高风险的广泛访问权限。平台团队可以提供一个单一的、受监管的代理，员工可以使用他们现有的工具进行访问。广泛性为 OpenClaw 带来了分发能力，而平台供应商提供了这种分发进入生产环境所需的控制手段。

## Hermes 的记忆优先设计

[Hermes Agent](https://github.com/nousresearch/hermes-agent) 采取了另一条路径。Nous Research 是 Hermes、Nomos 和 Psyche 模型家族背后的实验室，于 2 月 25 日在 MIT 许可下发布了该项目。它使用 Python 编写，旨在团队拥有的基础设施上持续运行：VPS、家庭服务器或笔记本电脑。

Hermes 的核心能力是跨会话的持久化记忆。它保持分层记忆，在处理艰巨任务后发展出新技能，并在使用过程中不断完善这些技能。它还会构建为其工作的开发者档案，因此每个会话开始时都比上一个会话拥有更多的上下文。这些技能遵循 [agentskills.io](https://agentskills.io) 标准，使其能够在不同代理间移植，而不是被锁定在一个代理上。

这种深度转化为可量化的使用量。到 5 月中旬，Hermes 在 GitHub 上的星标数超过 100,000，到月底达到约 160,000。5 月 10 日，它在 OpenRouter 的每日 token 排名中超过了 OpenClaw，当天报告的总量为 2240 亿个 token，高于之前的 1860 亿，使 Hermes 按总 token 量位居第一。

到 6 月下旬，OpenRouter 的应用排名中，Hermes 按总 token 量也位居第一，超过 22 万亿。GitHub 星标、token 体量和平台背书衡量的是不同类型的采用，它们很少同步变动。Nous 还将可移植性作为宣传重点，发布了一个 `hermes claw migrate` 命令，可以一步导入 OpenClaw 用户的设置、记忆、技能和密钥。

开发者可以持有一个包含代码库、约定和先前决策的代理，并持续数周，而不是每天早上重新构建该上下文。团队可以通过单个命令在不同提供商之间迁移代理，因为 Hermes 在数百个模型中保持模型不可知性（model-agnostic）。其代价是运营成本，因为运行 Hermes 的团队必须自行保障和维护其运行的基础设施。

## 广泛性、深度及适用场景

这种选择类似于托管云服务与自托管基础设施之间常见的权衡。托管服务方便且受供应商治理，而自托管基础设施提供完全的控制权和运营责任。

许多企业会根据工作负载同时运行这两者。两个项目都没有局限于单一能力。OpenClaw 包含记忆和技能，Hermes 也可以跨二十多个渠道进行通信，因此区别在于侧重点而非排他性。下表映射了常见案例，需要注意的是，两者都是新兴平台而非成熟产品。

| 场景 | 更适合的选择 | 原因及权衡 |
| --- | --- | --- |
| 需要审计和策略控制的受监管企业 | NemoClaw 下的 OpenClaw 或 Microsoft Scout | Nvidia 或 Microsoft 为代理包裹了治理和身份验证，尽管两者尚处于早期阶段且将买家绑定在他们的技术栈中 |
| 希望代理学习其工作并保持可移植性的开发者 | Hermes | 持久化记忆和自我提升技能是其设计中心，代价是需要自行运营基础设施 |
| 团队需要在多个聊天平台接触用户 | OpenClaw | 网关和庞大的技能市场覆盖了竞争对手无法比拟的广泛性，尽管技能质量参差不齐且供应链风险确实存在 |
| 组织标准化使用单一提供商的云 | Microsoft 365 内的 Scout | 在该生态系统内集成最深，但在生态系统之外的可移植性最差 |

实际部署不会标准化于一种方法。Nvidia 的 NemoClaw 蓝图已经在 OpenShell 下运行 Hermes 代理，就像它们运行 OpenClaw 一样容易。治理层正在构建，旨在位于多个代理项目之下，而不是二选一。

## 为什么工具链层至关重要

在任何代理触及生产系统之前，企业买家应放慢脚步，考虑两个问题。第一个问题是问责制。当代理像 Hermes 一样可以在会话之间重写其自身的记忆和技能时，团队需要知道谁可以解释行为的变化以及这些变化记录在哪里。第二个问题涉及所有权。当治理和身份验证来自平台供应商（如 NemoClaw 和 Scout）时，策略引擎和身份标识属于该供应商，而不是运行代理的团队。

> Nvidia 和 Microsoft 正在竞争，旨在将治理、身份验证和可观测性置于客户选择的任何代理之上。

对于平台供应商而言，奖品是运行时层，它将比任何单一的基础模型更长久。Nvidia 和 Microsoft 正在竞争，旨在将治理、身份验证和可观测性置于客户选择的任何代理之上，这就是为什么 NemoClaw 在支持 OpenClaw 的同时也支持 Hermes。

安全性属于同样的逻辑。对 OpenClaw [技能市场](https://thenewstack.io/openclaw-github-stars-security/)的审计在扫描的技能中标记了 341 个恶意条目，安全公司报告称，今年早些时候有数万个实例处于暴露状态——这就是受治理的运行时旨在解决的缺口。

## 未来展望

代理市场正在从模型选择转向运行时、治理和记忆层。OpenClaw 表明，广泛的网关和庞大的技能生态系统可以吸引开发者并吸引 OpenAI、Nvidia 和 Microsoft。Hermes 表明，持久化记忆和自我提升技能可以在没有相同平台支持的情况下驱动巨大的日常使用量。广泛性和深度是否会保留在单独的项目中尚不确定，因为 NemoClaw 在一套统一的控制下运行，且 Hermes 可以导入 OpenClaw 的设置。

### 下一个阶段将取决于所有权。

企业将需要知道谁控制代理积累的记忆，谁治理代理可以调用的工具，以及谁拥有维持其存活的运行时。一个已经学习了一年开发者习惯的代理，其转换成本要远高于仅仅连接到许多应用程序的代理。记忆，比渠道覆盖范围，正成为持久的锁定形式，这就是为什么运行时、治理和记忆层是平台供应商在两个项目之下进行竞争的战场。