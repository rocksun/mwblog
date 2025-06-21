<!--
title: 开发者生产力的反指标时代
cover: https://cdn.thenewstack.io/media/2025/06/7f2a730c-metrics.png
summary: 别再卷“开发者生产力”指标啦！拥抱 AI 编码助手，关注 DevEx 和工作流自动化才是王道！告别技术债务，拥抱基于主干的开发、持续交付和 Monorepos。小审查和资产所有权也很重要！用 Aviator 重建 EngProd，提升软件开发生命周期效率！
-->

别再卷“开发者生产力”指标啦！拥抱 AI 编码助手，关注 DevEx 和工作流自动化才是王道！告别技术债务，拥抱基于主干的开发、持续交付和 Monorepos。小审查和资产所有权也很重要！用 Aviator 重建 EngProd，提升软件开发生命周期效率！

> 译自：[The Anti-Metrics Era of Developer Productivity](https://thenewstack.io/the-anti-metrics-era-of-developer-productivity/)
> 
> 作者：Ankit Jain

复杂的 [AI 编码助手](https://thenewstack.io/ai-coding-assistants-are-reshaping-engineering-not-replacing-engineers/) 的引入从根本上改变了开发人员的工作方式。曾经需要数小时集中输入和调试的工作，现在可以通过精心设计的提示和与 AI 工具的迭代协作在几分钟内完成。

今天的开发过程通常是这样的：

- 开发人员收集任务的需求。
- 开发人员提供上下文，并向 AI 助手提供清晰的逐步指导。
- AI 生成初始代码实现。
- 开发人员审查、编辑和完善 AI 生成的代码。
- 开发人员和 AI 迭代，直到解决方案达到最佳状态。

这种工作流程与传统的编码过程几乎没有相似之处，在传统编码过程中，开发人员手动编写每一行代码。最重要的技能已经从打字速度和语法记忆转变为问题 формулировка、解决方案评估以及与 AI 工具的有效协作。

## 技术界对衡量生产力的痴迷

老话说，你无法改进你无法衡量的东西。但是科技行业已经断章取义，变得痴迷于衡量“我们能衡量的一切”，尽管二十多年前，现代软件开发的架构师 [Martin Fowler](https://twitter.com/martinfowler) 写道 [开发者生产力无法衡量](https://martinfowler.com/bliki/CannotMeasureProductivity.html)。

[开发者生产力指标](https://thenewstack.io/developer-productivity-whos-tracking-it-not-many/) 对于了解工程过程中的瓶颈很有用，但它们不是目标。
指标仍然很重要。[DevOps Research and Assessment (DORA)](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) 是一套行业标准指标，用于 [衡量和比较 DevOps 性能](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/)，由 DORA 团队开发，这是一个由 Google Cloud 领导的倡议，旨在推广良好的 DevOps 实践。

但指标只是一盏识别工程过程中问题的指南针，[不是解决方案](https://www.aviator.co/blog/everything-wrong-with-dora-metrics/)。当然也不是衡量个人绩效的方法。

衡量一切的需求在 COVID 期间真正激增，当时我们开始远程工作，并且没有一个好的方法来了解工作是如何完成的。部分原因还在于管理层对理解软件工程中发生的事情感到不安。

然而，当被问及开发者生产力指标的有用性时，大多数 [领导者承认](https://www.atlassian.com/software/compass/resources/state-of-developer-2024) 他们跟踪的指标不能代表开发者生产力，并且倾向于将生产力与经验混为一谈。现在大部分代码都是由 AI 编写的，以相同的方式衡量生产力就更没有意义了。如果 AI 将编程工作量提高 30%，这是否意味着我们的生产力会提高 30%？”

## 什么扼杀了生产力？

开发人员也很清楚什么会让他们更有效率。[Atlassian 的开发者体验状态](https://www.atlassian.com/software/compass/resources/state-of-developer-2024) 报告显示，69% 的开发人员每周因效率低下而损失 8 小时，占他们时间的 20%。主要的摩擦点是技术债务 (59%)、缺乏文档 (41%)、构建过程 (27%)、缺乏深度工作时间 (27%) 和缺乏明确的方向 (25%)。

无论你称之为 DevEx 还是平台工程，缺乏摩擦就等于快乐的开发人员，也就等于高效的开发人员。在同一项调查中，63% 的开发人员表示开发者体验对他们的工作满意度很重要。

## 反指标方法：自动化工作流程

这就是为什么我坚信开发者生产力的反指标方法，并专注于消除开发人员每天面临的必要但单调的任务。
工程负责人不应该只关注漂亮的仪表板，而应该关注开发者体验和[整个软件开发生命周期的自动化工作流程](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-home&utm_term=net-new&utm_content=awareness)：[开发](https://www.aviator.co/stacked-prs?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-stackedprs&utm_term=net-new&utm_content=awareness)、[代码审查](https://www.aviator.co/flexreview?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-flexreview&utm_term=net-new&utm_content=awareness)、[构建](https://www.aviator.co/merge-queue?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-mergequeue&utm_term=net-new&utm_content=awareness)、测试和[部署](https://www.aviator.co/releases?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-releases&utm_term=net-new&utm_content=awareness)。

这意味着专注于解决实际的开发者问题，而不是仅仅指出问题。

跟踪工程生产力指标仍然很重要。然而，指标只是识别问题的指南针，而不是解决方案。对开发者体验的真正影响来自于平衡三个关键因素：人、实践和工具。

这些工具应该依赖于五个核心交付实践：

**基于主干的开发**

根据[这个定义](https://trunkbaseddevelopment.com/#one-line-summary)，基于主干的开发是“一种源代码控制分支模型，开发者在名为“主干”的单个分支上协作处理代码*，通过采用有据可查的技术来抵制创建其他长期存在的开发分支的任何压力。软件交付领域的奠基性著作《[Accelerate](https://www.oreilly.com/library/view/accelerate/9781457191435/)》研究并记录了“在主干/主版本上开发而不是在长期存在的功能分支上开发与更高的交付性能相关……与团队规模、组织规模或行业无关。”

**持续交付**

持续交付是一种实践，其中代码更改被自动构建、测试并准备发布到生产环境。这种方法使团队能够更频繁、更可靠地部署代码更改，这对于高性能工程组织至关重要。通过自动化交付管道，团队可以保持持续的更新流，同时确保质量和稳定性。正如[Bryan Finster](https://www.linkedin.com/in/bryan-finster/)，一位热情的[持续交付](https://minimumcd.org/)倡导者所说：持续交付是关于始终可交付，即能够在任何时候将最新的更改部署到生产环境的能力。通过自动化交付管道，团队可以保持持续的更新流，同时确保质量和稳定性。请注意，持续交付不同于持续部署，即使部署是手动触发或以预设的节奏进行，拥有持续交付也更为重要。

**Monorepos**

Monorepo 设置通过集中构建配置、linting 规则和开发工作流程，帮助在项目中建立一致的标准。这种标准化降低了开发者在项目之间移动的认知负担，并确保统一的质量控制。将所有代码放在一个地方还可以简化依赖管理和跨项目更改。

**小型审查**

小型、集中的代码审查有助于保持高质量的代码和开发者生产力。通过将更改分解为更小、更易于理解的部分，审查者可以提供更彻底的反馈并更早地发现潜在问题。这种方法还减少了审查者的认知负荷并加快了审查过程，从而加快了迭代周期。

**清晰准确的所有权**

开发者资产的通用所有权促进了团队中明确定义的共同责任和知识共享。当每个人都对代码库感到拥有所有权时，它会鼓励协作，减少知识孤岛，并确保任何团队成员都可以为项目的任何部分做出贡献。

虽然指标框架和仪表板在工程组织中仍然发挥作用，但如果我们真正关心开发者生产力，我们需要停止沉迷于仪表板，而开始关注真正帮助团队做好工作的事情。

作为一队前Google员工，我们开始寻找工具来替代Google的EngProd，一个专注于构建工具和基础设施以优化工程流程的团队。由于Google内部构建一切，并非所有东西都易于复制。这促使我们创建了[Aviator](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-1-aviator-home&utm_term=net-new&utm_content=awareness) — 在现代工程堆栈上重建Google的工程生产力（EngProd），以解决从代码审查到构建、测试、合并和部署的开发过程的每个阶段的协作挑战。