# Argo 项目如何避免 WordPress 式的问题

![Argo 项目如何避免 WordPress 式问题的专题图片](https://cdn.thenewstack.io/media/2024/10/e62150b5-argo-1024x576.png)

对于开源软件来说，今年是充满挑战的一年，[Terraform](https://thenewstack.io/with-ibms-open-source-roots-terraform-could-be-free-again/) 和 [Redis](https://thenewstack.io/redis-users-want-a-change/) 都在更新其许可证，从开源转向一种“公平源代码”([fair source](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/)) 的风格，旨在保护其各自创建者的商业模式。

现在，[Automattic 和 WP Engine 之间的战争](https://thenewstack.io/the-wordpress-saga-does-matt-mullenwegg-wants-a-fork-or-not/) 正在升温，导致数千名用户无法获得更新，并给用户带来了不确定性。我不会评论这两者之间谁是谁非。这最终是一场商标纠纷，已经公开化了。

但这仅仅是商标纠纷而已。

关于从 [开源](https://thenewstack.io/open-source/) 中获利的个人如何进行公平贡献，有很多争论。这些是道德上的争论，我对此表示同情，但它们不是法律上的争论。当你将软件开源时，你就设定了它的使用规则，据我所知，没有任何主流许可证要求从开源软件中获利的人必须做出相应的贡献。

## 为什么 Argo 项目是开源的

当 Intuit 创建 Argo 时（[它在 Argo 项目网站上](https://argoproj.github.io/)），它押下了一个巨大的赌注，即 Argo 是服务于关键业务功能的最佳方式。它的创建者知道，让 Argo 成为一个成功项目的最佳机会是确保有企业有强烈的动机来维护和扩展该项目。

结果呢？Intuit 邀请 [Codefresh](https://codefresh.io/)（现为 [Octopus Deploy](https://octopus.com/) 的一部分）成为第一个项目维护者，在 Argo 项目的基础上建立商业模式。几个月后，红帽加入成为第二个商业供应商，18 个月后，Akuity 加入成为第三个商业供应商。

所有这三个商业维护者，[Codefresh](https://codefresh.io/?utm_content=inline+mention)、[红帽](https://www.openshift.com/try?utm_content=inline+mention) 和 [Akuity](https://akuity.io/?utm_content=inline+mention)，都决定以某种方式投资 Argo 项目，所有公司都有全职维护者，并 [在各个层面做出贡献](https://insights.lfx.linuxfoundation.org/foundation/cncf/overview?project=argo&repository=https:%2F%2Fgithub.com%2Fargoproj%2Fargo-cd&dateFilters=Last%2012%20Months&dateRange=2023-09-28%20to%202024-09-27&compare=PP&granularity=month&hideBots=true)。我不能代表红帽或 Akuity 发言，但我们在 Octopus 这样做是因为 Argo 是我们业务的核心，也是我们为用户创造价值的核心。我们在安全贡献方面投入巨资，因为我们的用户希望获得安全保障。我们在错误修复和功能贡献方面投入巨资，因为我们的 [企业用户](https://codefresh.io/enterprise-argo-support/) 依赖于此。

但需要明确的是，Argo 许可证中没有任何条款要求我们或任何其他公司为 Argo 项目做出贡献或支付费用。这是开源软件。它是 [免费的，就像言论自由一样，也像啤酒一样免费](https://www.howtogeek.com/31717/what-do-the-phrases-free-speech-vs.-free-beer-really-mean/)。

在这个公司转向更具限制性的许可证并通过商标获取价值的时代，我们并没有改变我们的立场。当其他公司贡献少而索取多的时候，我们会感到沮丧吗？当然。更糟糕的是，我还看到其他公司试图将 Argo 货币化，而这些公司根本没有为该项目做出任何贡献。但这违反了我们用来分发 Argo 的 Apache 许可证吗？没有。

当 Intuit 的 Argo 创始人之一 Ed Lee [添加 Apache 许可证](https://github.com/argoproj/argo-cd/commits/master/LICENSE) 时，我们支持继续使用该许可证，因为我们相信开源的力量足以抵御不良行为者和机会主义者。如果我们投资于社区，他们也愿意投资于我们。

我为我们与 [云原生计算基金会 (CNCF)](https://cncf.io/?utm_content=inline+mention)、Intuit 以及其他 Argo 商业供应商建立的合作伙伴关系感到自豪。
这种合作之所以至关重要，是因为 Argo 项目由 Intuit 和 Black Rock 等最终用户公司以及 Codefresh、RedHat、Akuity 和最近的 Pipekit 等供应商共同维护，其商标由 CNCF 信托持有。由于这种权力平衡，任何一家公司都不可能独揽大权并更改许可证。事实上，我们的治理制度防止任何人对重大问题或冲突拥有 [超过 40% 的投票权](https://github.com/argoproj/argoproj/blob/main/community/GOVERNANCE.md)。

在 Codefresh，我们在 Argo 的安全性、用户体验、可靠性和可扩展性方面投入巨资。我们这样做不仅仅是因为这是正确的做法，还因为我们相信这是为选择我们 [GitOps 平台](https://codefresh.io/product/gitops/) 作为其技术堆栈或使用我们的专家支持其 Argo 部署的客户提供服务的最佳方式。

当道德和经济激励一致时，成功的开源项目和企业才能运作起来。我希望 WordPress 社区能够从中恢复过来，并且用户在斗争持续期间不会遭受太长时间的痛苦。

[技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等内容。](https://youtube.com/thenewstack?sub_confirmation=1)