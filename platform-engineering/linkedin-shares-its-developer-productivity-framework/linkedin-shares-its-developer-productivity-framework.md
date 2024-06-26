<!--
title: 领英分享其开发者生产力框架
cover: https://cdn.thenewstack.io/media/2024/01/5adbd5b5-mimi-thian-vhq0cw2eua-unsplash-1024x768.jpg
-->

领英的新开源软件开发框架将硬数据与人文因素的重要性相融合。

> 译自 [LinkedIn Shares Its Developer Productivity Framework](https://thenewstack.io/linkedin-shares-its-developer-productivity-framework/)，作者 Mary Branscombe。

在远程工作、大规模离职潮、AI编码助手以及2023年科技行业[近25万人裁员的背景下](https://techcrunch.com/2023/12/15/tech-layoffs-2023-list/)，开发者生产力仍是一个棘手的话题。

寻找阻碍开发者、改善开发者体验以及确保开发者拥有正确的访问权限和工具来处理永无止境的积压工作的瓶颈和挫折感，所有这些努力都应该帮助企业和开发者实现双赢。今年，Atlassian 报告说，告诉其开发者将10%的时间用于“[改善让他们的日常工作感到糟糕的事情](https://www.atlassian.com/engineering/the-key-to-unlocking-developer-productivity)”，取得了良好的结果。

但是，衡量开发者生产力并不像听起来那么简单。做错了，它可能会感觉像是侵入式的密切监管，从而潜在地增加开发者的职业倦怠率，而职业倦怠率几乎没有从疫情高峰期下降。或者衡量过程最终被利用，甚至可能损害整体代码质量。

一些生产力问题，比如缓慢的开发基础设施或者规划足够强大的机器来运行要求苛刻的开发者工具，最好集中处理。关于发布速度、代码质量或协作的问题，可能需要针对具体团队来解决。但是您该如何找到阻碍开发者的因素，并检查改变事物的方式是否最终使他们变得更好呢？

LinkedIn 希望它刚开源的[开发者生产力与幸福(Developer Productivity and Happiness，DPH)框架](https://linkedin.github.io/dph-framework/)能对此有所帮助。该框架描述了LinkedIn用于建立其用于理解开发者、工程工作的成功(或失败)以及注意力应聚焦于何处(如其[开发者见解中心](https://engineering.linkedin.com/blog/2023/inside-look--measuring-developer-productivity-and-happiness-at-l))的系统的指导方针。

[Max Kanat-Alexander](https://www.linkedin.com/in/mkanat/) 是 LinkedIn 开发者生产力与幸福的技术主管之一，他向 The New Stack 解释了其工作方式。“当您与工程主管交谈时，他们常常会告诉您‘我真的想帮助人们提高生产力，但我不知道从哪里开始。我不知道问题出在哪里，也不知道我的投资会在哪里获得最大回报’。真正拥有数据和反馈可以让您做到这一点。”

Kanat-Alexander 之前是 Google 的代码健康状况的技术主管，在那之前是 Bugzilla 项目的首席架构师，所以他已经在开发者生产力领域工作了近20年。他告诉我们，近几年，软件行业对利用数据和反馈来提高开发者生产力和幸福感的兴趣显著增加。“关于数据和反馈的这整个课题真的已经蓬勃发展。”

## 找到您自己的指标

选择从[DORA](https://dora.dev/research/)(DevOps研究与评估研究小组)和[SPACE](https://queue.acm.org/detail.cfm？id=3454124)(GitHub和微软完成的工作，将DORA从最初的功能指标扩展到包括满意度和幸福感;表现;活动;沟通和协作以及效率和流程)等框架中跟踪指标列表的诱惑确实很大。DORA已经从最初的四个指标(部署频率、变更前导时间、变更失败率和服务恢复时间)扩展了非常多，而SPACE有一个可能的指标矩阵——但将这些指标视为菜单会是一个错误。

“大多数情况下，最有效和最成功的指标将非常具体于一个团队及其情况，”Kanat-Alexander警告道。

> “试图找到一组通用的指标模板在提高组织的生产力和真正使开发者的情况变得更好方面效果几乎总是很差。”

“人们需要的是一种定义自己指标的方法: 他们需要理解如何提出指标。”这就是DPH框架试图提供帮助的地方。

![放大](https://cdn.thenewstack.io/media/2024/01/202dda2b-image5-1024x570.png)

*图片来源:LinkedIn;LinkedIn的团队会追踪在整个公司中使用的指标组合以及一些针对特定团队的指标:DPH框架可作为找到您自己团队可能的指标的指南。*

DORA和SPACE等框架中的指标显然很有用，但它们可能过于宏观，您需要实现指标并收集其他数据才能使其对您自己的情况有用。

考虑端到端交付变更的时间，这看起来是一个不错的跟踪指标。“这可能显示了一个非常大型公司在非常宏观的层面上的变化。但是要了解驱动这些变化的因素，您需要更多的信息，而且还需要非常深入地理解开发者生产力。”即使有了所有这些信息，开发者所做的工作对最终指标的影响也可能并不明确，而一个更具体的指标可能会提供更多信息。

“您可能能够拥有另一个非常明确的指标，它显示了某些与您正在做的具体工作高度相关的改进，并真正展示了您的工作对业务的价值，同时也使您能够了解最大的痛点在哪里，这样您就知道自己正在尽可能做最有影响力的工作。”

同样，[代码审查的响应时间](https://linkedin.github.io/dph-framework/example-metrics.html#code-reviewer-response-time-rrt)也是一个有用的指标，它与代码更改的大小密切相关:“与大小的关系非常线性”，Kanat-Alexander指出;“随着更改变大，获取快速响应变得更加困难”。如果您决定跟踪复查响应时间以提高复查吞吐量，则可能需要按语言、框架或生态系统分拆指标，但更重要的是要知道您在优化什么以及为什么，因为鼓励较小的代码更改可以提高软件速度;这也是一个容易被操纵的指标。

“您必须拥有数据并查看数据，然后与开发者交谈并询问‘这是一个问题吗？缓慢的代码审查时间是一个您关心的问题吗？代码审查工具中是否存在今天的障碍？’如果您没有告诉我们这是一个问题，而我们为您提供了一个解决方案，您会欣赏它吗？您甚至会使用该解决方案吗？”

> “首先要从您的开发者那里了解他们认为存在什么问题，然后再检测该领域。”

尽管该框架[包括LinkedIn本身使用的一些指标的示例](https://linkedin.github.io/dph-framework/example-metrics.html)，但它们有意放在讨论的最后，讨论从用于选择这些指标的[目标-信号-指标](https://linkedin.github.io/dph-framework/goals-signals-metrics.html)方法开始。

“目标实际上是最重要的，而这些目标在组织结构图上下都是更容易保持一致的，因为您始终可以问为什么。对于任何目标，您可以说:这为什么是我的目标？如果您一直玩这个游戏，就像一个不停地说“为什么为什么为什么”的两岁小孩，最终您会达到公司的使命。”

对于组织和管理者来说，正确的指标可以帮助理解需要改变的地方，特别是在资源有限的情况下，他指出。“我们要做什么，什么最阻碍开发者，如果我只能指派有限的人来做这项工作，最有效的工作是什么？”

避免收集的数据无助于您做出决策的虚荣指标——毕竟，[收集数据的初衷就是为了做出决策](https://linkedin.github.io/dph-framework/driving-decisions.html)。组织必须愿意利用这些指标进行系统性变革，而不是试图将其用于个人绩效评估。“您必须始终拥有您愿意变差的指标，因为那时您会发现问题，而且指标也才会有效，”Kanat-Alexander指出。

> “坏消息的大好消息是它提供了您最佳的机会。这是您可以改变和采取行动的事情。”

## 开心的开发者，盈利的业务

框架不仅讨论生产力，您不应对此感到惊讶。“开心是一个非常重要的信号，领导者需要关注。人们有时会认为这是某种温情脉脉的东西，您想让人们开心，而他们会说‘我不需要员工开心。我只需要员工工作。’如果[您研究一下](https://www.microsoft.com/en-us/research/uploads/prod/2019/04/devtime-preprint-TSE19.pdf)，[很难区分生产力和幸福感](https://research.google/pubs/what-predicts-software-developers-productivity/)。它们[息息相关](https://queue.acm.org/detail.cfm?id=3595878)。”

“问题从来不是‘我自己如何编码得更快？’而是我们作为一个团队，一个组织或一个业务，应该以我们所能达到的最高质量，并尽可能快速地前进，同时让每个人都开心。因为开心的人更有生产力，有生产力的人更开心，开心的人会创造更好的产品。“

> “几乎所有人都感觉更好意味着公司更有效地实现其目标。”

将幸福感和生产力放在一起思考也有助于解决将抽象指标与阻碍开发者生产力的问题相联系的问题，他建议。

“很多时候您会发现，某人认为某项指标代表生产力，但开发者并不认为做那件事代表他们的生产力、影响力或创造价值。幸福感给了您这样的洞察力:‘嘿，你漏掉了什么’;也许您在衡量错误的东西。’ 很多时候，幸福感信号实际上是一个比定量生产力信号更广泛和全面的信号。”

人性因素很重要，因为软件工程，特别是在大型组织中，最好把它看作是一项团队运动;开发者遇到的问题既是人际问题也是技术问题。这可能是团队目标不明确，或者组织结构不高效。“也许他们参与了大量的调整会议，或者没有明确的计划过程;这最终会占用大量本可用于软件开发的时间。”

无论您是否认为现在每家公司都已经是软件公司，您可能会发现糟糕的开发者生产力实际上暴露了组织更深层次的问题。“理论上，这些数据绝对可以帮助您做出更明智的决定，以便使组织更加关注。”

但该框架也鼓励每个人都要实事求是。如果有人告诉你拥有这些数据实际上不会对他们的行为产生任何影响，那么你就知道这个指标不值得收集，分析也不值得进行。
