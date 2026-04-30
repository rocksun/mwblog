[Sentry](https://sentry.io/welcome/) 是一家应用监控和错误追踪服务提供商，该公司于周二发布了 Seer Agent。这是一款自然语言调试工具，允许开发者通过查询公司完整的可观测性技术栈来调查生产环境中的问题。

该工具目前对所有启用了 Seer 的 Sentry 客户开放公开测试版。在观察开发者实际如何使用其平台后，Sentry 发现了一个明显的缺口，而该工具正好填补了这一空白。

Sentry 工程高级总监兼 AI 业务负责人 Indragie Karunaratne 告诉 The New Stack，用户不断遇到 Sentry 现有 AI 工具并非为此设计的问题。Sentry 拥有调查这些数据，但这些问题并不是大多数开发者通常会与 Sentry 这样的平台联系起来的传统错误（Bug）。

![](https://cdn.thenewstack.io/media/2026/04/5025e36e-seer-agent_video.gif)

Sentry 的 Seer Agent。图片来源：Sentry。

“在观察人们使用 Autofix 以及普遍使用 Sentry 产品的过程中，我们注意到人们想要一些更具开放性的东西。因为有些类型的问题 Sentry 可能尚未察觉——例如客户通过反馈渠道报告了某些情况，或者你在仪表板上看到某个指标出现了异常，”Indragie Karunaratne 说道，“在 Sentry 的定义中，这些都不完全属于‘问题（issue）’；它们尚未以任何方式被识别为故障。”

Sentry 表示，Seer Agent 无需额外设置，可从 Sentry 仪表板的任何页面调用。它能为开发者当前查看的内容提供上下文，并能查询 Sentry 收集到的关于应用的所有遥测数据。

## 从 Autofix 到开放式调查

Seer Agent 是 Sentry [Seer](https://sentry.io/product/seer/) 旗下的第二个主要产品。第一个产品 [Autofix 于 2024 年 3 月发布](https://thenewstack.io/sentry-founder-ai-patch-generation-is-awful-right-now/)，是一款人机协同的调试工具。当时，Sentry 将其比作一名初级工程师，可以处理已知问题，执行根源分析并生成代码修复补丁，但在整个过程中需要人工引导。

但 Autofix 的启动前提是 Sentry 已经检测到了一个明确的问题。Seer Agent 则不同，开发者只需简单描述一个症状（比如页面变慢或客户投诉），代理程序就会开始调查问题。

Indragie Karunaratne 指出，Agent 和 Autofix “只是构建在相同基础、相同数据和相同代理架构上的两种工作流。Autofix 只是更侧重于 Sentry 发现的某个特定的、定义明确的问题，而 [Seer Agent] 则可以根据你的需求，调整调查范围的广度或深度。”

![](https://cdn.thenewstack.io/media/2026/04/b95d2dca-original_seer-agent-result-783x1024.png)

Sentry 已经在内部运行 Seer Agent 数月之久，Indragie Karunaratne 表示它改变了团队处理事故的方式。“每当 Sentry 宕机或出现严重告警时，工程师们就会开始使用 Seer Agent 进行排查。与人类手动分析问题、查找数据相比，他们通常能在几分钟内找到事故的根源，”他说道。

> “每当 Sentry 宕机或出现严重告警时，工程师们就会开始使用 Seer Agent 进行排查。与人类手动分析问题、查找数据相比，他们通常能在几分钟内找到事故的根源。”

在最近的一个案例中，Sentry 团队在公告中写道，Seer 本身开始出现故障。Indragie Karunaratne 在等待值班工程师上线时使用 Seer Agent 进行了调查。该代理识别出，由于供应商侧的[上游基础设施问题](https://blog.sentry.io/seer-fixes-seer-debugging-agent/)，导致特定区域对特定模型的调用失败。在通常情况下，诊断此类问题需要大量的侦察工作。

## 遍历遥测图谱

Sentry 指出，Seer Agent 搜索遥测数据的方式与带有搜索工具的通用大语言模型（LLM）不同。Sentry 的遥测数据已经实现了该公司所谓的“追踪关联（trace-connected）”。系统知道错误发生的追踪路径，代理随后可以利用这一点查看日志和其他相关数据。

“它不是在猜测时间范围，并希望正确的行出现在文本搜索中；它是在遍历摄取时构建的图谱，”Sentry 在公告中写道。

> “它不是在猜测时间范围，并希望正确的行出现在文本搜索中；它是在遍历摄取时构建的图谱。”

Indragie Karunaratne 解释说，为了让代理发挥出色，它需要访问所有这些数据，但[上下文管理](https://blog.sentry.io/want-ai-to-be-better-at-debugging-its-all-about-context/)在此至关重要。

“如果你做得太过火，把所有的上下文都拉进来，代理的表现会很差。如果你拉入的上下文太少，它也会以另一种方式表现不佳，”Indragie Karunaratne 说道，“在只拉取有用信息和缩小数据分组范围之间找到平衡，是一个非常普遍的难题。”

## 专用调试代理的必要性

考虑到现在的编程代理（coding agents）已经变得非常强大，专用的调试工具是否还有必要？Indragie Karunaratne 承认，开发者（以及为工具付费的人）可能会问自己这个问题。

“对于简单的调试，你可以从 Sentry 获取堆栈追踪并将其粘贴到编程代理中进行调试，”他说道，“但我们发现，生产环境中的大多数问题都有非常复杂的失败模式——跨多个代码仓库的问题、包含许多不同组件的复杂分布式系统、极其复杂的遥测数据——因此你需要一些关于如何引导代理正确利用这些遥测数据的知识。而所有这些都内置在 Seer 中。”

因此，Sentry 并没有与编程代理竞争，而是选择与它们集成。该公司已经为 Cursor 和 Claude Code 构建了集成，因此开发者可以将 Seer 的根源分析结果移交给他们自己环境中的编程代理。Sentry 计划将这些集成扩展到 GitHub 和其他开发者工具中。

长期的发展方向是迈向主动性。Indragie Karunaratne 表示，团队希望 Seer “表现得像一名 24/7 全天候在线的工程师，为你分拣问题、观察症状，然后决定是否深入挖掘。理想情况下，它只需在后台运行，发现问题、发出告警并修复问题——这是通过代理和 Autofix 工作流的结合来实现的。”