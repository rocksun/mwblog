<!--
title:驯服老虎：平台团队的趣味指南
cover: https://cdn.thenewstack.io/media/2023/11/f2851fb0-tiger-5256833_1280-1024x682.jpg
-->

在扩展组织和引导平台团队发展的过程中，我们总结了一些宝贵的经验。这些教训往往源自过往的错误。

> 译自 [Tame the Tiger: A Lighthearted Guide to Platform Teams](https://thenewstack.io/tame-the-tiger-a-lighthearted-guide-to-platform-teams/)，作者 Ashwin Raghav 担任谷歌项目IDX的工程负责人。那些讨厌的Firebase API也是他的杰作。在谷歌、Twitter、Zynga、Thoughtworks 和 Intel,他已有20年软件和软件团队建设的经验。他自认是开发者工具专家,同时也常面临来自全球不快开发者的愤怒。他和妻子以及两个孩子生活在一起。

在成功产品和快速扩张的团队背后的宏伟蓝图中，有一个鲜为人知却至关重要的实体——难以捉摸的平台团队。

在我的职业生涯中，我领导过两个平台组织，我对我们社区给予精心规划平台团队这一[精细艺术](https://thenewstack.io/high-performing-devops-teams-build-self-service-platforms/)的稀少关注感到略微恼火。

由于其天生的性质，这些团队往往成为[产品和他们所服务的其他团队](https://thenewstack.io/why-you-should-run-your-platform-team-like-a-product-team/)的软肋。

你能诚实地说，你没有遇到过内部的平台团队欢快地要求你等到下一财年才解决你勤奋提交的错误报告吗？

在这篇文章中，我将分享我在谷歌、Firebase 和 Zynga 工作时对建立平台团队的经验和思考。我将重点关注从中吸取的教训——通常源自所犯的错误——这些教训讲述了如何扩展组织，以及如何应对[平台团队发展](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/)的复杂性。

## 什么是平台团队，为什么它们如此兴盛？

随着组织的发展壮大，领导者广泛追求效率提升，以适应日益增长的员工队伍。平台团队因为承诺提供一系列效率改进措施而[变得越来越重要](https://thenewstack.io/humanitec-the-golden-path-to-platform-engineering/):

- 减少产品团队之间的重复工作量(考虑诸如可观测性、数据库和存储、DevOps 和工程效率工具等核心服务);
- 促进招聘各种“繁琐技能”方面的专家(运营、移动开发、前端、数据科学、指标等);
- 战略性地标准化服务，使您无需操心这些琐事，从而更好地应对组织扩张和团队重组。

的确，平台团队的概念已经确立并形成了标准的组织架构，我们也已逐渐习惯。

然而，我们所珍视的效率改进措施往往也成为低效的罪魁祸首。我们已经学会了容忍它们，因为总的来说平台团队带来的好处仍然大于弊端。

但事实证明，我们可以做得更好。

## 外包成本的副作用

如果这篇文章要表达的至关重要观点只有一个，那就是：最大限度地[减少外部成本](https://thenewstack.io/factor-cost-efficiency-into-platform-engineering-for-growth-profitability/)是平台组织设计的关键所在。

什么是这些外部成本呢？

想象这样一种情况：一支[发布工程](https://thenewstack.io/setting-kubernetes-standards-with-platform-engineering/)(releng)团队负责指导和落实你们整个组织的重大产品发布。

问题在于，这一过程中不可避免地涉及到大量手工流程和法律风险。要想实现完全的自助发布流程，感觉就像要拆解一个戈尔迪之结一样困难。

于是，releng 团队选择了一条更简单的路径——发布列车。产品团队依次“乘坐”这列发布列车，等待他们的车票被“打孔”。

这样一来，产品团队就必须寄希望于发布流程的可靠性，精心规划自己的产品发布日期和配套的市场宣传。

但是最关键的问题在于，定制化的热补丁和应急发布就好比曲球，常常让产品团队措手不及。高高在上的发布团队不得不思考，“什么样的情况才‘值得’我们在周五的加班夜晚进行热补丁发布？”

由于发布成本相对于产品团队来说是外部的，那么谁在这个过程中扮演了反派的角色呢？没错，就是那些放慢发布流程、设定高不可攀的热补丁门槛的发布团队。

反过来看，如果一个生产环境的错误被忽视到下一次预定发布，所有相关的外部成本都会加诸到发布团队头上，这对他们极为不利。

解决方案是什么呢？保持发布进程的存在，但同时制定自助、文档完备的热修复流程。让每个产品团队自行决定值得在周末修补的错误，突然间，发布的成本和隐藏在办公室的零食储藏柜一样，成为内部事务。

### 退款：因为“谁付这笔钱？”不是开玩笑

随着组织规模的扩大，各个团队朝着自己的节奏运转。即使这感觉像是一次集体性的乡村舞会，但使各团队保持同步还是非常重要的。当在竞争团队的优先事项中进行选择开始像真人秀的淘汰过程一样时，你就知道是时候加强决策能力了。

创立一个平台团队时应该承诺会提供持续的支持。领导者必须在成立仪式之外继续支持平台团队的各种需求，片面抛弃他们是不可取的！

那制定明确决策的秘诀是什么呢？退款！对于那些固执地驻留在产品团队责任范围之外的各种成本，退款是你的黄金门票。我们这里不仅谈论通常意义上的可疑成本——计算、存储和指标团队提供的各种欠条。

我们需要跳出框框思考:

还记得之前 releng 团队的例子吗？ 用软件工程师的工作时间(一个奇特但有效的度量标准)来衡量每个发布流程所花费的时间。产品团队会追求成本效率，而发布团队的目标则是尽可能降低“发布列车”上的各产品团队的“票价”。

有人提出功能弃用吗？计划告别遗留版本支持的团队，可以对那些[过时平台继续提供支持](https://thenewstack.io/how-team-topologies-supports-platform-engineering/)这一服务进行收费。突然间，这就酿成了一场竞价战！

## 支持平台团队人才方面的需求

正如前文所述，建立平台团队的主要原因之一是成为某些细分领域专业知识的“磁石”。(运维、移动开发、前端、数据科学、指标——各个你能想到的领域。)

但是请谨慎行事，因为您即将踏入业绩校准的殿堂。

是时候调整你的业绩评估准则了。以往在关键领域展示专业知识就可以自动获得嘉奖，这种方案现在行不通了。 即使你是“安全大师”，这种头衔也不会自动使你的业绩评级水涨船高。请记住，像[每秒查询数这样的影响指标](https://thenewstack.io/navigating-the-high-concurrency-challenges-of-user-facing-analytics/)并不与产品团队的记分卡关联。

如果要集中某些专业人才，就要全力以赴。比如，不要一边维持一个核心的移动团队，一边将移动开发者[分散到不同的产品团队中](https://thenewstack.io/scaling-a-backstage-developer-portal-for-a-finserv-dev-team/)。

这样你最终会面临一场音乐椅游戏，不得不在不同团队中公平地为每个人规划发展机会，并评估那些工作性质毫不相关的不同岗位员工所带来的影响。

集中化并不是一劳永逸的解决方案。要根据产品的实际需求，明智地选择哪些功能要集中化。例如，集中UI设计师看似一个合理的举措，但是如果你的产品高度依赖品牌认同感，将设计师作为共享资源可能会激发设计理念的冲突。

## 有项目经理或无项目经理：这是一个问题

古老的争论：平台团队应该引入产品经理吗？我坚定地站在将您的产品视为美食佳肴、将消费者视为挑剔食客的一方——这需要产品管理。

平台产品经理的角色可能与常规有所不同，但团队化学反应和清晰的期望则是必不可少的。在这里担任产品经理不是为了实现宏伟的创造，而是组织管理、有系统的沟通和运营细节方面的协调。并非每一位产品经理都能胜任这场舞蹈。

尽管用TPM(总体产品维护)来替代产品经理的诱惑仍然存在，但像珍惜名贵的兰花一样培育您的平台服务会为所有人带来更好的果实。

还记得我们讨论的组织管理吗？如果产品团队中的产品经理是遵循主要业务指标和财务指标而行动的话，那么在优先级会议上拥有一位说同样语言的平台产品经理将是改变游戏规则。

我亲爱的读者们，到此我们来到压轴表演！衷心祝愿您的[平台团队](https://thenewstack.io/infrastructure-as-code-or-cloud-platforms-you-decide/)一切顺利——愿您的收费公平，发布像黄油一样顺滑！
