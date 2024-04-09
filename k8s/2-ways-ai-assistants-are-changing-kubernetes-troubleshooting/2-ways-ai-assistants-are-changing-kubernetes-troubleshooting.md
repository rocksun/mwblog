
<!--
title: AI助手改变Kubernetes故障诊断的2种方式
cover: https://cdn.thenewstack.io/media/2024/04/d428b6a6-ai-changing-kubernetes-troubleshooting.jpg
-->

人工智能模拟人类解决故障的方法，可以实现民主化，并改善人们识别和修复 Kubernetes 问题的方式。

> 译自 [2 Ways AI Assistants Are Changing Kubernetes Troubleshooting](https://thenewstack.io/2-ways-ai-assistants-are-changing-kubernetes-troubleshooting/)，作者 Blair Rampling。

在围绕 AI 的所有喧嚣中，最误导人的部分是对微调大型语言模型 (LLM) 的坚持。太多人认为，基于大量特定领域数据对模型进行专门化是构建有用的 AI 助手唯一的方法。

在高度专业化或技术领域（例如软件开发和云服务）中，对微调的需求更为普遍。一个典型的例子是为交付应用程序而设计的 Kubernetes 集群的持续维护和故障排除。这种情况突出了 DevOps 和应用程序开发领导者面临的关键挑战：需要有更好的解决方案来管理[云原生基础设施](https://thenewstack.io/the-cloud-native-community-needs-to-talk-about-testing/)的复杂性。这些环境通常会带来难以解决的挑战，这些挑战会违背经验、智慧或[故障排除方面的直觉](https://thenewstack.io/why-intuitive-troubleshooting-has-stopped-working-for-you/)。

作为回应，初创公司和开源项目声称已经微调了现有模型，以包含有关 Kubernetes 的专门知识，而通用模型（甚至是 GPT-4 Turbo）通常不会摄取或访问这些知识。

然而，挑战不在于微调本身，而在于它无法模仿人类的故障排除方法。无论模型多么智能，除非它能够复制你执行故障排除的方式，否则你将无法获得任何实际价值：收集不同的资源，在你的脑海中整理你在日志和 kubectl 输出中找到的所有关键细节，依靠你的经验，并将所有这些提炼成一个合乎逻辑的下一步。

只有两个关键领域可以使 AI 助手在 [Kubernetes 世界](https://thenewstack.io/the-quest-for-high-quality-kubernetes-deployments/)中发挥作用。助手必须：

- 嵌入到 Kubernetes 集群中，可以访问描述其状态的工件，例如 kubectl get/logs/describe 的输出。
- 能够用自然语言理解你的问题，并将复杂的操作数据转换为简单、可操作的下一步。

微调只是优先考虑炒作，而不是对你最重要的事情：根据 pod、节点和应用程序的实际情况采取行动。

## 让 Kubernetes AI 辅助功能发挥一半作用

AI 和云原生空间正在同时增长，因此新工具在这两个领域中重叠。

[K8sgpt](https://github.com/k8sgpt-ai/k8sgpt) 和 [KoPylot](https://github.com/avsthiago/kopylot) 等新的开源命令行界面 (CLI) 工具围绕 kubectl 展开其操作以访问你的集群状态。通过使用 .kube/config 文件中可用的上下文代表你运行该命令，这些工具可以直接读取和处理输出，而不是强迫你切换上下文。然后，他们将数据代理到 OpenAI 的 API，以在你的终端中提供 AI 生成的响应。

这是一个聪明的解决方法，但这些 CLI 工具仍然需要高水平的 Kubernetes 知识或另一个 CLI 工具。你需要知道正确的命令，而不仅仅是你集群状态的问题，才能启动交互。

另一个开源工具 [mico](https://github.com/tahtaciburak/mico) 通过将你的自然语言查询转换为 kubectl 命令来推进这个概念。例如，你可以要求 mico 打印 xyz 命名空间中每个 pod 重新启动的次数，它将使用 kubectl 中的 jsonpath 参数将输出过滤到仅包含相关行。

我们很高兴看到开源社区如何利用 AI，但这些工具是有限的：它们要么理解集群状态但无法处理自然语言查询，要么帮助你编写查询但仅返回 kubectl 输出，而没有后续故障排除步骤。你可以使用专门的替代方案替换为这些工具提供支持的默认 OpenAI 模型，但这并不能帮助你减少故障排除时间或帮助经验较少的同行监控他们的应用程序。

## 什么让 AI 辅助功能对 Kubernetes 故障解决有价值？

答案是 AI 助手，它擅长理解集群状态和解释自然语言——该死的微调。

### 访问你的集群状态

如果没有访问集群状态，从 AI 助手那里获得帮助的唯一方法就是在解决问题的过程中玩一场电话游戏。即使使用经过微调的 AI，你也可以期待对话有点像这样：

1. 你对 Kubernetes 了解得足够多，可以在[部署](https://thenewstack.io/the-quest-for-high-quality-kubernetes-deployments/)W没有立即出现时运行 kubectl get pods。
2. 你问你的 AI 助手，为什么 pod 会因 CrashLoopBackOff 错误而崩溃。
3. AI 会告诉你 CrashLoopBackOfferror 最常见的原因包括内存不足、依赖项缺失以及由于端口冲突导致的容器故障。它可能足够智能，可以要求你运行 `kubectl describe pod POD_NAME` 来了解有关其资源使用情况和限制的线索……也许。
4. 你将该输出告诉你的 AI 助手，包括 Terminated 状态和最后发出的事件：回退重启失败的容器。
5. AI 建议你运行 `kubectl get events --field-selector involvedObject.name=POD_NAME` 来搜索其他可能的原因。
6. 你发现了有关失败的准备就绪和活动性探测以及回退过程的事件，但没有发现任何新内容，并让你的 AI 助手知道了这一点。
7. AI 助手建议你运行 `kubectl logs POD_NAME --all-containers` 来从你的清单中搜索容器化应用程序或其依赖项（如数据库或消息队列）的特定错误。
8. 在冗长的日志中，你发现了 `docker-entrypoint.sh` 的警告，称其由于 `not found` 参数而无法执行。
9. 你向你的 AI 助手询问了该警告，它（最终）告诉你检查你的 Kubernetes 清单，看看你附加到该容器的参数中是否存在拼写错误或错误配置，这是你问题的根源。

你的 AI 工具当然提供了帮助，但这种帮助并不是特别有效。它可能让你不必针对每个错误进行 Google 搜索或运行 `kubectl ... help` 命令来查找正确的语法。但是，由于你负责准确地共享有关集群状态的信息并理解 AI 助手中的每一步，因此你仍然承担了几乎所有的认知负荷，并且没有节省太多时间。

访问集群状态至关重要。一个有价值的 AI 助手必须自动响应你关于 CrashLoopBackOff 的原始问题，方法是自行运行 `kubectl` 命令，解析输出以获取线索，从网上提供的[集体 Kubernetes 故障排除知识](https://thenewstack.io/can-chatgpt-save-collective-kubernetes-troubleshooting/)中引入上下文，并提供精确的补救路径——无需运行手册或深入了解文档。

### 理解你的自然语言问题

一个能够读取输出或日志并提供下一步思考内容的执行摘要的 Kubernetes AI 助手非常棒，但它假设你拥有足够的 Kubernetes 知识来了解要运行什么问题或特定的 `kubectl` 命令。真正的附加值，尤其是对于 Kubernetes 操作知识有限的应用程序开发人员来说，来自于用自然语言提问的能力：

- 有些人可能需要询问初学者级别的提示：“什么是 Pod？”
- 其他人在对 Kubernetes 有基本了解的情况下可以询问有关集群的具体问题：“我的 xyz 命名空间中是否有任何失败的 Pod？”
- 最高级的 DevOps 工程师可能会更进一步：“我应该如何处理此通知，该通知称我的一个节点突然 NotReady？”

当 AI 可以将问题转换为收集状态上下文（`kubectl get pods -n xyz`）的相关命令时，它可以有效地减少团队的认知负荷。DevOps 工程师可以通过使用 AI 助手作为反映其专业知识的资源来减少其平均解决时间 (MTTR)，而开发人员可以自助方式对他们的应用程序进行故障排除。

当 AI 助手在你的团队操作的平台上运行时，例如 Slack 或 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Teams，此知识更易于访问和协作。当下一个重大事件影响你的应用程序时，DevOps 工程师和开发人员可以在同一渠道中让你的 AI 助手参与，以进行更有针对性的根本原因分析和超越临时修复的补救计划。

## 一种新型的 Kubernetes AI 助手

为了解决这些问题，Botkube 最近推出了 [AI 助手](https://botkube.io/blog/real-time-platform-engineer-advice-ai-assistant)，该助手旨在在 Kubernetes 故障排除的两个领域和协作平台中直接运行。

该助手的工作原理是倾听你关于 Kubernetes 集群及其应用程序的自然语言问题，将你的查询转换为适当的 `kubectl get/logs/describe` 命令，并与 LLM 交互以探索根本原因和机会。由此，该助手可以提供见解并推荐故障排除过程中的下一步。

![](https://cdn.thenewstack.io/media/2024/04/9b8d0ee9-updateyaml.gif)

此助手通过在两个领域的最佳范围内运行来增强 Botkube 的通知、调查和故障排除工具。使用 AI 助手可以帮助你研究问题发生的原因，学习 `kubectl` 来执行基本操作，或利用 Kubernetes 专业知识来找出根本原因并找到可行的解决方案。

## 集群状态 && 自然语言 >>> 微调 LLM

Botkube 的 AI 助手在底层使用 ChatGPT-4。

我们毫不羞愧地承认，我们使用的是与所有开源工具和大多数新付费平台相同的模型。我们无法微调 ChatGPT 所知的内容，但我们可以为查询添加细微差别，并调整其响应的性质，以提供更好的故障排除体验。

例如，我们在常见的自然语言查询和有关集群状态的数据之上添加了附加说明，以“强制”ChatGPT 提供更全面的答案。我们还使用更好的格式和组织结构丰富了 ChatGPT 的默认输出，以帮助你专注于故障排除，而不是破译说明。

在与 LLM 交互之前和之后添加价值可以做的事情远不止微调。我们设计 AI 助手使其具有上下文感知能力，并且与你真正想向集群提出的问题兼容——而不是你可能习惯的复杂的 `kubectl` 命令。

## 使用 AI 助手的方法

机会通常仅受 `kubectl` 发出的详细信息和 OpenAI 最新模型中内置的 Kubernetes 知识的限制……这已经相当多了。你可以询问：

- 有关 Kubernetes 生态系统的基本问题，例如容器、Pod 和节点之间的差异的详细信息。
- 与集群状态相关的具体问题，例如确认 `xyznamespace` 中的所有 Pod 是否正常。
- 有关新错误通知的具体故障排除帮助，而无需参考运行手册或阅读文档。

Botkube 的 [executor](https://docs.botkube.io/usage/executor/) 功能随后让你可以通过下拉界面（而不是运行十几次 `kubectl ... help`）帮助你制定正确的 `kubectl`，从而将 AI 助手见解转化为立即补救措施。

DevOps 工程师可以通过减少在终端上花费的时间和更多时间在协作发生的地方来加快工作流程。应用程序开发人员可以自行修复 Kubernetes 问题，而无需填写工单并等待他人提供帮助。

无论你的职位或角色如何，你都可以使用新的或现有的 Botkube 帐户立即开始使用 Botkube 的嵌入式 AI 助手。