
<!--
title: AI生成代码缺失了什么？重构
cover: https://cdn.thenewstack.io/media/2025/03/d7790286-refactoring1.jpg
summary: AI代码生成提速，但GitClear报告揭示重构骤降，代码重复激增！开发者需警惕AI Copilot带来的“生产力陷阱”，避免牺牲代码质量。拥抱AI提效同时，别忘了重构等软件工程基础实践，否则将面临软件危机！
-->

AI代码生成提速，但GitClear报告揭示重构骤降，代码重复激增！开发者需警惕AI Copilot带来的“生产力陷阱”，避免牺牲代码质量。拥抱AI提效同时，别忘了重构等软件工程基础实践，否则将面临软件危机！

> 译自：[What’s Missing With AI-Generated Code? Refactoring](https://thenewstack.io/whats-missing-with-ai-generated-code-refactoring/)
> 
> 作者：Steve Fenton

上个月，GitClear 发布了一份关于 2.11 亿行代码的分析报告，即[《AI Copilot 代码质量报告》](https://gitclear-public.s3.us-west-2.amazonaws.com/AI-Copilot-Code-Quality-2025.pdf)。其中一个关键发现是[重构信号](https://thenewstack.io/is-this-the-end-of-data-refactoring/)正在崩溃，而代码重复和变更正在增加。事实上，2024 年是引入重复代码的次数大于重构活动次数的第一年。

这一趋势归因于[AI 编码助手](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/)的兴起，如果这种情况持续下去，我们可能会走向软件危机。

## 采用 AI 的竞赛

如果你从事软件开发工作，肯定有人告诉过你“AI 不会取代开发人员；使用 AI 的开发人员会取代不使用 AI 的开发人员。” 这句话传达的信息很明确：要么使用 AI，要么准备转行。更积极的说法是，我们可以消除繁琐的工作——那些需要高度重复且无需思考的任务。

最近的 [Stack Overflow 开发者现状调查](https://survey.stackoverflow.co/2024/ai) 发现，超过 60% 的开发人员现在正在使用 AI 作为其工作的一部分，并且有更多的人计划这样做。采用 AI 的主要动机是提高生产力。正如 GitClear 报告显示的那样，想要提高生产力的一个巨大缺点是，你可能会为了更快地踩踏板而拆掉自行车的链条。

就软件开发而言，我们现在正在迅速加快代码库的变化速度。预计 2025 年的变化速度几乎是 AI 出现之前（2021 年）的两倍。

![Lines of code changed: The accelerating rate of change, including the predicted 2025 total. Image from Octopus Deploy. Data source: , GitClear](https://cdn.thenewstack.io/media/2025/03/502debee-image1-1024x682.png)

*变化速度加快，包括预计的 2025 年总数。图片来自 Octopus Deploy。数据来源：GitClear。*

许多人，尤其是那些销售 AI 的人，可能认为生产力的飞跃是个好消息。但是，我们应该记住我们前辈的智慧。[生产力对知识工作的看法很差](https://thenewstack.io/poorly-designed-rewards-crush-improvement-efforts/)，并且在衡量方面一直难以捉摸。

> “There is surely nothing quite so useless as doing with great efficiency what should not be done at all.” – Peter Drucker, 1963.

## 抛弃好的实践

在我们痴迷于生产力之前，软件行业发现了一些非常有价值的基础实践。其中之一就是重构。当你不断地重新审视你的代码，以保持组件的松散耦合，并确保你只定义一次概念时，你就可以构建更可靠的系统。如果它们因相同的原因而改变，你会将它们放在一起；如果它们有不同的变更驱动因素，你会将它们分开。

我的书架在 Kent Beck, Emily Bache, Martin Fowler, Robert C. Martin, Michael Feathers, Rebecca Parsons, Steve McConnell 等人编写的软件设计文献的重压下吱吱作响。这些书包含持久的技术和实践，对于长期成功的软件至关重要。编码助手不会改变软件开发的基础。

如果我们加快变化的速度，我们必须通过跟上软件的内部结构来匹配这一点。换句话说，为了使这成为一个成功的长期软件开发策略，我们必须能够以与更改代码相同的速度进行[重构](https://thenewstack.io/refactoring-is-not-bad-until-it-is/)。

但报告强调，目前情况并非如此。

重构活动是使用一种名为“移动代码”的变更类别来跟踪的。这是指基本逻辑保持不变，但已被改组以改进代码的设计。这包括经典的重构模式，如“提取方法”或“重命名变量”，这些模式通常由开发人员工具自动执行，以保证它们是安全的重构（更不用说测试驱动开发实践应该意味着你的测试会捕获任何意外的行为更改）。

自 2021 年以来，重构变更的比例已从 24% 骤降至 10% 以下。与此同时，复制/粘贴的代码行数（即重复）已从 10% 以下增加到近 15%。

![Code changes trend: The dramatic loss of refactoring and the climb of duplication. Image from Octopus Deploy. Data source: GitClear](https://cdn.thenewstack.io/media/2025/03/4988f93e-image2-1024x682.png)

*重构的急剧减少和重复的攀升。*

2025年的预测是，我们将达到重构消亡的临界点，重构所占的代码变更比例将仅略高于3%。我们的软件还会继续运行一段时间，之后这种影响才会变得明显。

## 亡羊补牢，为时已晚

我想起一个组织，我曾成功地用持续交付取代了一个混乱、脆弱的流程。安装的关键实践是测试自动化、部署自动化以及可靠的监控和警报系统。这些工具的结合大大提高了可靠性，并提升了开发人员和业务利益相关者之间的信任水平。

我离开后，团队认为管理测试数据是一项不受欢迎的任务。他们删除了在测试环境中运行的数据库脚本，该脚本用于将数据重置为已知状态。在许多个月里，集成测试仍然有效，如果没有人手动更改为集成测试配置的测试记录的测试数据，它们本可以继续工作。

一旦测试数据被破坏，团队面临着一个艰难的选择。他们可以重新创建测试数据管理脚本，对其进行更新，使其能够与他们所做的所有数据库更改一起工作。或者，他们可以删除失败的测试。在交付功能（并保持“高效”）的压力下，团队删除了测试。

删除测试没有直接影响。该功能在一段时间内继续工作，但最终引入了错误，然后成为一个反复出现的问题。

这就是当您选择生产力而不是长期可持续性时出现的问题。需要很长时间才能意识到存在损害。当过去的决定产生的影响显而易见时，通常为时已晚，无法减轻它。

## 飞行与坠落

AI 代码助手为抛物线式软件速度提供了完美的条件。就像零重力飞机飞行一样，它使用抛物线来提供失重感，代码助手让我们相信我们正在飞行，而实际上我们正在自由落体中遵循弹道轨迹。

为了让 AI 可持续地提高您的生产力，您不能让它决定您的代码质量。