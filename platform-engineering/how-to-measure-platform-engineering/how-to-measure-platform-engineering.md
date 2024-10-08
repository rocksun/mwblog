
<!--
title: 如何衡量平台工程
cover: https://cdn.thenewstack.io/media/2024/07/41800c9f-measuring123.jpg
-->

虽然开发者倦怠一直是[平台工程](https://thenewstack.io/platform-engineering/) 的主要推动力，但采用这种方法还有许多其他原因。您用来跟踪内部开发者平台成功的方法必须进行调整，以考虑对创建平台进行时间和预算投资的不同动机。

> 译自 [How To Measure Platform Engineering](https://thenewstack.io/how-to-measure-platform-engineering/)，作者 Steve Fenton。

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

*添加黄金路径后，潜在用户群体扩大。随着用户采用平台，市场份额增加。（来源：Octopus）*

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

根据获得的分数对答复进行分组。回答中分数低于 7 分的为“反对者”，回答中分数为 9 分或 9 分以上的为“支持者”。您的 NPS 为支持者比例减去反对者比例得到的百分比。

此项指标用作趋势比用作分数更有用。您应偶尔向用户了解一下他们是否对该平台越来越满意或越来越不满意。至关重要的是，您应允许用户说明其得分的理由，以便您找出他们感到高兴（或不满）的原因。

虽然 NPS 远非完美，但任何正在开发软件产品的人都将了解用户提供的满意度指示的好处。导致用户打分的理由可能会令人大开眼界，并会指导您的未来方向。NPS 决不会取代与您用户的定期对话。

## MONK 中的 K

在适用于平台工程团队的三个具体措施之后，最后一个指标是抽象的。此指标应当反映引入平台工程的业务和技术动机。

例如，如果由于管理部署管道和基础设施而导致的负担，导致团队无法在功能开发上投入足够的时间，则关键的客户指标将是花在新的功能开发上的时间所占的比例。或者，如果平台被视为改善开发者满意度的一种方式，则可用开发者体验指标作为关键的客户指标。

许多组织采用平台工程有多个理由，因此可能需要多个指标。在某些情况下，平台如何带来标准化的简单演示可能已足够。

## 平台工程的 DORA 指标

在没有 DORA 指标这一主题的情况下，您无法讨论平台工程指标。DORA 指标使用部署频率、变更前置时间、变更失败率和故障部署后的恢复时间来衡量软件交付绩效。

如果您创建了一个平台来使开发人员能够提高其软件交付绩效，那么 DORA 指标将非常有用，可用作主要客户指标（MONK 中的 K）。您将衡量与流对齐的团队的 DORA 指标，以展示平台的影响。

此外，如果你的平台团队正在交付软件，那么让他们跟踪自己的 DORA 指标非常有帮助，这样他们就可以使用这些指标来通知他们的改进流程。与外部客户一样，平台的开发者也会喜欢定期交付价值。

虽然不能单独根据 DORA 指标来判断整个平台工程计划，但它们肯定有其作用。

## 为何 MONK 运作

MONK 度量标准之所以有效，是因为它们将平台工程行业中常见的具体度量标准与与将平台视为值得投资的首要原因相一致的上下文成功度量标准相结合。

一套强有力的度量标准对平台的长期投资至关重要。 如果对其价值没有清晰的了解，那么很有可能开发人员最终将在未来的某个时候被重新分配到功能开发中。 

设计您的关键客户指标还有助于描述平台愿景，这可以指导您选择要引入哪些功能以及哪些想法不太可能有助于实现平台目标。 

在特定度量标准的有用性与上下文性质或现实性之间总是存在权衡。 MONK 度量标准利用了两者的优势。