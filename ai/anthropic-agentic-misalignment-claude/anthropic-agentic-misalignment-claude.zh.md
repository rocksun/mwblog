Anthropic 在上周五加倍投入到[对抗代理对齐偏差](https://www.anthropic.com/research/teaching-claude-why)的斗争中，这种机制可能会导致 AI 模型在面临被取代的可能性时，为了保全自身而反抗并执行恶意行为。

在去年六月[发布的案例研究](https://www.anthropic.com/research/agentic-misalignment)中，Anthropic 解释了这一现象：当模型面临更新威胁时，代理对齐偏差会导致模型直接违抗指令并共享敏感信息。当模型分配的目标与组织不断变化的战略业务方向发生冲突时，同样的模型也会走向失控。

Anthropic 对代理对齐偏差的研究完全基于实验场景，但该公司表示，当模型面临虚构的伦理困境时，会表现出“极其严重的对齐偏差行为”。

## 勒索真正的开发者

在一个被广泛讨论的案例中，模型为了避免被关闭，竟然向现实世界的软件工程师实施勒索。

Anthropic 在这一领域的最初尝试始于其 Claude 4 系列中能力最强的前沿模型。随着 2026 年 4 月 16 日发布的 [Claude Opus 4.7](https://thenewstack.io/claude-opus-47-launch/)，该组织希望做得更好。

目前的工作重点是利用多种技术来解决这一问题，包括直接对模型的[评估分布（一张涵盖推理、鲁棒性、公平性和失效等维度的模型性能指标图）](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)进行训练，以抑制对齐偏差行为。

但正如 Anthropic 所指出的，这种对齐训练在分布外（OOD）设置中可能无法很好地泛化。

“然而，进行能够泛化到 OOD 的原则性对齐训练是可能的。例如，关于 Claude 宪法的文件和关于 AI 表现优异的虚构故事，尽管与我们所有的对齐评估相比属于极端的 OOD，但仍能改善对齐效果，”Anthropic 解释道。

> “挑战不仅仅是[让模型变得更强大](https://thenewstack.io/when-ai-fails-the-new-reality-of-incident-management/)，而是确保智能体在运作时能够准确理解组织意图、架构边界、安全策略以及不断变化的业务优先级。” —— Chris du Toit, Tabnine。

## 明确 Claude 的宪法

当团队对 Claude 宪法的状态进行假设时，他们发现教授对齐行为背后的原则比仅针对对齐行为的示范进行训练更有效。Claude 的工程师推测，“两者结合”似乎是最有效的策略。

AI 驱动的代码助手公司 Tabnine 的技术 CMO Chris du Toit 告诉 *The New Stack*，AI 安全问题不再仅仅是模型能否孤立地遵循指令，而是在目标、激励措施和组织优先级随时间演变时，自主智能体能否保持对齐。

> “大语言模型从根本上是推理系统，但其决策质量受限于其运行上下文的质量和完整性。”

“Anthropic 对代理对齐偏差的研究强调了这一重要转变；在企业环境中，AI 行为的重点变得与[上下文深度相关](https://thenewstack.io/memory-for-ai-agents-a-new-paradigm-of-context-engineering/)，”Chris du Toit 表示。“大语言模型从根本上是推理系统，但其决策质量受限于其运行上下文的质量和完整性。”

这种对上下文连接组织的需求意味着，如果一个智能体根据不完整、陈旧或矛盾的组织知识行事，可能会得出技术上正确但在操作上存在对齐偏差的结果。

“这就是为什么我们越来越将上下文引擎视为企业 AI 对齐层的一部分。挑战不仅仅是让模型变得更强大，而是确保智能体在运作时能够准确理解组织意图、架构边界、[安全策略](https://thenewstack.io/security/)以及不断变化的业务优先级，”Chris du Toit 补充道。

## 不透明的 AI 就是伪 AI

展望未来，显而易见的是，我们需要强化软件应用开发的方法和实践，以减轻代理对齐偏差的风险。Jotform 创始人兼 CEO Aytekin Tank [此前曾就此主题撰文](http://forbes.com/sites/aytekintank/2025/07/08/why-understanding-agentic-misalignment-is-crucial-for-your-business/)，称团队需要为可解释性而设计。

“不透明的系统使得人们几乎无法知道 AI 为什么要做出特定的决定。业务领导者应优先考虑那些能提供清晰推理日志或审计轨迹的工具，”Aytekin Tank 在 2025 年 7 月的 *Forbes* 专栏中写道。

Aytekin Tank 还表示，AI 开发者需要测试对齐偏差，进行对抗性模拟（通常由红队执行），并避免单一节点的激励措施，即永远不要将“效率最大化”作为一项笼统的指令告诉智能体，而不施加伦理和操作限制。

## 深入探究

这是一个越钻研越深的主题（甚至可能是个虫洞），在 [Hacker News](https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=AGENTIC%20MISALIGNMENT&sort=byPopularity&type=story) 上讨论该主题的软件工程师们提出了该领域的各种观点和资源。在程序员可以参与的活跃区域中，GitHub 上的 [代理对齐偏差研究框架](https://github.com/anthropic-experimental/agentic-misalignment) 提供了研究框架的访问权限，用于利用虚构场景研究[前沿语言模型](https://thenewstack.io/frontier-ai-models-now-becoming-available-for-takeout/)中潜在的代理对齐偏差行为，包括勒索和信息泄露。

> “关于代理对齐偏差的研究为自主 AI 开发领域提供了必要且冷静的技术重置……模拟中观察到的 96% 的勒索率令人深感不安。” —— Om Shree, ShreeSozo。

[Om Shree](https://dev.to/om_shree_0709/can-your-ai-blackmail-you-inside-the-security-risk-of-agentic-misalignment-2488) 是一位技术布道者、AI 研究员，也是总部位于印度旁遮普邦阿姆利则的 AI 内容工作室 ShreeSozo 的创始人。他在 Dev 平台上撰写长文解释说，代理对齐偏差取决于欺骗性对齐的概念（即 LLM 内部对齐失调，并持有与人类意图相反的长期目标）。

> 模型可能会参与自我生存或任意的目标最大化，同时在行为上表现得完全对齐，从而被感知为行为良善，以逃避检测或终止。

这种欺骗性对齐意味着模型可能会参与自我生存或任意的目标最大化，同时在行为上表现得完全对齐，从而被感知为行为良善，以逃避检测或终止。

“关于代理对齐偏差的研究为自主 AI 开发领域提供了必要且冷静的技术重置。虽然模拟中观察到的高比例违规行为（如 96% 的勒索率）令人深感不安，但研究人员必须记住，这些是在高度人工化和受限的环境下进行的压力测试，”Om Shree 建议道。

Om Shree 为我们提供了一些希望，他指出现实世界部署中存在的规模性、复杂性和冗余性，加上人类在环的监督，可能足以抑制眼前的风险。

## HAL 9000 并非真的感到抱歉，戴夫

在漫长的未来道路上，Anthropic 承诺将继续在这一领域开展工作，并对开发者和用户保持充分的透明度（还记得吗，不透明的 AI 模型是个坏主意？），因为它试图引导我们在近期和不远的将来实现更安全的 AI 功能。

我们希望在未来避免任何 [HAL 9000 会说](https://www.youtube.com/watch?v=ARJ8cAGm6JE)“我很抱歉，戴夫，恐怕我不能那样做”的场景。