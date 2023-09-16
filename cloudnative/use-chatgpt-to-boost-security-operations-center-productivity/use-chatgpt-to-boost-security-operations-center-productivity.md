
<!-- 
# 利用 ChatGPT 提高安全运营中心的生产力

https://thenewstack.io/use-chatgpt-to-boost-security-operations-center-productivity/
https://cdn.thenewstack.io/media/2023/08/5563d721-hacker2-1024x711.jpg
Image by NoName_13 from Pixabay
 -->

通过捕获对话，从基础设施中获取相关数据并观察其活动，我们可以比以往获得更多洞察。

译自 [Use ChatGPT to Boost Security Operations Center Productivity](https://thenewstack.io/use-chatgpt-to-boost-security-operations-center-productivity/) 。

管理安全运营中心(SOC)一直是 CISO 和安全分析师的持续痛点。找到能够熟练使用和管理监控工具的经验丰富的网络安全专业人员一直是安全领域的长期挑战。此外，SO 流程的演进速度不足以应对快速转向云基础设施和云原生应用架构的趋势。因此，SOC 员工没有全部的技能、流程和工具来快速识别和响应网络安全事件。

我们相信，使用先进的机器学习和[大语言模型(LLM)](https://roadmap.sh/guides/introduction-to-llms)可以帮助优化安全流程和扩展事件响应(IR)。仅仅考虑自动生成的事后事件报告和自动连续反馈循环的益处。

## 人工智能在事件响应中的作用

类似 ChatGPT 这样的工具可以自动生成综合的事后报告。在事件发生后，它可以查看发生了什么，讨论了什么以及事件是如何得到解决的。它还可以检索与系统拓扑相关的指标、日志和其他元数据，以补充事件细节背景。我们可以利用这些报告决定采取什么行动，使团队变得更具弹性和主动性。

与任何新工具一样，ChatGPT 需要正确的监督并有其自己的学习曲线。人们需要掌握生成式 AI 工具，以确保其行为的准确性和可靠性。这将需要严格的测试和验证。它必须经过训练并定制到您特定的环境。它需要从包含大量上下文的丰富数据集中学习，以防在提示不明确的领域术语时陷入困境。

有了明确的指导方针、定期审查、丰富的基于上下文的数据集以及持续的反馈循环，我们可以实现这一目标。[LLM 的应用](https://roadmap.sh/guides/free-resources-to-learn-llms)可以真正改变 SOC，降低操作艰辛，提高生产力。

## 使用 PromptOps Slack 机器人

那么，您如何使用类似 ChatGPT 的技术来捕获每起事件周围的对话和数据，并有效地实施更改呢？无论您是在调查事件证据收集还是结束端对端的事件响应流程创建，PromptOps Slack 机器人都能满足您的需求。PromptOps 使您可以在 Slack 中存储围绕每个事件所讨论的内容以及它是如何解决的，而无需在平台之间移动。它还可以识别要实施的更改，并自动代表用户生成工单。

让我们来看一个使用 PromptOps 进行事后调查并生成 JIRA 工单应用更改的示例。

### 1. 聆听事件渠道中的讨论

可以将 PromptOps 视为事件渠道中的记录者，它会积极聆听以响应您的问题和请求。

![](https://cdn.thenewstack.io/media/2023/08/86f400d8-image1-e1692821767573.png)

### 2. 在 Confluence 中捕获并存储整个对话

使用 PromptOps 以系统的方式捕获、存储和共享所需上下文的根本原因分析和事后总结。

![](https://cdn.thenewstack.io/media/2023/08/545d1460-image2a.png)

PromptOps 可以根据您在 Slack 中的对话生成每起事件的文档——事件摘要、失败时间轴、相关人员、解决方案和纠正措施。通过这种工作流程，团队可以培养事件响应的速度和信任。

![](https://cdn.thenewstack.io/media/Recording%202023-08-23%20at%2015.37.05.gif)

### 3. 创建Jira工单

最后，PromptOps 可以根据需要实施的更改自动创建 Jira 工单。

![](https://cdn.thenewstack.io/media/2023/08/58dac2d1-image4.png)

我们收集事件证据和创建端到端事件响应流程的解决方案由 `/store` 命令提供支持。通过 Slack 的 slash 命令集成，我们创建了 `/store` 命令，以在您选择的文档存储(如 Confluence 或 Notion)中创建清晰的文档并存储。文档可以以现有模板的格式存储。

更重要的是，它为更好的事件响应创建了一个持续的反馈循环。例如，您使用 `/store` 命令在 Confluence 中的回顾模板中总结了一个事件。另一天，团队遇到同样的问题。但是，与其再次搜索 Slack 对话和知识库，不如直接询问 PromptOps。它会从您创建和存储的文档中提供确切需要的答案。

考虑使用 AI 进行根本原因调查所节省的时间以及使用 PromptOps 等 AI 工具收集证据的速度。如果事后确定根本原因调查不正确，则保存与问题相关的各种指标的给定窗口大小会对未来的分析有用。

## 通过数据进行持续改进

基于生成式 AI 的知识库允许我们拥有最佳实践的集中存储库，以赋能最初级的团队成员像老手一样做出贡献。通过 AI 助手，我们旨在使组织更民主化地访问有价值的信息，并推动更快速的问题解决。AI 将赋能 SecOps 和 DevOps 团队进行异步的沟通和协作，并从相同的上下文中工作。

像 ChatGPT 这样的智能工具最好的一点是它们会变得更加智能。数据为它们提供动力。通过捕获对话并从我们的基础设施中获取相关数据，将其提供并观察其活动，我们可以比以往获得更多洞察。我们可以微调工作流程，自动化更多流程，在降低错误的同时将效率提升到新的高度。

为什么要辛苦工作，当您可以将 PromptOps 等工具连接到SOC解决方案并开始更智能地工作呢？