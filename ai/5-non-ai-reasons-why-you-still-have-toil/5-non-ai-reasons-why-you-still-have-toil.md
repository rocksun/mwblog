
<!--
title: 导致你仍然有繁重工作的5个非AI原因
cover: https://cdn.thenewstack.io/media/2025/03/c3176c8c-wheel3.png
summary: SRE报告揭示Toil不降反升！别只盯着AI，"永远在线"协作、影子IT、官僚主义、技术债务和"快速修复"文化才是真凶。简化工具、拥抱自助服务、IPM监控、微服务和全班次自动化是破局关键，速速优化CI/CD，减少manual任务！
-->

SRE报告揭示Toil不降反升！别只盯着AI，"永远在线"协作、影子IT、官僚主义、技术债务和"快速修复"文化才是真凶。简化工具、拥抱自助服务、IPM监控、微服务和全班次自动化是破局关键，速速优化CI/CD，减少manual任务！

> 译自：[5 Non-AI Reasons Why You Still Have Toil](https://thenewstack.io/5-non-ai-reasons-why-you-still-have-toil/)
> 
> 作者：Leo Vasiliou

Toil——手动、重复性的任务，有时也被称为“忙碌的工作”——自 2020 年以来一直在稳步下降，这要归功于自动化和简化的工作流程。但[我们的年度 SRE 报告](https://www.catchpoint.com/asset/2025-sre-report)显示了一个令人惊讶的逆转，因为花费在 Toil 上的时间中位数在 2025 年停止改善，实际上回升到 2023 年的水平。

![The SRE Report 2025: Toil levels rise](https://cdn.thenewstack.io/media/2025/03/edba79df-image1-3-1024x351.png)

The SRE Report 2025 Insight: Toil levels stopped improving. Is AI adding new demands?

随着 AI 采用的加速，人们很容易想知道是否存在因果关系。头条新闻尖叫着自动化取代工作岗位，但工程师们悄悄地抱怨它带来的新的 Toil——争论提示链，分散我们对[正在累积的技术债务或调试幻觉代码的注意力](https://thenewstack.io/how-frontend-devs-can-take-technical-debt-out-of-code/)。正如一位 DevOps 工程师所说，“我花在修复 AI ‘创造性’基础设施模板上的时间比我编写自己的模板的时间还要多。”

然而，该报告提供了不同的视角。引用[2024 DORA 报告](https://dora.dev/research/2024/dora-report/)的调查结果，它表明，虽然 AI 加速了价值交付，但组织通常会用更多的任务来填补新发现的能力。也许这很方便，但我们不要忽视服务器机房里的大象：Toil 早于 ChatGPT。

回想一下 2010 年代，当时*“*云迁移*”*意味着凌晨 2 点手动重启服务器。或者自动化时代之前的 Excel 骑师，无休止地更新电子表格。Toil 一直是一个变形者，在组织惯性中茁壮成长。

在指责 AI 之前，让我们检查一下 Toil 卷土重来的五个可信的非 AI 原因，以及你可以做些什么来解决它们。

## 1. “永远在线”的协作陷阱

现代工作是一个碎片化工具的马戏团。Slack 的 ping！Teams 警报！日历弹出窗口！我们花费数小时进行上下文切换，追逐审批或协调跨平台的冲突更新。理论上[自动化的东西在实践中变成了手动的](https://thenewstack.io/how-to-mature-your-devops-automation-practices/)——Toil 伪装成生产力。根据 [Asana 的工作剖析指数](https://www.inc.com/rebecca-deczynski/asana-anatomy-of-work-index-meetings-remote-work-efficiency.html)，员工花费近 60% 的时间在“关于工作的工作”上，只剩下 27% 的时间用于熟练工作，13% 的时间用于战略规划。

你可以做什么：

- **简化协作工具**：向“关于工作的工作”宣战。审计工具——你真的需要 14 个 Slack 频道来处理“紧急-紧急”的事情吗？强制执行“安静时间”以进行深度工作。
- **自动化协调**：如果 Jira 工单移动到“完成”，让 Zapier 告诉 Slack。人类有更好的事情要做。

## 2. “影子 IT”的兴起

团队经常在没有中央监督的情况下采用未经授权的工具和 SaaS 应用程序，导致需要手动数据传输和协调的孤立系统。市场部使用 Airtable。销售部信誓旦旦地使用 Notion。工程师们沉迷于 Coda。没有人说同一种语言。突然，你扮演着数据管理员的角色，像 1999 年那样复制粘贴。

更糟糕的是，其中一些工具不仅未经批准，甚至在它们引起破坏性的[手动]喧嚣之前，IT 部门都不知道它们。Software AG 的一项研究表明，一半的员工正在使用未经授权的 AI 工具，通常被称为“[影子 IT](https://thefutureofwork.pro/study-finds-half-of-employees-using-unauthorised-ai-tools/)。”

**你可以做什么**：

- **确保影子 IT 的阴影不是幻觉**：识别并评估当前使用的所有未经授权的应用程序，删除冗余工具。准备好找到实际上提供 IT 从未考虑过的价值的工具。
- **构建自助服务平台**：为团队提供预先批准和集成的解决方案，以减少流氓 SaaS 的采用。这具有平台工程的氛围——创建一个结构化的环境，团队可以在其中快速行动，而不会造成集成混乱。

## 3. 恐惧驱动的官僚主义蔓延

规避风险的组织会叠加审批、审计和文档，以减轻 IT DevOps 事件。现在，代码部署需要五个签名、一个手动日志和一个针对错别字修复的事后分析——Toil 伪装成治理。

**你可以做什么**：

- **将[互联网性能监控](https://www.catchpoint.com/internet-performance-monitoring)(IPM)嵌入到你的生命周期中**：全面了解外部依赖关系，在问题升级之前检测到问题，并更快地解决事件，从而减少对过度审批和手动监督的需求。
- **采用非责备的事后分析**：培养一种从事件中学习而不是分配责任的文化，从而简化流程。

## 4. 技术债务持续累积利息
许多组织仍然依赖过时的遗留基础设施，这与现代云原生工具产生了摩擦。这种不一致通常导致手动干预来弥合技术差距。

**你可以做什么**：

*   **优先考虑“绞杀榕”现代化改造**：逐步用微服务替换遗留组件，同时保持核心系统运行。
*   **建立卓越的监控中心**：根据您的组织在数字化转型或现代化曲线上的位置，您需要一个专注于监控或观察[最终用户体验](https://www.catchpoint.com/blog/mastering-ipm-monitor-what-matters-from-where-it-matters)的卓越中心，以在进行这些更改时最大限度地减少影响。
*   **投资于互操作性**：使用 API 或中间件（例如 MuleSoft）来桥接新旧系统，从而减少手动粘合工作。

## 5. “快速修复”文化
在交付即时结果的压力下，团队经常走捷径——选择手动变通方法而不是长期自动化。[Stripe](https://www.pullrequest.com/blog/cost-of-bad-code/#:~:text=A%20recent%20study%20from%20Stripe,code%20that's%20difficult%20to%20maintain.)的一项研究发现，开发人员大约花费 42% 的时间用于维护活动，从而降低了他们专注于创新的能力。

**你可以做什么**：

*   **激励可靠性**。设置团队和领导层[与可衡量的手动任务减少相关的目标](https://thenewstack.io/set-goals-and-measure-progress-for-effective-ai-deployment/)。
*   **分配“全班次”自动化冲刺**。与其争论“左移”或“右移”，不如采用“全班次”方法，将至少 10% 的工程周期用于自动化整个 CI/CD 生命周期中的手动任务。[全班次方法](https://thenewstack.io/monitoring-developer-metrics-team-approach-is-best/)迫使团队协同工作，协调整个管道中的工作，而不是在孤岛中进行优化。结果是一个作为一个整体变得更高效的系统，而不仅仅是改进单个部分。

## 人工智能是反派——还是只是一面镜子？
数据很清楚：辛苦工作正在增加。但为什么呢？人工智能是罪魁祸首，还是仅仅反映了我们多年来一直忽视的习惯——快速修复、官僚主义膨胀以及用数字胶带粘合在一起的遗留系统？

《2025 年 SRE 报告》并未解决这场争论。然而，它确实提醒我们，辛苦工作在模糊性中茁壮成长。人工智能是放大现有低效率还是创造全新的低效率，取决于我们如何运用它。纠正文化。无情地自动化。为了生产力，删除一半的 Slack 频道。

对于那些渴望更少的隐喻和更多数据的人，[下载完整报告。](https://resources.catchpoint.com/hubfs/Website%20Assets%20-%20Briefs%2c%20EBooks%2c%20etc/The%20SRE%20Report%202025%20Catchpoint.pdf?_gl=1*174s7pu*_gcl_au*MTcyMzc5MzIwMC4xNzM5NTUwMzk2)