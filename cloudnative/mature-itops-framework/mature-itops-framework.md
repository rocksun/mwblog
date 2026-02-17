<!--
title: 基础设施在演进，你的运营框架还在原地踏步吗？
cover: https://cdn.thenewstack.io/media/2026/02/fe8b20f7-getty-images-fna4hy84ioi-unsplash-scaled.jpg
summary: 随着服务中断日益频繁，ITOps需从被动转向主动。文章提出四步成熟运营框架：标准化工作流、融入持续学习与可观测性、加速AI与自动化解决，并部署AI代理。旨在提升运营弹性与信心。
-->

随着服务中断日益频繁，ITOps需从被动转向主动。文章提出四步成熟运营框架：标准化工作流、融入持续学习与可观测性、加速AI与自动化解决，并部署AI代理。旨在提升运营弹性与信心。

> 译自：[Your infrastructure is evolving, but is your operational framework still stuck in the past?](https://thenewstack.io/mature-itops-framework/)
> 
> 作者：Cristina Dias

主要服务中断变得越来越频繁、严重，解决时间也越来越长。根据[最新调查数据](https://apexassembly.com/wp-content/uploads/2025/06/State-of-Resilience-2025-Report-FINAL.pdf)，普通组织每年报告86次中断，每周总停机时间达324分钟。超过一半（55%）的组织每周经历中断，而14%的组织每天报告中断。

被动事件管理已不足以应对事件的增加，因此IT运维（[ITOps](https://thenewstack.io/five-ways-process-automation-can-streamline-itops/)）需要一次彻底的改造。需要一个成熟的运营框架，使人员、流程和技术围绕主动预防和补救措施保持一致。

> 组织总是希望简化流程和工作流，但他们通常不知道从何开始。

这个框架可以产生变革性的影响。然而，由于IT基础设施日益复杂、工具套件庞杂以及自动化程度有限，实现这种[运营成熟度](https://thenewstack.io/a-five-step-operational-maturity-model-for-benchmarking-your-team/)是困难的。组织总是希望简化流程和工作流，但他们通常不知道从何开始。

以下是ITOps团队可以采取的四个步骤，以创建成熟的框架，实现主动、弹性的运营：

## 步骤1：通过黄金路径和模板标准化工作流

随着组织在产品线、区域和客户方面进行扩展，保持一致的事件管理方法变得越来越困难。由于服务的构建、部署和支持方式多种多样，缺乏一致性会增加[认知负荷并减慢人工响应人员的响应时间](https://thenewstack.io/wp-admin/%view_link%)。

黄金路径通过提供预先批准、可重用的工作流来解决这一挑战，指导ITOps团队从A到B。这些路径定义了诸如服务部署、告警配置和事件响应等操作的组织最佳实践。黄金路径还有助于在不减慢交付速度的情况下强制执行安全性、合规性和可靠性要求。此外，它们消除了大型分布式团队对事件可能做出不同反应而导致响应碎片化的问题。

## 步骤2：将持续学习融入运营

运营成熟度需要持续学习的文化，并利用运营数据中的洞察力来减少重复事件。可观测性通过提供系统在生产环境中如何运行的可靠、端到端证据来支持这一学习循环。通过跨指标、日志和追踪的相关信号，团队可以更早地发现问题，更快地诊断根本原因，并识别事件周围的重复模式。

正是这些信号使得[无责事后审查](https://thenewstack.io/3-strategies-to-turn-incidents-into-learning-opportunities/)变得有效。借助数据，团队可以重现事件经过，理解促成因素，并将发现转化为对运行手册、工作流、交接和自动化的具体改进。随着时间的推移，这个循环会稳步提高基线弹性，而不是反复应对相同的事件。

## 步骤3：利用AI和自动化加速事件解决

AI和自动化是[成熟ITOps框架](https://thenewstack.io/wp-admin/%view_link%)的基本要素。

根据[PagerDuty数据](https://www.pagerduty.com/assets/infographic-6-proven-strategies-to-supercharge-innovation-velocity-with-PagerDuty.pdf)，采用自动化的组织报告在事件管理任务上花费的时间显著减少，压力和倦怠感也降低。自动化可以处理重复的、耗时的任务，例如日志记录、路由和信息丰富，从而使工程师能够专注于更高价值的操作。

成熟的团队还通过实施保障措施来设计系统以实现持续、安全的迭代，例如用于分阶段发布的功能标志和金丝雀部署，这些部署在全面发布之前将更改暴露给一小部分用户，从而在出现问题时更容易快速恢复。

AI驱动的工作流通过分析告警模式、提出可能的根本原因并支持分类决策，进一步[改进事件管理](https://thenewstack.io/wp-admin/%view_link%)。这些能力帮助团队更快地诊断问题，并减少局部问题演变为重大事件的可能性。

## 步骤4：在事件生命周期中部署AI代理

最后一步引入了AI代理。

AI代理将运营从基于规则的自动化提升到能够跨事件生命周期进行推理、行动和学习的系统。代理可以独立识别和分类问题、触发故障转移，并[补救已知的事件模式](https://thenewstack.io/wp-admin/%view_link%)。这些代理根据结果不断改进其行为，使工程师能够更快地响应，减少手动工作和值班疲劳。

AI代理不会取代现有的运营模式。它们以一种补充方式存在，使人类工程师能够专注于监督和改进，而不是重复性任务。

AI代理的采用已经开始。[研究表明，75%](https://www.pagerduty.com/resources/insights/learn/executives-adopting-ai-agents/)的组织正在运营中部署多个AI代理。实际示例包括[站点可靠性工程代理](https://thenewstack.io/practical-guidance-for-first-time-site-reliability-engineers/)，它们从先前的事件中学习，自动呈现相关上下文，并执行诊断和补救。

其他代理可以转录通话，在Teams或Slack中生成实时摘要和状态更新，自动检测并解决排班冲突，或者提出主动建议，以便ITOps团队可以提前预测问题。

## 建立运营弹性和信心

一个成熟的运营框架减少了现代运营两大支柱——速度和可靠性之间的权衡。当组织采纳成熟的ITOps框架时，团队可以自信地发布、测试和扩展软件，确信组织具备在不中断的情况下吸收变化的弹性和响应能力。