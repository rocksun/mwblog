<!--
title: Anyshift：构建上下文，加速智能事件响应
cover: https://cdn.thenewstack.io/media/2025/10/f9a162fb-anyshift.png
summary: 现代复杂IT环境使SRE事件响应困难。Anyshift的Annie利用基础设施图谱和AI助手提供上下文，加速根本原因分析，从而提高效率，减少SRE工作量。
-->

现代复杂IT环境使SRE事件响应困难。Anyshift的Annie利用基础设施图谱和AI助手提供上下文，加速根本原因分析，从而提高效率，减少SRE工作量。

> 译自：[How Anyshift Builds the Context for Faster, Smarter Incident Response](https://thenewstack.io/how-anyshift-builds-the-context-for-faster-smarter-incident-response/)
> 
> 作者：Meredith Shubel

大多数现代公司都拥有庞大的业务版图，包括国际团队以及由Kubernetes、CI/CD管道、基础设施即代码（IaC）和许多其他互联工具整合在一起的巨大多云架构。

这些像拼图一样复杂的环境使团队能够快速行动并进行全球部署——但这却让[网站可靠性工程师](https://thenewstack.io/practical-guidance-for-first-time-site-reliability-engineers/)（SRE）的事件响应工作变得异常头疼。

[Roxane Fischer](https://www.linkedin.com/in/roxane-fischer-92a52414b/)，[Anyshift](https://www.anyshift.io/sre-experts) 的首席执行官兼联合创始人，以及她的联合创始人兼首席技术官 [Stephane Jourdan](https://www.linkedin.com/in/stephanejourdan/) 决定创立 Anyshift 时，都敏锐地意识到了这一现实：“从公司成立的第一天起，我们就明白，目前该领域的一个大问题是基础设施中存在不同的孤岛……当出现问题时，尤其是在生产环境中，这些孤岛之间无法相互响应，这给工程师带来了困扰。”

她并非唯一持有这种观点的人。而且，所有这些孤岛似乎都可能影响事件响应时间。在[2023年对1000名IT运营](https://devops.com/it-service-incidents-are-becoming-more-frequent-survey-says/?utm_source=chatgpt.com)、[DevOps](https://thenewstack.io/multipass-fast-scriptable-ubuntu-vms-for-modern-devops/)、SRE和平台工程专业人员进行的调查中，62%的人表示过去一年解决事件所需的时间有所增加。

是什么拖慢了他们的速度？Fischer 表示，这是由于管理碎片化、庞大的基础设施所带来的混乱和缺乏上下文。

## 工具太多，上下文不足

许多组织同时管理着 [AWS](https://aws.amazon.com/?utm_content=inline+mention)、GCP和Azure的混合环境，以及Kubernetes集群、CI/CD管道、IaC工具等。虽然构建多云或混合基础设施在灵活性、速度和冗余方面具有明显优势，但这也意味着在事件响应和根本原因分析时需要梳理大量信息。

正如 Fischer 所说：“当客户出现延迟问题时，很难知道它究竟是来自Kubernetes集群中的混合配置，还是……某个变更导致了连锁反应。”

即使只是一个警报，也可能由十几个不同的因素触发，为SRE们制造了令人眩晕的“兔子洞”去追查——在被称为“作战室”的高压环境中工作时，这尤其混乱。

Fischer 将这种追查根本原因的“寻鹅游戏”称为行业内最大的痛点之一。她声称，目前使用的工具支持不足：“传统的监控工具会告诉你什么发生了变化，但不会告诉你为什么。它们不会提供问题的上下文。”

Anyshift 旨在提供这种上下文。

## 认识 Annie：SRE们通往根本原因“兔子洞”的捷径

这种上下文来自于一个持续更新的基础设施图谱和一个名为 Annie 的智能助手。

Anyshift 从多个来源摄取并组织数据，以创建公司基础设施和生产的实时地图，建立一个单一的事实来源，映射服务、云资源、配置和代码之间的关系。

当事件发生时，所有SRE团队只需标记 Annie，她便会开始调查问题。她将警报作为切入点，沿着从前端到后端的依赖路径，并查询来自Datadog或Grafana等集成工具的实时日志和指标。

“她的行为将与……一名SRE类似，”Fischer 宣称。“她会通过不同的调查路径，查询她需要的信息，最后在事件频道中创建一份[根本原因分析]报告。”

值得注意的是，Annie 不仅会呈现她的发现；她还会展示她的工作过程。

“她会以一种非常结构化的方式解释她是如何做到的，她去了哪里，以及她探索了哪些路径，”Fischer 补充道。这超越了许多 [AIOps](https://thenewstack.io/sre-report-retrospectives-have-aiops-predictions-held-up/) 或 AI SRE 工具的能力，这些工具通常会获取大量数据以浮现潜在的根本原因，但却不提供解释。

## 专家来来去去——但助手永不离线

阻碍事件响应的不仅仅是传统监控工具的不足。许多SRE团队的制度性质也带来了风险。

如果你与经验丰富的SRE合作，他们经历过类似问题并知道如何追踪问题而无需浪费大量时间，那么有些事件可以轻松解决。

但如果你的团队缺乏这种实战经验，那么即使是例行调查也可能突然变得更加费力。Fischer 说：“这有点像大海捞针。我如何通过这些不同的探索路径来尝试理解问题是如何产生的？”

当事情出错时，经验丰富的SRE通常是第一个被通知的人。虽然他们多年的经验看似是一种财富，但实际上却是一种可能很快导致灾难的负债。

“如果这些人离开了，那将是一场灾难，”Fischer 警告说。“如果他们不在，初级人员往往会感到非常迷茫，因为他们得不到信息。”

## 更多上下文 = 更快修复 + 更少杂务

然而，冗长的事件响应所带来的影响远不止浪费时间，尽管这是一个显著的缺点。根据一本[Google SRE手册](https://sre.google/sre-book/eliminating-toil/#:~:text=Quarterly%20surveys%20of%20Google's%20SREs,to%20find%20satisfying%20engineering%20projects.)的数据，“对Google SREs的季度调查显示，平均花费在杂务上的时间约为33%”，一些极端情况甚至声称杂务时间高达80%。

当然，成本是另一个令人担忧的副作用。根据 [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention) 的一项[调查](https://www.pagerduty.com/newsroom/study-cost-of-incidents/?utm_source=chatgpt.com)，平均每个事件需要175分钟解决，花费近794,000美元。

除了损失时间和金钱，冗长的事件响应还会让SREs脱离更高价值的工作，从而损害公司。Fischer 对此尤其关注，她表示 Anyshift 的主要关注点之一就是帮助SREs找回这些时间：

“我们如何真正帮助这些SRE，让他们不再忙于修复由过去的修改引起的事件，而是为这些待命工程师腾出一些时间，让他们专注于那些能够真正改进并为公司创造价值的任务？”

## 构建上下文驱动未来的地图

目前，Anyshift 专注于值班场景——Fischer 称之为要扑灭的第一个“火”。但未来，她设想这家初创公司的基础设施图谱将成为下一代AI SRE的基础，这些AI SRE不仅能响应事件，还能帮助团队持续改进和优化基础设施，以实现成本、延迟和可靠性方面的优化。

要实现这一目标，需要通过在基础设施图谱上叠加应用数据来增加更多上下文，从而映射整个生产系统。Fischer 认为，只有这样，Anyshift 才能实现其最终目标：“弥合开发者与DevOps团队之间、基础设施与应用世界之间的鸿沟。”

这种端到端的可观测性不仅能改善事件响应；还能消除跨团队事件响应中经常出现的相互指责。

对 Fischer 而言，一切都归结为一个问题：“你如何才能真正让整个系统变得更好？”

他们尚未完全实现，但如果AI SRE的未来是上下文驱动的，那么Anyshift无疑正在构建通往彼方的“地图”。