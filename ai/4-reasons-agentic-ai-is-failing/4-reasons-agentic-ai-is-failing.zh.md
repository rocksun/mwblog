企业采用 AI Agent 有很多理由，例如可以提高生产力并减少员工的乏味感。

AI Agent 的实施也存在许多失败的可能 —— 随着越来越多的组织转向采用 Agentic AI，聪明的组织会积极思考如何领先于可能导致 Agentic 项目出错的陷阱。

作为一名已经为内部使用和代表企业客户部署了多个 AI Agent 的人，我已经学会了一些关于如何避免 AI Agent 实施失败的经验。请继续阅读，了解我对失败的主要原因的看法，以及缓解这些原因的技巧。

## 什么是 AI Agent，企业如何使用它们？

AI Agent 是一种自主软件系统，可以感知其环境、做出决策并采取行动。

通过创建与特定用例相符的自定义 Agent，组织可以部分或完全自动化复杂的任务，而这些任务以前需要员工手动完成。

Agentic AI 技术相对较新，生产就绪的 Agentic AI 技术和框架（例如 [模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)，或 MCP）在过去一年左右才开始可用。尽管如此，AI Agent 已经在商业环境中获得了广泛的应用：根据 IDC 2025 年夏季的研究，截至当时，[34.1% 的企业](https://my.idc.com/getdoc.jsp?containerId=US53383725) 已经开始采用 Agentic AI。

## 采用 Agentic AI 失败的主要原因

但同样，开始实施 AI Agent 是一回事。成功完成项目是另一回事。以下是 Agentic AI 实施可能失败的主要原因。

### 1. 不切实际的期望

AI Agent 是一种强大的解决方案，能够自动化任务和工作流程，否则这些任务和工作流程需要手动完成。但它们不能变魔术。它们可能无法完成高度复杂的任务，或者那些需要人类才能提供的上下文感知类型（如对人类情感的理解）的任务。

这并不是说 AI Agent 在这些情况下没有帮助。它们可能仍然有用，但前提是它们与人类一起工作，而不是代替人类。换句话说，通常需要保持“人机回路”，AI Agent 才能实现其目标。

通常情况下，Agent 也难以在最初就擅长其预期的任务。通常，它们[必须经过迭代开发过程才能](https://thenewstack.io/engineers-must-become-agile-collaboration-ninjas/) 能够满足期望，这意味着它们可能无法像高管希望或期望的那样快速地交付业务价值。

未能理解这些限制，或者对 AI Agent 的能力设定不切实际的期望，是实施未能完全实现其目标的一个常见原因。

### 2. 糟糕的用例优先级排序

鉴于 AI Agent 的巨大潜力，组织很容易尝试开发自定义 [Agent，旨在处理所有可能的用例或工作流程](https://thenewstack.io/semantic-router-and-its-role-in-designing-agentic-workflows/)。

对于大多数公司来说，这是一个错误，因为它使他们处于承担超出自己能力范围的位置。如果您的组织是 AI Agent 的实施和管理的新手，它应该从简单的用例开始，这些用例中的任务定义明确且结果易于衡量（例如部署软件应用程序或将数据写入数据库，仅举几个例子）。

只有在这些任务中取得成功后，组织才能转向更复杂的用例。尝试从一开始就处理涉及多个变量或系统的复杂任务不会让您走上成功的道路。

### 3. 数据质量问题

古老的“垃圾进，垃圾出”的说法适用于许多类型的 IT 系统。但它与 AI Agent 尤其相关，如果它们无法访问正确类型的数据，或者它们使用的数据质量较低，它们将难以有效地运行。

这就是为什么确保 [AI Agent 能够访问](https://thenewstack.io/system-two-ai-the-dawn-of-reasoning-agents-in-business/) 它们实现预期任务所需的数据至关重要。（当然，它们不应能够访问与其预期用例无关的资源，因为这会产生安全风险。）通常，这不仅包括易于管理的资源，例如结构化数据库，还包括自由格式的非结构化数据，例如文档集合。

同样重要的是在将数据暴露给 Agent 之前清理数据，以避免缺失、不完整、过时或陈旧的信息 —— 例如，一个 [来源的客户信息与](https://thenewstack.io/dispelling-myths-of-open-source-complexity-with-apache-iceberg/) 另一个来源的数据冲突的情况。如果没有准确和一致的数据，Agent 更容易做出错误的决策，因为它们无法有效地解释其环境。

### 4. 治理挑战

通过记录和审计 Agent 的 [活动来跟踪 Agent 正在做什么的能力对于治理和安全性至关重要](https://thenewstack.io/how-attackers-move-from-azure-active-directory-to-on-prem-ad/)。这种可见性还在 [Agent 的开发中起着重要作用](https://thenewstack.io/playing-dd-with-ai-the-agentic-ai-developers-achilles-heel/) 和增强，因为日志记录和审计跟踪对于识别错误（例如意外修改敏感数据）并通过实施新的防护措施来纠正它们是必要的。

不幸的是，目前大多数 Agentic AI 框架提供的用于解决这些挑战的内置功能有限。但是，通过足够的开发工作，可以实施自定义治理解决方案来支持 Agentic AI 的成功采用。这比采用现成的解决方案并称其为一天的结束要付出更多的努力，但对于平衡 AI Agent 的强大功能与潜在的治理风险是必要的。

## 一种生产就绪的 Agentic AI 采用方法

如果我上面提出的挑战听起来很熟悉，那可能是因为许多相同的问题在生成式 AI 采用过程中也存在。也就是说，AI Agent 使其中的一些挑战加倍，因为与生成式 AI 系统不同，Agent 不仅仅是创建内容。它们可以采取独立行动，直接影响 IT 系统的性能和可靠性，这就是为什么在制定 Agentic AI 采用和实施策略时，从一开始就做好事情如此重要的原因。