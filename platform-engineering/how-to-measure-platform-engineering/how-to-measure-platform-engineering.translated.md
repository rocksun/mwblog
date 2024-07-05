# 如何衡量平台工程
![平台工程衡量方法的特色图片](https://cdn.thenewstack.io/media/2024/07/41800c9f-measuring123-1024x576.jpg)
虽然开发者倦怠一直是[平台工程](https://thenewstack.io/platform-engineering/) 的主要推动力，但采用这种方法还有许多其他原因。您用来跟踪内部开发者平台成功的方法必须进行调整，以考虑对创建平台进行时间和预算投资的不同动机。

有效地[衡量平台工程](https://thenewstack.io/platform-engineering/) 在保护其开发的长期投资方面更为关键。作为一个行业，如果利益相关者没有看到持续资金的好处，我们可能会面临大规模的平台放弃。

鉴于许多不同的动机，您如何衡量平台工程？这就是[MONK 指标](https://octopus.com/devops/metrics/monk-metrics/) 的用武之地。

## 什么是 MONK 指标？
MONK 是四个项目的首字母缩写：

- 市场份额
- 入职时间
- 净推荐值 (NPS)
- 关键客户指标
MONK 指标中的三个是具体的，而第四个——关键客户指标——则更加抽象。这就是衡量方法灵活地适应平台引入的不同技术和商业原因的方式。

## MONK 中的 M：市场份额
市场份额是一个内部采用指标。该指标通过三个有形的数字来理解：

**开发者**: 您组织中的开发者数量**潜在用户**: 他们中有多少人使用平台辅助的技术**用户**: 在这第二组中，有多少人实际上正在使用平台
平台的采用可以通过用户数量与潜在用户数量的比率来评估。您可以将其表示为百分比，但绝对数字通常更重要。

![添加黄金路径后，潜在用户群体扩大。随着用户采用平台，市场份额增加。](https://cdn.thenewstack.io/media/2024/07/3d6e46bd-example-1024x588.png)
添加黄金路径后，潜在用户群体扩大。随着用户采用平台，市场份额增加。（来源：Octopus）

在考虑平台的新功能创意时，更改对采用（用户数量）和相关性（潜在用户数量）的影响可以为您的决策提供信息。新的[黄金路径](https://octopus.com/blog/paved-versus-golden-paths-platform-engineering/) 会导致更多开发者选择使用平台吗？

平台的价值因用户数量而放大，因此市场份额是所有平台工程计划的有用衡量指标。

## MONK 中的 O：入职时间
入职时间可以用两种方式表示：

- 开发者设置其开发环境、提交第一个更改并将其投入生产所需的时间。
- 团队引入[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) 元素所需的时间。
虽然您可能在考虑入职时间时会想到新开发者，但当[开发者转到不同的团队](https://thenewstack.io/engprod-the-secret-of-elite-developer-teams/)、接手他们一段时间没有使用过的应用程序或更换笔记本电脑时，它也很相关。

平台入职时间通常反映在市场份额指标中，因为困难或冗长的流程通常意味着团队没有时间完成它。您可以关注入职痛点的問題，看看简化流程是否会提高采用率。

为了收集开发者入职时间，您应该在开发者开始处理新的代码库时启动计时器，并在他们的第一个提交进入生产时停止计时器。如果您的内部开发者[平台解决了开发者工具链周围的常见问题](https://thenewstack.io/devops-toolchains-beat-off-the-shelf-platforms/) 和部署管道，新团队成员应该能够快速将他们的第一个小更改投入生产。

入职时间指标的目标不仅仅是加快第一次更改。它是所有平台工程团队共享的许多问题的有用衡量指标。它反映了开发者文档的质量以及[开发者集成其更改后提供的自动化程度](https://thenewstack.io/cloud-management-platforms-need-robust-automated-integration/)。

## MONK 中的 N：净推荐值
净推荐值 (NPS) 是财富 1000 强中三分之二公司使用的营销指标，软件即服务公司的预期得分在 30 到 40 之间。

要计算 NPS，您需要收集对以下问题的样本响应，该问题使用从 0（极不可能推荐）到 10（肯定会推荐）的量表进行回答：

> 您有多大可能向您的同事推荐我们的内部开发者平台？
*How likely are you to recommend the internal development platform to other developers?*

Group responses based on the score given. Those who answer with a score below 7 are considered "Detractors," while those who answer with a score of 9 or higher are considered "Promoters." Your NPS is the percentage of Promoters minus the percentage of Detractors.

This metric is better suited as a trend rather than a score. You should occasionally check in with users to see if their satisfaction with the platform is increasing or decreasing over time. It is crucial that you allow users to provide a reason for their score so that you can find out why they are happy (or frustrated).

While NPS is far from perfect, anyone who develops software products will understand the benefit of a user-provided satisfaction metric. The reasons users give for their rating can be eye-opening and will inform your future direction. NPS is never a replacement for regular conversations with your users.

## The K in MONK
After three concrete metrics that are widely applicable to platform engineering teams, the last metric is abstract. This metric should reflect the business and technical motivations for introducing platform engineering.

For example, if the team is not spending enough time on feature development due to the burden of managing deployment pipelines and infrastructure, then a key customer metric would be the percentage of time spent on new feature development. Or, if the platform is seen as a way to improve developer satisfaction, you could use [developer experience metrics](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/) as a key customer metric.

Many organizations have multiple reasons for adopting platform engineering, so multiple metrics may be needed. In some cases, simply demonstrating how the platform brings standardization may be sufficient.

## DORA Metrics for Platform Engineering
You can't talk about platform engineering metrics without mentioning DORA metrics. DORA metrics measure software delivery performance using deployment frequency, lead time for changes, change failure rate, and time to restore service after a deployment failure.

If you've created a platform to help developers improve their software delivery performance, then DORA metrics are very useful as a key customer metric (the K in MONK). You would measure the DORA metrics of the stream-aligned teams to demonstrate the impact of the platform.

Additionally, if your platform team is delivering software, it's also useful for them to track their own DORA metrics so they can use them to guide process improvements. Developers using the platform will appreciate the regular delivery of value, just like external customers.

While you can't judge an entire platform engineering initiative solely on DORA metrics, they do play a role.

## Why MONK Works
MONK metrics work because they blend concrete metrics common in the platform engineering industry with contextual success metrics that align with the reasons why the platform is considered a worthwhile investment.

A strong set of metrics is crucial for the long-term investment in a platform. Without a clear understanding of its value, developers are likely to eventually be reassigned to feature development at some point in the future.

Designing your key customer metrics also helps to articulate the vision for the platform, which can guide your choices about which features to introduce and which ideas are unlikely to help achieve the platform's goals.

There is always a trade-off between the practicality of specific metrics and the contextual nature or reality within a metrics framework. MONK metrics leverage the best of both.

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don't miss a beat. Subscribe to our YouTube
channel to watch all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)