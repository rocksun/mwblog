<!--
title: 避免AI代理可靠性税：开发者指南
cover: https://cdn.thenewstack.io/media/2025/08/b2fa5cf9-ai-agent-reliability-tax.jpg
summary: 文章强调了Agentic AI的可靠性至关重要，并提出了五个支柱：可预测性、保真度、可控性、稳健性以及安全和保障。同时，文章还强调了上下文工程的重要性，并提到了Salesforce的Agentforce平台如何通过提供测试、治理和监控工具来帮助企业大规模部署可靠的AI代理。
-->

文章强调了Agentic AI的可靠性至关重要，并提出了五个支柱：可预测性、保真度、可控性、稳健性以及安全和保障。同时，文章还强调了上下文工程的重要性，并提到了Salesforce的Agentforce平台如何通过提供测试、治理和监控工具来帮助企业大规模部署可靠的AI代理。

> 译自：[Avoiding the AI Agent Reliability Tax: A Developer’s Guide](https://thenewstack.io/avoiding-the-ai-agent-reliability-tax-a-developers-guide/)
> 
> 作者：Drew Robb

人们对生成式人工智能（GenAI）的兴趣正在从开发模型转向创建能够自主执行各种任务的代理。但是，如果不对端到端的可靠性有充分的掌握，就释放[Agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)的功能，麻烦就会随之而来。

Salesforce 的首席开发者倡导者 [Mohith Shrivastava](https://www.linkedin.com/in/mohith-shrivastava/) 在一次采访中告诉我：“不可靠的代理不仅仅是效率低下，它们代表着运营、财务、法律和声誉方面的重大风险。随着 Agentic AI 的大规模部署，可靠性成为中心架构原则。”

## 避免 AI 代理的“可靠性税”

一个不可靠的代理所带来的远不止效率低下。它是一种负担，可能引发运营中断、法律风险和声誉损害。 Shrivastava 将此称为“可靠性税”。

当今过多的 AI 应用程序和 Agentic AI 部署都是脆弱的、不一致的，并且需要持续的监督。因此，组织面临着对护栏、检索管道、监控、治理和安全加固的持续投资，以修复无法预见的 AI 问题并防止不准确和幻觉。

Shrivastava 说：“我们已经从确定性自动化（系统执行预先编程的规则）转变为概率自主（代理自行感知、推理和行动）。这带来了巨大的潜力，但也引入了[全新的故障模式](https://thenewstack.io/mcp-a-practical-security-blueprint-for-developers)。”

## Agentic AI 成功的 5 大支柱

他强调，可靠性是一个多维要素，由五个支柱组成：

* **可预测性：** 在限定范围内的一致行动。
* **保真度：** 基于可验证来源的准确性。
* **可控性：** 遵循明确的指示和约束。
* **稳健性：** 在混乱或对抗性条件下的弹性。
* **安全和保障：** 避免伤害和抵抗恶意利用。

许多设计者在其中一些支柱上做得很好。但每一个支柱都是必不可少的。如果其中一个失败，级联故障将不可避免。

## 防止范围蔓延和幻觉

坚持可靠性原则必须与避免范围蔓延的需求相平衡。 Shrivastava 建议在构建之前从战略范围定义开始。然后可以使用以下方法加强该定义：

* 零信任身份和访问控制
* 工具使用允许列表
* 人工参与的检查点
* 日志记录和监控
* 紧急停止开关

可以通过诸如[检索增强生成（RAG）](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary)之类的技术来解决幻觉问题，而无需重新训练模型。这有助于减少幻觉的数量，无论是在忠实性错误（与上下文相矛盾）还是事实性错误（与现实相矛盾）方面。

## 超越 Prompt 工程

诸如[思维链](https://towardsdatascience.com/short-and-sweet-enhancing-llm-performance-with-constrained-chain-of-thought-c4479361d995/)或[自我一致性](https://towardsdatascience.com/achieving-greater-self-consistency-in-large-language-models-6e6cb5f3c5b7/)之类的 Prompt 工程技术旨在确保代理遵循命令。但是，为了真正遵守指令，开发人员必须采用上下文工程。正如 Prompt 工程通过仔细考虑上下文和结构，远远超出了简单的 Prompt 提示一样，上下文工程使用严格的迭代方法来架构完整的上下文，从而优化指令以确保它们实现所需的结果。

“上下文工程是一门艺术和科学，它为 AI 代理提供正确的信息、正确的工具和正确的指令，以便代理能够完成给定的目标。将上下文视为代理的运行时“RAM”——Prompt 提示、指令、检索到的数据和历史记录，”Shrivastava 说。“超载它、毒害它或制造冲突，可靠性就会受到影响。”

开发人员需要他们可以使用的工具，这些工具可以将上下文工程付诸实践。此类工具必须能够定义捕获要完成的确切任务的主题，以便 AI 代理了解每个场景的范围、触发器和所需的结果。这些主题为代理何时以及如何采取行动提供了结构，从而确保响应保持相关并与业务目标保持一致。

Shrivastava 补充说，从那里开始，应该为代理配备有效的工具来完成给定的目标。然后，可以通过总结正在进行的对话并通过 Prompt 模板、对话变量或上下文变量重用该上下文来有效地管理内存。因此，勤奋的 Prompt 工程可以在主题、指令和范围的框架内完善代理的行为，并且通过 RAG 进行检索可以动态地[提取相关数据](https://thenewstack.io/beyond-ai-models-data-platform-requirements-for-agentic-ai)，以提供精确的、上下文感知的响应，同时保持上下文窗口的优化。

“企业需要一个平台，该平台提供所有工具，以简单易管理的方式完成上下文工程的许多方面，”Shrivastava 说。“这必须包括内置的护栏和治理，以评估代理在生成响应时解释主题指令的效果如何。”

在完成所有这些步骤后，仍然至关重要的是，要密切监控和衡量代理的性能。因此，开发人员工具应提供深度可观测性、实时健康状况监控、消耗跟踪和丰富的采用分析，以支持结果的验证和稳定改进。例如，使用 Salesforce 的 Agentforce 配置的服务代理具有报告已解决对话、升级和放弃对话的百分比的功能。同样，Agentforce 自带的销售代理具有分析功能，可以报告销售收入受代理的影响程度。

## 正确的平台和正确的工具 = 可靠性

对于企业 Agentic AI 而言，可靠性不再是可选功能。它已成为任何架构的基本组成部分。这种转变是必要的，因为代理现在在概率自主而不是确定性脚本上运行。

实现代理可靠性需要一种有纪律的端到端方法，而不仅仅是使用模型。根据 Shrivastava 的说法，它包括：

1. **上下文工程：** 仔细定义代理的范围、操作、内存、Prompt 提示和 RAG 用法。
2. **严格的治理：** 实施严格的控制，例如[零信任安全](https://thenewstack.io/what-is-zero-trust-security/ "zero trust security")、批准的操作列表（允许列表）、人工监督（人工参与，或 HITL）和全面的日志记录。
3. **持续评估：** 不断监控和测试代理在实际场景中的性能。

Shrivastava 说：“组织必须计划维护护栏、数据管道、测试和可观测性的持续成本。提供用于评估、RAG 和性能分析的内置工具的平台可以帮助降低此成本，并支持开发更高级的、自我纠正的 AI 系统。”

Salesforce 的 Agentforce 具有内置工具，可帮助企业大规模部署代理。例如，Agentforce 的[测试中心](https://www.salesforce.com/news/press-releases/2024/11/20/agentforce-testing-center-announcement/)部分允许团队在上线之前在沙盒中运行基于场景的、数据集驱动的评估（包括合成测试用例）。这样，他们可以及早发现不遵循指令和工具使用错误的情况，从而减少可靠性税。Agentforce 提供了大规模实施自主 AI 代理所需的所有工具，同时添加了企业运营中所需的护栏、治理和控制。

有关更多信息，请访问 [Agentforce](https://www.salesforce.com/agentforce/)。