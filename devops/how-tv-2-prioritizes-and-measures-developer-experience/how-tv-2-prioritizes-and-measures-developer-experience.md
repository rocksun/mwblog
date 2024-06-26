
<!--
title: TV 2如何优先考虑和衡量开发者体验
cover: https://cdn.thenewstack.io/media/2024/03/f0577183-emma-dahl-jeppesen.jpeg
-->

了解丹麦最大的媒体科技公司如何从专注于 DevOps 转变为专注于改善和衡量开发者体验。

> 译自 [How TV 2 Prioritizes and Measures Developer Experience](https://thenewstack.io/how-tv-2-prioritizes-and-measures-developer-experience/)，作者 Jennifer Riggins。

伦敦 — 如果你正在阅读本文，你可能从未听说过 TV 2。除非你是丹麦 85% 的人口中的一员，他们每天花一个小时十分钟来消费丹麦最大的国有商业资助广播网络的内容。

与所有历史悠久的电信公司一样，TV 2 从 80 年代的 [流动电视](https://en.wikipedia.org/wiki/Flow_(television)) 发展到流媒体服务和免费应用程序。这是另一家 [偶然的科技公司](https://thenewstack.io/finally-platform-engineering-for-enterprise-cloud-migration/)，但无论如何它都是一家科技公司。这意味着这家媒体科技公司不仅必须弄清楚如何采用现代的 [云原生技术](https://thenewstack.io/cloud-native/) 和 [DevOps](https://thenewstack.io/devops/) 理念，还必须弄清楚如何将开发者视为其客户。

对于 [Emma Dahl Jeppesen](https://www.linkedin.com/in/emmadj/) 来说，她在过去几年的产品经理角色已经从领导一个 DevOps 团队（该团队意外地给开发者增加了更多压力）演变为一个开发者体验团队，该团队研究并构建自助工具和一个新的可观测性平台，所有这些都专注于减少开发者的认知负荷。

Dahl Jeppesen 的团队处于技术和业务之间的关键边界，上周她在 Eficode 的 DevOps 大会上以及在随后的对 The New Stack 的采访中对此进行了反思。继续阅读，了解她的团队如何制定假设，然后测试和衡量其影响，以改善 TV 2 的开发者体验。

### 不仅仅是技术必须进化

“我们一直被称为媒体公司。现在我们是一家媒体科技公司，因为流动电视正在逐渐消亡，”Dahl Jeppesen 在 DevOps 大会上的炉边谈话中说道。当一家国有公司突然意识到 Netflix 是其最强大的竞争对手时，它该怎么办？“现在，这是一个完全不同的策略，让业务发挥作用，并调整业务以确保其在 2024 年仍然具有相关性。”

TV 2 与许多组织一样，从重组和重新关注采用新的云技术和 DevOps 开始。这导致整个工程组织迅速增长了约 350%，从大约 100 名工程师增加到现在的 450 名工程师。

然而，Dahl Jeppesen 说，这种数字化转型始于 DevOps 团队创建工具，他们会将这些工具交给站点可靠性工程师 [SRE]，“就像，‘给你！现在你可以随意使用它们了。’这带来了很多认知负荷。我们现在正试图做一些稍微不同的事情。”

她呼应了 [公司文化](https://thenewstack.io/tech-culture/) 转变的一个并不罕见的原因——异常高的离职率。“我们只是那个拥有太多工具、太多服务和遗留环境的 DevOps 团队。我们有很大的认知负荷。所以，在某个时候，他们都辞职了，团队解散了。”因此，她和剩下的那名工程师从 DevOps 转型为开发者体验团队。

对于 Dahl Jeppesen 来说，开发者体验就是“关于开发者如何看待他们的工作。这是关于他们在工作时感觉有多么高效。”她继续说道，“我认为，从 DevOps 中，我们了解了速度和质量反馈循环，但这将它提升到了一个全新的水平。它增加了其他东西，比如流状态——开发者在多大程度上能够在他们的工作中保持流状态？同样重要的是认知负荷，比如他们在工作时有多少认知负荷？”

她接着说，开发者体验——有时称为 DevEx——还关乎“尝试采用一些非常复杂的东西，比如工具，然后将其包装成一些美好的东西，考虑用户体验，并将他们 [开发者] 视为你的用户。”

这包括抽象和 [平台工程](https://thenewstack.io/platform-engineering/) 理念，在 TV 2 中，这是通过命令行界面和内部开发者平台实现的。他们还与许多 Kubernetes 和 Jenkins 合作，以实现持续集成。但几乎每个团队都有自己的堆栈。Dahl Jeppesen 评论说，这种拥有七条不同构建线和 Kubernetes 集群的庞大工具格局对业务不利，而且它使得难以汇总有关开发者体验的数据。现在，他们正在采用 [平台工程理念](https://thenewstack.io/platform-engineering-demands-a-product-mindset/)，在顶部使用命令行界面抽象，并通过 API 访问。

在过去的两个月中，所有工程师及其支持团队也开始在尝试[团队拓扑结构](https://thenewstack.io/how-team-topologies-supports-platform-engineering/)，这是一种组织团队能力的方式，每个人都围绕大约 15 个应用程序或流对齐，开发人员体验团队为整个组织和域级别的抽象服务。

在这些变化中，只要 [可观测性和监控](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) 到位，开发人员始终能够在他们想要的时候推送到生产环境。

### 如何衡量开发人员体验

随着 DevEx 团队发展到包括 Dahl Jeppesen 和四名工程师为 200 名工程师服务，他们了解和 [衡量开发人员体验](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/) 的工作已经扩展。

Dahl Jeppesen 说：“我们从 [DORA 指标](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) 开始，就像许多其他公司一样”，但他们在一年半后关闭了该仪表板，“因为团队感觉自己正在被衡量”。她说，开发人员正在玩弄这些指标，这意味着许多自称“精英”的团队实际上并非如此。[DORA 指标](https://thenewstack.io/despite-the-hype-engineers-not-impressed-with-dora-metrics/) 已由高管自上而下引入 TV 2，她指出，这些高管可能读过《加速》一书的一部分，但没有将指标与行动联系起来。

现在，她的团队正在努力实施 [DevEx 指标](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/)——专注于衡量流程状态、反馈循环和认知负荷——同时努力透明地了解他们衡量的内容以及原因。[开发人员调查](https://thenewstack.io/developer-productivity-in-2024-new-metrics-more-genai/) 已成为开发人员的一种低成本方法。

> “与你的开发人员交谈。了解他们。因为他们会告诉你他们讨厌的一切和他们喜欢的一切。”
>   ——Emma Dahl Jeppesen, TV 2

但她表示，虽然开发人员很容易填写这些调查，“老实说，调查设计真的非常困难”，但“我认为做一些事情总比什么都不做要好——询问你的开发人员他们对事物的体验”。

他们的调查工作始于询问开发人员对工具的看法，这揭示了 TV 2 工程师已经非常喜欢 GitHub Actions，这表明他们应该远离 Jenkins 而转向首选的 CI 流水线。

Jeppesen 建议：“与你的开发人员交谈。了解他们。因为他们会告诉你他们讨厌的一切和他们喜欢的一切。”以前，“我们采取了‘构建它，他们就会来’的方法，但这根本不起作用。因为你需要将开发人员视为用户。”

一旦你了解了他们的问题，开发人员体验和平台工程团队就更有能力解决这些问题。这就是她也不否认饮水机聊天可以了解他们真正想法的力量的原因。

TV 2 已采用 [目标和关键结果 (OKR)](https://thenewstack.io/a-guide-to-okrs-and-overcoming-the-pain-of-them/) 来协调工程组织。她的团队的目标是标准化他们的持续集成管道，而支持这一目标的一个关键结果是让三名开发人员加入并支持它。

她不仅表示大约 85% 的开发人员完成了他们的季度调查，而且他们的工程师保留率也有所提高。

![](https://cdn.thenewstack.io/media/2024/03/a674402b-developer-bottleneck-explained.gif)

### 规划开发人员旅程

当然，调查是一种非常主观的方式来衡量开发人员体验，这就是为什么 Dahl Jeppesen 的团队将它与系统数据（如遥测）结合起来，以平衡她所说的“说数据”（开发人员所说的内容）与“做数据”（实际发生的事情）。然后，除了这种定性和定量数据的组合之外，她还进行定性访谈，以规划开发人员的旅程，从构思到生产。

![](https://cdn.thenewstack.io/media/2024/03/e46b9b83-tv2-developer-journey-1024x722.jpg)

它帮助 TV 2 DevEx 团队了解他们可以在哪里整合反馈并优化体验。 Jeppesen 说，在这些较小的会议中，他们不仅询问步骤，还询问工程师在每个步骤中的感受，比如“这里的痛苦和收获是什么？他们会告诉你挫折或真正好的事情。”

最终，他们到达了可以将“现状旅程”与“未来旅程”的可视化曲线的位置，其中可观测性信号和其他渐进式改进可以应用于低点。然后她的团队问：“这是否提升了你的旅程？这是否真的改善了你的情况？”她继续说道。“那么，你又有了切实改善开发人员旅程中开发人员体验的可衡量方式。”

这些修复不需要是成熟的想法，而是她的团队将发布一个简单的原型，甚至是一个 [模型，以向开发者展示](https://thenewstack.io/mvp-or-tvp-why-your-internal-developer-platform-needs-both/)。开发者感觉能够做同样的事情，构思解决他们自己问题的方法。

在 CLI 的情况下，三位工程师兴奋地在白板上画出了他们的想法，但这并没有传达给他们的产品负责人。然后他们创建了一个 GIF，解释了他们希望自己的平台抽象是什么样的。她向其他一些开发者展示了它，他们很快对如何解决一个重大的开发者瓶颈有了共同的理解，因此他们构建了一些东西来验证它。

“不要在实际验证之前花费太多时间，”Dahl Jeppesen 强调说，“只需尝试一些东西，并将开发者视为用户。”

他们不仅衡量技术开发者体验，还衡量人员和流程的影响。她给 The New Stack 举了一个例子，“如果我们衡量流程状态，我们发现最大的问题是他们困在会议中，或者他们使用的敏捷框架对他们不起作用。”

毫不奇怪，出现的一个阻碍开发者流程状态的障碍是会议太多。她没有构建任何东西，而是有一个非技术性的但仍然非常有效的行动项目，即就此事向敏捷教练和领导提供建议，因为他们可以最好地影响会议文化。

Dahl Jeppesen 还提供了 [优先考虑开发者体验的四个步骤](https://www.linkedin.com/pulse/prioritizing-devex-core-successful-platform-emma-dahl-jeppesen-rv6ve/)：

**1. 了解你的用户。** 拥抱饮水机，开始一个免费加入的每周聚会，保持好奇心。

**2. 向公司的 UX 团队学习。** “DevEx 和 UX 实际上是同一件事，”她认为，主张采用 [双钻石](https://thefountaininstitute.com/blog/what-is-the-double-diamond-design-process) 的 UX 方法——发现、定义、开发和交付——并在探索模式中考虑有价值、可用、可行和可行的因素。

**3. 确保你的团队以用户为中心。** 这意味着在你的产品团队和你的内部开发者客户之间开发一个具体且共享的词汇表。她还建议对他们进行以用户为中心的方法的培训，并采用假设驱动的开发。

**4. 衡量你的用户的价值和体验。** Jeppesen 强调，这是最难的一步，但你真的无法改进你无法衡量的东西。如果开发者有指标来衡量其应用程序的成功，那么 DevEx 团队也应该有。她建议从小处着手，比如从你的平台或工具的采用率入手，并确保进行定性和定量测量。
